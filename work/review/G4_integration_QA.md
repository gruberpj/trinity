# G4 Integration + Smoothing QA — First-Retreat Supplements

**Date:** 2026-09-16 · **Scope:** chapters 1, 3, 4, 5, 6, Epilogue (ch. 2 excluded — separate agent)
**Gate:** G4-style recheck of the 2026-09-16 integration + smoothing pass (owner duties 1–2).
**Method:** word-level trace of every integrated supplement against `work/review/first_retreat_mine_talks12.md` / `talks34.md` / `talks56.md`; attribution word-checks against `research/verified_excerpts/SRC-064…071`; smoothing before→after spot-checks; flag inventory vs `scripts/09_validate_repository.py`; drafts-vs-reviewed diff. Reviewed by 4 parallel QA mules; all HIGH/MEDIUM claims independently re-verified against the source files.

---

## 1. Per-chapter verdicts

| Chapter | Verdict | Supplements traced | Trace ratio |
|---|---|---|---|
| 01 — Icons of the Trinity | **PASS_WITH_FINDINGS** | 11/11 (+ T1-D correctly excluded) | 100% |
| 03 — Gift and Liturgy | **PASS_WITH_FINDINGS** | 23/23 | 100% |
| 04 — Relationship | **PASS_WITH_FINDINGS** | 4/4 | 100% |
| 05 — Intimacy | **PASS_WITH_FINDINGS** | 16/16 | 100% |
| 06 — Evangelization | **PASS_WITH_FINDINGS** | 8/8 | 100% |
| Epilogue — Engineering Mystery | **PASS** | 0 (none expected — E01 source talk, not first-retreat) | n/a |

**Overall trace ratio: 62/62 = 100%. Zero FAILED traces.** No content in any in-scope chapter that matches no mine item or clean transcript was found (two initially-suspect ch. 1 sentences verified against the clean transcript: "He undergoes that out of love for us…" 00:18:46 and "No storms can disturb me" 00:20:55).

## 2. Traceability table (supplement → mine → chapter)

| Supplement | Mine | Chapter location | Result |
|---|---|---|---|
| T1-A…T1-L (11) | `first_retreat_mine_talks12.md` Talk 1 | ch1 §§2–11 (see `01_…provenance.md` §8.1) | All PASS; skipped portions absent as disclosed |
| T4-1, T4-2, T4-6, T4-8, T4-9 | `first_retreat_mine_talks34.md` Talk 4 | ch3 opening/§"The Trinity of love that overflows"/§"Mary's yes" | All PASS |
| T5-S1…T5-S7 | `first_retreat_mine_talks56.md` Talk 5 | ch3 §§"Mary's yes"/"Baptism: inserted into the Trinity" | PASS; T5-S7 tail drop under-disclosed (F-1) |
| T4-4 (Marshall) | talks34 T4-4 + SRC-065 | ch3 §"Everything is positive" | PASS — SRC-065 wording word-exact, attributed Bruce Marshall, Chesterton 0× |
| T3-16, T3-15, T4-3, T3-14, T4-5, T4-10, T4-7, T4-11, T4-13, T4-12 (C03 half) | talks34 Talks 3–4 | ch3 §§"Everything is positive"/"The enchanted world…"/"Deep calls to deep"/"Give thanks" | All PASS |
| T3-2, T3-8, T5-S10, T5-S15 | talks34/56 | ch4 §"Knowing…"/§"Encounter…"/closing | All PASS; Newman line (SRC-066) unquoted paraphrase, correct |
| T5-S8, S11, S12, S13, S14 | talks56 Talk 5 | ch5 §§"Being itself"/"Contemplation"/etc. | PASS; T5-S8 micro-drops undisclosed (L-5) |
| T6-S1…T6-S8, T6-S10, T6-S11, T6-S12 | talks56 Talk-5 tail | ch5 throughout | All PASS |
| T6-S13…T6-S20 (8) | talks56 Talk 6 | ch6 §§"Back to St. Patrick"/"Owning the mystery"/"Living it…"/"Missa est"/"Floodgates" | All PASS; CCC ¶460 wording word-exact |

## 3. Severity-tiered findings

### 🟠 HIGH

- **H-1 — SRC-064…SRC-071 have no rows in `research/source_ledger.csv`, and the gap is largely undisclosed.** The ledger's highest row is SRC-063. Five provenance files cite SRC-064–071, four of which feed **printed prose**: SRC-065 (Marshall, printed ch3), SRC-066 (Newman, printed ch4), SRC-067 (West, printed ch5), SRC-070 (Dante echo, printed ch5), SRC-071 (Athanasius/CCC ¶460, printed ch6). Only SRC-064 and SRC-069 are disclosed as ledger-less (and only inside mine files: `talks34.md:48`, `talks56.md:77`); nothing in `research/unresolved.md` or any chapter provenance records the gap for SRC-065/066/067/070/071. **Fix:** append 8 rows to `source_ledger.csv` with the statuses from the verified-excerpt files (SRC-065 ATTRIBUTION_UNCONFIRMED, SRC-068 ATTRIBUTION_UNCONFIRMED, others PARAPHRASE_CONFIRMED/VERIFIED_EXACT), or record the gap in `research/unresolved.md` before rebuild.

### 🟡 MEDIUM

- **M-1 — ch3 provenance item 8 (T5-S7) under-discloses a dropped sentence.** `03_gift_and_liturgy.provenance.md` discloses only "garbled banter fragments dropped" and "Self-deprecating tail kept", but the mine's coherent closing sentence — "Or if I'm just tagging along, I could sit there in choir, and maybe put a stole on after the Agnus Dei, because that's what you do." (`talks56.md:51`) — is absent from ch3 (text ends at "Only the main celebrant is doing that."). A fun-fact sentence, not garbled; its drop should be itemized.
- **M-2 — SRC-064 / O'Connor ("Dogma is the guardian of mystery", 1959 letter, VERIFIED_EXACT) omitted from ch3's consulted-excerpts disclosure.** ch3 provenance:30 says "SRC-065…SRC-070 consulted" and the "Not integrated" paragraph (:56) names SRC-066/067/068/069/070 but **not SRC-064**. Mine T3-4 (which SRC-064 supports) is not integrated into any chapter — confirmed absent from ch1/3/4/5/6 text. The non-integration decision is therefore undocumented at chapter level for this excerpt (the mine's "no ledger row" note is the only trace). Also: mine T3-4's own insertion suggestions were C03 sections, so the "C04/C02/E01 targets" bucket rationale in ch3:56 does not cleanly cover it.

### 🟢 LOW

- **L-1 — ch1 §8.2 smoothing log is not exhaustive.** ≥8 additional undisclosed micro-edits exist in the chapter (e.g., "to have an image around which could later be corrected, modified, where…" → "…that could later be corrected, modified, and through which…"; "there is the tree — the tree," → "there is the tree,"; "That symbolized" → "That symbolizes"). All meaning-preserving; the log's implied completeness is the issue. The §4 fidelity proof (3,786-word exact match) is explicitly "at draft creation" and no longer provable.
- **L-2 — ch4 provenance §14 item 2 (T3-8) cut span wider than disclosed.** Beyond the two named doctrinal-flag sentences, the passage "God [unclear] — he continues to draw us to himself." and "because we look at Christ crucified — this is Christ taking on all of our sins…" were omitted without individual disclosure.
- **L-3 — ch3 provenance item 20 (T4-7) under-discloses drops.** The packet sentence ("I included that in your packet because it was a meaningful psalm for me…") and the closing "That is what we do in liturgy." are absent but not itemized.
- **L-4 — ch4 T4-12 C04-half non-integration not disclosed.** The coworker/classmate/stranger sentence and "Everyone is potentially someone to love" (mine's C04 target) were not integrated anywhere in ch4; the provenance notes only the variant-non-merge, not the skip decision.
- **L-5 — ch5 T5-S8 has two undisclosed micro-drops.** Mine's "We'll get into this later. 'I am who I am' — we kind of extrapolate from that. But, like, God's essence —" → chapter "He is existence. God's essence —"; only "We'll get into this later" was disclosed. Also "it does so a little bit higher" → "and that's a participation a little bit higher" (rephrase, undisclosed). Plus an imprecise row description: the second questioner turn was rendered declarative ("You might think objects don't."), not as a rhetorical question as the row claims.
- **L-6 — ch6:35 stale flag pointer.** `[attribution questioned; see chapter note]` survives while Owner edit 2026-09-16 (§9 item 3) deleted the chapter note itself. The flag now points at nothing in the chapter; the attribution info lives only in the provenance sidecar §5. Provenance §11 deliberately retained the flag text — the pointer should be reworded (e.g., "see provenance note") or the flag dropped.
- **L-7 — hedge loss in supplement smoothing (ch3, blanket-disclosed).** "that is sort of an extension" → "that is an extension" (T5-S6); "just, you know," → "just" (T5-S1/S5); sentence-initial "So" dropped (T5-S1/S3/S6); "And so it kind of captures, like," dropped (T4-6). Voice profile §9.4 says keep hedges; these are minor and meaning-preserving but unlogged individually.
- **L-8 — T4-1 micro-edit undisclosed.** Come-Holy-Spirit epigraph comma relocation ("…and living, always conscious" → "…, and living always conscious"); provenance discloses only the added "Amen."
- **L-9 — ch1:83 T1-J creates a near-duplicate within one paragraph.** "the descent of Christ into the depths of human misery" (pre-existing) and mine's "he goes down into the depths of all human misery" (T1-J) both appear; faithful to the prescribed insertion point but copy-editor redundant.
- **L-10 — trivial undisclosed micro-edits (meaning-preserving, no action):** ch5:79 "In the same way, mystical knowledge works in that way" → "Mystical knowledge works in this way"; ch6:17 "It is now meant" → "it is meant"; ch6:31 "there's a fruitfulness that a third person comes forth — that helps us" → "…in which a third person comes forth — this helps us"; ch6:23/27 "those that" → "those who".

## 4. Attribution fidelity — results (all PASS)

| Check | Result |
|---|---|
| O'Connor 1959 letter (SRC-064) | Not printed anywhere; no misattribution possible. Non-use disclosure gap = M-2 |
| Marshall-not-Chesterton (ch3, SRC-065) | PASS — "the young man who rings the bell at the brothel is unconsciously looking for God" word-exact vs SRC-065; attributed Bruce Marshall; Chesterton 0× in ch3/ch4 |
| Newman paraphrase (ch4, SRC-066) | PASS — unquoted, "St. John Henry Newman says…", consistent with the Fifth-Station meditation text |
| West hedge (ch5, SRC-067) | PASS — "Christopher West says he once heard it said" (West's own book hedge, per SRC-067); no coinage asserted; West not quoted |
| Dante Longfellow (ch5, SRC-070) | PASS — T6-S10 printed unquoted as speaker's own variant ("…and the moon"); Longfellow wording absent; provenance note accurate |
| Athanasius / CCC ¶460 (ch6, SRC-071) | PASS — "For the Son of God became man so that we might become God" word-exact vs CCC ¶460; attributed St. Athanasius, not Irenaeus; garbled heard name ("Saint Inaus") not printed; maxim inside the outsider's-objection voice |

**No misattribution, no unmarked paraphrase-as-quote, no invented quotation found in any in-scope chapter.**

## 5. Flags preserved (check 4) — none disappeared

- ch1: `[possibly: both]`, `[possibly: these]` + 6× `[quotation wording unverified]` — all present. Owner-removed flags (Thérèse, descent, He, pagan) removed per documented owner edits.
- ch3: 4× `[unclear]` (T4-8, T3-14, T4-10, T4-13) + 4× `[possibly]` (rules, no one, love, **only**-new) — all present.
- ch4: `[possibly: third]` present.
- ch5: `[possibly: brand name — verify audio]` (new, T5-S8 Liquid Death) + 2× `[quotation wording unverified]` (1 new, T5-S11 1 Jn 3:2; 1 pre-existing) — all present.
- ch6: `[possibly: Michael]`, `[possibly: confession]`, `[possibly: mercy]`, `[unclear]` (all new from mine) + `[quotation wording unverified]` (Ignatius) + `[attribution questioned; see chapter note]` — all present (stale pointer = L-6).
- Epilogue: 3× `[possibly]` (`at last`, `mere`, `of`) + `[quotation wording unverified]` (SRC-045) — all present.

## 6. Marker hygiene (check 6)

`python3 scripts/09_validate_repository.py` → **exit 0, Gate G5 passes.** No `[VERIFY]`/`[TODO]` anywhere in `chapters/` (the only `[VERIFY]` occurrences in the repo are 2 in `research/voice_profile.md`). Chapter marker counts match provenance expectations exactly (see §5). New `[unclear]`/`[possibly]` additions from mines are listed in §5 and are acceptable per gate policy.

## 7. Duplicates (check 5) — all PASS

- Moon: epilogue has only the E01 Elizabeth/parallax telling; ch5 has only the T6-S10 *formula* (no story); ch3 zero moon content; no C02/E01 variant merged.
- "Everyone is potentially someone to love": printed once (ch4 via T3-2); T4-12 wording absent from ch3.
- Fivefold litany: C04 text unchanged; T5-S15 adds source attribution only.
- Shamrock/sign-of-cross: ch1 supplements use C01-only material; no C05 "hug" variant imported.
- Sun-and-stars formulas: "that love that made the sun and the stars" (ch6) and "the love that moves the sun and the stars and the moon" (ch5) kept distinct; non-merge recorded.
- No supplement re-introduced excised ch1 material (tent-peg etymology, monotheistic-religion passage, Moriah/Carmel, night-prayer parking).

## 8. Smoothing safety (check 3) — no meaning changes found

All logged smoothing entries in all six chapters verified against current text (ch1: 20/20; ch3: 19/19; ch4: 24/24; ch5: 4/4 + 15 supplement micro-edits; ch6: 22/22; epilogue: 39/39). No content silently deleted beyond disclosed excisions; no invented theology; no jargon added (perichoresis/consubstantial: 0 occurrences). Findings limited to *undisclosed* micro-edits (L-1, L-5, L-7, L-8, L-10) and one disclosed-but-imprecise description (ch5 T5-S8 row). No `[INCOHERENT — author review]` markers anywhere (consistent with provenance claims of NONE).

Drafts vs `chapters/reviewed/` copies: **byte-identical for all six in-scope chapters.**

---

## 9. Blocks rebuild (HIGH only)

1. **H-1** — `research/source_ledger.csv` missing rows for SRC-064…SRC-071 (five provenance files cite them; four feed printed prose with named attributions). Add the 8 rows (or record the gap in `research/unresolved.md`) before the next manuscript assemble.

All other findings are MEDIUM/LOW disclosure-hygiene items; they do not block rebuild but should be folded into the provenance sidecars at the next pass.
