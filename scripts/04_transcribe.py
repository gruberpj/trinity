#!/usr/bin/env python3
"""Prompt B/C (pilot and batch transcription): transcribe one recording with
the pinned ASR configuration from manifests/asr_config.yaml.

Usage: python3 scripts/04_transcribe.py --id C01

Pipeline per recording:
  1. Verify the source copy in audio_original/ against manifests/inventory.csv.
  2. Skip if a valid .done.json marker exists whose input/config/output hashes
     all match (handoff section 9: never overwrite a validated artifact).
  3. Transcribe with the pinned config (cpu/int8, beam_size=1, temperature=0,
     condition_on_previous_text=false, word timestamps, VAD filter, English).
  4. Write work/asr/{ID}.asr.{run_id}.json via .partial -> validate -> atomic
     rename, then a .done.json marker.
  5. Append JSON lines to logs/{run_id}.jsonl.

On any error: log, exit nonzero, leave the .partial file for inspection.
Engine output text is immutable evidence: this script never edits it.
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

import asrlib


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def log(run_id, recording_id, event, detail=None):
    os.makedirs(asrlib.LOGS_DIR, exist_ok=True)
    entry = {"ts": utc_now(), "id": recording_id, "event": event}
    if detail is not None:
        entry["detail"] = detail
    path = os.path.join(asrlib.LOGS_DIR, "%s.jsonl" % run_id)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, default=str) + "\n")


def fail(run_id, recording_id, message):
    log(run_id, recording_id, "error", {"message": message})
    print("ERROR: %s" % message, file=sys.stderr)
    sys.exit(1)


def atomic_write_json(path, doc):
    """json.dump into path.partial, fsync, then atomically rename to path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".partial"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, default=str)
        fh.write("\n")
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


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
    cfg_hash = asrlib.config_fingerprint(cfg)

    basename = asrlib.ID_MAP[recording_id]
    source = os.path.join(asrlib.AUDIO_DIR, basename)
    if not os.path.isfile(source):
        fail(run_id, recording_id, "source file missing: %s" % source)
    source_sha256 = asrlib.sha256_file(source)
    inv_sha256, inv_duration = asrlib.manifest_sha256(recording_id)
    if source_sha256 != inv_sha256:
        fail(
            run_id,
            recording_id,
            "source sha256 %s does not match manifest %s for %s"
            % (source_sha256, inv_sha256, basename),
        )

    out_path = asrlib.asr_json_path(recording_id, run_id)
    done_path = asrlib.asr_done_path(recording_id, run_id)

    # Skip logic (handoff section 9): a done marker alone is not enough; the
    # input, config, and output hashes must all match.
    if os.path.isfile(done_path):
        try:
            with open(done_path, encoding="utf-8") as fh:
                done = json.load(fh)
            marker_ok = (
                done.get("input_sha256") == source_sha256
                and done.get("config_sha256") == cfg_hash
                and os.path.isfile(out_path)
                and done.get("output_sha256") == asrlib.sha256_file(out_path)
            )
        except (OSError, ValueError) as exc:
            fail(
                run_id,
                recording_id,
                "unreadable done marker %s: %s" % (done_path, exc),
            )
        if marker_ok:
            log(
                run_id,
                recording_id,
                "skip",
                {"reason": "valid done marker, hashes match"},
            )
            print("SKIPPED (valid existing output): %s" % out_path)
            return
        fail(
            run_id,
            recording_id,
            "existing %s does not validate against current source/config; "
            "manual inspection required (refusing to overwrite)" % done_path,
        )
    if os.path.isfile(out_path):
        fail(
            run_id,
            recording_id,
            "output %s exists without a valid done marker; move it aside "
            "manually before rerunning" % out_path,
        )

    audio_duration = asrlib.probe_duration_seconds(source)
    if abs(audio_duration - inv_duration) > 0.5:
        log(
            run_id,
            recording_id,
            "duration_check",
            {"probed_seconds": audio_duration, "manifest_seconds": inv_duration},
        )

    started_at = utc_now()
    wall_start = time.monotonic()
    log(
        run_id,
        recording_id,
        "start",
        {
            "source": os.path.join("audio_original", basename),
            "source_sha256": source_sha256,
            "audio_duration_seconds": round(audio_duration, 3),
            "run_id": run_id,
            "config_sha256": cfg_hash,
        },
    )

    try:
        import faster_whisper

        model = faster_whisper.WhisperModel(
            cfg["model"], device=cfg["device"], compute_type=cfg["compute_type"]
        )
        log(
            run_id,
            recording_id,
            "model_loaded",
            {"model": cfg["model"], "engine_version": faster_whisper.__version__},
        )

        segments_iter, info = model.transcribe(
            source,
            language=cfg["language"],
            word_timestamps=cfg["word_timestamps"],
            vad_filter=cfg["vad_filter"],
            beam_size=cfg["beam_size"],
            temperature=cfg["temperature"],
            condition_on_previous_text=cfg.get("condition_on_previous_text", True),
            initial_prompt=cfg["initial_prompt"],
        )

        segments = []
        last_progress = time.monotonic()
        for seg in segments_iter:
            words = [
                {
                    "word": word.word,
                    "start": word.start,
                    "end": word.end,
                    "probability": word.probability,
                }
                for word in seg.words
            ]
            segments.append(
                {
                    "id": seg.id,
                    "start": seg.start,
                    "end": seg.end,
                    "text": seg.text,
                    "words": words,
                }
            )
            if time.monotonic() - last_progress >= 30:
                last_progress = time.monotonic()
                log(
                    run_id,
                    recording_id,
                    "progress",
                    {
                        "segments": len(segments),
                        "audio_at_seconds": round(seg.end, 1),
                        "audio_duration_seconds": round(audio_duration, 3),
                    },
                )

        finished_at = utc_now()
        wall_seconds = time.monotonic() - wall_start

        doc = {
            "header": {
                "recording_id": recording_id,
                "source_sha256": source_sha256,
                "run_id": run_id,
                "engine": cfg["engine"],
                "engine_version": faster_whisper.__version__,
                "model": cfg["model"],
                "device": cfg["device"],
                "compute_type": cfg["compute_type"],
                "language": cfg["language"],
                "word_timestamps": cfg["word_timestamps"],
                "vad_filter": cfg["vad_filter"],
                "beam_size": cfg["beam_size"],
                "temperature": cfg["temperature"],
                "condition_on_previous_text": cfg.get(
                    "condition_on_previous_text", True
                ),
                "initial_prompt": cfg["initial_prompt"],
                "started_at": started_at,
                "finished_at": finished_at,
                "audio_duration_seconds": round(audio_duration, 3),
            },
            "segments": segments,
        }

        tmp_path = out_path + ".partial"
        try:
            with open(tmp_path, "w", encoding="utf-8") as fh:
                json.dump(doc, fh, indent=2)
                fh.write("\n")
                fh.flush()
                os.fsync(fh.fileno())
        except OSError as exc:
            fail(
                run_id,
                recording_id,
                "failed writing %s: %s" % (tmp_path, exc),
            )

        with open(tmp_path, encoding="utf-8") as fh:
            reloaded = json.load(fh)
        result = asrlib.validate_asr(reloaded, audio_duration)
        if not result["ok"]:
            log(
                run_id,
                recording_id,
                "validation_failed",
                {"errors": result["errors"], "warnings": result["warnings"]},
            )
            fail(
                run_id,
                recording_id,
                "pre-rename validation failed; .partial left at %s" % tmp_path,
            )

        os.replace(tmp_path, out_path)
        output_sha256 = asrlib.sha256_file(out_path)

        done_doc = {
            "recording_id": recording_id,
            "run_id": run_id,
            "input_path": os.path.join("audio_original", basename),
            "input_sha256": source_sha256,
            "output_path": os.path.join(
                "work", "asr", os.path.basename(out_path)
            ),
            "output_sha256": output_sha256,
            "config": cfg,
            "config_sha256": cfg_hash,
            "started_at": started_at,
            "finished_at": finished_at,
            "wall_seconds": round(wall_seconds, 3),
            "rtf": (
                round(wall_seconds / audio_duration, 4) if audio_duration else None
            ),
            "engine_version": faster_whisper.__version__,
            "python_version": sys.version.split()[0],
            "engine_duration_seconds": round(info.duration, 3),
            "engine_language": info.language,
            "validation": {
                "ok": True,
                "segment_count": result["segment_count"],
                "span_coverage_pct": round(result["span_coverage_pct"], 2),
                "active_coverage_pct": round(result["active_coverage_pct"], 2),
                "total_words": result["total_words"],
                "gaps_over_10s": result["gaps_over_10s"],
                "max_repeat_run": result["max_repeat_run"],
                "warnings": result["warnings"],
            },
        }
        atomic_write_json(done_path, done_doc)
    except Exception as exc:  # noqa: BLE001 - log everything, leave evidence
        fail(
            run_id,
            recording_id,
            "%s: %s" % (type(exc).__name__, exc),
        )

    log(
        run_id,
        recording_id,
        "done",
        {
            "output_sha256": output_sha256,
            "wall_seconds": round(wall_seconds, 3),
            "rtf": done_doc["rtf"],
            "segments": len(segments),
            "total_words": result["total_words"],
            "span_coverage_pct": round(result["span_coverage_pct"], 2),
        },
    )
    print("DONE %s -> %s" % (recording_id, out_path))
    print(
        "  segments=%d words=%d rtf=%.3f wall=%.1fs"
        % (len(segments), result["total_words"], done_doc["rtf"], wall_seconds)
    )
    print(
        "  span coverage %.2f%% (>=98 required)" % result["span_coverage_pct"]
    )


if __name__ == "__main__":
    main()
