#!/usr/bin/env python3
"""
Wilmott Forum Thread Scraper

Scrapes the forum thread with parallelization, retry logic, and idempotency.
Raw HTML files are saved to ./archive/raw/ directory.
"""

import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import sys
from threading import Lock

# Configuration
THREAD_ID = 99702
POSTS_PER_PAGE = 15
MAX_WORKERS = 32
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0  # seconds
MAX_CONSECUTIVE_FAILURES = 10
RAW_DIR = Path("./archive/raw")

# Ordinary browser-like request headers. Authentication material must not be
# committed; supply any future session handling outside the repository.
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'origin': 'https://forum.wilmott.com',
    'referer': 'https://forum.wilmott.com/viewtopic.php?t=99702',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36',
}

COOKIES: dict[str, str] = {}

# Global failure tracking
consecutive_failures = 0
failure_lock = Lock()
should_exit = False


def get_page_filename(start: int) -> Path:
    """Get the filename for a page based on its start offset."""
    return RAW_DIR / f"page_start_{start:05d}.html"


def fetch_page(start: int, force_refresh: bool = False) -> tuple[int, bool, str]:
    """
    Fetch a single page with retry logic.

    Returns: (start, success, message)
    """
    global consecutive_failures, should_exit

    filename = get_page_filename(start)

    # Check if already downloaded
    if not force_refresh and filename.exists() and filename.stat().st_size > 1000:
        return (start, True, "already exists")

    url = f"https://forum.wilmott.com/viewtopic.php?t={THREAD_ID}&start={start}"

    for attempt in range(MAX_RETRIES):
        if should_exit:
            return (start, False, "exit requested")

        try:
            backoff = INITIAL_BACKOFF * (2 ** attempt)
            if attempt > 0:
                time.sleep(backoff)

            response = requests.get(
                url,
                headers=HEADERS,
                cookies=COOKIES,
                timeout=30,
                allow_redirects=True
            )

            # Check for Cloudflare challenge
            if response.status_code == 403 or 'Just a moment' in response.text:
                raise Exception("Cloudflare challenge detected - cookies may have expired")

            response.raise_for_status()

            # Verify it's actual content (not an error page)
            if len(response.text) < 5000 or 'postlist' not in response.text:
                raise Exception(f"Invalid content received (length: {len(response.text)})")

            # Save the raw HTML
            filename.parent.mkdir(parents=True, exist_ok=True)
            filename.write_text(response.text, encoding='utf-8')

            # Reset consecutive failures on success
            with failure_lock:
                consecutive_failures = 0

            return (start, True, f"downloaded ({len(response.text)} bytes)")

        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                with failure_lock:
                    consecutive_failures += 1
                    if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                        should_exit = True
                return (start, False, f"failed after {MAX_RETRIES} attempts: {e}")

    return (start, False, "unknown error")


def get_total_pages() -> int:
    """
    Fetch the first page to determine total number of pages.
    """
    print("Fetching first page to determine total pages...")

    url = f"https://forum.wilmott.com/viewtopic.php?t={THREAD_ID}"

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(
                url,
                headers=HEADERS,
                cookies=COOKIES,
                timeout=30,
                allow_redirects=True
            )

            if response.status_code == 403 or 'Just a moment' in response.text:
                raise Exception("Cloudflare challenge - update cookies")

            response.raise_for_status()

            # Parse total posts from the HTML
            # Look for a post-count marker or page count
            import re

            # Try to find the last page number in pagination
            # Pattern: start=XXXX in pagination links
            matches = re.findall(r'start=(\d+)', response.text)
            if matches:
                max_start = max(int(m) for m in matches)
                total_pages = (max_start // POSTS_PER_PAGE) + 1
                print(f"Found max start offset: {max_start}, estimated {total_pages} pages")
                return total_pages

            # Fallback: look for "Page X of Y" pattern
            page_match = re.search(r'Page\s+\d+\s+of\s+(\d+)', response.text)
            if page_match:
                return int(page_match.group(1))

            raise Exception("Could not determine total pages")

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(INITIAL_BACKOFF * (2 ** attempt))

    raise Exception("Failed to fetch first page after all retries")


def main():
    global should_exit

    print("=" * 60)
    print("Wilmott Forum Thread Scraper")
    print("=" * 60)

    # Create raw directory
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Get total pages
    try:
        total_pages = get_total_pages()
    except Exception as e:
        print(f"ERROR: {e}")
        print("\nThe Cloudflare cookies may have expired.")
        print("The forum rejected the request. Configure session handling outside the repository if needed.")
        sys.exit(1)

    # Generate all page offsets
    page_offsets = [i * POSTS_PER_PAGE for i in range(total_pages)]

    # Check how many already exist
    existing = sum(1 for offset in page_offsets if get_page_filename(offset).exists())
    print(f"\nTotal pages: {total_pages}")
    print(f"Already downloaded: {existing}")
    refresh_offset = max(page_offsets)
    print(f"Remaining: {total_pages - existing}")
    print(f"Refreshing current final page: start={refresh_offset}")
    print(f"Using {MAX_WORKERS} workers")
    print()

    # Download pages in parallel
    completed = 0
    failed = 0
    skipped = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(fetch_page, offset, offset == refresh_offset): offset
            for offset in page_offsets
        }

        for future in as_completed(futures):
            if should_exit:
                print("\n\nToo many consecutive failures - exiting!")
                executor.shutdown(wait=False, cancel_futures=True)
                sys.exit(1)

            offset = futures[future]
            try:
                start, success, message = future.result()

                if success:
                    if "already exists" in message:
                        skipped += 1
                    else:
                        completed += 1
                        print(f"[OK] Page start={start}: {message}")
                else:
                    failed += 1
                    print(f"[FAIL] Page start={start}: {message}")

            except Exception as e:
                failed += 1
                print(f"[ERROR] Page start={offset}: {e}")

    print()
    print("=" * 60)
    print(f"Completed: {completed}")
    print(f"Skipped (already existed): {skipped}")
    print(f"Failed: {failed}")
    print("=" * 60)

    if failed > 0:
        print(f"\nWARNING: {failed} pages failed to download.")
        print("Run the script again to retry failed pages.")
        sys.exit(1)


if __name__ == "__main__":
    main()
