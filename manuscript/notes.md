# Manuscript Notes — The Mystery of the Trinity: A Retreat with Fr. Peter Gruber, C.O.

*Pipeline draft assembled 2026-09-16. These notes accompany `Mystery_of_the_Trinity.md`.*

## Provenance

- Seven recordings (C01–C06 conferences, E01 engineering talk), transcribed with the pinned run `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, cpu/int8, greedy, `condition_on_previous_text=false`, word timestamps, VAD).
- Raw ASR JSON + raw transcripts are immutable evidence (`work/asr/`, `transcripts/raw/`).
- Clean transcripts (grammar-fixed, wording preserved, flags at topic boundaries) in `transcripts/clean/`; oral-to-written editorial layer in `transcripts/editorial/`; per-recording review logs in `work/review/`.
- Chapter drafts in `chapters/drafts/` each carry a `.provenance.md` sidecar mapping every section to transcript timestamps, verified sources, and disclosed editorial bridges. QA report: `work/review/G4_chapter_QA.md` (traceability sample 108/108 = 100%).
- Source ledger: `research/source_ledger.csv` (62 rows SRC-001…SRC-062) + verified excerpts in `research/verified_excerpts/`.

## Open items requiring the author (summary — full queue in `research/unresolved.md`)

1. **Human listening sign-off (handoff gate G2)** for all seven clean transcripts. Machine review used word-probability evidence; a human ear is required for ~100 flagged spots ([possibly:…], [unclear …]).
2. **SRC-024 — Benedict XVI "you are not made for comfort… made for greatness"** (Epilogue): not found in the official texts of the 20/21 Aug 2005 WYD homilies. Currently carried with `[quotation wording unverified]`; source must be located or the line recast.
3. **SRC-034 — "Bill Daniels" attribution** (Ch. 3, ~00:01:47): RESOLVED by owner 2026-09-16 — Bill Daniels is a retreatant on the retreat, not a published author; attribution removed from the chapter prose (bridge B17).
4. **C04 Benedict homily gap** (00:10:04–00:10:35, 31.4 s of audio lost to VAD): the chapter prints only the verified tail ("…of our friendship with him"); the human listener must recover the missing passage before fuller quotation.
5. **Scripture translation policy**: passages track the RSV family; several modernized/variant readings were kept as heard (Mt 28:18 "All power" vs RSV "authority"; Rom 12:2 "this age" vs "this world"). Author must choose the printed edition and normalize or footnote variants.
6. **Ratzinger page numbers** (SRC-001/002/003): wording verified against the 2004 edition, but pages 162/172/175 need physical-copy confirmation. The p.162 "mysterium" and p.175 observer passages appear in no talk — decide epigraph use or omit.
7. **St. Elizabeth of the Trinity prayer** (SRC-011): the standalone version heard matches no located published translation; the CCC ¶260 version is verified. Choose a printed text.
8. **DOCTRINAL_REVIEW items**: "one thing is three" (Ch. 5), subsistent relations/missions gloss (Ch. 2), Immaculate Conception framing and "passive tense" (Ch. 3), among others — need a qualified theological reviewer.
9. **Permissions**: CCC ¶¶199–267 long excerpt (SRC-009), ICEL Liturgy of the Hours antiphon (SRC-025), Rublev icon reproduction rights (SRC-013), and long quotations generally.
10. **Structural confirmations**: E01 as epilogue (evidence-based recommendation, owner has approved direction), chapter titles, closing Glory Be consolidation policy (Ch. 3 has none), Chesterton "poorly" vs "badly" (kept as heard, paraphrase), Weber reconstruction (00:31:57, human-listen first), eclipse "a year and a half ago" factual flag (Epilogue).
11. **Named reviewers**: transcript reviewer, voice reviewer, theological reviewer, citation/rights reviewer, final editor — per handoff Appendix B.

## Assembly details

- Order: `chapters/reviewed/ORDER.txt` (Ch. 1–6 + Epilogue).
- Assembled manuscript sha256: `e68152bd286723215f321b2d72fb39f10d8f605beb8f00784434950ad2f5619e` (2026-09-16 owner updates: official title page and provisional Note on the Text now emitted by `scripts/10_assemble_manuscript.py`).
- Notes and Sources section: generated from ledger rows with status VERIFIED_EXACT / VERIFIED_MINOR_VARIANT / PARAPHRASE_CONFIRMED (49 rows).
- Marker scan at assembly: 0 blocking markers; 20 intended `[possibly:…]` flags remain in prose.
