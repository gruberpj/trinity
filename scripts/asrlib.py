#!/usr/bin/env python3
"""Shared helpers for the ASR pipeline scripts (04_transcribe.py,
05_render_transcript.py, 06_validate_asr.py).

Read-only with respect to audio_original/: nothing here mutates source audio.
All paths are absolute, so scripts behave the same regardless of the caller's
working directory.
"""
import csv
import glob
import hashlib
import json
import os

PROJECT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIO_DIR = os.path.join(PROJECT, "audio_original")
MANIFEST_DIR = os.path.join(PROJECT, "manifests")
ASR_DIR = os.path.join(PROJECT, "work", "asr")
RAW_DIR = os.path.join(PROJECT, "transcripts", "raw")
LOGS_DIR = os.path.join(PROJECT, "logs")

# Short CLI alias -> canonical stable ID (handoff section 2).
SHORT_ALIASES = {
    "C01": "C01_icons_of_the_trinity",
    "C02": "C02_mystery",
    "C03": "C03_gift_and_liturgy",
    "C04": "C04_relationship",
    "C05": "C05_intimacy",
    "C06": "C06_evangelization",
    "E01": "E01_engineering_mystery",
}

# Canonical stable ID -> audio_original/ basename.
ID_MAP = {
    "C01_icons_of_the_trinity": "Conference 1_ Icons of the Trinity.m4a",
    "C02_mystery": "Conference 2_ Mystery.m4a",
    "C03_gift_and_liturgy": "Conference 3_ Gift and Liturgy.m4a",
    "C04_relationship": "Conference 4_ Relationship.m4a",
    "C05_intimacy": "Conference 5_ Intimacy.m4a",
    "C06_evangelization": "Conference 6_ Evangelization.m4a",
    "E01_engineering_mystery": (
        "Engineering Mystery - Retreat Talk for Engineering Students.m4a"
    ),
    "F01_icons": "Rednal Retreat House 3.m4a",
    "F02_mystery": "Rednal Retreat House 4.m4a",
}

# Approved benchmark values that must never drift. load_asr_config() refuses to
# run if the yaml deviates from these (guardrail: pinned ASR configuration).
# condition_on_previous_text=False is the repetition-loop fix: the original
# greedy run (condition_on_previous_text=true) cycled on C01 for ~12.5 min.
PINNED = {
    "engine": "faster-whisper",
    "engine_version": "1.2.1",
    "model": "large-v3",
    "device": "cpu",
    "compute_type": "int8",
    "language": "en",
    "word_timestamps": True,
    "vad_filter": True,
    "beam_size": 1,
    "temperature": 0,
    "condition_on_previous_text": False,
}


def resolve_recording_id(token):
    """Accept either the short CLI alias (C01) or the canonical stable ID."""
    if token in ID_MAP:
        return token
    if token in SHORT_ALIASES:
        return SHORT_ALIASES[token]
    valid = ", ".join(sorted(SHORT_ALIASES))
    raise SystemExit("unknown recording id %r (valid: %s)" % (token, valid))


def load_asr_config(path=None):
    import yaml

    cfg_path = path or os.path.join(MANIFEST_DIR, "asr_config.yaml")
    with open(cfg_path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    for key, value in PINNED.items():
        if cfg.get(key) != value:
            raise SystemExit(
                "asr_config.yaml %s=%r deviates from pinned value %r; "
                "refusing to run" % (key, cfg.get(key), value)
            )
    return cfg


def config_fingerprint(cfg):
    """SHA-256 of the canonical JSON form of the configuration."""
    canonical = json.dumps(cfg, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_sha256(recording_id):
    """Return (sha256, duration_seconds) for a recording from inventory.csv."""
    inv_path = os.path.join(MANIFEST_DIR, "inventory.csv")
    with open(inv_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["recording_id"] == recording_id:
                return row["sha256"], float(row["duration_seconds"])
    raise SystemExit(
        "recording_id %s not found in manifests/inventory.csv" % recording_id
    )


def probe_duration_seconds(path):
    """Container duration of an audio file in seconds, via PyAV."""
    import av

    container = av.open(path)
    try:
        stream = container.streams.audio[0]
        if stream.duration is not None and stream.time_base is not None:
            return float(stream.duration * stream.time_base)
        return float(container.duration / av.time_base)
    finally:
        container.close()


def asr_json_path(recording_id, run_id):
    return os.path.join(ASR_DIR, "%s.asr.%s.json" % (recording_id, run_id))


def asr_done_path(recording_id, run_id):
    return os.path.join(ASR_DIR, "%s.asr.%s.done.json" % (recording_id, run_id))


def raw_md_path(recording_id, run_id):
    return os.path.join(RAW_DIR, "%s.raw.%s.md" % (recording_id, run_id))


def newest_valid_run_id(recording_id):
    """Return the run_id of the newest valid ASR artifact for a recording.

    A run is valid if its .done.json marker exists and its input_sha256 matches
    the current audio_original/ copy and its output_sha256 matches the JSON
    artifact. Newest = lexicographically greatest run_id (run_ids are prefixed
    YYYYMMDD, so string ordering sorts runs chronologically).
    """
    candidates = []
    prefix = recording_id + ".asr."
    for path in glob.glob(os.path.join(ASR_DIR, prefix + "*.json")):
        run_id = os.path.basename(path)[len(prefix) : -len(".json")]
        if run_id.endswith(".done"):  # skip done markers matched by the glob
            continue
        done_path = asr_done_path(recording_id, run_id)
        if not os.path.isfile(done_path):
            continue
        try:
            with open(done_path, encoding="utf-8") as fh:
                done = json.load(fh)
            if done.get("output_sha256") != sha256_file(path):
                continue
            source = os.path.join(AUDIO_DIR, ID_MAP[recording_id])
            if done.get("input_sha256") != sha256_file(source):
                continue
        except (OSError, ValueError):
            continue
        candidates.append(run_id)
    if not candidates:
        raise SystemExit(
            "no valid ASR run found for %s in %s" % (recording_id, ASR_DIR)
        )
    return max(candidates)


def detect_repetition_loop(
    segments, phrase_len=6, min_repeats=4, window_segments=24
):
    """Loop heuristic: does any exact 6+-token phrase repeat >=min_repeats
    times within a window of consecutive segments ("consecutively-ish")?

    Segment texts are normalized to lowercase alphabetic tokens (punctuation
    stripped) and concatenated per window, so loops that split across short
    segments are caught (the failing greedy run produced 2-5 word segments
    cycling "and on the right, we have the Holy Spirit" / "the Father" /
    "and the Holy Spirit"). Returns (max_count, phrase, first_segment_index)
    of the worst offender, or None. Mirrors the diagnostic harness used to
    select the anti-loop configuration (B/C/D/E clip runs, 16 Sep 2026).
    """
    import re
    from collections import Counter

    texts = []
    for seg in segments:
        text = seg.get("text") if isinstance(seg, dict) else ""
        texts.append(text if isinstance(text, str) else "")
    tokens_per_seg = [
        re.sub(r"[^a-z0-9' ]+", " ", text.lower()).split() for text in texts
    ]
    best = (0, None, None)
    count = len(tokens_per_seg)
    for end in range(1, count + 1):
        start = max(0, end - window_segments)
        stream = [
            tok for toks in tokens_per_seg[start:end] for tok in toks
        ]
        if len(stream) < phrase_len:
            continue
        grams = Counter(
            " ".join(stream[i : i + phrase_len])
            for i in range(len(stream) - phrase_len + 1)
        )
        for phrase, occurrences in grams.items():
            if occurrences > best[0]:
                best = (occurrences, phrase, start)
    if best[0] >= min_repeats:
        return best
    return None


def validate_asr(data, audio_duration):
    """G1 checks over a parsed ASR JSON document.

    Returns a dict with ok/errors/warnings plus metrics used for reporting.
    Failures: non-dict document, missing/empty segments, non-monotonic
    timestamps, last end > duration + 5s, span coverage < 98%, empty text
    tail, zero total words.
    """
    res = {
        "ok": True,
        "errors": [],
        "warnings": [],
        "segment_count": 0,
        "first_start": None,
        "last_end": None,
        "span_coverage_pct": None,
        "active_coverage_pct": None,
        "total_words": 0,
        "empty_text_count": 0,
        "zero_word_segments": 0,
        "word_bounds_violations": 0,
        "gaps_over_10s": [],
        "max_repeat_run": 0,
    }

    if not isinstance(data, dict):
        res["errors"].append("document is not a JSON object")
        res["ok"] = False
        return res
    if not isinstance(data.get("header"), dict):
        res["errors"].append("header is missing or not an object")
    segments = data.get("segments")
    if not isinstance(segments, list) or not segments:
        res["errors"].append("segments is missing or empty")
        res["ok"] = False
        return res

    parsed = []
    prev_start = None
    prev_end = None
    last_index = len(segments) - 1
    for index, seg in enumerate(segments):
        res["segment_count"] += 1
        if not isinstance(seg, dict):
            res["errors"].append("segment %d is not an object" % index)
            continue
        try:
            start = float(seg["start"])
            end = float(seg["end"])
        except (KeyError, TypeError, ValueError):
            res["errors"].append(
                "segment %d missing or invalid start/end" % index
            )
            continue
        if end < start:
            res["errors"].append(
                "segment %d: end %.3f < start %.3f" % (index, end, start)
            )
        if prev_start is not None and start < prev_start - 0.001:
            res["errors"].append(
                "segment %d start %.3f decreases from previous start %.3f"
                % (index, start, prev_start)
            )
        if prev_end is not None and start < prev_end - 0.5:
            res["warnings"].append(
                "segment %d starts %.2fs before previous segment ends"
                % (index, prev_end - start)
            )
        if prev_end is not None:
            gap = start - prev_end
            if gap > 10.0:
                res["gaps_over_10s"].append(
                    (round(prev_end, 1), round(start, 1), round(gap, 1))
                )
        text = seg.get("text")
        if not isinstance(text, str) or not text.strip():
            res["empty_text_count"] += 1
            if index == last_index:
                res["errors"].append(
                    "empty text tail: last segment has no text"
                )
        words = seg.get("words")
        if isinstance(words, list) and words:
            res["total_words"] += len(words)
            for word in words:
                if not isinstance(word, dict):
                    res["word_bounds_violations"] += 1
                    continue
                try:
                    ws = float(word["start"])
                    we = float(word["end"])
                except (KeyError, TypeError, ValueError):
                    res["word_bounds_violations"] += 1
                    continue
                if ws < start - 0.5 or we > end + 0.5:
                    res["word_bounds_violations"] += 1
        else:
            res["zero_word_segments"] += 1
            res["warnings"].append(
                "segment %d has no word timestamps (word_timestamps=True)"
                % index
            )
        parsed.append((start, end))
        prev_start = start
        prev_end = end

    if parsed:
        res["first_start"] = min(p[0] for p in parsed)
        res["last_end"] = max(p[1] for p in parsed)
        span = res["last_end"] - res["first_start"]
        active = sum(max(0.0, e - s) for s, e in parsed)
        if audio_duration and audio_duration > 0:
            res["span_coverage_pct"] = span / audio_duration * 100.0
            res["active_coverage_pct"] = active / audio_duration * 100.0
            if res["last_end"] > audio_duration + 5.0:
                res["errors"].append(
                    "last segment end %.2fs exceeds audio duration %.2fs by "
                    "more than 5s" % (res["last_end"], audio_duration)
                )
            if res["span_coverage_pct"] < 98.0:
                res["errors"].append(
                    "span coverage %.2f%% below 98%% threshold"
                    % res["span_coverage_pct"]
                )
        else:
            res["errors"].append(
                "audio_duration_seconds missing or zero in header"
            )
    else:
        res["errors"].append("no segments with valid timestamps")

    if res["total_words"] == 0:
        res["errors"].append("total word count is 0")
    if res["word_bounds_violations"]:
        res["warnings"].append(
            "%d word timestamps fall outside their segment bounds"
            % res["word_bounds_violations"]
        )
    repeat = detect_repetition_loop(segments)
    if repeat is not None:
        run, phrase, first_idx = repeat
        res["max_repeat_run"] = run
        res["warnings"].append(
            "possible repetition loop: the 6+-token phrase %r repeats %d "
            "times within a short window of consecutive segments (starting "
            "at segment %d); review required" % (phrase, run, first_idx)
        )
    res["ok"] = not res["errors"]
    return res
