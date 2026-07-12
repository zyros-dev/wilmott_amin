#!/usr/bin/env python3
"""
Build a compressed PDF from the Wilmott thread markdown files.
Target: <8MB for Discord upload.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
from PIL import Image

# Configuration
MAX_IMAGE_DIM = 400  # pixels
JPEG_QUALITY = 55
BUILD_DIR = Path("/tmp/wilmott_pdf_build")
IMAGES_SRC = Path("./images")
THREAD_DIR = Path("./thread_page")
OUTPUT_PDF = Path("./wilmott_thread.pdf")

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

        # Preserve directory structure
        rel_path = src_path.relative_to(IMAGES_SRC)
        dest_path = dest_dir / rel_path.with_suffix(".jpg")
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            total_original += src_path.stat().st_size

            with Image.open(src_path) as img:
                # Convert to RGB (for JPEG)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                elif img.mode != "RGB":
                    img = img.convert("RGB")

                # Resize if larger than max
                w, h = img.size
                if max(w, h) > MAX_IMAGE_DIM:
                    ratio = MAX_IMAGE_DIM / max(w, h)
                    new_size = (int(w * ratio), int(h * ratio))
                    img = img.resize(new_size, Image.LANCZOS)

                # Save as JPEG
                img.save(dest_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
                total_compressed += dest_path.stat().st_size

            count += 1
            if count % 100 == 0:
                print(f"  Processed {count} images...")
        except Exception as e:
            print(f"  Warning: Failed to compress {src_path}: {e}")

    print(f"  Compressed {count} images: {total_original/1024/1024:.1f}MB -> {total_compressed/1024/1024:.1f}MB")
    return dest_dir

def combine_markdown(images_dir: Path):
    """Combine all markdown files into one, updating image paths."""
    print("Combining markdown files...")

    combined = []
    combined.append("---")
    combined.append("title: 'Breakthrough in the theory of stochastic differential equations and their simulation'")
    combined.append("subtitle: 'Wilmott Forum Thread Archive'")
    combined.append("geometry: margin=1in")
    combined.append("fontsize: 10pt")
    combined.append("---")
    combined.append("")

    # Get all page files in order
    page_files = sorted(THREAD_DIR.glob("page_*.md"))
    removed_images = 0

    for page_file in page_files:
        if page_file.name == "index.md":
            continue

        content = page_file.read_text(encoding="utf-8")

        # Update image paths: ../images/host/path/file.ext -> BUILD_DIR/images/host/path/file.jpg
        def replace_image_path(match):
            nonlocal removed_images
            alt = match.group(1)
            old_path = match.group(2)

            # Remove external URLs (http/https) - they cause pandoc to hang
            if old_path.startswith(("http://", "https://")):
                removed_images += 1
                return f"*[Image: {alt}]*"

            # Remove paths that aren't our local images
            if not old_path.startswith("../images/"):
                removed_images += 1
                return f"*[Image: {alt}]*"

            # Convert ../images/x/y/z.png to images_dir/x/y/z.jpg
            rel = old_path[len("../images/"):]
            # Change extension to .jpg
            rel = re.sub(r'\.(png|jpeg|webp)$', '.jpg', rel, flags=re.IGNORECASE)
            new_path = images_dir / rel

            # Check if compressed image exists
            if not new_path.exists():
                removed_images += 1
                return f"*[Image: {alt}]*"

            return f"![{alt}]({new_path})"

        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image_path, content)

        # Remove navigation lines
        content = re.sub(r'\[← Previous\].*?\n', '', content)
        content = re.sub(r'\[Next →\].*?\n', '', content)
        content = re.sub(r'\[Index\].*?\n', '', content)

        # Remove page headers (we'll have one title)
        content = re.sub(r'^# Breakthrough.*\n', '', content, flags=re.MULTILINE)
        content = re.sub(r'^\*\*Page \d+ of \d+\*\*.*\n', '', content, flags=re.MULTILINE)

        combined.append(content)
        combined.append("\n\\newpage\n")

    output_file = BUILD_DIR / "combined.md"
    output_file.write_text("\n".join(combined), encoding="utf-8")
    print(f"  Combined into {output_file} ({output_file.stat().st_size / 1024 / 1024:.1f}MB)")
    print(f"  Removed {removed_images} missing/external images")
    return output_file

def fix_latex_delimiters(content: str) -> str:
    """Fix common LaTeX delimiter issues in the markdown."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False

    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue

        if in_code_block:
            fixed_lines.append(line)
            continue

        # Fix "$ $" (dollar space dollar) -> "$$"
        line = re.sub(r'\$ \$', '$$', line)

        # Fix mixed display delimiters: $$...$ (single at end) -> $$...$$
        line = re.sub(r'\$\$([^$]+)\$(?!\$)', r'$$\1$$', line)

        # Fix trailing space before closing $ (pandoc requires no space)
        # $content $ -> $content$
        line = re.sub(r'\$([^$]+?) \$', r'$\1$', line)
        # $$content $$ with space -> $$content$$
        line = re.sub(r'\$\$([^$]+?) \$\$', r'$$\1$$', line)

        # Fix missing space before opening $ (pandoc requires space or line start)
        # word$\ or word$ X -> word $\ or word $ X  (only opening math, not closing)
        line = re.sub(r'([a-zA-Z])\$([ \\])', r'\1 $\2', line)

        # If line starts with $ and previous line has text, pandoc won't
        # recognize the $ as math delimiter. Add blank line to make new paragraph.
        if line.startswith('$') and fixed_lines and fixed_lines[-1].strip():
            fixed_lines.append('')  # Add blank line

        # Check for unbalanced $ in the line (after fixes)
        temp = line.replace(r'\$', '')  # Remove escaped dollars
        temp = re.sub(r'\$\$[^$]*\$\$', '', temp)  # Remove display math
        temp = re.sub(r'\$[^$]*\$', '', temp)  # Remove inline math

        # If there are still $ signs, the line has unbalanced math - escape them
        if '$' in temp:
            # This line has unbalanced delimiters - escape all $ to prevent LaTeX errors
            line = line.replace('$$', 'DOUBLE_DOLLAR_PLACEHOLDER')
            line = line.replace('$', r'\$')
            line = line.replace('DOUBLE_DOLLAR_PLACEHOLDER', '$$')

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def fix_latex_outside_math(content: str) -> str:
    """Escape backslashes in LaTeX commands that are outside math mode."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue

        # Skip lines in code blocks
        if in_code_block:
            fixed_lines.append(line)
            continue

        # Skip lines that have math delimiters - they're probably fine
        if '$' in line:
            fixed_lines.append(line)
            continue

        # Escape backslashes in LaTeX commands that aren't in math mode
        # This prevents pandoc/LaTeX from interpreting them
        line = re.sub(r'\\(text|frac|sqrt|sum|int|prod|left|right|cdot|times)\{', r'\\\1{', line)
        line = re.sub(r'\\(alpha|beta|gamma|sigma|mu|pi|Pi|Delta|infty|partial)\b', r'\\\1', line)

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def convert_to_pdf(markdown_file: Path):
    """Convert markdown to PDF using pandoc."""
    print("Converting to PDF (this may take a while)...")

    # Pre-process to fix LaTeX issues
    content = markdown_file.read_text(encoding='utf-8')
    content = fix_latex_delimiters(content)
    content = fix_latex_outside_math(content)
    markdown_file.write_text(content, encoding='utf-8')

    output = BUILD_DIR / "output.pdf"

    cmd = [
        "pandoc",
        str(markdown_file),
        "-o", str(output),
        "--pdf-engine=/Library/TeX/texbin/xelatex",
        "-V", "geometry:margin=0.75in",
        "-V", "fontsize=9pt",
        "-V", "documentclass=article",
        "--toc",
        "--toc-depth=1",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Pandoc error: {result.stderr[:1000]}")
        # Try without some options
        print("  Retrying with simpler options...")
        cmd = [
            "pandoc",
            str(markdown_file),
            "-o", str(output),
            "--pdf-engine=/Library/TeX/texbin/xelatex",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Pandoc failed: {result.stderr[:500]}")

    print(f"  Generated {output} ({output.stat().st_size / 1024 / 1024:.1f}MB)")
    return output

def compress_pdf(pdf_file: Path):
    """Compress PDF using ghostscript."""
    print("Compressing PDF with ghostscript...")

    output = BUILD_DIR / "compressed.pdf"

    cmd = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",  # 150 dpi images
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output}",
        str(pdf_file),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Warning: Ghostscript compression failed: {result.stderr[:500]}")
        return pdf_file

    print(f"  Compressed to {output} ({output.stat().st_size / 1024 / 1024:.1f}MB)")
    return output

def main():
    print("=" * 60)
    print("Building Wilmott Thread PDF")
    print("=" * 60)

    # Clean build directory
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)

    # Step 1: Compress images
    images_dir = compress_images()

    # Step 2: Combine markdown
    markdown_file = combine_markdown(images_dir)

    # Step 3: Convert to PDF
    pdf_file = convert_to_pdf(markdown_file)

    # Step 4: Compress PDF
    final_pdf = compress_pdf(pdf_file)

    # Copy to output
    shutil.copy(final_pdf, OUTPUT_PDF)

    print()
    print("=" * 60)
    size_mb = OUTPUT_PDF.stat().st_size / 1024 / 1024
    print(f"Done! Output: {OUTPUT_PDF} ({size_mb:.1f}MB)")
    if size_mb > 8:
        print(f"  Warning: File is larger than 8MB target!")
        print(f"  Consider reducing MAX_IMAGE_DIM or JPEG_QUALITY")
    print("=" * 60)

if __name__ == "__main__":
    main()
