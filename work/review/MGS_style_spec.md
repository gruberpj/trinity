# MGS Booklet — Typesetting Style Spec

Source: `MGS Booklet Jun 2025 interior.pdf` (InDesign, 80 pp, 306.0 × 495.0 pt = 4.25 × 6.875 in).
All measurements in points unless noted. Extracted with pypdf (visitor + content-stream tokenizer).

## 1. Page geometry

| Property | Value | Notes |
|---|---|---|
| Trim size | 306.0 × 495.0 pt | 4.25 × 6.875 in |
| Left margin | 36.0 pt | measured (body & headings x=36.0) |
| Right margin | ~36.0 pt | **INFERRED** — symmetric to left (not directly measured) |
| Text block width | ~234 pt | 36 → ~270 pt (3.25 in) |
| Body top (chapter openers) | 430.58 pt | first body baseline |
| Chapter title baseline | 449.58 pt | openers only |
| Last body line | ≈ 41.6 pt | measured on p. 7 (y=41.58) |
| Page-number baseline | 18.0 pt | bottom center |
| Lines per page | 40 | 430.58 → 41.58 at 10 pt steps |
| Body leading | 10.0 pt | exact, solid set (10/10) — delta-y = 10.00 on every consecutive body line |
| Baseline grid | none evident | leading is exact-10 but no other grid evidence |

Bottom margin ≈ 41.6 − 18.0 = ~23.6 pt to page number; top margin ≈ 495 − 449.58 ≈ 45.4 pt to title baseline (openers), ≈ 64.4 pt to body top.

## 2. Font table

All four subsets are **Adobe Garamond Pro** (Type1, embedded subsets `PKOJQT+…`, FontDescriptor family "Adobe Garamond Pro", flags 34 = serif/non-symbolic for the upright cuts). All text is black (CMYK 0,0,0,1) — no colored text observed.

| Font | Size | Style/case | Spacing | Usage |
|---|---|---|---|---|
| AGaramondPro-Regular | 10 pt | regular | Tc 0 | Body text (all chapters) |
| AGaramondPro-Regular | 10 pt | caps lead-in | Tc 0 | First words of chapter in plain caps ("WHEN we consider…") |
| AGaramondPro-Regular | 8 pt | regular | Tc 0 | Page numbers |
| AGaramondPro-Regular | 9 pt | regular | Tc 0 | Copyright page (p. 2) |
| AGaramondPro-Regular | 12 pt | regular | Tc 0 | TOC entries |
| AGaramondPro-Italic | 9 pt | italic | Tc 0 | Chapter epigraphs (p. 22 etc.) |
| AGaramondPro-Italic | 10 pt | italic | Tc 0 | Poem attribution (p. 5, "Dream of Gerontius") |
| AGaramondPro-Semibold | 18 pt | semibold + 9° shear | Tc 0 | Title page title; TOC heading |
| AGaramondPro-Semibold | 14 pt | semibold + 9° shear | **Tc −0.025** | Title page subtitle |
| AGaramondPro-Bold-SC700 | 13 pt | small caps, bold | Tc 0 | Chapter opener titles (also serve as running head) |
| AGaramondPro-Bold-SC700 | 14 pt | small caps, bold | Tc 0 | Half-title / part page (p. 5) |

Note: the SC700 cut renders *every* glyph as a small cap (no full-height capitals). The 9° shear on the title page is synthetic (matrix `c/a = tan 9°`, verified from `Tm`).

## 3. Heading hierarchy

- **Chapter title** (only heading level observed): Bold-SC700 13 pt, baseline y = 449.58, x = 36.0. Entire line in small caps. Body begins 19 pt below the title baseline (430.58). First 2–4 words of the body run in plain caps (Regular weight, not SC).
- Chapter openers: pp. 7, 22, 32, 42, 50, 65.
- **Part/half-title page** (p. 5): Bold-SC700 14 pt, y = 448.85, x = 35.94.
- No section/subsection levels observed. No space-before data (openers start at fixed y).

## 4. Title page (p. 1)

| Element | Spec |
|---|---|
| Title | Semibold 18 pt, 9° synthetic shear, x=42.1, baseline y=297.45 |
| Subtitle | Semibold 14 pt, 9° shear, tracking Tc −0.025 (≈ −25 ‰ em), y=274.79 |
| Publisher line | Regular 12 pt, no shear, x=90.2, y=43.1 ("The Pittsburgh Oratory") |

## 5. Table of contents (p. 3)

- Heading "Table of Contents": Semibold 18 pt (no shear), y=410.8, x=77.9.
- Entries: Regular 12 pt, x=35.3, dot leaders to page number right-aligned at x≈257.6.
- Entry spacing: ~23.4 pt single-line, wrapped lines 14.4 pt (12 pt × 1.2 auto leading).
- **INFERRED** leader style (periods as tab leader; exact leader char/weight not measurable from PDF).

## 6. Running heads

- Running heads appear **only on chapter-opener pages** — the chapter title line (SC700 13 pt) doubles as the head.
- Regular body pages: **no running head** (topmost line is body text at y≈448.6). Verified across pages 8–21, 23–31, 33–41, 43–49, 51–64, 66–80.

## 7. Page numbers

- Regular 8 pt, baseline y = 18.0, horizontally centered (x = 148.9–151.0, page center = 153; offset varies with digit count).
- Present on pages 3–80; **absent** on title (1), copyright (2), and blank pages (4, 6). Same position on odd and even pages (no inside/outside alternation).

## 8. Paragraph style

- First-line indent: **none observed** — every body line on sampled opener p. 7 starts at x=36.0. Mark as UNMEASURED on interior pages (full-page x-census not run).
- Paragraph separation: not detectable (no blank lines; block spacing if any is carried by indent only).
- Alignment: **NOT VERIFIED** — justification/raggedness requires right-edge bbox analysis (flagged).
- Hyphenation: **undetectable** from PDF text extraction.
- Poem (p. 5): Regular 10 pt, 12 pt leading, alternate lines indented (x=44.94 + leading spaces), stanza breaks = 24 pt.

## 9. Specials

- Blank pages: 4 and 6 — chapters begin on odd/recto pages (6 = verso of opener 7; 4 = verso of part page 5).
- No images, no vector rules, no ornaments anywhere — only clip rectangles (`re … W n`) on opener pages 5, 7, 22, 32, 42, 50, 65.
- Quotation marks: curly (“ ”). Dashes: en dash (–) used in prose. No drop caps. No ligature-specific findings (fi/fl etc. present in font, not separately verified).

## 10. Matching plan (system fonts only)

| Role | PDF font | Proposed match | Notes |
|---|---|---|---|
| Body 10 pt | AGaramondPro-Regular | **Baskerville** | closest installed old-style Garamond flavor |
| Emphasis/italic | AGaramondPro-Italic | Baskerville Italic | |
| Title page / TOC head | AGaramondPro-Semibold | Baskerville SemiBold + 9° shear transform | shear is synthetic in original too |
| Chapter heads / running head | AGaramondPro-Bold-SC700 | Baskerville Bold + synthesized small caps | scale caps ≈ 0.72×, add slight letter-spacing |
| Page numbers 8 pt | AGaramondPro-Regular | Baskerville 8 pt | |
| TOC entries 12 pt | AGaramondPro-Regular | Baskerville 12 pt | |

Fallbacks: **Hoefler Text** (Garamond-adjacent) → **Georgia** (if Georgia, use ≈ 9.5 pt body to compensate larger x-height).

**No exact equivalents on system**: true small caps (no installed face has real SC in this style family — must synthesize) and the 9° shear (synthetic — replicate via skew transform). Flagged in build step.

## 11. Uncertainties

1. Right margin ~36 pt — INFERRED (symmetric assumption; not measured).
2. Justification of body text — not verified.
3. First-line indent on interior pages — unmeasured (only opener page sampled for x).
4. TOC dot-leader style — inferred as period leader; exact glyph unverified.
5. AGaramondPro-Italic FontDescriptor flags/ItalicAngle — not extracted (true italic face assumed from rendering role).
6. Hyphenation — undetectable from extraction.
7. Baseline grid — none found; solid 10/10 leading is exact but grid alignment unproven.
