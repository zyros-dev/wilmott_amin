# Utility scripts

Run these commands from the repository root. Generated archives, reports, and charts are written into `archive/`, `reports/`, and `assets/`.

## Collection and extraction

- `scrape_wilmott.py` — download the forum thread into `archive/raw/`
- `image_scraper.py` — download externally linked images into `archive/images/`
- `extract_markdown.py` — convert the raw HTML into `archive/thread_page/`
- `latex_translator.py` — normalize the forum's LaTeX while extracting Markdown

```bash
python scripts/scrape_wilmott.py
python scripts/image_scraper.py
python scripts/extract_markdown.py
python scripts/latex_translator.py
```

## PDF builders

- `build_pdf.py` — original PDF builder
- `build_html_pdf.py` — HTML-based PDF builder
- `build_latex_pdf.py` — LaTeX-based PDF builder

## Analysis and reports

- `analyze_thread.py` — shared thread parser and exploratory report
- `analyze_amin_raw.py` — raw Amin-focused analysis
- `create_amin_report.py` — build `reports/amin_report.pdf`
- `build_posting_rate_chart.py` — build the README's `assets/posting_rate.png`

```bash
python scripts/analyze_thread.py
python scripts/create_amin_report.py
python scripts/build_posting_rate_chart.py
```
