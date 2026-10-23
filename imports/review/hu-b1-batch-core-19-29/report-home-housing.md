# Reader A report: hu b1, batch core 19-29 (Units 19, 21, 23)

The harness refused to write `report-home-housing.md`, so this reply is the only copy of the report.

Files written in `/home/user/parlour-read-a`, each `old` quoted exactly once (checked in memory only; `check_fixes.py` and the apply script were not run):
- `fixes-home-housing.json` (159 fixes), `challenges-home-housing.json` (6)
- `fixes-cities-communities.json` (155 fixes), `challenges-cities-communities.json` (6)
- `fixes-food-lifestyle.json` (151 fixes), `challenges-food-lifestyle.json` (6)

Every id that `check-content` or `unmet-words.js` flagged has a fix. `check-content` errors: U19 21, U21 16, U23 14 plus 1 suspect. Unmet hits: U19 247 over 63 ids, U21 245 over 57 ids, U23 248 over 54 ids.

**Screens rewritten as recaps:** every grammar screen presenting known grammar as new is rewritten as a recap with examples in met words. Recap sources:
- Units 19 and 23 have one new skill and none respectively, so most of their screens are recaps.
- Unit 21 is mixed, as listed in its section.

**Unmet-word checking:** core units, so every unmet word in items, options, prompts and screens is rewritten with met words. My own met-word check was approximate. The suffix stripping can pass an unmet word, e.g. *szemben* via *szem*, so the reviewer's run is the real test.

---
## UNIT 19 home-housing (b1-10-01 .. 05, consolidation; story b1-10-edesanna)

### 1. Found by reading
- Unit 19 teaches one new skill, `formal-obligation` (b1-10-03). Lessons 1, 2, 4, 5 present known grammar as new:
  - b1-10-01-a-gr and -b-gr: translative -vá/-vé and válik/tesz ("The translative case suffix … denotes"), A2 Unit 35 (a2-171).
  - b1-10-02-gr: aki/ami/amely (A2 Unit 4) and ahol (Unit 10).
  - b1-10-04-gr: postpositions with personal endings, A2 Unit 40.
  - b1-10-05-gr: "Számomra fontos, hogy" + subjunctive, Unit 5.
  - Fix: recap screens ("You know … from A2 Unit 35"), lesson-level `grammar` lines of b1-10-02, -03, -05 reworded.
- b1-10-02 uses *amiben, amire, amelyben, amitől, amivé, ahonnan, amelyről, amibe, ahová* (`vonatkozoi-nevmas-esetei`, taught b1-11-01-b, Unit 21): 3 taught-later ERRORs. Fix: only amely/ami/amit/aki/ahol; the three items retagged.
- b1-10-03-gr teaches *jogosult*, *esetén* (not skills, unmet) and never *kénytelen*. Fix: screen = köteles + kénytelen + infinitive, recap of *kell/muszáj* (A1 Unit 24); intro-2, controlled-1/2/4, writing-2 and check-2 now test it.
- Glued blanks, whole-word blank wanted:
  - b1-10-01-practice-2 *vendégszobá____*
  - b1-10-01-writing-1 *nyaraló____*
  - b1-10-04-practice-2 *sarok____*
  - b1-10-consolidation-7 *otthon____*
  - b1-10-consolidation-9 *fal____*
  - b1-10-03-dialogue-1 *a ______-vel*
- Unmet words: the lessons are in contract and building-trade Hungarian (*korszerűsítették, áramvezetékeket, törlesztőrészletét, homlokzat, lépcsőház, hőszivattyús, napkollektorok, kamionforgalomtól, felhőkarcolóktól*). Every flagged id is rewritten.
- Length give-aways and tells, all rewritten with equal-length options:
  - b1-10-01-controlled-4, -practice-3
  - 02-practice-3 (*Kizárólag*)
  - 03-check-1, 03-controlled-4 (*soha*)
  - 04-controlled-3, 04-practice-4 (*Kizárólag*)
  - 05-controlled-2/3/4 (*kizárólag*), 05-practice-3, 05-practice-4 (*Kizárólag*), 05-reading-1, 05-reading-3
- Wrong options that are not one clear fault:
  - b1-10-01-controlled-1 *házvé* (assimilation and harmony); b1-10-01-controlled-3 *modernné válogatott* (nonsense) and *modernné tett* (a fine sentence).
  - b1-10-04-controlled-3 garbled non-sentences (*A sarok áll könyvszekrény…*).
  - b1-10-01-dialogue-1 *hozott* (absurd; now a two-option *vált/tett* item).
  - Distractors from other lessons: b1-10-01-dialogue-2, 02-dialogue-2, 03-dialogue-2, 04-dialogue-2, 05-dialogue-2 (*szerződés, főbérlő, sarok, erkély, bérlője, kauciója, parasztfelkelés*).
  - 05-dialogue-1 *széthúzó/kiváltó*.
- Hungarian grammar metalanguage in question stems: b1-10-01-controlled-1/2/4, 01-check-1/2, 02-controlled-3, 03-controlled-1, 04-controlled-1/4, consolidation-6. Fix: English stems.
- Invented or untaught facts as items, replaced by plain vocabulary:
  - b1-10-03-controlled-3 (*A kauciót az önkormányzatnak kell befizetni*), 03-practice-3
  - 04-practice-4 (*amerikai konyhás nappali*)
  - 05-controlled-4 (*A fűtést kizárólag nyáron használják Magyarországon*), 05-practice-4
- consolidation-11 previews *Légy jó mindhalálig* (Unit 21 reading) and *Egri csillagok*. Fix: options use earlier readings.
- b1-10-05-reading-1/2/3: mixed English/Hungarian stems (*az adapted Kosztolányi-részlet*) with unmet options. Fix: English question and options, answerable from the story.
- STORY b1-10-edesanna:
  - Anna says *a tetszős lakás*; *tetszős* is not a word (fix *ez a lakás*).
  - Comprehension question 1 is generic (mood of the excerpt); fix: what Mrs Vizy says to Anna, correct option stays at index 2.
  - *a várva várt* (-va) and *megilletődve* (-ve) are B1 Unit 57 forms (unsure, incidental).

### 2. Metadata
- b1-10-02-controlled-1, practice-1, writing-2 tagged `vonatkozoi-nevmas-esetei` (Unit 21 skill). Retagged with the rewrite to `relative-clauses-aki-ami-amely`, `ahol-amikor`, `relative-clauses-aki-ami-amely`.
- `category: reading` with no text and no `teaches` on non-passage items: b1-10-02-practice-4, 03-controlled-3, 05-practice-4, consolidation-10 and -12. Set to `vocabulary` + `b1-home-housing-vocab`. consolidation-11 stays `reading`.
- b1-10-03-controlled-2 `distractor_skills` `causal-postpositions` / `concessive-postpositions` (B1 Units 31, 57) on *Kár miatt/ellenére*: item replaced, now `formal-obligation` with no ds.
- b1-10-03-writing-2 (esetén) and check-2 (jogosult) were vocabulary; now `formal-obligation` (grammar).
- `distractor_skills` added where a wrong option is a real form of another skill:
  - b1-10-02-controlled-1 (2: ahol-amikor), controlled-2 (2: relative-clauses-aki-ami-amely), controlled-3 (2: ahol-amikor), check-1 (2: ahol-amikor)
  - b1-10-05-controlled-1 (1: building-the-infinitive-the-suffix-ni, *lenni*)
  - consolidation-5 (2: ahol-amikor)
- Run `lock_tags.py` after applying.

### 3. Goals / checklists
- b1-10-01 line 3 "intransitive válik with transitive tesz": jargon, reworded.
- b1-10-02 line 1 names *amiben* (Unit 21); line 3 "common condominium features" is never practised.
- b1-10-03 lines 1-3 promise negotiating and contract terms with *köteles, jogosult, esetén*; practised none.
- b1-10-04 line 3 "functional zones" is never practised.
- b1-10-05 lines 1-2 "comprehensive criteria", "energy efficiency … amenities" are never practised.
- consolidation lines 2-3: *amiben*; "navigate tenancy agreements".
- Each change is made in all three places of the lesson file (goal, goal section, checklist).

### 4. Doubtful
- b1-10-03-voc *főbérlő* "landlord, property owner" (unsure): it is the main tenant who sublets. Gloss changed to "landlord, main tenant (who rents out rooms)", fix marked unsure, with intro-1 and practice-4.
- Consolidation title "Unit 10 Consolidation" and `unit: 10` against the course's Unit 19: course-wide numbering, not changed.
- b1-10-03-controlled-2 *kénytelen / kötelező / kénytelenek*: *köteles* would also fit the bus sentence, so it is not offered.
- b1-10-01-dialogue-1 two options *vált / tett* (unsure: a native reads *tett* as a missing object).
- Lessons 1, 2, 4, 5 are now recaps only; fuller B1 lessons there would need new content.
- Story: Vizyék, Krisztinaváros and Balatonfőkajár details are the adaptation's and were not checked against the novel.

### 5. Dictionary (b1-10-edesanna)
bútorviasz | bútorviasz | noun | furniture wax |
krisztinaváros | Krisztinaváros | noun | Krisztinaváros (a district of Buda, Budapest) |
krisztinavárosi | krisztinavárosi | adj | of Krisztinaváros (the Budapest district) |
levendulaillat | levendulaillat | noun | scent of lavender |
nagypolgári | nagypolgári | adj | grand bourgeois, upper-middle-class |
aranykeretes | aranykeretes | adj | gold-framed |
bársonyfüggönyök | bársonyfüggöny | noun | velvet curtain |
bátortalanul | bátortalan | adj | timid, shy |
cselédszobát | cselédszoba | noun | maid's room |
csempés | csempés | adj | tiled |
ezüstneműk | ezüstnemű | noun | silverware |
fecsegők | fecsegő | noun | chatterbox, gossip |
félszegen | félszeg | adj | awkward, shy |
lecsendesedve | lecsendesedik | verb | to calm down, to fall quiet |
mintaszerű | mintaszerű | adj | exemplary, model |
mintaszerűvé | mintaszerű | adj | exemplary, model |
parketta | parketta | noun | parquet floor |
pedáns | pedáns | adj | meticulous, pedantic |
tanácsosné | tanácsosné | noun | wife of a councillor |
tompították | tompít | verb | to muffle, to dull |
vasággyal | vaságy | noun | iron bed |
vitrinben | vitrin | noun | display cabinet |
vizsgálódó | vizsgálódó | adj | scrutinising, inspecting |
(*tetszős* is a non-word, fixed in the story.)

---
## UNIT 21 cities-communities (b1-11-01 .. 05, consolidation; story b1-11-legyjomindhalalig)

### 1. Found by reading
- b1-11-01-a-gr: "Advanced Relative Pronouns" presents aki/ami/amely (A2 Unit 4) as new. It adds *amelyik*, taught nowhere. Fix: recap screen, *amelyik* removed.
- b1-11-01-a-gr, b-gr, practice-1 and dialogue-2: *az a / azok a / az az* + noun (not taught). Fix: examples and items without it.
- b1-11-01-b-gr is the unit's skill (case-inflected relatives): clearer wording (endings the learner knows), examples in met words (*amelyben, akinek, amiről*; *ahová* in the text).
- b1-11-02:
  - Glued blanks: practice-2 *környék____* + beli, writing-2 *hely____* + beli.
  - The screen's third example *lakótelepi* is an -i adjective, not -beli. The lesson-level `grammar` line repeats it.
  - Glosses "townsperson", "fellow villager", "local resident" are nouns for adjectives.
  - practice-5 (sentence-builder) used *lakók/alkotnak*, dropped with the screen: fix sets `tiles`, `solutions`, `english`.
- b1-11-03-gr teaches *míg, ellenben, ugyanakkor*; the unit's skill is *azonban, viszont, ezzel szemben*, and *azonban* never appears. Fix: screen = azonban/viszont/ezzel szemben (recap *míg*, Unit 4); intro-2, items and the lesson-level `grammar` line follow.
- b1-11-04: the unit teaches no new skill here, and the screen presents *érdemes* + infinitive (A2 Unit 18) and *ha teheted* (A2 Unit 23) as new. *ha teheted* is called "polite conditional phrasing"; it is not a conditional. Fix: recap screen.
- b1-11-05:
  - The new skill is verbs with -ban/-ben, but controlled-1 and consolidation-6 have the right answer *rendezvényen* (-n).
  - The screen presents *hozzájárul* + -hoz/-hez (Unit 9) and *együttműködik* + -val/-vel (A2 Unit 5) as new, next to the new group. *hozzájárul* is in no A1-B1 list (first b2-29-02).
  - practice-2 and consolidation-8 blank the detached preverb *hozzá* after *járulnak* (unmet, split verb).
  - Fix: -ban/-ben screen with *részt vesz, bízik, hisz, csalódik*; recap of the other two groups with *csatlakozik*; items on *program/munka*.
- Unmet words: 245 hits (*közvilágítás, nehézipari, katonai, laktanyákat, repülőgépgyárakat, kaszinókat, magánrepülőtereket, valutatartalékok, államhatárok, vasútvonalak, határellenőrzés, nagykövetségek*). All 57 flagged ids rewritten with met words.
- Distractors that are unmet nonsense: *vilajet, zsoldoshiány, defterdár(a), kancellária, zsoldos, szultán, tételéhez, rombolásához, eladásihoz, hadrend, kincstár, koronázás, meggyengülés, főbérlője*.
- Length give-aways and tells: b1-11-01-practice-3; 02-controlled-4 (*kizárólag*), 02-practice-3 (*senki*), 02-practice-4; 03-controlled-4 (*senki*), 03-practice-3; 04-controlled-3, 04-dialogue-2; 05-controlled-2, 05-dialogue-1, 05-practice-3 (*Semmilyen*), 05-practice-4; consolidation-12. All rewritten.
- Hungarian metalanguage in stems (*vonatkozó névmás, képző, vonzattal, kötőszó, mediopasszív*): 01-controlled-1, 01-check-2, 02-controlled-1/2/3, 03-controlled-1/2, 04-controlled-2, 05-controlled-1/2, consolidation-4/5/6/11. Replaced.
- Trivia the lessons never teach, replaced by vocabulary items:
  - b1-11-02-controlled-4 (Hungarian housing estates)
  - 04-practice-3 (which city is famous for wine, *Dunaújváros/Százhalombatta*)
  - 05-practice-3/4
  - 03-practice-4
- Two-option or absurd wrong options: 02-dialogue-1/2, 04-controlled-4, 05-practice-3/4 (*Megakadályozza a szomszédok közötti beszélgetést*, *Bezárja a közösségi tereket*).
- b1-11-05-reading-3 asks about a feeling "walking in the Debrecen streets"; the story puts it in Pósalaky's room. Reading-1/2 have unmet options (*osztrák, hegyi, várnegyedben, polgármesterhez, egri*). All rewritten, answerable from the story.
- STORY b1-11-legyjomindhalalig: Q1 is generic (central idea); fix: what Pósalaky says to Misi, correct option stays at index 1. *szorongatva* (-va) and *reménykedve* (-ve) are B1 Unit 57 forms (unsure, incidental, replaced).

### 2. Metadata
- `category: reading` with no text: b1-11-01-practice-3, 02-controlled-4, 02-practice-3, 02-practice-4, 03-practice-3, 04-practice-3, 05-practice-3, 05-practice-4, consolidation-12. Set to `vocabulary` + `b1-cities-communities-vocab`.
- b1-11-01-practice-1, check-2 and consolidation-4 tagged `relative-clauses-aki-ami-amely` (A2) while the unit's skill is the case form: retagged `vonatkozoi-nevmas-esetei`.
- b1-11-05-controlled-1 and consolidation-6 tagged `verb-government-ban-ben` with a right answer in -n: items now use *programban, munkában*.
- b1-11-05-dialogue-2 was vocabulary; now `verb-government-ban-ben` with a plausible wrong reply (`distractor_skills` 1: case-inflected-pronouns).
- b1-11-04-controlled-4: `distractor_skills` `imperative-indefinite` did not fit; now `szabad-infinitive` / `kell-infinitive`.
- Added: b1-11-01-controlled-3 (2: vonatkozoi-nevmas-esetei), b1-11-03-controlled-1 (1: mert-because, 2: hogy-clauses), controlled-2 (1: mert-because), controlled-4 (same), b1-11-05-controlled-2 (1: ban-ben-in, 2: delative-rol-rel).
- Run `lock_tags.py` after applying.

### 3. Goals / checklists
- b1-11-01: "population trends", "informal ami vs literary amely" never practised.
- b1-11-02: first line was the topic, not the grammar (-beli); "neighborhood solidarity and community cohesion" overclaim.
- b1-11-03: line 1 named míg/ellenben/ugyanakkor, not the unit's connectors; "persuasive arguments" and "urbanization" never practised.
- b1-11-04: "conditional phrasing", "hidden culinary gems" never practised.
- b1-11-05: "local government, civic associations, community hubs" never practised; the verb line named the Unit 9 and A2 verbs.
- consolidation: míg/ellenben, and the unclear "participating verb governments".
- Each change is made in all three places.

### 4. Doubtful
- b1-11-05 recap names *csatlakozik* as the Unit 9 -hoz/-hez example: the pattern is Unit 9, the verb is my pick (unsure).
- *bízik, hisz, csalódik* are A2 words (a2-161, a2-141) used as the "new" -ban/-ben group; the general pattern is B1 by the A2 chunk rule (unsure).
- *részt vesz valamin* (-n) is the usual form for events (*rendezvényen*); the lesson's -ban/-ben holds for *program, munka, vita*. The unit's own screen example used both.
- b1-11-02 *a helybeli piac* is slightly odd Hungarian (unsure); *a falubeliek* plural as a noun.
- Challenge b1-11-04 says Meg recommends Szeged's church: invented (Szeged trip is a2-15, no church mentioned).
- Consolidation title "Unit 11 Consolidation": course-wide numbering.
- Story: Misi's background and Pósalaky's lines are the adaptation's, not checked against the novel.

### 5. Dictionary (b1-11-legyjomindhalalig)
kisdiák | kisdiák | noun | schoolboy, young pupil |
igazmondás | igazmondás | noun | telling the truth, truthfulness |
macskaköves | macskaköves | adj | cobbled |
misikém | Misi | noun | Misi (pet form of Mihály; -ikém = my dear) |
odakinn | odakinn | adv | out there, outside |
lutri | lutri | noun | lottery (old word for the Vienna lottery) |
öregúr | öregúr | noun | old gentleman |
cívisváros | cívisváros | noun | burgher town (Debrecen's nickname) |
karszékbe | karszék | noun | armchair |
köpenyes | köpenyes | adj | wearing a cloak |
mesteremberek | mesterember | noun | craftsman |
nagytiszteletű | nagytiszteletű | adj | very reverend (title for a Calvinist minister) |
nyerőszámait | nyerőszám | noun | winning number |
piacutcán | piacutca | noun | market street |
tanácsülésekről | tanácsülés | noun | council meeting |
tisztelettudóan | tisztelettudó | adj | respectful |

---
## UNIT 23 food-lifestyle (b1-12-01 .. 05, consolidation; story b1-12-szindbad)

### 1. Found by reading
- Unit 23 teaches no new skill; every screen presents known grammar as new:
  - b1-12-01-a-gr: "mediopassive -ódik/-ődik, -ul/-ül" (A2 Units 22 and 31). It shows no -ódik verb, only *megsül, megfő, megpuhul, elkészül*; the old lesson-level line repeats the claim.
  - b1-12-01-b-gr: kitchen prefixes (A2 Unit 22).
  - b1-12-02-gr: frequency adverbs and *előtt/után* (A1 Unit 17), *naponta* (A2 Unit 1), *rendszeresen/időnként* (A2 lists).
  - b1-12-03-gr: először/aztán/végül (A2 Unit 1), *majd* (A2 Unit 11), *miután* (Unit 1), imperative (A2 Unit 10).
  - b1-12-04-gr: "-ú/-ű flavour adjectives" with no -ú/-ű example (-s adjectives are A2 Unit 4).
  - b1-12-05-gr: ordering and paying (A1 Units 19, 23, 24: *kérek, szeretnék, kérnénk*).
  - Fix: recap screens ("You know … from A2 Unit 22"); the bare forms *fő, sül, főz, süt* are italicised so items can use them as met words.
- b1-12-01-a-gr third example uses *gyöngyözve* (-ve, B1 Unit 57) and the detached *fő meg*.
- Glued blanks:
  - b1-12-01-practice-2 *meg____* + puhul
  - b1-12-01-writing-1 *meg____* + fő
  - b1-12-01-writing-2 *fűszer____* + paprika
  - 01-controlled-2 *______aprítjuk* (blank glued to the verb)
  - 05-practice-2 *Fő____* + fogásként
  - 05-writing-2 / dictionary-style hints naming the ending
  - Fixes put the whole word in the blank.
- Unmet words: 248 hits over 54 ids (*perc, sütő, pogácsa, aranybarnára, curry, gyömbér, kurkuma, wasabi, koriander, csillagánizs, citrusfélékkel, zsiradék, energiaital, bélflórát, szervizdíj, csabai, kolbász, paella, croissant, gofri, sushi*). All rewritten.
- Absurd or unmet distractors: *defterdár, vilajet, kancellária, pincéreim, zsoldoshiány, elnéptelenedik, felújít, főbérlő, önkormányzatát*; garbled *napi kettőkor* (b1-12-02-check-2); *Soha* (03-controlled-1), *soha* (consolidation-5).
- Length give-aways: b1-12-02-controlled-3/4, practice-3/4; 03-check-1, 03-controlled-3, 03-practice-3, 03-practice-4; 04-controlled-2; 05-controlled-3/4; consolidation-12. All rewritten.
- Trivia and claims the lessons never teach, replaced by vocabulary items:
  - b1-12-01-practice-4 (traditional Hungarian spices)
  - 04-controlled-1/3, 04-practice-3 (*kürtőskalács* hungarikum), 04-practice-4 (*királyok bora* = Tokaji)
  - 05-controlled-2 (10-15% tip), 05-practice-4 (*szervizdíj*)
  - consolidation-11
- b1-12-05-controlled-4 asks "how many courses" with no number in the answer (suspect `question-answer-type`). b1-12-05-practice-3: all three options are things a waiter says. Both rewritten.
- b1-12-04-dialogue-2 and 04-writing-2 use *sütése* / *alapja* (verbal noun B1 Unit 31; *alapja* unmet). Replaced.
- Hungarian metalanguage in stems: b1-12-01-controlled-1, 01-check-2, 02-controlled-1/2, 03-controlled-1/2, 05-controlled-1, consolidation-4/6/10. Replaced.
- STORY b1-12-szindbad: Q1 is generic (the mood of the stories); fix: where Szindbád sits, correct option stays at index 2. *elűzve, megidézve, elgondolkodva* are -ve/-va forms (B1 Unit 57; unsure, incidental, replaced). Reading-1/2/3 stems were mixed English/Hungarian with unmet options.

### 2. Metadata
- `category: reading` with no text: b1-12-01-practice-4, 02-controlled-3/4, 02-practice-4, 03-practice-3/4, 04-controlled-3, 04-practice-3/4, 05-controlled-4, 05-practice-3/4, consolidation-11 (now grammar `van-zero-copula`), consolidation-10 (stays reading). The others are set to `vocabulary` or grammar tags.
- b1-12-01-controlled-3, check-2 (`mediopassive-verbs-odik`, which covers -ódik/-ik): the forms taught are bare intransitives and *meg-/el-* verbs plus -ul (*megpuhul*). No frozen skill covers -ul/-ül inchoatives (unsure); items kept on `mediopassive-verbs-odik`, controlled-2 on `meg-meaning`.
- b1-12-02-controlled-4: now `ik-verbs-dolgozom-not-dolgozok` with `distractor_skills` 2: how-the-accusative-t-works.
- Added `distractor_skills`:
  - b1-12-01-controlled-3 (2: definite-vs-indefinite-conjugation)
  - b1-12-03-controlled-3 (2: miutan-mielott)
  - b1-12-05-controlled-3 (1: imperative-indefinite, kept)
  - b1-12-consolidation-5 (mert-because, hogy-clauses), consolidation-11 (how-the-accusative-t-works, ban-ben-in)
- Run `lock_tags.py` after applying.

### 3. Goals / checklists
- b1-12-01: "food preparation prefixes (felaprít, átpasszíroz)" and "kitchen preparation stages" never practised.
- b1-12-02: "weight-loss routines", "benefits of dietary fiber, vitamins".
- b1-12-03: "understand and follow recipes", "temperatures".
- b1-12-04: "culinary heritage", "specialized adjectives (zamatos)", "national identity".
- b1-12-05: "service charge etiquette".
- consolidation: "follow and write recipes", "discuss … Hungarikums, and flavor profiles", "comfortably".
- Each change is made in all three places.

### 4. Doubtful
- b1-12-04 whether *kürtőskalács* is an official hungarikum was not checked (unsure): examples now only use *gulyás*, *paprika*, *halászlé* as dishes, and *gulyás* as the hungarikum.
- b1-12-02: the old screen's *eszem gyümölcsöt* is correct (-ik verb); no defect.
- b1-12-01-controlled-2 *A leves fő.* as a wrong option for "becomes done": a native might accept it as a plain statement (unsure).
- b1-12-05 lesson-level and screen *kérhetnénk* is -hat + conditional, both known; only the title is unmet.
- b1-12-consolidation-4 option *megkeményedik* is unmet by my count but was not flagged by the script (unsure).
- Challenge facts: Ildikó, Gulyás recipe (a2-10), Meg and Károly as a couple at dinner (A2 stories).
- Consolidation title "Unit 12 Consolidation": course-wide numbering.

### 5. Dictionary (b1-12-szindbad)
cserépkályha | cserépkályha | noun | tiled stove |
lovaskocsi | lovaskocsi | noun | horse-drawn carriage |
macskaköves | macskaköves | adj | cobbled |
vendéglős | vendéglős | noun | innkeeper |
aranyló | aranyló | adj | golden |
badacsonyi | badacsonyi | adj | of Badacsony (the Balaton wine region) |
eloszlatta | eloszlat | verb | to disperse, to dispel |
kisasztalt | kisasztal | noun | small table |
kiskocsmában | kiskocsma | noun | small inn, tavern |
kristálypoharakon | kristálypohár | noun | crystal glass |
metéltet | metélt | noun | noodles (cut egg noodles) |
porcelántányérból | porcelántányér | noun | porcelain plate |
ráérős | ráérős | adj | unhurried, leisurely |
sarokasztalhoz | sarokasztal | noun | corner table |
szűrődött | szűrődik | verb | to filter in, to seep through |
támlájára | támla | noun | back of a chair |
tisztelettudóan | tisztelettudó | adj | respectful |
üvegezett | üvegezett | adj | glazed, with glass panes |
vendégtérbe | vendégtér | noun | dining room, guest area |
zsírkarikákat | zsírkarika | noun | ring of fat (on soup) |

---
## Fix counts
- Unit 19: 159 fixes (83 exercise `set`, 76 text), 6 challenges
- Unit 21: 155 fixes (80 exercise `set`, 75 text), 6 challenges
- Unit 23: 151 fixes (76 exercise `set`, 75 text), 6 challenges

Also: `/home/user/parlour-read-a` shows only the six new JSON files (and the three `prior-*.md` sheets) as untracked; no content file was edited.