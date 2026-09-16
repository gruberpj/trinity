# ARCHITECTURE.md — Mystery of the Trinity

## Build State

| Aspect | State |
|---|---|
| Project | Audio-to-book pipeline for "The Mystery of the Trinity", Fr. Peter Gruber, C.O. |
| Repository | `github.com/gruberpj/trinity` (public), branch `main`, SSH remote |
| Source audio | 7 M4A recordings (C01–C06 conferences, E01 engineering talk), originals read-only at project root, copies in `audio_original/` (untracked) |
| Transcription | COMPLETE — all 7 recorded, validated (coverage ≥99.6%), run `20260916_fasterwhisper_largev3_nocond` |
| Transcript review | COMPLETE (machine pass) — clean + editorial layers + review logs for all 7; human listening sign-off PENDING |
| Source ledger | 62 rows (SRC-001…062), 43 verified excerpts, unresolved queue maintained |
| Voice profile | `research/voice_profile.md` (24 timestamped exemplars) |
| Chapter map | `chapters/outlines/` — talk_map.md (73 segments), theme_matrix.md (18 themes), chapter_briefs.md (7 briefs) |
| Chapter drafts | 7 drafts + provenance sidecars in `chapters/drafts/`; G4 QA done (traceability 100%, findings fixed) |
| Manuscript | `manuscript/Mystery_of_the_Trinity.md` — assembled draft, 26,771 words, 7 parts (Ch. 1–6 + Epilogue), 0 blocking markers |
| Human gates | OPEN — transcript listen sign-off, theological review, citation/rights review, author decisions (see `manuscript/notes.md` and `research/unresolved.md`) |

## Pinned ASR configuration

engine: faster-whisper 1.2.1 · model: large-v3 · device: cpu · compute_type: int8 · language: en · word_timestamps: true · vad_filter: true · beam_size: 1 · temperature: 0 · condition_on_previous_text: false · run_id: 20260916_fasterwhisper_largev3_nocond.
Note: the initial greedy run (run_id `..._largev3`) exhibited a repetition-loop failure at C01 ~12:20; it is preserved as evidence. Config changes require a new run ID — never overwrite artifacts.

## Directory map (canonical, per handoff)

- `audio_original/` — immutable M4A copies (untracked)
- `source_material/` — handoff PDF, DOCX, extracted text
- `manifests/` — inventory.csv, checksums.sha256, asr_config.yaml
- `scripts/` — 01…10 deterministic pipeline (inventory, seed ledger, intake, transcribe, render, validate, extract sources, repository validation, manuscript assembly) + asrlib.py
- `work/` — normalized_audio, chunks, asr (JSON evidence), review logs (untracked)
- `transcripts/` — raw / clean / editorial layers
- `research/` — source_ledger.csv, verified_excerpts/, unresolved.md, voice_profile.md
- `chapters/` — outlines/ (map, matrix, briefs, parking_lot), drafts/ (+ provenance), reviewed/ (promoted, ORDER.txt)
- `manuscript/` — Mystery_of_the_Trinity.md, notes.md
- `logs/` — run jsonl (untracked)

## Verification commands

```
python3 scripts/06_validate_asr.py --id C01            # ASR integrity (G1)
python3 scripts/09_validate_repository.py              # marker scan + gates
python3 scripts/10_assemble_manuscript.py --dry-run    # assembly plan
shasum -c manifests/checksums.sha256                   # audio fingerprint check
```

## Decisions recorded

- E01 → Epilogue (owner instruction; evidence-based: self-contained, compresses ch. 2/3/5 themes, audience application).
- Transcription: local only (no hosted API), privacy-preserving.
- Chapters respect the author's spoken wording; only basic grammar fixes applied; all edits disclosed in provenance sidecars.
- No fabricated theology, quotations, or citations anywhere in the pipeline; unverifiable items carry explicit flags.
