#!/usr/bin/env python3
"""Prompt E (source ledger and verification), extraction step: scan reviewed
clean transcripts for candidate source mentions and write
work/review/candidate_sources.csv for human review.

Usage:
  python3 scripts/08_extract_sources.py --id C01
  python3 scripts/08_extract_sources.py --all-reviewed

Detection (one row per matched family per transcript line):
  quote         the line contains quotation marks (" or the curly variants)
  scripture_ref a Scripture-like reference appears (book name + chapter,
                optionally :verse or :verse-verse; e.g. "John 14",
                "Matthew 28", "Genesis 18:1-8", "Romans 12")
  named_source  a citation-like phrase appears ("Pope Benedict", "Ratzinger",
                "the Catechism", "Canon Law", "St. ..." names) or a handoff
                source-verification marker ([VERIFY], [TODO], [quotation
                wording unverified], ATTRIBUTION_UNCONFIRMED, LOCATOR_MISSING,
                DOCTRINAL_REVIEW, PERMISSION_REVIEW). The marker vocabulary is
                folded into the named_source family because the output schema
                defines exactly three match_type values and these markers
                concern named sources and citations.

Timestamps come from the [HH:MM:SS] block prefix of the line (carried forward
from the last seen block). Front matter above the first block is not a clean
block and is skipped. Transcripts whose inventory.csv reviewed_at is empty are
skipped. The CSV is regenerated deterministically from scratch (it is a derived
work artifact, not a reviewed artifact, so overwriting is safe by design).
"""
import argparse
import csv
import os
import re
import sys

import asrlib

PROJECT = asrlib.PROJECT
INVENTORY = os.path.join(PROJECT, "manifests", "inventory.csv")
OUT_PATH = os.path.join(PROJECT, "work", "review", "candidate_sources.csv")

FIELDS = ["recording_id", "timestamp", "detected_text", "match_type", "notes"]

TIMESTAMP_RE = re.compile(r"^\[(\d{1,2}:\d{2}(?::\d{2})?)\]")

BOOK_NAMES = (
    r"(?:[123]\s*)?(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|"
    r"Judges|Ruth|1\s*Samuel|2\s*Samuel|1\s*Kings|2\s*Kings|"
    r"1\s*Chronicles|2\s*Chronicles|Ezra|Nehemiah|Tobit|Judith|Esther|"
    r"1\s*Maccabees|2\s*Maccabees|Job|Psalms?|Proverbs|Ecclesiastes|"
    r"Song\s+of\s+Songs|Wisdom|Sirach|Isaiah|Jeremiah|Lamentations|Baruch|"
    r"Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|"
    r"Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|"
    r"Romans|1\s*Corinthians|2\s*Corinthians|Galatians|Ephesians|"
    r"Philippians|Colossians|1\s*Thessalonians|2\s*Thessalonians|"
    r"1\s*Timothy|2\s*Timothy|Titus|Philemon|Hebrews|James|1\s*Peter|"
    r"2\s*Peter|1\s*John|2\s*John|3\s*John|Jude|Revelation|Apocalypse)"
)
SCRIPTURE_RE = re.compile(
    r"\b" + BOOK_NAMES + r"\s+\d{1,3}(?::\d{1,3}(?:\s*[–—−-]\s*\d{1,3})?)?\b",
    re.IGNORECASE,
)

NAMED_SOURCE_RE = re.compile(
    r"\bPope\s+Benedict\b|\bRatzinger\b|\bthe\s+Catechism\b|"
    r"\bCatechism\s+of\s+the\s+Catholic\s+Church\b|\bCCC\b|"
    r"\bCanon\s+Law\b|\bCode\s+of\s+Canon\s+Law\b|"
    r"\b(?:St\.?|Saint)\s+[A-Z][A-Za-z'’-]*",
    re.IGNORECASE,
)

SOURCE_MARKER_RE = re.compile(
    r"\[VERIFY\]|\[TODO\]|\[quotation wording unverified\]|"
    r"ATTRIBUTION_UNCONFIRMED|LOCATOR_MISSING|DOCTRINAL_REVIEW|"
    r"PERMISSION_REVIEW"
)


def load_inventory():
    with open(INVENTORY, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def transcript_path_for(row):
    rel = (row.get("transcript_path") or "").strip()
    if not rel:
        rel = os.path.join(
            "transcripts", "clean", "%s.clean.md" % row["recording_id"]
        )
    return rel if os.path.isabs(rel) else os.path.join(PROJECT, rel)


def scan_transcript(recording_id, path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        last_ts = ""
        for line in fh:
            match = TIMESTAMP_RE.match(line)
            if match:
                last_ts = match.group(1)
            if not last_ts:  # front matter above the first block
                continue
            text = line.strip()
            if not text:
                continue
            has_quote = (
                '"' in text or "\u201c" in text or "\u201d" in text
            )
            has_scripture = SCRIPTURE_RE.search(text) is not None
            has_named = (
                NAMED_SOURCE_RE.search(text) is not None
                or SOURCE_MARKER_RE.search(text) is not None
            )
            for kind, hit in (
                ("quote", has_quote),
                ("scripture_ref", has_scripture),
                ("named_source", has_named),
            ):
                if hit:
                    rows.append(
                        {
                            "recording_id": recording_id,
                            "timestamp": last_ts,
                            "detected_text": text,
                            "match_type": kind,
                            "notes": "",
                        }
                    )
    return rows


def write_csv(rows):
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    tmp = OUT_PATH + ".partial"
    with open(tmp, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp, OUT_PATH)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--id",
        help="recording id: short (C01) or canonical (C01_icons_of_the_trinity)",
    )
    group.add_argument(
        "--all-reviewed",
        action="store_true",
        help="scan every reviewed clean transcript (inventory reviewed_at set)",
    )
    args = parser.parse_args()

    inventory = load_inventory()

    if args.id:
        recording_id = asrlib.resolve_recording_id(args.id)
        row = next(
            (r for r in inventory if r["recording_id"] == recording_id), None
        )
        if row is None:
            sys.exit(
                "ERROR: %s not found in manifests/inventory.csv" % recording_id
            )
        if not (row.get("reviewed_at") or "").strip():
            print(
                "SKIPPED: %s has no reviewed_at in inventory (not reviewed)"
                % recording_id
            )
            return
        selected = [row]
    else:
        selected = [
            r for r in inventory if (r.get("reviewed_at") or "").strip()
        ]
        for rid in sorted(
            r["recording_id"] for r in inventory if not (r.get("reviewed_at") or "").strip()
        ):
            print("SKIPPED (no reviewed_at in inventory): %s" % rid)
        if not selected:
            sys.exit("ERROR: no reviewed recordings in manifests/inventory.csv")

    all_rows = []
    for row in selected:
        recording_id = row["recording_id"]
        path = transcript_path_for(row)
        if not os.path.isfile(path):
            message = (
                "clean transcript missing: %s (%s)" % (recording_id, path)
            )
            if args.id:
                sys.exit("ERROR: %s" % message)
            print("WARNING: %s; skipped" % message, file=sys.stderr)
            continue
        rows = scan_transcript(recording_id, path)
        all_rows.extend(rows)
        print("scanned %s: %d candidate row(s)" % (recording_id, len(rows)))

    write_csv(all_rows)
    print("wrote %d candidate row(s) to %s" % (len(all_rows), OUT_PATH))


if __name__ == "__main__":
    main()
