# MGS Booklet Cover — Style Spec (for the new "Mystery of the Trinity" cover)

Source: `cover Apr 2026 MGS booklet.pdf` (1 page, 83 MB). Extracted with pypdf 6.16.2
(hand-rolled content-stream tokenizer + `visitor_text`), positions/rendering verified
against MuPDF 1.26 render; colors measured by pixel-sampling the rendered page
(no color operators exist in the content stream, so stream-only color analysis
reports nothing — see §4).

## 1. Page geometry

| Property | Value | Notes |
|---|---|---|
| Pages | 1 | single spread: back + spine + front in one page |
| MediaBox/TrimBox/CropBox/BleedBox/ArtBox | all **645.36 × 513.12 pt** | **8.9633 × 7.1267 in**; no separate bleed box |
| Interior trim (from MGS interior spec) | 306.0 × 495.0 pt | 4.25 × 6.875 in |
| Cover height | 513.12 pt | 495 + 18.12 ≈ 6.875 + 0.25 in (≈⅛ in top/bottom bleed) |
| Spine width | **33.36 pt (0.463 in)** — INFERRED | 645.36 − 2×306; consistent with the 80-pp interior (~0.0058 in/sheet) |
| Panel zones (INFERRED from trim geometry) | back [0, 306] · spine [306, 339.36] · front [339.36, 645.36] pt | artwork seam in the imagery sits at x ≈ 315 pt (not aligned to the spine edges) |
| Page /Rotate | none | — |
| Producer | "Adobe Photoshop for Macintosh -- Image Conversion Plug-in" (Creator: Adobe Photoshop 25.12) | the cover is a Photoshop export, not an InDesign layout |

## 2. Construction (how the cover is built)

- **Everything is raster**: 16 CMYK JPEG layers (2689 × 2138 px, /DCTDecode, 8 bpc), each
  placed with the identical full-page CTM `[645.36 0 0 513.12 0 0]`.
- `Im0` = full-bleed base layer (the dark background + artwork); `Im1…Im15` are masked
  layers (8 clip regions: back panel `[-19.4..315.1]×[-21.1..513.1]`, front panel
  `[315.1..645.1]×[0..513.1]`, a framed panel on the back `[44.5..280.2]×[128.9..469.4]`,
  and a small logo zone `[126.8..198.4]×[28.9..55.3]`).
- **Live text exists but is not painted directly**: all 10 text blocks set `7 Tr`
  (rendering mode 7 = add to clipping path), then a following image `Do` paints an image
  layer *through the glyph outlines*. Visible "text" color therefore comes from image
  layers, not from stream color operators.
- **No fill/stroke color operators anywhere** in the stream (no rg/RG/k/K/g/G/scn/SCN) —
  the only color source is the imagery. Text is emitted per-glyph (`Tj` per glyph,
  CID-encoded strings with a ToUnicode CMap; `Td` offsets in glyph space, scaled by the
  text-matrix axes).
- Text blocks are double-drawn (Bold + Medium of the same line overlaid — a faux-bold
  technique); the blurb paragraphs are emitted twice as well.

## 3. Fonts (by role)

All Type0 `/Identity-H` subset fonts (CIDs mapped via ToUnicode). `Tf` size is 1.0;
real size is carried by the text-matrix scale × page height.

| Role | Font | Effective size (MuPDF-verified) | Text-matrix scale | Color (see §4) |
|---|---|---|---|---|
| Front title "Marian Meditations for May" | **Vatican-Bold** (+ Vatican-Medium 24.69 pt overlay) | ≈ **25.98 pt** | [0.04, 0, −0.0, 0.05] | light blue |
| Front author "St. John Henry Newman" | **Vatican-Bold** (+ Vatican-Medium overlay) | **18.0 pt** | [0.03, 0, −0.0, ~0.035] | light blue |
| Front publisher "The Pittsburgh Oratory" | **Vatican-Medium** | **14.0 pt** | [~0.02, 0, 0, ~0.027] | cream |
| Back blurb paragraphs | **AGaramondPro-Regular** | **11.0 pt** | [0.01704, 0, 0, 0.02144] | white |
| Back "About the Author" heading | **AGaramondPro-Bold** | 11.0 pt | — | white |
| Back author bio | **AGaramondPro-Regular** | 10.0 pt | — | white |
| Back address block | **AGaramondPro-Regular** | 8.0 pt | — | white |

Note: the "Vatican" display face is not a system font on macOS; see matching plan §7.

## 4. Colors (pixel-sampled from the render at 150–200 dpi)

No color operators in the stream — all color values below are measured from the
rasterized page (dominant colors per zone).

| Element | RGB | Hex | Notes |
|---|---|---|---|
| Background (entire spread incl. spine) | (42, 38, 37) | **#2A2625** | very dark warm near-black, uniform |
| Back text (blurb, bio, address, logo glyph) | (255, 255, 255) | **#FFFFFF** | pure white |
| Front title + author | (116, 147, 204) | **#7493CC** | light Marian blue; icon halo shares this blue |
| Front publisher line | (243, 232, 213) | **#F3E8D5** | cream / parchment |
| Spine | (42, 38, 37) + faint (11–13, 13–15, 23–28) | #2A2625 / #0C0E1A | dark, no spine text |
| Icon: robe (lower) | (12, 14, 26) | #0C0E1A | dark navy |
| Icon: warm passages (upper/mid) | (113, 77, 41) / (212, 184, 145) | #714929 / #D4B891 | ochre/gold |
| Icon: faces | (75, 38, 25) | #4B2619 | dark reddish brown |

Overall look: near-black field, one dark iconic image, small white text — a
"dark devotional icon" cover.

## 5. Zones (device coordinates, pt, PDF y-up)

| Zone | x-range | y (baselines) | Content |
|---|---|---|---|
| Front title | 341.15 – 635.8 | 464.83 | "Marian Meditations for May", Vatican-Bold ~26 pt, blue; near top of front panel (bbox top ≈ 25 pt from top edge), nearly full panel width |
| Front author | 344.6 – 518.2 | 439.7 | "St. John Henry Newman", 18 pt, blue; ~11 pt below title |
| Front publisher | 508.7 – 638.6 | ~30.2 | "The Pittsburgh Oratory", Vatican-Medium 14 pt, cream, bottom-right of front panel |
| Back blurb | 44.58 – 291.1 | 461.7 → 230.7 | 11 pt white, 11 pt leading; 3 paragraphs; block starts ~34 pt below top trim |
| Back "About the Author" | 44.58 | 197.7 | AGaramondPro-Bold 11 pt |
| Back author bio | 44.59 | 186.7 → 131.7 | 10 pt, 11 pt leading |
| Back address block | 125.6 – 199.7 | 49.35 / 39.75 / 30.15 | 8 pt white: logo glyph + "The Pittsburgh Oratory" · "4450 Bayard Street" · "Pittsburgh, PA 15213", bottom-center |
| Spine | 306 – 339.4 | — | no text (dark field) |

Back text column: left inset 44.6 pt from the spread edge (≈35.5 pt from the
back-panel trim at x=9 bleed edge), right edge ≈ 291 pt.

## 6. Full extracted text (back cover)

> Enter into the month of May with these daily meditations on the Blessed Virgin Mary
> by St. John Henry Newman, Oratorian, Cardinal, and Doctor of the Church. Each day
> offers a brief meditation on a title of Mary drawn from the Litany of Loreto, inviting
> the reader to contemplate her privileges, her virtues, and her maternal care.
>
> These thirty-two meditations form part of an unfinished "Year-Book of Devotion" that
> Newman began for reading and meditation according to the seasons and feasts of the
> year. Though never completed, his reflections on Our Lady stand as a coherent and
> luminous whole – at once theologically rich and devotional,ly profound
>
> Written for prayer rather than study, these meditations are well suited for daily
> reading throughout May, whether in the quiet of the morning or before the Blessed
> Sacrament. They help the reader understand Marian devotion from within: not as mere
> sentiment, but as a path to Christ through the one who bore Him.
>
> About the Author
> St. John Henry Newman (1801–1890) was an English convert to the Catholic faith, priest
> of the Oratory of St. Philip Neri, cardinal of the Roman Catholic Church, and recently
> declared Doctor of the Church. His sermons and writings continue to guide readers
> toward a deeper, more personal knowledge of Christ.
>
> [logo glyph] The Pittsburgh Oratory · 4450 Bayard Street · Pittsburgh, PA 15213

("devotional,ly" as extracted — the comma is an artifact of the double-drawn line
overlap in the source PDF, not a typo to reproduce.)

## 7. "Similar look" plan for the new cover ("Mystery of the Trinity")

Strictly from the extracted data:

1. **Geometry**: same spread — 645.36 × 513.12 pt, 4.25 × 6.875 in panels, spine width
   computed from the final page count (MGS 80 pp → 33.36 pt; formula ≈ 0.0058 in × pages).
2. **Background**: full-bleed near-black **#2A2625** (RGB 42,38,37) — dark/neutral field.
3. **Artwork**: centered icon image on the front panel, filling most of the panel
   (the MGS icon spans the full panel width, top to bottom) — Rublev's *Trinity*
   (acquired in Part 2) fits the same dark-icon language: deep blues, warm ochres,
   near-black background. Front panel = image only, no text on the artwork except the
   title band at top.
4. **Title**: at the top of the front panel (baseline ≈ 465 pt, i.e. ~25–33 pt below the
   top trim), nearly full panel width, ~26 pt display face in **light blue #7493CC**
   (or white if the blue clashes with the Rublev blues); author line ~11 pt below at
   18 pt, same blue.
5. **Minimal text**: front carries only title + author + small cream **#F3E8D5**
   publisher line at bottom-right (14 pt). Spine: keep blank (as MGS) unless the final
   page count demands spine text.
6. **Back cover**: white text on the dark field — a blurb block starting ≈ 34 pt below
   the top trim at x ≈ 44.6 pt, 11 pt body / ~10–11 pt leading, plus a small bottom-
   center address block (8 pt).
7. **Fonts**: "Vatican" is not installed on macOS — no exact match. Use
   **Baskerville** (project's standing AGaramondPro stand-in) or a Trajan-like incised
   display face for the title; AGaramondPro Regular/Bold for back-cover text
   (consistent with the interior). Colors carried exactly (#7493CC title, #F3E8D5
   publisher, #FFFFFF back text, #2A2625 field).

## 8. Uncertainties

1. Spine width 33.36 pt is INFERRED from 645.36 − 2×306 (consistent with the 80-pp
   interior); the PDF carries no explicit panel/spine marks.
2. Text colors are pixel-sampled from the render (no stream color ops); title blue
   #7493CC is also the icon-halo color, so the two cannot be separated at the stream
   level (zone sampling of glyph flanks confirms the glyphs are #7493CC).
3. Cover is a Photoshop layer export; per-layer content (which of Im1…Im15 paints the
   title/author/address) was not attributed layer-by-layer.
4. Front title ~26 pt / author 18 pt from MuPDF; pypdf text-matrix scales give
   ≈25.7 pt for the title (rounding of the 0.05 scale).
5. Rendering was characterized programmatically (pixel sampling + ASCII luminance map);
   **a human visual check of the rendered spread is recommended** (the analyzing model
   cannot view images).
