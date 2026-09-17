# Owner-Edit Proofread & Consistency Review — Chapters 1–4

**Date:** 2026-09-17 · **Scope:** `chapters/drafts/01…04` (+ sidecars), `manuscript/Mystery_of_the_Trinity.md` (assembly), `research/voice_profile.md`, RSV-2CE worksheet, unresolved.md, clean transcripts.
**Method:** full paragraph-by-paragraph read of all four chapters; diff of the owner's uncommitted hand-edits (`git diff`) to separate owner-authored text from pipeline text; mechanical greps (misspellings, double spaces, repeated words, contractions, dashes, heading case, pronoun case); cross-check of every scripture reference and attribution against the verified set (worksheet / SRC excerpts / transcripts).
**Marking:** each finding tagged **[owner]** (owner's hand-edit, incl. wording preserved verbatim from the owner's docx per provenance) or **[pipeline]** (pre-existing text, often with a tracking note in the sidecars).
**Severity legend:** 🔴 blocking · 🟠 high · 🟡 medium · 🟢 low. No blocking (logic) defects found — this is prose/formatting.

---

## TYPO

- 🟡 **ch1 §Another Icon of the Trinity, l.19 — [owner]** `Saying that it is written seperates the icon from every other kind of art.` → "separates". The ch1 provenance notes the owner's spelling was "preserved verbatim" — confirm it is a typo, not intentional. Fix: `separates`.
- 🟡 **ch1 §Another Icon of the Trinity, l.21 — [owner]** `Andrei Rublev wrote this icon of  the Trinity, included on the cover of this book.` → double space in "of  the". Fix: `icon of the Trinity`.
- 🟡 **ch4 opening prayer, l.11 — [owner]** `for Thou art wisdom itself, the the food of angels,` → repeated word "the the". (Provenance: carried verbatim from the owner's docx.) Fix: `the food of angels`.
- 🟡 **ch4 opening prayer, l.11 — [owner]** `By this mirrored light I know Thou are the highest good,` → "are" should be "art" (the prayer is in archaic second person; elsewhere "Thou art"). Fix: `Thou art the highest good`.
- 🟡 **ch4 opening prayer, l.9 — [owner]** `what greater gift could Thou givest me then Thy very Self?` → "then" should be "than". Fix: `than Thy very Self`.
- 🟡 **ch4 opening prayer, l.5 — [owner]** `And truly hast the Holy Spirit, who procedeth from Thee, Father and Son,` → "procedeth" should be "proceedeth". Fix: `proceedeth`.
- 🟢 **ch4 opening prayer, l.9 — [owner, suspected]** `Thou art a fire that burns eternally yet never consumed,` → likely a dropped verb: "yet is never consumed" / "yet never consuming". Verify against the translation used; recommend `yet is never consumed`.
- 🟢 **ch4 opening prayer, l.9 — [owner]** `a fire who taketh away all cold heartedness` → one word in standard renderings: "coldheartedness" (or "cold-heartedness"). Fix: `coldheartedness`.

## FORMAT

- 🟠 **manuscript/Mystery_of_the_Trinity.md, ll.378–390 — [owner-induced]** The six paragraphs of the Catherine of Siena prayer **and its attribution line** are rendered as `## ` headings (`## O Eternal God! O Eternal Trinity! …`, `## —St. Catherine of Siena (1347-1380), Doctor of the Church`) instead of an italic blockquote. The owner's docx carried the prayer as Section-styled paragraphs, and the docx→md assembly mapped them to Heading 2. Every other chapter prayer in the manuscript is a proper `> *…*` blockquote. As-is this typesets as six giant headings and breaks the standing prayer policy (italic, no subheadings). Fix: re-style the prayer in the docx to the book's prayer paragraph style and regenerate the manuscript assembly (draft/reviewed files are already correct blockquotes).
- 🟡 **ch1 opening (ll.1–5) — [pipeline]** The Breastplate prayer (`> *I bind unto myself the name, the strong name of the Trinity…*`) has **no attribution line** after the blockquote; the section heading follows immediately. Ch2 (`— Prayer of St. Elizabeth of the Trinity`), ch3 (`— Psalm 42:1–7`), and ch4 all have one. Fix: add e.g. `— St. Patrick's Breastplate` after the prayer.
- 🟢 **ch4 l.15 — [owner]** `—St. Catherine of Siena (1347-1380), Doctor of the Church` — three deviations from ch2/ch3 attribution style: (a) no space after the em dash (ch2/ch3 use `— Prayer of…` / `— Psalm 42:1–7`); (b) hyphenated date range `1347-1380` where ch3 uses an en dash (`42:1–7`); (c) no `Prayer of` prefix that ch2 uses. Fix for uniformity: `— Prayer of St. Catherine of Siena (1347–1380), Doctor of the Church`.
- 🟢 **ch1 l.61 — [owner]** `I recommend taking this to the chapel – or your own inner room in your own time of silent recollection – to pray with this icon.` — uses **en dashes** `–`; the book's convention is spaced em dashes `—`. Fix: em dashes.
- 🟢 **ch4 ll.3 vs 5/7/9/11/13 — [owner]** Within the prayer: `O Eternal God! O Eternal Trinity!` (l.3) but `O eternal Trinity` (l.5, l.7…) — capital "Eternal" inconsistent inside one prayer. Fix: pick one (follow the source translation).
- 🟢 **ch2 l.79 — [pipeline]** `And why do you not drive in separate directions, and both of you observe the moon.` — interrogative ends with a period. Fix: `…observe the moon?`

## CONSISTENCY

- 🟡 **ch1 l.29 — [owner]** Contraction policy: `What I'm giving you is the reading I find most illuminating…` — `I'm` is the **only** contraction in ch1–4 (mechanically verified: zero others). Policy is "sparse"; flagged as owner-authored, listed, no prescription.
- 🟡 **ch3 l.89 vs l.81 — [owner] vs [pipeline]** `There is something that St. John Paul II understood` (owner added "St.") vs `Recall John Paul II's Theology of the Body.` — same person, same chapter, two honorifics. Fix: harmonize (`St. John Paul II` both places, or drop both "St.").
- 🟡 **book-wide heading case — [pipeline]** Title Case: ch1, ch2, ch4, epilogue (`## Two Kinds of Knowledge`); sentence case: ch3, ch5, ch6 (`## Two kinds of feedback`). Pick one convention book-wide; ch4 vs ch3 differ inside this review's scope.
- 🟡 **divine-pronoun capitalization — [pipeline]** Mixed: `He encompasses us in His infinite embrace` (ch2 l.137), `He comes to save us. He comes to save you` (ch2 l.105), `He was infinitely perfect` (ch3 l.13), `He who is between the Father and the Son` (ch4 l.57) — vs lowercase `he is within` (ch2 l.133), `his love… from him` (ch2 l.129), `he created male and female` (ch3 l.25), `he says… he creates` (ch3 l.37). Fix: one convention for God's pronouns in author prose.
- 🟢 **ch3 l.17 — [owner]** `When I was in college, I remember how Fr. Michael explained the Trinity` — "Fr. Michael" now matches ch6 l.91 (`As Fr. Michael often says…`) ✓. But every audio source says "**Father Mike**"; the formalization Mike→Michael is unverified. Confirm the priest's name with the owner before print.
- 🟡 **ch4 opening prayer — [owner decision, flag]** The owner replaced the ch4 opening prayer (previously the C02 Elizabeth prayer, duplicated) with Catherine of Siena's "O Eternal God! O Eternal Trinity!". voice_profile.md §6 documents C04's actual opening as Elizabeth of the Trinity's "**O eternal Word, Word of my God… O my three, my all, my beatitude…**". The substitution is recorded as deliberate in the provenance, but it no longer matches the talk the chapter is built from — confirm the swap is intended for print.
- 🟢 **clean checks — [pass]** "Fr. Peter" / "Fr. Gruber": absent from ch1–4 prose (no issue). its/it's: clean. Elisabeth (niece, ch2 ll.73–121) vs Elizabeth (saint, ch2 l.5/19, ch3 l.69): correct everywhere ✓.

## CONSTRUCTION

- 🟢 **ch2 l.111 — [owner]** `This lamp here even is a mystery.` — awkward word order ("here even is"). Suggest: `Even this lamp here is a mystery.`
- 🟢 **ch1 l.61 — [owner]** `With our own prayer, I recommend taking this to the chapel…` — the owner deleted the lead-in ("There are probably other parts of this image, and there could be fruit drawn from it. And with our own prayer…"), so the paragraph now opens on a dangling "With our own prayer". Also "your own … your own" repeats. Suggest restoring a short lead-in.
- 🟢 **ch1 §Another Icon of the Trinity (l.17–21) — [owner]** The deleted intro ("I want to turn to another icon of the Trinity… a Russian icon from Andrei Rublev…") means **Andrei Rublev is never identified** — no nationality, no century. The section starts cold ("It is not usual to depict the Trinity") and "Andrei Rublev wrote this icon of  the Trinity" hangs without context for a reader who doesn't know him. Section still reads grammatically, but consider a one-line identification.
- 🟢 **ch4 l.53 — [pipeline]** `…to stress not just reverence towards the other — we are really talking about a singular person.` — "not just…" without a "but also" leaves the contrast unbalanced (provenance l.183 discloses the smoothing of "but we're really talking about"). Consider `not just reverence towards the other — we are really talking about a singular person` → add "but also the singularity:".
- 🟢 **ch4 l.23 — [pipeline]** `Carpet is not the best example, where I become like the thing.` — the "where" clause has no clear referent. Suggest: `Carpet is not the best example of becoming like the thing you know.`
- 🟢 **ch3 l.91 — [pipeline]** `If you start going faster than your speed, the car will slow down.` — "than your speed" reads oddly. Suggest: `faster than the set speed`.

## FACTUAL

- 🟡 **ch3 opening Psalm block (l.3) — [pipeline, tracked-open]** Ps 42:5 prints `Hope in God; for I shall again praise him, my savior and my God.` — the RSV-2CE worksheet row 11 records the 2CE reading as "**my help** and my God" and marks the row ⚠SUSPECT (its own line-68 summary contradicts the row). Owner decision outstanding. The spoken/LOTH text says "savior"; if RSV-2CE alignment is the rule, this needs the owner's call.
- 🟢 **ch3 opening Psalm block (l.3) — [pipeline, tracked-open]** Ps 42:3 prints `"Where is your God."` (period) — worksheet flags v3 punctuation ("?" vs ".") as an outstanding owner decision, with conflicting entries between row 11 and line 68. Resolve against the 2CE text before print.
- 🟢 **ch1 l.49 — [pipeline]** Luke 2:49 quote drops the closing question mark: `"Did you not know that I must be in my Father's house", that is, the temple.` — RSV-2CE: `"Did you not know that I must be in my Father's house?"`. Fix: add `?` inside the quote.
- 🟢 **ch3 l.17 — [owner]** `When I was in college, I remember how Fr. Michael explained the Trinity` — the college setting appears in **no source** for the buckets anecdote (clean transcript + first-retreat supplement both read simply "I remember how Father Mike explained the Trinity"). Owner-added detail; verify or drop.
- 🟢 **ch3 l.43 — [pipeline, tracked-open]** `As one author, Aidan Kavanagh, said: "The liturgy is doing the world the way the world was meant to be done."` — unresolved.md item 2 is still open: credit as Kavanagh-via-Fagerberg or Fagerberg is pending the citation reviewer's decision (the talk credited Fagerberg).
- 🟢 **ch2 l.51 — [pipeline]** `(The Philosophy of Existence, Harari, Harvill 1948)` — "Harari" is the translator (Manya Harari), not an author; without "trans." the parenthetical reads like an author name. Suggest: `(The Philosophy of Existence, trans. Harari, Harvill Press, 1948)`. (Verified form per SRC-072.)
- 🟢 **ch1 ll.19/21/47 — [pass]** "icons are not painted but written" claim is internally consistent with the rest of the chapter ("wrote this icon", "when it was originally written") ✓ — no conflict introduced by the new paragraph.
- 🟢 **verified-set pass — [pass]** Rom 12:2 "this world" intact (ch3 l.9, ch4 l.41) ✓; Mt 28 baptismal form ✓; Gen 1:26 "Let us make man in our image, after our likeness" ✓; Jn 12:24 ✓; Jn 14:2 "many rooms" ✓ (worksheet row 19 MATCH); Mt 18:20 ✓; 2 Cor 12:2 "third heaven" ✓; Benedict XVI 2005 homily quotation ✓ (SRC-004); "graveyard of heresies" ✓ (SRC-002); Catherine of Siena dates 1347–1380 ✓; Maritain "(A Preface to Metaphysics, 1948)" matches the verified 1948 printing (SRC-073) ✓; uncle Mark's litany attribution is owner-sanctioned and resolved (ch4 provenance l.163, l.228) — not a finding.

---

## Notes on method / non-findings
- The `chapters/reviewed/` copies are byte-identical to the drafts per the provenance (`cmp`-verified) — all findings apply to both.
- The manuscript TOC lists chapters only, so the deleted "The Hospitality of Abraham" subheading leaves no stale TOC entry ✓.
- No stray markdown (`**`, backticks) in ch1–4 prose; no space-before-comma/period; only one double space (ch1 l.21); "that that" at ch1 l.57 is legitimate ("I read that that rectangle…").
