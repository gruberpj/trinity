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
  * Title page ("The Mystery of the Trinity" by Fr. Peter Gruber, C.O.).
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

BOOK_TITLE = "The Mystery of the Trinity"
AUTHOR = "Fr. Peter Gruber, C.O."

NOTE_ON_THE_TEXT = (
    "This book was prepared from seven audio recordings of a retreat and a talk given by Fr. Peter Gruber, C.O., in 2025 and 2026. The text was produced by an auditable audio-to-book pipeline: each recording was machine-transcribed (faster-whisper, large-v3 model), reviewed against word-level confidence data, lightly corrected for grammar while preserving the author's spoken wording, and assembled into chapters, with a provenance record kept for every section of every chapter. Quotations were checked against published editions where possible; any wording or attribution that could not be verified is flagged in the project records and consolidated in the accompanying notes file. Scripture is cited as heard, with translation questions noted for the author."
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
    # Book-style "Notes and Sources": grouped by chapter, prose entries,
    # no URLs and no access dates. Deterministic from the source ledger.
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

    CHAPTER_LABELS = {
        "C01": "Chapter 1 — Icons of the Trinity",
        "C02": "Chapter 2 — Mystery",
        "C03": "Chapter 3 — Gift and Liturgy",
        "C04": "Chapter 4 — Relationship",
        "C05": "Chapter 5 — Intimacy",
        "C06": "Chapter 6 — Evangelization",
        "E01": "Epilogue — Engineering Mystery",
    }
    SPECIAL = {
        "SRC-045": (
            "St. Augustine, *Confessions* X.41.66. The 'deepest wound' "
            "passage is a modern paraphrase of this text; the speaker's "
            "hedge is retained."
        ),
    }

    def note_entry(row):
        sid = (row.get("source_id") or "").strip()
        if sid in SPECIAL:
            return SPECIAL[sid]

        def clean(value):
            value = (value or "").strip()
            if value in ("—", "(no source located)", "(attribution "
                          "doubtful — speaker hedges)"):
                return ""
            return value

        author = clean(row.get("attributed_author"))
        work = clean(row.get("work_title"))
        year = clean(row.get("year"))
        locator = clean(row.get("page_or_section")) or clean(
            row.get("claimed_locator")
        )
        discrepancy = (row.get("discrepancy") or "")

        # Sources removed from the book by owner decision are not cited.
        if "removed from book" in discrepancy:
            return ""
        # Bare scripture citations are covered by the opening paragraph.
        verse = r"\d?\s?[A-Za-z0-9]+ \d+:\d+(?:[–-]\d+)?(?:, \d+:\d+)*"
        if re.fullmatch(verse, work) or re.fullmatch(verse, locator):
            return ""
        if not author and re.search(
            r"\b[A-Za-z]+ \d+:\d+(?:[–-]\d+)?\s*/", work
        ):
            return ""
        # Bare Bible book names (seeded scripture-range rows) are covered
        # by the opening paragraph.
        if not author and re.fullmatch(
            r"(Psalms|Genesis|Exodus|Mark|Matthew|John|Luke|Romans|"
            r"1 Corinthians|2 Corinthians|1 Thessalonians|1 John|Judges)",
            work,
        ):
            return ""
        # Mention-only sources (no printed quotation) are not notes.
        if "reference" in locator.lower() or "reference" in work.lower():
            return ""
        # The Icon paragraph at the end covers Rublev's artwork.
        if "Rublev" in author and "Trinity" in work:
            return ""

        # Compact author: first clause before a parenthesis.
        short_author = re.split(r"\s*[;(]\s*", author, maxsplit=1)[0].rstrip(", ")
        # Compact work title: first clause before parenthesis/semicolon;
        # if that is empty (e.g. "(cf. The Religious Sense)"), recover
        # the title after "cf.".
        short_work = re.split(r"\s*[;(]\s*", work, maxsplit=1)[0].strip(" ,")
        if not short_work:
            m = re.search(r"\bcf\.\s*([^)]+)", work)
            if m:
                short_work = m.group(1).strip(" ,")
        # First 4-digit year in the year field.
        m = re.search(r"\b(1[89]\d{2}|20\d{2})\b", year)
        year_short = m.group(1) if m else ""
        # Compact locator: first clause if it runs long.
        loc_short = locator
        if len(locator) > 70:
            loc_short = re.split(r"\s*[;(]\s*", locator, maxsplit=1)[0].rstrip(", ")
        # Drop trailing parenthetical qualifiers like "(of 9)".
        loc_short = re.sub(r"\s*\([^)]{1,40}\)$", "", loc_short).rstrip(", ")
        # Drop a locator that merely repeats the work title.
        if loc_short and (
            loc_short.lower() in short_work.lower()
            or short_work.lower() in loc_short.lower()
        ):
            loc_short = ""

        parts = []
        if short_author:
            parts.append(short_author)
        if short_work:
            parts.append("*%s*" % short_work)
        if year_short:
            parts.append(year_short)
        if loc_short:
            parts.append(loc_short)
        if not parts:
            return ""
        entry = ", ".join(parts)
        if entry[-1] not in ".?!)":
            entry += "."
        return entry

    lines = ["# Notes and Sources", ""]
    if not rows:
        lines.append("_(no verified sources.)_")
        return lines
    lines.append(
        "Quotations follow the editions noted below. Scripture quotations "
        "follow the Revised Standard Version, Second Catholic Edition "
        "(Ignatius Press, 2006); a few verses retain the wording as spoken."
    )
    lines.append("")

    grouped = {}
    for row in rows:
        cid = (row.get("chapter_id") or "").strip()
        grouped.setdefault(cid or "_general", []).append(row)

    for cid in ("C01", "C02", "C03", "C04", "C05", "C06", "E01"):
        if cid not in grouped:
            continue
        lines.append("## " + CHAPTER_LABELS[cid])
        lines.append("")
        for row in grouped[cid]:
            entry = note_entry(row)
            if entry:
                lines.append(entry)
        lines.append("")

    if "_general" in grouped:
        lines.append("## General")
        lines.append("")
        for row in grouped["_general"]:
            entry = note_entry(row)
            if entry:
                lines.append(entry)
        lines.append("")

    lines.append("## Translations")
    lines.append("")
    lines.append(
        "The prayers from St. Augustine's *Confessions* use E. B. Pusey's "
        "public-domain translation. The closing line of Dante's *Paradiso* "
        "is Henry Wadsworth Longfellow's 1867 translation."
    )
    lines.append("")
    lines.append("## Icon")
    lines.append("")
    lines.append(
        "The cover art is Andrei Rublev's *The Trinity* (c. 1411 or "
        "1425–1427), State Tretyakov Gallery, Moscow."
    )
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
    print("  title: %s" % BOOK_TITLE)
    print("  byline: by %s" % AUTHOR)
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
