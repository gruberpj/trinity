# Manuscript Notes — The Mystery of the Trinity: A Retreat with Fr. Peter Gruber, C.O.

*Pipeline draft assembled 2026-09-16. These notes accompany `Mystery_of_the_Trinity.md`.*

## Provenance

- Seven recordings (C01–C06 conferences, E01 engineering talk), transcribed with the pinned run `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, cpu/int8, greedy, `condition_on_previous_text=false`, word timestamps, VAD).
- Raw ASR JSON + raw transcripts are immutable evidence (`work/asr/`, `transcripts/raw/`).
- Clean transcripts (grammar-fixed, wording preserved, flags at topic boundaries) in `transcripts/clean/`; oral-to-written editorial layer in `transcripts/editorial/`; per-recording review logs in `work/review/`.
- Chapter drafts in `chapters/drafts/` each carry a `.provenance.md` sidecar mapping every section to transcript timestamps, verified sources, and disclosed editorial bridges. QA report: `work/review/G4_chapter_QA.md` (traceability sample 108/108 = 100%).
- Source ledger: `research/source_ledger.csv` (63 rows SRC-001…SRC-063) + verified excerpts in `research/verified_excerpts/`.

## Open items — resolved vs remaining (synced 2026-09-16 with the owner's answers)

### Resolved (owner, 2026-09-16)

1. **C04 Benedict homily** — full quote restored in Ch. 4 from the DOCX (matches vatican.va verbatim); the 31.4 s audio gap is noted but no longer limits the quotation.
2. **Scripture translation policy** — POLICY RECORDED: target RSV-2CE unless substantial deviation; see `research/verified_excerpts/RSV-2CE-plan.md`; verification workflow queued. Mt 18:20 row added (SRC-063); SRC-046 C04 anchor added.
3. **SRC-024 (Benedict "made for greatness")** — rendered as paraphrase, no quotation marks; endnote handled later (`SRC-024-origin.md` pending).
4. **SRC-034 ("Bill Daniels")** — a retreatant on the retreat; attribution removed from the prose (bridge B17).
5. **St. Elizabeth of the Trinity prayer (SRC-011)** — CCC ¶260 official text now prints in Ch. 2 and Ch. 4.
6. **St. Patrick's Breastplate (SRC-012)** — asterisk dropped.
7. **CCC ¶¶199–267 (SRC-009)** — the excerpt will NOT be printed; permissions handled later.
8. **Chesterton (SRC-023)** — exact wording printed, followed by the author's correction: "I would correct Chesterton here. Anything worth doing is worth doing poorly."
9. **Weber (SRC-030)** — removed from Ch. 3 and the Epilogue; recast as "living in an enchanted world."
10. **"Law of the gift" (SRC-038)** — "as it is commonly called" hedge + George Weigel endnote confirmed.
11. **Giussani (SRC-036)** — commonly cited aphorism; rendered with attribution, no quotation marks.
12. **Thérèse (SRC-027/028/029/041)** — "Everything is grace" dated 5 June 1897; C01 attribution → Thérèse; E01 → "her Last Conversations"; the SRC-028 line was found by the owner in a Jean LeFrance book (usual published spelling: "Jean Lafrance") — book/page pin pending.
13. **Rublev dating (SRC-013)** — "most accurate": c. 1411 or 1425–1427; ROC custody (`SRC-013-dating.md` pending).
14. **Eclipse flag** — "the eclipse of April 2024."
15. **C03 closing Glory Be** — unparked; appended as the chapter's "## Closing Prayer".
16. **C01 amen/tent-peg etymology** — excised per owner (Hebrew "tent peg" = *yated*); the intimus note remains valid.
17. **Ratzinger pages (SRC-001/002/003)** — the owner has the physical 2004 Ignatius copy; page confirmation to follow.

### Remaining

1. **Human listening sign-off (handoff gate G2)** — ~100 flagged spots, incl. the register forms and the E01 review Q1–Q29 queue (listening batches).
2. **RSV-2CE verification workflow** — queued per `research/verified_excerpts/RSV-2CE-plan.md`.
3. **Ratzinger page confirmation** — from the owner's physical 2004 copy (SRC-001/002/003); epigraph use of the p. 162 / p. 175 passages undecided.
4. **LeFrance book/page pin** (SRC-028).
5. **Citation-reviewer items** — Fagerberg page (SRC-022), Maritain page (SRC-020), John of the Cross saying number (SRC-040), Augustine "deepest wound" hedge (SRC-045).
6. **Theological/rights reviewers** — DOCTRINAL_REVIEW items ("one thing is three" Ch. 5; subsistent relations/missions Ch. 2; Immaculate Conception framing + "passive tense" Ch. 3; confession quasi-materia Ch. 3); ICEL (SRC-025/026); Rublev image rights (SRC-013); long-quote permissions.
7. **Named reviewers** — transcript reviewer, voice reviewer, theological reviewer, citation/rights reviewer, final editor — per handoff Appendix B.

## Assembly details

- Order: `chapters/reviewed/ORDER.txt` (Ch. 1–6 + Epilogue).
- Assembled manuscript sha256: `e68152bd286723215f321b2d72fb39f10d8f605beb8f00784434950ad2f5619e` (2026-09-16 owner updates: official title page and provisional Note on the Text now emitted by `scripts/10_assemble_manuscript.py`).
- Notes and Sources section: generated from ledger rows with status VERIFIED_EXACT / VERIFIED_MINOR_VARIANT / PARAPHRASE_CONFIRMED (52 rows).
- Marker scan at assembly: 0 blocking markers; 20 intended `[possibly:…]` flags remain in prose.
