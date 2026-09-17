# Manuscript Notes — The Mystery of the Trinity

*Pipeline draft assembled 2026-09-16. These notes accompany `Mystery_of_the_Trinity.md`.*

## Provenance

- Seven recordings (C01–C06 conferences, E01 engineering talk), transcribed with the pinned run `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, cpu/int8, greedy, `condition_on_previous_text=false`, word timestamps, VAD).
- Raw ASR JSON + raw transcripts are immutable evidence (`work/asr/`, `transcripts/raw/`).
- Clean transcripts (grammar-fixed, wording preserved, flags at topic boundaries) in `transcripts/clean/`; oral-to-written editorial layer in `transcripts/editorial/`; per-recording review logs in `work/review/`.
- Chapter drafts in `chapters/drafts/` each carry a `.provenance.md` sidecar mapping every section to transcript timestamps, verified sources, and disclosed editorial bridges. QA report: `work/review/G4_chapter_QA.md` (traceability sample 108/108 = 100%).
- Source ledger: `research/source_ledger.csv` (71 rows SRC-001…SRC-071) + verified excerpts in `research/verified_excerpts/`.

## Open items — resolved vs remaining (synced 2026-09-17 with the owner's answers)

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
18. **Kavanagh credit (SRC-022)** — the book credits Aidan Kavanagh (*On Liturgical Theology* 1984, pp. 117–18), the phrase's originator, as quoted by Fagerberg; Ch. 3 prose names Kavanagh.
19. **St. John of the Cross "one Word in silence" (SRC-040)** — PARAPHRASE_CONFIRMED: paraphrased quote from memory; not printed as a verbatim quotation.
20. **Listening batches 1–2** — Q2/Q8/Q9/Q11 (batch 1) and Q22 "the resting" / Q10 "icon" (batch 2) resolved by owner listening; Q13 "saw you out" resolved by replacement. C01 "We [possibly: He] looked upon us" resolved ("He"); C02 "Jake" omitted per owner.
21. **Sign-of-the-cross / Glory Be policy applied** — all ritual sign-of-the-cross recitations and Glory Be prayers omitted from the book (Mt 28:19 Scripture quotations and prose about the sign of the cross retained); omissions recorded in `chapters/outlines/parking_lot.md` ("Owner omissions 2026-09-16").
22. **Integration complete** — Ch. 1–6 + Epilogue smoothing applied; QA: PASS_WITH_FINDINGS ×5 (ch1–6), PASS (epilogue); traceability 100%.
23. **First-retreat verification batch** — SRC-064…SRC-071 (8 rows) added to the ledger: O'Connor "Dogma is the guardian of mystery" (1959 letter — ch2 integration pending), Marshall-not-Chesterton brothel line (C03, attributed correctly), Newman Simon of Cyrene (C04), West "into me see" (C05, hedge form), Arinze anecdote (unverified — omitted from print), Dubay *Fire Within* (C05, bibliographic), Dante Paradiso XXXIII.145 (C05), Athanasius De Incarnatione 54.3 via CCC ¶460 (C06).

### Resolved (owner, 2026-09-17)

24. **Tolle Lege paper unpublished (rights OK)** — the 2013 "Marcel and Maritain on Mystery" submission was never published in Tolle Lege, so the author's own text is free to reuse and the earlier "confirm publication status" gate is closed. (The paper's internal quotations of the Marcel/Maritain translations remain flagged for permission review only if ever reprinted — see SRC-072/SRC-073.)
25. **Three intellectual thirsts skipped** — the paper's Maritain "three intellectual thirsts" material (*A Preface to Metaphysics*, First Lecture; SRC-073) is not integrated into the book.
26. **Inside title simplified** — the book title is "The Mystery of the Trinity" (subtitle dropped); the author line stays "by Fr. Peter Gruber, C.O." (`scripts/10_assemble_manuscript.py`).
27. **Prayer style** — prayers print as italic, indented set-off text with no subheading (the "## Opening Prayer" / "## Closing Prayer" headings are removed from the chapters); Ch. 3's second opening prayer ("Come, Holy Spirit") is removed.
28. **Contraction policy** — the speaker's contractions are kept as heard in print (restored where an earlier pass had expanded them).
29. **Uncle named Mark** — the uncle in the Trinity-Sunday-deadline story is named Mark ("Uncle Mark", Epilogue).
30. **Niece spelling Elisabeth** — the niece in the moon story (Ch. 2 and Epilogue) is spelled "Elisabeth".
31. **Radiating Christ prayer attribution** — the prayer prints attributed to St. John Henry Newman (the traditional attribution), per the owner.
32. **Genuine-Pusey correction** — the printed *Confessions* translation (X.27 opening prayer and the I.1 "restless hearts" passage) is confirmed to be E. B. Pusey's own; earlier notes describing the newadvent.org text as "J.G. Pilkington, a revision of Pusey" are corrected. The attribution line "trans. E. B. Pusey" stands.
33. **Flowing-page layout** — chapters flow continuously in the PDF (the title page and Table of Contents keep their own pages); no forced odd-page chapter starts or blank pages (`manuscript/build_pdf.py`).
34. **Word document deliverable** — `scripts/11_make_docx.py` generates `manuscript/Mystery_of_the_Trinity.docx` (Garamond 12 pt body, heading hierarchy, italic indented prayers) for the owner to edit in Word.

### Remaining

**Deferred owner questions:**

1. **Listening batches (handoff gate G2)** — remaining: E01 Q6 ("going to Mass"), Q7 ("Not this summer…"), Q12 ("mere"), Q21 ("at last"), plus the register forms and the other ~100 flagged spots.
2. **Pusey decision (SRC-025/026)** — RESOLVED (owner, 2026-09-17): the public-domain Pusey translation is adopted for the Augustine prayers, and the owner confirms the printed translation is genuinely Pusey's (see Resolved items 27/32 above). ICEL permission no longer applies to these quotations.
3. **Ch. 2 "as one in three" vs "three in one"** — context requested from the owner; pending.
4. **Ch. 3 "biology [possibly: physiology]"** — context requested from the owner; pending.
5. **RSV-2CE verification workflow** — queued per `research/verified_excerpts/RSV-2CE-plan.md`.
6. **Ratzinger page confirmation** — from the owner's physical 2004 copy (SRC-001/002/003); epigraph use of the p. 162 / p. 175 passages undecided.
7. **LeFrance book/page pin** (SRC-028).

**Pipeline items:**

8. **Augustine X.41.66 endnote recommendation (SRC-045)** — verification round 2: closest genuine source = Confessions X.41.66; keep the speaker's "apparently said" hedge + endnote X.41.66 (see SRC-045-verify.md).
9. **Citation-reviewer items** — Fagerberg page (SRC-022, credit now Kavanagh), Maritain page (SRC-020), John of the Cross saying number (SRC-040).
10. **Theological/rights reviewers** — DOCTRINAL_REVIEW items ("one thing is three" Ch. 5; subsistent relations/missions Ch. 2; Immaculate Conception framing + "passive tense" Ch. 3; confession quasi-materia Ch. 3); Rublev image rights (SRC-013); long-quote permissions. (ICEL SRC-025/026 closed via the Pusey decision — item 2 above.)
11. **Named reviewers** — transcript reviewer, voice reviewer, theological reviewer, citation/rights reviewer, final editor — per handoff Appendix B.

## Assembly details

- Order: `chapters/reviewed/ORDER.txt` (Ch. 1–6 + Epilogue).
- 2026-09-17: inside title simplified to "The Mystery of the Trinity" (subtitle dropped; `scripts/10_assemble_manuscript.py`) — the assembled manuscript sha256 changes at the next assembly run.
- Assembled manuscript sha256: `e68152bd286723215f321b2d72fb39f10d8f605beb8f00784434950ad2f5619e` (2026-09-16 owner updates: official title page and provisional Note on the Text now emitted by `scripts/10_assemble_manuscript.py`).
- Notes and Sources section: generated from ledger rows with status VERIFIED_EXACT / VERIFIED_MINOR_VARIANT / PARAPHRASE_CONFIRMED (52 rows).
- Marker scan at assembly: 0 blocking markers; 20 intended `[possibly:…]` flags remain in prose.
