# Reader A: hu b1 complex-opinions (B1 Unit 67, b1-34-*)

Fixes: fixes-complex-opinions.json (88 fixes). Challenges: challenges-complex-opinions.json (6).
check-content: 8 errors (length-giveaway x6, tell-absolute x2), all fixed below. unmet-words: 70+ hits, all rewritten.
Note for the reviewer: a multi-word italic phrase on a screen (*mindent egybevetve*, *nem állja meg a helyét*) is NOT met in later lessons (unmet-words only counts single italic words), so the consolidation items avoid them.

## 1. Found by reading
- All five grammar screens present known material as new, with no "You know …": a2 hogy/szerintem + A1 mert (01-a), részben egyetértek B1 U41 and -an/-en A2 U19 (01-b), egyrészt … másrészt B1 U7 and egyfelől … másfelől B1 U25 (02-a), viszont B1 U21 and mindazonáltal B1 U35 (02-b), bár/habár B1 U9, noha/jóllehet (03-a), ha/amennyiben A2 U13 and feltéve, hogy B1 U55 (03-b), ezzel szemben B1 U21 and cáfol B1 U25 (04-a), kétségkívül/nyilvánvalóan B1 U30 and minden bizonnyal B1 U43 (04-b), mindent összevetve/végeredményben B1 U25 and összegzésképpen B1 U41 (05-a), szerintem A2 U12 and valaki szerint B1 U41 (05-b). Fix: recap sentence at the start of each screen text.
- 03-b text: "*amennyiben… úgy…* (insofar as… then…)": amennyiben is taught as "if" (A2 U13), and no example has *úgy*; the text names *azzal a feltétellel / kikötéssel* but example 1 has *azzal a fenntartással*. Fix: text and examples rewritten (also removes the B2 anchor, see 4).
- 05-b example 1 "Meglátásom szerint a kérdés sokkal összetettebb annál, semhogy gyorsan döntsünk." uses *annál, semhogy* (C1-level) and the gloss "far more complex than to decide hastily" is not what it says. Fix: "…összetettebb, mint gondoljuk."
- b1-34-02 title "Egyrészről..., másrészről..." uses forms the lesson never teaches (it teaches egyrészt/másrészt). Fix: title.
- Every sentence-builder (01 ex03/ex07, 02 ex03/ex07, 03 ex03/ex07, 04 ex03/ex07, 05 ex03/ex07, cons ex03/ex07) has `english` = "Build the sentence in the correct order." instead of the translation. Fix: real English lines.
- Glued blanks on a stem (rulebook § 2.5): 01.ex05 *Határozott_____*, 02.ex05 *szempon_____*, 03.ex02 *még_____*, 03.ex05 *kivé_____*, 04.ex02 *mutat_____*, 04.ex05 *meggyőződés_____*, 05.ex02 *tükré_____*, cons ex02 *még_____*, cons ex05 *ellenérv_____*. Fix: blank the whole word (with the unmet words in them gone).
- Vocabulary items with absurd wrong options (a station name, a pay category, post-office parcel weights, a medicine, a court adjournment, "stand up from a chair", a tank army and a chancellor) and unmet words: 01.ex01, 02.ex04, 03.ex04, 04.ex01, 04.ex06, 05.ex01, 05.ex04, 05.ex06, cons ex01/ex04/ex06. Fix: B1-32-style definition items with met words and one fault per option.
- length-giveaway: 01.ex01 (62 v 36), 04.ex01 (47 v 35), 04.ex04 (29 v 15), 05.ex06 (46 v 31), cons ex01 (73 v 48), cons ex04 (66 v 40). tell-absolute: 01.ex06 *Soha*, 03.ex04 *Teljesen*. All fixed.
- 03.ex01 "Melyik kötőszó fejezi ki a megengedést a mondatban?": no sentence is shown; slash options; unmet minthogy, hacsak, feltéve. 04.ex04 and 03.ex01 also used slash-joined options. Fix: "Melyik szó jelenti ugyanazt, mint a *noha*?" etc.
- 02.ex06 and 03.ex06 put an English quote ('by contrast', 'Insofar as') in a Hungarian question. Fix: Hungarian questions.
- 05.ex06 (reading, "Kivel vív belső küzdelmet …") wrong options invent an army and a chancellor; unmet éjszakai, rémálmaiban, katonájával, kancellárjával. Fix: question about the professor's view of dreams, answerable from his line in the story (unsure).
- Story b1-34-babits uses *mintha … akarná* (skill `mixed-conditionals`, taught b1-35-02-a, Unit 70) and twice *bármilyen … is* (B2 `concessive-indefinites`): "mintha a fizikai hűvösséggel akarná elcsitítani", "bármilyen nehéz és félelmetes is a kettős lét lélektani rejtélye", "bármilyen árat kérjen is a valóság". Fix: rewritten without them (unsure: stories may be above the learner, but these are later-list forms).
- Story question 2, option 2: "Egy szegény, megalázott asztaloslegényként a rideg valóságban." contradicts the story (he lives the apprentice in his nightmares). Fix: "…a rémálmaiban."
- Vocabulary glosses: viszonylagosság "relativity, nuance, non-absoluteness" (nuance is árnyalás); "qualification" glosses árnyalás, megkötés and fenntartás; "reservation" glosses megkötés and fenntartás; "point of view" glosses álláspont and szempont; "consideration" glosses mérlegelés and szempont. Fix: distinct glosses.
- 01-a: the "anticipatory demonstrative pronoun" description (*azt gondolom*, *úgy vélem*, *amellett vagyok*) is the B2 skill `b2-cataphoric-clauses`; removed.

## 2. Metadata
- 02.ex05: tagged `how-the-accusative-t-works` but fills a noun (word meaning). Fix: category vocabulary, `b1-complex-opinions-vocab`.
- 04.ex05: tagged `val-vel`, but the item is a vocabulary fill. Fix: category vocabulary, vocab tag, `answers` removed.
- 05.ex02: tagged `ban-ben-in`, but the item tests the fixed phrase *a fentiek tükrében*. Fix: vocabulary, vocab tag.
- cons ex05: tagged `how-the-accusative-t-works`, plural nominative needed. Fix: `plural-nouns-k`.
- 02.ex06, 03.ex01, 03.ex06: `distractor_skills` added/updated where a wrong option is a real form of another skill (additive-connectors, mig-egyidejuseg, miutan-mielott).
- The unit teaches no grammar skill of its own (every grammar item is tagged with an earlier skill or the vocab skill). Fine under the frozen list; nothing to add.

## 3. Goals / checklists
- Lessons have no `srs` / `checklist` sections (compare b1-32); the goal lines are the only checklist. I used the first goal line as `canDo`.
- Overclaiming goals rewritten: 01 g1 "multi-level nested opinion clauses", g3 "master 4 core vocabulary terms", g4 "well-grounded personal opinions with confidence"; 02 g3, g4 ("fair-minded comparative assessments"); 03 g2 (azzal a fenntartással, no longer taught), g3, g4; 04 g2 ("disjuncts"), g3, g4 ("structured debate"); 05 g1, g2, g3, g4 ("read and analyze … masterpiece"); all four consolidation goals ("Review all 20 vocabulary items", "epistemic reinforcement", "Confirm mastery", "Demonstrate readiness").

## 4. Doubtful
- 03-b *azzal a fenntartással, hogy* and 04-a *az az állítás, hogy* / *azt a megállapítást, miszerint* are cataphoric anchors (`b2-cataphoric-clauses`, B2). I removed them from the screens, examples, builder and goals. If the user wants them kept at B1 the skill's level is wrong. (unsure)
- vocab-unused still reported for viszonylagosság (02) and megkötés (03) (véleménynyilvánítás and kivétel are now used). Either add an item or drop the word from the list; I did not want to pad the lesson. (unsure)
- 05.ex04, 05.ex06 wording (compromise = "both sides get something") (unsure).
- Story summary calls the scene an adaptation of Babits's novel; I could not check the plot against the book.

## 5. Dictionary
asztaloslegény | asztaloslegény | noun | journeyman carpenter, carpenter's apprentice |
asztaloslegényként | asztaloslegény | noun | journeyman carpenter, carpenter's apprentice |
bársonnyal | bársony | noun | velvet |
egybevetve | egybevet | verb | to compare, to put side by side |
felőrlöd | felőröl | verb | to grind down, to wear out |
intelligenciájú | intelligencia | noun | intelligence |
kavargó | kavarog | verb | to swirl, to churn |
felmérhetetlenül | felmérhetetlen | adj | immeasurable, incalculable |
szerteszét | szerteszét | adv | all over the place, in all directions |

Fix count, Unit 67 complex-opinions: 88.
