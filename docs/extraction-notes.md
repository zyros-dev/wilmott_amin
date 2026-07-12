# Wilmott LaTeX Extraction

## Status
- 3227 posts extracted
- 64 errors (2.0%) - unfixable source data issues (unbalanced delimiters in original posts)
- 11/11 translator tests passing

## "go fix" workflow
```
while errors > 0:
    rm -rf archive/thread_page && python scripts/extract_markdown.py
    fix in scripts/latex_translator.py based on error types
    python scripts/latex_translator.py

# when done, validate with samplers:
sample pages 1-20, 21-40, 41-60, and 61-65
```

## Files
- `scripts/latex_translator.py` - Transform pipeline
- `scripts/extract_markdown.py` - Main script
- `archive/thread_page/` - Output (65 pages)

## Transforms (in order)
1. fix_sqrt_parens: `\sqrt()` → `\sqrt{}`
2. fix_text_with_math: `\text{$x$}` → `x\text{}`
3. remove_embedded_emoji: `![;)](./images/...)` → ``
4. fix_currency: `$2700` → `\$2700`
5. fix_escaped_triple_dollar: `\$$$` → `$$`
6. normalize_delimiters: `[$]`, `\[`, `\(` → `$`, `$$`
7. fix_standalone_dollar: lone `$` or `> $` → `$$`
8. fix_trailing_double_dollar: `$ $` at EOL → `$`
9. fix_mixed_display_delimiters: `$$...$` → `$$...$$`
10. fix_missing_space_before_math: `of$X$` → `of $X$`

## Remaining issues (source data)
- 45 posts have unbalanced `$` or `$$` in original forum posts
- Cannot be auto-fixed without knowing author intent
