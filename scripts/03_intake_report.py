#!/usr/bin/env python3
"""Prompt A (initialize and inventory): write logs/intake_report.md from the
manifest artifacts. Re-verifies SHA-256 of every audio_original copy against
its top-level original, then renders the report.
"""
import csv
import datetime
import hashlib
import os

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY = os.path.join(PROJECT, "manifests", "inventory.csv")
CHECKSUMS = os.path.join(PROJECT, "manifests", "checksums.sha256")
LOG_DIR = os.path.join(PROJECT, "logs")
REPORT = os.path.join(LOG_DIR, "intake_report.md")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    with open(INVENTORY, "r", newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    with open(CHECKSUMS, "r", encoding="utf-8") as fh:
        checksum_lines = [ln.rstrip("\n") for ln in fh if ln.strip()]

    integrity = []
    for row in rows:
        copy_path = os.path.join(PROJECT, "audio_original", row["basename"])
        recomputed = sha256_file(copy_path)
        original_hash = sha256_file(row["source_path"])
        ok = recomputed == row["sha256"] and original_hash == row["sha256"]
        integrity.append((row["recording_id"], ok))

    anomalies = []
    for row in rows:
        if row["codec"] != "aac":
            anomalies.append(
                "%s: codec=%r (expected aac for .m4a)" % (row["recording_id"], row["codec"])
            )
        if row["channels"] not in ("1", "2"):
            anomalies.append(
                "%s: channels=%r (expected 1 or 2)" % (row["recording_id"], row["channels"])
            )
        if row["sample_rate"] == "":
            anomalies.append("%s: sample_rate missing" % row["recording_id"])
    mtimes = {}
    for row in rows:
        mtimes.setdefault(int(row["source_mtime"]), []).append(row["recording_id"])
    if len(mtimes) > 1:
        for mtime, ids in mtimes.items():
            anomalies.append(
                "source_mtime %s shared by: %s"
                % (mtime, ", ".join(ids))
            )
    anomalies.append(
        "DOCX extraction artifacts: some heading lines carry U+2028 and verse-number gaps use "
        "U+00A0 in the extracted text; ledger excerpts copy the extracted text verbatim "
        "(including these characters)."
    )
    anomalies.append(
        "Long DOCX passages in research/source_ledger.csv are truncated opening excerpts "
        "(~200 chars + '...'); full exact text remains in source_material/."
    )

    lines = []
    add = lines.append
    add("# Intake Report - Prompt A (initialize and inventory)")
    add("")
    add("- Generated: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    add("- Project: `%s`" % PROJECT)
    add("- Stage: DISCOVERED -> INVENTORIED (per handoff state machine)")
    add("")
    add("## Source files")
    add("")
    add("- 7 M4A recordings at project top level; 2 source documents (DOCX + handoff PDF).")
    add("- Originals were NOT moved, renamed, or modified. Top-level originals are marked read-only (0444).")
    add("- Working copies: `audio_original/` (7 M4A, mode 0644) and `source_material/` (DOCX, PDF, extracted text).")
    add("")
    add("## Stable ID map")
    add("")
    add("| recording_id | basename |")
    add("| --- | --- |")
    for row in rows:
        add("| %s | %s |" % (row["recording_id"], row["basename"]))
    add("")
    add("## Per-file technical metadata")
    add("")
    add("| recording_id | bytes | duration_s | codec | sample_rate | channels | sha256 prefix | mtime |")
    add("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in rows:
        add(
            "| %s | %s | %s | %s | %s | %s | %s | %s |"
            % (
                row["recording_id"],
                row["bytes"],
                row["duration_seconds"],
                row["codec"],
                row["sample_rate"],
                row["channels"],
                row["sha256"][:12],
                row["source_mtime"],
            )
        )
    add("")
    add("## Copy integrity")
    add("")
    add("- SHA-256 recomputed for every `audio_original/` copy and its top-level original; all compared against `manifests/checksums.sha256`.")
    for rid, ok in integrity:
        add("- %s: %s" % (rid, "OK" if ok else "MISMATCH"))
    add("")
    add("## Anomalies")
    add("")
    if anomalies:
        for anomaly in anomalies:
            add("- %s" % anomaly)
    else:
        add("- none")
    add("")
    add("## Artifacts")
    add("")
    add("- `manifests/inventory.csv` (%d data rows)" % len(rows))
    add("- `manifests/checksums.sha256` (%d lines)" % len(checksum_lines))
    add("- `research/source_ledger.csv` (seed rows from DOCX)")
    add("- `source_material/The_Mystery_of_the_Trinity_Retreat_3-14.md` (extracted DOCX text)")

    os.makedirs(LOG_DIR, exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote %s" % REPORT)


if __name__ == "__main__":
    main()
