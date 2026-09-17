#!/usr/bin/env python3
"""Final cover analysis for 'cover Apr 2026 MGS booklet.pdf'.

Method (pypdf, per MGS style-spec convention): hand-rolled content-stream
tokenizer for text runs (font/size/color/position), color operators, rect
fills, clip regions and image Do placement; ToUnicode CMaps parsed for CID
text. Positions cross-checked against MuPDF rendering.
"""
import re
from collections import Counter

from pypdf import PdfReader

PDF = "/Users/fr.peter/OpenCode/Mystery of the Trinity/cover Apr 2026 MGS booklet.pdf"

reader = PdfReader(PDF)
page = reader.pages[0]

# ------------------------------------------------------------------ boxes
print("=== boxes (pt) ===")
for name in ("mediabox", "trimbox", "cropbox", "bleedbox", "artbox"):
    b = getattr(page, name)
    print(f"  {name:9s}: [{b.left:.2f} {b.bottom:.2f} {b.right:.2f} {b.top:.2f}] "
          f"w={b.width:.2f} h={b.height:.2f} ({b.width / 72:.4f} x {b.height / 72:.4f} in)")

W, H = float(page.mediabox.width), float(page.mediabox.height)

# ---------------------------------------------------------------- resources
res = page["/Resources"]
fonts_res = {str(k): v.get_object() for k, v in res["/Font"].items()}
xobjects = res["/XObject"]

FONT_NAMES = {}
for k, fo in fonts_res.items():
    bf = str(fo.get("/BaseFont"))
    desc = fo.get("/DescendantFonts")
    FONT_NAMES[k] = bf
    print(f"font {k}: {bf}" + (f"  desc={desc[0].get_object().get('/BaseFont')}" if desc else ""))


def parse_tounicode(fo):
    """Return {cid_int: unicode_str} from a Type0 font's ToUnicode CMap."""
    cmap = {}
    fo = fo if fo is not None else None
    src = None
    for cand in (fo,):
        if cand is None:
            break
        tu = cand.get("/ToUnicode")
        if tu:
            try:
                src = tu.get_object().get_data().decode("latin-1")
            except Exception:  # noqa: BLE001
                src = None
            break
        desc = cand.get("/DescendantFonts")
        if desc:
            d0 = desc[0].get_object()
            tu2 = d0.get("/ToUnicode")
            if tu2:
                try:
                    src = tu2.get_object().get_data().decode("latin-1")
                except Exception:  # noqa: BLE001
                    src = None
    if not src:
        return cmap
    bfchar = re.findall(r"beginbfchar(.*?)endbfchar", src, re.S)
    for block in bfchar:
        for m in re.finditer(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            cmap[int(m.group(1), 16)] = "".join(
                chr(int(m.group(2)[i:i + 4], 16)) for i in range(0, len(m.group(2)), 4))
    bfrange = re.findall(r"beginbfrange(.*?)endbfrange", src, re.S)
    for block in bfrange:
        for m in re.finditer(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            lo, hi, start = int(m.group(1), 16), int(m.group(2), 16), int(m.group(3), 16)
            for cid in range(lo, hi + 1):
                cmap[cid] = chr(start + (cid - lo))
    return cmap


TOUNICODE = {k: parse_tounicode(v) for k, v in fonts_res.items()}


def cid_text(font_key, raw):
    """Decode a 2-byte-CID text-showing string via ToUnicode."""
    cmap = TOUNICODE.get(font_key, {})
    bs = raw.encode("latin-1")
    out = []
    for i in range(0, len(bs) - 1, 2):
        cid = (bs[i] << 8) | bs[i + 1]
        out.append(cmap.get(cid, f"<{cid:04x}>"))
    return "".join(out)


# ------------------------------------------------------------------ tokenizer
TOKEN_RE = re.compile(
    r"""
      (?P<ws>\s+)
    | (?P<num>[+-]?(?:\d+\.?\d*|\.\d+))
    | (?P<name>/[A-Za-z0-9_.+#-]*)
    | (?P<lits>\((?:[^()\\]|\\.)*\))
    | (?P<hex><[0-9A-Fa-f\s]*>)
    | (?P<lb>\[) | (?P<rb>\]) | (?P<ld><<) | (?P<rd>>>)
    | (?P<kw>[A-Za-z"\'*]+)
    | (?P<bad>.)
    """,
    re.VERBOSE,
)


def unescape(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 1
            if i >= len(s):
                break
            e = s[i]
            if e in "nrtbf":
                out.append({"n": "\n", "r": "\r", "t": "\t", "b": "\b", "f": "\f"}[e])
            elif e in "()\\":
                out.append(e)
            elif e in "01234567":
                o, j = e, i + 1
                while j < len(s) and j < i + 3 and s[j] in "01234567":
                    o += s[j]
                    j += 1
                out.append(chr(int(o, 8)))
                i = j - 1
            elif e == "\n":
                pass
            else:
                out.append(e)
        else:
            out.append(c)
        i += 1
    return "".join(out)


data = page.get_object()["/Contents"].get_object().get_data().decode("latin-1")
toks = [(m.lastgroup, m.group()) for m in TOKEN_RE.finditer(data)]
n = len(toks)

ctm = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
font_key = None
font_size = 0.0
tm = None
tlm = None
in_text = False
text_runs = []
fills = []
dos = []
clip_bboxes = []
path_pts = []          # points of current path (user space)
pending_rect = None
colors_seen = Counter()
stack = []
op_count = Counter()

i = 0
while i < n:
    t, val = toks[i]
    if t != "kw":
        i += 1
        continue
    op = val
    j = i - 1
    ops = []
    while j >= 0:
        tj, vj = toks[j]
        if tj in ("ws", "bad"):
            j -= 1
            continue
        if tj == "num":
            ops.append(float(vj))
        elif tj in ("lits", "hex"):
            ops.append(vj)
        elif tj == "name":
            ops.append(vj)
        elif tj == "rb":
            ops.append("]")
        else:
            break
        j -= 1
    ops.reverse()
    i += 1
    op_count[op] += 1

    def dev(x, y):
        return ctm[0] * x + ctm[2] * y + ctm[4], ctm[1] * x + ctm[3] * y + ctm[5]

    if op == "q":
        stack.append((ctm[:], font_key, font_size, tm, tlm))
    elif op == "Q":
        if stack:
            ctm, font_key, font_size, tm, tlm = stack.pop()
    elif op == "cm" and len(ops) == 6:
        a, b, c, d, e, f = ops
        ctm = [ctm[0] * a + ctm[2] * b, ctm[1] * a + ctm[3] * b,
               ctm[0] * c + ctm[2] * d, ctm[1] * c + ctm[3] * d,
               ctm[0] * e + ctm[2] * f + ctm[4], ctm[1] * e + ctm[3] * f + ctm[5]]
    elif op == "rg" and len(ops) == 3:
        colors_seen[f"rgb{tuple(ops)}"] += 1
    elif op == "RG" and len(ops) == 3:
        colors_seen[f"RGB{tuple(ops)}"] += 1
    elif op == "g" and len(ops) == 1:
        colors_seen[f"gray{ops[0]}"] += 1
    elif op == "G" and len(ops) == 1:
        colors_seen[f"GRAY{ops[0]}"] += 1
    elif op == "k" and len(ops) == 4:
        colors_seen[f"cmyk{tuple(ops)}"] += 1
    elif op == "K" and len(ops) == 4:
        colors_seen[f"CMYK{tuple(ops)}"] += 1
    elif op in ("scn", "sc", "SCN", "SC") and ops:
        colors_seen[f"{op}{ops}"] += 1
    elif op in ("m", "l") and len(ops) == 2:
        path_pts.append(dev(ops[0], ops[1]))
    elif op in ("c", "v", "y"):
        pass
    elif op == "re" and len(ops) == 4:
        pending_rect = ops
    elif op in ("f", "f*", "B", "b", "B*", "b*", "n", "s", "S"):
        if pending_rect and op not in ("n", "s", "S"):
            x, y, w, h = pending_rect
            dx, dy = dev(x, y)
            fills.append((dx, dy, ctm[0] * w, ctm[3] * h, op))
        pending_rect = None
    elif op in ("W", "W*"):
        if path_pts:
            xs = [p[0] for p in path_pts]
            ys = [p[1] for p in path_pts]
            clip_bboxes.append((min(xs), min(ys), max(xs), max(ys), op))
        path_pts = []
    elif op == "h":
        pass
    elif op == "BT":
        in_text = True
        tm = None
        tlm = None
    elif op == "ET":
        in_text = False
    elif in_text:
        if op == "Tf" and len(ops) == 2:
            font_key, font_size = ops[0], ops[1]
        elif op == "Tm" and len(ops) == 6:
            tm = ops[:]
            tlm = ops[:]
        elif op in ("Td", "TD") and len(ops) == 2:
            tx, ty = ops[0], ops[1]
            if tlm is None:
                tlm = [1, 0, 0, 1, 0, 0]
            a, b, c, d = tlm[0], tlm[1], tlm[2], tlm[3]
            # NOTE: this export puts Td offsets in glyph space; renderers
            # (pypdf/MuPDF) scale them by the text-matrix axes:
            tlm = [a, b, c, d, tlm[4] + tx * a + ty * c, tlm[5] + tx * b + ty * d]
            tm = tlm[:]
            if op == "TD":
                pass  # leading not used here
        elif op == "Tj" and ops and isinstance(ops[0], str):
            raw = unescape(ops[0][1:-1])
            if raw:
                fx = (tm or [0, 0, 0, 0, 0, 0])[4]
                fy = (tm or [0, 0, 0, 0, 0, 0])[5]
                dx, dy = dev(fx, fy)
                a, b, c, d = (tm or [0, 0, 0, 0])[:4]
                eff = font_size * (abs(d) or abs(a) or 1.0) * ((ctm[3] ** 2 + ctm[1] ** 2) ** 0.5 or 1.0)
                text_runs.append((cid_text(font_key, raw), dx, dy, font_key, eff))
    elif op == "Do" and ops:
        dos.append((ops[0], dev(0, 0), ctm[:]))

print(f"\n=== op histogram: {dict(op_count)}")
print(f"=== color ops seen: {dict(colors_seen) if colors_seen else 'NONE (all text default black)'}")
print(f"=== filled rects: {fills if fills else 'NONE'}")
print(f"\n=== Do placements ({len(dos)}) ===")
for name, (dx, dy), m in dos:
    print(f"  {name}: origin=({dx:.2f},{dy:.2f}) scale=({m[0]:.2f},{m[3]:.2f})")
print(f"\n=== clip regions ({len(clip_bboxes)}) ===")
for b in clip_bboxes:
    print(f"  x [{b[0]:.3f}..{b[2]:.3f}] y [{b[1]:.3f}..{b[3]:.3f}]  {b[4]}")

print(f"\n=== text runs ({len(text_runs)}) ===")
for text, dx, dy, fk, eff in text_runs:
    print(f"  x={dx:7.2f} y={dy:7.2f} size={eff:6.2f} font={FONT_NAMES.get(fk, fk):28s} '{text}'")

# ---------------------------------------------------------------- line groups
lines = []
for text, dx, dy, fk, eff in text_runs:
    placed = False
    for ln in lines:
        if abs(ln[1] - dy) < 2.0:
            ln[0].append((dx, text, fk, eff))
            placed = True
            break
    if not placed:
        lines.append([[(dx, text, fk, eff)], dy, None])
for ln in lines:
    ln[0].sort(key=lambda r: r[0])
    line_text = "".join(r[1] for r in ln[0])
    ln[2] = line_text

print(f"\n=== reconstructed lines ({len(lines)}) ===")
for runs, y, text in sorted(lines, key=lambda l: -l[1]):
    x0 = runs[0][0]
    fk = Counter(r[2] for r in runs).most_common(1)[0][0]
    eff = runs[0][3]
    print(f"  y={y:7.2f} x={x0:7.2f} size={eff:5.2f} font={FONT_NAMES.get(fk, fk):28s} '{text}'")

# ---------------------------------------------------------------- images
print("\n=== XObject images ===")
for name, ref in xobjects.items():
    xo = ref.get_object()
    print(f"  {name}: {xo.get('/Width')}x{xo.get('/Height')} {xo.get('/ColorSpace')} "
          f"filter={xo.get('/Filter')} bpc={xo.get('/BitsPerComponent')}")
