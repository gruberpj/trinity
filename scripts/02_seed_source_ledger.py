#!/usr/bin/env python3
"""Prompt A (initialize and inventory): seed research/source_ledger.csv from the
extracted DOCX text (source_material/The_Mystery_of_the_Trinity_Retreat_3-14.md).

Quoted text is copied byte-for-byte from the DOCX extraction by slicing between
exact heading lines; nothing is paraphrased. Long passages are reduced to a
distinctive opening (~200 chars) followed by "...", per the intake spec. All
rows start as ATTRIBUTION_UNCONFIRMED; verification fields are left blank.
"""
import csv
import os
import sys

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_TXT = os.path.join(PROJECT, "source_material", "The_Mystery_of_the_Trinity_Retreat_3-14.md")
LEDGER = os.path.join(PROJECT, "research", "source_ledger.csv")
ACCESSED_AT = "2026-09-16"

FIELDS = [
    "source_id",
    "chapter_id",
    "transcript_anchor",
    "item_type",
    "attributed_author",
    "work_title",
    "quoted_or_paraphrased_text",
    "claimed_locator",
    "verified_text",
    "edition_or_translation",
    "publisher",
    "year",
    "page_or_section",
    "canonical_url",
    "accessed_at",
    "verification_status",
    "discrepancy",
    "permission_status",
    "reviewer",
]

# Exact heading lines in document order; used to delimit quoted blocks.
ANCHORS = [
    "St Patrick’s Breastplate",
    "O My God, Trinity Whom I Adore",
    "Quotes Referenced",
    "Joseph Ratzinger, Introduction to Christianity, 162",
    "Joseph Ratzinger, Introduction to Christianity, 172",
    "Joseph Ratzinger, Introduction to Christianity, 175",
    "Pope Benedict XVI, Sermon April 24, 2005",
    "Code of Canon Law, Can. 225.1",
    "Code of Canon Law, Can. 781",
    "Catechism of the Catholic Church, 234",
    "Catechism of the Catholic Church, 2845",
    "An Infinite Abyss of Existence, from St. John Henry Newman, “The Individuality of the Soul”",
    "Scripture Passages",
    "Psalm 42",
    "Genesis 18:1-8",
    "Mark 1:9-13",
    "Matthew 17:1-8",
    "John 14:1-15:12",
    "Matthew 28: 16-20",
    "Catechism of the Catholic Church, 199-267",
]

# (source_id, anchor_key, item_type, attributed_author, work_title,
#  claimed_locator, take_first_line_only)
SOURCES = [
    ("SRC-001", "Joseph Ratzinger, Introduction to Christianity, 162", "quote", "Joseph Ratzinger", "Introduction to Christianity", "162", False),
    ("SRC-002", "Joseph Ratzinger, Introduction to Christianity, 172", "quote", "Joseph Ratzinger", "Introduction to Christianity", "172", False),
    ("SRC-003", "Joseph Ratzinger, Introduction to Christianity, 175", "quote", "Joseph Ratzinger", "Introduction to Christianity", "175", False),
    ("SRC-004", "Pope Benedict XVI, Sermon April 24, 2005", "quote", "Pope Benedict XVI", "Sermon", "April 24, 2005", False),
    ("SRC-005", "Code of Canon Law, Can. 225.1", "canon", "", "Code of Canon Law", "Can. 225.1", False),
    ("SRC-006", "Code of Canon Law, Can. 781", "canon", "", "Code of Canon Law", "Can. 781", False),
    ("SRC-007", "Catechism of the Catholic Church, 234", "catechism", "", "Catechism of the Catholic Church", "234", False),
    ("SRC-008", "Catechism of the Catholic Church, 2845", "catechism", "", "Catechism of the Catholic Church", "2845", False),
    ("SRC-009", "Catechism of the Catholic Church, 199-267", "catechism_section", "", "Catechism of the Catholic Church", "199-267", True),
    ("SRC-010", "An Infinite Abyss of Existence, from St. John Henry Newman, “The Individuality of the Soul”", "quote", "St. John Henry Newman", "The Individuality of the Soul", "", False),
    ("SRC-011", "O My God, Trinity Whom I Adore", "prayer", "St. Elizabeth of the Trinity", "O My God, Trinity Whom I Adore", "", False),
    ("SRC-012", "St Patrick’s Breastplate", "hymn", "St. Patrick", "St Patrick’s Breastplate", "", False),
    # Rublev: artwork reference only; no quoted text in the DOCX beyond the caption line.
    ("SRC-013", None, "artwork", "Andrei Rublev", "Trinity", "", False),
    ("SRC-014", "Psalm 42", "scripture", "", "Psalms", "Psalm 42", False),
    ("SRC-015", "Genesis 18:1-8", "scripture", "", "Genesis", "Genesis 18:1-8", False),
    ("SRC-016", "Mark 1:9-13", "scripture", "", "Mark", "Mark 1:9-13", False),
    ("SRC-017", "Matthew 17:1-8", "scripture", "", "Matthew", "Matthew 17:1-8", False),
    ("SRC-018", "John 14:1-15:12", "scripture", "", "John", "John 14:1-15:12", False),
    ("SRC-019", "Matthew 28: 16-20", "scripture", "", "Matthew", "Matthew 28: 16-20", False),
]

RUBLEV_CAPTION = "Andrei Rublev, Trinity"  # exact DOCX caption line


def normalize_block(lines):
    """Join non-empty lines with single spaces; never collapse intra-line spacing."""
    return " ".join(line.rstrip() for line in lines if line.strip() != "").strip()


def excerpt(text):
    """Keep exact text up to 400 chars; reduce longer passages to ~200 chars + '...'."""
    if len(text) <= 400:
        return text
    cut = text.rfind(" ", 0, 200)
    if cut == -1:
        cut = 200
    return text[:cut] + "..."


def main():
    with open(SRC_TXT, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    # Some heading lines carry a leading U+2028 line separator and trailing
    # whitespace/non-breaking spaces in the DOCX extraction; strip for matching
    # only (never inside quoted text, which is sliced verbatim).
    anchor_positions = {}
    for index, line in enumerate(lines):
        cleaned = line.replace("\u2028", "").strip()
        if cleaned in ANCHORS and cleaned not in anchor_positions:
            anchor_positions[cleaned] = index
    missing = [a for a in ANCHORS if a not in anchor_positions]
    if missing:
        print("missing anchor(s) in extracted text: %r" % missing, file=sys.stderr)
        sys.exit(1)

    ordered = sorted((idx, key) for key, idx in anchor_positions.items())

    def block_for(anchor_key):
        start = anchor_positions[anchor_key]
        end = None
        for idx, _key in ordered:
            if idx > start:
                end = idx
                break
        return lines[start + 1 : end if end is not None else len(lines)]

    rows = []
    problems = []
    for source_id, anchor_key, item_type, author, work_title, locator, first_line_only in SOURCES:
        if anchor_key is None:
            text = RUBLEV_CAPTION
        else:
            block = block_for(anchor_key)
            if first_line_only:
                non_empty = [ln for ln in block if ln.strip() != ""]
                if not non_empty:
                    problems.append("empty block for %s (%s)" % (source_id, anchor_key))
                    text = ""
                else:
                    text = non_empty[0].strip()
            else:
                text = normalize_block(block)
                # Strip the author label line that precedes the Elizabeth prayer.
                if anchor_key == "O My God, Trinity Whom I Adore" and text.startswith("St. Elizabeth of the Trinity "):
                    text = text[len("St. Elizabeth of the Trinity ") :]
        row = {
            "source_id": source_id,
            "chapter_id": "",
            "transcript_anchor": "",
            "item_type": item_type,
            "attributed_author": author,
            "work_title": work_title,
            "quoted_or_paraphrased_text": excerpt(text),
            "claimed_locator": locator,
            "verified_text": "",
            "edition_or_translation": "",
            "publisher": "",
            "year": "",
            "page_or_section": "",
            "canonical_url": "",
            "accessed_at": ACCESSED_AT,
            "verification_status": "ATTRIBUTION_UNCONFIRMED",
            "discrepancy": "",
            "permission_status": "",
            "reviewer": "",
        }
        rows.append(row)

    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print("ledger rows: %d" % len(rows))
    for problem in problems:
        print("ANOMALY: %s" % problem, file=sys.stderr)
    if len(rows) != len(SOURCES):
        sys.exit(1)


if __name__ == "__main__":
    main()
