# Review of B1 Units 13, 15 and 17 (prompt-b): final report

The harness refused the report file (`/home/user/parlour-read-b/report-education-learning.md`), so this reply is the only report.

Written to `/home/user/parlour-read-b/`:
- `fixes-education-learning.json`: 81 fixes
- `fixes-travel-mobility.json`: 78 fixes
- `fixes-health-wellbeing.json`: 71 fixes
- `challenges-education-learning.json`, `challenges-travel-mobility.json`, `challenges-health-wellbeing.json`: 6 challenges each

I ran the five commands from the prompt for each unit, and nothing else. The one exception is `audit-reader-coverage.js` with `--top 50` instead of `--top 0`, because `--top 0` hides the "not in the dictionary" list. Nothing was tested or applied: no `check_fixes.py`, no repo copies, no `lock_tags.py`. Run `lock_tags.py` per unit after applying.

Notes that apply to every unit:
- Goal and checklist changes are three fixes per lesson file (goal array, goal section, checklist section). `curriculum/curriculum.json` and `indexes/competencies-index.json` repeat those lines and are built from the lessons, so I did not fix them.
- Every lesson's challenge screen carries the generic text "Put your Hungarian skills into practice for this goal." and a truncated title. The six new challenges per unit replace them. Each `canDo` is the lesson's first checklist line.
- Where a rebuilt wrong option is a real form of another skill, I added `distractor_skills`.

---

# 1. hu b1 education-learning (Unit 13)
Lessons b1-07-01 to b1-07-05 and b1-07-consolidation, story b1-07-tanarurkerem.

Every grammar point in this unit is taught earlier, so the first four lessons present known material as new.

## 1. Found by reading
Screens:
- **b1-07-01-a-gr:** *-hat/-het* presented as new, but `potential-hat-het` is A2 Unit 23. Fix: "You know … from A2 (Unit 23)". The tip example *megtanulhatja* is unmet; replaced by *olvashatja*.
- **b1-07-01-b-gr:** *után, előtt, közben* presented as new, but `temporal-postpositions` is A1 Unit 17. Fix: recap. The example *gyakorlati tapasztalatot* is unmet; replaced by *sokat tanulunk*.
- **b1-07-02-gr:** *azért, hogy* + *-jon/-jen* presented as new, but both skills are B1 Unit 5. Fix: "You know … from Unit 5".
- **b1-07-03-gr:** *összpontosít vmire* + *-ra/-re* presented as new, but `verb-government-ra-re` is B1 Unit 3. Fix: recap.
- **b1-07-04-gr:** the superessive *-n* is explained as new (A1 Unit 16). Fix: "you know from A1".
- **b1-07-05-gr:**
  - It teaches "nominal compounds" (`noun-compounds`, Unit 31) and doesn't recap the two known patterns.
  - Example 3, *gondolkodásunk*, is a verbal noun in -ás (Unit 31). Replaced by *A kíváncsiság segít abban, hogy új dolgokat tanuljunk.*

Items:
- **07-01-controlled-4:** the wrong options are word salads (*Előtt az érettségi a diákok tanulnak sokat*). Rebuilt as one sentence with előtt / után / közben.
- **07-01-practice-1:** *kérdezhet* is unmet and on no screen. Replaced by *felvételizhet*.
- **07-01-practice-3:** *gyermek, ingyen* unmet. Replaced by *diák, ingyenesen*.
- **07-01-practice-4:** *nyugdíjba* is unmet and absurd. Replaced by *Gimnáziumba jelentkeznek.*
- **07-01-dialogue-1:** *nevű* unmet.
- **07-01-dialogue-2:**
  - The third option, *Nem, de szerencsére rosszul sikerül.*, is absurd and has two faults.
  - The item tests the past form but is tagged `yes-no-questions`.
  - Options are now sikerült / sikerül / sikerülni.
- **07-01-writing-1:** *bárki* unmet; *Mindenki* is a tell-absolute (ERROR); the wrong options have two faults. Rebuilt.
- **07-01-writing-2:** *felépített, rendszere, állandóan* unmet; the wrong options are non-phrases. Rebuilt.
- **07-01-check-1:** the wrong option *választás* is an unmet verbal noun. Replaced by *választ*.
- **07-01-check-2:** *óvoda, bölcsőde* are unmet and precede primary school. Replaced by *általános iskola, egyetem*.
- **07-02-controlled-3:** *szaktudását* unmet. Replaced by *szakismeretét*.
- **07-02-practice-2:**
  - Length-giveaway 65 vs 36 and *senki* tell (both ERRORS).
  - *munkavállalók, korszerű, ismeretekkel, bezárjanak* unmet; absurd wrong options.
  - Rebuilt on mood and agreement.
- **07-02-practice-3:** *járhassak* (-hat + subjunctive) is taught nowhere. Replaced by *járjak*.
- **07-02-dialogue-1:** *elmélyítsem, tudásomat* unmet.
- **07-02-dialogue-2:** option 3 is garbled with two faults.
- **07-02-writing-1:** *holott* unmet; option 3 is a non-answer.
- **07-02-writing-2:** *semmilyen* tell (ERROR); *szükséges, nincsen, ismeret, pozícióról* unmet. Rebuilt as *Mi a célkitűzésed?*.
- **07-03-controlled-3:** *sikeres, tanuláshoz, szükséges* unmet.
- **07-03-controlled-4:** length-giveaway 19 vs 14 (ERROR); *tanuló, jegyzet* unmet; absurd wrong options.
- **07-03-practice-1:** *figyelmesen, hatékony, tanulási, alapos* unmet.
- **07-03-practice-2:** length-giveaway 56 vs 40 and *soha* tell (ERRORS); *úgy* unmet. Rebuilt as short answers *Sok ismétléssel / ismétlést / ismétlésben*.
- **07-03-practice-3:** *előadáson, hallgatók, füzetükbe* unmet.
- **07-03-dialogue-1:** *próbálj, sémákat, próbálsz* unmet; option 3 garbled. Rebuilt on the definite imperative.
- **07-03-dialogue-2:** *gondolatokra, emlékezni, emlékszem* unmet.
- **07-03-writing-1:** *soha* tell (ERROR); *zaj, zajra* unmet.
- **07-03-writing-2:** *tanulást* unmet.
- **07-03-check-1:** *tanítás, vizsgázás* unmet.
- **07-04-controlled-3:** *sikeres, átvehette* unmet.
- **07-04-practice-1 and -practice-2:** *kitűnő, elégtelen, osztályzat, felelet, ötös, jeles, egyes, tízes* unmet. practice-2 also has length-giveaway 23 vs 9 (ERROR).
- **07-04-practice-3:** *bukom* unmet. The blank is now *megbukom* in an affirmative sentence, because a negated sentence needs the prefix split.
- **07-04-practice-4:** length-giveaway 41 vs 24 (ERROR).
- **07-04-dialogue-1:** *ötöst* unmet.
- **07-04-dialogue-2:** *tanévzáró, ünnepségen/-ben/-ről* unmet; option 3 has two faults.
- **07-04-writing-1 and -writing-2:** *eljöttem, írásban, esszéjére, esszét* unmet; non-phrases.
- **07-04-check-2:** length-giveaway 8 vs 4 (ERROR).
- **07-05-intro-2:** length-giveaway 28 vs 15 (ERROR).
- **07-05-controlled-2:** *naplókat* unmet; length 13 vs 9 (ERROR).
- **07-05-controlled-3:** *fedezzünk* unmet.
- **07-05-controlled-4:** *soha* tell (ERROR); *fejlődhet, tanulás* unmet.
- **07-05-practice-1:** *folyamatos, kiváló, természetes* unmet.
- **07-05-practice-2:** length 50 vs 33 and *mindenki* tell (ERRORS); *gazdaság, technológia* unmet.
- **07-05-practice-3:** *elérhetővé* unmet.
- **07-05-dialogue-1:** *újrakezdésre/-ben* unmet; option 3 (*Igen, nem félek semmitől*) is a second kind of fault.
- **07-05-dialogue-2:** *podcastokat, cikkeket* unmet; option 2 has two faults.
- **07-05-writing-1:** length 54 vs 36 (ERROR); *ösztönöz, felfedezésére, kíváncsi, kíváncsian, televíziót* unmet.
- **07-05-writing-2:** *senki* tell (ERROR).
- **07-05-reading-1:** *büféhez, igazgatójához* unmet; the right option has him go to the teacher too, but he stays at the board.
- **07-05-reading-2:** *fizikából* unmet.
- **07-05-reading-3:** length 59 vs 33 (ERROR); seven unmet words.
- All three readings are rebuilt on met words and story facts: Steinmann at the board, warm sunny weather outside, relief at the end.
- **consolidation-5:** *tananyagra* unmet.
- **consolidation-6:** *ötös, egyes, tízes* unmet.
- **consolidation-8:** *tanfolyam, szaktudását* unmet.
- **consolidation-9:** *soha* tell (ERROR); *folyamatos, készségek, elsajátítását, hagyhatják* unmet.
- **consolidation-10:** *bárki* unmet; *Mindenki* tell (ERROR).
- **consolidation-11:** *figyelmesen, előadás* unmet.
- **consolidation-12:** *megbuktuk* is not a real form; *írásban* unmet.
- The consolidation speaking lines are generated from items 5 and 8, so they change with those fixes.

## 2. Metadata
- **07-01-dialogue-2:**
  - `yes-no-questions` → `past-tense-indefinite`.
  - ds: sikerül `present-tense-routine-language`, sikerülni `building-the-infinitive-the-suffix-ni`.
- **07-02-practice-2:** vocabulary → `hogy-jon-jen` (grammar).
- **07-02-dialogue-2:** `present-tense-routine-language` → `nek-conditional`; ds `definite-past`.
- **07-02-writing-2:** vocabulary → `possessive-suffixes`; ds `3rd-person-possessive`.
- **07-03-practice-2:** vocabulary → `val-vel`.
- **07-03-dialogue-1:** `imperative-indefinite` → `imperative-definite`; ds `definite-vs-indefinite-conjugation` and `imperative-indefinite`.
- **07-04-dialogue-1:** `present-tense-routine-language` → `past-tense-indefinite`.
- **07-04-dialogue-2:** `on-en-on` → `ban-ben-in`; ds `movement-with-ba-be`.
- **07-05-dialogue-2:** vocabulary → `val-vel`; ds `ban-ben-in`.
- **07-05-dialogue-1:** ds `how-the-accusative-t-works`.
- **New ds on rebuilt options:** 07-01-writing-1 and -check-1; 07-02-writing-1; 07-04-writing-1; consolidation-10 and -12.

## 3. Goals / checklists
- **b1-07-01 line 3:** "schools and qualifications" (no such word is taught) → "schools and the school-leaving exam".
- **b1-07-01 line 4:** "admission requirements and graduation exams" (admission requirements aren't practised) → "I can say what students may do after primary school."
- **b1-07-02 line 4:** "long-term training plans with peers" → "I can say why I joined a course or a training."
- **b1-07-03 line 4:** "organize their study schedule" → "I can advise a friend how to remember new words."
- **b1-07-05 line 3:** "complex aspirations" → "I can say what lifelong learning offers adults."

## 4. Doubtful
- **Story question 1** of b1-07-tanarurkerem ("Milyen alapvető helyzetet és hangulatot mutat be a karcolat?") asks about text type and mood, not what happens. (unsure; questions 2 and 3 are fine)
- **Words in no vocabulary list:** *tanfolyam* (07-02), *rendszeres* (07-03), *szakma, felnőttkori, munkaerőpiac, nagyszerű* (07-05) pass only because a screen of their own lesson uses them. I did not add them to the vocabulary lists, because each list is "four new words" by design. The reviewer may want them listed. (unsure)
- **07-01-practice-2** (*Hány évig tart … általános iskola?*) tests a fact but is tagged vocabulary. (unsure, left)
- **07-03 screen title** "Verbs of Study & Attention: összpontosít, jegyzetel": *jegyzetel* takes no case. (unsure, left)
- I found no later-list forms (-andó, -va/-ve, volna, ahol, reported commands) in items.
- The story uses *mintha* and *fejcsóválva* (-va). That is exempt as a story.

## 5. Dictionary
leghátsó | hátsó | adj | rear, back (superlative: the one furthest back) |
mázsás | mázsás | adj | weighing a quintal (100 kg), very heavy |
padtárs | padtárs | noun | desk mate, classmate who shares a bench |
visszasiet | visszasiet | verb | to hurry back |
bemagolja | bemagol | verb | to learn by rote, to cram |
dermesztő | dermesztő | adj | chilling, bone-chilling |
fejcsóválva | fejcsóvál | verb | to shake one's head |
görcsösen | görcsösen | adv | tensely, convulsively |
ismételgeti | ismételget | verb | to repeat over and over |
katedrára | katedra | noun | teacher's desk, lectern, podium |
katedráról | katedra | noun | teacher's desk, lectern, podium |
köhécsel | köhécsel | verb | to cough lightly, to clear one's throat |
lemondóan | lemondó | adj | resigned (adverb: resignedly) |
megfellebbezhetetlen | megfellebbezhetetlen | adj | final, not open to appeal |
ólomsúlyúnak | ólomsúlyú | adj | heavy as lead, leaden |
osztálynaplót | osztálynapló | noun | class register |
padlózatra | padlózat | noun | flooring, floor |
padsorokban | padsor | noun | row of desks |
roskad | roskad | verb | to sag, slump, collapse |
vesztőhelyre | vesztőhely | noun | place of execution, scaffold |
(*steinmann* is a character's name and is skipped.)

**Fix count: 81 (education-learning); challenges 6.**

---

# 2. hu b1 travel-mobility (Unit 15)
Lessons b1-08-01 to b1-08-05 and b1-08-consolidation, story b1-08-szentpeter.

b1-08-03 already opens "You know *-ig* …", as required.

## 1. Found by reading
Screens:
- **b1-08-01-a-gr:**
  - *keresztül* presented as new (A2 Unit 5).
  - It doesn't say which case *felé/felől* take. Fixed: plain nominative.
- **b1-08-01-b-gr:**
  - *átszáll vmire* + -ra/-re presented as new (B1 Unit 3). Recap added.
  - Example 2 has the verbal noun *felszállás* (-ás, Unit 31). Replaced by *Mielőtt felszállunk, érvényesítenünk kell a jegyet.*
  - *menetrend szerint* is a chunk with *szerint*, whose evidential skill is Unit 25. Left as a listed phrase. (unsure)
- **b1-08-02-gr:** the directional prefixes fel-/le-/be- (A1 Unit 28) and *keresztül* (A2 Unit 5) are presented as new. Recap added.
- **b1-08-04-gr:**
  - Prefixes are not recapped (A2 Unit 22).
  - Example 2, *felújítás alatt álló*, has a verbal noun and a participle. Replaced by *Pótlóbusz jár a vonatok helyett.*
- **b1-08-05-gr:**
  - It teaches "compound nouns" (Unit 31).
  - Example 1 has *megtekintésével* (-és, Unit 31).
  - It doesn't recap the unit's own points. Rewritten.

Items:
- **08-01-controlled-2:** *felé* and *felől* both fit, because no meaning is given. Pinned with "(towards the Danube)".
- **08-01-controlled-3:** *gyorsvonat, percen, belül* unmet.
- **08-01-controlled-4:** word-salad wrong options.
- **08-01-practice-1:** *pontos, közvetlen, végső, automatikus* unmet.
- **08-01-practice-2:** *hegyi* unmet, and *hágó* is taught in the next lesson.
- **08-01-practice-3:** *szellő, völgybe* unmet.
- **08-01-practice-4:** length 62 vs 32 (ERROR); *közvetlenül* unmet.
- **08-01-dialogue-1:** *közvetlen, járat, mégis, szállnod* unmet.
- **08-01-writing-1 and -writing-2:** non-phrase or unrelated wrong options.
- **08-02-intro-2:** length 13 vs 9 (ERROR).
- **08-02-controlled-3:**
  - "Duna-" is glued to the blank.
  - *Duna-folyóparton* is not Hungarian.
  - Blank the whole word.
- **08-02-controlled-4:** length 18 vs 13 (ERROR).
- **08-02-practice-1:** *megnézi* unmet.
- **08-02-practice-2:** *megtaláljuk, helyes, ösvényt, lefényképezzük* unmet; *túrázás/való*.
- **08-02-practice-3:** *kirándulók* unmet.
- **08-02-practice-4:** *átkelés* is a verbal noun (-és, Unit 31).
- **08-02-dialogue-1:** *erdős, völgybe* unmet; option 3 has two faults.
- **08-02-dialogue-2:** *semmilyen* tell (ERROR); *részletes* unmet; option 2 has two faults.
- **08-02-writing-1:** *semmilyen* tell (ERROR); *nincsen* unmet.
- **08-02-writing-2:** *átúsztunk* unmet.
- **08-02-check-2:** length 9 vs 5 (ERROR).
- **08-03-intro-2:** length 20 vs 15 (ERROR).
- **08-03-controlled-4:** *időtartama, órakor* unmet.
- **08-03-practice-1:** *pontos, jelentős, időtartama* unmet.
- **08-03-practice-2:** length 45 vs 26 (ERROR); *indulási, perccel* unmet.
- **08-03-practice-3:** *kimerítő, buszozás* unmet.
- **08-03-dialogue-1:**
  - ERROR taught-later: tagged `causal-postpositions` (B1 Unit 31), but the answer uses *miatt* (A2).
  - *perc, műszaki, percre, várható* unmet.
- **08-03-writing-1:** *fürödtünk* unmet.
- **08-03-writing-2:** *várható, korábbi* unmet.
- **08-04-controlled-3:** *megrongálódott* unmet.
- **08-04-controlled-4:**
  - The right option says *elkéstük a csatlakozást*, which is wrong Hungarian. *elkésik* means "be late"; missing a connection is *lekésik*.
  - Length 60 vs 37 (ERROR); *kocsiban* unmet.
- **08-04-practice-1:** *száll* unmet (split in *száll át*).
- **08-04-practice-2:** length 60 vs 32 (ERROR); *vasúti, sínek, könyvesbolthoz* unmet.
- **08-04-practice-3:** *szállítják, utasokat, pótlóbusszal, pályafelújítás* (-ás) unmet.
- **08-04-dialogue-1:** *kalauz* unmet; options 2 and 3 have two faults each.
- **08-04-dialogue-2:** *Azt mondják, hogy …* is reported speech (Unit 25, later); *felsővezeték, szakadás* unmet.
- **08-04-writing-1:** *soha* tell (ERROR).
- **08-05-controlled-2:** *főszezonban* unmet.
- **08-05-controlled-3:** *összeállítottuk, egyhetes, részletes* unmet.
- **08-05-controlled-4:** length 57 vs 36 (ERROR); *lefoglaltuk, összeírtuk, főbb* unmet.
- **08-05-practice-1:** *sikeres, részletes* unmet.
- **08-05-practice-2:** *beosszuk, vasúton, felejtsük* unmet.
- **08-05-practice-3:** *híres* unmet.
- **08-05-practice-4:** length 38 vs 27 (ERROR).
- **08-05-dialogue-1:** *panziót/-ban, nincsen* unmet.
- **08-05-dialogue-2:** *belvárost/-ban/-ból* unmet.
- **08-05-writing-2:** *ködben* unmet.
- **08-05-reading-1:** *elbeszélésében, jogi, konferenciára, tengerpartra* unmet.
- **08-05-reading-2:**
  - Length 65 vs 35 (ERROR).
  - *ellenére* (concessive-postpositions, Unit 57) in the question.
  - *néhai, édesanyját* unmet.
- **08-05-reading-3:** *postakocsin, gyorsvonattal, gőzhajón* etc. unmet.
- All three readings are rebuilt on story facts: Glogova, a lost fortune, autumn rain.
- **consolidation-5:** *hegyi* unmet.
- **consolidation-7:** *repülőgépek* unmet.
- **consolidation-8:** *szezonra* unmet.
- **consolidation-9:** length 58 vs 43 (ERROR) and many unmet words.
- **consolidation-10:** wrong options have two faults.
- **consolidation-11:** wrong options are different sentences.
- **consolidation-12:** *kiírva* (-va participle, Unit 57) in a wrong option.

## 2. Metadata
- **08-02-practice-2:** vocabulary → `hogy-jon-jen`.
- **08-02-writing-1:** vocabulary → `keresztul`; ds `ban-ben-in`, `postposition-fele`.
- **08-02-dialogue-2:** ds `yes-no-questions` → `van-and-nincs-there-is-there-isn-t`.
- **08-03-dialogue-1:** `causal-postpositions` → unit vocabulary; ds `ra-re`, `postposition-fele`.
- **08-03-practice-2:** vocabulary → `temporal-postpositions`.
- **08-04-dialogue-2:** `fog-infinitive` → `mert-because`.
- **08-04-dialogue-1:** ds `on-en-on`.
- **08-05-practice-2:** vocabulary → `hogy-jon-jen`.
- **08-05-controlled-3:** `acc-poss` → vocabulary, because the answer is now nominative.
- **New ds on rebuilt options:** 08-01-controlled-4 and -writing-1; 08-02-controlled-4, -dialogue-1 and -writing-2; 08-03-writing-1; 08-05-dialogue-1, -dialogue-2 and -writing-2; consolidation-10 and -11.

## 3. Goals / checklists
- **b1-08-01 line 4:** "directions and transfer information" → "I can ask whether a train needs a transfer."
- **b1-08-03 line 4:** "calculate travel time differences" → "I can say how long a journey takes and how late a train is."
- **b1-08-05 line 3:** "recommendations for exploring towns" → "I can say what we visit and where we stay on a trip."

## 4. Doubtful
- ***perc*** is in no vocabulary list. Screen examples of 08-01 and 08-03 use it; the items now avoid it. If wanted, add it to b1-08-01's vocabulary. (unsure)
- **08-01-dialogue-2** is tagged `yes-no-questions`, but its wrong options fault the time suffix and a *Nem*. Mixed tag, left. (unsure)
- **Story questions** are fine. Q3 is abstract but answerable.

## 5. Dictionary
ázó | ázik | verb | to get soaked, drenched |
bankutalványos | bankutalványos | adj | consisting of bank drafts (bankutalvány = bank draft) |
bepárásodott | bepárásodik | verb | to mist up, fog up |
bőrkabátban | bőrkabát | noun | leather coat |
bőrtáskáját | bőrtáska | noun | leather bag, satchel |
célállomásig | célállomás | noun | destination, terminus |
csóválta | csóvál | verb | to wag, shake (head, tail) |
fanyelében | fanyél | noun | wooden handle |
fatemplom | fatemplom | noun | wooden church |
felsejlő | felsejlik | verb | to loom up, appear dimly |
fenyvesek | fenyves | noun | pine forest |
hegyoldalak | hegyoldal | noun | mountainside, hillside |
kishúgának | kishúg | noun | younger sister |
léckerítésének | léckerítés | noun | slat/picket fence |
mikorra | mikor | adv | when |
pipázó | pipázik | verb | to smoke a pipe |
sziklafalak | sziklafal | noun | rock face, cliff wall |
zötykölődés | zötykölődés | noun | jolting, bumping along |
zötykölődött | zötykölődik | verb | to jolt, bump along |
zsúpfedeles | zsúpfedeles | adj | thatched, thatch-roofed |

**Fix count: 78 (travel-mobility); challenges 6.**

---

# 3. hu b1 health-wellbeing (Unit 17)
Lessons b1-09-01 to b1-09-05 and b1-09-consolidation, story b1-09-estikornel.

This unit also teaches nothing new: everything in it is known, so the grammar screens present known material as new.

## 1. Found by reading
Screens:
- **b1-09-01-b-gr:**
  - The rule "modals take a dative subject" is false for its own examples, which have none.
  - It presents *kell/muszáj* (A1 Unit 24), *lehet* (A1 Unit 30) and inflected infinitives (A2 Unit 21) as new. Rewritten as a recap.
  - Example 2 has *bejelentkezés* (-és, later). Replaced.
- **b1-09-02-gr:** *szabad/tilos* presented as new (A2 Unit 23). Example 2 has the compound *Gyógyszerszedés* and *fogyasztani*. Fixed.
- **b1-09-03-gr:** *panaszkodik vmire* + -ra/-re needs a recap (Unit 3).
- **b1-09-05-gr:** *érdemes/ajánlott* presented as new (A2 Unit 18, `kellene`). Only *tanácsos* is new.
- **b1-09-04-gr** is fine.

Items:
- **09-01-controlled-3:** *erősíti, emberi* unmet.
- **09-01-controlled-4:** length 63 vs 34 and *soha* tell (ERRORS); *helyes, hozzátartozik, betegség* unmet.
- **09-01-practice-1:** *kiegyensúlyozott, betegségek, emberi* unmet.
- **09-01-practice-2:** length 68 vs 37 and *senki* tell (ERRORS); several unmet words.
- **09-01-dialogue-1:** *soha* tell (ERROR); *megőrzéséért* is a verbal noun (-és, Unit 31).
- **09-01-dialogue-2:** *egyáltalán* tell (ERROR); *úgy* unmet; option 3 contradicts *De igen*.
- **09-01-writing-1:** *gyógyítás, betegség, gyorsabban* unmet.
- **09-02-intro-1:** length 20 vs 15 (ERROR).
- **09-02-controlled-3:** *túlzott, rendkívül* unmet.
- **09-02-controlled-4:** length 57 vs 41 (ERROR); *bármennyi, korlátlanul, legfontosabb* unmet.
- **09-02-practice-1:** *szenvedély, helyes, túlzott* unmet.
- **09-02-practice-2:** *fogyaszd* unmet.
- **09-02-practice-3:** *megpróbálni* unmet.
- **09-02-practice-4:** length 30 vs 19 (ERROR).
- **09-02-dialogue-1:** option 2 has two faults; option 3 uses unmet *parkolás/épület*.
- **09-02-dialogue-2:** *csökkentettem, gyógyteát, úgy, feketekávét* unmet; option 2 has two faults. The verbs are past, so the tag was wrong.
- **09-02-writing-1:** *soha* tell (ERROR); *túlzott, sófogyasztás* unmet.
- **09-03-intro-2:**
  - *eltépi, megeszi* are unmet and absurd.
  - The question has "an Hungarian".
- **09-03-controlled-3:** *alapos, hatékony* unmet.
- **09-03-controlled-4:** *orvosság* unmet.
- **09-03-practice-1:** *meghallgat* unmet.
- **09-03-practice-2:** *pénztárcájában* unmet.
- **09-03-practice-4:** length 42 vs 26 (ERROR); *gyógyszerkiváltás* is an -ás compound.
- **09-03-dialogue-1:** *teljesen* tell (ERROR); *megvizsgálom/-ja, kórosat* unmet. Rebuilt as a doctor's question with one fault each.
- **09-03-dialogue-2:** *semmilyen* tell (ERROR); option 2 has two faults.
- **09-04-intro-2:** *megállít* unmet.
- **09-04-controlled-3:** *megtartani, közötti* unmet.
- **09-04-controlled-4:** length 54 vs 35 (ERROR); *kiadós, feszülten, vitatkozni* unmet.
- **09-04-practice-1:** *lelki, aktív, feszültségmentes, környezet* unmet.
- **09-04-practice-2:** length 53 vs 31 and *soha* tell (ERRORS); *regenerálódjon, belső* unmet.
- **09-04-practice-3:** *zavartalan* unmet.
- **09-04-practice-4:** length 33 vs 25 (ERROR); *aktív* unmet.
- **09-04-dialogue-1:** *kimerültnek, férne, kipihent* unmet; option 3 absurd; the `case-inflected-pronouns` tag doesn't show.
- **09-04-dialogue-2:** *késő, megnyugodjak* unmet.
- **09-04-writing-1:** *semmilyen* tell (ERROR); *nincsen, növeli* unmet.
- **09-04-writing-2:** *megtalálnunk* unmet.
- **09-04-check-2:** *elvinni, behozni* unmet.
- **09-05-controlled-3:** *helyes, meghozta* unmet.
- **09-05-controlled-4:** length 58 vs 41 and *Soha* tell (ERRORS); *elmúlik* unmet.
- **09-05-practice-1:** *teljes, fizikai* unmet.
- **09-05-practice-2:** *bőséges, éjszakai, elutasításával* unmet.
- **09-05-practice-3:** *szívből, mielőbbi* unmet.
- **09-05-dialogue-2:** *semmilyen* tell (ERROR); *mézes, jeges* unmet.
- **09-05-writing-1:** *semmilyen* tell (ERROR); *mielőbbi* unmet.
- **09-05-writing-2:** *betegség* unmet.
- **09-05-reading-1:** length 28 vs 20 (ERROR); *budai* (Unit 20, later) unmet.
- **09-05-reading-2:** length 50 vs 36 (ERROR); several unmet words.
- **09-05-reading-3:** length 34 vs 25 (ERROR); several unmet words.
- **consolidation-4:** *szigorúan* unmet.
- **consolidation-5:** *panaszkodott* is in no vocabulary list (it appears only on the 09-03 screen). Rebuilt on *háziorvoshoz*.
- **consolidation-6:** length 29 vs 17 (ERROR).
- **consolidation-8:** *felépüléshez, szükséges* unmet.
- **consolidation-10:** *mindennapi, odafigyelnie* unmet.
- **consolidation-11:** *szigorúan, dohányoztunk* unmet.

## 2. Metadata
- **09-01-controlled-3:** → unit vocabulary.
- **09-01-dialogue-1:** ds `how-the-accusative-t-works`.
- **09-01-dialogue-2:** → `inflected-infinitives`.
- **09-02-dialogue-1:** ds `ban-ben-in`.
- **09-02-dialogue-2:** `present-tense-routine-language` → `irregular-past`.
- **09-03-dialogue-1:** → `possessive-suffixes`.
- **09-04-dialogue-1:** `case-inflected-pronouns` → `possessive-suffixes`.
- **09-04-controlled-3:** → unit vocabulary.
- **consolidation-5:** `past-tense-indefinite` → `hoz-suffix`.
- **consolidation-11:** ds `itt-ott-here-there`.

## 3. Goals / checklists
- **b1-09-03 line 2:** "understand examination instructions and prescriptions" (not practised) → "I can say what I complain of and what the doctor prescribes."
- **b1-09-04 line 2:** *egyensúlyt tart* is never practised → "megtalálja az egyensúlyt".
- **b1-09-05 line 2:** → "I can say what treatment helps and wish someone a quick recovery."

## 4. Doubtful
- **Story question 3** (mood on arrival) and **question 1** (the main insight) are abstract but answerable. (unsure)
- **09-02-writing-2** keeps *A dohányzás nem mindenhol tilos* as a wrong option. It is contradictory, but the English pins "strictly". (unsure)
- **Missing vocabulary:** *kezelés, tanácsos* are listed. *betegség, mozgás, feszült* are in no list; I avoided them. Whether to add *betegség* is for the reviewer. (unsure)

## 5. Dictionary
belgyógyász | belgyógyász | noun | internist, specialist in internal medicine |
falikút | falikút | noun | wall fountain |
gyógyszerszag | gyógyszerszag | noun | smell of medicine |
méregdrága | méregdrága | adj | very expensive, extremely dear |
szemközti | szemközti | adj | opposite, facing |
akaratlanul | akaratlanul | adv | involuntarily |
bőrfotelbe | bőrfotel | noun | leather armchair |
elcsendesedik | elcsendesedik | verb | to fall silent |
fanyarul | fanyarul | adv | wryly, with a sour smile |
forgatagában | forgatag | noun | hustle and bustle, whirl |
fürkészte | fürkész | verb | to scrutinize, search with the eyes |
kiadós | kiadós | adj | substantial, generous, ample |
lélegzetvisszafojtva | lélegzetvisszafojt | verb | to hold one's breath |
megilletődik | megilletődik | verb | to be moved, be touched, be overcome |
mélységesen | mélységesen | adv | deeply, profoundly |
ólmos | ólmos | adj | leaden, heavy as lead |
pumpás | pumpás | adj | with a pump, pump-operated |
receptpapírt | receptpapír | noun | prescription paper |
szorongatta | szorongat | verb | to squeeze, grip, press hard |
várószobájába | váróterem | noun | waiting room |
(*kornél* is a character's name and is skipped.)

**Fix count: 71 (health-wellbeing); challenges 6.**

---

**Fix counts: education-learning 81, travel-mobility 78, health-wellbeing 71 (230 in all); challenges 6 + 6 + 6.**