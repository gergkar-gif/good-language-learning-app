# Reader B report: hu b2 three-ts-censorship (Unit 30)

Files: fixes-three-ts-censorship.json (107 fixes), challenges-three-ts-censorship.json (6), facts-three-ts-censorship.md.

## 1. Found by reading
- Stories are weak on neutrality and facts (all on the segment files, in the fixes): S1 "teljhatalmú kultúrpápája", "Mindenki pontosan tudta" (contradicts "soha nem lehettek biztosak"), "nem nyilvánítják-e" (nem … -e), "A magyar értelmiség a legvidámabb barakkban élt" (the label is for Hungary in the bloc); S2 "elutasításra lelt" (not Hungarian), "zsarolási technika" (loaded), "Aczél … a minisztériumból" (he headed no ministry), "Amennyiben … megtagadta" (Ha), anecdotes as fact; S3 "A szovjet szót ki sem lehetett ejteni" (false), "szovjet katonai megszállás" (loaded label, S1 too), the censor in the box, "A mai napig jellemző a hazai kultúrafogyasztókra" (sweeping present-day claim); S4 "totalitárius", "ellenállhatatlan fegyver", "megelégelte/rájöttek" (mind-reading), AB founders and the 1956 "titkos dokumentumok" unverified; S5 quotation "Kádárnak mennie kell!" put into the Társadalmi szerződés from memory (paraphrased), "szinte egy időben a lengyelországi szükségállapot", Monor "kemping faházai" / "először", "a parlament és a független sajtó vezetőiként", "győzelemmel zárult".
- The segments have no `questions` array; the reading items are the lessons' ex06 (all answerable from the segments; none copies a story question).
- b2-szamizdat-01 ex02 "szocialista realizmust részesítette előnyben" (not the Kádár-era line) -> fixed. ex03 and consolidation ex06: the sentences name an overt subject (a bírálók / a tisztviselők) although the screen says the pattern drops it -> fixed; consolidation ex11 and 01 ex08 model answers likewise.
- Two right answers: 03 ex03 and consolidation ex06 (*tartották / tekintették*), consolidation ex05 (*áthallás / áthallások*) -> `answers`. 01 ex04 wrong option *tiltva vannak* is acceptable Hungarian: question made "Melyik a természetesebb?" (unsure). 03 ex01 wrong option "szomszédos termekből átszűrődő zene" is the literal meaning of *áthallás*.
- Question stems with unmet grammar jargon or English inside Hungarian: 01 ex04, 02 ex04, 03 ex04 ("dative"), 04 ex04, 05 ex04, consolidation ex01 (személyű, igealak, alannyal, segédigés, képző), ex03, ex09 -> rewritten.
- 03 ex05 "a terror éveiben" contradicts S1 (the Kádár regime left open terror) -> "a Kádár-korszakban". 05 ex05, ex07, consolidation ex08, ex10: hindsight overclaims ("megtörte", "elképzelhetetlen lett volna", "alapozta meg") -> softened. 02 ex06 / 03 ex08 / 04 ex08 / 05 ex06: overclaims or prompt/answer mismatch (épült ki vs kiépült) -> fixed.
- check-content ERRORs (10) all fixed: length-giveaway 02 ex01, ex06; 03 ex01, ex06; 04 ex01, ex06; consolidation ex01; tell-absolute 02/03/04 ex06 (Kizárólag).
- Grammar screens: L4 lists *terjed*, *alakul* under the suffix -ódik/-ődik (neither is); example *elkobzódott* is not a normal verb; L2 example adds *a vámosok által* to an agent-dropping construction; L3 calls -nak/-nek "dative/essive" (essive is -ként/-ul). Fixed.
- Lessons 1, 2, 4, 5 present B2 Unit 29's agent-backgrounding (3rd plural, *-ra/-re kerül*, -ódik verbs), plus B1 Unit 31 nominalization, as NEW ("you will master", titles "Agent Backgrounding: …"): recap wording added to the four screens and titles ("Recap: …"). L3 (evaluative predicates with *tart / tekint / tűnik*) is not a listed skill: left as the lesson's own material.
- Unmet words: 4 vocabulary appends (all hits, culture words kept) and 3 removals of vocab-unused entries (*szerkesztőségi alku*, *diplomáciai érzék*, *cenzúrázatlan* on L3, *stencilgép*), see fixes.

## 2. Metadata
- 04 ex03, ex04 and consolidation ex03 tested on -ódik verbs but tagged `agentless-constructions`: retag to `mediopassive-verbs-odik` (unsure; consolidation ex03 gets `distractor_skills` {1: causative-verbal-derivations, 2: nek-conditional}). 05 ex04, ex05 and consolidation ex10 test the verbal noun: `nominalization` (unsure). Run lock_tags if locked.

## 3. Goals / checklists
- All six first goal lines rewritten as plain can-do lines (they were "analyze / evaluate / architecture / fluent B2" templates): L1, L2, L3, L4, L5, consolidation; goal/checklist blocks in each lesson file (3 places each). L5 line 2 promised *elemzés tárgyát képezi*, which the lesson never practises -> replaced with *nyilvánosságra hozatala*. L1 and consolidation line 3 ("in fluent B2 Hungarian") rewritten.
- L1 intro: "uniquely insidious", "commissar", "you will master" -> neutral/recap wording.

## 4. Doubtful
- Unit 30's grammar: no skill is taught here ("Grammar this unit teaches" is empty); the whole unit re-drills Unit 29's `agentless-constructions` (b2-15-01 to 05) plus -ódik (A2 Unit 31) and nominalization (B1 Unit 31). Not a defect for the later skills, but the lessons are a replay of Unit 29: the reviewer may want to decide whether to keep the five-lesson shape.
- *sokszorosítódik* (L4 vocab, ex03, consolidation) is a rare/awkward middle verb (the usual forms are *sokszorosodik*, "multiplies", or *másolódik*): unsure; left (no replacement proposed).
- "szovjet megszállás": loaded label in the old goals/screens/items (L3 goal 1 still says "Soviet occupation" in English, now changed to "such as 1956" only). The Kádár-era official wording was "ideiglenesen állomásozó szovjet csapatok"; I used *szovjet csapatok jelenléte*. Decide if *megszállás* is acceptable as a historians' term.
- Story 1/2 `location` fields ("Szalay utca (Kulturális Minisztérium)", "miniszteri dolgozószoba") give Aczél a ministry: not fixed (metadata); check.
- Five consolidation-only hits (*hasáb, minisztériumi, egyeztetés, elkerül, fellépés, fontosságú*) were put on lesson 5's list because the consolidation has no list: "vocab-unused" may fire; leave or drop.
- L3 ex08 / S3 / S5: all "check" lines in facts-three-ts-censorship.md.

## 5. Dictionary
arctalan | arctalan | adjective | faceless, impersonal |
filmrendezőit | filmrendező | noun | film director |
önfeladás | önfeladás | noun | self-abandonment, giving up one's principles |
útlevélkérelme | útlevélkérelem | noun | passport application |
békemozgalmakról | békemozgalom | noun | peace movement |
faházaiban | faház | noun | wooden cabin |
jogfosztottságáról | jogfosztottság | noun | state of being deprived of rights |
közzétételre | közzététel | noun | publication, making public |
különszámaként | különszám | noun | special issue |
stencilek | stencil | noun | stencil |
szerveződő | szerveződik | verb | to organise itself, to form |
tényfeltáró | tényfeltáró | adjective | investigative, fact-finding |
szükségállapot | szükségállapot | noun | state of emergency |
antikommunista | antikommunista | adjective | anti-communist |
kultúrpápája | kultúrpápa | noun | cultural "pope" (nickname for the cultural-policy chief) |
lebegtetett | lebegtet | verb | to keep in suspense, to leave open |
papírkvótát | papírkvóta | noun | paper quota |
szegmensét | szegmens | noun | segment |
teljhatalmú | teljhatalmú | adjective | all-powerful |
kimondhatóság | kimondhatóság | noun | sayability, what may be said |
félelemmentes | félelemmentes | adjective | fearless, free of fear |
festékszag | festékszag | noun | smell of paint or ink |
szamizdathálózat | szamizdathálózat | noun | samizdat network |
szitanyomó | szitanyomó | adjective | screen-printing |
titkosrendőrség | titkosrendőrség | noun | secret police |
virágnyelv | virágnyelv | noun | flower language, coded language |
információmonopóliumot | információmonopólium | noun | information monopoly |
présházak | présház | noun | wine-press house |
ramkákat | ramka | noun | frame (for hand screen-printing) |
sokszorosítódtak | sokszorosítódik | verb | to be duplicated, to multiply |
sokszorosított | sokszorosít | verb | to duplicate, to copy in numbers |
stencileket | stencil | noun | stencil |
beszédmód | beszédmód | noun | manner of speaking |
ezópuszi | ezópuszi | adjective | Aesopian, allegorical |
helyőrségekről | helyőrség | noun | garrison |
jelenkorról | jelenkor | noun | the present age |
kultúrafogyasztókra | kultúrafogyasztó | noun | consumer of culture |
olvasat | olvasat | noun | reading, interpretation |
tabutémát | tabutéma | noun | taboo subject |
virágnyelvet | virágnyelv | noun | flower language, coded language |

Fix count: 107.
