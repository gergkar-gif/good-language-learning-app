# Reader B report: hu B1 Units 49, 51, 53 (change-development, work-ambition-balance, social-life-communication)

Commands run per unit: check-content (`python scripts/check-content.py hu b1 <unit slug>`; the numeric id `25` reports nothing), render_lesson, audit-reader-coverage, unmet-words. Nothing was applied: fixes are in `fixes-<slug>.json`, challenges in `challenges-<slug>.json`.

General finding for all three units: the content is generator-style. Every exercise set was written with unmet words (the unmet-words run lists 100+ hits per unit), every fill-blank is glued to a stem, every sentence-builder has the english `Build the sentence in the correct order.`, the five lessons of a unit share one `grammar` line and one set of goal lines, and the screens are phrase lists without explanation or, in Unit 53, present A1-B1 material as new. Almost every exercise was rewritten with met words (a screen's own phrases, the unit's vocabulary up to the lesson, A1-A2 words); the exercises kept unchanged are named below.


## 1. hu b1 change-development (B1 Unit 49)


### 1. Found by reading

check-content reported 12 errors: length-giveaway b1-25-01.ex01, ex04; b1-25-02.ex01, ex04; b1-25-03.ex01; b1-25-04.ex01, ex04, ex06; b1-25-05.ex01, ex04; b1-25-consolidation.ex08 (+ tell-absolute `soha` in cons.ex08); 3 suspects vocab-unused (fejlődés, érlelődés, kiteljesedés). All items are rewritten (the vocabulary words are used now).
Screens (grammar json) and lesson files:
- b1-25-01-a: presents `-ódik` verbs (A2 Unit 31), `válik` + `-vá/-vé` (A2 Unit 35) and `-ás/-és` nouns (B1 Unit 31) as new, and lists `tisztul`, `szépül` (-ul/-ül) under the `-odik/-edik/-ödik` suffixes. Fix: recap with unit numbers, then the new adjective-to-verb pattern (gazdag → gazdagodik, szép → szépül, tiszta → tisztul).
- b1-25-01-b, 02-b, 03-a, 04-a, 04-b, 05-a, 05-b: bare phrase lists, no explanation. Fix: one or two plain sentences each, with recaps (`-ó/-ő` B1 Unit 11, prefix placement A2 Unit 10, `-hoz` verbs B1 Unit 9, plural possessed A2 Unit 39, `számít` A2 Unit 33, `amely` A2 Unit 4).
- b1-25-02-a: *Fokozatosan* ('gradually') presented as new; it is A2 Unit 18 vocabulary (adverb in -an/-en, A2 Unit 19). Fix: recap.
- b1-25-03-b: *Míg korábban … mostanra viszont* presented as new; *míg* is B1 Unit 4, *viszont* B1 Unit 21 (A2 Unit 37). Fix: recap.
- Lesson `grammar` line identical in all five lessons (and 'Temporal Contrasts & Epochal Milestone Idioms' is not lesson 1's content). Fix: one line per lesson.
- Story b1-25-moricz, comprehension question 1 'Mi a történet központi konfliktusa?' is generic and duplicates question 2. Fix: 'Kit tanít Misi minden délután?' (answer in paragraph 1), correct index stays 1.
Exercises (all rewritten except where said; wrong options each break one thing, no option is a second right answer):
- b1-25-01.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *átalakulás* mean? | right: transformation
- b1-25-01.ex02: glued blank (valóság_____ + gá) and unmet tanulás: blank the whole word. Fix: A kitartó munka révén a terv végül _____ vált. → valósággá
- b1-25-01.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Ez az irányzat egyre nagyobb teret hódít.
- b1-25-01.ex04: unmet words (core unit): rewritten with met words. Fix: Q: Which word means *trend, movement*? | right: irányzat
- b1-25-01.ex05: glued blank (fejlő_____ + dés) and unmet rohamos/technológiai: blank the whole word. Fix: Gratulálok, nagy a _____: már jól beszélsz magyarul! → fejlődés
- b1-25-01.ex06: item asked for -ul/-ül verbs by naming suffixes (unmet nézeget, melegszik, vitakodik as options, and the three options were suffix lists, not forms); now a sentence choice on válik + -vá/-vé (the skill a wrong answer shows is valik-verb). Fix: Q: Which sentence says that the garden became beautiful? | right: A kert széppé vált.
- b1-25-01.ex07: glued blank (szép_____ + ült): blank the whole word. Fix: A város az utóbbi években nagyon _____. → szépült
- b1-25-01.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az utóbbi években sok változás történt a városban.
- b1-25-02.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *kibontakozás* mean? | right: blossoming
- b1-25-02.ex02: glued blank (fokozato_____ + san), unmet kapkodva/gyakorlatba. Fix: Nem sietünk, _____ tanulunk magyarul. → fokozatosan
- b1-25-02.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Lépésről lépésre jobban beszélünk magyarul.
- b1-25-02.ex04: unmet words (core unit): rewritten with met words. Fix: Q: Which word means *transition*? | right: átmenet
- b1-25-02.ex05: item was a phrase-fill with only one answer for a unit word 'képez'; now tests the vocabulary word fokozatosság (unmet words removed). Fix: A _____ azt jelenti: lépésről lépésre haladunk. → fokozatosság
- b1-25-02.ex06: options 'Egy szempillantás alatt', 'Visszafelé haladva' were unmet and plainly absurd; now the item tests the -ról … -ra pair of lépésről lépésre. Fix: Q: How do you say *step by step* in Hungarian? | right: Lépésről lépésre.
- b1-25-02.ex07: glued blank (kibontakoz_____ + ott), unmet zenei/kiváló; the item was tagged vocabulary but tests the past form. Fix: A fiatal tehetség gyorsan _____. → kibontakozott
- b1-25-02.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az új projekt nagy áttörést hozott.
- b1-25-03.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *újjászületés* mean? | right: rebirth
- b1-25-03.ex02: unmet érdeklődés/hatalmas/látogatják; ezzel szemben is a right answer of the skill (adversative-contrast). Fix: Míg régen kevés ember tanult magyarul, ma _____ sok ember tanul. → ['viszont', 'azonban', 'ezzel szemben']
- b1-25-03.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A gazdaság a válság után új lendületet kapott.
- b1-25-03.ex04: item 'Mi a hanyatlás ellentéte?' had three answers (Fejlődés, Visszaesés and Pusztulás are all opposites or near-opposites of decline; visszaesés is also unmet). Fix: Q: What does *hanyatlás* mean? | right: decline
- b1-25-03.ex05: glued blank (újjászüle_____ + tett), unmet köszönhetően/várnegyed. Fix: A történelmi városközpont a felújítások révén szinte _____. → újjászületett
- b1-25-03.ex06: options 'A múltnak köszönhetően' (unmet köszönhetően) and 'A múltban maradt' did not break one thing and were absurd; now each wrong option breaks the -val/-vel ending. Fix: Q: How do you say *in contrast to the past*? | right: A múlttal ellentétben.
- b1-25-03.ex07: glued blank (in_____ + dult), unmet kultúra/eszmék. Fix: A cég hanyatlásnak _____, de később új lendületet kapott. → indult
- b1-25-03.ex08: unmet words (core unit): rewritten with met words. Fix: builder: A megújulás új reményt hozott a közösségnek.
- b1-25-04.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *alkalmazkodás* mean? | right: adaptation
- b1-25-04.ex02: glued blank (céljai_____ + mat) hid a plural-possessed accusative; blank the whole word. Fix: Az események után teljesen átértékeltem a saját _____. → céljaimat
- b1-25-04.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Az új tapasztalatok új szemléletmódot hoznak.
- b1-25-04.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *szemléletmód* mean? | right: an outlook on life
- b1-25-04.ex05: glued blank (érlelő_____ + dése), unmet személyiség/küzdelmes. Fix: Az _____ sokáig tart, mert az ember tapasztalatot gyűjt. → érlelődés
- b1-25-04.ex06: options were absurd (Sötétben hagyja a kérdést, Kikapcsolja a villanyt) and unmet; now met phrases of the unit. Fix: Q: Which phrase means that something is seen in a new light? | right: új megvilágításba helyez
- b1-25-04.ex07: glued blank (körülmények_____ + hez), unmet piaci/körülmények. Fix: Gyorsan alkalmazkodnunk kell az új _____. → helyzethez
- b1-25-04.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Új helyzetben az alkalmazkodás nagyon fontos.
- b1-25-05.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *kiteljesedés* mean? | right: fulfilment
- b1-25-05.ex02: glued blank (számí_____ + tott), unmet technológia/döntő. Fix: A törvény elfogadása fontos mérföldkőnek _____. → számított
- b1-25-05.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A jó könyv kiállja az idő próbáját.
- b1-25-05.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *maradandóság* mean? | right: lasting quality
- b1-25-05.ex05: blank was glued to a prefix (teljesedett _____ + ki) in a sentence with unmet words; now tests the vocabulary word korszakváltás. Fix: Az internet elterjedése _____ jelentett. → korszakváltást
- b1-25-05.ex06: unmet words (core unit): rewritten with met words. Fix: Q: What does *kiállja az idő próbáját* mean? | right: it stays valuable over time
- b1-25-05.ex07: glued blank (terem_____ + tett), unmet alkotó. Fix: A művész maradandó értéket _____. → teremtett
- b1-25-05.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Egy világos irányvonal sokat segít.
- b1-25-consolidation.ex01: question and options had unmet words (minőségi, elképzelés); two wrong options 'valóságban állt'/'valóságról döntött' broke the sentence in two ways (verb and case); distractor_skills moved to the option that is a real -ban form. Fix: Q: Which sentence says that the plan became reality? | right: A terv végül valósággá vált.
- b1-25-consolidation.ex02: glued blank (megér_____ + ett), unmet jelleme/diákévek. Fix: A nehéz napok után Misiben fokozatosan _____ a felismerés. → megérett
- b1-25-consolidation.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Az események után Misi átértékelte a céljait.
- b1-25-consolidation.ex04: glued blank (érté_____ + ket), unmet tudás/emberség. Fix: A művész maradandó _____ teremt. → értéket
- b1-25-consolidation.ex05: unmet words (core unit): rewritten with met words. Fix: builder: A korszakváltás után új irányvonal kell.
- b1-25-consolidation.ex06: unmet esztétikai/homokóra/raktárában; wrong options were absurd. Fix: Q: A song *kiállja az idő próbáját*. What does that say about the song? | right: It is still valued after many years.
- b1-25-consolidation.ex07: glued blank (szerkeze_____ + tét), unmet alakította/társadalom. Fix: Misi nagyon tiszteli a _____. → szüleit
- b1-25-consolidation.ex08: question and options had unmet words (jelleme, leküzdve, megerősödik, kereskedővé, katonának); reading question now asks what Misi says in the story. Fix: Q: Mit mond Misi a tanároknak? | right: Azt mondja, hogy nem vett el semmit.

### 2. Metadata

- b1-25-01.ex06: `mediopassive-verbs-odik` on an item that asked for suffix lists; now a sentence choice on válik + -vá/-vé: `teaches` valik-verb, `distractor_skills` {2: ban-ben-in} (szépben is a real -ben form).
- b1-25-02.ex05: grammar `past-tense-indefinite` → now the vocabulary word fokozatosság: `teaches` b1-change-development-vocab, `category` vocabulary. b1-25-02.ex07: was vocabulary (képez) → now the past form kibontakozott: `teaches` past-tense-indefinite, `category` grammar.
- b1-25-02.ex06: vocabulary → `teaches` delative-rol-rel, `category` grammar (the pair lépésről … lépésre). (unsure: ra-re would also do)
- b1-25-03.ex06: vocabulary → `teaches` val-vel, `category` grammar, `distractor_skills` {1: on-en-on}.
- b1-25-03.ex02: `answers` now also takes `ezzel szemben` (the third connector of adversative-contrast).
- b1-25-05.ex05: stays vocabulary (korszakváltást). b1-25-consolidation.ex01: `distractor_skills` {1: ban-ben-in, 2: delative-rol-rel} sat on options that broke the sentence in two ways; now {0: ban-ben-in} on 'valóságban'.
- After these tag changes: `python scripts/lock_tags.py hu b1/change-development --update --reason "..."` (reviewer).

### 3. Goals / checklists

- All five lessons had the same lines 2-4 ('I can describe gradual growth, transformations, and contrasting eras in Hungarian.', 'I can express maturation, personal change, adaptation, and enduring historical legacies.', 'I can master four new target vocabulary items in authentic context.') and a vacuous line 1 ('I can understand and use vocabulary for change and shifts.'). Fix: three lines per lesson, each practised in the lesson's items, in the lesson file (`goal` and the goal section's `items`); line 1 is the communicative one and is the challenge's canDo. The consolidation lesson has no goal lines (as in the frozen units).
- curriculum.json also carries the old goals; it is generated by build-manifest.py (not edited).

### 4. Doubtful

- b1-25-04-b example 'A túlélés kulcsa a megváltozott helyzethez való gyors alkalmazkodás.' (and its speaking step): *helyzethez való* is a participle of van, not taught anywhere before B1 Unit 53+. Not fixed. (unsure)
- Story b1-25-moricz uses *hirdetve* (-va/-ve, B1 Unit 57), *legyőzhetetlen* (-hetetlen, B1 Unit 59) and *olthatatlan*. Stories are exempt from met words; noted only. (unsure)
- Story: the last paragraph's first line has Misi say 'Már nem sírok a sarokban', which the narration never showed. Noted. (unsure)
- Vocabulary lists re-list known words (tapasztalat A2 Unit 27); parked, not reported.
- The `-odik/-edik/-ödik` vs `-ódik` wording on 25-01-a: *fejlődik* (long ő) is no longer listed under the short-vowel suffixes. (unsure about the exact A2 Unit 31 wording)
- The recaps name units as '(A2 Unit 35)' without 'from'; run check_unit_refs.py.

### 5. Dictionary

aláz | aláz | verb | humiliate, disgrace |
diákbarakkban | diákbarakk | noun | students' barracks (boys' dormitory hut) |
fojtogatták | fojtogat | verb | choke, strangle |
mélységes | mélységes | adj | profound, deep |
olthatatlan | olthatatlan | adj | unquenchable |
önzéssel | önzés | noun | selfishness |
palástos | palástos | adj | wearing a cloak, cloaked |
reskontó | reskontó | noun | lottery ticket (old word) |
reskontóval | reskontó | noun | lottery ticket (old word) |
sorsjátékon | sorsjáték | noun | lottery, game of chance |
tölgyfakapuján | tölgyfakapu | noun | oak gate |
vékonyka | vékonyka | adj | slender, rather thin |
lutriszelvény | lutriszelvény | noun | lottery ticket |
(doroghy: a name)

Fix count change-development: 79 (48 exercises, 10 goal blocks, 10 screens, 5 lesson grammar lines, 6 story-question strings). Challenges: 6.

## 2. hu b1 work-ambition-balance (B1 Unit 51)


### 1. Found by reading

check-content reported 12 errors: length-giveaway b1-26-01.ex04; 26-02.ex04; 26-03.ex01 (+ tell-absolute `soha`), ex04; 26-04.ex01, ex04; 26-05.ex01 (+ tell `Kizárólag`), ex04; cons.ex06, ex08. Suspects: glued-blank b1-26-05.ex02 (munka____ + ban); vocab-unused karrier, pályafutás (26-01), rugalmasság (26-03). All rewritten; every vocabulary word is used now.
- Screens b1-26-01-a … 05-b: bare phrase lists with no explanation; fixed with plain-language notes and recaps (-nak/-nek A2 Unit 12, -ként A2 Unit 36, -ra/-re B1 Unit 3, szabad A2 Unit 23, -ba/-be A1 Unit 12, -ban/-ben B1 Unit 21, részesül B1 Unit 33, -ó/-ő B1 Unit 11, -hoz B1 Unit 9, reflexive A2 Unit 17).
- b1-26-05-b example 'A nehézségek ellenére mindvégig hű maradt …': the postposition *ellenére* is `concessive-postpositions`, B1 Unit 57 (taught later). Fix: 'Bár nehéz volt, mindvégig hű maradt a becsületéhez és a hivatásához.' (*bár* B1 Unit 9) and its english line; the speaking step follows.
- Lesson `grammar` line identical in all five lessons. Fix: one line per lesson.
- Story b1-26-kosztolanyi, comprehension question 1 'Mi a történet legfontosabb központi üzenete?' is generic. Fix: 'Mit mond Moviszter doktor Vizynének Annáról?' (answer index 2, in the story's third dialogue).
- Story: the last paragraph is author commentary ('Kosztolányi halhatatlan regénye … maradt'), not narration of the scene. Noted. (unsure)
Exercises (b1-26-02.ex06 and b1-26-03.ex06 are kept: met words, one fault per wrong option):
- b1-26-01.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *hivatás* mean? | right: a calling
- b1-26-01.ex02: glued blank (hivatásá_____ + nak) and unmet gyermekek/nevelését. Fix: A tanár a munkáját _____ tekinti. → hivatásának
- b1-26-01.ex03: english said 'Build the sentence in the correct order.' and did not fit the sentence. Fix: builder: A mérnök kiváló szakértelemmel tervezte meg az új házat.
- b1-26-01.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *szakértelem* mean? | right: professional skill
- b1-26-01.ex05: glued blank (pálya_____ + futás), unmet sebészorvos. Fix: Hosszú és sikeres _____ áll az orvos mögött. → pályafutás
- b1-26-01.ex06: the question asked about suffix lists in Hungarian metalanguage (vonzattal) with example sentences as options; now a sentence choice with one wrong ending per option. Fix: Q: Which sentence says that Anna is well-versed in her profession? | right: Anna jártas a szakmájában.
- b1-26-01.ex07: glued blank (szente_____ + lte), unmet tudománynak. Fix: A fiatal orvos egész életét a munkájának _____. → szentelte
- b1-26-01.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az orvos karrierje sikeres volt.
- b1-26-02.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *leterheltség* mean? | right: being overburdened
- b1-26-02.ex02: glued blank (pihenés_____ + re). Fix: Fontos, hogy időt szánjunk a _____. → pihenésre
- b1-26-02.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A család a hétvégén új energiával töltődött fel.
- b1-26-02.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *kimerültség* mean? | right: exhaustion
- b1-26-02.ex05: glued blank (leterhelts_____ + ég), unmet megnövekedett. Fix: Sok a munka, nagy a _____: túl sokat dolgozunk. → leterheltség
- b1-26-02.ex07: glued blank (pihenés_____ + hez/re) accepted both hez and re for 'joga van'; now one whole-word answer with -hez. Fix: A túl sok túlóra _____ vezet. → kimerültséghez
- b1-26-02.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az egészséges ember időt szán a pihenésre.
- b1-26-03.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *egyensúly* mean? | right: balance
- b1-26-03.ex02: glued blank (élvez_____ + nek). Fix: A sürgős feladatok mindig prioritást _____ a napi beosztásban. → élveznek
- b1-26-03.ex03: english said 'Build the sentence in the correct order.' and did not fit the sentence. Fix: builder: A rugalmas munkaidő segít megteremteni a kívánt egyensúlyt.
- b1-26-03.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *időbeosztás* mean? | right: time management
- b1-26-03.ex05: glued blank (rugalmas_____ + ság). Fix: Nálunk nagy a _____: dolgozhatok otthon is. → rugalmasság
- b1-26-03.ex07: glued blank (család_____ + val), unmet összeegyeztetni (infinitive form not on the screen). Fix: Ő összeegyezteti a munkát a _____. → családdal
- b1-26-03.ex08: unmet words (core unit): rewritten with met words. Fix: builder: A sürgős munka mindig prioritást élvez.
- b1-26-04.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *ambíció* mean? | right: ambition
- b1-26-04.ex02: glued blank (előléptetés_____ + re), unmet vállalatnál. Fix: A kollégám az _____ törekszik. → előléptetésre
- b1-26-04.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A kolléga sok elismerést kapott.
- b1-26-04.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *előléptetés* mean? | right: promotion
- b1-26-04.ex05: glued blank (érvényesül_____ + és), unmet felkészülést/igényel. Fix: Az _____ sok munkát jelent. → érvényesülés
- b1-26-04.ex06: two of the three options were unmet and absurd (Kétségbe vonja a sikereket, Elhallgatja a tényeket). Fix: Q: Which phrase means *receives recognition*? | right: Elismerésben részesül.
- b1-26-04.ex07: glued blank (része_____ + sültek). Fix: Az év végén a csapat elismerésben _____. → részesült
- b1-26-04.ex08: unmet words (core unit): rewritten with met words. Fix: builder: A jó ambíció sokat segít a karrierben.
- b1-26-05.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *önmegvalósítás* mean? | right: self-fulfilment
- b1-26-05.ex02: glued blank (munka_____ + ban) is a suspect in check-content; unmet alkotó. Fix: A dolgozó örömét leli a _____. → munkában
- b1-26-05.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A kellemes munkahelyi légkör mindenkinek fontos.
- b1-26-05.ex04: unmet words (core unit): rewritten with met words. Fix: Q: What does *munkahelyi légkör* mean? | right: the mood at a workplace
- b1-26-05.ex05: glued blank (hű_____ + ség), unmet becsület/fontosabb. Fix: A hű ember mindig hű marad az értékeihez: ez a _____. → hűség
- b1-26-05.ex06: distractor_skills named the government skills; the wrong options are real -val/-ra forms, so the form skills (val-vel, ra-re) are used as in the frozen units (unsure). Fix: Q: Hogyan fejezzük ki: 'He remained faithful to his principles'? | right: Hű maradt az elveihez. (unsure)
- b1-26-05.ex07: glued blank (elégedett_____ + ség), unmet fokú/iránti. Fix: Ha jó a légkör, nagy az _____ a munkahelyen. → elégedettség
- b1-26-05.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az önmegvalósítás fontos az ember életében.
- b1-26-consolidation.ex01: unmet elhanyagolja; wrong options now stay about work and family without a tell. Fix: Q: Which phrase says that someone creates balance between work and family? | right: Megteremti az egyensúlyt a munka és a család között.
- b1-26-consolidation.ex02: glued blank (méltósá_____ + gát), unmet fáradhatatlanul/házaspár/becsülte; the story fact (Vizyné shows her flat to her guests) is in the story. Fix: Vizyné a vendégeinek mutatja a _____. → lakását
- b1-26-consolidation.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Az egyensúly sokat jelent a munkában és a családban.
- b1-26-consolidation.ex04: glued blank (kimerült_____ + séghez), unmet túlzott/hiánya. Fix: A túl sok túlóra nagy _____ okoz. → kimerültséget
- b1-26-consolidation.ex05: unmet words (core unit): rewritten with met words. Fix: builder: A kellemes légkör sokat segít a munkahelyen.
- b1-26-consolidation.ex06: unmet túlhajszolja/kerítést/téglából/felmond; wrong options were absurd. Fix: Q: What does it mean if someone *nem szab határt a munkának*? | right: He works too much and does not rest.
- b1-26-consolidation.ex07: glued blank (előléptet_____ + és), unmet szakember. Fix: Az egyik kollégám _____ kapott, mert jól dolgozik. → előléptetést
- b1-26-consolidation.ex08: question and options had unmet words (munkavállalót, gépi, költségvetési, velencei); wrong options were absurd; reading question now asks what a character says. Fix: Q: Mit mond Moviszter doktor Vizynének? | right: Azt mondja, hogy az ember nem gép: Annának elismerésre, pihenésre és meleg szóra van szüksége.

### 2. Metadata

- b1-26-01.ex06: new `distractor_skills` {0: val-vel, 2: ra-re} (the wrong options are real -val/-ra forms); `teaches` verb-government-ban-ben stays.
- b1-26-05.ex06: `distractor_skills` {1: verb-government-val-vel, 2: verb-government-ra-re} → {1: val-vel, 2: ra-re}: the frozen units name the form skills on the wrong options (b1-11-05). (unsure)
- b1-26-02.ex07: tagged verb-government-hoz-hez but `answers` [hez, re] accepted -re as well; now one answer, kimerültséghez.
- b1-26-consolidation.ex02 (acc-poss): the blank was glued to the stem; now lakását. cons.ex04, ex07 stay vocabulary.
- After these tag changes: `lock_tags.py hu b1/work-ambition-balance --update --reason "..."` (reviewer).

### 3. Goals / checklists

- All five lessons had the same lines 2-4 ('I can discuss career aspirations, professional expertise, and workloads in Hungarian.', 'I can express strategies for maintaining healthy work-life balance and preventing burnout.', 'I can master four new target vocabulary items in authentic context.') plus a vacuous line 1. Fix: three lines per lesson, line 1 communicative (the challenge's canDo).

### 4. Doubtful

- Story b1-26-kosztolanyi has *felmaródott*, *elnémított* (past participles, fine) and *áldozható* (-ható); noted only. (unsure)
- b1-26-04 and b1-26-01 lesson vocabulary re-list karrier, előléptetés, túlóra, pihenés (known, A2); parked.
- 26-01-a: *tekint a munkájára* is given with -ra/-re (B1 Unit 3 says verbs governing -ra/-re): fine; *hivatásának tekint* is a dative construction, not a verb-government skill in skills/hu.json, so the nak-nek tag on b1-26-01.ex02 is the closest. (unsure)
- cons.ex02: the new fact 'Vizyné shows her flat to her guests' is in the first paragraph of the story ('Vizyné … mutatta körbe vendégeit'). Checked.

### 5. Dictionary

barátnőit | barátnő | noun | girlfriend, female friend |
bezártságban | bezártság | noun | confinement, being shut in |
büntetlenül | büntetlenül | adv | with impunity, unpunished |
éjszakánként | éjszakánként | adv | every night, night after night |
elsorvadt | elsorvad | verb | wither away, waste away |
felgyülemlett | felgyülemlik | verb | pile up, accumulate |
felmaródott | felmaródik | verb | become eaten away, become raw (by acid) |
fensőbbséges | fensőbbséges | adj | haughty, superior |
kárpitokon | kárpit | noun | upholstery, drapery |
katonás | katonás | adj | soldierly, in strict order |
könyörületes | könyörületes | adj | merciful, compassionate |
meisseni | meisseni | adj | of Meissen (porcelain) |
nagyszalonban | nagyszalon | noun | grand drawing room |
rézkilincsek | rézkilincs | noun | brass door handle |
szótlanul | szótlanul | adv | silently, without a word |
túlterheltségben | túlterheltség | noun | being overburdened, overload |
áldozható | áldozható | adj | that can be sacrificed |
porszem | porszem | noun | speck of dust |
(annáét: a name, from Édes Anna)

Fix count work-ambition-balance: 79 (46 exercises, 10 goal blocks, 10 screens, 2 example lines, 5 lesson grammar lines, 6 story-question strings). Challenges: 6.

## 3. hu b1 social-life-communication (B1 Unit 53)


### 1. Found by reading

check-content reported 10 errors: length-giveaway b1-27-01.ex04 (+ tell `soha`), ex06; 27-02.ex01, ex06 (+ tell `Mindig` on ex04); 27-03.ex01; 27-04.ex01; cons.ex04, ex08. All rewritten.
- b1-27-01-a presents reported statements (`reported-speech-statements`, B1 Unit 25) as new; b1-27-02-a presents indirect questions (`indirect-questions`, B1 Unit 25) as new and calls *vajon* a 'polite interrogative particle' (it means 'I wonder', A2 Unit 28); b1-27-04-a presents *egymás* with all its endings as new (A2 Unit 5, B1 Unit 9; *-ért* A2 Unit 8); b1-27-05-b presents concessive clauses *bár/noha/annak ellenére, hogy* as new (B1 Unit 9; *noha* B1 Unit 20). Fix: each opens with 'You know … from <level> Unit N'.
- b1-27-03-a is the unit's new grammar (reported commands, `reported-commands`) but does not recap `hogy` + -jon/-jen (B1 Unit 5). Fix: recap, then what is new.
- b1-27-04-b example 'A fiúk közötti szilárd összetartás tette legyőzhetetlenné a közösséget.': *legyőzhetetlen* is `verbal-adjectives-hatatlan-hetetlen`, B1 Unit 59 (taught later). Fix: '… erőssé tette a közösséget.' (-vé, A2 Unit 35) and its english line.
- b1-27-01-b, 02-b, 03-b, 04-b, 05-a: formula/phrase lists with no explanation; plain notes and recaps added.
- Lesson `grammar` line identical in all five lessons. Fix: one line per lesson.
- Story b1-27-molnar, comprehension question 1 'Mi a történet fő mondanivalója Nemecsek Ernő áldozatáról?' is generic. Fix: 'Mit tesz Nemecsek, amikor Geréb elárulja a társait?' (index 0, paragraph 2).
- b1-27-04.ex07: 'A fiúk kölcsönösen segítették egymást' teaches *segít* with an accusative object; *segít* takes the dative (rulebook § 6b). Fix: támogatták egymást.
- b1-27-05.ex02: the blank 'még_____' with answer 'is' teaches the misspelling *még is* for *mégis*. Fix: whole-word blank, answer mégis.
- b1-27-03.ex05: the blank was a prefix glued to the verb ('_____bízom', hint 'prefix', tag meg-meaning). Fix: whole-word blank on the -ban of megbízik vkiben.
Exercises (b1-27-03.ex04 is kept: met words, one fault per wrong option; b1-27-04.ex06 kept):
- b1-27-01.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *összejövetel* mean? | right: a gathering
- b1-27-01.ex02: glued blank (összejövetel_____ + en). Fix: Péter azt mondta, hogy örömmel részt vesz az esti _____. → összejövetelen
- b1-27-01.ex03: english said 'Build the sentence in the correct order.' and did not fit the sentence. Fix: builder: A házigazdák meleg vendégszeretettel fogadták a meghívott vendégeket.
- b1-27-01.ex04: wrong options (A meghívást a fiókba dobjuk örömmel; Nem érkezünk meg ... soha) were absurd, had a 'soha' tell and unmet words; now each wrong option breaks the -nak/-nek of eleget tesz. Fix: Q: Which sentence politely accepts an invitation? | right: Nagy örömmel teszünk eleget a meghívásnak.
- b1-27-01.ex05: glued blank (társalg_____ + ás), unmet elmélyült/alakult; a supplied noun is vocabulary. Fix: A vacsoránál kellemes _____ volt: sokat beszéltünk. → társalgás
- b1-27-01.ex06: unmet words (core unit): rewritten with met words. Fix: Q: What does *vendégszeretet* mean? | right: hospitality
- b1-27-01.ex07: glued blank (érez_____ + te), unmet szombati. Fix: Anna azt mesélte, hogy nagyon jól _____ magát a bulin. → érezte
- b1-27-01.ex08: unmet words (core unit): rewritten with met words. Fix: builder: A házigazdák vendégszeretete nagyon kedves volt.
- b1-27-02.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *nézeteltérés* mean? | right: a disagreement
- b1-27-02.ex02: glued blank (ráér_____ + ek) with unmet ráér/egyeztetésre; tag present-tense-routine-language did not show the skill (the -e of an indirect question). Fix: Anna azt kérdezte Pétertől, hogy _____ a találkozóra. → jön-e
- b1-27-02.ex03: english said 'Build the sentence in the correct order.' and did not fit the sentence. Fix: builder: A felek hosszú tárgyalás után méltányos kompromisszumot kötöttek.
- b1-27-02.ex04: Hungarian metalanguage in the question (kötőszó, kérdőpartikulát, felkiáltójelet) and absurd wrong options (felkiáltójel, tagadó forma); now a reported question with one fault per wrong option. Fix: Q: Péter asked Anna: *Jössz a buliba?* Which sentence reports this question? | right: Péter azt kérdezte Annától, hogy jön-e a buliba.
- b1-27-02.ex05: glued blank (félreért_____ + és) with a hint naming the suffix, unmet sajnálatos/befejezése; a supplied noun is vocabulary. Fix: Egy _____ miatt késett a munka: nem értettük egymást. → félreértés
- b1-27-02.ex06: Hungarian options with unmet words (szántóföldön, dűlőúton, kiborítja); same idea in English. Fix: Q: What does *dűlőre jut* mean? | right: to reach an agreement
- b1-27-02.ex07: glued blank (tisztáz_____ + niuk). Fix: A megbeszélésen sikerült _____ a félreértést. → tisztázniuk
- b1-27-02.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Egy jó megbeszélés után nincs több nézeteltérés.
- b1-27-03.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *pletyka* mean? | right: gossip
- b1-27-03.ex02: glued blank (mond_____ + ja). Fix: Arra kértem a barátomat, hogy ne _____ el senkinek a titkot. → mondja
- b1-27-03.ex03: unmet alapköve; the screen's own example sentence is used instead. Fix: builder: A titoktartás és az őszinteség minden tartós barátság sarokköve.
- b1-27-03.ex05: the blank was a prefix glued to the verb (_____bízom, hint 'prefix') and the tag meg-meaning did not match the phrase; now a whole-word blank for the -ban/-ben of megbízik vkiben. Fix: Teljes mértékben megbízom a régi _____. → barátomban
- b1-27-03.ex06: correct option 3x longer than the others (give-away) and unmet words (kihasználja, jóhiszeműségét, betartja). Fix: Q: What does *visszaél a bizalommal* mean? | right: He abuses someone's trust.
- b1-27-03.ex07: glued blank (válaszol_____ + janak), unmet feltett. Fix: A tanár arra kérte a diákokat, hogy őszintén _____ a kérdésre. → válaszoljanak
- b1-27-03.ex08: unmet words (core unit): rewritten with met words. Fix: builder: Az őszinteség és a bizalom fontos a barátságban.
- b1-27-04.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *bajtársiasság* mean? | right: camaraderie
- b1-27-04.ex02: glued blank (egymás_____ + ért). Fix: A jó barátok mindig kiállnak _____ a nehéz időkben. → egymásért
- b1-27-04.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A közösség ereje az összetartásban van.
- b1-27-04.ex04: the old item asked for a list of case forms (Egymással, egymásért, egymás mellett) against lists of other pronouns (magammal, valakivel); now one sentence with the right case of egymás. Fix: Q: Which sentence says that the friends love each other? | right: A barátok szeretik egymást.
- b1-27-04.ex05: glued blank (marad_____ + tak) in a sentence with unmet words; the vocabulary word hűség of the lesson was never used. Fix: A _____ azt jelenti: mindvégig hű maradsz a barátaidhoz. → hűség
- b1-27-04.ex07: segítették egymást is not standard (segít takes the dative: segítettek egymásnak); glued blank (segítet_____ + ték). Fix: A fiúk kölcsönösen _____ egymást. → támogatták
- b1-27-04.ex08: unmet words (core unit): rewritten with met words. Fix: builder: A jó barátok megbíznak egymásban.
- b1-27-05.ex01: unmet words (core unit): rewritten with met words. Fix: Q: What does *empátia* mean? | right: empathy
- b1-27-05.ex02: the blank split mégis into 'még' + 'is' (taught a misspelling); now blank the whole word. Fix: Bár fáradt volt, _____ elment a találkozóra. → mégis
- b1-27-05.ex03: unmet words (core unit): rewritten with met words. Fix: builder: Egy apró figyelmesség is sokat jelent.
- b1-27-05.ex04: unmet vidáman/köszöntötte/lefeküdt; one wrong option was a correct causal sentence (a different structure, not a fault of the same kind); now each wrong option breaks the connector. Fix: Q: Which sentence says that he was tired but went to the meeting anyway? | right: Annak ellenére, hogy fáradt volt, elment a találkozóra.
- b1-27-05.ex05: glued blank (kapcsolatápol_____ + ás) with a hint naming the suffix; a supplied noun is vocabulary. Fix: A _____ fontos a barátságban. → kapcsolatápolás
- b1-27-05.ex06: unmet words (bevágás, kereszteződésben, kifizetésének) and absurd wrong options. Fix: Q: Which of these is a *kedves gesztus*? | right: A flower for a sick friend.
- b1-27-05.ex07: glued blank (grund_____ + ért), unmet grund (a word of the story, not met in a lesson). Fix: Noha Nemecsek nagyon gyenge volt, mégis kiállt a _____. → barátaiért
- b1-27-05.ex08: plural subject (A figyelmesség és az empátia) with the singular teszi is doubtful; one singular subject is clearer. Fix: builder: Az empátia szebbé teszi az életet. (unsure)
- b1-27-consolidation.ex01: unmet eljön/másnap/eljövök and a time shift (holnap/másnap) the unit never teaches; the statement now has no time word and the wrong options break the person and the type. Fix: Q: Péter said: *Nagyon fáradt vagyok.* Which sentence reports this? | right: Azt mondta, hogy nagyon fáradt.
- b1-27-consolidation.ex02: glued blank (kompromisszum_____ + ot), unmet tanácskozáson/észszerű/kössenek. Fix: Anna arra kérte Pétert, hogy ne mondja el senkinek a _____. → titkot
- b1-27-consolidation.ex03: unmet words (core unit): rewritten with met words. Fix: builder: A fiúk kiállnak egymásért a nehéz időkben.
- b1-27-consolidation.ex04: generic literary question ('How does Molnár present camaraderie') with unmet words and a wrong option that could not be tested from the story; now asks what a character says in the story (Nemecsek refuses to leave his friends). Fix: Q: Mit mond Nemecsek Áts Ferinek? | right: Azt mondja, hogy a barátaival marad.
- b1-27-consolidation.ex05: glued blank (tisztelet_____ + tel), unmet vörösingesek/adózott. Fix: Nemecsek nem megy el: a _____ marad. → barátaival
- b1-27-consolidation.ex06: unmet words (core unit): rewritten with met words. Fix: builder: Az összetartás erőssé teszi a közösséget.
- b1-27-consolidation.ex07: glued blank (csapat_____ + ot), unmet győztek/közlegény/elvesztése/borította; the possessed noun makes acc-poss the skill shown. Fix: Anna meghívta a _____ az összejövetelre. → barátját
- b1-27-consolidation.ex08: 'Mit szimbolizál a grund' is not answerable from the story and had unmet words; now asks who the main character is. Fix: Q: Ki Nemecsek Ernő a történetben? | right: Egy kis fiú a Pál utcából.

### 2. Metadata

- b1-27-01.ex04: vocabulary → `teaches` verb-government-nak-nek, `category` grammar, `distractor_skills` {1: how-the-accusative-t-works, 2: ra-re}.
- b1-27-01.ex05, 27-02.ex05, 27-05.ex05: `teaches` nominalization on a blank that supplies a noun → vocabulary (`b1-social-life-communication-vocab`, `category` vocabulary).
- b1-27-02.ex02: `present-tense-routine-language` → `indirect-questions` (the -e of an indirect question).
- b1-27-03.ex05: `meg-meaning` → `verb-government-ban-ben`.
- b1-27-04.ex05: grammar past-tense-indefinite → vocabulary (hűség, which no item of the lesson used).
- b1-27-consolidation.ex07: `how-the-accusative-t-works` → `acc-poss` (barátját).
- b1-27-05.ex04 keeps `distractor_skills` {1: mert-because}; b1-27-consolidation.ex01 keeps {2: reported-commands}, now on 'ne legyen fáradt'.
- After these tag changes: `lock_tags.py hu b1/social-life-communication --update --reason "..."` (reviewer).

### 3. Goals / checklists

- All five lessons had 'I can discuss <topic> in fluent Hungarian.' plus the same three lines ('I can report statements, questions, and requests using authentic indirect syntax.', 'I can use targeted interpersonal vocabulary for trust, empathy, and conflict resolution.', 'I can appreciate classic Hungarian cultural themes of community and sacrifice.'), none practised as written. Fix: three lines per lesson, line 1 the communicative one (the challenge's canDo). These lessons have no top-level `goal`, only the goal section's `items`.

### 4. Doubtful

- b1-27-04.ex06 (reading, stage literature) asks about Nemecsek from the novel in lesson 4, but the story only comes in the consolidation lesson. Kept. (unsure)
- Story b1-27-molnar question 3: the correct option is about three times as long as the others (a give-away). Not fixed. (unsure)
- Story uses -va/-ve (*sírva*, *tántorogva*, *félrebeszélve*; B1 Unit 57). Stories are exempt from met words; noted only. (unsure)
- Lesson titles of Unit 53 are Hungarian with an English gloss in brackets ('Társasági összejövetelek és vendégszeretet (Gatherings, …)'), Units 49 and 51 use English titles. Noted. (unsure)
- b1-27-05.ex08 now uses one singular subject (Az empátia szebbé teszi az életet): the old 'A figyelmesség és az empátia szebbé teszi' with a singular verb is acceptable but less natural. (unsure)
- cons.ex04 / ex08: both reading questions now ask what a character says or who a character is, answerable from the first and second paragraph of the story.

### 5. Dictionary

feküdt | fekszik | verb | lie, be situated |
belopózni | belopózik | verb | sneak in |
deszkapalánkokra | deszkapalánk | noun | wooden plank fence |
fahasábokkal | fahasáb | noun | log, split piece of firewood |
főhadnaggyá | főhadnagy | noun | first lieutenant |
főhadnagyok | főhadnagy | noun | first lieutenant |
fűrészporhalmokkal | fűrészporhalom | noun | pile of sawdust |
labdázóhelynek | labdázóhely | noun | place for playing ball |
lopózott | lopózik | verb | sneak, creep |
szálkás | szálkás | adj | splintery, rough |
szobácska | szobácska | noun | small room |
szülőhazáról | szülőhaza | noun | native land |
tanyázó | tanyázik | verb | camp, hang out |
zokszó | zokszó | noun | complaint, grumbling word |
emberfeletti | emberfeletti | adj | superhuman |
testalkatú | testalkatú | adj | of a certain build or physique |

Fix count social-life-communication: 74 (46 exercises, 5 goal blocks, 10 screens, 2 example lines, 5 lesson grammar lines, 6 story-question strings). Challenges: 6.

## Fix counts

- change-development: 79
- work-ambition-balance: 79
- social-life-communication: 74
