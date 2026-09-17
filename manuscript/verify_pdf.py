#!/usr/bin/env python3
"""Self-check for Mystery_of_the_Trinity.pdf against the flowing-layout spec.

Layout under test (manuscript/build_pdf.py):
  - title page and Table of Contents keep their own pages (1 and 3);
    everything else — Note on the Text, chapters, epilogue, Notes and
    Sources — flows continuously, no forced odd-page starts, no blanks.
  - chapter/epilogue/notes headings render as one-line small caps
    (extraction yields inter-letter spacing, so heading matching strips
    all whitespace).
  - prayers are italic, indented blockquotes with no "Opening Prayer" /
    "Closing Prayer" subheadings.

Expected failures against the current STALE PDF (old fixed-page layout,
"OPENING PRAYER" subheading, pre-Pusey Augustine wording): the prayer-
heading absence check and the Augustine verbatim probe. Everything else
(page size, dynamic TOC-vs-actual page numbers, dot leaders, baselines,
fonts) is layout-independent and should pass on both.
"""

import re
import sys
from pathlib import Path

from pypdf import PdfReader

PDF = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.pdf"

TOC_PAGE_INDEX = 2  # title = page 1, Note on the Text = page 2, TOC = page 3

# Heading lines with all whitespace removed (small caps + inter-letter gaps).
HEAD_RE = re.compile(r"^(CHAPTER\d+—.+|EPILOGUE—.+|NOTESANDSOURCES)$")
PRAYER_HEAD_RE = re.compile(r"^(OPENINGPRAYER|CLOSINGPRAYER)$")

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


def strip_ws(text):
    """Uppercase with all whitespace removed — robust against the inter-letter
    spacing that small-caps extraction introduces."""
    return re.sub(r"\s+", "", text or "").upper()


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
    check("page count in 85..125", 85 <= n <= 125, str(n))

    # 2. spot text extraction (normalized)
    p1 = norm(pages[0].extract_text())
    check(
        "page 1: title/author/edition",
        all(
            s in p1
            for s in (
                "The Mystery of the Trinity",
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
    p3 = norm(pages[TOC_PAGE_INDEX].extract_text())
    check(
        "page 3: TOC heading + entries",
        "Table of Contents" in p3 and "Chapter 1" in p3 and "Notes and Sources" in p3,
        p3[:100],
    )
    mid = norm(pages[n // 2].extract_text())
    check("middle page: body text present", len(mid) > 200, mid[:60])
    plast = norm(pages[-1].extract_text()) + " " + norm(pages[-2].extract_text())
    check("last page: notes tail", "Matthew 18:20" in plast or "Judges 4:21" in plast or "St. Augustine" in plast or "Athanasius" in plast, plast[-100:])

    # 3. dynamic heading extraction: first body page of every chapter,
    #    epilogue, and Notes and Sources (TOC page excluded). Also flags any
    #    leftover "Opening Prayer" / "Closing Prayer" heading line.
    heading_pages = {}  # stripped-upper heading text -> 1-based page
    prayer_pages = set()
    for i, page in enumerate(pages):
        if i == TOC_PAGE_INDEX:
            continue
        for y, fs in lines_by_y(page):
            line = " ".join(t for x, t in fs)
            key = strip_ws(line)
            if HEAD_RE.match(key) and key not in heading_pages:
                heading_pages[key] = i + 1
            if PRAYER_HEAD_RE.match(key):
                prayer_pages.add(i + 1)
    print("  heading pages:", heading_pages)

    ch1_key = strip_ws("Chapter 1 — Icons of the Trinity")
    if ch1_key in heading_pages:
        ch1_text = strip_ws(pages[heading_pages[ch1_key] - 1].extract_text())
        check(
            "chapter 1 opener (small caps) on its page",
            "CHAPTER1" in ch1_text and "ICONSOFTHETRINITY" in ch1_text,
            f"page {heading_pages[ch1_key]}",
        )
    else:
        check("chapter 1 heading found in body", False, "not found")

    # 4. TOC entries vs actual heading pages
    toc = {}
    dot_leaders_ok = True
    for y, fs in lines_by_y(pages[TOC_PAGE_INDEX]):
        left = " ".join(t for x, t in fs if x < 100).strip()
        right = "".join(t for x, t in fs if x >= 100)
        if not left:
            continue
        m = re.search(r"(\d+)\s*$", right)
        if m:
            toc[left] = int(m.group(1))
            if "." not in right:
                dot_leaders_ok = False
    print("  TOC parsed:", toc)
    check("TOC entries have dot leaders", dot_leaders_ok)

    matched = 0
    for label, printed in toc.items():
        actual = heading_pages.get(strip_ws(label))
        if actual is None:
            check(f"TOC entry {label!r}: no heading found in body", False)
        elif actual != printed:
            check(f"TOC entry {label!r}: printed {printed}, actual {actual}", False)
        else:
            matched += 1
    for key, page_no in heading_pages.items():
        if not any(strip_ws(label) == key for label in toc):
            check(f"heading {key!r} (page {page_no}) missing from TOC", False)
    check(
        "TOC page numbers match actual heading pages",
        bool(toc) and matched == len(toc),
        f"{matched}/{len(toc)}",
    )

    # 5. prayers carry no subheadings
    check(
        "no Opening/Closing Prayer headings",
        not prayer_pages,
        f"pages {sorted(prayer_pages)}" if prayer_pages else "none",
    )

    # 6. baselines: page numbers only (body top varies in flowing layout)
    pn_ok = True
    for idx in (1, 2, 4, n // 2, n - 1):
        ys = [y for y, _ in lines_by_y(pages[idx]) if y < 25]
        if not any(abs(y - 18.0) < 0.5 for y in ys):
            pn_ok = False
            check(f"page {idx + 1}: page number at baseline ~18", False, str(ys))
    check("page numbers at baseline ~18 (sampled)", pn_ok)
    t1 = [y for y, _ in lines_by_y(pages[0]) if y < 25]
    check("page 1: no page number", not t1, str(t1))

    # 7. fonts embedded
    font_names = set()
    for idx in (0, 2, 4, n // 2, n - 1):
        res = pages[idx].get("/Resources", {})
        for v in res.get("/Font", {}).values():
            font_names.add(str(v.get_object().get("/BaseFont")))
    print("  embedded fonts:", sorted(font_names))
    check("Baskerville subsets embedded", any("Baskerville" in f for f in font_names))

    # 8. verbatim probes (whitespace-normalized full text)
    all_text = norm(" ".join(norm(p.extract_text()) for p in pages))
    for probe in (
        "I bind unto myself the name, the strong name of the Trinity",
        "pregnant with intelligibility",
        "Go, set the world on fire",
        "Too late loved I Thee, O Thou Beauty of ancient days",
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
