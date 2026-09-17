#!/usr/bin/env python3
"""Build manuscript/Mystery_of_the_Trinity.docx from the manuscript markdown.

Parses the markdown subset used by the manuscript (h1/h2/h3 headings, body
paragraphs joined from consecutive non-empty lines, blockquotes, TOC link
lines, numbered list items) and renders it with a small set of Garamond
paragraph styles. See the project notes for the style specification.
"""

import re
from collections import Counter
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

BASE_DIR = Path(__file__).resolve().parent.parent
MD_PATH = BASE_DIR / "manuscript" / "Mystery_of_the_Trinity.md"
DOCX_PATH = BASE_DIR / "manuscript" / "Mystery_of_the_Trinity.docx"

BYLINE = "by Fr. Peter Gruber, C.O."

TOC_LINK_RE = re.compile(r"^(\s*)- \[(.+?)\]\(#[^)]*\)$")
NUM_ITEM_RE = re.compile(r"^\d+\.\s")


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
def set_garamond(style):
    """Set Garamond on a style: font name plus explicit w:ascii / w:hAnsi."""
    style.font.name = "Garamond"
    rpr = style.element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    rf.set(qn("w:ascii"), "Garamond")
    rf.set(qn("w:hAnsi"), "Garamond")


def make_styles(doc):
    normal = doc.styles["Normal"]
    set_garamond(normal)
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(6)
    # first_line_indent stays None (template default)

    def add_para_style(name):
        try:
            style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            style.base_style = normal
        except ValueError:
            style = doc.styles[name]
            if style.type != WD_STYLE_TYPE.PARAGRAPH:
                # The default template ships "Book Title" as a *character*
                # style; drop it and create a paragraph style with that name.
                style.element.getparent().remove(style.element)
                style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
                style.base_style = normal
        set_garamond(style)
        style.font.size = Pt(12)  # explicit; subclasses override below
        return style

    book_title = add_para_style("Book Title")
    book_title.font.size = Pt(26)
    book_title.font.bold = True
    book_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    book_title.paragraph_format.keep_with_next = True

    chapter = add_para_style("Chapter")
    chapter.font.size = Pt(16)
    chapter.font.bold = True
    chapter.paragraph_format.space_before = Pt(12)
    chapter.paragraph_format.space_after = Pt(6)
    chapter.paragraph_format.keep_with_next = True

    section = add_para_style("Section")
    section.font.size = Pt(12.5)
    section.font.bold = True
    section.font.italic = True
    section.paragraph_format.space_before = Pt(10)
    section.paragraph_format.space_after = Pt(4)
    section.paragraph_format.keep_with_next = True

    prayer = add_para_style("Prayer")
    prayer.font.italic = True
    prayer.paragraph_format.left_indent = Inches(0.5)
    prayer.paragraph_format.space_after = Pt(6)

    toc_entry = add_para_style("TOC Entry")
    toc_entry.paragraph_format.space_after = Pt(0)

    attribution = add_para_style("Attribution")
    attribution.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    attribution.paragraph_format.space_after = Pt(6)

    return {
        "Book Title": book_title,
        "Chapter": chapter,
        "Section": section,
        "Prayer": prayer,
        "TOC Entry": toc_entry,
        "Attribution": attribution,
    }


# ---------------------------------------------------------------------------
# Inline markup
# ---------------------------------------------------------------------------
def add_runs(paragraph, text, base_bold=False, base_italic=False):
    """Add runs for *text*, splitting on ** (bold) first, then * (italic)."""
    bold_on = False
    for segment in text.split("**"):
        italic_on = False
        for part in segment.split("*"):
            if part:
                run = paragraph.add_run(part)
                run.bold = base_bold or bold_on
                run.italic = base_italic or italic_on
                run.font.name = "Garamond"
            italic_on = not italic_on
        bold_on = not bold_on


# ---------------------------------------------------------------------------
# Markdown subset parser
# ---------------------------------------------------------------------------
def parse_markdown(text):
    lines = text.split("\n")
    blocks = []
    current = []

    def flush_paragraph():
        if current:
            blocks.append(("para", " ".join(current)))
            current.clear()

    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped == "" or stripped == "---":
            flush_paragraph()
        elif stripped.startswith("# "):
            flush_paragraph()
            blocks.append(("h1", stripped[2:].strip()))
        elif stripped.startswith("## "):
            flush_paragraph()
            blocks.append(("h2", stripped[3:].strip()))
        elif stripped.startswith("### "):
            flush_paragraph()
            blocks.append(("h3", stripped[4:].strip()))
        elif line.startswith(">"):
            flush_paragraph()
            raw = []
            while i < n and lines[i].startswith(">"):
                rest = lines[i][1:]
                raw.append(rest[1:] if rest.startswith(" ") else rest)
                i += 1
            blocks.append(("blockquote", raw))
            continue
        else:
            toc_match = TOC_LINK_RE.match(line)
            if toc_match:
                flush_paragraph()
                level = 2 if len(toc_match.group(1)) >= 2 else 1
                blocks.append(("toc", toc_match.group(2).strip(), level))
            elif NUM_ITEM_RE.match(stripped):
                flush_paragraph()
                blocks.append(("listitem", stripped))
            else:
                current.append(stripped)
        i += 1
    flush_paragraph()
    return blocks


def is_wrapped_italic(text):
    """True when the line is a standalone paragraph entirely wrapped in *...*."""
    return (
        len(text) > 1
        and text.startswith("*")
        and text.endswith("*")
        and text.count("*") == 2
    )


def split_blockquote(lines):
    """Split blockquote raw lines into paragraphs on blank lines."""
    groups, current = [], []
    for line in lines:
        if line == "":
            if current:
                groups.append(" ".join(current))
                current = []
        else:
            current.append(line)
    if current:
        groups.append(" ".join(current))
    return groups


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def render(doc, styles, blocks):
    first_h1 = None
    for block in blocks:
        kind = block[0]
        if kind == "h1":
            text = block[1]
            if first_h1 is None:
                first_h1 = text
                paragraph = doc.add_paragraph(style=styles["Book Title"])
            else:
                paragraph = doc.add_paragraph(style=styles["Chapter"])
            add_runs(paragraph, text)
        elif kind in ("h2", "h3"):
            paragraph = doc.add_paragraph(style=styles["Section"])
            add_runs(paragraph, block[1])
        elif kind == "para":
            text = block[1]
            if text == BYLINE:
                paragraph = doc.add_paragraph(style="Normal")
                paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_runs(paragraph, text)
            elif is_wrapped_italic(text):
                inner = text[1:-1].strip()
                if inner.startswith("—"):
                    # italic attribution, e.g. "*— Prayer of St. Elizabeth ...*"
                    paragraph = doc.add_paragraph(style=styles["Attribution"])
                    add_runs(paragraph, inner, base_italic=True)
                else:
                    # standalone prayer paragraph
                    paragraph = doc.add_paragraph(style=styles["Prayer"])
                    add_runs(paragraph, inner, base_italic=True)
            elif text.startswith("—"):
                paragraph = doc.add_paragraph(style=styles["Attribution"])
                add_runs(paragraph, text)
            else:
                paragraph = doc.add_paragraph(style="Normal")
                add_runs(paragraph, text)
        elif kind == "blockquote":
            for quote in split_blockquote(block[1]):
                if quote.startswith("—"):
                    paragraph = doc.add_paragraph(style=styles["Attribution"])
                    add_runs(paragraph, quote, base_italic=True)
                else:
                    paragraph = doc.add_paragraph(style=styles["Prayer"])
                    add_runs(paragraph, quote, base_italic=True)
        elif kind == "toc":
            paragraph = doc.add_paragraph(style=styles["TOC Entry"])
            if block[2] == 2:
                paragraph.paragraph_format.left_indent = Inches(0.25)
            add_runs(paragraph, block[1])
        else:  # listitem
            paragraph = doc.add_paragraph(style="Normal")
            add_runs(paragraph, block[1])
    return first_h1


def main():
    text = MD_PATH.read_text(encoding="utf-8")
    blocks = parse_markdown(text)

    doc = Document()
    styles = make_styles(doc)
    first_h1 = render(doc, styles, blocks)

    doc.core_properties.title = first_h1
    doc.save(DOCX_PATH)

    style_counts = Counter(p.style.name for p in doc.paragraphs)
    summary = ", ".join(
        f"{name}={count}" for name, count in sorted(style_counts.items())
    )
    print(f"Wrote {DOCX_PATH.relative_to(BASE_DIR)}")
    print(f"  paragraphs: {len(doc.paragraphs)}  title: {first_h1!r}")
    print(f"  styles: {summary}")
    print(f"  file size: {DOCX_PATH.stat().st_size} bytes")


if __name__ == "__main__":
    main()
