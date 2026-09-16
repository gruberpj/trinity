# G4 Chapter QA — Book-Level Review (Mystery of the Trinity)

- **Gate:** G4 (chapter QA). **Reviewer role:** independent chapter QA (book level). **Date:** 2026-09-16.
- **Scope:** all 7 drafts (`chapters/drafts/`) + provenance sidecars + briefs + theme matrix + voice profile + source ledger + clean transcripts.
- **Method:** repository marker scan (`09_validate_repository.py`); traceability sampling (108 substantive sentences, spread across all 7 chapters, each traced to clean-transcript anchor / verified ledger row / disclosed bridge); full quotation-fidelity audit vs ledger + clean transcripts; voice-delta check vs voice_profile.md; cross-chapter consistency pass; full independent verification of ch. 4 by the QA reviewer. Read-only. No draft modified.
- **Note:** `chapters/outlines/parking_lot.md` is under repair by another agent. Its sections (E01, C01–C06) are present and the provenance sidecars' parking references resolve; no chapter is failed for parking-lot state.

## Marker scan (script output)

`python3 scripts/09_validate_repository.py` → **BLOCKED: gate G5 FAILS**, on one blocking occurrence:
- `chapters/drafts/03_gift_and_liturgy.provenance.md:121` — `[VERIFY]`. **False positive:** the occurrence is the sidecar's own self-referential verdict line, "voice-profile compliant; no [VERIFY]-worthy vocabulary drift found." It is not an unresolved marker. **Fix (mechanical):** reword that line before manuscript assembly so the G5 scan passes.
- Chapter prose contains ONLY intended flags: `[possibly:...]` (20 in prose), `[quotation wording unverified]`, `[attribution questioned; see chapter note]`. No `[VERIFY]`/`[TODO]` in any chapter body. ✓
- Warning-class markers in sidecars (ATTRIBUTION_UNCONFIRMED, LOCATOR_MISSING, DOCTRINAL_REVIEW, PERMISSION_REVIEW) are status labels with owners in `research/unresolved.md` — expected, never gate-failing.

## Verdicts per chapter

| Chapter | Verdict |
|---|---|
| 01 Icons of the Trinity | PASS_WITH_FINDINGS |
| 02 Mystery | PASS_WITH_FINDINGS |
| 03 Gift and Liturgy | PASS_WITH_FINDINGS |
| 04 Relationship | PASS_WITH_FINDINGS (QA-verified in full) |
| 05 Intimacy | **FAIL** (1 HIGH: Ratzinger quotation) |
| 06 Evangelization | PASS_WITH_FINDINGS |
| Epilogue — Engineering Mystery | **FAIL** (1 HIGH: Chesterton quotation) |

## Findings by severity

### 🔴 HIGH (2)

- **H1 [epilogue_engineering_mystery.md:155 / provenance line 97 — Chesterton, SRC-023]** Draft prints `And he says, no — that's not true. "Whatever is worth doing is worth doing poorly."` — quotation marks around wording Chesterton never wrote. Ledger (SRC-023, PARAPHRASE_CONFIRMED): Chesterton's words are "if a thing is worth doing, it is worth doing badly"; "worth doing poorly" is the speaker's own rendering. The quotation marks were **added by the drafter** (E01 clean 00:37:49 has the sentence unquoted), and the epilogue's own provenance line 97 claims "Chesterton-as-heard … rendered without quotation marks." Violates: handoff "paraphrases are not quoted" + Appendix B "Direct quotations match the selected edition." **Fix:** remove the quotation marks (keep as reported speech), or print the verified wording ("…worth doing badly") with attribution; correct provenance line 97. (unresolved.md Stage 2 item 4 is the authoritative decision entry.)
- **H2 [05_intimacy.md:37 / provenance §2 line 45 — Ratzinger fifth transcendental, LOCATOR_MISSING]** Draft prints quotation marks around the fifth-transcendental passage (`Joseph Ratzinger said, "Well, maybe there's a fifth transcendental…"`) with **no** `[quotation wording unverified]` label, while the provenance sidecar states "Rendered as heard paraphrase, NO quotation marks, never asserted as verified" — the draft contradicts its own sidecar. The heard quotation has no ledger row (LOCATOR_MISSING), so per handoff §5 it may only appear in quotation marks if verified or labeled. Every other unverified quotation in the book carries the label (01:37, 01:71, 01:87, 05:79, 06:49, epilogue:127/171). **Fix:** de-quote to reported speech (as the sidecar already claims), or add `[quotation wording unverified]`; make sidecar and draft agree.

### 🟡 MED (8)

- **M1 [03_gift_and_liturgy.md:83]** Chapter ends at "Saint Paul says, 'Give thanks.'" with no closing sign-of-the-cross + Glory Be, unlike every other chapter. Brief's global note requires the author to decide (keep per-chapter or consolidate) — currently flagged in sidecar + parking lot, not silently deleted, but the book is inconsistent until the author rules. Resolve before assembly.
- **M2 [05_intimacy.md:85 / provenance §5 line 63]** `"Each one of us is the result of a thought of God," Pope Benedict said` — printed in quotation marks with attribution while the ledger's VERIFIED_EXACT text reads "**Each of us** is the result of a thought of God." The sidecar labels it "SRC-004 … VERIFIED_EXACT — printed in quotation marks" without disclosing the one-word heard variant. Fix: disclose the variant (as done for Jn 14:6 etc.) or normalize to the verified wording; citation reviewer rules.
- **M3 [02_mystery.md:5, 04_relationship.md:5 — SRC-011]** Both Elizabeth of the Trinity opening prayers print a translation that "matches NO located published translation" (unresolved.md C, ATTRIBUTION_UNCONFIRMED). Ch. 2 adds the attribution line "— Prayer of St. Elizabeth of the Trinity"; ch. 4 names no saint (audio names none). Translation identity must be resolved (or swapped for the CCC ¶260 official text) before publication; attribution practice should also be harmonized.
- **M4 [03_gift_and_liturgy.md:77 — SRC-028]** "St. Thérèse says, prayer [possibly: love] is to be poured out into another." — quotation marks correctly withheld, but the attribution is asserted unhedged though the source is ATTRIBUTION_UNCONFIRMED (no located Thérèse text; the heard word itself is uncertain). Author must supply the source or the line is recast (unresolved Stage 2 item 6c).
- **M5 [06_evangelization.md:29]** "it actually belongs to a rather intellectual saint of the 19th century, an Oratorian priest named John Henry Newman" asserts the contested authorship as fact in prose, in tension with the chapter's own note (line 9: "the attribution is questioned by some scholars") and the flagged form at line 25. Carry the hedge into line 29 or generalize.
- **M6 [05_intimacy.provenance.md:93]** Sidecar claims "All other wording follows the clean transcript." False: ≈10 undisclosed micro-edits, including a full clause deletion ("Next week you'll hear it as your first reading at Mass, where"), "I mentioned before that" removed, "the Rublev's icon"→"the Rublev icon", "We try to find God and beauty that is derivative"→"God in beauty" (semantic touch-up of probable ASR error). No invented content, but G4 requires disclosed bridges; amend the sidecar.
- **M7 [03_gift_and_liturgy.provenance.md:72]** "Bridge count: 11. All are connective/rendering only" omits: exitus–reditus sentence repair (dropped "with a U-S at the end"/"R-E-D-I-T-U-S"), cruise-control compression beyond B6's description, "our Father"→"Our Father", and an **unlogged sentence relocation** ("In engineering, a positive feedback loop is destructive…" moved from the 00:19:42 block to close the mic-screech paragraph). Amend the bridge ledger.
- **M8 [05_intimacy.md:5-7 — SRC-025]** The opening prayer prints the ICEL Liturgy of the Hours wording of Confessions X.27 at length; ICEL © permission is required (unresolved item 17) or swap to the public-domain Pusey rendering. Rights reviewer to close before publication.

### 🟢 LOW (10)

- **L1** Glory Be rendered three ways across the book: ch. 1/2/6/epilogue with Oxford commas + italics (ch. 2 only), ch. 4/5 without commas, ch. 3 absent (M1). Each matches its own transcript's heard form, but the fixed liturgical formula needs one house rendering (author decision already queued).
- **L2 [01:21 vs 06:17]** Mt 28:18 rendered two ways ("All power in heaven and on earth…" vs "all authority in heaven and earth has been given over to me") — both heard-authentic; edition-choice note (unresolved F) needed at book level.
- **L3 [05:5-7 vs epilogue:125]** Augustine Confessions rendered differently (ICEL "O Beauty ever ancient…" vs heard "Beauty ever ancient, ever new — late have I loved you!" + I.1 "yourselves…thee" blend). Both transcript-faithful; recommend a book-level note.
- **L4 [01:37 vs 03:29]** Gen 1:26 "Let us create" carries `[quotation wording unverified]` in ch. 1 but not ch. 3 — harmonize flag usage.
- **L5 [research/source_ledger.csv SRC-058]** anchor "00:23:32" points at the Glory Be block; the "Give thanks" sentence is in the 00:22:56 block. Fix the anchor.
- **L6 [02:67-73 vs epilogue:69-77]** The moon story's facts differ between ch. 2 (five years old; brother-in-law's family; "Jake [possibly: 'kay]") and the epilogue (four-year-old; niece's grandmother; parallax joke). Variants are policy-sanctioned and correctly NOT merged (voice profile §9.6) — no fix to prose; consider a book-level note for readers.
- **L7 [01_icons_of_the_trinity.md:95 / parking_lot C01.2]** The signature "We're at 21 minutes and I'm sorry. But you're permitted to groan." aside is removed per the brief ("keep only if voice review approves"). Disclosed and preserved in the parking lot, but voice-profile restraint §9.1 says do not smooth it away — the voice reviewer must rule explicitly.
- **L8 [epilogue:193-195]** Closing sequence re-sequenced (single In-the-name relocated after the B14 bridge; "Thank you, everyone." parked) — not itemized as a bridge. Also three small speaker-text cuts unlisted in the sidecar lists.
- **L9 [01_icons_of_the_trinity.provenance.md:134]** "zero remaining differences" is word-level only; 10 quote-punctuation placements differ from the transcript (covered by the "lightly punctuated for print" commitment — worth one sentence).
- **L10 [06:25/27]** Mt 25 and Acts 9 dramatizations printed in quotation marks without ledger rows — disclosed as heard dramatization; consider wording-flags if they will read as Scripture citations in print.

## Cross-chapter consistency (verified OK)

- Chapter titles match the briefs (1–6 + "Epilogue — Engineering Mystery"). ✓
- Prayer bookends: each chapter opens with its own talk's prayer (Breastplate / Elizabeth I / Ps 42 / Elizabeth II / Confessions / Radiating Christ / Marian prayer + Rom 12:2); closes on Glory Be except ch. 3 (M1). ✓
- "The love that made the sun and the stars" refrain preserved with the correct per-chapter variants: ch. 2, 3, 6 = the refrain; ch. 4 = "before the sun and the stars"; epilogue = solar-flare/strewn-stars variant. ✓
- Story variants NOT merged (voice profile §9.6): moon story (C02 vs E01), waiting-friend (C05 Giant Eagle vs E01 couch), fivefold litany (C04 "Motherhood expresses it… when it does not despair, adores it" vs E01 "Motherhood embraces it… does not give in to despair — adores it"). Each chapter keeps its own variant. ✓
- Epilogue recapitulation of ch. 2/3/5 themes is compressed callbacks, consistent with the chapters (B14 "Christ sleeps in the boat" matches ch. 5; *intimus* compressed to one line per theme-matrix rule). No contradictions found. ✓
- "Fr. Peter" naming: only the epilogue names him ("Father Peter Gruber"); ch. 1–6 retain the conference register. Consistent. ✓
- No off-profile vocabulary found in any draft (no *perichoresis*, no *consubstantial*); hedges, asides, and pastoral direct address survive. ✓

## Traceability sample table (summary; full per-sentence evidence in the four mule sub-check reports)

| Chapter | Sampled | Traced | Failed |
|---|---|---|---|
| 01 Icons of the Trinity | 16 | 16 | 0 |
| 02 Mystery | 15 | 15 | 0 |
| 03 Gift and Liturgy | 16 | 16 | 0 |
| 04 Relationship | 13 | 13 | 0 |
| 05 Intimacy | 12 | 12 | 0 |
| 06 Evangelization | 12 | 12 | 0 |
| Epilogue | 24 | 24 | 0 |
| **Total** | **108** | **108** | **0** |

**Trace ratio: 108/108 = 100%.** Zero failed traces. Every sampled sentence anchored to a clean-transcript block, a ledger row with its stated status, or a disclosed editorial bridge. No invented theology, examples, transitions, or citations found in any chapter. Ch. 4's SRC-004 gap gate verified directly by QA: only the ellipsis fragment "…of our friendship with him." appears; no other homily wording anywhere.

## Blocks assembly? (only HIGH + mechanical gate fixes)

1. **Epilogue (H1):** Chesterton line 155 — remove the quotation marks (paraphrase) or print the verified wording "if a thing is worth doing, it is worth doing badly"; reconcile provenance line 97. → MUST fix before assembly.
2. **Ch. 5 (H2):** line 37 — de-quote the Ratzinger passage to reported speech (or add `[quotation wording unverified]`); reconcile provenance §2 line 45. → MUST fix before assembly.
3. **Mechanical:** reword the self-referential `[VERIFY]` mention in `03_gift_and_liturgy.provenance.md:121` so the G5 repository scan passes. → MUST fix before assembly.

All MED items (M1–M8) are tracked author/reviewer decisions and do not block assembly of a review manuscript, but each should have a named owner before a final release.

