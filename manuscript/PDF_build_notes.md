# PDF Build Notes — The Mystery of the Trinity

Built 2026-09-16 from `manuscript/Mystery_of_the_Trinity.md` (text preserved verbatim;
formatting/typography only). Layout follows the measured spec of
`MGS Booklet Jun 2025 interior.pdf` (306.0 × 495.0 pt, 4.25 × 6.875 in).

## Fonts actually used

- Primary: **Baskerville.ttc** (`/System/Library/Fonts/Supplemental/`), loaded via
  reportlab `TTFont(subfontIndex=…)`:
  - 0 `Baskerville` (body Regular)
  - 1 `Baskerville Bold` (chapter titles; bold in Notes entries)
  - 2 `Baskerville Italic` (set-off prayers, italic attributions, inline `*ital*`)
  - 3 `Baskerville Bold Italic` (registered, unused in output)
  - 4 `Baskerville SemiBold` (title page; `##` section heads; TOC heading)
  - 5 `Baskerville SemiBold Italic` (registered, unused in output)
- Fallback (coded, not triggered): Georgia.ttf family.
- All 15 non-ASCII characters in the manuscript (— – ’ ł é è ê Ê ü ç × ¶ § © …)
  verified present in the Baskerville cmap before building; no glyph-substitution
  or .notdef warnings in the build log.

## Geometry (as built)

- Page 306 × 495 pt; text measure 234 pt (margins 36 pt each side).
- Body frame top edge 440.58 pt → first body baseline 430.58 pt; 10 pt leading,
  40-line grid; last baseline ≈ 40.58. Paragraph gap 19 pt (spaceAfter 9).
- Chapter/title frame top edge 462.58 pt → title baseline 449.58 pt; body starts
  19 pt below the title.
- Page numbers: Baskerville Regular 8 pt, centered, baseline 18.0 pt; omitted on
  the title page only.
- Chapters start on odd pages; blank pages are inserted when needed (numbered,
  per the spec's "all pages except the title page" rule).

## Approximations vs. the spec (all deliberate; flagged here)

1. **Synthesized small caps** — Baskerville has no small-caps face. Chapter titles
   (and `##` subheads) are set uppercase in Baskerville Bold/SemiBold, with letters
   that were lowercase in the source at 0.72× size via `<font size>` markup
   (mirrors the reference's `AGaramondPro-Bold-SC700` behavior).
2. **Synthetic italic shear (title page)** — ~9° oblique via
   `canvas.transform(1,0,0.1584,1,0,0)` with an equal left pre-shift so baselines
   sit at x=36; only ascenders lean right.
3. **TOC dot leader glyph** — `' . '` (space-dot-space, reportlab default), not
   the reference's tighter period run.
4. **Paragraph spacing** — spaceAfter 9 pt (measured reference gap of 19 pt between
   paragraph baselines = 10 + 9), versus the spec's "≈ leading" (10). Chosen to
   match the reference measurement.
5. **Uniform body top** — the spec's 430.58 pt is used for ALL body pages. The
   reference's *regular* (non-chapter) pages were measured at 451.75 pt; the spec
   value (matching chapter-opener pages) was followed.
6. **Numbered blank pages** — inserted blank (odd-start) pages carry a page number,
   per "all pages except the title page get centered page numbers".
7. **Bold in Notes and Sources** — the manuscript's `**author**` markup is rendered
   bold there; body prose uses no bold (per spec).
8. **`##` subheads** — not covered by the spec; set as 10 pt Baskerville SemiBold,
   synthesized small caps, on the 10 pt grid (spaceBefore 9), keepWithNext.
9. **Edition line** — new editorial text, Baskerville Regular 9 pt, centered at
   baseline 43: "Working manuscript draft · 2026".
10. **TOC entry added** — "Notes and Sources" is not in the manuscript's TOC list
    but is included per the spec's structure (chapters + epilogue + Notes and
    Sources). TOC heading is Semibold 18 pt at the body-frame top (baseline
    422.58, ≈ 12 pt lower than the reference's heading).
11. **Title-page layout** (not fully specified) — mirrors the reference placement:
    title 18 pt SemiBold sheared, baseline 297; subtitle split over two 14 pt lines
    ("A Retreat with" / "Fr. Peter Gruber, C.O.") at baselines 275/252 because the
    single line (241.85 pt) exceeds the 234 pt measure; author line "by Fr. Peter
    Gruber, C.O." 14 pt at baseline 229; all left-aligned at x=36.
12. **Justification** — body set justified per spec ("assume justified"); no
    evidence of ragged-right found in the reference (right-edge widths could not be
    conclusively extracted from its Type-1 subsets).
13. **Block quotes** — `>` prayers: Regular 10 pt, left indent 18 pt, justified
    (editorial choice per spec note); attributions inside quotes right-aligned
    italic 9 pt. Standalone `*italic*` prayers: Italic 10 pt, left indent 18 pt.
14. **Chapter-title shrink-to-fit** — fallback coded (scale 13 pt if the
    small-caps title exceeds 234 pt); not triggered: longest title measures
    200.3 pt at 13 pt.
15. **reportlab 5.0.1 first-baseline behavior** — the first paragraph baseline
    lands at `frame_top − fontSize` (not `− ascent`); frame tops were calibrated
    accordingly (440.58/462.58) and verified against the built PDF.
16. **Front-matter heads** — "Note on the Text" and "Notes and Sources" use the
    chapter-opener treatment (small-caps bold 13 pt at 449.58); the running-head
    rule (head only on opener pages) is satisfied by the title line itself, as in
    the reference.

## Build command

```
python3 manuscript/build_pdf.py   # two-pass; pass A anchors pages, pass B adds
                                  # odd-page blanks + final TOC numbers
python3 manuscript/verify_pdf.py  # 19/19 checks
```

## Result

- `manuscript/Mystery_of_the_Trinity.pdf` — **93 pages**.
- Chapter starts (all odd): Ch.1 p.5, Ch.2 p.17, Ch.3 p.27, Ch.4 p.37, Ch.5 p.45,
  Ch.6 p.55, Epilogue p.63, Notes and Sources p.83. Title p.1 (unnumbered),
  Note on the Text p.2, TOC p.3. Blank pages: 4, 26, 36, 44.
- Build log (`manuscript/build_log.txt`): no warnings, no glyph/substitution
  errors. Embedded fonts: Baskerville-0/-Bold-1/-Italic-2/-SemiBold-4 subsets
  (plus an unused default /Helvetica initial-state entry per page — no text drawn).
