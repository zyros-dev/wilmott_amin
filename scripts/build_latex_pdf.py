#!/usr/bin/env python3
"""
Build PDF directly via LaTeX from Wilmott thread markdown.
Target: <8MB for Discord upload.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
from PIL import Image

# Configuration
MAX_IMAGE_DIM = 400
JPEG_QUALITY = 55
BUILD_DIR = Path("/tmp/wilmott_latex_build")
IMAGES_SRC = Path("./images")
THREAD_DIR = Path("./thread_page")
OUTPUT_PDF = Path("./wilmott_thread.pdf")

LATEX_HEADER = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[margin=0.75in]{geometry}
\usepackage{graphicx}
\usepackage{amsmath,amssymb}
\usepackage{fancyvrb}
\usepackage{listings}
\lstset{basicstyle=\ttfamily\small,breaklines=true,breakatwhitespace=true}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{parskip}
\usepackage{titlesec}

% Compact section formatting
\titleformat{\section}{\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{1em}{}
\titlespacing*{\section}{0pt}{2ex}{1ex}
\titlespacing*{\subsection}{0pt}{1.5ex}{0.5ex}

% Allow line breaks in URLs
\usepackage{url}
\urlstyle{same}

\title{Breakthrough in the Theory of Stochastic Differential Equations and Their Simulation}
\author{Wilmott Forum Thread Archive}
\date{}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

LATEX_FOOTER = r"""
\end{document}
"""

def compress_images():
    """Compress all images to BUILD_DIR/images/"""
    print("Compressing images...")
    dest_dir = BUILD_DIR / "images"
    dest_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    total_original = 0
    total_compressed = 0

    for src_path in IMAGES_SRC.rglob("*"):
        if not src_path.is_file():
            continue
        if src_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
            continue

        rel_path = src_path.relative_to(IMAGES_SRC)
        dest_path = dest_dir / rel_path.with_suffix(".jpg")
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            total_original += src_path.stat().st_size

            with Image.open(src_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                elif img.mode != "RGB":
                    img = img.convert("RGB")

                w, h = img.size
                if max(w, h) > MAX_IMAGE_DIM:
                    ratio = MAX_IMAGE_DIM / max(w, h)
                    new_size = (int(w * ratio), int(h * ratio))
                    img = img.resize(new_size, Image.LANCZOS)

                img.save(dest_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
                total_compressed += dest_path.stat().st_size

            count += 1
            if count % 100 == 0:
                print(f"  Processed {count} images...")
        except Exception as e:
            pass  # Skip problematic images silently

    print(f"  Compressed {count} images: {total_original/1024/1024:.1f}MB -> {total_compressed/1024/1024:.1f}MB")
    return dest_dir


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in plain text."""
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    return text


def sanitize_math(line: str, in_display_math: bool) -> tuple[str, bool]:
    """Keep math as-is when balanced, escape when not."""
    stripped = line.strip()

    # Track display math state
    if stripped.startswith('$$'):
        if stripped.endswith('$$') and len(stripped) > 4:
            return line, in_display_math  # Complete on one line
        elif stripped == '$$':
            return line, not in_display_math  # Toggle
        else:
            return line, True  # Opening

    if stripped.endswith('$$') and in_display_math:
        return line, False  # Closing

    if in_display_math:
        return line, True  # Inside display math

    # Check balance for regular lines
    temp = line.replace(r'\$', '')
    temp = temp.replace('$$', '')
    if temp.count('$') % 2 == 0:
        return line, False

    # Unbalanced - escape
    return line.replace('$', r'\$'), False


def markdown_to_latex(content: str, images_dir: Path) -> str:
    """Convert markdown content to LaTeX."""
    lines = content.split('\n')
    output = []
    in_code_block = False
    in_blockquote = False
    in_display_math = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                output.append(r'\end{lstlisting}')
                in_code_block = False
            else:
                output.append(r'\begin{lstlisting}')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            output.append(line)
            i += 1
            continue

        # Skip empty lines
        if not line.strip():
            output.append('')
            i += 1
            continue

        # Page/navigation lines to skip
        if line.startswith('[← Previous]') or line.startswith('[Next →]') or line.startswith('[Index]'):
            i += 1
            continue

        # Horizontal rules
        if line.strip() == '---':
            output.append(r'\vspace{1em}\hrule\vspace{1em}')
            i += 1
            continue

        # Main title (skip, we have it in header)
        if line.startswith('# Breakthrough'):
            i += 1
            continue

        # Page headers
        if line.startswith('**Page '):
            i += 1
            continue

        # Post headers: ### #123 — Author
        if line.startswith('### #'):
            match = re.match(r'### #(\d+) — (.+)', line)
            if match:
                post_num = match.group(1)
                author = match.group(2)
                author = escape_latex(author)
                output.append(f'\\subsection*{{\\#{post_num} — {author}}}')
            i += 1
            continue

        # Timestamp lines: *April 20, 2016, 1:32 PM*
        if line.startswith('*') and line.endswith('*') and ',' in line and not line.startswith('**'):
            timestamp = line[1:-1]
            output.append(f'\\textit{{{timestamp}}}\\\\')
            i += 1
            continue

        # Blockquotes
        if line.startswith('> '):
            if not in_blockquote:
                output.append(r'\begin{quote}')
                in_blockquote = True
            quote_text = line[2:]
            quote_text = process_inline(quote_text, images_dir)
            output.append(quote_text)
            i += 1
            continue
        elif in_blockquote:
            output.append(r'\end{quote}')
            in_blockquote = False

        # Handle broken latex markers - convert to proper LaTeX
        if '(broken latex:' in line:
            # Convert **text** to \textbf{text} and escape $ signs
            line = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', line)
            line = line.replace('$$', 'DISPLAY-MATH')
            line = line.replace('$', r'\$')
            line = line.replace('DISPLAY-MATH', 'DISPLAY-MATH')  # Keep as text
            output.append(line)
            i += 1
            continue

        # Regular line - sanitize math and process inline elements
        line, in_display_math = sanitize_math(line, in_display_math)
        processed = process_inline(line, images_dir)
        output.append(processed)
        i += 1

    # Close any open environments
    if in_code_block:
        output.append(r'\end{lstlisting}')
    if in_blockquote:
        output.append(r'\end{quote}')

    return '\n'.join(output)


def process_inline(line: str, images_dir: Path) -> str:
    """Process inline markdown elements."""

    # Images: ![alt](path) -> \includegraphics
    def replace_image(match):
        alt = match.group(1)
        path = match.group(2)

        # Handle linked images: [![alt](img)](url)
        if path.startswith('[!['):
            return f'[Image: {alt}]'

        # Skip external URLs
        if path.startswith(('http://', 'https://')):
            return f'[Image: {alt}]'

        # Convert path
        if path.startswith('../images/'):
            rel = path[len('../images/'):]
            rel = re.sub(r'\.(png|jpeg|webp)$', '.jpg', rel, flags=re.IGNORECASE)
            new_path = images_dir / rel
            if new_path.exists():
                # Escape path for LaTeX
                latex_path = str(new_path).replace('_', r'\_')
                return f'\\includegraphics[width=0.8\\textwidth]{{{new_path}}}'

        return f'[Image: {alt}]'

    # Process images first (before other processing might break the syntax)
    line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image, line)

    # Also handle linked images [![...](img)](link)
    line = re.sub(r'\[!\[([^\]]*)\]\([^)]+\)\]\([^)]+\)', r'[Image: \1]', line)

    # Links: [text](url) -> \href{url}{text} or just text for simplicity
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        # Simple approach: just show the text
        return text

    line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, line)

    # Bold: **text** -> \textbf{text}
    line = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', line)

    # Italic: *text* -> \textit{text} (but not inside math)
    # This is tricky - skip if it looks like math
    def replace_italic(match):
        text = match.group(1)
        # Don't replace if it contains math-like content
        if '\\' in text or '$' in text:
            return match.group(0)
        return f'\\textit{{{text}}}'

    line = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', replace_italic, line)

    # Inline code: `code` -> \texttt{code}
    line = re.sub(r'`([^`]+)`', r'\\texttt{\1}', line)

    # Escape problematic characters in non-math parts
    # This is complex - we need to avoid escaping inside $...$
    # For now, do minimal escaping
    # line = line.replace('&', r'\&')  # Often in math, skip
    # line = line.replace('%', r'\%')

    return line


def build_latex(images_dir: Path) -> Path:
    """Build the complete LaTeX document."""
    print("Building LaTeX document...")

    latex_parts = [LATEX_HEADER]

    page_files = sorted(THREAD_DIR.glob("page_*.md"))

    for page_file in page_files:
        if page_file.name == "index.md":
            continue

        content = page_file.read_text(encoding="utf-8")
        latex_content = markdown_to_latex(content, images_dir)
        latex_parts.append(latex_content)
        latex_parts.append(r'\newpage')

    latex_parts.append(LATEX_FOOTER)

    tex_file = BUILD_DIR / "document.tex"
    tex_file.write_text('\n'.join(latex_parts), encoding='utf-8')

    print(f"  Generated {tex_file} ({tex_file.stat().st_size / 1024 / 1024:.1f}MB)")
    return tex_file


def compile_pdf(tex_file: Path) -> Path:
    """Compile LaTeX to PDF."""
    print("Compiling PDF (this may take a while)...")

    # Run xelatex twice for TOC - use scrollmode to continue past errors
    for run in [1, 2]:
        print(f"  Pass {run}/2...")
        result = subprocess.run(
            ["/Library/TeX/texbin/xelatex", "-interaction=scrollmode", "-output-directory", str(BUILD_DIR), str(tex_file)],
            capture_output=True,
            text=True,
            cwd=BUILD_DIR,
            timeout=600  # 10 minute timeout
        )

        if result.returncode != 0 and run == 2:
            # Check if PDF was still generated
            pdf_path = BUILD_DIR / "document.pdf"
            if not pdf_path.exists():
                print(f"  LaTeX errors (showing last 50 lines of log):")
                log_file = BUILD_DIR / "document.log"
                if log_file.exists():
                    log_content = log_file.read_text()
                    print('\n'.join(log_content.split('\n')[-50:]))
                raise RuntimeError("LaTeX compilation failed")

    pdf_path = BUILD_DIR / "document.pdf"
    print(f"  Generated {pdf_path} ({pdf_path.stat().st_size / 1024 / 1024:.1f}MB)")
    return pdf_path


def compress_pdf(pdf_file: Path) -> Path:
    """Compress PDF using ghostscript."""
    print("Compressing PDF...")

    output = BUILD_DIR / "compressed.pdf"

    result = subprocess.run([
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output}",
        str(pdf_file),
    ], capture_output=True, text=True)

    if result.returncode != 0 or not output.exists():
        print(f"  Ghostscript failed, using uncompressed PDF")
        return pdf_file

    print(f"  Compressed to {output} ({output.stat().st_size / 1024 / 1024:.1f}MB)")
    return output


def main():
    print("=" * 60)
    print("Building Wilmott Thread PDF (Direct LaTeX)")
    print("=" * 60)

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)

    # Step 1: Compress images
    images_dir = compress_images()

    # Step 2: Build LaTeX
    tex_file = build_latex(images_dir)

    # Step 3: Compile PDF
    pdf_file = compile_pdf(tex_file)

    # Step 4: Compress
    final_pdf = compress_pdf(pdf_file)

    # Copy to output
    shutil.copy(final_pdf, OUTPUT_PDF)

    print()
    print("=" * 60)
    size_mb = OUTPUT_PDF.stat().st_size / 1024 / 1024
    print(f"Done! Output: {OUTPUT_PDF} ({size_mb:.1f}MB)")
    if size_mb > 8:
        print(f"  Warning: File exceeds 8MB target")
    print("=" * 60)


if __name__ == "__main__":
    main()
