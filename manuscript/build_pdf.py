#!/usr/bin/env python3
"""
Build a print-interior PDF of "The Mystery of the Trinity" matching the
measured layout of 'MGS Booklet Jun 2025 interior.pdf' (306.0 x 495.0 pt).

Two-pass build:
  Pass A: build with dummy TOC page numbers; record the start page of every
          chapter (and Notes and Sources) via an afterFlowable hook.
  Pass B: rebuild with the real TOC.

Layout: the title page and the Table of Contents keep their own pages;
everything else (Note on the Text, chapters, epilogue, Notes and Sources)
flows continuously, one after another, with no forced page breaks.
Headings keep-with-next so a heading is never left alone at a page bottom.

Fonts: EB Garamond (bundled in manuscript/fonts/, SIL OFL 1.1), Georgia.ttf fallback.
"""

import contextlib
import io
import math
import re
import sys
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import portrait
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
)
from reportlab.platypus.tableofcontents import TableOfContents

# --------------------------------------------------------------------------
# Geometry (measured from the reference booklet; see PDF_build_notes.md)
# --------------------------------------------------------------------------
PAGE_W, PAGE_H = 306.0, 495.0
MARGIN = 36.0
TEXT_W = PAGE_W - 2 * MARGIN  # 234
BODY_TOP_BASELINE = 430.58     # first body-line baseline
BODY_LINES = 40
LEADING = 10.0
BODY_BOTTOM_BASELINE = BODY_TOP_BASELINE - (BODY_LINES - 1) * LEADING  # 40.58
PAGE_NUM_BASELINE = 18.0

BODY_FONT = "EBGaramond-Regular"
BOLD_FONT = "EBGaramond-Bold"
ITAL_FONT = "EBGaramond-Italic"
BOLD_ITAL_FONT = "EBGaramond-BoldItalic"

# EB Garamond hhea ascent = 1007/1000 em; reportlab 5.0.1 empirically places
# the first paragraph baseline at frame_top - fontSize (it falls back to
# fontSize for the line ascent), so frame tops are set to
# (desired baseline + fontSize) — geometry unchanged from the Baskerville build.
BODY_FRAME_TOP = BODY_TOP_BASELINE + 10.0            # 440.58
BODY_FRAME_BOTTOM = 34.0
BODY_FRAME_HEIGHT = BODY_FRAME_TOP - BODY_FRAME_BOTTOM    # 406.58 (>= 40 lines + one 9pt gap)

FRAME_BODY = Frame(
    MARGIN,
    BODY_FRAME_BOTTOM,
    TEXT_W,
    BODY_FRAME_HEIGHT,
    id="body-frame",
    leftPadding=0,
    rightPadding=0,
    topPadding=0,
    bottomPadding=0,
)

MANUSCRIPT = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.md"
OUT_PDF = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.pdf"
LOG_FILE = Path(__file__).resolve().parent / "build_log.txt"

SHEAR = math.tan(math.radians(9.0))  # synthetic oblique for the title page
SC_SCALE = 0.72                       # small-caps scale for synthesized small caps

# --------------------------------------------------------------------------
# Fonts (EB Garamond bundled in manuscript/fonts/; Georgia fallback)
# --------------------------------------------------------------------------
FONT_DIR = Path(__file__).resolve().parent / "fonts"
GEO_DIR = "/System/Library/Fonts/Supplemental/"


def register_fonts():
    """Register EB Garamond from manuscript/fonts/ or fall back to Georgia.
    Returns the family used."""
    try:
        pdfmetrics.registerFont(TTFont(BODY_FONT, str(FONT_DIR / "EBGaramond-Regular.ttf")))
        pdfmetrics.registerFont(TTFont(BOLD_FONT, str(FONT_DIR / "EBGaramond-Bold.ttf")))
        pdfmetrics.registerFont(TTFont(ITAL_FONT, str(FONT_DIR / "EBGaramond-Italic.ttf")))
        pdfmetrics.registerFont(TTFont(BOLD_ITAL_FONT, str(FONT_DIR / "EBGaramond-BoldItalic.ttf")))
        pdfmetrics.registerFontFamily(
            BODY_FONT,
            normal=BODY_FONT,
            bold=BOLD_FONT,
            italic=ITAL_FONT,
            boldItalic=BOLD_ITAL_FONT,
        )
        return "EB Garamond (manuscript/fonts/)"
    except Exception:
        pdfmetrics.registerFont(TTFont(BODY_FONT, GEO_DIR + "Georgia.ttf"))
        pdfmetrics.registerFont(TTFont(BOLD_FONT, GEO_DIR + "Georgia Bold.ttf"))
        pdfmetrics.registerFont(TTFont(ITAL_FONT, GEO_DIR + "Georgia Italic.ttf"))
        pdfmetrics.registerFont(TTFont(BOLD_ITAL_FONT, GEO_DIR + "Georgia Bold Italic.ttf"))
        pdfmetrics.registerFontFamily(
            BODY_FONT,
            normal=BODY_FONT,
            bold=BOLD_FONT,
            italic=ITAL_FONT,
            boldItalic=BOLD_ITAL_FONT,
        )
        return "Georgia.ttf (fallback)"


FONT_SUMMARY = register_fonts()

# --------------------------------------------------------------------------
# Styles
# --------------------------------------------------------------------------
BODY = ParagraphStyle(
    "body",
    fontName=BODY_FONT,
    fontSize=10,
    leading=LEADING,
    alignment=TA_JUSTIFY,
    spaceAfter=9,  # measured reference gap of 19pt between paragraph baselines (10 + 9)
    allowWidows=0,  # widow/orphan protection: no single lines at page top/bottom
    allowOrphans=0,
)
BODY_ITALIC = ParagraphStyle(
    "body-italic",
    parent=BODY,
    fontName=ITAL_FONT,
    leftIndent=18,  # set-off prayers
)
BODY_QUOTE = ParagraphStyle(
    "body-quote",
    parent=BODY,
    fontName=ITAL_FONT,  # prayers print as italic, indented blockquotes
    leftIndent=18,
)
ATTRIB = ParagraphStyle(
    "attrib",
    parent=BODY,
    fontSize=9,
    leading=LEADING,
    alignment=TA_RIGHT,
)
ATTRIB_ITALIC = ParagraphStyle("attrib-italic", parent=ATTRIB, fontName=ITAL_FONT)
QUOTE_ATTRIB = ParagraphStyle(
    "quote-attrib",
    parent=ATTRIB_ITALIC,
    leftIndent=18,
)
H2_STYLE = ParagraphStyle(
    "h2",
    fontName=BOLD_FONT,
    fontSize=10,
    leading=LEADING,
    alignment=TA_LEFT,
    spaceBefore=9,
    spaceAfter=0,
    keepWithNext=1,
)
H1_STYLE = ParagraphStyle(
    "chapter-title",
    fontName=BOLD_FONT,
    fontSize=13,
    leading=13,
    alignment=TA_LEFT,
    spaceAfter=0,
    keepWithNext=1,  # a chapter title never sits alone at a page bottom
)
TOC_HEAD_STYLE = ParagraphStyle(
    "toc-head",
    fontName=BOLD_FONT,
    fontSize=18,
    leading=18,
    alignment=TA_LEFT,
    spaceAfter=18,
)
TOC_ENTRY_STYLE = ParagraphStyle(
    "toc-entry",
    fontName=BODY_FONT,
    fontSize=12,
    leading=14.4,
    alignment=TA_LEFT,
    spaceBefore=9,
)
NOTES_ENTRY = ParagraphStyle(
    "notes-entry",
    parent=BODY,
    leftIndent=20,
    firstLineIndent=-20,
    splitLongWords=1,  # long URLs must wrap
)

# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_to_xml(text: str) -> str:
    """Convert markdown inline markup (*italic*, **bold**) to reportlab XML."""
    text = xml_escape(text)
    parts = re.split(r"\*\*", text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append("<b>%s</b>" % part)
        else:
            sub = re.split(r"\*", part)
            for j, piece in enumerate(sub):
                out.append("<i>%s</i>" % piece if j % 2 == 1 else piece)
    return "".join(out)


def small_caps(text: str, size: float, font: str, scale: float = SC_SCALE) -> str:
    """Synthesize small caps: uppercase everything; letters that were lowercase
    in the source are set at scale*size via <font size> markup (reportlab cannot
    use EB Garamond's real smcp feature, so caps stay synthesized)."""
    esc = xml_escape(text)
    out = []
    for ch in esc:
        if ch.isalpha():
            if ch.islower():
                out.append('<font size="%.2f">%s</font>' % (size * scale, ch.upper()))
            else:
                out.append(ch.upper())
        else:
            out.append(ch)
    return "".join(out)


def small_caps_width(text: str, size: float, font: str, scale: float = SC_SCALE) -> float:
    """Exact rendered width of a synthesized small-caps run (per-char sizes)."""
    total = 0.0
    for ch in text:
        if ch.isalpha() and ch.islower():
            total += pdfmetrics.stringWidth(ch.upper(), font, size * scale)
        elif ch.isalpha():
            total += pdfmetrics.stringWidth(ch.upper(), font, size)
        else:
            total += pdfmetrics.stringWidth(ch, font, size)
    return total


def chapter_title_size(text: str, size: float = 13.0) -> float:
    """Shrink-to-fit: if the synthesized small-caps title exceeds the text
    measure at 13 pt bold, scale the size so it fits on one line."""
    w = small_caps_width(text, size, BOLD_FONT)
    if w <= TEXT_W:
        return size
    return size * (TEXT_W / w)


class ChapterTitle(Paragraph):
    """Chapter/head title paragraph; also an anchor for page-number capture."""

    def __init__(self, text: str, aname: str):
        size = chapter_title_size(text)
        super().__init__(small_caps(text, size, BOLD_FONT), H1_STYLE)
        self.aname = aname


# --------------------------------------------------------------------------
# Markdown block parser (headings / paragraphs / blockquotes / TOC links /
# numbered list items / horizontal rules)
# --------------------------------------------------------------------------
TOC_LINK_RE = re.compile(r"^- \[(.+?)\]\(#[^)]*\)$")
NUM_ITEM_RE = re.compile(r"^\d+\.\s+\S")


def parse_blocks(text: str):
    lines = text.split("\n")
    blocks = []
    cur = []

    def flush_para():
        nonlocal cur
        if cur:
            blocks.append(("para", " ".join(cur)))
            cur = []

    i = 0
    n = len(lines)
    while i < n:
        s = lines[i].strip()
        if s == "" or s == "---":
            flush_para()
        elif s.startswith("# "):
            flush_para()
            blocks.append(("h1", s[2:].strip()))
        elif s.startswith("## "):
            flush_para()
            blocks.append(("h2", s[3:].strip()))
        elif s.startswith(">"):
            flush_para()
            raw = []
            while i < n and lines[i].startswith(">"):
                raw.append(lines[i][1:].strip())
                i += 1
            blocks.append(("blockquote", raw))
            continue
        elif TOC_LINK_RE.match(s):
            flush_para()
            blocks.append(("toclink", TOC_LINK_RE.match(s).group(1)))
        elif NUM_ITEM_RE.match(s):
            flush_para()
            blocks.append(("listitem", s))
        else:
            cur.append(s)
        i += 1
    flush_para()
    return blocks


def classify_para(text: str):
    """Decide how a plain paragraph renders."""
    s = text.strip()
    if s.startswith("*") and s.endswith("*") and s.count("*") == 2:
        inner = s[1:-1].strip()
        if inner.startswith("—"):
            return ("attrib", inner, True)  # italic attribution
        return ("italic", inner, False)     # set-off italic paragraph (prayer)
    if s.startswith("—"):
        return ("attrib", s, False)         # plain attribution
    return ("body", s, False)


# --------------------------------------------------------------------------
# Document template
# --------------------------------------------------------------------------
class BookDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=portrait((PAGE_W, PAGE_H)),
            leftMargin=MARGIN,
            rightMargin=MARGIN,
            topMargin=0,
            bottomMargin=0,
        )
        self.anchors = {}

    def afterFlowable(self, flowable):
        if isinstance(flowable, ChapterTitle):
            self.anchors[flowable.aname] = self.page


def draw_page_number(canv, doc):
    canv.saveState()
    canv.setFont(BODY_FONT, 8)
    canv.drawCentredString(PAGE_W / 2.0, PAGE_NUM_BASELINE, str(canv.getPageNumber()))
    canv.restoreState()


def draw_title_page(canv, doc):
    canv.saveState()
    # Synthetic ~9 deg oblique shear. The shear matrix shifts a point at page
    # height y right by SHEAR*y, so each line is pre-shifted left by SHEAR*y:
    # the baseline lands at x=MARGIN while ascenders lean right (italic look).
    canv.transform(1, 0, SHEAR, 1, 0, 0)
    canv.setFont(BOLD_FONT, 18)
    canv.drawString(MARGIN - SHEAR * 297, 297, TITLE_MAIN)
    canv.setFont(BOLD_FONT, 14)
    y = 275
    for line in TITLE_SUB_LINES:
        canv.drawString(MARGIN - SHEAR * y, y, line)
        y -= 23
    canv.drawString(MARGIN - SHEAR * y, y, BYLINE)
    canv.restoreState()
    canv.setFont(BODY_FONT, 9)
    canv.drawCentredString(PAGE_W / 2.0, 43, EDITION_LINE)


def make_toc(page_numbers):
    """TableOfContents with dot leaders (dotsMinLevel=1) and right-aligned page
    numbers. Entries are pre-registered and drawn in the same build pass."""
    toc = TableOfContents(dotsMinLevel=1)
    toc.levelStyles = [TOC_ENTRY_STYLE, TOC_ENTRY_STYLE]
    toc.tableStyle = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]
    for text in TOC_ORDER:
        toc.addEntry(1, text, page_numbers.get(text, 0))
    toc._lastEntries = list(toc._entries)  # draw our own entries this pass
    return toc


# --------------------------------------------------------------------------
# Story assembly
# --------------------------------------------------------------------------
def assemble_story(blocks, page_numbers):
    story = []
    # Page 1 is the title page; body content starts on page 2. From here on,
    # everything flows continuously — no forced page breaks between chapters.
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())
    i = 2  # skip blocks[0] (book title) and blocks[1] (byline) -> title page
    while i < len(blocks):
        kind, payload = blocks[i]
        if kind == "h1":
            text = payload
            if text == "Table of Contents":
                # the TOC keeps its own page
                story.append(NextPageTemplate("body"))
                story.append(PageBreak())
                story.append(Paragraph("Table of Contents", TOC_HEAD_STYLE))
                story.append(make_toc(page_numbers))
                story.append(PageBreak())
            else:
                # Note on the Text, chapters, Epilogue, Notes and Sources
                story.append(ChapterTitle(text, aname=text))
        elif kind == "h2":
            story.append(Paragraph(small_caps(payload, 10, BOLD_FONT), H2_STYLE))
        elif kind == "para":
            cls, inner, ital = classify_para(payload)
            if cls == "body":
                story.append(Paragraph(inline_to_xml(inner), BODY))
            elif cls == "italic":
                story.append(Paragraph(inline_to_xml(inner), BODY_ITALIC))
            else:  # attribution
                story.append(Paragraph(inline_to_xml(inner), ATTRIB_ITALIC if ital else ATTRIB))
        elif kind == "blockquote":
            # split the raw quote lines into paragraphs on empty lines
            qparas = []
            cur = []
            for line in payload:
                if line == "":
                    if cur:
                        qparas.append(" ".join(cur))
                        cur = []
                else:
                    cur.append(line)
            if cur:
                qparas.append(" ".join(cur))
            for q in qparas:
                if q.startswith("—"):
                    story.append(Paragraph(inline_to_xml(q), QUOTE_ATTRIB))
                else:
                    story.append(Paragraph(inline_to_xml(q), BODY_QUOTE))
        elif kind == "listitem":
            story.append(Paragraph(inline_to_xml(payload), NOTES_ENTRY))
        elif kind == "toclink":
            pass  # rendered via the TOC flowable
        i += 1
    return story


def build_pass(blocks, page_numbers, outfile):
    doc = BookDoc(outfile)
    doc.addPageTemplates(
        [
            PageTemplate(id="title", frames=[Frame(0, 0, 1, 1, id="title-none")], onPage=draw_title_page),
            PageTemplate(id="body", frames=[FRAME_BODY], onPage=draw_page_number),
        ]
    )
    doc.build(assemble_story(blocks, page_numbers))
    return doc.anchors


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    text = Path(MANUSCRIPT).read_text(encoding="utf-8")
    blocks = parse_blocks(text)

    # Title-page material (verbatim from the manuscript)
    global TITLE_MAIN, TITLE_SUB_LINES, BYLINE, EDITION_LINE, TOC_ORDER
    assert blocks[0][0] == "h1", "manuscript must start with the book title"
    title_full = blocks[0][1]  # e.g. "The Mystery of the Trinity"
    TITLE_MAIN, _, TITLE_SUB = title_full.partition(": ")
    BYLINE = blocks[1][1]  # "by Fr. Peter Gruber, C.O."
    EDITION_LINE = "Working manuscript draft \u00b7 2026"

    # Split the subtitle (if any) across lines if it exceeds the text measure
    # at 14 pt
    if not TITLE_SUB:
        TITLE_SUB_LINES = []
    elif pdfmetrics.stringWidth(TITLE_SUB, BOLD_FONT, 14) <= TEXT_W:
        TITLE_SUB_LINES = [TITLE_SUB]
    else:
        # split so the author's name stays intact on the second line
        words = TITLE_SUB.split(" ")
        k = len(words) - 1
        for j, w in enumerate(words):
            if w.rstrip(".") == "Fr":
                k = j
                break
        TITLE_SUB_LINES = [" ".join(words[:k]), " ".join(words[k:])]

    # TOC order: manuscript TOC links + Notes and Sources
    toclinks = [p for k, p in blocks if k == "toclink"]
    TOC_ORDER = toclinks + ["Notes and Sources"]

    # Pass A: dummy page numbers -> record start pages
    tmp_pdf = str(Path(OUT_PDF).with_suffix(".passA.pdf"))
    log = io.StringIO()
    with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        anchors_a = build_pass(blocks, {t: 0 for t in TOC_ORDER}, tmp_pdf)

    # Chapters flow continuously: TOC page numbers are the observed starts.
    final_pages = {name: anchors_a[name] for name in TOC_ORDER}

    # Pass B: real TOC page numbers
    with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        anchors_b = build_pass(blocks, final_pages, str(OUT_PDF))

    # Verify determinism of the two passes
    for name in TOC_ORDER:
        assert anchors_b[name] == final_pages[name], (name, anchors_b[name], final_pages[name])

    LOG_FILE.write_text(log.getvalue(), encoding="utf-8")
    Path(tmp_pdf).unlink(missing_ok=True)

    from pypdf import PdfReader

    total_pages = len(PdfReader(str(OUT_PDF)).pages)

    print("fonts:", FONT_SUMMARY)
    print("page count:", total_pages)
    print("chapter starts:", {k: v for k, v in anchors_b.items()})
    print("log:", LOG_FILE)

    # quick self-check of build log for warnings
    warnings = [
        ln
        for ln in log.getvalue().splitlines()
        if re.search(r"warn|error|glyph|substitut|notdef", ln, re.I)
    ]
    print("log warnings:", warnings if warnings else "none")


if __name__ == "__main__":
    main()
