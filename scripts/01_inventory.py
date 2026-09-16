#!/usr/bin/env python3
"""Prompt A (initialize and inventory): build manifests/inventory.csv and
manifests/checksums.sha256 for the seven M4A recordings.

Non-destructive: reads originals and audio_original copies only, never writes
to them. Stops (exit 1) on missing files, unexpected files, or checksum drift
between a top-level original and its audio_original copy.
"""
import csv
import hashlib
import os
import sys

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIO_DIR = os.path.join(PROJECT, "audio_original")
MANIFEST_DIR = os.path.join(PROJECT, "manifests")

# Stable ID -> top-level original filename (handoff section 2 / Appendix C).
ID_MAP = {
    "C01_icons_of_the_trinity": "Conference 1_ Icons of the Trinity.m4a",
    "C02_mystery": "Conference 2_ Mystery.m4a",
    "C03_gift_and_liturgy": "Conference 3_ Gift and Liturgy.m4a",
    "C04_relationship": "Conference 4_ Relationship.m4a",
    "C05_intimacy": "Conference 5_ Intimacy.m4a",
    "C06_evangelization": "Conference 6_ Evangelization.m4a",
    "E01_engineering_mystery": "Engineering Mystery - Retreat Talk for Engineering Students.m4a",
}

# Durations (seconds) from macOS afinfo on the top-level originals.
DURATIONS = {
    "C01_icons_of_the_trinity": 1489.428,
    "C02_mystery": 1131.903,
    "C03_gift_and_liturgy": 1438.164,
    "C04_relationship": 805.844,
    "C05_intimacy": 1393.236,
    "C06_evangelization": 952.105,
    "E01_engineering_mystery": 2766.292,
}

FIELDS = [
    "recording_id",
    "source_path",
    "basename",
    "bytes",
    "sha256",
    "duration_seconds",
    "codec",
    "sample_rate",
    "channels",
    "source_mtime",
    "status",
    "asr_run_id",
    "transcript_path",
    "reviewer",
    "reviewed_at",
    "notes",
]


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def probe_av(path):
    """Return (codec, sample_rate, channels) via PyAV; blank fields on failure."""
    try:
        import av

        container = av.open(path)
        stream = container.streams.audio[0]
        codec = stream.codec_context.name or ""
        sample_rate = stream.codec_context.sample_rate or ""
        channels = stream.codec_context.channels or ""
        container.close()
        return codec, sample_rate, channels
    except Exception:  # noqa: BLE001 - inventory must not die on one bad file
        return "", "", ""


def main():
    problems = []
    hard_failures = []

    # Exactly the seven expected files may live in audio_original.
    found = set(os.listdir(AUDIO_DIR)) if os.path.isdir(AUDIO_DIR) else set()
    expected = set(ID_MAP.values())
    for extra in sorted(found - expected):
        if os.path.isfile(os.path.join(AUDIO_DIR, extra)):
            hard_failures.append("unexpected file in audio_original/: %s" % extra)

    rows = []
    for recording_id in sorted(ID_MAP):
        basename = ID_MAP[recording_id]
        original = os.path.join(PROJECT, basename)
        copy = os.path.join(AUDIO_DIR, basename)
        if not os.path.isfile(original):
            hard_failures.append("missing top-level original: %s" % basename)
            continue
        if not os.path.isfile(copy):
            hard_failures.append("missing audio_original copy: %s" % basename)
            continue
        orig_hash = sha256_file(original)
        copy_hash = sha256_file(copy)
        if orig_hash != copy_hash:
            hard_failures.append("checksum drift copy vs original: %s" % basename)
        codec, sr, ch = probe_av(copy)
        if codec == "" or sr == "" or ch == "":
            problems.append(
                "PyAV metadata incomplete for %s (codec=%r sample_rate=%r channels=%r)"
                % (basename, codec, sr, ch)
            )
        st = os.stat(original)
        rows.append(
            {
                "recording_id": recording_id,
                "source_path": original,
                "basename": basename,
                "bytes": st.st_size,
                "sha256": copy_hash,
                "duration_seconds": DURATIONS[recording_id],
                "codec": codec,
                "sample_rate": sr,
                "channels": ch,
                "source_mtime": int(st.st_mtime),
                "status": "INVENTORIED",
                "asr_run_id": "",
                "transcript_path": "",
                "reviewer": "",
                "reviewed_at": "",
                "notes": "top-level original kept read-only; working copy in audio_original/ (hash-verified)",
            }
        )

    os.makedirs(MANIFEST_DIR, exist_ok=True)

    inv_path = os.path.join(MANIFEST_DIR, "inventory.csv")
    with open(inv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    ck_path = os.path.join(MANIFEST_DIR, "checksums.sha256")
    with open(ck_path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write("%s  audio_original/%s\n" % (row["sha256"], row["basename"]))

    print("inventory rows: %d" % len(rows))
    for problem in problems:
        print("ANOMALY: %s" % problem, file=sys.stderr)
    for failure in hard_failures:
        print("HARD FAILURE: %s" % failure, file=sys.stderr)
    if len(rows) != 7:
        hard_failures.append("expected 7 rows, got %d" % len(rows))
    if hard_failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
