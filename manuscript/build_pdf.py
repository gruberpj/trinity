#!/usr/bin/env python3
"""
Build a print-interior PDF of "The Mystery of the Trinity" matching the
measured layout of 'MGS Booklet Jun 2025 interior.pdf' (306.0 x 495.0 pt).

Two-pass build:
  Pass A: build with dummy TOC page numbers; record the start page of every
          chapter (and Notes and Sources) via an afterFlowable hook.
  Pass B: compute final page numbers (chapters must start on odd pages,
          inserting blank pages where needed), rebuild with the real TOC.

Fonts: Baskerville.ttc (macOS Supplemental), Georgia.ttf fallback.
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
BODY_TOP_BASELINE = 430.58     # first body-line baseline (chapter pages: 19pt below title)
BODY_LINES = 40
LEADING = 10.0
BODY_BOTTOM_BASELINE = BODY_TOP_BASELINE - (BODY_LINES - 1) * LEADING  # 40.58
TITLE_BASELINE = 449.58        # chapter title / running head baseline
PAGE_NUM_BASELINE = 18.0

BODY_FONT = "Baskerville"
BOLD_FONT = "Baskerville-Bold"
ITAL_FONT = "Baskerville-Italic"
SEMI_FONT = "Baskerville-SemiBold"
BOLD_ITAL_FONT = "Baskerville-BoldItalic"
SEMI_ITAL_FONT = "Baskerville-SemiBoldItalic"

# Baskerville hhea ascent = 1839/2048 em -> reportlab ascent/1000 = 897.95
ASCENT_10 = 8.98     # ascent at 10 pt
ASCENT_13_BOLD = 11.654  # Bold ascent (896.484/1000) at 13 pt

# Frame top edges so that first baselines land exactly on the grid
BODY_FRAME_TOP = BODY_TOP_BASELINE + ASCENT_10            # 439.56
BODY_FRAME_BOTTOM = 34.0
BODY_FRAME_HEIGHT = BODY_FRAME_TOP - BODY_FRAME_BOTTOM    # 405.56 (>= 40 lines + one 9pt gap)
TITLE_FRAME_TOP = TITLE_BASELINE + ASCENT_13_BOLD         # 461.234
TITLE_FRAME_BOTTOM = TITLE_FRAME_TOP - 20.0
TITLE_FRAME_HEIGHT = TITLE_FRAME_TOP - TITLE_FRAME_BOTTOM

FRAME_TITLE = Frame(MARGIN, TITLE_FRAME_BOTTOM, TEXT_W, TITLE_FRAME_HEIGHT, id="title-frame")
FRAME_BODY = Frame(MARGIN, BODY_FRAME_BOTTOM, TEXT_W, BODY_FRAME_HEIGHT, id="body-frame")

MANUSCRIPT = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.md"
OUT_PDF = Path(__file__).resolve().parent / "Mystery_of_the_Trinity.pdf"
LOG_FILE = Path(__file__).resolve().parent / "build_log.txt"

SHEAR = math.tan(math.radians(9.0))  # synthetic oblique for the title page
SC_SCALE = 0.72                       # small-caps scale for synthesized small caps

# --------------------------------------------------------------------------
# Fonts (Baskerville TTC primary; Georgia fallback)
# --------------------------------------------------------------------------
BASK_TTC = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
GEO_DIR = "/System/Library/Fonts/Supplemental/"


def register_fonts():
    """Register Baskerville (TTC subfaces) or fall back to Georgia. Returns the family used."""
    try:
        pdfmetrics.registerFont(TTFont(BODY_FONT, BASK_TTC, subfontIndex=0))
        pdfmetrics.registerFont(TTFont(BOLD_FONT, BASK_TTC, subfontIndex=1))
        pdfmetrics.registerFont(TTFont(ITAL_FONT, BASK_TTC, subfontIndex=2))
        pdfmetrics.registerFont(TTFont(BOLD_ITAL_FONT, BASK_TTC, subfontIndex=3))
        pdfmetrics.registerFont(TTFont(SEMI_FONT, BASK_TTC, subfontIndex=4))
        pdfmetrics.registerFont(TTFont(SEMI_ITAL_FONT, BASK_TTC, subfontIndex=5))
        pdfmetrics.registerFontFamily(
            BODY_FONT,
            normal=BODY_FONT,
            bold=BOLD_FONT,
            italic=ITAL_FONT,
            boldItalic=BOLD_ITAL_FONT,
        )
        return "Baskerville.ttc (subfaces 0,1,2,3,4,5)"
    except Exception:
        pdfmetrics.registerFont(TTFont(BODY_FONT, GEO_DIR + "Georgia.ttf"))
        pdfmetrics.registerFont(TTFont(BOLD_FONT, GEO_DIR + "Georgia Bold.ttf"))
        pdfmetrics.registerFont(TTFont(ITAL_FONT, GEO_DIR + "Georgia Italic.ttf"))
        pdfmetrics.registerFont(TTFont(BOLD_ITAL_FONT, GEO_DIR + "Georgia Bold Italic.ttf"))
        pdfmetrics.registerFont(TTFont(SEMI_FONT, GEO_DIR + "Georgia Bold.ttf"))
        pdfmetrics.registerFont(TTFont(SEMI_ITAL_FONT, GEO_DIR + "Georgia Bold Italic.ttf"))
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
    leftIndent=18,  # quoted prayers in the body
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
    fontName=SEMI_FONT,
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
)
TOC_HEAD_STYLE = ParagraphStyle(
    "toc-head",
    fontName=SEMI_FONT,
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
    in the source are set at scale*size via <font size> markup (Baskerville has
    no real small-caps face)."""
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


class ChapterTitle(Paragraph):
    """Chapter/head title paragraph; also an anchor for page-number capture."""

    def __init__(self, text: str, aname: str):
        super().__init__(small_caps(text, 13, BOLD_FONT), H1_STYLE)
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
    canv.setFont(SEMI_FONT, 18)
    canv.transform(1, 0, SHEAR, 1, 0, 0)  # synthetic ~9 deg oblique
    canv.drawString(MARGIN, 297, TITLE_MAIN)
    canv.setFont(SEMI_FONT, 14)
    y = 275
    for line in TITLE_SUB_LINES:
        canv.drawString(MARGIN, y, line)
        y -= 23
    canv.drawString(MARGIN, y, BYLINE)
    canv.restoreState()
    canv.setFont(BODY_FONT, 9)
    canv.drawCentredString(PAGE_W / 2.0, 43, EDITION_LINE)


def make_toc(page_numbers):
    """TableOfContents with dot leaders (dotsMinLevel=1) and right-aligned page
    numbers. Entries are pre-registered and drawn in the same build pass."""
    toc = TableOfContents(dotsMinLevel=1)
    toc.levelStyles = [TOC_ENTRY_STYLE, TOC_ENTRY_STYLE]
    for text in TOC_ORDER:
        toc.addEntry(1, text, page_numbers.get(text, 0))
    toc._lastEntries = list(toc._entries)  # draw our own entries this pass
    return toc


# --------------------------------------------------------------------------
# Story assembly
# --------------------------------------------------------------------------
def assemble_story(blocks, page_numbers, blanks_before):
    story = []
    i = 2  # skip blocks[0] (book title) and blocks[1] (byline) -> title page
    while i < len(blocks):
        kind, payload = blocks[i]
        if kind == "h1":
            text = payload
            if text == "Table of Contents":
                story.append(NextPageTemplate("body"))
                story.append(PageBreak())
                story.append(Paragraph("Table of Contents", TOC_HEAD_STYLE))
                story.append(make_toc(page_numbers))
            else:
                # Note on the Text, chapters, Epilogue, Notes and Sources
                for _ in range(blanks_before.get(text, 0)):
                    story.append(NextPageTemplate("body"))
                    story.append(PageBreak())
                story.append(NextPageTemplate("chapter"))
                story.append(PageBreak())
                story.append(ChapterTitle(text, aname=text))
        elif kind == "h2":
            story.append(Paragraph(small_caps(payload, 10, SEMI_FONT), H2_STYLE))
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


def build_pass(blocks, page_numbers, blanks_before, outfile):
    doc = BookDoc(outfile)
    doc.addPageTemplates(
        [
            PageTemplate(id="title", frames=[Frame(0, 0, 1, 1, id="title-none")], onPage=draw_title_page),
            PageTemplate(id="body", frames=[FRAME_BODY], onPage=draw_page_number),
            PageTemplate(id="chapter", frames=[FRAME_TITLE, FRAME_BODY], onPage=draw_page_number),
        ]
    )
    doc.build(assemble_story(blocks, page_numbers, blanks_before))
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
    title_full = blocks[0][1]  # "The Mystery of the Trinity: A Retreat with Fr. Peter Gruber, C.O."
    TITLE_MAIN, _, TITLE_SUB = title_full.partition(": ")
    BYLINE = blocks[1][1]  # "by Fr. Peter Gruber, C.O."
    EDITION_LINE = "Working manuscript draft \u00b7 2026"

    # Split the subtitle across lines if it exceeds the text measure at 14 pt
    if pdfmetrics.stringWidth(TITLE_SUB, SEMI_FONT, 14) <= TEXT_W:
        TITLE_SUB_LINES = [TITLE_SUB]
    else:
        words = TITLE_SUB.split(" ")
        best = 1
        while (
            best < len(words)
            and pdfmetrics.stringWidth(" ".join(words[:best]), SEMI_FONT, 14) <= TEXT_W
        ):
            best += 1
        TITLE_SUB_LINES = [" ".join(words[:best]), " ".join(words[best:])]

    # TOC order: manuscript TOC links + Notes and Sources
    toclinks = [p for k, p in blocks if k == "toclink"]
    TOC_ORDER = toclinks + ["Notes and Sources"]

    # Pass A: dummy page numbers, no blank pages -> record start pages
    tmp_pdf = str(Path(OUT_PDF).with_suffix(".passA.pdf"))
    log = io.StringIO()
    with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        anchors_a = build_pass(blocks, {t: 0 for t in TOC_ORDER}, {}, tmp_pdf)

    # Compute final page numbers; chapters must start on odd pages.
    blanks_before = {}
    final_pages = {}
    offset = 0
    for name in TOC_ORDER:
        start = anchors_a[name] + offset
        if start % 2 == 0:
            offset += 1
            blanks_before[name] = 1
        final_pages[name] = anchors_a[name] + offset

    # Pass B: real TOC page numbers + blank pages for odd starts
    with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        anchors_b = build_pass(blocks, final_pages, blanks_before, str(OUT_PDF))

    # Verify determinism of the offset math
    for name in TOC_ORDER:
        assert anchors_b[name] == final_pages[name], (name, anchors_b[name], final_pages[name])

    LOG_FILE.write_text(log.getvalue(), encoding="utf-8")
    Path(tmp_pdf).unlink(missing_ok=True)

    from pypdf import PdfReader

    total_pages = len(PdfReader(str(OUT_PDF)).pages)

    print("fonts:", FONT_SUMMARY)
    print("page count:", total_pages)
    print("chapter starts:", {k: v for k, v in anchors_b.items()})
    print("blanks inserted before:", blanks_before)
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
