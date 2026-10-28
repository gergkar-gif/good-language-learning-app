# Reader A report, batch core 55-65: Units 55, 57, 59

## Unit 55 rules-rights-responsibilities (b1-28)

Commands run: check-content (10 length-giveaway ERRORs, 2 suspects), render_lesson, unmet-words (about 150 hits), audit-reader-coverage. All fixes are in `fixes-rules-rights-responsibilities.json` (68), challenges in `challenges-rules-rights-responsibilities.json` (6).

### 1. Found by reading
- Every exercise of b1-28-01..05 and consolidation used unmet words (legal register: *ceruza, hegyezés, védőszemüveg, tartózkodni, elválaszthatatlan, szabadságjog, fegyelmi, kényes, reklámfüzet, kamat, vállfára, pártatlan, ítélet, bankutalvány*, forms like *betartani/betartó/követő* that no list or own screen carries). All 48 items rewritten with met words (one fix per id, `set`).
- 10 check-content ERRORs (b1-28-01.ex01/ex04, 02.ex01/ex06, 03.ex01/ex04, 04.ex01/ex04, 05.ex01/ex04): right option 1.5-2x the wrong ones; fixed inside the rewrites (vocabulary items now "What does *X* mean?" with three English options of one length; grammar options rebuilt).
- Glued blanks that make the unmet-word checker read stems (*til_____, vol_____, kötele_____, ar_____, él_____, számá_____, kérés_____, kivétel_____, engedély_____, tettei_____, elvégz_____, marad_____*): 01.ex02/ex07, 02.ex02/ex05/ex07, 03.ex02/ex05/ex07, 04.ex02/ex05/ex07, 05.ex02/ex05/ex07, consolidation.ex02/ex05/ex07 all blank the whole word now.
- All 12 sentence-builders (01.ex03/ex08 … consolidation.ex06) had `english` "Build the sentence in the correct order." instead of a translation; every builder now has a real `english`.
- Screens presenting known material as new: b1-28-01-a (*tilos, szabad, kötelező* + infinitive = A2 Unit 23), 02-a (*-andó/-endő* = B1 Unit 27, `future-participle-ando`), 02-b (*felelősséget vállal* B1 Unit 45, *-ért* A2 Unit 8), 03-b (*kell, muszáj* A1 Unit 24, *kénytelen* B1 Unit 19), 04-b (*amennyiben* A2 Unit 13, `ha-clause`), 05-b (*ezzel szemben* B1 Unit 21, *ugyanakkor* B1 Unit 35). Each now opens "You know … from <unit>" with the new part named.
- b1-28-05-b: example 2 (*A vitát végül kölcsönös megegyezéssel …*) illustrates none of *ezzel szemben / ugyanakkor / holott*, and *holott* has no example: replaced by *A cég azt állítja, hogy mindent betartott, holott …*.
- b1-28-05.ex04 and ex06 are reading questions about Mikszáth's novel, but the story appears only in the consolidation lesson (the learner has not read it); ex04's right answer says "A gazdag nagybácsi elveszett örökségét" while the story says Wibra György's *apja* hid the money; wrong options absurd (*Házat akart vásárolni*, *a besztercei püspök*). Replaced by a grammar item (`adversative-contrast`, ezzel szemben was never practised) and a vocabulary item (*igazságosság* was `vocab-unused`). `stage` "literature" removed from ex04.
- b1-28-consolidation.ex04 / ex08: wrong options absurd (*Minden vagyont felgyújtanak*, *börtönbe zárja … az összes lakóját*, *varázserejű kard*) and full of unmet words; rewritten as English questions with plausible wrong options that the story rules out (consolidation.ex04 asks why György goes to Glogova, ex08 what happened to the handle).
- b1-28-consolidation.ex01 (*-andó/-endő* choice): *követendő* and *követő* are in no list at this point and the screens of lesson 02 are not "earlier screens" for the checker; replaced by a *kénytelen volt* tense item (`formal-obligation`). consolidation.ex02 copied the speaking line; replaced.
- b1-28-02.ex04 asked in Hungarian metalanguage (*beálló melléknévi igenév*) with absurd option *A betartó törvények sétálnak a téren*; now an English question with `a megoldandó / megoldott / megoldani feladat`.
- b1-28-03.ex04 (*Miben különbözik a 'muszáj' a 'kell'-től?*): tests an invented nuance with *csak múlt időben létezik* (false); replaced by a *kellett / kell / kellene* item (`kell-infinitive`).
- Vocabulary items unused: *tiltás* (b1-28-03) and *igazságosság* (b1-28-05) are now used (03.ex06, 05.ex06).
- Wrong option as a second right answer: b1-28-04.ex02 (*köteles* / *kénytelen* both fit "obliged"): `answers` lists both.
- Story b1-28-mikszath: comprehension question 2 explanation says *a nagybácsi*, the text says Wibra's *apja* (fixed to *az apja*); `characters` lists *Sztolarik közjegyző úr*, who never appears (removed, unsure).

### 2. Metadata
- b1-28-02.ex05: tagged `possessive-suffixes` (A1); the tested form is the plural possessed *kötelességei*, so now `plural-possessive` (A2 Unit 3).
- b1-28-03.ex04: `kell-infinitive` kept, `distractor_skills` {2: kellene} added for *kellene mennem*.
- b1-28-05.ex04: category reading -> grammar, `teaches` adversative-contrast, `distractor_skills` {1: mert-because, 2: ha-clause}; ex06 reading -> vocabulary with the unit vocab skill.
- b1-28-02.ex04: `distractor_skills` moved from index 2 to index 1 (*megoldott*, `past-participle-adjective`); the other wrong option is the ungrammatical *megoldani feladat* (none).
- b1-28-01.ex04 keeps its two `distractor_skills`; b1-28-04.ex04 now {1: mert-because, 2: concessive-annak-ellenere}.
- consolidation.ex01 teaches `formal-obligation`, ex02 `ha-clause`, ex07 -> vocabulary skill. After applying: `python scripts/lock_tags.py hu b1/rules-rights-responsibilities --update --reason "reader fixes"`.

### 3. Goals / checklists
- The five lessons had the same three of four goal lines ("I can use impersonal rules, future obligation participles (-andó/-endő), and formal conditional clauses.", "I can express legal rights, duties, contracts, and dispute resolution …", "I can appreciate classic Hungarian literature …"), none practised in lessons 1, 3-5 (-andó only in lesson 2, literature only in the consolidation). Rewritten as three lesson-specific lines each, promising only what the items practise.
- No lesson had `srs` or `checklist` sections (units 49-53 have both); added to all six, checklist = goal lines, consolidation checklist one retelling line. challenge `canDo` = first checklist line.

### 4. Doubtful
- b1-28-mikszath: the text calls Gregorics Pál Wibra György's *apja* (and Wibra says *az apám*) although the surnames differ (in the novel Gregorics is an uncle): left as the story says (unsure).
- b1-28-mikszath comprehension question 1 ("Mi a történet központi gondolata?") is generic (the Spanish rules call this a defect); left.
- Lesson 1 vocabulary re-lists nothing, lesson 3 re-lists *engedély* (A2 Unit 23): parked.
- Reading questions in the consolidation are now English-stemmed because story words are not "met" for the checker (unsure of house style; frozen Unit 53 used Hungarian).

### 5. Dictionary
bankutalványok | bankutalvány | noun | banker's draft, bank order |
bankutalványt | bankutalvány | noun | banker's draft, bank order |
csodatevő | csodatevő | adj | miracle-working |
dicsfényes | dicsfényes | adj | radiant, surrounded by a halo |
érő | ér | verb | to be worth; to reach |
felserdült | felserdül | verb | to grow up, reach adolescence |
kitartóan | kitartó | adj | persistent, steadfast |
meggyógyul | meggyógyul | verb | to recover, get well |
mesés | mesés | adj | fabulous, fairy-tale |
roskadozó | roskadozik | verb | to sag, be on the point of collapse |
tisztaságú | tisztaságú | adj | of a (given) purity |
csupaszív | csupaszív | adj | all heart, very kind-hearted |
odakint | odakint | adv | outside, out there |
záporeső | záporeső | noun | downpour, rain shower |

Fix count Unit 55: 68 (48 exercises, 11 goal/checklist, 7 screen texts, 2 story)

## Unit 57 migration-identity (b1-29)

Commands run: check-content (14 ERRORs: 12 length-giveaway, 2 tell-absolute; 4 suspects), render_lesson, unmet-words (149 hits), audit-reader-coverage. Fixes: `fixes-migration-identity.json` (66), challenges: `challenges-migration-identity.json` (6).

### 1. Found by reading
- 48 of the 49 exercises (all but 01.ex09) used unmet words (*repülőjegyet, szállodai, sátor, felverését, fülbevaló, termőföldet, növénytermesztésre, generációról, bankbetét, elvehetetlenek, országhatárok*…) and most wrong options were absurd (*A szállodai szoba lemondását*, *Két személyi igazolványt hord*, *A nehézségekben sétált az utcán*, *miatt alszik a ház*, *dacára esik a hó*, *Visszatekintő ember sétál a járdán*). All rewritten, one `set` per id.
- 12 length-giveaway ERRORs (b1-29-01.ex01/ex06, 02.ex01/ex06, 03.ex01, 04.ex01/ex06, 05.ex01/ex06, consolidation.ex01/ex04/ex08) and 2 `tell-absolute` (*Kizárólag*: 04.ex06, consolidation.ex04): fixed in the rewrites.
- Glued blanks: 01.ex02 (*mi_____*), ex05 (*_____vándorlás*), ex07 (*dacá_____*); 02.ex05, ex07; 03.ex02, ex05, ex07; 04.ex02, ex05, ex07; 05.ex02, ex05, ex07; consolidation.ex02, ex05, ex07: all blank the whole word now.
- Builders: 01.ex03/ex08, 02.ex03/ex08, 03.ex03/ex08, 04.ex03/ex08, 05.ex03/ex08, consolidation.ex03/ex06 had `english` "Build the sentence in the correct order."; real translations now. 01.ex09 is fine (it carries `solutions`).
- b1-29-02-a presents *letelepszik*, which is not a Hungarian verb (it is *letelepedik*; the example even says *telepedett le*); the grammar file title says the same. Fixed (screen text and title).
- b1-29-01-a: *folytán* "usually with instrumental -val/-vel" is false (it follows the plain noun), "preceded by the noun's unmarked or possessive form" misleads; *miatt* and *következtében* (B1 Unit 31) presented as new. b1-29-01-b: "take the possessive or unmarked form" misleads (plain noun); recap *annak ellenére, hogy* (B1 Unit 9) added.
- b1-29-02-b: *miközben* is B1 Unit 4 (`mig-egyidejuseg`): recap; b1-29-03-b: *nemcsak … hanem … is* is A2 Unit 5: recap, *egyszerre … és …* named as the new part; b1-29-03-a: *tartozik* with "sublative -ra/-re" is wrong for "belongs" (that is *-hoz/-hez*), and *-hoz/-hez* verbs are Unit 9.
- Reading questions before the story: b1-29-04.ex04 (*Melyik felvidéki város …*) and ex06 (*Mit jelentett Márai … a magyar nyelv*) ask about the story that appears only in the consolidation. Replaced by a government item (`verb-government-bol-bol`) and a vocabulary item (*emlékőrzés*).
- Unused vocabulary (suspects): *kivándorlás, idegenség, örökség, befogadás* occurred only glued to a stem or not at all; each is now used whole (01.ex05, 03.ex05, 04.ex05, 05.ex08).
- b1-29-05.ex04: Hungarian metalanguage (*határozói igenév*) and an option with a present participle *visszatekintő* that is not a real contrast; rebuilt with infinitive and wrong-case options.
- b1-29-02.ex02 accepts both *le* and *meg* (*megtelepedik* is rare but exists); kept.
- Forms before their screen: none found beyond the above (*-va/-ve* appears only from 05-b on; present participles *élő, eltelő* are Unit 11; *ahol* Unit 10).

### 2. Metadata
- b1-29-03.ex07 and b1-29-04.ex02 (*tartozik, származik*): tagged `present-tense-routine-language`, but the wrong answer (*tartozok*) shows the -ik conjugation: now `ik-verbs-dolgozom-not-dolgozok`.
- b1-29-04.ex04: reading -> grammar, `verb-government-bol-bol`, `distractor_skills` {1: delative-rol-rel, 2: on-en-on}, `stage` "literature" removed; ex06: reading -> vocabulary with the unit vocab skill.
- b1-29-consolidation.ex02: acc-poss -> `concessive-postpositions` (the copy of the speaking line is gone).
- b1-29-01.ex04 keeps {1: causal-postpositions}; consolidation.ex01 {1: concessive-postpositions}; 05.ex04 {1: building-the-infinitive-the-suffix-ni, 2: how-the-accusative-t-works}; 03.ex04 {1: mert-because}.
- After applying: `python scripts/lock_tags.py hu b1/migration-identity --update --reason "reader fixes"`.

### 3. Goals / checklists
- All five lessons carry the same lines "I can use causal and concessive postpositions (miatt, ellenére, folytán, során)." / "I can express complex themes of dual identity, homesickness, and belonging." / "I can appreciate Sándor Márai's masterpiece …", none lesson-specific and mostly not practised. Rewritten (three lines per lesson, each practised).
- No lesson has `srs` or `checklist`; added to all six. `canDo` of each challenge = first checklist line.

### 4. Doubtful
- b1-29-01-a: the sheet gives no unit for plain *miatt* (A2 Unit 40 has *miattam*): recap says "from earlier units".
- Story b1-29-marai: question 1 ("Mi … legfőbb gondolata …") is generic; left. Explanation of question 2 quotes the text loosely; left.
- 04.ex07 accepts *gyermekeiknek* as well as *gyerekeiknek* (unsure *gyermek* is met).

### 5. Dictionary
előretörése | előretörés | noun | advance, rise, breakthrough |
kitörölhetetlenül | kitörölhetetlen | adj | indelible, impossible to erase |
kőtornyának | kőtorony | noun | stone tower |
művészkávéházak | művészkávéház | noun | artists' café |
otthontalanság | otthontalanság | noun | homelessness, feeling of not belonging |
polgárházak | polgárház | noun | bourgeois town house |
teáscsészék | teáscsésze | noun | teacup |
tengerentúli | tengerentúli | adj | overseas |
weimari | weimari | adj | of Weimar, Weimar |
zúgása | zúgás | noun | roar, hum, ringing |

Fix count Unit 57: 66 (48 exercises, 11 goal/checklist, 7 screen texts)
