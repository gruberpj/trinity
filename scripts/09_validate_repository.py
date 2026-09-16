#!/usr/bin/env python3
"""Gate scan (G3 sources / G5 manuscript): search transcripts/, chapters/,
manuscript/, and research/ for unresolved editorial and verification markers
and print a human-readable report.

Usage:
  python3 scripts/09_validate_repository.py [--gate G3]

Markers:
  blocking  [VERIFY], [TODO]          -> fail the gate only when found in
                                         chapters/ or manuscript/ (handoff
                                         section 8, gates G4/G5)
  warning   [unclear..., [possibly..., ATTRIBUTION_UNCONFIRMED,
            LOCATOR_MISSING, DOCTRINAL_REVIEW, PERMISSION_REVIEW
                                         -> reported, never fail the gate
                                            (handoff: transcript flags are
                                            warnings, not failures)

Exit code: 0 unless a blocking marker occurs in chapters/ or manuscript/.
Scan scope is exactly the four directory roots above; scripts/, work/, logs/,
and audio_original/ are not scanned, so marker words in the pipeline code
itself can never appear as findings.
"""
import argparse
import os
import sys

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCAN_ROOTS = ["transcripts", "chapters", "manuscript", "research"]
TEXT_EXTS = {".md", ".markdown", ".txt", ".csv"}
BLOCKING = ["[VERIFY]", "[TODO]"]
WARNING = [
    "[unclear",
    "[possibly",
    "ATTRIBUTION_UNCONFIRMED",
    "LOCATOR_MISSING",
    "DOCTRINAL_REVIEW",
    "PERMISSION_REVIEW",
]
MARKERS = BLOCKING + WARNING
BLOCKING_DIRS = {"chapters", "manuscript"}
GATE_LABELS = {
    "G0": "intake gate",
    "G1": "ASR gate",
    "G2": "transcript gate",
    "G3": "sources gate",
    "G4": "chapter gate",
    "G5": "manuscript gate",
}


def scan():
    file_counts = {}
    totals = {marker: 0 for marker in MARKERS}
    word_total = 0
    file_count = 0
    for root in SCAN_ROOTS:
        base = os.path.join(PROJECT, root)
        if not os.path.isdir(base):
            print("NOTE: %s/ not found; skipped" % root, file=sys.stderr)
            continue
        for dirpath, _dirnames, filenames in os.walk(base):
            for name in sorted(filenames):
                if name.startswith("."):
                    continue
                ext = os.path.splitext(name)[1].lower()
                if ext not in TEXT_EXTS:
                    continue
                path = os.path.join(dirpath, name)
                try:
                    with open(path, encoding="utf-8", errors="replace") as fh:
                        text = fh.read()
                except OSError as exc:
                    print(
                        "WARNING: unreadable, skipped: %s (%s)" % (path, exc),
                        file=sys.stderr,
                    )
                    continue
                file_count += 1
                word_total += len(text.split())
                counts = {marker: text.count(marker) for marker in MARKERS}
                present = {
                    marker: n for marker, n in counts.items() if n
                }
                if present:
                    rel = os.path.relpath(path, PROJECT)
                    file_counts[rel] = present
                for marker, n in counts.items():
                    totals[marker] += n
    return file_counts, totals, word_total, file_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gate",
        default="G5",
        choices=sorted(GATE_LABELS),
        help="gate label for the report header (default G5)",
    )
    args = parser.parse_args()

    file_counts, totals, word_total, file_count = scan()

    print(
        "Repository marker scan  |  Gate %s (%s)"
        % (args.gate, GATE_LABELS[args.gate])
    )
    print(
        "Scanned: %s (files: %d, words: %d, estimate)"
        % (", ".join(SCAN_ROOTS), file_count, word_total)
    )
    print(
        "Scope note: scripts/, work/, logs/, audio_original/ are excluded by "
        "design; marker words in pipeline code are never findings."
    )
    print()

    blocking = []
    for rel, counts in file_counts.items():
        top = rel.split(os.sep)[0]
        if top in BLOCKING_DIRS:
            n = counts.get("[VERIFY]", 0) + counts.get("[TODO]", 0)
            if n:
                blocking.append((rel, n))

    print("Per-file marker counts (files without findings omitted)")
    print("-" * 60)
    if not file_counts:
        print("  (no findings)")
    else:
        for rel in sorted(file_counts):
            print(rel)
            for marker in MARKERS:
                n = file_counts[rel].get(marker, 0)
                if n:
                    print("    %-24s %d" % (marker, n))
    print()

    print("Summary by marker")
    print("-" * 60)
    print("%-24s %8s %12s" % ("MARKER", "FILES", "OCCURRENCES"))
    for marker in MARKERS:
        files = sum(
            1 for counts in file_counts.values() if counts.get(marker)
        )
        print("%-24s %8d %12d" % (marker, files, totals[marker]))
    print()

    total_flags = sum(totals.values())
    if word_total:
        per_1000 = total_flags * 1000.0 / word_total
        print(
            "Flag density: %.2f unresolved flags per 1000 words "
            "(%d flags / %d words, estimate)" % (per_1000, total_flags, word_total)
        )
    else:
        print("Flag density: n/a (no words scanned)")
    print(
        "Warning-class markers (%s) are reported above but never fail "
        "the gate." % ", ".join(WARNING)
    )

    if blocking:
        total = sum(n for _rel, n in blocking)
        print()
        print(
            "BLOCKING markers ([VERIFY] / [TODO]) found in chapters/ or "
            "manuscript/:"
        )
        for rel, n in blocking:
            print("  %s: %d" % (rel, n))
        print(
            "BLOCKED: %d blocking occurrence(s); gate %s FAILS"
            % (total, args.gate),
            file=sys.stderr,
        )
        sys.exit(1)

    print()
    print(
        "Gate %s: no blocking markers in chapters/ or manuscript/ (exit 0)"
        % args.gate
    )


if __name__ == "__main__":
    main()
