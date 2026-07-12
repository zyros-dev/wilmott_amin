#!/usr/bin/env python3
"""
Wilmott Forum Image Scraper

Extracts and downloads images from forum thread HTML files.
Images are downloaded from external sources while filtering out avatars,
logos, emojis, and forum attachments.

Requirements:
- Extract image URLs from HTML files in ./raw/*.html
- Filter out forum attachments (download/file.php URLs)
- Filter out avatars, icons, emojis, logos, and GIFs
- Preserve URL path structure in ./images/
- Use 32 thread pool with retries and exponential backoff
- Idempotent operation with file existence checks
- Track failures and exit on too many consecutive failures
- Validate downloaded files
"""

import html
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock
from typing import Generator, Optional, Tuple
from urllib.parse import urlparse

import requests  # type: ignore[import-untyped]

# Configuration
MAX_WORKERS = 32
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0  # seconds
MAX_CONSECUTIVE_FAILURES = 10
RAW_DIR = Path("./raw")
IMAGES_DIR = Path("./images")
MIN_IMAGE_SIZE = 100  # bytes
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

# Request headers
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-GB,en;q=0.8",
    "cache-control": "max-age=0",
    "dnt": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
}

# Global failure tracking
consecutive_failures = 0
failure_lock = Lock()
should_exit = False


def should_skip_url(url: str) -> bool:
    """
    Determine if a URL should be skipped based on filters.

    Filters:
    - Forum attachments (download/file.php)
    - Avatars (contains 'avatar', 'user' avatars)
    - Icons, emojis, logos (common patterns)
    - GIFs (animated images)
    """
    url_lower = url.lower()

    # Skip forum attachments
    if "download/file.php" in url_lower:
        return True

    # Skip common asset patterns
    skip_patterns = [
        r"avatar",
        r"/icon",
        r"/emoji",
        r"logo",
        r"/img/.*logo",
        r"favicon",
        r"smilies",
        r"/assets/",
        r"\.gif$",  # Skip GIFs
    ]

    for pattern in skip_patterns:
        if re.search(pattern, url_lower):
            return True

    return False


def extract_image_urls(html_content: str) -> Generator[str, None, None]:
    """
    Extract image URLs from HTML content.

    Yields: Decoded, valid image URLs
    """
    # Pattern to find both regular src and data-src attributes
    patterns = [
        r'src="([^"]*)"',
        r"src='([^']*)'",
        r'data-src="([^"]*)"',
        r"data-src='([^']*)'",
        # Also look for href in attachments
        r'href="([^"]*\.(jpg|jpeg|png|webp))"',
        r"href='([^']*\.(jpg|jpeg|png|webp))'",
    ]

    found_urls = set()

    for pattern in patterns:
        matches = re.finditer(pattern, html_content, re.IGNORECASE)
        for match in matches:
            url = match.group(1)

            # Decode HTML entities
            url = html.unescape(url)

            # Skip if we've already found this URL
            if url in found_urls:
                continue

            # Only process HTTP(S) URLs
            if not url.startswith(("http://", "https://")):
                continue

            # Check if it's an image URL based on extension
            url_lower = url.lower()
            if not any(url_lower.endswith(ext) for ext in IMAGE_EXTENSIONS):
                # Try to detect by content disposition or check if common image format
                if not any(
                    fmt in url_lower
                    for fmt in [".jpg", ".jpeg", ".png", ".gif", ".webp"]
                ):
                    continue

            # Apply filters
            if should_skip_url(url):
                continue

            found_urls.add(url)
            yield url


def get_image_output_path(url: str) -> Path:
    """
    Convert a URL to a local file path preserving the structure.

    Examples:
    - https://i.postimg.cc/029J5LX5/Ito-Hermite-New-Exp09.png
      -> ./images/i.postimg.cc/029J5LX5/Ito-Hermite-New-Exp09.png
    - https://i.imgur.com/XK2jpwF.png
      -> ./images/i.imgur.com/XK2jpwF.png
    """
    parsed = urlparse(url)

    # Combine domain and path
    domain = parsed.netloc
    path = parsed.path.lstrip("/")

    # Remove query parameters from filename
    if "?" in path:
        path = path.split("?")[0]

    output_path = IMAGES_DIR / domain / path

    return output_path


def download_image(url: str) -> Tuple[str, bool, str]:
    """
    Download a single image with retry logic.

    Returns: (url, success, message)
    """
    global consecutive_failures, should_exit

    output_path = get_image_output_path(url)

    # Check if already downloaded
    if output_path.exists() and output_path.stat().st_size > 0:
        return (url, True, "already exists")

    for attempt in range(MAX_RETRIES):
        if should_exit:
            return (url, False, "exit requested")

        try:
            # Exponential backoff
            if attempt > 0:
                backoff = INITIAL_BACKOFF * (2**attempt)
                time.sleep(backoff)

            # Download the image
            response = requests.get(
                url, headers=HEADERS, timeout=30, allow_redirects=True
            )
            response.raise_for_status()

            # Validate image size
            content_length = len(response.content)
            if content_length < MIN_IMAGE_SIZE:
                raise Exception(
                    f"Image too small ({content_length} bytes, min: {MIN_IMAGE_SIZE})"
                )

            # Create output directories
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Write the image
            output_path.write_bytes(response.content)

            # Reset consecutive failures on success
            with failure_lock:
                consecutive_failures = 0

            return (url, True, f"downloaded ({content_length} bytes)")

        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                with failure_lock:
                    consecutive_failures += 1
                    if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                        should_exit = True
                return (url, False, f"failed after {MAX_RETRIES} attempts: {e}")

    return (url, False, "unknown error")


def extract_urls_from_html_files() -> Generator[str, None, None]:
    """
    Extract all unique image URLs from HTML files in ./raw/

    Yields: Unique image URLs
    """
    found_urls = set()

    html_files = sorted(RAW_DIR.glob("*.html"))

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"[WARN] Could not read {html_file}: {e}")
            continue

        for url in extract_image_urls(content):
            if url not in found_urls:
                found_urls.add(url)
                yield url


def main() -> None:
    """Main entry point."""
    global should_exit

    print("=" * 60)
    print("Wilmott Forum Image Scraper")
    print("=" * 60)
    print()

    # Create images directory
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Extract all image URLs from HTML files
    print("Extracting image URLs from HTML files...")
    image_urls = list(extract_urls_from_html_files())

    if not image_urls:
        print("No image URLs found in HTML files.")
        return

    print(f"Found {len(image_urls)} unique image URLs")

    # Check how many already exist
    existing = sum(
        1 for url in image_urls if get_image_output_path(url).exists()
    )
    print(f"Already downloaded: {existing}")
    print(f"Remaining to download: {len(image_urls) - existing}")
    print(f"Using {MAX_WORKERS} workers")
    print()

    if existing == len(image_urls):
        print("All images already downloaded!")
        return

    # Download images in parallel
    completed = 0
    failed = 0
    skipped = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(download_image, url): url for url in image_urls
        }

        for future in as_completed(futures):
            if should_exit:
                print("\n\nToo many consecutive failures - exiting!")
                executor.shutdown(wait=False, cancel_futures=True)
                sys.exit(1)

            url = futures[future]
            try:
                url_result, success, message = future.result()

                if success:
                    if "already exists" in message:
                        skipped += 1
                    else:
                        completed += 1
                        # Only print successful downloads (not skipped)
                        print(f"[OK] {url}: {message}")
                else:
                    failed += 1
                    print(f"[FAIL] {url}: {message}")

            except Exception as e:
                failed += 1
                print(f"[ERROR] {url}: {e}")

    print()
    print("=" * 60)
    print(f"Completed: {completed}")
    print(f"Skipped (already existed): {skipped}")
    print(f"Failed: {failed}")
    print("=" * 60)

    if failed > 0:
        print(f"\nWARNING: {failed} images failed to download.")
        print("Run the script again to retry failed images.")
        sys.exit(1)


if __name__ == "__main__":
    main()
