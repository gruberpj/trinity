#!/usr/bin/env python3
"""Self-check for Mystery_of_the_Trinity.pdf against the reference spec."""

import re
import sys
from pathlib import Path

from pypdf import PdfReader

PDF = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.pdf"

failures = []
checks = []


def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    if not ok:
        failures.append(name)


def frags(page):
    """List of (x, y, text) fragments in device space (cm applied)."""
    out = []

    def v(t, cm, tm, fd, fs):
        x = cm[4] + tm[4]
        y = cm[5] + tm[5]
        if t.strip() and y > 0:
            out.append((x, y, t))

    page.extract_text(visitor_text=v)
    return out


def lines_by_y(page):
    groups = {}
    for x, y, t in frags(page):
        groups.setdefault(round(y, 1), []).append((x, t))
    return sorted(groups.items(), reverse=True)


def norm(text):
    return re.sub(r"\s+", " ", text or "")


def main():
    r = PdfReader(str(PDF))
    pages = r.pages
    n = len(pages)

    # 1. page size + count
    sizes_ok = all(
        abs(float(p.mediabox.width) - 306.0) < 0.1 and abs(float(p.mediabox.height) - 495.0) < 0.1
        for p in pages
    )
    check("all pages 306x495 pt", sizes_ok, f"{n} pages")
    check("page count in 85..110", 85 <= n <= 110, str(n))

    # 2. spot text extraction (normalized)
    p1 = norm(pages[0].extract_text())
    check(
        "page 1: title/author/edition",
        all(
            s in p1
            for s in (
                "The Mystery of the Trinity",
                "A Retreat with Fr. Peter Gruber, C.O.",
                "by Fr. Peter Gruber, C.O.",
                "Working manuscript draft",
            )
        ),
        p1[:100],
    )
    p2 = norm(pages[1].extract_text()).upper()
    check(
        "page 2: Note on the Text",
        "NOTE ON THE TEXT" in p2 and "MACHINE-TRANSCRIBED" in p2,
        p2[:100],
    )
    p3 = norm(pages[2].extract_text())
    check(
        "page 3: TOC heading + entries",
        "Table of Contents" in p3 and "Chapter 1" in p3 and "Notes and Sources" in p3,
        p3[:100],
    )
    p5 = norm(pages[4].extract_text()).upper()
    check(
        "page 5: chapter 1 opener (small caps)",
        "CHAPTER 1" in p5 and "ICONS OF THE TRINITY" in p5 and "OPENING PRAYER" in p5,
        p5[:100],
    )
    mid = norm(pages[n // 2].extract_text())
    check("middle page: body text present", len(mid) > 200, mid[:60])
    plast = norm(pages[-1].extract_text())
    check("last page: notes tail", "Judges 4:21" in plast or "St. Augustine" in plast, plast[-100:])

    # 3. TOC page numbers vs actual chapter starts
    expected = {
        "Chapter 1 — Icons of the Trinity": 5,
        "Chapter 2 — Mystery": 17,
        "Chapter 3 — Gift and Liturgy": 27,
        "Chapter 4 — Relationship": 37,
        "Chapter 5 — Intimacy": 45,
        "Chapter 6 — Evangelization": 55,
        "Epilogue — Engineering Mystery": 63,
        "Notes and Sources": 83,
    }
    toc = {}
    for y, fs in lines_by_y(pages[2]):
        left = " ".join(t for x, t in fs if x < 100).strip()
        right = "".join(t for x, t in fs if x >= 100)
        m = re.search(r"(\d+)\s*$", right)
        if m and left:
            toc[left] = int(m.group(1))
    matched = sum(1 for k, want in expected.items() if toc.get(k) == want)
    for k, want in expected.items():
        if toc.get(k) != want:
            check(f"TOC entry {k!r} -> {toc.get(k)} (want {want})", False)
    check("TOC page numbers match chapter starts (>=3)", matched >= 3, f"{matched}/{len(expected)}")
    print("  TOC parsed:", toc)

    # 4. baselines
    l5 = lines_by_y(pages[4])
    ys5 = [y for y, _ in l5]
    check(
        "page 5: chapter title baseline ~449.58",
        any(abs(y - 449.58) < 0.5 for y in ys5),
        str(ys5[:3]),
    )
    check(
        "page 5: first body baseline ~430.58",
        any(abs(y - 430.58) < 0.5 for y in ys5),
        str(ys5[:3]),
    )
    l6 = lines_by_y(pages[5])
    body6 = [y for y, _ in l6 if y > 40]
    check("page 6: first body baseline ~430.58", abs(body6[0] - 430.58) < 0.5, str(body6[0]))
    pn_ok = True
    for idx in (1, 2, 4, n // 2, n - 1):
        ys = [y for y, _ in lines_by_y(pages[idx]) if y < 25]
        if not any(abs(y - 18.0) < 0.5 for y in ys):
            pn_ok = False
            check(f"page {idx + 1}: page number at baseline ~18", False, str(ys))
    check("page numbers at baseline ~18 (sampled)", pn_ok)
    t1 = [y for y, _ in lines_by_y(pages[0]) if y < 25]
    check("page 1: no page number", not t1, str(t1))

    # 5. fonts embedded
    font_names = set()
    for idx in (0, 2, 4, n // 2, n - 1):
        res = pages[idx].get("/Resources", {})
        for v in res.get("/Font", {}).values():
            font_names.add(str(v.get_object().get("/BaseFont")))
    print("  embedded fonts:", sorted(font_names))
    check("Baskerville subsets embedded", any("Baskerville" in f for f in font_names))

    # 6. verbatim probes (whitespace-normalized full text)
    all_text = norm(" ".join(norm(p.extract_text()) for p in pages))
    for probe in (
        "I bind unto myself the name, the strong name of the Trinity",
        "pregnant with intelligibility",
        "Go, set the world on fire",
        "Late have I loved you, O Beauty ever ancient, ever new",
    ):
        check(f"verbatim probe {probe[:34]!r}...", probe in all_text)

    print()
    print(f"CHECKS: {sum(1 for _, ok, _ in checks if ok)}/{len(checks)} passed")
    if failures:
        print("FAILED:", *failures, sep="\n  ")
        sys.exit(1)
    print("ALL CHECKS PASSED — page count:", n)


if __name__ == "__main__":
    main()
