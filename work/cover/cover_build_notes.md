# Cover Build Notes — "The Mystery of the Trinity" (Lulu print-ready)

Built by `build_cover.py` → `Mystery_of_the_Trinity_cover.pdf` (single page).

## Dimensions (in)
- Trim: 4.25 × 6.875 (82 pages, B&W). Bleed: 0.125 all sides.
- Spine = 82 × 0.002252 = **0.1847**.
- Full spread: **8.9347 × 7.125** (verified mediabox 8.9347 × 7.1250).
- Panel x-zones: back [0.125, 4.375] · spine [4.375, 4.5597] · front [4.5597, 8.8097].

## Front panel — full-bleed artwork (new approach, replaces centered inset)
- Rublev image fills the ENTIRE front panel edge-to-edge: x 4.5597–8.9347
  (spine boundary → right bleed edge) × y 0–7.125 (bottom → top bleed).
- Aspect preserved (no distortion): source 3231×4000 (aspect 0.80775)
  center-cropped horizontally to 2456×4000 (aspect 0.61400 vs target rect
  0.61404 — 0.006% rounding stretch, invisible) and drawn at exactly
  4.375 × 7.125. Effective ≈561 DPI source (≥300 required).
- Title + author OVERLAID on the image (not below it): title baseline 6.45,
  author 6.256 (14 pt below), centered on the front panel (cx 6.6847).

## Title color + overlay (measured decision, 2026-09-17)
- Reference blue **#7493CC REJECTED**: the icon's top band is the golden house
  (mean luminance L ≈ 0.30–0.36); blue (L ≈ 0.29) measures contrast 0.8–1.5
  against it — unreadable, and it stays <2.1 even under the dark overlay.
- **TITLE / AUTHOR = WHITE (#FFFFFF)** — consistent with the back-panel text.
- Subtle dark gradient baked into the raster (no PDF transparency → print-safe):
  #2A2625 at 72% opacity at the top edge, easing (^1.6) to 0 at 40% of the
  image height. Measured behind the actual glyphs: background mean L 0.132,
  p95 0.211 → white contrast mean 5.8 / p95 4.0 (WCAG AA large-text = 3.0);
  re-verified on the rendered PDF: mean 7.9 / p95 3.5. No /SMask, /CA, /ca,
  /BM operators in the file.

## Fonts (embedded subsets, /System/Library/Fonts/Supplemental/Baskerville.ttc)
- Title: Baskerville SemiBold (subfont 4), 23.5 pt — auto-fit from 26 pt to
  max width 4.0 in (26 pt overflows the panel; same as previous build).
- Author: Baskerville Regular (subfont 0), 18 pt.
- Back blurb: Baskerville Regular, 11 pt / 1.25 leading; final paragraph 10 pt.
- All fonts used by the content stream are subset-embedded
  (Baskerville-SemiBold-4, Baskerville-0).

## Colors (from style spec)
- Background/spine/back panel: #2A2625 · title/author/back text: #FFFFFF.
- Publisher/cream line (#F3E8D5): omitted per instructions.

## Back copy (updated per owner corrections)
- Para 1: "This book was derived from retreat talks given at three retreats in
  February and March of 2025."
- Para 2: unchanged long blurb ("Beginning with St. Patrick's shamrock …").
- Para 3: "…closes with a talk Fr. Peter gave at a retreat for engineering
  students…" (was "the talk Fr. Peter gave to engineering students").
- Source of truth: `back_cover_blurb.md` (updated to match).

## Layout (in, y-up)
- Back text: left margin 0.4 (x = 0.525), column width 3.45, first line
  y ≈ 6.55, block ends y ≈ 3.52 — all blurb text ≥ 0.125 in from trim edges.
- Spine: blank (dark field only).

## Approximations
1. Title 23.5 pt (auto-fit) rather than 26 pt — panel width constraint.
2. Leading 1.25×; paragraph gap ~0.45× leading.
3. Gradient strength (72% top, fade to 0 at 40% height) chosen from measured
   text-mask contrast; top of the icon (house gable) darkens slightly —
   intended, matches the dark-field reference look.
4. Front publisher line / back address block omitted (not requested).

## Verification (pypdf 6.16.2 + MuPDF 1.26)
- Pages: 1. Mediabox 8.9347 × 7.1250 in (exact, within 0.01).
- Image rect: x 4.5597–8.9347, y 0–7.125 in — right edge 8.9347 ≥ 8.8097
  (front trim edge 8.8097 and right bleed covered); left edge exactly at the
  spine boundary.
- Text extraction contains title, author, and updated blurb para 1.
- Fonts used are embedded (subset); no Helvetica stub resource (initial font
  set to Baskerville).
- Title/author spans: white (0xFFFFFF) @ 23.5 / 18 pt; blurb white @ 11 / 10 pt.
- All back-panel text ≥ 0.125 in from trim edges; spine has no text.

## Lulu upload checklist
1. Single-page PDF, exact 8.9347 × 7.125 in — matches the 4.25×6.875 +
   0.1847 spine template; no trim/crop marks.
2. Fonts embedded (subset) — yes; image is RGB JPEG (Lulu converts).
3. No transparency operators — overlay is baked into the raster.
