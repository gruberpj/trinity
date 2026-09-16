#!/usr/bin/env python3
"""Prompt B/C: validate a raw ASR JSON against the G1 checks.

Usage: python3 scripts/06_validate_asr.py --id C01

Checks: JSON parses; segment timestamps monotonic non-decreasing; last
segment end <= audio duration + 5s; span coverage (first word to last word /
audio duration) >= 98%; no empty text tail; total word count > 0. Also runs
the repetition-loop heuristic (asrlib.detect_repetition_loop): any exact
6+-token phrase repeated >=4 times within a 24-segment window is reported as
a WARNING (not a failure - review handles it) with the max repeat count.

Prints a compact validation report. Exit 0 iff every check passes.
"""
import argparse
import json
import os
import sys

import asrlib


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--id",
        required=True,
        help="recording id: short (C01) or canonical (C01_icons_of_the_trinity)",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="path to ASR config yaml (default manifests/asr_config.yaml)",
    )
    args = parser.parse_args()

    recording_id = asrlib.resolve_recording_id(args.id)
    cfg = asrlib.load_asr_config(args.config)
    run_id = cfg["run_id"]

    json_path = asrlib.asr_json_path(recording_id, run_id)
    if not os.path.isfile(json_path):
        print("MISSING %s" % json_path, file=sys.stderr)
        sys.exit(1)
    try:
        with open(json_path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except ValueError as exc:
        print("JSON PARSE FAILED: %s" % exc, file=sys.stderr)
        sys.exit(1)

    duration = float(doc.get("header", {}).get("audio_duration_seconds") or 0)
    res = asrlib.validate_asr(doc, duration)

    print("recording_id    : %s" % recording_id)
    print("run_id          : %s" % run_id)
    print("json            : %s" % json_path)
    print("segments        : %d" % res["segment_count"])
    if res["first_start"] is not None:
        print(
            "transcribed span: %.2fs -> %.2fs"
            % (res["first_start"], res["last_end"])
        )
    print("audio duration  : %.3fs" % duration)
    if res["span_coverage_pct"] is not None:
        print(
            "span coverage   : %.2f%% (>=98%% required) -> %s"
            % (
                res["span_coverage_pct"],
                "PASS" if res["span_coverage_pct"] >= 98.0 else "FAIL",
            )
        )
        print("active coverage : %.2f%%" % res["active_coverage_pct"])
    print("total words     : %d" % res["total_words"])
    print("empty-text segs : %d" % res["empty_text_count"])
    print("zero-word segs  : %d" % res["zero_word_segments"])
    print("max repeat run  : %d (a 6+-token phrase repeating within a "
          "24-segment window; >=4 => loop warning)" % res["max_repeat_run"])
    for start, end, length in res["gaps_over_10s"]:
        print("gap > 10s       : %.1f-%.1f (%.1fs)" % (start, end, length))
    for warning in res["warnings"]:
        print("WARN            : %s" % warning)
    for error in res["errors"]:
        print("ERROR           : %s" % error)
    if res["ok"]:
        print("VALIDATION: PASS")
        sys.exit(0)
    print("VALIDATION: FAIL")
    sys.exit(1)


if __name__ == "__main__":
    main()
