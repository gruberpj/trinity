#!/usr/bin/env python3
"""Prompt B/C: render a raw ASR JSON to timestamped Markdown.

Usage: python3 scripts/05_render_transcript.py --id C01 [--run-id RUN_ID]

Reads work/asr/{ID}.asr.{run_id}.json and writes
transcripts/raw/{ID}.raw.{run_id}.md. Without --run-id, the newest valid run
is chosen (valid = .done.json marker exists and input/output hashes match).
The YAML-style header block follows handoff section 4 ("Raw transcript
header") with engine_version, compute_type, beam_size, temperature and
vad_filter lines added. One paragraph per segment: [HH:MM:SS] SPEAKER_01:
<text>, timestamp = segment start.

Engine text is immutable evidence: it is rendered verbatim; only whitespace is
normalized for markdown layout. Word timestamps stay in the JSON. An existing
output markdown is never overwritten.
"""
import argparse
import json
import os
import sys

import asrlib


def format_hms(seconds):
    total = int(seconds)
    return "%02d:%02d:%02d" % (total // 3600, (total % 3600) // 60, total % 60)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--id",
        required=True,
        help="recording id: short (C01) or canonical (C01_icons_of_the_trinity)",
    )
    parser.add_argument(
        "--run-id",
        default=None,
        help="run_id to render (default: newest valid run)",
    )
    args = parser.parse_args()

    recording_id = asrlib.resolve_recording_id(args.id)
    run_id = args.run_id or asrlib.newest_valid_run_id(recording_id)

    json_path = asrlib.asr_json_path(recording_id, run_id)
    if not os.path.isfile(json_path):
        sys.exit(
            "ASR JSON not found: %s (run 04_transcribe.py first)" % json_path
        )
    with open(json_path, encoding="utf-8") as fh:
        doc = json.load(fh)
    header = doc["header"]

    # Audit: the source file must still match the hash the JSON was made from.
    basename = asrlib.ID_MAP[recording_id]
    current_sha = asrlib.sha256_file(os.path.join(asrlib.AUDIO_DIR, basename))
    if header.get("source_sha256") != current_sha:
        sys.exit(
            "source hash mismatch: JSON says %s but audio_original/%s is %s"
            % (header.get("source_sha256"), basename, current_sha)
        )

    lines = [
        "---",
        "recording_id: %s" % header["recording_id"],
        "source_sha256: %s" % header["source_sha256"],
        "asr_run_id: %s" % header["run_id"],
        "engine: %s" % header["engine"],
        "engine_version: %s" % header["engine_version"],
        "model: %s" % header["model"],
        "compute_type: %s" % header["compute_type"],
        "beam_size: %s" % header["beam_size"],
        "temperature: %s" % header["temperature"],
        "vad_filter: %s" % str(header["vad_filter"]).lower(),
        "language: %s" % header["language"],
        "word_timestamps: %s" % str(header["word_timestamps"]).lower(),
        "status: machine_raw",
        "---",
        "",
    ]
    for seg in doc["segments"]:
        text = " ".join(seg["text"].split()).strip()
        lines.append("[%s] SPEAKER_01: %s" % (format_hms(seg["start"]), text))
        lines.append("")

    out_path = asrlib.raw_md_path(recording_id, run_id)
    if os.path.exists(out_path):
        sys.exit(
            "output already exists; refusing to overwrite: %s (move it aside "
            "manually if a re-render is truly needed)" % out_path
        )
    os.makedirs(asrlib.RAW_DIR, exist_ok=True)
    tmp = out_path + ".partial"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, out_path)
    print("WROTE %s (%d paragraphs)" % (out_path, len(doc["segments"])))


if __name__ == "__main__":
    main()
