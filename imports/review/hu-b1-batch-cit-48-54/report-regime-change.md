# Report, hu b1 Unit 54 regime-change

Commands run: check-content (12 ERRORs: 10 length-giveaway, 2 tell-absolute; 6 vocab-unused), render_lesson, audit-reader-coverage (6 stems), unmet-words (about 80 hits, many fragments of glued blanks). Fixes in `fixes-regime-change.json` (129), challenges in `challenges-regime-change.json` (6), facts in `facts-regime-change.md`.

## 1. Found by reading
Stories (fixes on the segment files only):
- 01 "feltartóztathatatlan hulláma" is a -hatatlan form (Unit 59) and teleological; "a magyar értelmiség színe-java" and "Magyarország a vérontás nélküli forradalom példájává vált a világban" are judgements. "Antall József ellenzéki vezető" (and the character line "az Ellenzéki Kerekasztal vezető tárgyalója") puts invented words in a real person's mouth and gives him a role he did not have (check). The National Roundtable had three sides, and the 1989 agreement was not signed by the SZDSZ and Fidesz: the old text said "megegyeztek" without that (now one line). Summary: "eight" parties (the EKA had nine founding organisations, check), "patriotic writers and dissidents".
- 02 the Horn-Mock wire-cutting was on 27 June, not "tavaszán"; "több tízezer ... Budapestre" (most came to Hungary generally); "Kozma Imre atya Máltai Szeretetszolgálatánál" (the Hungarian Maltese Charity Service); "áttörték a kaput" (about 600 crossed at the Picnic); "Ez a bátor döntés döntötte le az első dominót" is praise and a disputed causal claim (now "Sok történész szerint ... hozzájárult"); the summary mixes 10 and 11 September, "tearing the first brick" and "uniting Europe".
- 03 "fenséges és mély csend", "szavai villámként járták be az országot" (praise of a present-day politician), "a kádárizmus erkölcsileg összeomlott ... tiszta örökség" (political judgement), "Háromszázezer" as a plain number (now an estimate). Summary "moral funeral of the communist system".
- 04 "A Parlament homlokzatáról már korábban levették a vörös csillagot" is false (the star came off in July 1990); "százezres" crowd (unverified); "zúgtak a harangok" unverified; "könnyeikkel küszködve" is a -ve participle (Unit 57); "lőttek ránk a gyilkosok" is an accusation (now the plain fact); "megszűnt az egypártrendszer ... kitűzték az első szabad választások időpontját" (the multi-party system was legal since early 1989; the date was not set by the amendment).
- 05 "nyerte meg" / "decisive victory" (the MDF got the most seats, about 42 percent); "negyvenöt év" now stated as "1945 óta először" with the two round dates; "a határokon túli testvéreinket is beleértve" is not in Antall's sentence as far as I know (check) and is now a separate hedged line; "Göncz ... első elnöke" (he was the first President after 1990, not the first of any republic); "A békés rendszerváltoztatás befejeződött: ... teljes nemzeti függetlenségét és szuverenitását" is a judgement; summary "center-right", "third Republic".
- Grammar screen 01 teaches *megállapodnak abban, hogy*, a cataphoric clause (B2, `b2-cataphoric-clauses`); also used in its example and in ex02; rewritten as a recap of *hogy* clauses (A2 Unit 11) and *hogy* + subjunctive (B1 Unit 5). Screen 02 titled "Decisive Historical Turning Points", example 1 claims the border opening "opened the way to the reunification of Germany and Europe". Screen 03 example 2 uses "megszálló szovjet csapatok" (a loaded label as the neutral word). Screen 05 examples use preverb inversion (*alakult meg* after *vezetésével*, *választotta meg* after *Göncz Árpádot*), a B2 form; also several items (*tartották meg*, *lépett hivatalba*, *dolgozták ki*), all rewritten without inversion.
- Items: every fill-blank glued a suffix to a stem (L1 ex02, ex05, ex07; L2 ex02, ex05, ex07; L3 ex02, ex05, ex07; L4 ex02, ex05, ex07; L5 ex02, ex05, ex07; consolidation ex02, ex05, ex07): whole-word blanks now. Other defects: L1 ex01/ex04/ex06 absurd wrong options (sports club, Kremlin, junta); L1 ex08 "győzelmét"; L2 ex02 and ex03 causal/symbol claims; L2 ex06 attributes "the Hungarians knocked out the first brick of the Berlin Wall" to Kohl (not in story; the saying's source is debated); L3 ex05/ex06/ex08 judgements ("döntő pillanata", "erkölcsi bukás", "visszaszerezte a büszkeségét"); L3 ex07 "demokrácia előtt" is a figurative claim; L4 ex01 "harmadik Magyar Köztársaság" (a label not in the story); L4 ex04 wrong options Kádár János and Nagy Imre (dead in 1989, absurd); L4 ex05 "népszuverenit_ás elve alapján" a definition with a glued blank; L4 ex06 asks why the date was chosen (not in the story); L4 ex07 "felszámolta az egypártrendszert" (false); L5 ex04 wrong options Kádár János and Rákosi Mátyás (absurd); L5 ex04 "első elnökévé"; L5 ex06 "mit jelentett" answer is an interpretation; consolidation ex04 "Döntő lökést adott ... leomlásához és újraegyesítéséhez" (debated claim as fact); consolidation ex08 uses "visszaállítva" (-va/-ve, Unit 57) in a question; consolidation ex07 "dolgozták ki" is preverb inversion.
- Tell/length ERRORs fixed: L1 ex01, ex04, ex06; L2 ex01, ex04, ex06 (*semmilyen*); L3 ex04, ex06; L4 ex06 (*mindig*); L5 ex06; consolidation ex04.
- Builders: all carry `english: "Build the sentence in the correct order."`; replaced by the real translation, and several sentences rewritten (L1 ex03, ex08; L2 ex03; L3 ex03, ex08; L4 ex08; L5 ex03, ex08; consolidation ex06).

## 2. Metadata
- L2 ex02 and L3 ex05 etc. keep their tags; retagged: L5 ex07 `translative-morphology` (elnökévé), consolidation ex05 `delative-rol-rel` (feltételeiről), consolidation ex07 `past-tense-indefinite` (ültek). L1 ex02 stays `hogy-jon-jen` (legyen).
- vocab-unused: L1 "Lakiteleki találkozó" renamed "Lakitelek"; L2 "európai újraegyesítés" (an overclaim: "reunification triggered by Hungarian border opening") replaced by "berlini fal"; L3 "szovjet csapatkivonás" renamed "kivonás", "mártírok rehabilitációja" renamed "mártír"; L4 "október huszonharmadika" renamed "október 23."; L5 "parlamenti demokrácia" now used in ex08.
- Unmet words added to the vocabulary file of the first lesson that uses them (6 + 7 + 5 + 8 + 1 entries). I could not run unmet-words on the fixed text, so the lists come from the original hits that remain plus my new words.
- Loaded glosses fixed: "Soviet occupation forces", "executed 1956 heroes", "center-right coalition", "the birth of the democratic opposition", "complete transformation".

## 3. Goals / checklists
- All five lessons use the same template goals ("I can understand and discuss <title> during Hungary's democratic transition", "I can use constitutional, political, and historical terminology of 1989-1990", the same citizenship line, "I can master six target vocabulary items"): lines 2-4 identical in every lesson. Rewritten lesson-specific. No lesson has a checklist section and the consolidation has no goal: added (unsure, structural).

## 4. Doubtful
- The Vadászterem as the venue of the National Roundtable plenary and the number of founding EKA organisations need a reference.
- Szűrös's, Horn's, Antall's, Göncz's and Orbán's quoted words are paraphrases or inventions; I kept them close to the record and marked them "check" in the facts file. Orbán Viktor is a present-day politician: the text now names him neutrally as a speaker for Fidesz demanding the Soviet withdrawal.
- 19 August Picnic: "mintegy hatszáz" is an estimate.
- Antall's phrase "tizenötmillió magyar" (consolidation/L5 ex06) is a quoted number; Hungary's population then was about 10 million.
- L2 grammar screen is now a phrase list (no grammar) and L4 grammar screen is left as it was (phrases; no form taught).

## 5. Dictionary
kerekasztal | kerekasztal | noun | round table; roundtable talks |
kiskun | Kiskun | noun | Kiskun (part of the county name Bács-Kiskun; a historical people, the Cumans) |
pártállam | pártállam | noun | one-party state |
sátorkertjében | sátorkert | noun | garden with a tent (here the garden in which the Lakitelek meeting was held) |
ülnünk | ül | verb | to sit |
jelzőrendszer | jelzőrendszer | noun | signal system, alarm system |
mehetünk | megy | verb | to go |
zugligeti | zugligeti | adjective | of Zugliget (a district of Budapest) |
háromszázezer | háromszázezer | numeral | three hundred thousand |
szilágyi | Szilágyi | noun | Szilágyi (surname, József Szilágyi) |
alkotmánymódosítás | alkotmánymódosítás | noun | constitutional amendment |
alapjogokat | alapjog | noun | basic right, fundamental right |
népszuverenitáson | népszuverenitás | noun | popular sovereignty |
közjogi | közjogi | adjective | constitutional-law, public-law |
rendszerváltoztatás | rendszerváltoztatás | noun | change of regime |
tizenötmillió | tizenötmillió | numeral | fifteen million |
kígyóztak | kígyózik | verb | to snake, to wind (of a queue) |
szavazókörök | szavazókör | noun | polling district, polling station |

Fix count Unit 54: 129 (26 on stories, 21 on grammar screens, 12 on lessons (goals, checklists), 46 on exercises, 24 on vocabulary files).
