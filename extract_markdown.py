#!/usr/bin/env python3
"""
Extract Wilmott forum thread from raw HTML files into individual Markdown pages.

Usage: python extract_markdown.py
Output: ./thread_page/page_001.md, page_002.md, etc. + index.md
"""

from __future__ import annotations

import html
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Final
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel, field_validator

from latex_translator import translate, Ok, Err

# Constants
RAW_DIR: Final[Path] = Path("./raw")
OUTPUT_DIR: Final[Path] = Path("./thread_page")

# Track translation errors during processing
translation_errors: list[tuple[int, str, str, str]] = []  # (post_number, error, snippet, full_content)
SCRAPE_DATE: Final[datetime] = datetime(2026, 1, 20)
LINE_WIDTH: Final[int] = 120
POSTS_PER_PAGE: Final[int] = 50
THREAD_TITLE: Final[str] = "Breakthrough in the theory of stochastic differential equations and their simulation"
IMAGES_DIR: Final[Path] = Path("./images")


def url_to_local_path(url: str) -> tuple[str, str] | None:
    """
    Convert an image URL to local paths.
    Returns (disk_path, markdown_path) or None if URL should not be converted.
    - disk_path: for checking if file exists (relative to script working dir)
    - markdown_path: for use in markdown (relative to thread_page/ directory)
    """
    # Skip forum attachments
    if "download/file.php" in url:
        return None

    # Skip non-image URLs
    if not any(ext in url.lower() for ext in [".jpg", ".jpeg", ".png", ".webp"]):
        return None

    # Parse the URL to extract host and path
    if url.startswith("//"):
        url = "https:" + url

    if not url.startswith(("http://", "https://")):
        return None

    # Extract host and path
    parsed = urlparse(url)
    host = parsed.netloc
    path = parsed.path

    # disk_path: for checking existence from script's working directory
    disk_path = f"./images/{host}{path}"
    # markdown_path: for use in markdown files (which are in thread_page/)
    markdown_path = f"../images/{host}{path}"
    return disk_path, markdown_path


class Post(BaseModel):
    """Represents a single forum post with validated fields."""

    post_number: int
    post_id: str
    author: str
    is_topic_author: bool
    timestamp: datetime
    content: str

    @field_validator("post_number")
    @classmethod
    def post_number_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError(f"post_number must be positive, got {v}")
        return v

    @field_validator("post_id")
    @classmethod
    def post_id_must_be_valid(cls, v: str) -> str:
        if not v.startswith("p") or not v[1:].isdigit():
            raise ValueError(f"post_id must be 'p' followed by digits, got {v}")
        return v

    @field_validator("author")
    @classmethod
    def author_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("author must not be empty")
        return v.strip()

    @field_validator("content")
    @classmethod
    def content_must_not_be_empty(cls, v: str) -> str:
        # Allow empty content for deleted/moderated posts
        if not v.strip():
            return "[This post has been deleted or contains no text content]"
        return v


def parse_timestamp(timestamp_str: str) -> datetime:
    """
    Parse a timestamp string into a datetime object.
    Handles both absolute dates and relative dates (Today, Yesterday).
    """
    timestamp_str = timestamp_str.strip()

    # Handle relative dates
    if timestamp_str.startswith("Today,"):
        time_part = timestamp_str.replace("Today,", "").strip()
        time_obj = datetime.strptime(time_part, "%I:%M %p")
        return SCRAPE_DATE.replace(
            hour=time_obj.hour,
            minute=time_obj.minute,
            second=0,
            microsecond=0
        )

    if timestamp_str.startswith("Yesterday,"):
        time_part = timestamp_str.replace("Yesterday,", "").strip()
        time_obj = datetime.strptime(time_part, "%I:%M %p")
        yesterday = SCRAPE_DATE.replace(day=SCRAPE_DATE.day - 1)
        return yesterday.replace(
            hour=time_obj.hour,
            minute=time_obj.minute,
            second=0,
            microsecond=0
        )

    # Handle absolute dates like "April 17th, 2016, 12:24 pm"
    # Remove ordinal suffixes (st, nd, rd, th)
    cleaned = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", timestamp_str)
    return datetime.strptime(cleaned, "%B %d, %Y, %I:%M %p")


def extract_post_number(post_div: Tag) -> int:
    """Extract post number from a post div."""
    # Look for the post number link like "#2911"
    post_link = post_div.select_one("a.icon_post_target")
    if post_link:
        text = post_link.get_text(strip=True)
        if text.startswith("#"):
            return int(text[1:])
    raise ValueError("Could not find post number")


def extract_post_id(post_div: Tag) -> str:
    """Extract post ID from a post div."""
    anchor = post_div.select_one("a.st-anchor")
    if anchor:
        post_id = anchor.get("id")
        if isinstance(post_id, str):
            return post_id
    raise ValueError("Could not find post ID")


def extract_author(post_div: Tag) -> tuple[str, bool]:
    """Extract author name and whether they are the topic author."""
    username_link = post_div.select_one("a.username")
    if not username_link:
        raise ValueError("Could not find username")

    author = username_link.get_text(strip=True)
    is_topic_author = post_div.select_one(".topic-author-label") is not None

    return author, is_topic_author


def extract_timestamp(post_div: Tag) -> datetime:
    """Extract and parse the post timestamp."""
    # The post timestamp is in p.author > span.timestamp
    author_p = post_div.select_one("p.author")
    if author_p:
        timestamp_span = author_p.select_one("span.timestamp")
        if timestamp_span:
            return parse_timestamp(timestamp_span.get_text(strip=True))
    raise ValueError("Could not find timestamp")


def html_to_markdown(content_div: Tag) -> str:
    """
    Convert HTML content to Markdown.
    Handles common HTML elements and preserves LaTeX.
    """
    # Work with a copy to avoid modifying the original
    content_html = str(content_div)

    # Decode HTML entities first
    content_html = html.unescape(content_html)

    # Convert code blocks: <pre><code class="prettyprint">...</code></pre> -> fenced code
    # Must happen BEFORE HTML stripping to protect < and > in code
    def convert_pre_code_block(match: re.Match[str]) -> str:
        code = match.group(1)
        # Strip any remaining HTML tags inside the code block
        code = re.sub(r'<[^>]+>', '', code)
        # Escape < and > as HTML entities to protect from later HTML stripping
        # We'll unescape them after all HTML processing
        code = code.replace("<", "&lt;").replace(">", "&gt;")
        return f"\n```\nCODE_BLOCK_START{code}CODE_BLOCK_END\n```\n"

    content_html = re.sub(
        r'<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>',
        convert_pre_code_block,
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Also handle the codebox header pattern (remove it, the code block is already converted)
    content_html = re.sub(
        r'<div class="codebox">.*?<div class="codebox__header">.*?</div>',
        '',
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Convert images: <img src="url" alt="text"> -> ![text](local_path or url)
    def replace_image(match: re.Match[str]) -> str:
        attrs = match.group(1)
        src_match = re.search(r'src=["\']([^"\']+)["\']', attrs)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', attrs)
        if src_match:
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else "Image"

            # Try to use local path if image was downloaded
            paths = url_to_local_path(src)
            if paths:
                disk_path, markdown_path = paths
                if Path(disk_path).exists():
                    return f"![{alt}]({markdown_path})"
            # Fall back to original URL
            return f"![{alt}]({src})"
        return ""

    content_html = re.sub(
        r'<img\s+([^>]+)/?>',
        replace_image,
        content_html,
        flags=re.IGNORECASE
    )

    # Convert YouTube embeds: <iframe ... data-youtube-id="XXX" ...> -> [YouTube Video](url)
    def replace_youtube(match: re.Match[str]) -> str:
        attrs = match.group(1)
        yt_id_match = re.search(r'data-youtube-id=["\']([^"\']+)["\']', attrs)
        src_match = re.search(r'src=["\']([^"\']+)["\']', attrs)
        if yt_id_match:
            return f"[YouTube Video](https://www.youtube.com/watch?v={yt_id_match.group(1)})"
        elif src_match and "youtube" in src_match.group(1):
            return f"[YouTube Video]({src_match.group(1)})"
        return "[Embedded Video]"

    content_html = re.sub(
        r'<iframe\s+([^>]+)>[^<]*</iframe>',
        replace_youtube,
        content_html,
        flags=re.IGNORECASE
    )

    # Convert <br> and <br/> to newlines
    content_html = re.sub(r"<br\s*/?>", "\n", content_html, flags=re.IGNORECASE)

    # Convert links: <a href="url">text</a> -> [text](url)
    def replace_link(match: re.Match[str]) -> str:
        url = match.group(1)
        text = match.group(2)
        # Strip any HTML tags from text
        text = re.sub(r"<[^>]+>", "", text)
        if text.strip() == url.strip():
            # If text is same as URL, just use bare URL
            return url
        return f"[{text}]({url})"

    content_html = re.sub(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
        replace_link,
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Convert <b> and <strong> to **bold**
    content_html = re.sub(
        r"<(?:b|strong)>(.*?)</(?:b|strong)>",
        r"**\1**",
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Convert <i> and <em> to *italic*
    content_html = re.sub(
        r"<(?:i|em)>(.*?)</(?:i|em)>",
        r"*\1*",
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Convert <code> to `code`
    content_html = re.sub(
        r"<code>(.*?)</code>",
        r"`\1`",
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Convert blockquotes
    content_html = re.sub(
        r"<blockquote[^>]*>(.*?)</blockquote>",
        lambda m: "\n".join(f"> {line}" for line in m.group(1).strip().split("\n")),
        content_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Remove remaining HTML tags
    content_html = re.sub(r"<[^>]+>", "", content_html)

    # Restore < and > in code blocks (they were protected with &lt; &gt; markers)
    def restore_code_block(match: re.Match[str]) -> str:
        code = match.group(1)
        code = code.replace("&lt;", "<").replace("&gt;", ">")
        return code

    content_html = re.sub(
        r'CODE_BLOCK_START(.*?)CODE_BLOCK_END',
        restore_code_block,
        content_html,
        flags=re.DOTALL
    )

    # Run content through the LaTeX translator module
    # This handles: \sqrt() -> \sqrt{}, \text{$...$}, delimiters, emoji, etc.
    result = translate(content_html)
    match result:
        case Ok(value):
            content_html = value
        case Err(error, original):
            # Record error with full content for logging
            snippet = original[:80].replace('\n', ' ')
            translation_errors.append((0, error, snippet, original))  # post_number filled later
            # Wrap in code block to contain the broken delimiters (code blocks don't render math)
            content_html = f"**(broken latex: {error})**\n\n```latex\n{original}\n```"

    # Clean up excessive whitespace while preserving paragraph breaks
    lines = content_html.split("\n")
    cleaned_lines: list[str] = []
    for line in lines:
        # Strip trailing whitespace but preserve leading whitespace for code/math
        cleaned_lines.append(line.rstrip())

    # Join and normalize multiple blank lines to max 2
    content = "\n".join(cleaned_lines)
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip()


def hard_wrap_text(text: str, width: int = LINE_WIDTH) -> str:
    """
    Hard wrap text at specified width while preserving:
    - Math blocks ($$...$$)
    - Inline math ($...$)
    - URLs
    - Code blocks
    """

    def wrap_line_with_math(line: str) -> list[str]:
        """Wrap a line that contains inline math, preserving $...$ blocks."""
        # Split line into segments: text and math alternating
        # Use regex to find all $...$ blocks (non-greedy)
        segments: list[tuple[str, bool]] = []  # (content, is_math)
        last_end = 0

        for match in re.finditer(r'\$[^$]+\$', line):
            # Text before this math
            if match.start() > last_end:
                segments.append((line[last_end:match.start()], False))
            # The math block
            segments.append((match.group(), True))
            last_end = match.end()

        # Remaining text after last math
        if last_end < len(line):
            segments.append((line[last_end:], False))

        if not segments:
            return [line]

        # Now wrap: accumulate segments into lines, wrapping text segments
        result_lines: list[str] = []
        current_line = ""

        for segment, is_math in segments:
            if is_math:
                # Math block - don't break it
                if len(current_line) + len(segment) > width and current_line:
                    # Start new line before math if it would exceed width
                    result_lines.append(current_line.rstrip())
                    current_line = segment
                else:
                    current_line += segment
            else:
                # Text segment - can be wrapped
                words = segment.split()
                for word in words:
                    if not current_line:
                        current_line = word
                    elif len(current_line) + 1 + len(word) <= width:
                        current_line += " " + word
                    else:
                        result_lines.append(current_line.rstrip())
                        current_line = word

        if current_line:
            result_lines.append(current_line.rstrip())

        return result_lines if result_lines else [line]

    lines = text.split("\n")
    wrapped_lines: list[str] = []
    in_math_block = False

    for line in lines:
        # Track multi-line display math blocks ($$...$$ spanning multiple lines)
        # Only toggle state if line is JUST $$ by itself
        stripped = line.strip()
        if stripped == "$$":
            in_math_block = not in_math_block
            wrapped_lines.append(line)
            continue

        # Don't wrap lines inside multi-line math blocks
        if in_math_block:
            wrapped_lines.append(line)
            continue

        # Don't wrap empty lines
        if not line.strip():
            wrapped_lines.append(line)
            continue

        # Short lines don't need wrapping
        if len(line) <= width:
            wrapped_lines.append(line)
            continue

        # Lines with URLs - don't wrap (URLs can be long)
        if "http://" in line or "https://" in line:
            wrapped_lines.append(line)
            continue

        # Lines with any math ($ or $$) need special handling to preserve math blocks
        if "$" in line:
            wrapped_lines.extend(wrap_line_with_math(line))
            continue

        # Standard wrapping for plain text
        wrapped = textwrap.fill(
            line,
            width=width,
            break_long_words=False,
            break_on_hyphens=False
        )
        wrapped_lines.extend(wrapped.split("\n"))

    return "\n".join(wrapped_lines)


def extract_posts_from_html(html_content: str) -> list[Post]:
    """Extract all posts from an HTML page."""
    soup = BeautifulSoup(html_content, "lxml")
    posts: list[Post] = []

    post_divs = soup.select("div.post.has-profile")

    for post_div in post_divs:
        try:
            post_number = extract_post_number(post_div)
            post_id = extract_post_id(post_div)
            author, is_topic_author = extract_author(post_div)
            timestamp = extract_timestamp(post_div)

            content_div = post_div.select_one("div.content")
            if not content_div:
                raise ValueError("Could not find content div")

            content = html_to_markdown(content_div)
            content = hard_wrap_text(content)

            post = Post(
                post_number=post_number,
                post_id=post_id,
                author=author,
                is_topic_author=is_topic_author,
                timestamp=timestamp,
                content=content
            )
            posts.append(post)

        except Exception as e:
            print(f"Warning: Failed to parse post: {e}", file=sys.stderr)
            continue

    return posts


def format_post_as_markdown(post: Post) -> str:
    """Format a single post as Markdown."""
    author_suffix = " (Topic Author)" if post.is_topic_author else ""
    timestamp_str = post.timestamp.strftime("%B %d, %Y, %I:%M %p").replace(" 0", " ")

    return f"""### #{post.post_number} — {post.author}{author_suffix}
*{timestamp_str}*

{post.content}"""


def load_all_posts() -> list[Post]:
    """Load and parse all posts from raw HTML files."""
    all_posts: list[Post] = []

    # Get all raw HTML files, sorted by start offset
    html_files = sorted(RAW_DIR.glob("page_start_*.html"))

    if not html_files:
        raise RuntimeError(f"No HTML files found in {RAW_DIR}")

    print(f"Loading {len(html_files)} HTML files...")

    for html_file in html_files:
        html_content = html_file.read_text(encoding="utf-8")
        posts = extract_posts_from_html(html_content)
        all_posts.extend(posts)
        print(f"  {html_file.name}: {len(posts)} posts")

    return all_posts


def deduplicate_and_sort(posts: list[Post]) -> list[Post]:
    """Remove duplicate posts and sort by post number."""
    seen_numbers: set[int] = set()
    unique_posts: list[Post] = []

    for post in posts:
        if post.post_number not in seen_numbers:
            seen_numbers.add(post.post_number)
            unique_posts.append(post)

    return sorted(unique_posts, key=lambda p: p.post_number)


def chunk_posts(posts: list[Post], chunk_size: int) -> list[list[Post]]:
    """Split posts into chunks of specified size."""
    chunks: list[list[Post]] = []
    for i in range(0, len(posts), chunk_size):
        chunks.append(posts[i:i + chunk_size])
    return chunks


def assemble_page(
    posts: list[Post],
    page_num: int,
    total_pages: int,
    total_posts: int,
    date_range: tuple[datetime, datetime],
) -> str:
    """Assemble a single page of posts into Markdown."""
    first_post = posts[0].post_number
    last_post = posts[-1].post_number

    # Navigation links
    nav_parts: list[str] = []
    if page_num > 1:
        nav_parts.append(f"[← Previous](page_{page_num - 1:03d}.md)")
    nav_parts.append(f"[Index](index.md)")
    if page_num < total_pages:
        nav_parts.append(f"[Next →](page_{page_num + 1:03d}.md)")

    nav_line = " | ".join(nav_parts)

    header = f"""# {THREAD_TITLE}

**Page {page_num} of {total_pages}** — Posts #{first_post}–#{last_post}

{nav_line}

---

"""

    post_texts = [format_post_as_markdown(post) for post in posts]
    body = "\n\n---\n\n".join(post_texts)

    footer = f"""

---

{nav_line}
"""

    return header + body + footer


def assemble_index(
    posts: list[Post],
    total_pages: int,
    chunks: list[list[Post]],
) -> str:
    """Assemble the index page with links to all pages."""
    date_range_str = (
        f"{posts[0].timestamp.strftime('%B %d, %Y')} — "
        f"{posts[-1].timestamp.strftime('%B %d, %Y')}"
    )

    header = f"""# {THREAD_TITLE}

**Forum:** Wilmott Technical Forum
**Total Posts:** {len(posts)}
**Date Range:** {date_range_str}
**Pages:** {total_pages}

---

## Pages

"""

    page_links: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        first = chunk[0].post_number
        last = chunk[-1].post_number
        first_date = chunk[0].timestamp.strftime("%b %d, %Y")
        page_links.append(f"- [Page {i}](page_{i:03d}.md) — Posts #{first}–#{last} ({first_date})")

    return header + "\n".join(page_links) + "\n"


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_posts(posts: list[Post]) -> None:
    """
    Validate the list of posts. Raises ValidationError if any check fails.
    """
    errors: list[str] = []

    # Check 1: Post count
    if len(posts) == 0:
        errors.append("No posts found")
        raise ValidationError("Post validation failed:\n" + "\n".join(f"  - {e}" for e in errors))

    # Check 2: Post numbers form a sequence from 1 to max with allowed gaps (deleted posts)
    max_post_number = max(p.post_number for p in posts)
    min_post_number = min(p.post_number for p in posts)

    if min_post_number != 1:
        errors.append(f"First post number should be 1, got {min_post_number}")

    expected_numbers = set(range(1, max_post_number + 1))
    actual_numbers = {p.post_number for p in posts}

    missing = expected_numbers - actual_numbers
    if missing:
        # Gaps are allowed (deleted posts) - just warn
        print(f"Note: {len(missing)} missing post numbers (likely deleted): {sorted(missing)}")

    extra = actual_numbers - expected_numbers
    if extra:
        errors.append(f"Post numbers outside expected range: {sorted(extra)[:20]}")

    # Check 3: Post numbers match their position (after sorting)
    for i, post in enumerate(posts):
        expected_num = i + 1
        if post.post_number != expected_num:
            # This is a gap - track it but don't fail
            pass

    # Check 4: Timestamps are monotonically increasing (with some tolerance for same-minute posts)
    prev_timestamp: datetime | None = None
    timestamp_violations: list[tuple[int, datetime, datetime]] = []

    for post in posts:
        if prev_timestamp is not None:
            if post.timestamp < prev_timestamp:
                timestamp_violations.append((post.post_number, prev_timestamp, post.timestamp))
        prev_timestamp = post.timestamp

    if timestamp_violations:
        errors.append(
            f"Timestamps not monotonic: {len(timestamp_violations)} violations. "
            f"First: post #{timestamp_violations[0][0]}"
        )

    if errors:
        raise ValidationError("Post validation failed:\n" + "\n".join(f"  - {e}" for e in errors))

    print(f"✓ Post validation passed: {len(posts)} posts")


def validate_markdown(content: str) -> None:
    """
    Validate the generated Markdown content. Raises ValidationError if any check fails.
    Some checks are warnings only (original data issues).
    """
    errors: list[str] = []
    warnings: list[str] = []

    # Check 1: Math delimiters are balanced (WARNING - original data may have issues)
    # Count $$ (display math)
    display_math_count = content.count("$$")
    if display_math_count % 2 != 0:
        warnings.append(f"Unbalanced $$ delimiters: {display_math_count} found (should be even)")

    # Count $ (but not $$) for inline math
    # This is tricky - we need to exclude $$ from the count
    temp_content = content.replace("$$", "DOUBLEDOLLAR")
    inline_math_count = temp_content.count("$")
    if inline_math_count % 2 != 0:
        warnings.append(f"Unbalanced $ delimiters: {inline_math_count} found (should be even)")

    # Check 2: No HTML remnants (ERROR - these should be converted)
    html_patterns = [
        (r"<br\s*/?>", "<br> tags"),
        (r"<div", "<div> tags"),
        (r"<span", "<span> tags"),
        (r"<p>", "<p> tags"),
        (r"&amp;", "&amp; entities"),
        (r"&lt;", "&lt; entities"),
        (r"&gt;", "&gt; entities"),
        (r"&nbsp;", "&nbsp; entities"),
    ]

    for pattern, description in html_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"Found {len(matches)} {description}")

    # Check 3: KaTeX-breaking patterns (ERROR - these will cause parse failures)
    katex_breaking_patterns = [
        # \text{$...} - nested $ inside \text{} breaks KaTeX delimiter parsing
        (r'\\text\{\$', "\\text{$ patterns (nested math in text)"),
        # Unconverted forum delimiters
        (r'\[\$\]', "[$] unconverted forum math delimiters"),
        (r'\[\$/\]', "[$/] unconverted forum math delimiters"),
        (r'\[/\$\]', "[/$] unconverted forum math delimiters"),
    ]

    for pattern, description in katex_breaking_patterns:
        matches = re.findall(pattern, content)
        if matches:
            errors.append(f"Found {len(matches)} {description}")

    # Check 4: Line lengths
    # - Lines > 2000 chars without URLs/math are ERROR (wrapping clearly failed)
    # - Lines > 500 chars without URLs/math are WARNING (could be code blocks)
    # - Lines > 120 chars are WARNING (acceptable for math/code)
    lines = content.split("\n")
    long_lines: list[tuple[int, int]] = []
    very_long_lines: list[tuple[int, int]] = []  # >2000 = ERROR
    moderately_long_lines: list[tuple[int, int]] = []  # >500 = WARNING
    in_math_block = False

    for i, line in enumerate(lines, 1):
        # Track standalone $$ lines for multi-line math
        if line.strip() == "$$":
            in_math_block = not in_math_block
            continue

        if in_math_block:
            continue

        has_url = "http://" in line or "https://" in line
        has_math = "$" in line

        # Extremely long lines (>10000) without URLs/math are errors - clearly prose that failed to wrap
        if len(line) > 10000 and not has_url and not has_math:
            very_long_lines.append((i, len(line)))
        # Moderately long lines (>500) could be code blocks - warning only
        elif len(line) > 500 and not has_url and not has_math:
            moderately_long_lines.append((i, len(line)))

        if "http://" in line or "https://" in line:
            continue

        # Allow some tolerance for lines with inline math
        if "$" in line:
            continue

        if len(line) > LINE_WIDTH:
            long_lines.append((i, len(line)))

    if very_long_lines:
        errors.append(
            f"Found {len(very_long_lines)} lines >10000 chars (wrapping failed). "
            f"First: line {very_long_lines[0][0]} ({very_long_lines[0][1]} chars)"
        )

    if moderately_long_lines:
        warnings.append(
            f"Found {len(moderately_long_lines)} lines >500 chars (likely code blocks). "
            f"First: line {moderately_long_lines[0][0]} ({moderately_long_lines[0][1]} chars)"
        )

    if long_lines:
        warnings.append(
            f"Found {len(long_lines)} lines exceeding {LINE_WIDTH} chars. "
            f"First: line {long_lines[0][0]} ({long_lines[0][1]} chars)"
        )

    # Print warnings
    for warning in warnings:
        print(f"⚠ Warning: {warning}")

    if errors:
        raise ValidationError("Markdown validation failed:\n" + "\n".join(f"  - {e}" for e in errors))

    print(f"✓ Markdown validation passed ({len(warnings)} warnings)")


def main() -> int:
    """Main entry point."""
    # Clear any previous errors
    translation_errors.clear()

    print("=" * 60)
    print("Wilmott Thread Markdown Extractor")
    print("=" * 60)
    print()

    # Step 1: Load all posts
    try:
        all_posts = load_all_posts()
    except Exception as e:
        print(f"ERROR: Failed to load posts: {e}", file=sys.stderr)
        return 1

    print(f"\nLoaded {len(all_posts)} total posts")

    # Step 2: Deduplicate and sort
    posts = deduplicate_and_sort(all_posts)
    print(f"After deduplication: {len(posts)} unique posts")

    # Step 3: Validate posts
    print("\nValidating posts...")
    try:
        validate_posts(posts)
    except ValidationError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # Step 4: Split into chunks
    chunks = chunk_posts(posts, POSTS_PER_PAGE)
    total_pages = len(chunks)
    print(f"\nSplitting into {total_pages} pages ({POSTS_PER_PAGE} posts per page)")

    # Step 5: Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 6: Assemble and write pages
    print("\nAssembling and writing pages...")
    date_range = (posts[0].timestamp, posts[-1].timestamp)
    total_chars = 0

    for i, chunk in enumerate(chunks, 1):
        page_content = assemble_page(
            posts=chunk,
            page_num=i,
            total_pages=total_pages,
            total_posts=len(posts),
            date_range=date_range,
        )

        # Validate each page
        try:
            validate_markdown(page_content)
        except ValidationError as e:
            print(f"ERROR on page {i}: {e}", file=sys.stderr)
            return 1

        page_file = OUTPUT_DIR / f"page_{i:03d}.md"
        page_file.write_text(page_content, encoding="utf-8")
        total_chars += len(page_content)
        print(f"  {page_file.name}: {len(chunk)} posts, {len(page_content):,} chars")

    # Step 7: Write index
    print("\nWriting index...")
    index_content = assemble_index(posts, total_pages, chunks)
    index_file = OUTPUT_DIR / "index.md"
    index_file.write_text(index_content, encoding="utf-8")

    print()
    print("=" * 60)
    print(f"Done! Output: {OUTPUT_DIR}/")
    print(f"  - {total_pages} page files")
    print(f"  - 1 index file")
    print(f"  - Total: {total_chars:,} characters")

    # Report and log translation errors
    if translation_errors:
        print()
        print(f"LaTeX translation errors: {len(translation_errors)}")
        # Group by error type
        by_type: dict[str, int] = {}
        for _, error, _, _ in translation_errors:
            by_type[error] = by_type.get(error, 0) + 1
        for error, count in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  - {error}: {count}")

        # Write broken-latex.md for manual review
        broken_file = OUTPUT_DIR / "broken-latex.md"
        with broken_file.open("w", encoding="utf-8") as f:
            f.write("# Broken LaTeX Posts\n\n")
            f.write(f"Total: {len(translation_errors)} posts with errors\n\n")
            f.write("---\n\n")
            for i, (_, error, snippet, full_content) in enumerate(translation_errors, 1):
                f.write(f"## Error {i}: {error}\n\n")
                f.write(f"**Snippet:** `{snippet}`\n\n")
                f.write("**Full content:**\n\n")
                f.write("```\n")
                f.write(full_content)
                f.write("\n```\n\n")
                f.write("---\n\n")
        print(f"  Logged to: {broken_file}")
    else:
        print()
        print("LaTeX translation: 0 errors")

    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
