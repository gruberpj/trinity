#!/usr/bin/env python3
"""Build the Lulu print-ready cover PDF for 'The Mystery of the Trinity'.

Single-page spread (back + spine + front), 8.9347 x 7.125 in, no trim marks.
Vector text (Baskerville) over a full-bleed raster (Rublev Trinity) on the
front panel; a dark top gradient is baked into the raster (no PDF transparency).
"""
from pathlib import Path

import numpy as np
from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

WORK = Path("/Users/fr.peter/OpenCode/Mystery of the Trinity/work/cover")
OUT = WORK / "Mystery_of_the_Trinity_cover.pdf"
IMG = WORK / "rublev_trinity.jpg"
BLURB = WORK / "back_cover_blurb.md"
FRONT_CROP = WORK / "_front_panel_crop.jpg"  # derived raster, removed after build
BASKERVILLE = "/System/Library/Fonts/Supplemental/Baskerville.ttc"

# ---- geometry (inches, PDF y-up, origin bottom-left) -----------------------
PAGE_W = 8.9347           # 0.125 + 4.25 back + 0.1847 spine + 4.25 front + 0.125
PAGE_H = 7.125            # 6.875 trim + 0.125 top + 0.125 bottom bleed
SPINE_W = 0.1847          # 82 pages x 0.002252 in/page (Lulu)
TRIM_BACK_L = 0.125
TRIM_BACK_R = 4.375
TRIM_FRONT_L = 4.5597     # spine boundary -> front panel left edge
TRIM_FRONT_R = 8.8097
TRIM_TOP = 7.0
TRIM_BOT = 0.125

FRONT_W = PAGE_W - TRIM_FRONT_L   # 4.375  (trim 4.25 + right bleed 0.125)
FRONT_H = PAGE_H                  # 7.125  (trim 6.875 + top/bottom bleed)

# ---- colors ----------------------------------------------------------------
BG = HexColor("#2A2625")
WHITE = HexColor("#FFFFFF")

# ---- fonts -----------------------------------------------------------------
pdfmetrics.registerFont(TTFont("Baskerville", BASKERVILLE, subfontIndex=0))
pdfmetrics.registerFont(TTFont("Baskerville-SemiBold", BASKERVILLE, subfontIndex=4))

# ---- front-panel raster: center-crop to panel aspect + baked top gradient ---
def bake_front_raster() -> None:
    target_aspect = FRONT_W / FRONT_H
    src = Image.open(IMG).convert("RGB")
    sw, sh = src.size
    crop_w = int(round(sh * target_aspect))      # 2456 px
    x0 = (sw - crop_w) // 2                       # center-crop horizontally
    arr = np.asarray(src.crop((x0, 0, x0 + crop_w, sh)), dtype=np.float64)
    ch, cw = arr.shape[:2]
    # subtle dark gradient over the top 40% of the image (#2A2625 @ 72% -> 0)
    t = np.arange(ch, dtype=np.float64)[:, None] / ch
    base = np.clip(1.0 - t / 0.40, 0.0, 1.0)
    alpha = np.where(t < 0.40, 0.72 * base ** 1.6, 0.0)
    overlay = np.array([42.0, 38.0, 37.0])        # #2A2625
    arr = arr * (1.0 - alpha[:, :, None]) + overlay * alpha[:, :, None]
    Image.fromarray(arr.clip(0, 255).astype(np.uint8)).save(
        FRONT_CROP, "JPEG", quality=95, subsampling=2
    )
    print(f"front raster: src {sw}x{sh} -> crop {crop_w}x{sh} @x{x0} -> {FRONT_CROP}")


bake_front_raster()

# ---- blurb (verbatim from file) --------------------------------------------
blurb_paras = [
    ln.strip()
    for ln in BLURB.read_text(encoding="utf-8").splitlines()
    if ln.strip()
]

c = canvas.Canvas(str(OUT), pagesize=(PAGE_W * 72, PAGE_H * 72),
                  initialFontName="Baskerville", initialFontSize=11)
c.setTitle("The Mystery of the Trinity - cover")
c.setAuthor("Fr. Peter Gruber, C.O.")
c.setSubject("Print-ready cover spread (back + spine + front)")

# 1. dark field (back panel + spine; the front image covers the rest)
c.setFillColor(BG)
c.rect(0, 0, PAGE_W * 72, PAGE_H * 72, stroke=0, fill=1)

# 2. front panel: full-bleed artwork edge-to-edge (spine edge -> right bleed,
#    top/bottom bleed), aspect preserved via pre-crop
c.drawImage(FRONT_CROP, TRIM_FRONT_L * 72, 0, FRONT_W * 72, FRONT_H * 72)

# 3. title + author overlaid on the image (white; see cover_build_notes.md
#    for the measured rejection of the reference blue #7493CC)
front_cx = (TRIM_FRONT_L + TRIM_FRONT_R) / 2
title = "The Mystery of the Trinity"
author = "Fr. Peter Gruber, C.O."

title_size = 26.0
while title_size > 14 and pdfmetrics.stringWidth(title, "Baskerville-SemiBold", title_size) > 4.0 * 72:
    title_size -= 0.5

title_baseline = 6.45
author_baseline = title_baseline - 14 / 72.0

c.setFillColor(WHITE)
c.setFont("Baskerville-SemiBold", title_size)
c.drawCentredString(front_cx * 72, title_baseline * 72, title)
c.setFont("Baskerville", 18)
c.drawCentredString(front_cx * 72, author_baseline * 72, author)

# 4. back panel: blurb, white, left-aligned, 0.4 in margins, upper third start
body_x = TRIM_BACK_L + 0.4
body_w = TRIM_BACK_R - 0.4 - body_x
y = 6.55 * 72                    # cursor (upper third of back panel)
c.setFillColor(WHITE)
for i, para in enumerate(blurb_paras):
    size = 10 if i == len(blurb_paras) - 1 else 11   # final para smaller
    leading = size * 1.25
    c.setFont("Baskerville", size)
    lines = []
    words = para.split(" ")
    line = ""
    for w in words:
        trial = (line + " " + w).strip()
        if pdfmetrics.stringWidth(trial, "Baskerville", size) <= body_w * 72 or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    for ln in lines:
        c.drawString(body_x * 72, y, ln)
        y -= leading
    y -= leading * 0.45          # paragraph gap

end_y = y / 72
assert end_y >= TRIM_BOT + 0.125, f"blurb overflows bottom: end y {end_y:.2f} in"

c.showPage()
c.save()
FRONT_CROP.unlink()

print(f"wrote {OUT}")
print(f"page: {PAGE_W:.4f} x {PAGE_H:.4f} in; spine {SPINE_W:.4f} in")
print(f"title: {title_size:.1f} pt SemiBold white, baseline {title_baseline:.3f} in; "
      f"author 18 pt white, baseline {author_baseline:.3f} in")
print(f"front art rect (in): x {TRIM_FRONT_L:.4f}..{TRIM_FRONT_L + FRONT_W:.4f}, "
      f"y 0..{FRONT_H:.4f} (full bleed: spine edge -> right bleed, top -> bottom bleed)")
print(f"back text: x {body_x:.3f} in, width {body_w:.3f} in, end y {end_y:.2f} in")
