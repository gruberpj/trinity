# Owner Hand-Edit Proof — Chapters 5–6 + Epilogue (2026-09-17)

Scope: owner's manual docx edits reverse-integrated into `chapters/drafts/05_intimacy.md`, `06_evangelization.md`, `epilogue_engineering_mystery.md` (working-tree diff vs HEAD), plus consistency checks against ch2–ch4, the compiled manuscript, sidecars, and voice profile. Each finding is tagged **owner-authored** (owner's hand-edit/dictation) or **pipeline** (pre-existing text the owner did not touch). READ-ONLY review; no source files modified.

---

## 🔴 Blocking

### 1. Broken sentence in the condensed burning-bush passage — TYPO/CONSTRUCTION (owner-authored)
- **ch5 §Being itself** (line 21): "Moses, wandering in the desert and tending the flock of his father-in-law Jethro, sees on Mount Sinai is this bush burning but not being consumed."
- The condensation dropped the clause connector: "sees on Mount Sinai is this bush" is ungrammatical.
- **Fix:** "…sees on Mount Sinai that there is this bush burning but not being consumed" (or "…sees this bush burning on Mount Sinai, not being consumed"). Must be fixed before print — it appears identically in the drafts, reviewed copies, and compiled manuscript (manuscript line 473).

---

## 🟠 High

### 2. Approved X.41.66 endnote never carried into the Notes section — FACTUAL (owner-approved, unapplied)
- **Epilogue §Intimacy — The Most In** (line 99): the hedge is present and correct — "this one thing that St. Augustine apparently said: 'I looked into my deepest wound, and there I saw your glory, and it dazzled me'" — but owner batch-4 (2026-09-17) resolved that the Notes section should carry an endnote citing *Confessions* X.41.66 (SRC-045 → PARAPHRASE_CONFIRMED). The compiled manuscript's Notes still print endnote 35 as: "**St. Augustine (attribution doubtful — speaker hedges)**, *(no source located)*, —, —, —, —." and the wound-quote paragraph carries no endnote marker.
- **Fix:** update endnote 35 with the X.41.66 citation (see `research/verified_excerpts/SRC-045-verify.md` option 2) and add the note marker to the quote. This is the exact item the task flagged — hedge ✓ present, endnote ✗ absent.

### 3. Great Commission printed as a quotation with a missing verse clause — FACTUAL (pipeline, owner-decision pending)
- **ch6 §Back to St. Patrick** (line 13): "All authority in heaven and on earth has been given to me. Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit. Behold, I am with you always, to the close of the age."
- Mt 28:19b–20 is quoted in quotation marks but omits "teaching them to observe all that I have commanded you" (the RSV-2CE alignment pass applied replace-only and did not insert the unspoken clause; disclosed in the 06 sidecar §5 and RSV-2CE worksheet).
- **Fix:** insert the missing clause (2CE wording) or recast as a paraphrase — owner decision, but a quoted "Great Commission" must not silently drop v.20a.

### 4. Prayer attribution hedge lost in the ch6 opening — FACTUAL (owner-authored, deliberate but risky)
- **ch6 opening** (line 5): "— St. John Henry Newman" replaces "This prayer is traditionally attributed to St. John Henry Newman."
- The Radiating Christ prayer's authorship is ATTRIBUTION_UNCONFIRMED in the ledger (questioned by scholars; see 06 sidecar §5 row 1). The name-only attribution line now asserts authorship where the book's own pipeline treated it as traditional-only.
- **Fix:** restore the hedge (e.g., "— St. John Henry Newman (attributed)") or confirm authorship with the owner before print.

---

## 🟡 Medium

### 5. Attribution-line formatting is inconsistent across chapters (and md↔docx) — CONSISTENCY/FORMAT (owner-authored)
- ch5 line 5: `*— St. Augustine, Confessions, X.27 (trans. E. B. Pusey)*` — **whole line italic**, book title un-marked.
- ch2: "— Prayer of St. Elizabeth of the Trinity" (roman) · ch3: "— Psalm 42:1–7" (roman) · ch6 md: "— St. John Henry Newman" (roman).
- The owner's docx has ch5 and ch6 attribution lines *italic*, ch2/3/4 roman; the drafts md mirrors the italic only for ch5 (ch6 md drops it) — so the md and docx now disagree for ch6, and the docx itself is mixed. (ch4's "—St. Catherine of Siena…" also uses a different paragraph style and no space after the dash — pre-existing.)
- **Fix:** pick one convention (all roman with `*Confessions*` marked, or all italic) and apply it to all five attribution lines in both md and docx.

### 6. Missal dismissal misquoted — FACTUAL (pipeline, sidecar Q13 open)
- **ch6 §Missa est** (line 69): "Go and announce the gospel of the world" — the Missal dismissal is "Go and announce the Gospel of the Lord" (*Ite ad Evangelium Domini annuntiandum*). Printed inside quotation marks as one of the dismissal variants; the sidecar kept the heard form (p=1.00) with Q13 open for human listen.
- **Fix:** correct to "Gospel of the Lord" or drop the quotation marks (owner's call; sidecar discloses).

### 7. Epilogue Augustine quote silently deviates from the cited translation — FACTUAL (owner-authored, disclosed in sidecar)
- **Epilogue §Intimacy — The Most In** (line 97): "Too late loved I Thee, O Thou Beauty of ancient days, yet ever new! too late I loved Thee! … Thou hast made us for Thyself, and our heart is restless, until it repose in Thee."
- Genuine Pusey (Gutenberg #3296) reads "Thou **madest** us for Thyself". The sidecar records the "hast made" form as owner preference — a silent modernization inside an otherwise archaic Pusey rendering (mixed register: "Thou hast made" beside "until it repose").
- **Fix:** restore "madest" for quotation fidelity, or add an endnote disclosing the modernization.

### 8. Comma splice in the owner-dictated veils paragraph — CONSTRUCTION (owner-authored, dictated verbatim)
- **Epilogue §The Feed and the Feasts** (line 145): "Unlike screens, veils clothe mystery, they accentuate it; they show what is behind the veil."
- Two independent clauses joined by a comma; also "We do not look at the veils, we look beyond them" in the same dictated paragraph is a second comma splice.
- **Fix:** semicolon or em-dash after "mystery" (and after "veils").

---

## 🟢 Low

### 9. Period outside closing quote in the Augustine wound quote — FORMAT (pipeline)
- **Epilogue** (line 99): `"I looked into my deepest wound, and there I saw your glory, and it dazzled me".` — the book elsewhere places terminal periods inside quotes ("I AM WHO I AM.", Mt 11:28 close). **Fix:** `…it dazzled me."`

### 10. Dangling demonstrative at the trimmed Moon section — CONSTRUCTION (owner-caused)
- **Epilogue §The Moon and the Child** (line 53): "You look up in the sky — those things do not matter to you." The section now opens with "those things" referring to celestial bodies that are no longer introduced (the deleted story's setup line "I will talk about another celestial body: the moon." went with the cut). The recall itself is sound: "Recall the story of Elisabeth and the moon" resolves to ch2's §"Elisabeth and the Moon" (same spelling, story intact). **Fix:** name the referent, e.g., "the moon, the stars — those things do not matter to you."

### 11. Mixed participle in the owner's solar-flare dictation — CONSTRUCTION (owner-authored)
- **Epilogue §A Solar Flare of Love** (line 71): "the excess, the abundance of God's love spilled out and strewn across the sky" — **Fix:** "spilled out and was strewn across the sky."

### 12. Feedback-loop definition stated twice in the recast paragraph — CONSTRUCTION (owner-authored)
- **Epilogue §The Enchanted World** (line 117): "In systems engineering, a feedback loop is where an output is fed into its own input." … two sentences later: "We want the output to be fed back into the input and to increase things exponentially." The recast adds a definition that the retained sentence already supplies. **Fix:** cut the duplicated definitional clause in the second sentence.

### 13. Mt 6:6 paraphrase says "hears" for "sees" — FACTUAL (pipeline, unquoted paraphrase kept as heard)
- **Epilogue §Intimacy — The Most In** (line 91): "your Father who hears in secret will reward you" — Mt 6:6 (RSV) reads "your Father who **sees** in secret will reward you"; "street corners and marketplaces" likewise deviates from "synagogues and street corners" (Mt 6:5). It is an unquoted paraphrase, so no alignment was mandated, but worth owner review.
- **Fix:** "sees in secret" if the paraphrase is to track Scripture.

### 14. "most interior to ourselves" — CONSTRUCTION (pipeline)
- **Epilogue §Intimacy — The Most In** (line 95): "he is most interior to ourselves" — reflexive doesn't agree with the subject "he". **Fix:** "he is most interior to us."

### 15. Missing possessive in "respond to him in redeeming us" — CONSTRUCTION (pipeline)
- **Epilogue §The Enchanted World** (line 115): "We are meant to respond to him in redeeming us." — **Fix:** "in his redeeming us" or "to his redemption of us."

### 16. Circular 1 Jn 3:2 paraphrase — CONSTRUCTION (owner-approved, disclosed in sidecar)
- **ch5 §Intimus: the most in** (line 75): "Contemplate him in the holy Eucharist, and we become like him — for we shall see him as he really is, for we will be like him." — "we become like him … for we will be like him" is circular. Owner batch-4 chose this unattributed paraphrase (sidecar discloses the RSVCE mismatch). **Fix (optional):** "…we become like him — for we shall see him as he really is."

### 17. Incomplete question in the storm passage — CONSTRUCTION (pipeline)
- **ch5 §Christ resting in the storm** (line 105): "How is it that when the boat is being rocked about, water is entering in, there is danger of being capsized, or the ship breaking under the waves? But Christ is there, sleeping." — the "when…" clause never resolves into a question. **Fix:** merge: "…or the ship breaking under the waves, Christ is there, sleeping?" (spoken style; smoothing-4 repair disclosed in the sidecar).

### 18. "the one time that the apostles were all together on the boat" — FACTUAL (pipeline, weak)
- **ch5 §Christ resting in the storm** (line 105): the apostles are together on boats in several gospel episodes (Mt 14:22ff, Jn 6, Jn 21); the intended sense is "the one time he slept through the storm." **Fix (optional):** "the time that…" if uniqueness isn't meant.

### 19. Dangling-participle fragment — CONSTRUCTION (pipeline)
- **ch6 §The Easter flame** (line 65): "Lifting it up and saying, 'Lumen Christi' — the light of Christ." — no subject/main verb. **Fix:** "…the priest blesses the fire, the sacred fire, lifting it up and saying, 'Lumen Christi' — the light of Christ."

### 20. Subject–verb agreement in the doxology — CONSTRUCTION (pipeline)
- **ch6 §Missa est** (line 83): "to whom all praise and glory belongs forever and ever" — **Fix:** "belong" (Missal: "is yours").

### 21. ch6 heading: straight quotes; sidecar claims a curly normalization that never happened — FORMAT (pipeline/process)
- **ch6** (line 67): `## Missa est: "it has been sent"` — straight ASCII quotes in both the md and the docx; the 06 sidecar's reverse-integration note says the "heading's quotes normalized to curly quotes per the docx," which is false. Also "Missa est" is italicized in the body (*Missa est*) but not in the heading. **Fix:** correct the sidecar claim; optionally unify heading styling.

### 22. Epilogue sidecar reverse-integration list incomplete — PROCESS
- **epilogue provenance, final section** (line 293–299): reports "7 paragraphs deleted, 7 replaced" but itemizes only five bullets and omits the deletion of "Recall the moon that followed Elizabeth: it truly follows her." from §The Enchanted World; the section ends abruptly mid-list. **Fix:** complete the change ledger.

### 23. Heading capitalization after colon — FORMAT (pipeline)
- **ch5**: "## Intimus: the most in" (lowercase) vs "## The cross: the Trinity's embrace" (uppercase). **Fix:** pick one convention.

### 24. "That is not liturgy as rubrics." — CONSTRUCTION (pipeline)
- **Epilogue §The Enchanted World** (line 113): compressed and ambiguous between "that is not liturgy — that is rubrics" and "that is not liturgy reduced to rubrics." **Fix (optional):** "That is not liturgy — that is rubrics."

---

## Verified clean (no action)

- **Pusey X.27 prayer (ch5)**: fetched Gutenberg #3296 and compared word-for-word — "Too late loved I Thee…" through "…I burned for Thy peace" matches Pusey exactly, including "deformed I, plunging amid those fair forms" and "which, unless they were in Thee, were not at all." Attribution "St. Augustine, Confessions, X.27 (trans. E. B. Pusey)" is accurate.
- **RSV-2CE intact**: Mt 11:28 "all who labor and are heavy laden" (epilogue line 161) ✓; Rom 12:2 indirect "this age" kept per owner (epilogue line 105) ✓; Mt 5:11 form (ch6 line 93) ✓.
- **Contractions policy**: every contraction in the three files sits inside quotation marks (dialogue/dramatized speech) — none owner-reintroduced outside quotes. ✓
- **"Ite, missa est" italics** present (ch6 lines 71, 75, 77) ✓; ***poorly*** italic in the Chesterton correction (epilogue line 127) ✓; **"doom scroll"** two-word form (epilogue line 139) ✓.
- **Elisabeth spelling**: the epilogue recall "the story of Elisabeth and the moon" now matches ch2's "Elisabeth and the Moon" section and its "Elisabeth"/"niece Elisabeth" spellings — the owner's change removes a latent Elizabeth/Elisabeth split. ✓
- **Fr. Michael**: ch6's "As Fr. Michael often says" matches ch3's established "Fr. Michael". ✓ (notes.md item 49 still says "Father Michael" — stale queue note, harmless.)
- **Benedict paraphrase**: "As Pope Benedict has said, you are not made for comfort — you are made for greatness." — paraphrase, no quotation marks, per owner direction. ✓
- **Eclipse date**: "the eclipse of April 2024" ✓; new closing "The engineering worldview is not sufficient in itself." reads coherently with the welding-lens joke. ✓
- **"bought my first brown scapular and was invested"**: "invested" is the correct investiture term. ✓
- **ch5 ending**: after deleting the final "God rests in us. He is intimate with us.…" paragraph, the chapter closes cleanly on the sign-of-the-cross hug paragraph; no dangling references (the epilogue's "friend already home" and "Christ sleeps in the boat" callbacks still resolve to retained ch5 sections). ✓
- **Moon-and-the-Child trim**: no dangling references to deleted details anywhere in the book ("man in the moon", "parallax", "Uncle PJ", "Mary Margaret" survive only inside ch2's intact telling). ✓
- **No double spaces, no trailing whitespace, no repeated-word errors** in any of the three files. ✓
