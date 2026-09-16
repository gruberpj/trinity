# PDF Content Parity Review

**Date:** 2026-09-16
**Files:** `manuscript/Mystery_of_the_Trinity.md` (source) vs `manuscript/Mystery_of_the_Trinity.pdf` (93 pages)
**Tooling:** Python 3.9, pypdf, difflib.SequenceMatcher (script: `scripts/verify_pdf_parity.py`)

## Method

1. Extracted all text from the PDF page by page with pypdf; joined pages with spaces; whitespace normalized (`\s+` → single space).
2. Normalized the manuscript: stripped markdown syntax (`#`, `##`, `>`, `-`, `*`, `**`, backticks), rewrote TOC list entries (`- [Chapter 1 — …](#anchor)` → `Chapter 1 — …`), stripped link/image URL tails; punctuation preserved.
3. Tokenized both into word tokens (lowercase). Ran `SequenceMatcher` on the token streams and inspected every opcode: `equal` = matched, `delete` = manuscript words not found in the PDF, `insert` = PDF-only additions. Reported manuscript runs of ≥3 consecutive missing words.
4. Word counts computed on the token streams.
5. Special-character spot checks (counts in both files + presence checks).

## Counts

| Metric | Manuscript | PDF | Delta |
|---|---|---|---|
| Word tokens | 26,974 | 27,189 | +215 (expected ≥ 0 — front matter/TOC/page numbers/footnotes) |
| `[possibly` flags | 20 | 20 | 0 |
| Em-dash U+2014 | 392 | 392 | 0 |
| En-dash U+2013 | 1 | 1 | 0 |
| Ellipsis U+2026 | 1 | 1 | 0 |
| Double quotes `"` | 274 | 274 | 0 |
| Apostrophes `'` | 485 | 485 | 0 |
| Curly quotes | 0 (1 right-single-quote both) | 0 (1 right-single-quote both) | 0 |
| U+FFFD replacement char | 0 | 0 | 0 |

## Subsequence Result: **PASS**

- Matched manuscript words: **26,907 / 26,974** (99.75%); SequenceMatcher ratio 0.993556.
- Missing manuscript words: 67 — **all** are tokenization artifacts of hyphenated line-breaks in the Notes & Sources section (long URLs split across lines, e.g. `biblegateway` → `biblegatewa- y`, `https` → `htt- ps`) plus the four `--` horizontal-rule markers not rendered as text.
- **Missing runs (≥3 consecutive manuscript words): 0.**

All PDF-only insertions were accounted for and are front-matter artifacts, not content loss:
- page numbers 1–93,
- TOC dot-leaders and page-number column (chapters at 17, 27, 37, 45, 55, 63, notes at 83),
- footnote reference numbers 1–49,
- Notes & Sources footnote text (rendered as footnotes at page bottoms).

## Special-Character Spot Checks

| Check | Result |
|---|---|
| `[possibly: …]` flags in PDF | **20 / 20** ✓ |
| Epilogue Chesterton sentence ("Whatever is worth doing is worth doing poorly") | Present (2 occurrences: epilogue + Notes entry, matching manuscript) ✓ |
| Ch. 4 ellipsis quotation "…of our friendship with him" | Present (2 occurrences, matching manuscript lines 392 & 570) ✓ |
| Em-dashes | 392 in both — no loss ✓ |
| Curly quotes | Source uses straight quotes; PDF preserves all 274 `"` and 485 `'` exactly ✓ |
| Small-caps chapter headings | Confirmed: build script synthesizes small caps (uppercase + 0.72-scaled lowercase, `small_caps()` in `build_pdf.py`); headings extract as "Chapter 1 — Icons of the Trinity" etc.; embedded Baskerville family fonts ✓ |
| Garbling (U+FFFD, mojibake) | None ✓ |

## Verdict

**PASS — no content loss or garbling.** The PDF (93 pages, 27,189 words) contains the complete manuscript (26,974 words) as an ordered subsequence. Every ≥3-word run of the manuscript is present. The only "missing" tokens are hyphenation splits of URLs in the endnotes and markdown-only `--` rules — text-preserving artifacts. All 20 `[possibly: …]` flags, all em-dashes, and the spot-checked quotations are intact.
