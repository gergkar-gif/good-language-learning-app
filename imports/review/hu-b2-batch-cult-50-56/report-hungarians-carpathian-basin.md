# Reader B report: hu b2 Unit 54 hungarians-carpathian-basin (culture track)

Commands run: check-content (2 ERRORs: tell-absolute in 01.ex08 and 02.ex08; 1 suspect: 03.ex04 answer-in-prompt), render_lesson, audit-reader-coverage for the five stories, unmet-words, check_c1_forms (0 hits). All findings are in `fixes-hungarians-carpathian-basin.json` (118 fixes), `challenges-hungarians-carpathian-basin.json` (6) and `facts-hungarians-carpathian-basin.md`.

## 1. Found by reading
Stories (fixes on the five segment files):
- 01 par.1 "Hargita, Kovászna és Maros megye vidéke" -> Székelyföld is Hargita, Kovászna and only part of Maros county: "Hargita és Kovászna megye, valamint Maros megye egy része"; "döntő többsége" -> "nagy többsége". Item 01.ex08 follows.
- 01 par.3 "A Farkas utcai református kollégium és a BBTE ... egyetemi képzést nyújt": the kollégium is a secondary school; "vitathatatlan fővárosa" is a judgement -> "egyik legfontosabb központja"; "Kolozsvári Állami Magyar Színház és Opera" -> "Színház és a Kolozsvári Magyar Opera" (check).
- 01 par.4 plural subject (székelykapuk, borvízforrások ...) with "meghatározza"; "ősi szokása" -> reworded. 01 par.5 "kihívások és környezet ... kíván" -> "kívánnak".
- 02 par.1 "Európa legnagyobb folyami szigete" stated as fact -> hedged (gyakran emlegetik). 02 par.2 two bridges "biztosít" -> "biztosítanak"; "akadálytalanul" -> "általában könnyen". 02 par.3 Raichle-palota Zsolnay claim dropped (unsure), "lenyűgöző/csodálatos" removed. 02 par.4 "ma a magyar nyelv hivatalos használata biztosított" is a present-day legal claim as settled fact -> what the laws allow (check). 02 par.5 "híd szerepet" -> "hídszerepet".
- 03 par.1 "egyértelműen bizonyítják ... drasztikusan lelassul" unattributed overclaim -> "Egyes szociológiai kutatások szerint ... lassabb". 03 par.2 "három bástya" but four institutions. 03 par.4 "rangos nemzetközi fesztiválok rendszeres díjazottai" unverifiable -> "gyakori vendégei". 03 par.5 war refuge claim removed, present status "tovább működik" (check).
- 04 par.1 "legmélyebb érzelmeket kavaró", "súlyos lelki sebeket", loaded "elszakított nemzetrészek" removed; the 2004 referendum was invalid for low turnout. 04 par.2 "történelmi fordulat", "elsöprő többség" -> neutral, effective date 1 Jan 2011 added (check). 04 par.3 "Beregszászvidékig" is not a word -> "Beregszászig"; figure hedged ("kormányzati adatok szerint ... több mint egymillió"); "mélyen átélt ... újraegyesülés" (political judgement) -> "sokak számára ... szimbolikus jelentősége". 04 par.4 "pragmatikus elfogadás", "ellen-törvény" (judgement of neighbouring states, wrong spelling) -> what the Slovak, Romanian, Serbian and Ukrainian rules say (check). 04 par.5 "új alapokra helyezte a nemzetpolitikát", "valósággá vált" -> judgement removed, attributed to those concerned.
- 05 par.2 "a Mária Valéria híd újjáépítésével megalakult Ister-Granum EGTC" wrong cause: bridge reopened 2001, Euroregion 1999, EGTC 2008 -> two separate statements (check). 05 par.3 "évszázados elszigeteltség" softened. 05 par.4 "követeli meg" with two subjects -> "követelik meg". 05 par.5 "visszafordíthatatlanul ... közös európai otthon" prediction/judgement -> "sokak szerint tartósan alakítja".
Lessons:
- b2-hatarontul-01 intro: "békediktátum" loaded label and "Szovjetunió (ma Ukrajna)" is wrong for 1920 (Kárpátalja went to Czechoslovakia) -> "trianoni békeszerződés (1920)", Czechoslovakia / Serb-Croat-Slovene Kingdom.
- Grammar 01 example 3 "vonzanák" (conditional) contradicts the screen's rule "both clauses indicative" -> "vonzzák".
- Grammar 02 (the warned mistake): "Még ha viták kísérték volna is ..., a hidat átadták" and "Még ha drága lett volna is ..., a hidat megépítették" and "... elengedhetetlen volt" put a factual main clause after a counterfactual clause; a counterfactual about the past takes volna in both clauses: fixed in text, table row, example (speaking step 2 reads it) and the tip, which also said "always pair with is" (it is optional, Unit 53) and "without is the force is weakened" (wrong).
- Grammar 03 row 3 "mindenkit segít" -> "mindenkinek segít"; "prepositional-postpositional construction" wrong; "európai diplomát" -> "elismert diplomát".
- Grammar 04: "dacára governs an allative ... annak" is wrong: annak is a dative (-nak) possessor of dacára; table and examples with judgements ("the emotional unity strengthened", "historical redress", "institution consolidated"), a claim about neighbouring states' protests, "language strictly checked / majority passed" replaced with story facts (speaking steps 1 and 2 read two of these examples).
- Grammar 05 "a conditional or subjunctive verb form" (all examples subjunctive) and "subjunctive replaces conditional" corrected; "megkérdőjelezhetetlen" judgement.
Items:
- 01.ex03 unmet faépítészet and "legszebb jelképe"; 01.ex04 and 02.ex04, 04.ex04, 05.ex04, consolidation ex02/ex08: question stems in Hungarian grammar terms (kötőszói, megengedő, partikula, névutó, kötőmód): replaced by "Melyik mondat helyes?" / "Melyik szó illik a mondatba?".
- 01.ex05 blank before the comma, stored answer "is," -> blank "...akkor _____, ha", answer "is".
- 02.ex04 two wrong options are plain grammatical concessives (second right answer) or two-fault; rebuilt. 02.ex07 third option two faults. 02.ex08 and 01.ex08 tell-absolute ERRORs fixed with plausible, equal-length options.
- 03.ex03 "színházak kinevelik ... a jövő vezetőit" not in the story -> universities, story's wording. 03.ex04 "attól" in the stem (suspect) and missing comma before "hogy"; distractor_skills added (arról, ahhoz, abban are real forms of other skills). 03.ex07 did not use the lesson grammar and had a two-fault wrong option: rebuilt on függetlenül attól, hogy.
- 04.ex03 "közjogi tagjaivá váltak" -> citizenship received on taking the oath (check). 04.ex05 dacára/ellenére are equal answers -> `answers`; old sentence judged two unnamed neighbouring states. 04.ex06 figure removed. 04.ex07 claimed Hungarian-Serbian relations "kifejezetten szorossá váltak" (present-day political claim); third option two faults. 04.ex08 absurd wrong options.
- 05.ex02 "hivatalos európai fejlesztési társulás" describes the EGTC, not a Euroregion. 05.ex04 one wrong option nonsense ("is nem"). 05.ex07 "uniós forrásokból" not in the story; third option two faults. 05.ex08 "szimbólumává vált" judgement.
- consolidation ex03 superlative question; ex05 "beregszászi és komáromi egyetemek" (Beregszász has a főiskola), "anyanyelvi diplomát"; ex09 invented "lassú döntéshozatal", "forrasztotta össze"; ex12 prompts did not pin the stored answers (only the constructions).
- Lessons' reading items do not copy story questions (the story files carry no questions); all reading answers are in the corrected segments.

## 2. Metadata
- Grammar items in lessons 03, 04, 05 and consolidation are all tagged `even-if-ha-is`, but they test other skills. Retagged (category stays `grammar`): 03.ex04-07 and cons ex05, ex10 -> `b2-cataphoric-clauses` (függetlenül attól, hogy, Unit 17); 04.ex05, ex06, ex07, cons ex08 -> `concessive-postpositions` (dacára, B1 Unit 57); 04.ex04 -> `concessive-annak-ellenere` (jóllehet; unsure, nearest concessive-connector skill); 05.ex04-06, cons ex09, ex11 -> `concessive-indefinites` (bármilyen ... is, Unit 7); 05.ex07 -> unit vocabulary (it tests a case, not bármilyen).
- distractor_skills added on 03.ex04 (1 delative-rol-rel, 2 hoz-suffix, 3 ban-ben-in) and 03.ex07 (1 delative-rol-rel).
- Lesson 01-02 items keep `even-if-ha-is` (right). lock_tags --update is needed after applying.

## 3. Goals / checklists
- 01 goal 3 "block Hungarian communities" (tömbmagyarság is compact/bloc-majority areas) rewritten; 02 line 2 "irrealis" jargon rewritten; 03 line 3 "Ferenc Rákóczi II College" -> "II. Rákóczi Ferenc College"; 04 line 3 promises passport applications, emotional ties, diplomatic complexities which no item practises; 05 line 3 promises Schengen and EU regional development, line 2 *akárhogy* (not practised); consolidation "master", "minority rights", "fluent B2" rewritten. Each is fixed in the top `goal` (lessons 01-05), the goal section and the checklist.
- First goal lines are already plain can-do lines and stay (they are the challenges' canDo).

## 4. Doubtful
- Replay of the core unit (one line): all five lessons replay Unit 53's skills (01 *még akkor is, ha*, 02 *még ha ... is / volna is* = Unit 53; 03 *függetlenül attól, hogy* = Unit 17/53; 04 *dacára* B1 Unit 57, *annak ellenére, hogy* B1 Unit 9, *jóllehet*; 05 *bármilyen ... is* Unit 7) and presented them as new: recap lines added to all five grammar screens (named units only where the sheet names them; *jóllehet* "in earlier units").
- Nothing in the "later" lists is used before its screen; no C1 formula found (check_c1_forms: 0).
- The lesson files carry `"unit": 27`, the preceding core unit's index (the same pattern in Unit 56 with 28): probably intended.
- Facts needing a reference (see facts file): Farkas utca school; Cluj theatre/opera names; Subotica Zsolnay buildings; language-use law thresholds; Selye founding year; citizenship total "more than one million" and its source/year; Slovak 2010 amendment and Ukrainian rule; EGTC dates (1999/2001/2008); Trianon "one third".
- 04.ex04 tag is unsure; 02.ex04 and cons ex02 wrong options are judgement calls (see fixes marked "sure": false).

## 5. Dictionary
székelyföld | Székelyföld | noun | Székelyföld (Szeklerland), the Székely region of eastern Transylvania |
hídváros | hídváros | noun | bridge city, a town on both sides of a river joined by bridges |
történelmileg | történelmileg | adverb | historically |
közpolitikai | közpolitikai | adjective | relating to public policy |
vízgyűjtő | vízgyűjtő | noun | catchment area, drainage basin |
bánsági | bánsági | adjective | of the Banat |
borvízforrások | borvízforrás | noun | mineral-water spring |
fafaragás | fafaragás | noun | wood carving |
néptánccsoportokat | néptánccsoport | noun | folk-dance group |
székelykapuk | székelykapu | noun | carved Székely gate |
tömbmagyarságot | tömbmagyarság | noun | compact Hungarian community (a Hungarian-majority block) |
felértékelődik | felértékelődik | verb | to gain in value or importance |
felmenőit | felmenő | noun | ancestor, forebear |
felvehesse | felvesz | verb | to take up, to acquire (citizenship); to put on |
törvénymódosítást | törvénymódosítás | noun | amendment of a law |
árvízvédelme | árvízvédelem | noun | flood protection |
eurorégiók | eurorégió | noun | Euroregion |
kerékpárutak | kerékpárút | noun | cycle path |

Fix count: 118 fixes (fixes-hungarians-carpathian-basin.json), 6 challenges.
