#!/usr/bin/env python3
"""
Build PDF directly from raw HTML files.
"""

import re
import shutil
import subprocess
from pathlib import Path
from PIL import Image

# Configuration - okay quality for 3-part split
MAX_IMAGE_DIM = 400
JPEG_QUALITY = 50
NUM_PARTS = 3
BUILD_DIR = Path("/tmp/wilmott_html_build")
RAW_DIR = Path("./archive/raw")
IMAGES_SRC = Path("./archive/images")
OUTPUT_PDF = Path("./archive/pdfs/wilmott_thread.pdf")


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
            pass

    print(f"  Compressed {count} images: {total_original/1024/1024:.1f}MB -> {total_compressed/1024/1024:.1f}MB")
    return dest_dir


def combine_html(images_dir: Path) -> Path:
    """Combine all raw HTML files into one, fixing image paths."""
    print("Combining HTML files...")

    # Get all raw HTML files in order
    html_files = sorted(RAW_DIR.glob("page_start_*.html"))

    html_header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Wilmott Thread: Breakthrough in SDEs</title>
    <style>
        body { font-family: Helvetica, Arial, sans-serif; font-size: 9pt; max-width: 800px; margin: auto; padding: 10px; line-height: 1.3; }
        .post { margin-bottom: 1em; border-bottom: 1px solid #ccc; padding-bottom: 0.5em; }
        .author { font-weight: bold; color: #333; }
        .timestamp { color: #666; font-size: 0.9em; }
        .content { margin-top: 0.5em; }
        pre, code { background: #f4f4f4; padding: 2px 5px; font-size: 0.9em; }
        pre { padding: 10px; overflow-x: auto; }
        img { max-width: 100%; height: auto; }
        blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 1em; color: #555; }
        h1 { font-size: 1.5em; }
        h2 { font-size: 1.2em; }
        @media print {
            .post { page-break-inside: avoid; }
        }
    </style>
</head>
<body>
<h1>Breakthrough in the Theory of Stochastic Differential Equations and Their Simulation</h1>
<p><em>Wilmott Forum Thread Archive</em></p>
<hr>
"""

    combined_parts = []

    seen_posts = set()

    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8")

        # Extract just the post divs
        # Find all post content between <div class="post has-profile"> ... </div>
        post_pattern = r'<div class="post has-profile"[^>]*>(.*?)</div>\s*</div>\s*</div>'

        # Simpler: just extract the content div
        for match in re.finditer(r'<a class="icon_post_target"[^>]*>#(\d+)</a>.*?<div class="content">(.*?)</div>\s*(?=<div class="back2top|<div class="post|$)', content, re.DOTALL):
            post_num = match.group(1)
            if post_num in seen_posts:
                continue
            seen_posts.add(post_num)

            post_content = match.group(2)

            # Fix image paths
            def fix_image(m):
                src = m.group(1)
                # Handle postimg.cc images
                if 'postimg.cc' in src or 'imgur.com' in src:
                    for domain in ['i.postimg.cc', 's26.postimg.cc', 'i.imgur.com']:
                        if domain in src:
                            idx = src.find(domain)
                            path = src[idx + len(domain):]
                            path = re.sub(r'\.(png|jpeg|webp)$', '.jpg', path, flags=re.IGNORECASE)
                            local_path = images_dir / domain / path.lstrip('/')
                            if local_path.exists():
                                return f'src="{local_path}"'
                return m.group(0)

            post_content = re.sub(r'src=["\']([^"\']+)["\']', fix_image, post_content)

            combined_parts.append((post_num, f'<div class="post"><strong>#{post_num}</strong><div class="content">{post_content}</div></div>'))

    # Split by content size into NUM_PARTS
    total_size = sum(len(p[1]) for p in combined_parts)
    target_size = total_size // NUM_PARTS
    print(f"  Total content: {total_size/1024/1024:.1f}MB, target per part: {target_size/1024/1024:.1f}MB")

    output_files = []
    current_parts = [html_header]
    current_size = 0
    part_num = 1

    for post_num, post_html in combined_parts:
        post_size = len(post_html)

        # Start new part if we've exceeded target (but not on last part)
        if current_size >= target_size and part_num < NUM_PARTS:
            current_parts.append("</body></html>")
            output_file = BUILD_DIR / f"combined_part{part_num}.html"
            output_file.write_text('\n'.join(current_parts), encoding='utf-8')
            output_files.append(output_file)
            print(f"  Part {part_num}: posts up to #{post_num} ({output_file.stat().st_size / 1024 / 1024:.1f}MB)")

            part_num += 1
            current_parts = [html_header]
            current_size = 0

        current_parts.append(post_html)
        current_size += post_size

    # Final part
    current_parts.append("</body></html>")
    output_file = BUILD_DIR / f"combined_part{part_num}.html"
    output_file.write_text('\n'.join(current_parts), encoding='utf-8')
    output_files.append(output_file)
    print(f"  Part {part_num}: posts up to #{post_num} ({output_file.stat().st_size / 1024 / 1024:.1f}MB)")

    print(f"  Combined {len(seen_posts)} posts into {len(output_files)} parts")
    return output_files


def html_to_pdf(html_file: Path) -> Path:
    """Convert HTML to PDF."""
    print("Converting to PDF...")

    output = BUILD_DIR / "output.pdf"

    # Use xhtml2pdf (pure Python, no system dependencies)
    try:
        from xhtml2pdf import pisa
        print("  Using xhtml2pdf...")

        html_content = html_file.read_text(encoding='utf-8')

        with open(output, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

        if pisa_status.err:
            print(f"  Warning: xhtml2pdf had {pisa_status.err} errors")

        if output.exists():
            print(f"  Generated {output} ({output.stat().st_size / 1024 / 1024:.1f}MB)")
            return output
    except Exception as e:
        print(f"  xhtml2pdf failed: {e}")

    raise RuntimeError("Could not convert to PDF")


def compress_pdf(pdf_file: Path) -> Path:
    """Compress PDF using ghostscript."""
    print("Compressing PDF...")

    output = BUILD_DIR / "compressed.pdf"

    result = subprocess.run([
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",  # Good quality for 3-part split
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-dSubsetFonts=true",
        "-dEmbedAllFonts=false",  # Don't embed standard fonts
        "-dCompressFonts=true",
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
    print(f"Building Wilmott Thread PDF ({NUM_PARTS} parts)")
    print("=" * 60)

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)

    # Step 1: Compress images
    images_dir = compress_images()

    # Step 2: Combine HTML (returns list of files)
    html_files = combine_html(images_dir)

    # Step 3-4: Convert and compress each part
    output_pdfs = []
    for i, html_file in enumerate(html_files, 1):
        print(f"\nProcessing Part {i}/{len(html_files)}...")
        pdf_file = html_to_pdf(html_file)
        final_pdf = compress_pdf(pdf_file)

        output_name = Path(f"./archive/pdfs/wilmott_thread_part{i}.pdf")
        shutil.copy(final_pdf, output_name)
        output_pdfs.append(output_name)

    print()
    print("=" * 60)
    total_size = 0
    for pdf in output_pdfs:
        size_mb = pdf.stat().st_size / 1024 / 1024
        total_size += size_mb
        status = "OK" if size_mb <= 8 else "WARNING: >8MB"
        print(f"  {pdf}: {size_mb:.1f}MB [{status}]")
    print(f"  Total: {total_size:.1f}MB across {len(output_pdfs)} files")
    print("=" * 60)


if __name__ == "__main__":
    main()
