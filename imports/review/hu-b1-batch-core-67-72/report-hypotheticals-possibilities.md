# Reader A: hu b1 hypotheticals-possibilities (B1 Unit 70, b1-35-*)

Fixes: fixes-hypotheticals-possibilities.json (76 fixes). Challenges: challenges-hypotheticals-possibilities.json (6).
check-content: 7 errors (length-giveaway x5, tell-absolute x2), all fixed. unmet-words: about 90 hits, all rewritten.

## 1. Found by reading
- Lessons 01 and 03 re-teach B1 Unit 39 (`past-conditional-volna`, `kellett-volna`, "bárcsak + past conditional", "utólag") and 05-a/05-b, 02-b, 04-b present known words as new, with no "You know …": past conditional B1 U39 (01-a, 05-b), bárcsak B1 U5 and B1 U39 (01-b), past conditional + present conditional A2 U28 (02-a), különben A2 U41 (02-b), kellett volna B1 U39 (03-a), lehetett volna B1 U39 and -hat/-het A2 U23 (03-b), feltehetően B1 U30, valószínűleg B1 U41, minden bizonnyal B1 U43 (04-b), ha + conditional A2 U28 and utólag B1 U39 (05-a). Only mixed conditionals (02-a), máskülönben/ellenkező esetben (02-b), mintha … volna (04-a) and vélhetően are new. Fix: recap sentences at the start of the screen texts.
- Wrong Hungarian in screen examples (a past counterfactual with a present condition): 01-a ex.3 "…, ha elmagyarázzuk." (needs "ha elmagyaráztuk volna"), 03-b ex.1 "…, ha jobb az idő." (needs "ha jobb lett volna az idő"), 04-b ex.1 "…, ha felkészültebbek vagyunk." (needs "ha felkészültebbek voltunk volna"). They are also the speaking/example lines. Fix: corrected.
- 04-a says *mintha* takes "the conditional mood with *volna*"; every example is past tense + volna. Fix: text.
- 05-b ex.3 "Bármit tettünk volna, a dolgok természete nem változott volna meg." is a concessive indefinite (*bármi*): the B2 family `concessive-indefinites`. Fix: replaced by "Ha akkor nem szóltunk volna, a baj úgyis megtörtént volna." (unsure whether the user wants it kept).
- Every sentence-builder except 02.ex10 (01 ex03/ex07, 02 ex03/ex07, 03 ex03/ex07, 04 ex03/ex07, 05 ex03/ex07, cons ex03/ex07) has `english` = "Build the sentence in the correct order." instead of the translation. Fix: real English lines. 05.ex03 "Úgyis így történt volna minden előbb-utóbb." is not natural word order; fixed with the tiles.
- Glued or cut blanks (rulebook § 2.5): 01.ex02 *eljött_____*, 01.ex05 *té_____*, 02.ex02 *lekést_____*, 02.ex05 *köz_____*, 02.ex09 *beszél____* (four underscores), 03.ex02 *vitatkoz_____* (a non-word stem), 03.ex05 *vesz_____*, 04.ex02 *történ_____*, 04.ex05 *forgatókönyv_____*, 05.ex02 *vo_____* (cut mid-word: tokens "vo", "lt" are unmet), 05.ex05 *sorsfordí_____* (cut mid-word), cons ex02 *le_____*, cons ex05 *áll_____*. Fix: blank the whole word.
- Vocabulary items with absurd wrong options and unmet words: 01.ex04 (drawing, photograph), 02.ex04 (car wheel, book page numbering), 03.ex04, 03.ex06 (village fair), 04.ex04 (autumn leaves, financial loss), 05.ex01 (London bridge, Szeged square), 05.ex04 (heart disease, travel agency offer), 05.ex06 ("Ma este megcsinálom a feladatot", "Fejjel lefelé csinálom a munkát"), cons ex04 (court compensation, lost in the forest). Fix: B1-32-style definition items with met words and one fault per option.
- length-giveaway: 01.ex04 (55 v 36), 02.ex04 (47 v 33), 03.ex04 (43 v 26), 04.ex01 (62 v 34), 05.ex04 (54 v 39). tell-absolute: 01.ex06 *Mindig*, 04.ex06 *Teljesen*. All fixed.
- 01.ex01, 04.ex01 explain the grammar in Hungarian metalanguage (*idejű*, *igéhez*, *szócskát*, *toldalékot*, *segédigéjét*, *kötőszóval*): replaced by "which sentence" items.
- 02.ex08 repeats ex01's question word for word (adjacent-looking pair). Fix: new question line; option 0 is a real past conditional, so `distractor_skills` {"0": "past-conditional-volna"}.
- cons ex06 tests reported speech (*azt állította, hogy …*), which no lesson of this unit teaches (Units 25 and 53), and has a bracketed Hungarian scene line in the question. Fix: replaced by a mixed-conditional item.
- 04.ex06 and 03.ex07 are fine in content; only english lines needed. 03.ex01 mixes an English quote into a Hungarian question ('I should have called you'); left, no unmet words (unsure it matters).
- Reading question 05.ex01 asked for "Gubbio olasz középkori sikátoraiban" (unmet) with London and Szeged as wrong options. Fix: "Hol van Mihály a történetben?" with olasz / magyar / spanyol városban.
- Story b1-35-szerb question 2 explanation quotes words that are not in the story ("A hold ezüstös fénnyel világította meg Gubbio ősi, középkori kőfalait. Mihály lassan sétált a meredek sikátorokban."). Fix: quote the real sentence.
- Vocabulary glosses: eshetőség "…possibility" (also glosses lehetőség); választás "choice, election, option selected"; fixed.
- The story is clean for level: *mintha* comes after its screen (04-a). The characters match the book (Mihály, Tamás and Éva, Gubbio, Umbria).

## 2. Metadata
- 01.ex02: tagged `past-tense-indefinite`, but *eljöttem* is the irregular past (jött). Fix: `irregular-past` (unsure).
- 01.ex07, 02.ex05, 02.ex07, 03.ex05, 04.ex07: tagged `kell-infinitive`, `postpositions-basic`, `definite-past`, `past-tense-indefinite`, `kell-infinitive`, but they test a word (elképzelés, eltérés, fordulat, kárba veszett, kockázat). Fix: vocabulary, `b1-hypotheticals-possibilities-vocab`.
- 04.ex02: tagged `past-tense-indefinite`; the new item blanks *volna* in a *mintha* clause, tagged `mixed-conditionals`.
- 01.ex01, 01.ex06, 02.ex08, cons ex06: `distractor_skills` set where a wrong option is a real form of another skill (ha-clause, hypothetical-ha-conditional, barcsak-wish, definite-past, past-conditional-volna).
- cons ex06: was `reported-speech-statements` (off-unit); now `mixed-conditionals`.
- Doubtful: the `mixed-conditionals` skill ("mixed conditionals and mintha clauses") has `taught_in` b1-35-02-a-gr, but the *mintha* half is taught on b1-35-04-a-gr; 04.ex01/ex02 are tagged with it (unsure).

## 3. Goals / checklists
- Lessons have no `srs` / `checklist` sections (compare b1-32); the goal lines are the only checklist. `canDo` = first goal line after the fixes.
- Overclaiming or vague goals rewritten: 01 g3, g4 ("imagine alternative scenarios"); 02 g1 ("counterfactual actions"), g3, g4; 03 g2 (lehetett volna never practised), g3, g4 ("evaluate past actions constructively"); 04 g3, g4 ("analyze counterfactual scenarios in historical and personal contexts"); 05 g2 ("philosophical closure"), g3, g4 ("read and analyze … classic"); all four consolidation goals ("Review all 20 vocabulary words", "mintha … volna" not practised, "Demonstrate mastery", "Prepare for … the final B1 capstone unit").

## 4. Doubtful
- vocab-unused: elképzelés, megbánás, kárba veszett, választás are now used; nothing left unused in this unit.
- 05-b ex.3 replacement and the B2 `concessive-indefinites` family (unsure).
- Story b1-35-szerb is a literary adaptation; the plot details (bankári karrier, 15 years ago) were not checked against the novel.

## 5. Dictionary
signore | signore | noun | sir, mister (Italian form of address) |
etruszk | etruszk | adj | Etruscan |
kacérkodó | kacérkodik | verb | to flirt, to toy (with something) |
kőfaragás | kőfaragás | noun | stone carving |
kőkorlátnál | kőkorlát | noun | stone railing, stone parapet |
olajfaligetek | olajfaliget | noun | olive grove |
tornyában | torony | noun | tower |
umbriai | umbriai | adj | Umbrian, of Umbria |
(francesco, san, umbriában look like names and are left out.)

Fix count, Unit 70 hypotheticals-possibilities: 76.
