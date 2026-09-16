# C06 "Evangelization" — Transcript Review Log

- **Recording:** C06_evangelization
- **Source SHA-256:** `c6ffff0258b4ecb3f3b69a202367f9944377f67b9d295ad083824f876c692aaa`
- **ASR run:** `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, int8, beam 1, temp 0, VAD, word timestamps)
- **Raw transcript:** `transcripts/raw/C06_evangelization.raw.20260916_fasterwhisper_largev3_nocond.md` (281 segments, 00:00:01–00:15:48; media duration ≈ 15:52)
- **Clean output:** `transcripts/clean/C06_evangelization.clean.md`
- **Editorial output:** `transcripts/editorial/C06_evangelization.editorial.md`
- **Reviewer:** pipeline-review · **Reviewed:** 2026-09-16
- **Method note:** No audio listening available to the machine reviewer. Corrections rest on (a) verified source texts (ledger/excerpts/DOCX) and (b) per-word ASR probabilities (words < 0.3 suspect, < 0.15 likely wrong). **Human audio spot-listening is required** for the open questions in §5 before sign-off.

## 1. Change summary (counts by category)

| Category | Count |
|---|---|
| Paragraphs in clean transcript (timestamp blocks) | 36 |
| [unclear HH:MM:SS] flags | 0 |
| [possibly: term] flags | 2 |
| Filler words deleted ("um"/"uh"/"you know") | 1 ("you know"; 0 um/uh) |
| Duplicated words / ASR segment-boundary echoes deleted | 5 |
| Abandoned false starts removed | 2 (incl. 1 isolated low-probability word) |
| Capitalization fixed (sentence starts, God, Father/Son/Holy Spirit, Trinity, Church, Amen, proper nouns) | ~140 |
| Punctuation added/adjusted (sentence ends, commas, em-dashes, quotes, colons) | ~140 |
| ASR errors corrected against verified source / standard form | 7 ("and"→"in" ×2 in Mt 28:18; "Misa/Misa Es"→"Missa est" ×4; "amen"→"Amen" ×7 counted in capitalization) |
| Minor grammar fixes (added "it", "than", possessive "'s") | 3 |
| Quotations / citations detected (see §3) | 24 |

Deletion/edit detail (raw → clean), all at segment boundaries unless noted:

1. `churches / Church's canon law` → `the Church's canon law` (00:02:18, "churches" p=0.92 = ASR split of "Church's" p=0.86; merged)
2. `light. Mother Teresa understood` → `his light. Mother Teresa understood` (00:04:20, boundary "light." p=0.003 = echo of previous segment's final word)
3. `beautiful, Pope Benedict says` → `beautiful, Pope Benedict says` (00:06:04, boundary "beautiful," p=0.17 deleted)
4. `belongs to a rather intellectual saint` → `it actually belongs to a rather intellectual saint` (00:04:05, "it" added — basic grammar fix, subject of the clause)
5. `then for us to know Christ` → `than for us to know Christ` (00:06:04, "then" p=0.80 — comparative "nothing more beautiful … than")
6. `the deacon part` → `the deacon's part` (00:08:51, possessive — human confirm)
7. `his agape, agape, that has been poured out` → `his agape — that has been poured out` (00:11:46, boundary "agape," p=0.50 deleted as echo)
8. `should be be spilling out` → `should be spilling out` (00:13:11, duplicated "be" p=0.43)
9. `not just be out of the words that we, you know, we reduce everything` → `not just be out of the words — we reduce everything` (00:13:15, false start "that we" + filler "you know" removed)
10. `We are to be the light to the world. own. How could we contain` → `…light to the world. How could we contain` (00:12:15, isolated "own." p=0.36 deleted as abandoned start; candidates "Oh"/"Now"/"our" — see Q17)
11. `All power and heaven and earth, all authority and heaven and earth has been given over to me` → `All power in heaven and earth — all authority in heaven and earth has been given over to me` (00:01:43–00:01:45, "and"→"in" ×2 corrected against SRC-019 Mt 28:18; "given over" kept as heard — RSV reads "given")
12. `Ite misa est / Misa est / Misa est / Misa Es` → `Ite, missa est / Missa est / Missa est / missa est` (00:09:17, 00:10:13, 00:10:18, 00:10:36; Latin form restored)
13. `amen.` → `Amen.` throughout (opening/closing sign of cross, prayer; capitalization)
14. `Glory be to the Father and to the Son and to the Holy Spirit` → commas added per standard text rendering used in C01/C03 (00:15:35)
15. `the Passion of the Christ` → `The Passion of the Christ` (00:09:44, film title)

## 2. Uncertainty flags ([possibly])

| # | Timestamp | Raw ASR text | Action | Reason |
|---|---|---|---|---|
| 1 | 00:08:33 | "Each of us burying in ourselves the flame of Christ in our hearts" | Kept "burying", flagged `[possibly: carrying]` | "burying" p=0.83, but context ("the candle that we carry", the fire meant to spread, never confined) favors "carrying" or "bearing". Human listen required. |
| 2 | 00:08:47 | "At the end of every Mass, the priests are actually more fittingly always the deacon" | Kept "the priests are", flagged `[possibly: the priest says]` | "priests" p=0.88, "are" p=0.66, yet the clause needs a dismissal-word subject; candidates: "the priest says", "the words are", "the dismissal is" (see Q12). Human listen required. |

## 3. Quotations and citations detected

| # | Timestamp | Item heard | Type / attribution | Verification vs ledger | Action in clean |
|---|---|---|---|---|---|
| 1 | 00:00:01, 00:01:18, 00:15:31, 00:15:46 | "In the name of the Father, and of the Son, and of the Holy Spirit. Amen." (repeated) | Liturgical formula / Mt 28:19 wording | Matches SRC-019 (RSV). VERIFIED. | Kept as spoken. |
| 2 | 00:00:06–00:01:17 | "Dear Jesus, help me to spread your fragrance everywhere I go… the evident fullness of the love my heart bears to you." | "Radiating Christ" prayer; speaker attributes it to St. John Henry Newman (00:02:37, 00:04:05) | **Not in ledger.** Widely printed as by (Bl.) John Henry Newman and prayed daily by St. Teresa of Calcutta; authorship traditionally Newman but questioned by some scholars. Wording matches common published text except: "will be for all from you" (print: "will be all from You"; "for" p=0.96 — variant kept as heard) and "not by words but by example" (print: "by my example" — no "my" in audio). Recommend adding to ledger; status ATTRIBUTION_UNCONFIRMED pending author/publisher confirmation. | Kept as heard; variants noted here. |
| 3 | 00:01:43–00:01:59 | "All power in heaven and earth — all authority in heaven and earth has been given over to me. Go, therefore, make disciples of all nations… Behold, I am with you always, even to the close of the age." | Matthew 28:18–20 | SRC-019 (RSV): VERIFIED_MINOR_VARIANT — speaker self-corrects "power"→"authority"; adds "over" ("given over to me" vs RSV "given to me"); "Go, therefore, make disciples" vs RSV "Go therefore and make"; "Behold" matches DOCX variant "and behold" vs RSV "and lo". "and"→"in" corrected against source. | Kept as heard (with source-based "in"); discrepancies logged. |
| 4 | 00:02:23–00:02:31 | "all of us, by virtue of our baptism and confirmation, are by nature missionary" | Code of Canon Law, Can. 225 §1 / Can. 781 paraphrase | SRC-005 + SRC-006: PARAPHRASE_CONFIRMED — speaker condenses both canons, does not quote. | Kept as spoken. |
| 5 | 00:02:55–00:03:12 | "How, Lord, when did we see you hungry… find you in prison and visit you?" / "Amen. Whatever you did for the least of my brothers, you did for me." | Matthew 25:37–40 paraphrase | Not in ledger. RSV: "Truly, I say to you, as you did it to one of the least of these my brethren…" Speaker's "Amen." replaces "Truly, I say to you" (kept as heard); "least of my brothers" = loose rendering. Paraphrase — no source match forced. | Kept as heard. |
| 6 | 00:03:16–00:03:23 | "Saul, Saul, why are you persecuting me?" / "Who are you, Lord, that I may know who I'm persecuting?" / "I am Jesus, whom you are persecuting." | Acts 9:4–5 | Not in ledger. Acts 9:5 RSV: "Who are you, Lord?" — the expansion "that I may know who I'm persecuting" is the speaker's own addition (all words p ≥ 0.66; human confirm, Q5). | Kept as heard. |
| 7 | 00:04:09 | "a rather intellectual saint of the 19th century, an Oratorian priest named John Henry Newman" | Factual claim | Newman founded the Birmingham Oratory, joined the Oratory 1845 — accurate. Cf. SRC-010. | Kept. |
| 8 | 00:06:02–00:06:19 | "There's nothing more beautiful, Pope Benedict says, than for us to know Christ, for us to know that we are loved by him, and for us to tell others of our friendship with him." | Benedict XVI, homily 24 April 2005 | SRC-004: VERIFIED_EXACT for the homily text ("There is nothing more beautiful than to know Him and to speak to others of our friendship with Him"). Speaker paraphrases and inserts "for us to know that we are loved by him" (not in the homily) — kept as heard; paraphrase, not forced to source. | Kept as heard. |
| 9 | 00:06:41–00:06:53 | "Who, having a light, puts it under a basket?" / "You are the light of the world" / "I am the light of the world" | Matthew 5:15, Matthew 5:14, John 8:12 | Not in ledger. Loose quotes: Mt 5:15 RSV "Nor do men light a lamp and put it under a bushel, but on a stand". Speaker's "you put on a lampstand" (no "it") kept as heard. | Kept as heard. |
| 10 | 00:07:05–00:07:08 | "Christ came that we might have life and have it abundantly" / "He came to set the world on fire, and how he wished it were already ablaze" | John 10:10 / Luke 12:49 paraphrase | Not in ledger. Jn 10:10 RSV "I came that they may have life, and have it abundantly"; Lk 12:49 RSV "I came to cast fire upon the earth; and would that it were already kindled!" — speaker paraphrases. | Kept as heard. |
| 11 | 00:07:11–00:07:28 | "go, set the world on fire" attributed to St. Ignatius of Loyola to his missionaries | Traditional attribution ("Ite, inflammate omnia") | Not in ledger. The dictum is traditionally credited to St. Ignatius but is not documented in his own writings — flag ATTRIBUTION_UNCONFIRMED for the citation reviewer. Kept as heard. | Kept as heard. |
| 12 | 00:07:57–00:08:05 | "That same fire that St. Patrick had blessed in the 400s that could not be extinguished by any attempts of the Druid pagans" | Hagiographic tradition (St. Patrick's paschal fire at Slane) | Not in ledger. The story appears in Muirchú's *Life of St. Patrick* and the Tripartite Life. Status LOCATOR_MISSING — needs a named edition. Kept as heard. | Kept as heard. |
| 13 | 00:08:21 | "Lumen Christi — the light of Christ" | Easter Vigil acclamation | Liturgical; standard text. | Kept; italics not used (matches house style). |
| 14 | 00:08:59–00:09:06 | "Go forth, the Mass has ended" / "Go and announce the gospel of the world" | Mass dismissal formulas | Paraphrase of the dismissal options ("Go forth, the Mass is ended" / "Go and announce the Gospel of the Lord" / "Go in peace…"). "gospel" p=0.45 (Q13); "of the world" kept as heard (p=1.00) though the Missal reads "of the Lord". | Kept as heard. |
| 15 | 00:09:17–00:10:36 | "Ite, missa est… 'Ite' means go… 'Missa est' does not mean 'the Mass has ended.' It means 'it has been sent.'" | Liturgical formula + etymology claim | Etymology ("missa" from sending/dismissal) matches standard scholarly account. Speaker's grammar gloss ("something has been sent") kept as heard. | Latin form corrected. |
| 16 | 00:09:41 | "Behold, I make all things new." | Revelation 21:5 | Not in ledger. RSV: "Behold, I make all things new." — exact. | Kept. |
| 17 | 00:09:56 | "Behold, Mother, I make all things new." | The Passion of the Christ (2004) scene | Film line is "See, Mother, I make all things new." Speaker's "Behold" (p=0.75) kept as heard; discrepancy noted (Q14). | Kept as heard. |
| 18 | 00:11:45–00:12:06 | "his agape… the pouring out of God — his agape — and our Eucharistia" | Theological terms (Greek) | No quoted source; vocabulary consistent with C03 theme. | Kept. |
| 19 | 00:12:21 | "transformed by the renewal of your mind" | Romans 12:2 allusion | Not in ledger. RSV: "but be transformed by the renewal of your mind" — allusion, no verbatim conflict. | Kept as spoken. |
| 20 | 00:13:50 | "no one is a mere mortal, as C.S. Lewis would say" | The Weight of Glory | Not in ledger. Lewis: "There are no ordinary people. You have never talked to a mere mortal." — paraphrase. | Kept as heard. |
| 21 | 00:13:53 | "everyone, as St. John Henry Newman says, is an infinite abyss of existence" | Newman, "The Individuality of the Soul" | SRC-010: VERIFIED_EXACT — "He has a depth within him unfathomable, an infinite abyss of existence" (Parochial and Plain Sermons IV.6). Speaker's compressed rendering kept as heard. | Kept as heard. |
| 22 | 00:14:53–00:14:56 | "Let the waves and the billows, the torrents, all wash over us" | Psalm 42:7 allusion | SRC-014 (RSV): "all thy waves and thy billows have gone over me" — PARAPHRASE_CONFIRMED. | Kept as heard. |
| 23 | 00:15:35–00:15:43 | "Glory be to the Father, and to the Son, and to the Holy Spirit, as it was in the beginning, is now, and ever shall be, world without end. Amen." | Glory Be (standard English text) | Not in ledger; standard text — matches common English rendering (as C01). | Kept. |
| 24 | 00:09:32–00:09:36 | "all things might be recapitulated in him" | Ephesians 1:10 allusion | Not in ledger. RSV: "to unite all things in him" — "recapitulated" = traditional rendering (Vulgate instaurare/recapitulare tradition). Allusion. | Kept as heard. |

Also noted (not quotations, factual/theological claims for reviewer):
- **00:10:21–00:10:36** — the speaker's gloss of the grammar of *missa est* ("something has been sent"; "Who has it been sent to?" — the offering sent *to the Father*). Coherent with his point that the Mass is our offering to the Father, not offered *to us*; no change made.
- **00:05:28** — "In an atomic bomb, this would result in a massive explosion of megatons of dynamite" — pastoral analogy, not a physics claim; kept verbatim.

## 4. Proper nouns checked

Confirmed via ASR probabilities (>0.5 unless noted) and context/verified sources: St. Patrick, Ireland, Druid pagans, St. John Henry Newman (Newman p=1.00 ×3), Oratorian, Mother Teresa (Teresa p=0.96/0.99), Matthew 25, St. Paul, Saul, Pope Benedict (Benedict p=1.00), Holy Eucharist, corporal works of mercy, Trinity / Holy Trinity, St. Ignatius of Loyola (Ignatius p=1.00, Loyola p=0.87), Jesuits, Easter Vigil, Paschal candle, Lumen Christi, deacon, Ite missa est (Latin form corrected), Eucharistia, agape, Revelation, The Passion of the Christ, C.S. Lewis, Romans 12:2 (allusion), Psalm 42 (allusion), Glory Be, four corners of the world, Church (capitalized as institution), Father, Son, Holy Spirit, Jesus, Christ.

Note: low-probability proper-noun-adjacent words ("gospel" p=0.45 at 00:09:02, "Holy" p=0.37 at 00:14:16, "Passion" p=0.64 at 00:09:44) were kept because semantic context is unambiguous; see §5 for human confirmation.

## 5. Open questions for the human listener

1. **00:00:46** — prayer line "The light, O Jesus, will be for all from you": confirm "for all" (p=0.96) vs printed "will be all from You".
2. **00:01:05** — prayer line "not by words but by example": confirm whether the speaker said "by my example" (printed text) — no "my" in audio.
3. **00:01:59** — "even to the close of the age": "even" p=0.03 (very low); context strongly implies it (KJV-style "even unto"), but confirm.
4. **00:02:18** — "the churches / Church's canon law": confirm the merge to "the Church's canon law".
5. **00:03:18** — "Who are you, Lord, that I may know who I'm persecuting?": all words p ≥ 0.66 but the expansion is not in Acts 9:5; confirm the speaker's wording.
6. **00:04:31** — "We are other Christs, not just for any, because we belong to Christ": "for any" (for p=0.82, any p=1.00) is incoherent; confirm what was said.
7. **00:05:21** — "who cannot experience the love of God through us even, and be transformed by it?": confirm "even" placement.
8. **00:06:32** — "And then others received also into that gift of the Trinity": "and" p=0.04, "received" p=0.51; confirm sentence.
9. **00:06:53 / 00:11:29** — "other Christ" (singular) vs "other Christs" (plural at 00:04:31, 00:11:09): confirm each instance.
10. **00:07:46** — "The way we evangelize the love of the Trinity is the same way we evangelize": confirm the repeated phrase (emphatic vs ASR echo).
11. **00:08:33** — "burying [possibly: carrying] in ourselves the flame": confirm word (burying p=0.83; carrying/bearing candidates).
12. **00:08:47** — "the priests are [possibly: the priest says] actually more fittingly always the deacon": confirm wording; candidates "the priest says", "the words are", "the dismissal is".
13. **00:09:02** — "Go and announce the gospel of the world": "gospel" p=0.45; Missal reads "Gospel of the Lord" — confirm what the speaker said ("world" p=1.00 kept as heard). Also "on any" (on p=0.80) at 00:09:04.
14. **00:09:56** — "Behold, Mother, I make all things new": film line is "See, Mother…"; confirm the speaker's word.
15. **00:10:04** — "and happens through us": "happens" p=0.58; confirm.
16. **00:11:37** — "that where we could always pray to the Father in secret": "where" p=0.54; candidates "there"/"where".
17. **00:12:15** — isolated "own." (p=0.36) deleted as abandoned start; confirm (candidates: "Oh", "Now", "our own").
18. **00:12:43** — "but just know that Jesus loves you": "know" p=0.21; confirm.
19. **00:13:15** — "not just be out of the words — we reduce everything to the words": false start "that we, you know," removed; confirm reconstruction.
20. **00:15:48–00:15:52** — transcript ends 00:15:48; media duration ≈ 15:52 — confirm tail is clean (closing sign of the cross complete).

## 6. Compliance notes

- Raw transcript untouched; clean and editorial layers are new files.
- No invented theology, transitions, or citations; every edit above traces to a listed item.
- Both [possibly] flags carry the raw word plus a bracketed guess; nothing substituted silently.
- Quotations kept as heard where the speaker paraphrases; source wording was never forced onto the audio (except the two "and"→"in" corrections in Mt 28:18, corrected against SRC-019/DOCX).
- Status of this file: **pending human transcript sign-off** (handoff G2). Inventory row updated with transcript_path/reviewer/reviewed_at only; status remains INVENTORIED until a named human reviews.
