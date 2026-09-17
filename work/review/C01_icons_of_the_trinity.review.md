# C01 "Icons of the Trinity" — Transcript Review Log

- **Recording:** C01_icons_of_the_trinity
- **Source SHA-256:** `7d1716be0645fd0176ce17117db837f3e60fd94e78975d3fb3dd35d538e7dfb2`
- **ASR run:** `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, int8, beam 1, temp 0, VAD, word timestamps)
- **Raw transcript:** `transcripts/raw/C01_icons_of_the_trinity.raw.20260916_fasterwhisper_largev3_nocond.md` (348 segments, 00:00:01–00:24:46)
- **Clean output:** `transcripts/clean/C01_icons_of_the_trinity.clean.md`
- **Editorial output:** `transcripts/editorial/C01_icons_of_the_trinity.editorial.md`
- **Reviewer:** pipeline-review · **Reviewed:** 2026-09-16
- **Method note:** No audio listening available to the machine reviewer. Corrections rest on (a) verified source texts (ledger/excerpts/DOCX) and (b) per-word ASR probabilities (words < 0.3 suspect, < 0.15 likely wrong). **Human audio spot-listening is required** for the open questions in §5 before sign-off.

## 1. Change summary (counts by category)

| Category | Count |
|---|---|
| Paragraphs in clean transcript (timestamp blocks) | 26 |
| [unclear HH:MM:SS] flags | 0 |
| [possibly: term] flags | 6 |
| Filler words deleted ("um"/"uh") | 3 |
| Duplicated words / ASR segment-boundary echoes deleted | 14 |
| Abandoned false starts removed (including 1 garbled clause) | 4 |
| Capitalization fixed (sentence starts, I, God, Father/Son/Holy Spirit, Trinity, proper nouns, book names) | ~140 |
| Punctuation added/adjusted (sentence ends, commas, em-dashes, quotes) | ~150 |
| ASR errors corrected against verified source text | 1 (Breastplate duplicated "word.") |
| Proper nouns corrected with probability + obvious form (rule b) | 1 ("J.L." → "Jael") |
| Minor grammar fixes (word-order swap, preposition, 's added) | 4 |
| Quotations / citations detected (see §3) | 16 |

Deletion/edit detail (raw → clean), all at segment boundaries unless noted:

1. `Word. word.` → `Word.` (00:00:25, "word." p=0.009; duplicate of Breastplate line confirmed by SRC-012/DOCX)
2. `in at least in our country` → `at least in our country` (00:00:52, false start "in" p=0.075)
3. `a pagan religion religion of Druidism. Druidism that saw that there was a pagan religion that saw spirits` → `a pagan religion — the religion of Druidism — a pagan religion that saw spirits` (00:01:21, duplicated "religion" p=0.161 + garbled echo; see open question Q2)
4. `convert this this land` → `convert this land` (00:01:48, "this" p=0.472)
5. `religion, which we / We do have` → `religion — which we do have` (00:02:40, boundary duplication)
6. `no affront there. there. But` → `no affront there. But` (00:04:34, "there." p=0.433)
7. `reasons for that. that. But looking` → `reasons for that. But looking` (00:07:19, "that." p=0.013)
8. `and communicated / communicated with God` → `and communicated with God` (00:09:36, second "communicated" p=0.074)
9. `the red of, of um it's kind of` → `the red of — it's kind of` (00:10:57, "um" p=0.092, "of" p=0.145)
10. `poor uh some would say` → `poor. Some would say` (00:11:02, "uh" p=0.442)
11. `and uh that could symbolize` → `and that could symbolize` (00:11:07, "uh" p=0.807)
12. `divinity of Christ. Christ, what we call` → `divinity of Christ — what we call` (00:11:45, "Christ," p=0.088)
13. `symbolized in that. that, the whole image` → `symbolized in that. The whole image` (00:14:07, "that," p=0.090)
14. `through Christ / Christ is through` → `through Christ is through` (00:16:31, second "Christ" p=0.227)
15. `that can, there could be fruit` → `— there could be fruit` (00:16:40, abandoned start "that can")
16. `Spirit. Amen. men. Those words` → `Spirit. Amen. Those words` (00:17:30, "men." p=0.164 = split echo of "Amen")
17. `sloppy Father, Son, Holy Spirit` — kept verbatim (characteristic phrasing)
18. `I am putting / putting this is my stability` → `I am putting — this is my stability` (00:22:11, boundary duplication)
19. `holy spirit / Spirit, we are made` → `Holy Spirit — we are made` (00:23:31, "Spirit," p=0.033)
20. `poured three times water over our heads` → `water poured three times over our heads` (00:17:30, adjacent-word swap, basic grammar fix — human confirm)
21. `it symbolized in the gold stripe` → `it's symbolized in the gold stripe` (00:11:20, "it" p=0.414; 's added — human confirm)
22. `that equal dignity` → `that's equal dignity` (00:14:35, "that" p=0.403; 's added — human confirm)
23. `grip onto on their minds` → `grip onto in their minds` (00:03:26, preposition fix)
24. `for which St. Patrick was incredibly successful at` → `at which St. Patrick was incredibly successful` (00:03:36, relative-pronoun fix)
25. `It says, let us create man` → `when God says, "Let us create man` (00:06:22, "It" p=0.186 dropped as false start; "let" p=0.309 — human confirm)

## 2. Uncertainty flags ([possibly])

| # | Timestamp | Raw ASR text | Action | Reason |
|---|---|---|---|---|
| 1 | 00:02:46 | "And if you were Jewish and you believed in many gods" | Kept "Jewish", flagged `[possibly: pagan]` | "Jewish" p=0.492; context ("believed in many gods") fits a pagan/polytheist, not a Jew; possible speaker slip or loose syntax. Human listen required. |
| 2 | 00:17:21 | "beginning prayer and ending prayer, bulk ending it with the sign of the cross" | Kept "bulk", flagged `[possibly: both]` | "bulk" p=0.899 but semantically incoherent; likely "both" (both beginning and ending with the sign of the cross). Human listen required. **RESOLVED (owner, batch 3, 2026-09-16): owner dictated replacement wording — "As Catholics, we are very used to beginning and ending prayer with the sign of the cross." Applied to the clean transcript and both chapter copies; flag removed.** |
| 3 | 00:18:31 | "Every word matters. even the and of thus." | Kept "thus", flagged `[possibly: these]`; rendered as "even the 'and' of thus [possibly: these]" | "thus" p=0.888 but "the 'and' of thus" is meaningless; context ("every word matters", the words just quoted) suggests "of these [words]". Human listen required. **RESOLVED (owner, batch 3, 2026-09-16): rendered with the owner's phrase — "Every word matters — even the 'and of the's." Applied to the clean transcript and both chapter copies; flag removed.** |
| 4 | 00:19:13 | "that saint teres talks about when she says what is prayer but a simple glance directed towards heaven" | Rendered "St. Teresa", flagged `[possibly: Thérèse]` | "teres" p=0.64; ambiguous between Teresa (of Avila) and Thérèse (of Lisieux). The "simple glance directed towards heaven" is classically St. Thérèse of Lisieux's (Story of a Soul, ch. XI: "a simple look turned toward heaven"). Attribution must be confirmed by the author. |
| 5 | 00:20:41 | "This scent of the Holy Spirit is now with us." | Kept "scent", flagged `[possibly: descent]` | "scent" p=0.355 and contextually wrong; candidates: "descent" (parallels "the descent of Christ" at 00:19:54), "sending" (parallels "has been sent among us" at 00:20:37), or "same". Human listen required. **RESOLVED by owner listening 2026-09-16: the word is "descent"; flag removed from the clean transcript and chapter layers.** |
| 6 | 00:23:47 | "he said, it is good. We looked upon us created in his image and likeness" | Kept "We", flagged `[possibly: He]` | "We" p=0.77 but "We looked upon us" is ungrammatical; the subject is God (parallel with "when God looked… he said" and "He looked at us and said"). Almost certainly "He". Human listen required. |

## 3. Quotations and citations detected

| # | Timestamp | Item heard | Type / attribution | Verification vs ledger | Action in clean |
|---|---|---|---|---|---|
| 1 | 00:00:01, 00:00:33, 00:17:24, 00:18:16, 00:24:27, 00:24:43 | "In the name of the Father, and of the Son, and of the Holy Spirit. Amen." (repeated) | Liturgical formula / Mt 28:19 wording | Matches SRC-019 (RSV "in the name of the Father and of the Son and of the Holy Spirit"). VERIFIED. | Kept as spoken. |
| 2 | 00:00:12–00:00:27 | "I bind unto myself the name, the strong name of the Trinity, by invocation of the same, the three in one, and one in three, of whom all nature hath creation, eternal Father, Spirit, Word. Praise to the Lord of my salvation. Salvation is of Christ the Lord. Amen." | St. Patrick's Breastplate, final stanza (C. F. Alexander tr., 1889) | SRC-012 / DOCX: VERIFIED_MINOR_VARIANT — wording matches Alexander's translation exactly; speaker recites continuously with comma after "same" (print: period) and lowercase "name"/"three". Duplicated ASR "word." (p=0.009) corrected against source. | Corrected to source wording. |
| 3 | 00:03:04 | "All power in heaven and on earth has been given to me." | Matthew 28:18 | SRC-019 (RSV) reads "All **authority** in heaven and on earth has been given to me." Speaker said "power" — paraphrase/variant; NOT forced to match source. | Kept "power" as heard; discrepancy logged here. |
| 4 | 00:05:03–00:05:46 | Retelling of Genesis 18:1-8 (three visitors, Oak of Mamre, hospitality, promise of Isaac) | Scripture paraphrase | SRC-015 (RSV): PARAPHRASE_CONFIRMED — "Oak of Mamre" capitalization follows DOCX; speaker retells, does not quote. | Kept as spoken. |
| 5 | 00:06:22 | "Let us create man in our own image and likeness." | Genesis 1:26 (speaker's paraphrase) | Not in ledger (ledger has Gen 18, not Gen 1:26). RSV: "Let us make man in our image, after our likeness." Speaker's wording differs — flagged as paraphrase from memory; no source match forced. | Kept as spoken. |
| 6 | 00:09:24–00:09:47 | Mount Moriah/Isaac, Mount Sinai/Moses 40 days, Elijah "still small voice" (1 Kings 19:12), Mount Carmel | Scripture allusions | Not individually in ledger; standard biblical references. "still small voice" phrase matches KJV tradition. | Kept as spoken. |
| 7 | 00:10:15–00:10:25 | Mount Tabor, Peter/James/John, cloud, Father's voice | Matthew 17:1-8 allusion | SRC-017 (RSV): speaker paraphrases; no verbatim conflict. | Kept as spoken. |
| 8 | 00:13:17 | "In my Father's house there are many rooms." | John 14:2 | SRC-018 (RSV): "In my Father's house **are** many rooms" — speaker inserts "there"; minor spoken variant. VERIFIED_MINOR_VARIANT. | Kept as heard. |
| 9 | 00:13:24 | "Do you not know I must be about my Father's business and my Father's house" | Luke 2:49 paraphrase | Not in ledger. "About my Father's business" = KJV tradition; speaker merges with "my Father's house". Paraphrase — no source match forced. | Kept as spoken. |
| 10 | 00:16:21 | "Unless a seed fall to the ground and dies, it remains but a seed. But if it dies, it produces much fruit." | John 12:24 paraphrase | Not in ledger. RSV: "unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit." Speaker's wording differs — paraphrase from memory; NOT forced to match. | Kept as heard. |
| 11 | 00:18:16 | "In the name of the Father and of the Son and of the Holy Spirit." | Matthew 28:19 (attributed to Matthew 28 by speaker) | SRC-019: VERIFIED_EXACT wording. | Kept; Matthew 28 attribution correct. |
| 12 | 00:19:20 | "What is prayer but a simple glance directed towards heaven?" | Attributed to "St. Teresa" [possibly: Thérèse] | Not in ledger. Classic Thérèse of Lisieux paraphrase (Story of a Soul XI). Attribution needs author/human confirmation (see flag #4). | Kept with [possibly] flag. |
| 13 | 00:22:18 | "Jael killing Sisera in the tent, using a tent peg" | Judges 4:21 allusion | Not in ledger. Reference correct (Jael kills Sisera with a tent peg, Judges 4:21). ASR "J.L." corrected to "Jael" (J p=0.94, .L. p=0.859 — proper noun, prob > 0.5, obvious form). | Corrected. |
| 14 | 00:23:54–00:24:05 | "It is good" / "You are very good" | Genesis 1:31 allusion | Not in ledger. RSV: "it was very good". Speaker's paraphrase. | Kept as spoken. |
| 15 | 00:24:33 | "Glory be to the Father, and to the Son, and to the Holy Spirit, as it was in the beginning, is now, and ever shall be, world without end. Amen." | Glory Be (liturgical, standard English text) | Not in ledger; standard text — matches the common English rendering. | Kept. |
| 16 | 00:02:00 / 00:22:42 | "the central mystery of our faith" / "the most central mystery of our faith" | Doctrinal echo of CCC ¶234 | SRC-007 (CCC ¶234: "The mystery of the Most Holy Trinity is the central mystery of Christian faith and life"). Speaker alludes, does not quote. PARAPHRASE_CONFIRMED. | Kept as spoken. |

Also noted (not quotation, but a factual claim needing review): **00:21:04** — "Amen … is actually derived from another Hebrew word, aman. Aman means tent peg." Standard lexicons derive amen from the Hebrew root *'mn* (firmness, faithfulness, reliability); the specific gloss "aman = tent peg" was not confirmed (Hebrew "tent peg" is *yated*, Judg 4:21). The speaker uses it as a homiletic image. → Flag for theological/etymological review; no change made to the transcript.

## 4. Proper nouns checked

Confirmed via ASR probabilities (>0.5 all unless noted) and context/verified sources: Andrei Rublev (Andrei p=0.944/0.943/0.776, Rublev p=0.999/0.984/0.998), Trinity, St. Patrick / Patrick's / Breastplate, Ireland, Saint Joseph, Druidism, Genesis 18, Abraham, Sarah, Isaac, Oak of Mamre (Oak p=0.568/0.565 — moderate; kept, context-consistent with SRC-015), Mount Moriah, Mount Sinai, Moses, Elijah, Mount Carmel, Sea of Galilee, Mount Tabor, Peter, James, John, Calvary, Pentecost, Holy Spirit, Christ, hypostatic union, Father, Son, Word, John 14, Luke 2, Matthew 28, Jael (corrected), Sisera, Israelites, Coptic, Eastern, Western, Hebrew, amen/aman, Eve, "St. Teresa" [possibly: Thérèse — see flag #4].

Note: "Ratzinger", "Newman", "Elizabeth of the Trinity", CCC, and canon-law citations — all present in the DOCX source list — do **not** appear in C01 audio; expected to surface in later conferences.

## 5. Open questions for the human listener

1. **00:02:46** — "if you were Jewish [possibly: pagan] and you believed in many gods": confirm the actual word. Argument context suggests "pagan".
2. **00:01:21** — garbled Druidism passage ("religion of Druidism … that saw that there was … that saw spirits"): confirm the speaker's exact wording; clean rendering is a conservative reconstruction.
3. **00:02:43** — "one God, one person, one God": all words high-probability, but confirm whether the final "one God" is the speaker's emphatic repetition or an ASR echo.
4. **00:06:22** — "when God says, 'Let us create man…'": confirm the dropped false start "It says," (It p=0.186) — speaker may have said "when God says it".
5. **00:07:59** — "this scepter, this stave — in their, I believe that's the word, stave? We'll go with that": confirm "stave" (staff) and the dangling "in their" (he means the left hands).
6. **00:12:53** — "It's original — when it was originally written": confirm whether the speaker said "It's original" or "In the original".
7. **00:17:21** — "bulk [possibly: both] ending it with the sign of the cross": confirm word. **RESOLVED (owner, batch 3, 2026-09-16): owner dictated the replacement sentence — "As Catholics, we are very used to beginning and ending prayer with the sign of the cross." Flag removed from the clean transcript and both chapter copies.**
8. **00:17:30** — "water poured three times over our heads": confirm word order (transposed in clean).
9. **00:18:31** — "even the 'and' of thus [possibly: these]": confirm the phrase. **RESOLVED (owner, batch 3, 2026-09-16): rendered with the owner's phrase — "Every word matters — even the 'and of the's." Flag removed from the clean transcript and both chapter copies.**
10. **00:19:13** — St. Teresa vs St. Thérèse of Lisieux: confirm whom the speaker named; the "simple glance" quote is Thérèse's.
11. **00:20:39** — "Pour it out for the forgiveness of sins.": confirm "Pour it out" vs "Poured out" (Pour p=0.938).
12. **00:20:41** — "This scent [possibly: descent] of the Holy Spirit is now with us.": confirm the word (scent p=0.355). Candidates: descent / sending / same. **RESOLVED (owner 2026-09-16, listening): "descent" confirmed; flag removed in clean + drafts/reviewed.**
13. **00:22:33** — "those nails that went through our Lord's hands, for them, for our salvation": confirm "for them" ("them" p=0.997) — possibly "for men" or "for us".
14. **00:23:10** — "We are made in his image and likeness": first word "We" p=0.039 (very low); context confirms, but listen.
15. **00:23:39** — "We are inscribed in our very natures" (repeats 00:23:10): confirm intentional emphatic repetition vs ASR echo.
16. **00:23:47** — "when God looked in creation": confirm "in" vs "at" (in p=0.865). And "We [possibly: He] looked upon us": confirm "He".
17. **00:24:42–00:24:46** — closing sign of the cross after the Glory Be: confirm complete; transcript ends at 00:24:46, media duration ≈ 24:49.
18. **00:21:04** — etymology claim "aman means tent peg": for the theological/etymological reviewer (see §3 note), not a transcription issue.

## 6. Compliance notes

- Raw transcript untouched; clean and editorial layers are new files.
- No invented theology, transitions, or citations; every edit above traces to a listed item.
- All six [possibly] flags carry the raw word plus a bracketed guess; nothing substituted silently.
- Status of this file: **pending human transcript sign-off** (handoff G2). Inventory row updated with transcript_path/reviewer/reviewed_at only; status remains INVENTORIED until a named human reviews.

## Owner resolutions 2026-09-16 (listening)

Recorded 2026-09-16 after the owner listened to the audio. Applied to the clean transcript, the chapter draft/reviewed copies, and this log.

1. **Q12 (00:20:41) — "scent [possibly: descent]" → "descent" (owner-confirmed).** The word is "descent". The `[possibly: descent]` flag is removed from the clean transcript and from both chapter copies. Annotated inline at §2 (flags table) and §5 Q12.

## Owner resolutions 2026-09-16 (batch 3)

Recorded 2026-09-16 after the owner's batch-3 resolutions. Applied to the clean transcript, the chapter draft/reviewed copies, and this log.

1. **Q7 (00:17:21) — "bulk [possibly: both]" → owner's dictated sentence.** Owner dictated the replacement wording: "As Catholics, we are very used to beginning and ending prayer with the sign of the cross." Applied in place of "Catholics, we are very used to beginning prayer and ending prayer, bulk [possibly: both] ending it with the sign of the cross." in the clean transcript and both chapter copies; flag removed. Annotated inline at §2 (flags row 2) and §5 Q7.
2. **Q9 (00:18:31) — "the 'and' of thus [possibly: these]" → owner's phrase.** Rendered with the owner's phrase, keeping his tone: "Every word matters — even the 'and of the's." Applied in the clean transcript and both chapter copies; flag removed. Annotated inline at §2 (flags row 3) and §5 Q9.
