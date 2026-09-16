#!/usr/bin/env python3
"""Prompt H (manuscript assembly): assemble manuscript/Mystery_of_the_Trinity.md
from approved chapter files in chapters/reviewed/ in canonical order.

Usage:
  python3 scripts/10_assemble_manuscript.py [--approved-only] [--dry-run]

Chapter selection and order
  * Only *.md files in chapters/reviewed/ are chapters (ORDER.txt is not).
  * If chapters/reviewed/ORDER.txt exists it defines the order (one filename
    per line; blank lines and # comments ignored). Listed-but-missing files
    are an error; files not listed are excluded with a warning.
  * Otherwise, files mapping to canonical positions (C01..C06 or 01..06 = the
    six conferences; E01/epilogue = epilogue) are ordered canonically; if any
    file does not map to a canonical position, the whole set is ordered by
    plain filename sort.
  * --approved-only additionally requires each chapter file to carry
    "status: CHAPTER_APPROVED" (or "approved") in its YAML front matter;
    files without it are excluded with a warning.

Manuscript structure (generated deterministically; no content invented)
  * Title page ("The Mystery of the Trinity: A Retreat with Fr. Peter Gruber, C.O." by Fr. Peter Gruber, C.O.).
  * "Note on the Text": provisional note text (owner-confirmable) emitted verbatim.
  * Table of contents built from each chapter's first #/## heading.
  * The chapter files concatenated verbatim, in order.
  * "Notes and Sources" from research/source_ledger.csv rows whose
    verification_status is VERIFIED_EXACT, VERIFIED_MINOR_VARIANT, or
    PARAPHRASE_CONFIRMED (sorted by source_id; format: attribution, work,
    edition/publisher/year, locator, URL + access date).
"""
import argparse
import csv
import hashlib
import os
import re
import sys

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_DIR = os.path.join(PROJECT, "chapters", "reviewed")
ORDER_FILE = os.path.join(CHAPTERS_DIR, "ORDER.txt")
LEDGER = os.path.join(PROJECT, "research", "source_ledger.csv")
OUT_PATH = os.path.join(PROJECT, "manuscript", "Mystery_of_the_Trinity.md")

BOOK_TITLE = "The Mystery of the Trinity: A Retreat with Fr. Peter Gruber, C.O."
AUTHOR = "Fr. Peter Gruber, C.O."

NOTE_ON_THE_TEXT = (
    "This book was prepared from seven audio recordings of a retreat and a talk given by Fr. Peter Gruber, C.O., in 2025 and 2026. The text was produced by an auditable audio-to-book pipeline: each recording was machine-transcribed (faster-whisper, large-v3 model), reviewed against word-level confidence data, lightly corrected for grammar while preserving the author's spoken wording, and assembled into chapters, with a provenance record kept for every section of every chapter. Quotations were checked against published editions where possible; any wording or attribution that could not be verified is flagged in the project records and consolidated in the accompanying notes file. Scripture is cited as heard, with translation questions noted for the author. This is a working manuscript draft: final doctrinal review, quotation-permission review, and editorial approval remain with the author and his reviewers."
    "\n\n*Provisional note — the author may confirm, correct, or replace it.*"
)

VERIFIED_STATUSES = {
    "VERIFIED_EXACT",
    "VERIFIED_MINOR_VARIANT",
    "PARAPHRASE_CONFIRMED",
}

MARKERS = [
    "[VERIFY]",
    "[TODO]",
    "[unclear",
    "[possibly",
    "ATTRIBUTION_UNCONFIRMED",
    "LOCATOR_MISSING",
    "DOCTRINAL_REVIEW",
    "PERMISSION_REVIEW",
]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
APPROVAL_RE = re.compile(
    r"^\s*status:\s*(chapter_approved|approved)\s*$", re.IGNORECASE
)


def words(text):
    return len(text.split())


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def natural_key(value):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", value)]


def canonical_key(filename):
    stem = os.path.splitext(filename)[0]
    match = re.match(r"^(?:c)?0?([1-6])(?![0-9])", stem, re.IGNORECASE)
    if match:
        return int(match.group(1))
    if re.match(r"^(?:e01|epilogue)(?![0-9a-z])", stem, re.IGNORECASE):
        return 7
    return None


def chapter_order(files):
    """Return (ordered_filenames, order_source, warnings)."""
    if os.path.isfile(ORDER_FILE):
        with open(ORDER_FILE, encoding="utf-8") as fh:
            listed = [
                line.strip()
                for line in fh
                if line.strip() and not line.strip().startswith("#")
            ]
        missing = [name for name in listed if name not in files]
        if missing:
            sys.exit(
                "ERROR: chapters/reviewed/ORDER.txt lists missing file(s): %s"
                % ", ".join(missing)
            )
        ordered = [name for name in listed]
        excluded = sorted(set(files) - set(listed))
        warnings = []
        if excluded:
            warnings.append(
                "not listed in ORDER.txt, excluded: %s" % ", ".join(excluded)
            )
        return ordered, "chapters/reviewed/ORDER.txt", warnings
    keys = {name: canonical_key(name) for name in files}
    if all(key is not None for key in keys.values()):
        ordered = sorted(files, key=lambda name: (keys[name], name))
        return ordered, "canonical order (C01..C06 + E01)", []
    return sorted(files), "filename sort", []


def is_approved(path):
    try:
        with open(path, encoding="utf-8") as fh:
            head = fh.read(4096)
    except OSError:
        return False
    lines = head.splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if APPROVAL_RE.match(line):
            return True
    return False


def load_chapters(filenames):
    chapters = []
    for name in filenames:
        path = os.path.join(CHAPTERS_DIR, name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        chapters.append((name, path, text))
    return chapters


def first_heading(text):
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            return len(match.group(1)), match.group(2)
    return None


def clean_heading_text(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def slug(text):
    text = clean_heading_text(text)
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text.strip().lower())


def build_toc(chapters):
    lines = ["# Table of Contents", ""]
    for name, _path, text in chapters:
        heading = first_heading(text)
        if heading is None:
            title = os.path.splitext(name)[0]
            lines.append("- [%s](#%s)" % (title, slug(title)))
            continue
        level, title = heading
        entry = "- [%s](#%s)" % (clean_heading_text(title), slug(title))
        if level == 2:
            entry = "  " + entry
        lines.append(entry)
    return "\n".join(lines)


def build_notes():
    if not os.path.isfile(LEDGER):
        return [
            "# Notes and Sources",
            "",
            "_(research/source_ledger.csv not found — no verified sources "
            "to list.)_",
        ]
    rows = []
    with open(LEDGER, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("verification_status") or "").strip() in (
                VERIFIED_STATUSES
            ):
                rows.append(row)
    rows.sort(key=lambda row: natural_key(row.get("source_id", "")))
    lines = ["# Notes and Sources", ""]
    if not rows:
        lines.append(
            "_(no ledger rows with VERIFIED_EXACT / VERIFIED_MINOR_VARIANT / "
            "PARAPHRASE_CONFIRMED.)_"
        )
        return lines
    lines.append(
        "Compiled from research/source_ledger.csv (verification status "
        "VERIFIED_EXACT, VERIFIED_MINOR_VARIANT, or PARAPHRASE_CONFIRMED only)."
    )
    lines.append("")
    for index, row in enumerate(rows, 1):
        author = (row.get("attributed_author") or "").strip()
        work = (row.get("work_title") or "").strip()
        edition = (row.get("edition_or_translation") or "").strip()
        publisher = (row.get("publisher") or "").strip()
        year = (row.get("year") or "").strip()
        locator = (row.get("page_or_section") or "").strip() or (
            row.get("claimed_locator") or ""
        ).strip()
        url = (row.get("canonical_url") or "").strip()
        accessed = (row.get("accessed_at") or "").strip()

        parts = []
        if author:
            parts.append("**%s**" % author)
        if work:
            parts.append("*%s*" % work)
        edition_info = ", ".join(
            part for part in (edition, publisher, year) if part
        )
        if edition_info:
            parts.append(edition_info)
        if locator:
            parts.append(locator)
        head = ", ".join(parts) if parts else (
            "(source_id %s)" % row.get("source_id", "")
        )
        if head and head[-1] not in ".?!)":
            head += "."
        entry = "%d. %s" % (index, head)
        if url:
            entry += " — %s" % url
            if accessed:
                entry += " (accessed %s)" % accessed
        lines.append(entry)
    return lines


def assemble(chapters):
    out = []
    out.append("# %s" % BOOK_TITLE)
    out.append("")
    out.append("by %s" % AUTHOR)
    out.append("")
    out.append("---")
    out.append("")
    out.append("# Note on the Text")
    out.append("")
    out.append(NOTE_ON_THE_TEXT)
    out.append("")
    out.append("---")
    out.append("")
    out.append(build_toc(chapters))
    out.append("")
    out.append("---")
    out.append("")
    for _name, _path, text in chapters:
        out.append(text.rstrip())
        out.append("")
        out.append("")
    out.append("---")
    out.append("")
    out.extend(build_notes())
    return "\n".join(out).rstrip() + "\n"


def count_verified_rows():
    count = 0
    with open(LEDGER, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("verification_status") or "").strip() in (
                VERIFIED_STATUSES
            ):
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--approved-only",
        action="store_true",
        help="include only chapter files whose front matter marks them "
        "CHAPTER_APPROVED",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the assembly plan without writing the manuscript",
    )
    args = parser.parse_args()

    if not os.path.isdir(CHAPTERS_DIR):
        sys.exit("ERROR: chapters/reviewed/ not found: %s" % CHAPTERS_DIR)
    all_files = sorted(
        name
        for name in os.listdir(CHAPTERS_DIR)
        if name.lower().endswith(".md") and not name.startswith(".")
    )

    if not all_files:
        print(
            "No chapter files found in chapters/reviewed/ — nothing to "
            "assemble."
        )
        print(
            "(Chapter drafting and approval are later stages; full assembly "
            "is expected after chapters exist.)"
        )
        if args.dry_run:
            return
        sys.exit(
            "Refusing to assemble: no chapter files (writing would clobber "
            "any existing manuscript with an empty one)."
        )

    ordered, order_source, warnings = chapter_order(all_files)
    for warning in warnings:
        print("WARNING: %s" % warning, file=sys.stderr)

    if args.approved_only:
        included = []
        for name in ordered:
            path = os.path.join(CHAPTERS_DIR, name)
            if is_approved(path):
                included.append(name)
            else:
                print(
                    "WARNING: --approved-only: no CHAPTER_APPROVED status in "
                    "front matter; excluded: %s" % name,
                    file=sys.stderr,
                )
        ordered = included
        if not ordered:
            print(
                "--approved-only: no chapter file carries a CHAPTER_APPROVED "
                "front-matter status."
            )
            if args.dry_run:
                return
            sys.exit("Refusing to assemble: no approved chapter files.")

    chapters = load_chapters(ordered)
    word_counts = {name: words(text) for name, _path, text in chapters}
    total_words = sum(word_counts.values())

    print("Manuscript plan (%s)" % ("dry run" if args.dry_run else "assemble"))
    print("  output: %s" % os.path.relpath(OUT_PATH, PROJECT))
    print("  chapter source: chapters/reviewed/ — %s" % order_source)
    print(
        "  mode: %s"
        % ("approved-only" if args.approved_only else "all reviewed")
    )
    print("  order (%d file(s)):" % len(ordered))
    for index, (name, _path, _text) in enumerate(chapters, 1):
        print("    %d. %-44s %6d words" % (index, name, word_counts[name]))
    print("  chapter words total: %d" % total_words)
    if not os.path.isfile(LEDGER):
        print(
            "  notes: research/source_ledger.csv missing — Notes and Sources "
            "will be empty"
        )
    else:
        print(
            "  notes: %d verified ledger row(s) (VERIFIED_EXACT / "
            "VERIFIED_MINOR_VARIANT / PARAPHRASE_CONFIRMED)"
            % count_verified_rows()
        )

    if args.dry_run:
        return

    text = assemble(chapters)

    if os.path.isfile(OUT_PATH):
        print(
            "NOTE: overwriting existing manuscript (assembly output is "
            "deterministic and regenerable)"
        )

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    tmp = OUT_PATH + ".partial"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, OUT_PATH)

    print()
    print("Assembled: %s" % OUT_PATH)
    print("Included files and sha256 (content, as embedded):")
    for name, _path, chapter_text in chapters:
        print("  %s  %s" % (sha256_text(chapter_text), name))
    print("total words (manuscript): %d" % words(text))
    print("Marker scan of assembled manuscript:")
    for marker in MARKERS:
        print("  %-24s %d" % (marker, text.count(marker)))
    print("manuscript sha256: %s" % sha256_text(text))


if __name__ == "__main__":
    main()
