# Unresolved items — Stage 1 (Prompt E: source ledger and verification)

Created 2026-09-16 by `pipeline-researcher`. Each entry: what is missing / uncertain and the human decision required. No entry below is a blocker for the pipeline except where noted (per handoff §6, LOCATOR_MISSING / ATTRIBUTION_UNCONFIRMED / PERMISSION_REVIEW / DOCTRINAL_REVIEW items are closed by named humans).

## A. Ratzinger, Introduction to Christianity (SRC-001, SRC-002, SRC-003) — page numbers
- **What's missing:** Exact page numbers for the Ignatius Press 2004 edition (ISBN 1586170295, 388 pp.). The DOCX claims pp. 162, 172, 175. All three quotations were confirmed verbatim in the 2004 edition's OCR text (via Open Library/Internet Archive search-inside of scan `introductiontoch0000bene_v8m7`), but no page-bearing snippet could be obtained (Google Books API quota-blocked; archive.org scan lending-restricted; its search-inside endpoint returns "Item not available").
- **Corroborating evidence:** In the 298-page printings (Herder & Herder 1969/1970; Ignatius/Communio 1990), the "trophies/graveyard" passage sits on printed page 123 (running head "BELIEF IN THE TRIUNE GOD 123") — so the claimed pages can only refer to the 2004 typesetting.
- **Human decision required:** Verify pp. 162/172/175 against a physical copy of Ignatius Press 2004 before printing page numbers; otherwise cite without page locators. Owner: theological/citation reviewer.
- **Also (SRC-003):** DOCX phrase "something of man, of what is characteristically ours" appears to conflate two printings' readings ("something of man, of our individuality," 1969/1990 vs "of what is characteristically ours," 2004). Confirm against the physical copy and pick one.
- **Rights:** All three quotes are from a copyrighted work (trans. J. R. Foster). Permission review required — status PERMISSION_REVIEW.

## B. Code of Canon Law Can. 225 §1 (SRC-005) — translation choice
- **What's missing:** The DOCX wording matches the CLSA translation, not the official vatican.va English (verified text recorded in the ledger is the Vatican English). The DOCX also contains a transcription error: "whether s individuals" (missing "a").
- **Human decision required:** Choose which translation the book cites (Vatican English vs CLSA — CLSA is © Canon Law Society of America and needs its own attribution/permission), and fix the "s individuals" typo in editorial stages (evidence field left untouched per rules). Owner: author/editor.

## C. St. Elizabeth of the Trinity prayer (SRC-011) — translation identity
- **What's missing:** The DOCX contains two renderings. The one embedded in the ¶¶199-267 range = CCC ¶260 official English (VERIFIED EXACT). The standalone version ("as still and as peaceful…", "O my Unchanging One", "wholly surrendered to Your creative Action") matches NO located published translation (checked: CCC/Kane, Dijon Carmel official site, O.Carm, Stanbrook 1914).
- **Human decision required:** Either cite the CCC ¶260 text or the official Dijon Carmel translation, or supply the source of the standalone rendering from the author. If the Kane/ICS translation is used, it is © ICS Publications (permission). Owner: author + rights reviewer.

## D. St. Patrick's Breastplate (SRC-012) — asterisk artifact
- **What's missing:** "His coming at the day of doom;*" carries an asterisk that exists only on the prayerfoundation.org web rendering (footnote: "'day of doom' is an Old English term meaning 'Day of Judgment'"); no printed hymnal has it. Text itself = Cecil Frances Alexander's 1889 translation (public domain).
- **Human decision required:** Keep the asterisk with the Prayer Foundation footnote (with attribution) or drop it. Owner: editor.

## E. Rublev "Trinity" (SRC-013) — dating and current location
- **What's missing:** Scholarly dating is disputed (c. 1410/1411 vs 1425-1427). Also, in 2023 the icon was transferred from the Tretyakov Gallery to Russian Orthodox Church custody (displayed at Cathedral of Christ the Saviour) — any statement of current location depends on publication date.
- **Human decision required:** Choose a date range for the book and decide how to state location; image reproduction needs rights/licensing. Owner: editor + rights reviewer.

## F. Scripture passages (SRC-014 … SRC-019) — exact edition confirmation
- **What's found:** All six passages are RSV-family. Psalm 42: RSV and RSV-CE are word-identical for this psalm. The DOCX consistently modernizes "thee/thou"→"you" (Ps 42; Mark 1:11) and "lo"→"behold" (Matt 17:5; Matt 28:20), with isolated substitutions: "deer" for "hart" and "my savior" for "my help" (Ps 42:1,5), "Why do I go mourning" for "Why go I mourning" (Ps 42:9), "ask" for "pray" (John 14:16), "from here" for "hence" (John 14:31).
- **What's missing:** Whether the author intends RSV, RSV-CE (1966), or RSV-2CE (Ignatius 2006) — the two John 14 readings cannot be matched to RSV/RSVCE and could reflect RSV-2CE (whose text is not freely available online for verification).
- **Human decision required:** Author confirms the edition; decide whether to print the DOCX's modernized wording (attributed as authorial) or the exact edition text (recorded in the ledger). RSV(-CE) is © NCC — attribution required; the 45-verse John 14:1-15:12 excerpt needs permission review (status PERMISSION_REVIEW). Owner: author + citation/rights reviewer.

## G. Catechism ¶¶199-267 (SRC-009) — permissions and doctrinal review
- **What's found:** Translation identity = official CCC English; spot checks ¶199, ¶234, ¶260, ¶266 exact (only Oxford-comma variants in ¶234/¶266).
- **Human decision required:** 70-paragraph excerpt — obtain publisher permission (CCC English © LEV/USCCB) and have a qualified theologian review the assembled range before publication. Owner: rights reviewer + theological reviewer.

## H. Doctrine spot-check (no blocking issues)
- All other rows verified without doctrinal problems. A final theological review of the whole ledger remains a later pipeline gate (handoff §8, human sign-offs), not a stage-1 blocker.

---

# Stage 2 additions (Prompt E Stage 2 — quotations newly detected in the reviewed transcripts; rows SRC-020…SRC-062)

Appended 2026-09-16 by `pipeline-researcher`. Each entry: what is missing / uncertain and the human decision required.

## 1. Pope Benedict XVI, "you are not made for comfort… made for greatness" (SRC-024, E01 00:41:37)
- **What's missing:** The sentence does NOT occur in the official English or German texts of the XX World Youth Day vigil (Marienfeld, 20 Aug 2005) or the 21 Aug 2005 Mass homily (also absent from the 24 Apr 2005 inauguration homily). It circulates only as an unsourced attribution (Goodreads etc.).
- **Human decision required:** Author must supply the actual source (if it exists), or the line must be dropped/recast as the speaker's own formulation. Owner: author + citation reviewer.

## 2. Fagerberg/Kavanagh "liturgy is doing the world…" (SRC-022, C03 00:08:24; E01 00:33:13)
- **What's found:** Wording verified verbatim in Fagerberg, *Theologia Prima* (2nd ed., Hillenbrand/LTP ©2004) OCR, but the printed page could not be pinned. Fagerberg himself attributes the formulation to Aidan Kavanagh, *On Liturgical Theology* (Pueblo Press, 1984) 117-18.
- **Human decision required:** (a) Check the page in a physical copy of *Theologia Prima* 2nd ed.; (b) decide how the book credits the maxim (Kavanagh via Fagerberg, or Fagerberg). Owner: citation reviewer.

## 3. Maritain "pregnant with intelligibility" (SRC-020, C02 00:04:04)
- **What's found:** Source located — *A Preface to Metaphysics: Seven Lectures on Being* (Sheed & Ward 1939, trans. of *Sept leçons sur l'être* 1934), "being is a mystery, either because it is too pregnant with intelligibility…"; printed page ≈172 (scan-index only). Not in *The Degrees of Knowledge* (checked).
- **Human decision required:** Confirm the printed page and which lecture in a physical copy before printing a locator. Owner: citation reviewer.

## 4. Chesterton "worth doing badly" (SRC-023, E01 00:37:49)
- **What's found:** Original confirmed — *What's Wrong with the World* (1910), Part IV ch. XIV, closing line: "if a thing is worth doing, it is worth doing badly" (Gutenberg #1717).
- **Human decision required:** Decide whether the book prints Chesterton's exact wording (public domain) or keeps the speaker's "worth doing poorly" paraphrase. Owner: editor.

## 5. St. Thérèse, "Everything is grace" (SRC-029, C03 00:13:49)
- **What's found:** Verified in *Novissima Verba* (1952 ed.): 5 June 1897 entry, "Everything is a grace" ("Tout est grâce").
- **Human decision required:** If a date is printed, reconcile 5 June 1897 (fetched 1952 edition) vs the commonly cited 11 June 1897 (French *Cahier jaune* was Cloudflare-blocked to the pipeline). Owner: citation reviewer.

## 6. St. Thérèse attributions in audio
- **(a) C01 00:19:13** — ASR heard "St. Teresa"; the "simple glance" prayer quote is Thérèse's (CCC ¶2558 / Story of a Soul, Ms C 25r — SRC-027). Human listen required to confirm which saint the speaker named.
- **(b) E01 00:26:12** — speaker says "in one of her letters"; the material is from the Last Conversations (*Novissima Verba*), not a letter (SRC-041). Attribution must be corrected in the book.
- **(c) C03 00:21:19** — "prayer [possibly: love] is to be poured out into another" cannot be matched to any Thérèse source (SRC-028); the heard word itself is uncertain (ASR p=0.249). Author must supply the source or recast the line as the speaker's own image (kenosis context). Owner: author + theological reviewer.

## 7. Weber "19th-century German philosopher" (SRC-030, E01 00:31:57; C03 00:14:51)
- **What's found:** The speaker inverts Weber's "disenchantment of the world" (Entzauberung der Welt — verified, *Wissenschaft als Beruf* 1919, Gerth & Mills 1946 p. 155). Weber (1864–1920) is usually classed early-20th-century sociologist; audio says "19th-century German philosopher."
- **Human decision required:** Author decides whether to keep the spoken classification or adjust in editorial stages. Owner: editor.

## 8. "Law of the gift" (SRC-038, C03 00:15:21; E01 00:35:44)
- **What's found:** The exact phrase does not occur in the vatican.va TOB audience texts; it is George Weigel's popularization of John Paul II's "sincere gift of himself" (TOB audience 20 Feb 1980; rooted in GS §24).
- **Human decision required:** Attribution strategy for the book (e.g., "the 'law of the gift,' as it is commonly called…"). Owner: author + theological reviewer.

## 9. Scripture edition confirmation (extends Stage 1 item F)
- New scripture rows SRC-046…SRC-061 are all RSV-family; Romans 12:2 heard as "this age" blends RSV with NABRE. The author's single-edition choice (RSV / RSV-CE / RSV-2CE) remains open and now covers these rows too. Owner: author.

## 10. "Bill Daniels" (SRC-034, C03 00:01:47)
- **What's found:** No Catholic author named Bill/William Daniels could be identified anywhere fetchable. ASR probability 1.0/1.0 — the audio clearly says a name like it.
- **Human decision required:** Re-listen to C03 00:01:47 and name the correct person. (Pipeline speculation for the human check ONLY — not a finding: the name may be garbled; do not assert any candidate without audio confirmation.) Owner: author/human listener.

## 11. Giussani "Everything is positive" (SRC-036, C03 00:13:47)
- **What's missing:** Exact sentence unverifiable (The Religious Sense, McGill-Queen's 1997, lending-restricted; all text-search routes blocked).
- **Human decision required:** Author supplies the source or a print-copy page, else the line is printed as the speaker's rendering, not a quotation. Owner: author + citation reviewer.

## 12. St. John of the Cross "one Word… in silence" (SRC-040, E01 00:26:47)
- **What's found:** Saying verified in "Counsels of Light and Love" (saying no. 100, p. 106, 2007 ed. OCR); numbering differs elsewhere ("Maxims on Love" no. 21; ICS K&R numbering unverified).
- **Human decision required:** Confirm the saying number against the ICS Collected Works (Kavanaugh & Rodriguez) print edition before printing a numbered citation. Owner: citation reviewer.

## 13. Augustine "I looked into my deepest wound…" (SRC-045, E01 00:30:15)
- **What's found:** Not attested in Augustine's corpus via any fetched source; likely a modern devotional paraphrase. The speaker hedges ("apparently said").
- **Human decision required:** If used, keep the speaker's hedge and label the attribution as traditional/unverified. Owner: author + theological reviewer.

## 14. Etymological claims for the theological reviewer (from review logs)
- C01 00:21:04 — "amen… derived from aman; aman means tent peg" (standard lexicons derive amen from the root 'mn; Hebrew "tent peg" is yated, Judg 4:21 — homiletic image; flag for etymological review).
- E01 00:28:15 — "intimus = superlative, 'the most in'" and the debunking of "intimacy = into me see" (the debunking is correct; Conf. III.6.11 "interior intimo meo" verified as SRC-062).
- Owner: theological/etymological reviewer.

## 15. Doctrinal notes from review logs (for the theological reviewer when chapters are drafted)
- C02 00:13:49/00:14:00 — "subsistent relation" / "missions of the Trinity" (Thomist/CCC vocabulary; cf. CCC ¶¶252-258).
- C03 00:06:34 — Immaculate Conception framed as the moment God "could find within humanity a way to respond" (Ineffabilis Deus; CCC ¶¶490-493) — orthodox-sounding, but flag for the theological reviewer.
- C03 00:06:47 — speaker calls the creation verbs "the passive tense" (grammatically loose; fiat is jussive/passive, "Let us make" is cohortative plural).
- C03 00:12:00 — "even confession, which has no physical symbol" (confession's quasi-materia — for the theological reviewer).

## 16. C05 (Intimacy) not yet reviewed
- Stage 2 task item 7 expected Thérèse quotations from C05, but no C05 review log exists yet (only C01/C02/C03/E01 are reviewed). C05's quotations will be verified when its review log is produced. Also: the "interior intimo meo" Latin phrase is not heard in the four reviewed talks (SRC-062 kept as a verified reference).
- Owner: pipeline (future stage) — no human action yet.

## 17. ICEL permission note (SRC-025, SRC-026)
- The heard Confessions quotations match the ICEL Liturgy of the Hours renderings ("O Beauty ever ancient, ever new…"; "you have made us for yourself…"). If printed as quotations, ICEL (©) permission applies; alternatively cite the public-domain Pusey translation. Owner: rights reviewer.

