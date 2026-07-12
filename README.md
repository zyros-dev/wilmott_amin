# Wilmott Amin archive

This repository is an archival copy of the Wilmott Technical Forum thread
[*Breakthrough in the theory of stochastic differential equations and their simulation*](https://forum.wilmott.com/viewtopic.php?f=4&t=99702).

The thread was started by the forum user **Amin** and combines proposed mathematics about stochastic differential equations and simulation with extensive personal writing. This repository preserves the public discussion for easier reading and analysis. Inclusion here does not endorse or verify any mathematical, medical, political, or personal claims made in the posts.

## Coverage

- 2,913 posts
- 59 cleaned Markdown pages
- 195 raw HTML pages
- Date range: April 17, 2016 to January 20, 2026
- 1,117 locally archived images
- Combined and split PDF editions

The Markdown archive begins at [`thread_page/index.md`](thread_page/index.md). The combined PDF is [`wilmott_thread.pdf`](wilmott_thread.pdf); three smaller parts are also included.

## Repository contents

- `raw/` — HTML responses captured from the forum
- `raw.zip` — compressed copy of the raw responses
- `thread_page/` — extracted and cleaned Markdown, split into 59 pages
- `images/` — images downloaded from links embedded in the posts
- `scrape_wilmott.py` — forum scraper
- `image_scraper.py` — linked-image downloader
- `extract_markdown.py` and `latex_translator.py` — HTML-to-Markdown and LaTeX cleanup pipeline
- `build_*_pdf.py` — PDF generation scripts
- `wilmott_thread*.pdf` — rendered editions of the thread
- `wilmott_analysis.pdf` and `amin_report.pdf` — exploratory reports generated from the archive

## Extraction notes

All 2,913 posts were extracted. The cleanup pipeline reports 45 posts (about 1.5%) with unbalanced LaTeX delimiters inherited from the source material. Those expressions were not guessed or silently rewritten where the author's intent was unclear.

The raw HTML remains available when fidelity matters. Forum pages may have changed since this snapshot was collected.

## Attribution and status

The posts and embedded materials belong to their respective authors and rights holders. This is an independent archival project and is not affiliated with, sponsored by, or endorsed by Wilmott, Wilmott.com, or the forum participants.

No license is granted for the archived third-party content. The utility scripts are included for reproducibility, but this repository as a whole should not be treated as an open-licensed dataset.
