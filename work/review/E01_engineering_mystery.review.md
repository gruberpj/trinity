# E01 "Engineering Mystery" — Transcript Review Log

- **Recording:** E01_engineering_mystery
- **Source SHA-256:** `d4795bdcce1135868c2a85445c5d8b6b8a980843f204d58485e8d00423b18377`
- **ASR run:** `20260916_fasterwhisper_largev3_nocond` (faster-whisper 1.2.1, large-v3, int8, beam 1, temp 0, VAD, word timestamps)
- **Raw transcript:** `transcripts/raw/E01_engineering_mystery.raw.20260916_fasterwhisper_largev3_nocond.md` (858 segments, 00:00:02–00:46:02; media duration ≈ 46:06)
- **Clean output:** `transcripts/clean/E01_engineering_mystery.clean.md`
- **Editorial output:** `transcripts/editorial/E01_engineering_mystery.editorial.md`
- **Reviewer:** pipeline-review · **Reviewed:** 2026-09-16
- **Method note:** No audio listening available to the machine reviewer. Corrections rest on (a) verified source texts (ledger/excerpts/DOCX) and (b) per-word ASR probabilities (words < 0.3 suspect, < 0.15 likely wrong). **Human audio spot-listening is required** for the open questions in §6 before sign-off.

## 1. Change summary (counts by category)

| Category | Count |
|---|---|
| Paragraphs in clean transcript (timestamp blocks) | 43 |
| [unclear HH:MM:SS] flags | 0 |
| [possibly: term] flags | 6 |
| Filler words deleted ("um"/"uh") | 0 |
| Duplicated words / ASR segment-boundary echoes deleted | 18 |
| Abandoned false starts / fragments removed | 4 |
| Capitalization fixed (sentence starts, I, God, Father/Son/Holy Spirit, Trinity, proper nouns, book names, quoted titles) | ~160 |
| Punctuation added/adjusted (sentence ends, commas, em-dashes, quotation marks) | ~210 |
| ASR errors corrected against verified source text | 1 (Augustine, Confessions — see §3; source to be added to ledger by Prompt E) |
| Proper nouns corrected (probability + context) | 4 ("Fred Sisson" → Franciscan; "Carol Ortiz" → Karol Wojtyła; "Liszt" → Lisieux; "what may be" → Max Weber) |
| Minor grammar fixes (word order, prepositions, articles, plural, verb form) | 15 |
| Quotations / citations detected (see §3) | 30 |

Deletion/edit detail (raw → clean), all at segment boundaries unless noted:

1. `So my name is Father Peter Gruber.` → `My name is Father Peter Gruber.` (00:00:02, leading discourse marker "So")
2. `You heard from Dr. Sanchez earlier. earlier,` → `earlier —` (00:00:25, 2nd "earlier," p=0.018)
3. `when he was still just graduate student` → `just a graduate student` (00:00:29, 'a' added)
4. `I was very much of the engineering worldview. of you. It was a safe way` → `worldview. It was a safe way` (00:02:22, fragment "of you" p=0.215/0.694 removed; see Q27)
5. `for the most part it / It actually worked.` → `it actually worked.` (00:03:41, boundary dup "It")
6. `the Fred Sisson Youth Conference` → `the Franciscan youth conference` (00:07:19, Fred p=0.280, Sisson p=0.440; internal consistency with 00:04:12 "Franciscan youth conference", Franciscan p=0.997) — **Q11 confirmed by owner listening 2026-09-16.**
7. `read this, imaging classes,` → `read this in between classes,` (00:07:53, imaging p=0.498)
8. `towards silence, the regressing,` → kept `the regressing` + `[possibly: the resting]` (00:08:17, regressing p=0.743; see flag #1)
9. `I have an idea for you / you after / not this summer` → `You are to — not this summer` (00:09:26, "after" p=0.974; reconstruction "are to"; see Q7)
10. `Come a Trinity Sunday` → `Come Trinity Sunday` (00:10:26, "a" p=0.387)
11. `the same priest that that have influenced` → `the same priest who had influenced` (00:11:28, 2nd "that" p=0.473)
12. `I work in chemistry` → kept `chemistry` + `[possibly: campus ministry]` (00:11:30, chemistry p=0.284; see flag #2) — **flag #2 removed by owner resolution 2026-09-16 (listening): "campus ministry" confirmed.**
13. `a son or daughter of God's Father` → `of God the Father` (00:12:16, God's p=0.857; grammar; see Q26)
14. `an incentive not to virtue, virtue, but to a great fear` → dup `virtue,` deleted (00:06:24, 2nd p=0.279)
15. `Not YouTube then. Then,` — 2nd "Then," p=0.148 but context-required; kept
16. `how they looked up the stars` → `how they looked up at the stars` (00:17:33, 'at' added)
17. `the engineering world of you,` → `the engineering worldview,` (00:18:05, "world of you" p=0.730/0.611/0.885 = split of "worldview"; internal consistency — phrase occurs 6× elsewhere at p≥0.9)
18. `Carol Ortiz. one. Gabriel Marcel` → `Karol Wojtyła. Gabriel Marcel` (00:18:43, Ortiz p=0.449, "one." p=0.054 removed; context: 20th-c. personalism, "a different area of the world" = Poland vs France; see Q8) — **Q8 confirmed by owner listening 2026-09-16.**
19. `mystery novels, mystery novels are problems` — kept as emphatic repetition (both instances p=1.000)
20. `any difference and the angle` → `any difference in the angle` (00:15:19, and p=0.893; grammar)
21. `You'll see that's following both of you` → `that it's following both of you` (00:15:52, 'it' added)
22. `The moon had any care` → `Had the moon any care` (00:16:38, word-order fix for rhetorical question)
23. `things of his world` → `things of this world` (00:29:18, his p=0.448)
24. `But as everyone, he looked` → kept + `[possibly: at last]` (00:29:21, see flag #3)
25. `Laid have I loved you, beauty be ever ancient, ever now. Laodice, I love you.` → `Late have I loved you, Beauty ever ancient, ever new — late have I loved you!` (00:29:26, source-driven: Augustine, Confessions X.27; "Laid" p=0.589, "be" p=0.156, "Laodice," p=0.557; see Q5)
26. `You have made us for yourselves` — kept (yourselves p=0.993; standard translations use singular "yourself/thyself"; see Q5)
27. `God rest in those deepest` → `God rests in those deepest` (00:30:24, rest p=0.465; grammar)
28. `Phrasing that part of the engineering worldview` — kept as heard (Phrasing p=0.739; see Q23)
29. `what may be a 19th century German philosopher called` → `what Max Weber, a 19th-century German philosopher, called` (00:31:57, what p=0.994, may p=0.719, be p=1.000; reconstruction — grammar demands a name; "enchanted world" alludes to Weber's *Entzauberung der Welt*; see Q1)
30. `not near magic` → kept `near` + `[possibly: mere]` (00:32:16, near p=0.854; see flag #4)
31. `an egon yet to be transformed` → kept `egon` + `[possibly: icon]` (00:33:01, egon p=0.311; see flag #5)
32. `respond him in redeeming us` → `respond to him in redeeming us` (00:34:23, him p=0.232; 'to' added)
33. `in the offer to our enemy, give ourselves over` → `in the Offertory, we give ourselves over` (00:34:46, "enemy," p=0.172; reconstruction; see Q9) — **Q9 confirmed by owner listening 2026-09-16.**
34. `to to stay out of constant speed` → `to stay at a constant speed` (00:35:16, dup "to" p=0.260; out-of → at-a grammar fix)
35. `they do not not amid of excess` → `they do not admit of excess` (00:37:16, dup "not"; amid → admit)
36. `too much courage is full heartedness` → `is foolhardiness` (00:37:20, "full heartedness" p=0.503/0.753 = split word; see Q14)
37. `the smallest amounts amounts` → `the smallest amounts` (00:37:44, dup)
38. `the engineering worldview worldview,` → `the engineering worldview,` (00:38:13, 2nd p=0.663)
39. `the emphasis we have as Franciscan here` → `as Franciscans here` (00:39:15, plural)
40. `to what you're meant to be` → kept `to` + `[possibly: of]` (00:39:37, to p=0.625; see flag #6)
41. `gets in the way on this habit` → `of this habit` (00:39:40, on p=0.977; preposition fix)
42. `social media media. Get caught up` → `social media. Get caught up` (00:40:13, dup)
43. `like like pigs` → `like pigs` (00:41:08, dup)
44. `doom scroll` → `doomscroll` (00:41:08)
45. `life. In the interior life,` → `In the interior life,` (00:42:37, boundary dup)
46. `attitudes we have have to have` → `have to have` (00:43:33, dup)
47. `are heavy burdened` → `are heavily burdened` (00:45:34, grammar)
48. `a beloved daughter, beloved son` → `a beloved daughter, a beloved son` (00:25:55, 'a' added; 2nd "beloved" p=0.641)
49. `St. Therese of Liszt` → `St. Thérèse of Lisieux` (00:26:12, Liszt p=0.731; proper noun, obvious form)
50. `It's a Latin word. It's a Latin word, intimus.` → `It's a Latin word — intimus.` (00:28:13/28:15, boundary dup)
51. `Okay, so I'm going to... I've said anything, so I'm sorry.` — kept as heard (I've p=0.672, anything, p=0.773; see Q4)
52. `Intimacy. Intimos. In. In. Comparative. Superlative. of intimus.` → `Intimacy. In. Interior. Comparative. Superlative: intimus.` (00:28:51-59, 2nd "In." p=0.005 → "Interior."; board sequence reconstruction; see Q3)
53. `transubstantiated the body` → `transubstantiated into the body` (00:25:11, 'into' added)
54. `throw herself in the arms` → `into the arms` (00:26:22, grammar)
55. `It's in the silence of the heart Christ instructs` → `... heart that Christ instructs` (00:27:08, 'that' added)
56. `Who's ever heard the intimacy means into me see?` → `that "intimacy" means "into me see"?` (00:27:55, the→that; quote marks added)
57. `Fatherhood mirrors it. it. Friendship` → `it. Friendship` (00:23:11, dup)
58. `Yes, wow, yes. yes. And my mom` → `Yes, wow, yes. And my mom` (00:11:02/11:04, boundary dup)
59. `returned from from a trip` → `from a trip` (00:14:54, dup)
60. `of being. Being. Being that we have` → `of being. Being that we have` (00:20:45, restart removed)
61. `Loneliness does not give in to despair. Adores it.` → em-dash join (00:23:19)
62. `the three-fold invocation` → `the threefold invocation` (00:25:40, hyphen)
63. `a four year old` → `a four-year-old` (00:15:58, hyphens)

## 2. Uncertainty flags ([possibly])

| # | Timestamp | Raw ASR text | Action | Reason |
|---|---|---|---|---|
| 1 | 00:08:17 | "opening up towards silence, the regressing, and the embrace of Christ" | Kept "regressing", flagged `[possibly: the resting]` | "regressing" p=0.743 but contextually odd; candidates: "the resting" (parallel: silence, resting, embrace). Human listen required. |
| 2 | 00:11:30 | "I work in chemistry to give back to the students at Pitt, CMU, and Chatham" | Kept "chemistry", flagged `[possibly: campus ministry]` | "chemistry" p=0.284 (<0.3, suspect). Opening sentence (00:00:12) says "we serve the campus ministry for the University of Pittsburgh, Carnegie Mellon, and Chatham Universities" — decisive internal context. Human listen required. **RESOLVED by owner listening 2026-09-16: "campus ministry" confirmed; flag removed from the clean transcript.** |
| 3 | 00:29:21 | "But as everyone, he looked into his heart" | Kept "as everyone", flagged `[possibly: at last]` | "as everyone," p=0.744 but ungrammatical; "at last" fits the contrast (looked outside → at last looked within). Human listen required. **RESOLVED (owner, batch 3, 2026-09-16): "at last" — "But at last, he looked into his heart." Flag removed from the clean transcript and both chapter copies.** |
| 4 | 00:32:16 | "When we live in this way as Christians, not near magic, but the love of God..." | Kept "near", flagged `[possibly: mere]` | "near" p=0.854; "mere magic" parallels the talk's repeated "mere matter"/"mere bread and wine". Human listen required. **RESOLVED (owner, batch 3, 2026-09-16): "mere" — "not mere magic". Flag removed from the clean transcript and both chapter copies.** |
| 5 | 00:33:01 | "It is an egon yet to be transformed" | Kept "egon", flagged `[possibly: icon]` | "egon" p=0.311 (<0.3). Candidates: "icon" (creation as icon to be transformed — echoes C01's iconography and the following recapitulation theme) or "eon". Human listen required. |
| 6 | 00:39:37 | "won't deprive you of what you're meant to have, to what you're meant to be" | Kept "to", flagged `[possibly: of]` | "to" p=0.625; parallel construction suggests "of what you're meant to have, of what you're meant to be". Human listen required. **RESOLVED (owner, batch 3, 2026-09-16): "of" — "of what you're meant to have, of what you're meant to be." Flag removed from the clean transcript and both chapter copies.** |

## 3. Quotations and citations detected

Ledger status column: rows marked **NOT_IN_LEDGER** are candidates for Prompt E addition; nothing was corrected against them in this stage except the Augustine line (item 12, source-driven with the flag in §1/25 and open question Q5).

| # | Timestamp | Item heard | Type / attribution | Verification vs ledger | Action in clean |
|---|---|---|---|---|---|
| 1 | 00:00:55, 00:01:41, 00:45:45, 00:45:58 | "In the name of the Father, and of the Son, and of the Holy Spirit. Amen." | Liturgical formula / Mt 28:19 wording | SRC-019 (RSV): VERIFIED — wording matches ("I baptize you" variant also used at 00:25:42). | Kept as spoken. |
| 2 | 00:00:58-00:01:22 | Marian prayer ("Blessed Virgin Mary, may we be responsive to your spouse...") | Speaker's own composed prayer | NOT_IN_LEDGER (author's composition). | Kept as spoken. |
| 3 | 00:01:27-00:01:35 | "Hail Mary, full of grace, the Lord is with thee..." | Hail Mary (standard English text) | NOT_IN_LEDGER; standard text. | Kept. |
| 4 | 00:01:45-00:01:53 | "Do not be conformed to this age, but be transformed by the renewal of your mind." Romans 12. | Romans 12:2, quoted with reference by speaker | NOT_IN_LEDGER. Wording matches NABRE-style "this age" with RSV-style "Do not be conformed"; exact edition needs author confirmation (cf. unresolved.md item F). Speaker repeats the verse at 00:31:35-37 as "to not be conformed to this age but be transformed by the renewal of your mind". | Kept as heard (quoted). |
| 5 | 00:07:48 | "the Imitation of Christ" | Thomas à Kempis, work reference | NOT_IN_LEDGER (title only, no quotation). | Kept. |
| 6 | 00:09:30, 00:10:26 | "Trinity Sunday — that's the Sunday after Pentecost" | Liturgical calendar fact | Standard; correct. | Kept. |
| 7 | 00:12:26 | "Arthur Conan Doyle's Sherlock Holmes" | Literary reference | Standard; correct. | Kept. |
| 8 | 00:18:34-00:19:17 | Gabriel Marcel, personalism, "problem vs mystery", "mystery involves the viewer" | Philosophical paraphrase | NOT_IN_LEDGER. Marcel's problem/mystery distinction is standard (Être et avoir, 1935); speaker paraphrases, no verbatim quotation. Karol Wojtyła named as fellow personalist (corrected proper noun, §4). | Kept as spoken. |
| 9 | 00:19:17-00:20:20 | Observer effect, qubit collapse ("once you measure it, it defaults to a zero or a one") | Physics illustration | Standard physics (cf. SRC-003 Ratzinger, Intro to Christianity, makes the same observer-participation point — good cross-reference for the book). | Kept as spoken. |
| 10 | 00:24:18-00:24:45 | Newman: invisible world "more real... than the visible world"; visible world "like a shroud placed over us" | Attributed to St. John Henry Newman (childhood) | NOT_IN_LEDGER. Lead for Prompt E: Apologia pro Vita Sua (1864), Part I, childhood recollection ("I thought the visible world... a veil" — wording to be verified). Speaker retells, does not read. | Kept as spoken. |
| 11 | 00:25:42-00:25:45 | "I baptize you in the name of the Father, and of the Son, and of the Holy Spirit" | Baptismal formula (Mt 28:19) | SRC-019 (RSV): VERIFIED wording for the Trinitarian formula. | Kept as spoken (quoted). |
| 12 | 00:26:12-00:26:28 | St. Thérèse of Lisieux: "even if she were to commit the worst sin, she could throw herself into the arms of God, her Father, and be confident that he would catch her" | Attributed to Thérèse, "in one of her letters" | NOT_IN_LEDGER. Lead for Prompt E: likely her letters (LT), phrasing "I would throw myself into the arms of..." — verify. Speaker paraphrases from memory. | Kept as spoken. |
| 13 | 00:26:47-00:26:55 | "God the Father spoke one word from all eternity — St. John of the Cross says — and that word was his Son, and that word was uttered in silence" | Attributed to St. John of the Cross | NOT_IN_LEDGER. Lead for Prompt E: cf. Sayings of Light and Love / Maxims ("The Father spoke one Word, which was His Son, and this Word He speaks always in eternal silence..."). | Kept as spoken. |
| 14 | 00:27:13-00:27:23 | "when you pray, do not be like the hypocrites who like to stand on street corners and marketplaces... go into your inner room, close the door, and your Father who hears in secret will reward you" | Matthew 6:5-6, paraphrase | NOT_IN_LEDGER. RSV: "And when you pray, you must not be like the hypocrites; for they love to stand and pray in the synagogues and at the street corners..." Speaker's memory paraphrase; not forced to match. | Kept as spoken. |
| 15 | 00:28:15-00:29:11 | "intimus" — Latin superlative of "in" ("the most in"), "intimacy" ≠ "into me see" (folk etymology debunked) | Linguistic/etymology claim | NOT_IN_LEDGER. Lexically standard (intimus = superlative of interior). The debunking of "into me see" is correct. Flag for theological/etymological review like C01's amen/tent-peg note; no transcript change. | Kept as spoken. |
| 16 | 00:29:26-00:29:35 | "Late have I loved you, Beauty ever ancient, ever new — late have I loved you! You have made us for yourselves, O Lord, and our hearts are restless till they rest in thee." | St. Augustine, Confessions X.27 and I.1 | NOT_IN_LEDGER. Wording matches the standard English rendering ("Late have I loved you, O Beauty ever ancient, ever new" — Chadwick/Pine-Coffin tradition); "You have made us for yourself... restless until they rest in you" = Conf. I.1. ASR errors corrected against this source text (see §1/25); add to ledger in Prompt E. | Corrected to source wording (flagged). |
| 17 | 00:30:15-00:30:21 | "I looked into my deepest wound, and there I saw your glory, and it dazzled me." | Attributed by speaker to St. Augustine with hedge ("apparently said") | NOT_IN_LEDGER. Widely circulated quotation of doubtful authenticity (speaker himself hedges: "apparently"). → ATTRIBUTION_UNCONFIRMED candidate for Prompt E; keep speaker's hedge in any book use. | Kept as spoken (speaker's hedge preserved). |
| 18 | 00:30:42-00:30:54 | "and this is love: not that we have loved God, but that he has loved us and sent his Son as expiation for our sins" | 1 John 4:10, near-quotation + homiletic expansion | NOT_IN_LEDGER. RSV: "In this is love, not that we loved God but that he loved us and sent his Son to be the expiation for our sins." Speaker's variant kept (paraphrase from memory). | Kept as spoken (not forced). |
| 19 | 00:31:57-00:32:07 | "living in what Max Weber, a 19th-century German philosopher, called 'living in an enchanted world that has a magic behind it'" | Allusion to Max Weber's "disenchantment of the world" (*Entzauberung der Welt*) | NOT_IN_LEDGER. Name reconstructed from ASR "what may be" (§1/29, Q1). Weber (1864-1920) is usually classed early-20th-century; speaker says "19th century" — keep as heard, note for author. | Reconstructed (flagged). |
| 20 | 00:33:01-00:33:09 | "an egon [possibly: icon] yet to be transformed... Christ came to draw all things to himself, to recapitulate all things in Christ, and to offer himself to God the Father" | Eph 1:10 allusion + Irenaean recapitulation | NOT_IN_LEDGER. Paraphrase; no verbatim conflict. | Kept as spoken. |
| 21 | 00:35:44-00:35:58 | "the law of the gift" — "when you give something away, you don't lose it. You actually gain." | John Paul II, theology of the body, "law of the gift" | NOT_IN_LEDGER. Concept standard in TOB catechesis; speaker's own gloss ("It's actually a spiritual life hack"). | Kept as spoken. |
| 22 | 00:36:05-00:36:08 | "There's only a sincere gift of oneself, the Second Vatican Council says, that man finds himself." | Gaudium et Spes 24, paraphrase | NOT_IN_LEDGER. GS 24: "man... cannot fully find himself except through a sincere gift of himself." Speaker's compressed oral rendering kept; discrepancy logged here for Prompt E. | Kept as spoken. |
| 23 | 00:37:09-00:37:28 | "Faith, hope, and love. The greatest of these is love." + theological virtues "do not admit of excess" | 1 Corinthians 13:13 + virtue-ethics point | NOT_IN_LEDGER. 1 Cor 13:13 standard; "too much courage is foolhardiness" = classical mean doctrine. | Kept as spoken. |
| 24 | 00:37:49-00:38:04 | Widow's two small coins ("that woman has given more than everyone else... She gave from her poverty, her whole livelihood") | Mark 12:41-44 / Luke 21:1-4, retelling | NOT_IN_LEDGER. Retelling with "on the eve of his passion" setting — consistent with Luke's Jerusalem context. | Kept as spoken. |
| 25 | 00:38:13-00:38:35 | "whatever is worth doing is worth doing well" contrasted with Chesterton: "Whatever is worth doing is worth doing poorly." | G.K. Chesterton aphorism | NOT_IN_LEDGER. **Verified this stage:** Chesterton, What's Wrong with the World (1910), Part IV, ch. XIV ("Folly and Female Education"), closing line: "that if a thing is worth doing, it is worth doing badly." (Project Gutenberg eBook #1717, accessed 2026-09-16.) Speaker's "whatever... poorly" is his own paraphrase of "if a thing is worth doing, it is worth doing badly" — VERIFIED_MINOR_VARIANT; add to ledger. | Kept as spoken (paraphrase). |
| 26 | 00:39:47-00:39:55 | "what the author of The Soul of the Apostolate calls dissipation... We ought to have the custody of our hearts" | Jean-Baptiste Chautard, OCSO, The Soul of the Apostolate | NOT_IN_LEDGER. "Custody of the heart" and "dissipation" are Chautard's recurring themes; speaker paraphrases. | Kept as spoken. |
| 27 | 00:41:37-00:41:44 | "As Pope Benedict says, you are not made for comfort. You are made for greatness." | Attributed to Pope Benedict XVI | NOT_IN_LEDGER. Lead for Prompt E: Benedict XVI, Address at the vigil with young people, XX World Youth Day, Marienfeld (Cologne), 20 August 2005 ("You were not made for comfort, you were made for greatness" — wording to be verified against vatican.va; the 21 Aug 2005 Marienfeld homily does NOT contain it — checked this stage). Keep as spoken; do not print as a direct quotation until verified. | Kept as spoken. |
| 28 | 00:43:45-00:44:00 | Newman "watching... that feeling you have when you're expecting a friend to come to your house, and for some reason he's delayed" | Attributed to St. John Henry Newman | NOT_IN_LEDGER. Lead for Prompt E: Newman, "Watching," Parochial and Plain Sermons vol. IV, sermon 22 (1839). Speaker paraphrases; also notes Newman "was an Oratorian priest like myself" (correct). | Kept as spoken. |
| 29 | 00:45:34-00:45:42 | "Come to me, all you who labor and are heavily burdened, and I will give you rest." | Matthew 11:28, near-quotation | NOT_IN_LEDGER. RSV: "Come to me, all who labor and are heavy-laden, and I will give you rest." Speaker's variant "heavily burdened" kept (memory paraphrase; also §1/47). | Kept as spoken (quoted). |
| 30 | 00:45:49-00:45:57 | "Glory be to the Father, and to the Son, and to the Holy Spirit..." | Glory Be (liturgical, standard English text) | Not in ledger; standard text — matches the common English rendering. | Kept. |

Also noted (not a quotation, but factual claims for author review): **00:13:39** — "Think of the eclipse we had a year and a half ago" (recording dated Sept 2026; the total solar eclipse was 8 Apr 2024, ≈ 2.4 years prior — kept as heard, minor imprecision). **00:18:43** — Karol Wojtyła described as belonging to personalism "in a different area of the world" from Marcel (correct: Poland vs France). **00:09:51** — "December of 2008... 19 years old... ordained 2017" — biographical timeline internally consistent (Trinity Sunday decision summer 2009).

## 4. Proper nouns checked

Confirmed via ASR probabilities (>0.5 unless noted) and context/verified sources: Father Peter Gruber; Oratory of St. Philip Neri (Neri p=0.511 — kept); University of Pittsburgh; Carnegie Mellon (Carnegie p=0.389 — context-confirmed via "Pitt, CMU"); Chatham; Dr. Sanchez / David Sanchez (David p=0.731); PJ; Brother Peter; Franciscan (youth conference, university); AP; MySpace; Tom; the Imitation of Christ; Uncle Mark (Mark p=0.999); Trinity Sunday; Pentecost; December of 2008; electrical engineering; Pitt; CMU; Arthur Conan Doyle; Sherlock Holmes; Eastern Pennsylvania; Elizabeth (p=0.446 at 00:15:19 — context-confirmed by repeated direct address); Mary Margaret; parallax; Gabriel Marcel (Marcel p=0.893); **Karol Wojtyła** (corrected from "Carol Ortiz"; Ortiz p=0.449 — see Q8); qubit; capital-B Being; St. John Henry Newman (Newman p=0.651); Oratorian (p=0.883); St. Thérèse of Lisieux (corrected from "Liszt", p=0.731); St. Augustine; St. John of the Cross; Second Vatican Council; G.K. Chesterton; St. Francis; Franciscan spirituality; The Soul of the Apostolate; TikTok; Instagram; Instagram Reels; YouTube Shorts; Circe (p=0.986); Odysseus' (p=0.999); Odyssey; Pope Benedict (Benedict p=0.979); Advent; **Max Weber** (reconstructed from "what may be" — see Q1).

Note: "Ratzinger", "Rublev", "St. Patrick", "Elizabeth of the Trinity", "Code of Canon Law" — all present in the DOCX source list — do **not** appear in E01 audio. "Pope Benedict XVI" appears once (as "Pope Benedict", 00:41:37).

## 5. Placement evidence (prologue vs epilogue decision)

- **(a) Prior knowledge assumed?** None. The talk introduces everything from scratch: it defines "mystery" against the Sherlock Holmes connotation (00:12:23-00:13:13), introduces the Trinity via "so much to understand... overwhelms our ability to think" (00:21:13), explains the sacraments, baptism, and the baptismal formula (00:24:50-00:25:45), and even glosses "Trinity Sunday — that's the Sunday after Pentecost" (00:09:30). Nothing requires C01-C06. It is self-contained.
- **(b) References to the six conferences or their themes?** No conference is mentioned by name or number. The single internal cross-reference is "you can see when we get to the section on mystery why the Trinity matters so much" (00:10:46) — a section *of this same talk*, not the retreat. Thematically, however, E01 is a compressed tour of the retreat's territory: mystery (C02), gift and liturgy (C03: law of the gift, liturgy, Offertory/Communion), intimacy (C05: intimus, silence, inner room), with evangelization-adjacent material (dissipation, screens, "made for greatness"). The talk's own frame: "structured around the themes of mystery and interiority" (00:00:42-47).
- **(c) Structure.** Opening self-introduction (Oratory, ordination 2017, campus ministry Pitt/CMU/Chatham, Dr. Sanchez, 00:00:02) → opening prayer + theme verse Rom 12:2 (00:00:52-00:01:53) → autobiographical "engineering worldview" (00:01:54-00:11:30: optimization, Pitt, vocation story, Uncle Mark, Trinity Sunday decision, switch to philosophy) → definition of Christian mystery: problem vs mystery, sun/eclipse, moon story, Gabriel Marcel, quantum physics (00:12:23-00:20:20) → God and Trinity as mystery; creation as excess of God's love; marriage/motherhood/fatherhood/friendship/loneliness (00:20:25-00:23:32) → invisible world (Newman) and sacraments (00:23:32-00:26:04) → intimacy: Thérèse, John of the Cross, inner room, intimus, Augustine (00:26:04-00:30:57) → God's initiative (1 John 4:10) and the reward-system critique (00:30:57-00:31:57) → enchanted world, liturgy, feedback loops, law of the gift, Vatican II, widow's mite, Chesterton, poverty (00:31:57-00:39:47) → dissipation vs recollection: Soul of the Apostolate, the "feed", Circe, Benedict XVI "made for greatness", screens and veils (00:39:47-00:42:37) → watching for the Christ already within (Newman, 00:42:37-00:45:34) → invitation (Mt 11:28) and closing prayers (00:45:34-00:46:02).
- **(d) Self-references.** "So my talk today is going to be on the interior life..." (00:00:42) — a standalone *talk*, never "this retreat" or "the conferences". "You heard from Dr. Sanchez earlier" (00:00:19) — an earlier speaker at the same engineering event, not the retreat. "here at Franciscan" / "Franciscan" addressed to the audience at least six times (00:04:00, 00:05:22, 00:28:28, 00:33:37, 00:35:52, 00:39:15) — the audience is Franciscan University of Steubenville engineering students, a different venue/audience from the March 2025 six-conference retreat. Recording made Sept 2026 (source mtime), ≈ 18 months after the retreat.
- **Implication for the owner's decision (evidence only, no recommendation forced):** the talk is self-contained and audience-specific. As a PROLOGUE it works because it introduces mystery from scratch, tells the author's own vocation story, and opens with Rom 12:2 "be transformed by the renewal of your mind" — a book-opening theme. Against prologue: its repeated second-person address to engineers ("you guys", "here at Franciscan") presupposes that audience. As an EPILOGUE/appendix it reads as a personal coda. The "section on mystery" cross-reference (00:10:46) is internal to E01 and would need an editorial note if E01 is placed at the front of the book.

## 6. Open questions for the human listener

1. **00:31:57** — "what Max Weber, a 19th-century German philosopher, called": confirm the name. ASR: "what may be" (what p=0.994, may p=0.719, be p=1.000). Grammar demands a name; "enchanted world" = Weber's disenchantment thesis. **Highest-priority listen.**
2. **00:11:30** — "I work in chemistry [possibly: campus ministry]": confirm. chemistry p=0.284; opening sentence says "we serve the campus ministry." **RESOLVED (owner 2026-09-16, listening): "campus ministry" confirmed; `[possibly: campus ministry]` flag removed from the clean layer.**
3. **00:28:51-00:28:59** — "Intimacy. In. Interior. Comparative. Superlative: intimus.": confirm the spoken sequence. ASR: "Intimacy. Intimos. In. In. Comparative. Superlative. of intimus." (2nd "In." p=0.005 → rendered "Interior.").
4. **00:28:44** — "Okay, so I'm going to — I've said anything, so I'm sorry.": confirm wording ("I've said enough"? "I'm going to say something"?).
5. **00:29:26-00:29:35** — Augustine quotation: confirm exact words spoken. Rendered against Confessions X.27/I.1 ("Late have I loved you, Beauty ever ancient, ever new — late have I loved you!"); confirm whether speaker said "O Beauty", and "for yourself" vs heard "yourselves" (p=0.993).
6. **00:10:01** — "I've been doing Mass every day": confirm "doing" (p=0.889) vs "going to".
7. **00:09:26** — "You are to — not this summer, but the summer after": confirm. ASR: "you after" (after p=0.974).
8. **00:18:43** — "Karol Wojtyła": confirm name. ASR: "Carol Ortiz" (Ortiz p=0.449) + trailing "one." (p=0.054). **RESOLVED (owner 2026-09-16, listening): "Karol Wojtyła" confirmed as printed.**
9. **00:34:46** — "in the Offertory, we give ourselves over to him in Holy Communion": confirm. ASR: "in the offer to our enemy," (enemy, p=0.172). **RESOLVED (owner 2026-09-16, listening): "Offertory" confirmed; prose already reads "in the Offertory, we give ourselves over…" in all layers.**
10. **00:33:01** — "an egon [possibly: icon] yet to be transformed": confirm the word (icon? eon? egon p=0.311).
11. **00:07:19** — "Franciscan youth conference": confirm (ASR "Fred Sisson", Fred p=0.280). **RESOLVED (owner 2026-09-16, listening): "Franciscan youth conference" confirmed as printed; no text change.**
12. **00:32:16** — "not near [possibly: mere] magic": confirm word. **RESOLVED (owner, batch 3, 2026-09-16): "mere" — flag removed in clean + drafts/reviewed.**
13. **00:05:28** — "They saw you out and said": confirm "saw you out" (saw p=0.989) vs "sought you out".
14. **00:37:20** — "too much courage is foolhardiness — in the midst of excess": confirm the trailing phrase; ASR "full heartedness in the midst of excess" is a split-word mis-hearing of "foolhardiness" but the tail clause is uncertain.
15. **00:35:16** — "to stay at a constant speed": confirm (ASR "to stay out of constant speed", out p=0.974).
16. **00:25:40** — "over the threefold invocation": confirm "over" (p=0.740) vs "at"/"with".
17. **00:24:21** — "St. John Henry Newman — when he was a child": confirm; ASR had "and when he was a child" (and p=0.507, dropped).
18. **00:14:17** — "so it should have been fun": confirm "fun" (p=0.937) vs "fine".
19. **00:15:19** — "any difference in the angle": confirm "in" (ASR "and", p=0.893).
20. **00:16:38** — "Had the moon any care for little four-year-old Elizabeth?": confirm question inversion.
21. **00:29:21** — "But as everyone [possibly: at last], he looked into his heart": confirm. **RESOLVED (owner, batch 3, 2026-09-16): "at last" — flag removed in clean + drafts/reviewed.**
22. **00:08:17** — "the regressing [possibly: the resting]": confirm word.
23. **00:31:03** — "Phrasing that part of the engineering worldview is that we've got to work": confirm the opening word ("Phrasing" p=0.739; candidates: "For instance, part of...").
24. **00:42:16** — "The abstract veils — they clothe mystery...": confirm "the abstract veils" (abstract p=0.979); the clause reads like he may mean the veils clothe mystery while screens block it — confirm the spoken contrast.
25. **00:45:34** — "are heavily burdened": confirm (ASR "heavy burdened", heavy p=0.998).
26. **00:12:16** — "a son or daughter of God the Father": confirm (ASR "God's Father", God's p=0.857).
27. **00:02:22** — "I was very much of the engineering worldview.": confirm what follows the period (ASR fragment "of you." p=0.215/0.694 removed; possibly the start of a clause the clean layer dropped).
28. **00:46:02-00:46:06** — closing "Thank you, everyone.": confirm complete; transcript ends 00:46:02 vs media duration 2766s (46:06) — gap ≈ 4s, within tolerance.
29. **00:13:39** — "the eclipse we had a year and a half ago": for the author, not a transcription item — recording Sept 2026 vs total eclipse 8 Apr 2024 (~2.4 years prior). Kept as heard.
30. **00:28:15** — etymology "intimus = superlative, 'the most in'": for the theological/etymological reviewer (like C01's amen/tent-peg note); the debunking of "into me see" is correct.

## 7. Compliance notes

- Raw transcript and ASR JSON untouched; clean and editorial layers are new files.
- No invented theology, transitions, or citations; every edit above traces to a listed item. Reconstructions (items 9, 18, 25, 29, 33, 52 in §1) are all flagged in §6 for human listen.
- All six [possibly] flags carry the raw word plus a bracketed guess; nothing substituted silently.
- No quotation in the clean layer was forced to match a source except the Augustine line (§1/25), which follows the established C01 practice of correcting against source wording where the ASR is clearly garbled; it remains open (Q5) and the ledger entry is a Prompt E task.
- Status of this file: **pending human transcript sign-off** (handoff G2). Inventory row updated with transcript_path/reviewer/reviewed_at only; status remains INVENTORIED until a named human reviews.
- Placement evidence for the owner's prologue/epilogue decision is in §5; final disposition (handoff Appendix C) is an ownership decision, not made here.

## 8. Owner resolutions 2026-09-16 (listening)

Recorded 2026-09-16 after the owner listened to the audio. Applied to the clean transcript, the chapter draft/reviewed copies, and this log.

1. **Q2 (00:11:30) — "campus ministry" confirmed.** The `[possibly: campus ministry]` flag is removed from the clean transcript ("I work in campus ministry to give back to the students at Pitt, CMU, and Chatham."). The chapter layers already print "campus ministry".
2. **Q8 (00:18:43) — "Karol Wojtyła" confirmed.** Already printed without a flag in all layers; no `[possibly]` flag existed on it. Confirmation recorded.
3. **Q9 (00:34:46) — "Offertory" confirmed.** The prose already reads "in the Offertory, we give ourselves over…" in all layers; no change needed. Confirmation recorded.
4. **Q11 (00:07:19) — "Franciscan youth conference" confirmed as printed.** No text change; confirmation recorded.

**Not in this batch:** Q6 (00:10:01, "doing Mass" vs "going to Mass") remains open.

## 9. Owner resolutions 2026-09-16 (batch 3)

Recorded 2026-09-16 after the owner's batch-3 resolutions. Applied to the clean transcript, the chapter draft/reviewed copies, and this log.

1. **Q21 (00:29:21) — "as everyone [possibly: at last]" → "at last".** "But at last, he looked into his heart, and he found God there." Flag removed from the clean transcript and both chapter copies. Annotated inline at §2 (flags row 3) and §6 Q21.
2. **Q12 (00:32:16) — "near [possibly: mere]" → "mere".** "When we live in this way as Christians — not mere magic, but the love of God…" Flag removed from the clean transcript and both chapter copies. Annotated inline at §2 (flags row 4) and §6 Q12.
3. **Flags row 6 (00:39:37) — "to [possibly: of]" → "of".** "…won't deprive you of what you're meant to have, of what you're meant to be." Flag removed from the clean transcript and both chapter copies. Annotated inline at §2 (flags row 6).
4. **Augustine quotation — Pusey translation adopted (owner decision A, print layer only).** The epilogue's Confessions quotation is reprinted in E. B. Pusey's public-domain translation, verbatim from newadvent.org (fathers/110110.htm, 110101.htm): "Too late did I love You, O Fairness, so ancient, and yet so new! Too late did I love You! You have made us for Yourself, and our hearts are restless until they rest in You." The clean transcript keeps the heard wording. Ledger rows SRC-025/SRC-026 and unresolved.md item 17 updated (RESOLVED — public domain).
