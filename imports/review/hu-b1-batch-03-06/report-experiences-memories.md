# Reader A: hu b1 experiences-memories (Unit 3) and carpathian-basin-before-magyars (Unit 4)

The harness refused `report-experiences-memories.md` ("Subagents should return findings as text"), so this reply is the only copy of the report.

**Files written in `/home/user/parlour-read-a`:**
- `fixes-experiences-memories.json` (71 fixes, 1 unsure)
- `challenges-experiences-memories.json` (6 challenges)
- `fixes-carpathian-basin-before-magyars.json` (113 fixes, 13 unsure)
- `challenges-carpathian-basin-before-magyars.json` (6 challenges)
- `facts-carpathian-basin-before-magyars.md`

I edited nothing else and touched no git or tool config.

**Checks run:** `check-content`, `render_lesson`, `audit-reader-coverage` per story, and `unmet-words` for both units. I applied both fix lists to a scratch copy of the repo (not the worktree) and ran `check_fixes.py` there. 71 and 113 fixes applied with 0 rejected. check-content went from 17 errors to 0 in each unit, and unmet-words to 0 hits in each. `validate-content.py` fails only on "locked tags changed" for 18 exercises (13 in Unit 3, 5 in Unit 4). That is expected until `lock_tags.py --update` runs after the fixes are applied.

**Before applying Unit 4:** run `python scripts/build_word_lesson_index.py hu`. The new vocabulary entries only count as met once the index is rebuilt.

**Not checked by unmet-words:** it does not read `substitution` and `sentence-order` items, or story questions. I checked those by hand.

---

# UNIT 3: hu b1 experiences-memories (stems b1-02-01 … b1-02-consolidation, story b1-02-hetkrajcar)

## 1. Found by reading

**b1-02-01**
- **b1-02-01-a-gr text:** "only the second one answers 'have you ever been?'". *Voltam Londonban* alone also answers it. Fix: "*már* makes it explicit" (unsure).
- **b1-02-01-a-gr tip:** says *már* is "directly in front of the verb", but its own example *Jártál már Japánban?* has it after the verb. "Not *Már jártál*" is also possible Hungarian. Fix: after the verb in a question, before it in a statement; "that would contradict" softened.
- **b1-02-01-b-gr text:** presents *soha nem* as new; it is A1 Unit 17. Fix: "You know *soha nem* from A1 Unit 17."
- **b1-02-01-intro-1, -controlled-4, consolidation-1:** *soha* appears only in a wrong option (tell-absolute). Fix: *most* / *néha*.
- **b1-02-01-intro-2, consolidation-2:** length give-away, 12 vs 8 characters. Fix: *már soha nem*, *most már nem* (*már soha nem* also gets `distractor_skills` soha-needs-nem).
- **b1-02-01-controlled-1:** *kipróbál* and *megtapasztal* are listed but never tested, and *megtapasztal* is never used. Fix: the matching now tests the four lesson words.
- **b1-02-01-practice-3:** *osztrigát* is in no list. Fix: *halat*.
- **b1-02-01-dialogue-2:** *szörfözni* is unmet in this lesson. Fix: *Kipróbáltad már a halászlét?* (uses the unused *kipróbál*).
- **b1-02-01-check-1:** *próbálsz* unmet. Fix: *Szoktál szusit enni?*

**b1-02-02**
- **b1-02-02-intro-1:** *soha többé* is a tell, and length is 17 vs 11. Fix: *egész életemben*, *még egyszer*.
- **b1-02-02-intro-2:** *bátor* is unmet (taught in b2-16-05). Fix: *boldog*.
- **b1-02-02-controlled-4 and 02-b-gr example:** "hogy … utazzak" is hogy + subjunctive (B1 Unit 5, `hogy-jon-jen`), and *ijedtség* is in no list. Fix: "Egyedül utaztam, és sok ____ kellett hozzá." The screen example becomes "Életemben először utaztam egyedül, és sok bátorság kellett hozzá."
- **b1-02-02-practice-3:** *vitorlázni* is in no list. Fix: *úszni*.
- **b1-02-02-practice-4:** length give-away, 29 vs 22. Fix: *Már jártam Japánban kétszer.* / *Szoktam Japánba járni nyáron.*
- **b1-02-02-dialogue-2:** tell *mindig*, length 43 vs 23. Fix: wrong reply "Igen, tegnap ideges voltam a kihívás előtt." (does not answer the question).
- **b1-02-02-check-2:** *elutazni* is in no list. Fix: *utazni*.
- **b1-02-02-b-gr tip:** "same logic as *odamegy valakinek*" is not Hungarian (it is *odamegy valakihez*). Fix: recap of the A2 Unit 12 -nak/-nek verbs.

**b1-02-03**
- **b1-02-03-a-gr table:** *elveszít → elveszett kulcs* is wrong. *elveszett* comes from *elveszik*; *elveszít* gives *elveszített*. Fix: *elveszik → elveszett kulcs*, "to get lost".
- **b1-02-03-a-gr text:** "Every verb can also work as an adjective" is too strong. Fix: "Many verbs … 3rd-person -t/-tt form".
- **b1-02-03-a-gr tip:** *által* is A2 Unit 18 and is given without a recap. Fix: "from A2 Unit 18".
- **b1-02-03-intro-1:** *készít* is unmet, and both wrong options fail the same way. Fix: *elkészít étel* (present, with `distractor_skills`) and *étel elkészített* (word order).
- **b1-02-03-controlled-4:** *elveszik* is unmet. Fix: *elveszít*, *elveszítettem* (with `distractor_skills`).
- **b1-02-03-practice-3:** *elküldött*, *megkapott* are in no list. Fix: *aláírt*, *feladott*.
- **b1-02-03-dialogue-1:** *felejthetetlen* is never used. Fix: "Felejthetetlen volt, mély benyomást tett rám." / "… tettem rá."
- **b1-02-03-dialogue-2:** *megtaláltad* and *elveszteni* are unmet, and the wrong reply "Nem, holnap fogom elveszteni." is plainly absurd. Fix: *Hol találtad meg a régen elveszett kulcsot?* with "Az asztal alatt találtam meg, tegnap." / "Igen, az asztal alatt …" (an open question answered with *Igen*).

**b1-02-04**
- **b1-02-04-b-gr examples, tip and goal:** *visszatekintve* is an adverbial participle (-va/-ve, B1 Unit 57). Fix: *Ha visszatekintek, érett döntésnek tartom.*, and the tip rebuilt on *Ha visszatekintek, azt látom, hogy minden más volt*. The text recaps -ra/-re from A2 Unit 6.
- **b1-02-04-dialogue-1:** *érettebb* is unmet, and the wrong reply is self-contradictory with tell *egyáltalán*. Fix: "ma már érett ember vagyok" / "… voltam".
- **b1-02-04-dialogue-2:** the wrong reply changes the person twice (*visszatekintesz … voltál*). Fix: "… egészen más lesz."
- **b1-02-04-check-1:** *azután* is unmet and *mindig* is a tell. Fix: *utána*, *később*.
- **b1-02-04-check-2:** *érettebb* is unmet. Fix: blank the listed word *érett* ("Ma már ____ ember vagyok, nem olyan, mint azelőtt.").

**b1-02-05**
- **b1-02-05-gr:** the screen never teaches *minél … annál*, the unit skill `correlative-minel-annal`, although items use *minél*. The table title "New comparison words" lists *mint*, which is A2 Unit 13. Fix: a table row, the example *Minél többször próbáltam, annál bátrabb lettem.*, and a tip sentence. *visszatekintve* in the opening text is replaced too.
- **b1-02-05-check-2:** now tests *annál*.
- **b1-02-05-practice-1 (sentence-order):** *egyedül*, *útnak*, *helyi*, *lakos* are unmet. Fix: sentences rewritten.
- **b1-02-05-dialogue-1:** *önmagadhoz* and *félénkebb* are unmet. Fix: *a régi énedhez képest*; the wrong reply differs only in tense ("… bátrabb voltam.").
- **b1-02-05-dialogue-2:** *út* and *ugyanolyan* are unmet, and the old wrong reply (the trips were equal) could answer the question. Fix: *Melyik utazásod …?*; the wrong reply lacks *mint*; `distractor_skills` removed.
- **b1-02-05-practice-6:** *úthoz* is unmet. Fix: tiles on *az elsőhöz képest a mostani utam izgalmasabb volt* (the file uses `solutions`, so the fix sets `solutions`).
- **b1-02-05-reading-1/2/3:**
  - Unmet words: *krajcárt*, *szappant*, *iskolatáskáját*, *ahogyan*, *megőrizte*, *jókedvét*, *legfontosabb*, *szegénynek*. *vehessen* is hogy + subjunctive (B1 Unit 5).
  - Length give-aways 37/26, 65/37, 81/46, and tell *mindig*.
  - The story never mentions a school bag.
  - reading-3 asked what he "realised looking back", but the answer was the closing reflection. The story says he realised, as an adult, what a challenge it was for his mother.
  - Fix: three new questions on met words.

**b1-02-hetkrajcar story file**
- **Comprehension Q2:** the options drill hogy + subjunctive (*vehessen*, *vásároljon*, *kifizesse*, *vegyen*), and the explanation quotes a sentence that is not in the story. Fix: noun options and the exact quote.

**b1-02-consolidation**
- **b1-02-consolidation lesson title:** "Unit 2 Consolidation" should be "Unit 3 Consolidation".
- **consolidation-6:** *elmúlt* is unmet. Fix: *a régi életemre*.
- **consolidation-7:** *elutazom* is unmet. Fix: *utazom oda*.
- **consolidation-8 (sentence-order):** *sokszor*, *útra*, *asszony*, *egyedül*, *bátrabb* are unmet here. Fix: rewritten.
- **consolidation-9:** *visszatekintve* (-va/-ve), *ijesztő* unmet, length 67 vs 41, and the wrong reply is a plainly absurd future. Fix: *Nehéz volt …* / "… tettem rá".
- **consolidation-10:** *önmagamhoz* and *félénk* are unmet, and *a mai önmagamhoz képest* is unidiomatic. Fix: *A mai énemhez képest, régen ideges voltam.*
- **consolidation-11:** *szusit* is unmet. Fix: *halászlét*.
- **consolidation-12:** *visszatekintve* (-va/-ve) and *bátrabb* unmet. Fix: *Azóta egyre jobban érzem magam.*

## 2. Metadata
- **b1-02-01-dialogue-1:** teaches yes-no-questions → mar-experiential (the replies differ in *már* / *még nem*).
- **b1-02-03-dialogue-1:** teaches present-tense-routine-language → case-inflected-pronouns (the fault is *rám* / *rá*).
- **b1-02-04-dialogue-1:** teaches vocabulary → van-zero-copula, `distractor_skills` {1: van-past}.
- **b1-02-04-dialogue-2:** teaches present-tense-routine-language → van-past.
- **b1-02-04-check-2:** category grammar → vocabulary, and teaches comparative-bb → unit vocabulary (the blank is the listed word).
- **b1-02-consolidation-9:** teaches van-past → case-inflected-pronouns.
- **`distractor_skills` added:** b1-02-01-intro-2, consolidation-2 (soha-needs-nem), b1-02-03-intro-1, b1-02-03-controlled-4.
- **`distractor_skills` removed:** b1-02-03-dialogue-2 (the fog option is gone), b1-02-05-dialogue-2 (the olyan-mint option is gone).
- **After applying:** `python scripts/lock_tags.py hu b1/experiences-memories --update --reason "reader A fixes"`.
- **Unsure, not changed:** b1-02-01-intro-1/2 and b1-02-02-intro-1 ask "which word/phrase means …" about the unit's grammar markers. By the rulebook's "Which means … → vocabulary" they could be vocabulary.

## 3. Goals / checklists
- **b1-02-04 goal, goal section and checklist, line 1:** "using visszatekintve" → "using ha visszatekintek, and say what I am looking back at with -ra/-re". The challenge canDo copies this line.
- **b1-02-04 line 3:** "combine looking-back language with past-participle adjectives in one sentence" is not practised by any item. Fix: "I can answer how much I have changed over the years." (dialogue-1 practises it).
- **b1-02-05 line 1:** a synthesis line that only sentence-order and writing practise. Kept (it is the first line); the challenge target now combines *már*, *először*, *azelőtt*, *azóta*, *egyre*.

## 4. Doubtful
- **b1-02-hetkrajcar:** the text is a loose retelling. As far as I remember, Móricz's *Hét krajcár* ends with the mother crying, not laughing, yet goal line 4 and the summary call it an "adapted classic" (unsure; compare with the original).
- **b1-02-03-a-gr:** *az anyám által elkészített étel* (agent phrase + participle before the noun) is the pattern the sheet lists as B2 `participial-clauses` (unsure).
- **b1-02-04 *visszatekintve*:** if the reviewer accepts it as a fixed adverb, keep the old goal and screen text. I replaced it because Unit 57 teaches -va/-ve (unsure).
- **b1-02-05 example 2, controlled-3, writing-2:** "Egyre bátrabb lettem, minél többször próbáltam …" mixes *egyre* and *minél* without *annál*. Acceptable but heavy; the screen now shows the plain pair beside it (unsure).
- **b1-02-05:** the comma after *képest* ("A mai önbizalmamhoz képest, régen …") is not needed (unsure).
- **b1-02-01-dialogue-1/-2:** the wrong replies (*Igen, még nem jártam*, *Igen, még soha nem próbáltam*) are the typical learner error but self-contradictory. Kept as one-fault yes/no items (unsure).
- **b1-02-03-dialogue-1 and consolidation-9:** the wrong reply swaps the roles (*tettem rá*), which is a person fault. Kept (unsure).
- **Words from a screen's own examples** not in a list (*önbizalom*, *szörfözés*, *kaviár*, *megszeret*) are allowed by the rule and left alone.
- **consolidation-4 and -5** are copies of lesson items; not reported (replays wanted).

## 5. Dictionary (b1-02-hetkrajcar)
asztalfiókokat | asztalfiók | noun | drawer of a table |
fapadlóján | fapadló | noun | wooden floor |
kincsvadászatra | kincsvadászat | noun | treasure hunt |
legkilátástalanabb | kilátástalan | adjective | hopeless, without any prospect |
megfoltozott | megfoltoz | verb | to patch up, to mend with a patch |
mindhiába | mindhiába | adverb | all in vain |
nagymosáshoz | nagymosás | noun | big wash, laundry day |
fogytán | fogytán | adverb | running low (fogytán van: is running out) |
lelkierő | lelkierő | noun | strength of spirit, mental fortitude |

**Unit 3 fix count: 71** (fixes-experiences-memories.json). Challenges: 6.

---

# UNIT 4: hu b1 carpathian-basin-before-magyars (citizenship track)

## 1. Found by reading

The facts file lists every claim with sure/check. Every item below that mentions a story edit or a "check" claim is also there.

**Stories, all five segment files**
- **Reading questions:** the three questions of each story were copies of a1-unit-01's questions (Meg and Károly's table). Fix: 15 new questions, answerable from each story's own text, with new `correctIndex` and explanations.
- **keyVocabulary:** a placeholder (*könyv*, *telefon*, *ház*, A1) in all five. Fix: three real B1 words each.
- **story 02 p2:** "Pannonia tartományt" is spelled differently from "Pannónia" everywhere else. Fixed.
- **story 01 p4:** "meghatározó őslakosai". The Celts arrived c. 4th century BC, so "original inhabitants" is wrong. Fix: "egyik meghatározó népe" (unsure).
- **story 04 p4:** "békében éltek" (in peace) is unsupported. Fix: "itt éltek" (unsure).
- **story 04 p5:** "könnyen beolvadtak" is stated too strongly. Fix: "beolvadtak" (unsure).
- **story 05 p5:** "dicsőséges honfoglalás" is a patriotic judgement. Fix: removed (unsure).

**b1-karpatmedence-01**
- **ex03:** *Kr.e.* is taught on lesson 2's screen, the wrong options (*A 20. században*, *Csak a honfoglalás után*) are absurd, and the date claim is stated nowhere in the lesson. Fix: *Mikor éltek a kelták?* with *Az ókorban.* / *A magyarok után.* / *A hunok után.*
- **ex05:** length 17 vs 10, and *az avarok* is not a Celtic tribe. Fix: *A pannon törzsek.* / *A hunok törzsei.*
- **ex07:** tell *Senki*, length 30 vs 18, absurd *Csak a magyarok*. Fix: wrong options *A hunok és a magyar törzsek.* / *A hunok és a rómaiak népe.*
- **ex08:** *vasmegmunkálással* and *pénzveréssel* are verbal nouns (-ás/-és, B1 Unit 31), and *fejlett* and *rendelkeztek* are unmet. Fix: the sentence follows the story ("fejlett kézművességgel és kereskedelemmel foglalkoztak").
- **Grammar screen:** presents the A2 past endings and the A1 plural verb endings as new. Fix: a recap.
- **Goals 2/3:** the goal on where "Pannónia" comes from and ex02 rest on a fact neither the story nor the screen states. Fix: a new screen example, *A pannon törzsek … róluk kapta a nevét Pannónia.*

**b1-karpatmedence-02**
- **Screen example 1 and its speaking prompt:** "a Dunától nyugatra eső területet" uses a present participle (B1 Unit 11). Fix: "a Duna jobb partját", as in the story.
- **Tip on Kr.e./Kr.u.:** wrong. It says the abbreviations come before the number "just like English BC/AD", but BC follows the year in English. It also claims an exception to Hungarian word order. Fix: rewritten.
- **ex05:** length 82 vs 46, *érkező* is a present participle, *nyomást* is unmet, and the story gives a different reason. Fix: "Mert a birodalom meggyengült."
- **ex07:** tell *Egyáltalán* and absurd *Csak öt évig*. Fix: *Körülbelül száz évig.* / *Közel ötven évig.*
- **ex08:** the hot-springs claim is doubtful and *forrásai*, *gyógyfürdő*, *alapját* are unmet. Fix: a story-based sentence, "Aquincum a Duna partján volt, a mai Óbuda helyén."
- **ex03:** *Savaria* is in no list. Added to the vocabulary.

**b1-karpatmedence-03**
- **Screen example 1 and speaking:** "keleten más népek éltek a medencén kívül". The east (Transylvania, the Plain) is inside the basin. Fix: "a medence keleti részén".
- **Screen example 2 and speaking:** "másfél évszázadig" contradicts the lesson's own ex05 (two and a half centuries). Fix: duration removed.
- **Tip:** the skill is "míg and miközben" but *miközben* is never taught, though the story uses it. Fix: a tip sentence.
- **ex02:** *rómaivá* and *erősödött* are unmet. Fix: plausible wrong options.
- **ex04:** *központi*, *maradékát*, *próbálták* are unmet and the claim is vague. Fix: the lesson-4 style sentence on met words.
- **ex05:** "Avar Kaganátus" is not a word of the story, and "közel két és fél évszázadig" is imprecise and contradicted the screen. Fix: *Meddig uralkodtak az avarok …?* with *Több mint két évszázadig.*
- **ex06:** "Slavs lived on the periphery" is not in the story. Fix: "Slavic groups settled along the rivers" (story p4); *peremvidéken* was unmet.
- **ex07:** the wrong options are plainly unrelated and full of unmet words (*újkori*, *telepesek*, *tengerentúlra*, *iparosodást*, *kísérő* = participle). Fix: periods that did happen.
- **ex08:** *létrehoz*, *vezetésével* (verbal noun) and *hatalmas* are unmet. Fix: rewritten on met words.

**b1-karpatmedence-04**
- **Screen example 2:** míg means "until" here, and the Goths come before the Huns (story 3 has the Huns first). It sits in the simultaneity lesson. Fix: replaced by a simultaneity example.
- **Screen example 3:** *formáltak önálló közösségeket* is vague (unsure).
- **ex02:** *egymást követő* and *élő* are present participles (B1 Unit 11), *teljesen* is a tell, and the claim is shaky. Fix: rewritten.
- **ex03:** *erősödött*, *egyesült* unmet. Fix: met words.
- **ex05:** *teljesen* tell, *amelyeket* (accusative relative, B1 Unit 21), length 80 vs 43. Fix: *Helynevekben és régészeti leletekben.* / *Egyetlen nyomuk sem maradt meg.* / *Csak a római városokban.*
- **ex06:** factual error. The Slavs were not in the east while the Romans ruled Pannonia (they arrived in the 6th century). Fix: "other peoples".
- **ex07:** "no people ever ruled the whole basin before the honfoglalás" is doubtful, because the Avars ruled most of it for over two centuries. It also has tells *mindig* and *örökre*, and length 68 vs 42. Fix: now about the end of the 9th century, as story 4 says (unsure).
- **ex08:** *megtalálható* (-ható) and *táj* unmet. Fix: *látszik* / *vidék*.

**b1-karpatmedence-05**
- **ex02:** *egymást követő* is a participle, and the answer "no earlier people could unify it" contradicts the Avar rule; length 74 vs 39. Fix: the story's reason, "sok nép és helyi uralkodó élt egymás mellett".
- **ex03:** duplicates 04.ex03, and the wrong options are absurd. Fix: *Hol éltek a magyarok a honfoglalás előtt?* (story p1).
- **ex04 and consolidation ex11:** "hogy új hont keressen" is hogy + subjunctive (B1 Unit 5). Fix: *… elindult keletről.*
- **ex05:** *sűrűn*, *nagyvárosokkal*, *teli*, *füves* unmet. Fix: plain options.
- **ex06:** *felé* is B1 Unit 15 (`postposition-fele`), *hágói* is unmet, and the passes are tradition, not in the story. Fix: *hegyeken át érkeztek*.
- **ex07:** long wrong options with many unmet words. Fix: rewritten.
- **ex08:** hogy + subjunctive. Fix: *elindult új hazát keresni*.
- **Screen example 2:** míg joins non-simultaneous events (the Roman withdrawal and the later Migration Period). Fix: *majd … míg szláv csoportok a folyók mentén telepedtek le*.

**b1-karpatmedence-consolidation**
- **Lesson title:** "Unit 2 Consolidation" should be "Unit 4 Consolidation".
- **ex04:** tell *mindig*/*soha*, unrelated word lists. Fix: the same words in the wrong order.
- **ex05:** length 62 vs 32, wrong options are word salads. Fix: full sentences with one fault each (position of míg, tense).
- **ex06:** factual error (Huns and Slavs side by side) and *élve* is -va/-ve (B1 Unit 57). Fix: Avars.
- **ex09:** *központját*, *uralták*, *peremeken* unmet, and the claim is not in the story. Fix: the lesson-4 style sentence.
- **ex12:** *uralták* unmet, "the Celts ruled the region" is shaky, and the item is tagged definite-past but uses *éltek*.
- **ex14:** hogy + subjunctive. Fix: *… elindult új hont keresni.*
- **ex15:** tell *Senki* and absurd wrong options.
- **ex16:** participles *egymást követő* and *harcoló*, the Avar contradiction, and length 50 vs 33. Fix: the end of the 9th century.

**Vocabulary (citizenship rule: keep the real history words)**
- **Added:** every word that unmet-words reported and the items rely on, to the vocabulary list of the first lesson that uses it.
  - 01: *közé, római, pannon, Pannónia, fejlett, kézművesség, kereskedelem, foglalkozik*
  - 02: *Savaria, meggyengül, század*
  - 03: *amíg, időszak, halál*
  - 04: *összeomlik, régészeti, lelet, uralkodó, egyetlen, látszik, vidék, más*
  - 05: *helyi, lovas, legelő, nyílt, elfoglal, kelet, kor*
- **Duplicates:** *kereskedelem* is listed in lessons 1 and 2.
- **pos for names:** the schema rejects "proper noun", so the entries for *Pannónia* and *Savaria* use `"noun"`.

## 2. Metadata
- **b1-karpatmedence-01 … 05 `.ex07`:** dialogue-complete items tagged category reading with no skill. Fix: category dialogue, teaches the unit vocabulary skill (unsure; the consolidation's equivalents are already dialogue + vocabulary).
- **consolidation.ex12:** teaches definite-past → past-tense-indefinite (it uses *éltek*).
- **Left unchanged, doubtful:**
  - The fact items (`ex02`, `ex03`, `ex05` and similar) are tagged `reading` without a skill, so the learner model does not track them. If they should count, tag them with the unit vocabulary skill.
  - consolidation.ex03 has `distractor_skills` {2: present-tense-routine-language} for *letelepedik*; `ik-verbs-dolgozom-not-dolgozok` is closer (unsure).
- **After applying:** `python scripts/lock_tags.py hu b1/carpathian-basin-before-magyars --update --reason "reader A fixes"`, and rebuild the word index.

## 3. Goals / checklists
- **b1-karpatmedence-01 goal 1:** "name at least three peoples … including the Celts". The lesson names only the Pannonian tribes and the Celts. Fix: "name two peoples … the Pannonian tribes and the Celts" (all three places; the challenge canDo copies it).
- **b1-karpatmedence-02 goal 2:** "at least three Roman cities". Story and items name two. Fix: "two Roman cities in Pannonia, Aquincum and Savaria, and say where they are today".
- **b1-karpatmedence-04 goal 2 and consolidation goal 3:** "no single people controlled the whole basin before 895" is wrong, because the Avars did for two centuries. Fix: "no single ruler controlled the whole basin at the end of the 9th century".
- **b1-karpatmedence-05 goal 3:** "why it happened around 895". The lesson does not explain why. Fix: "when it happened".
- **b1-karpatmedence-05 goal 4:** "without narrating the crossing itself" described what the lesson avoids. Fix: "I can say that the Magyar tribal confederation set out from the east to find a new homeland."
- **Challenges:** the placeholder challenges are replaced with six "At your naturalization interview" entries, one per lesson. The canDo lines are the first checklist lines after the fixes. The targets avoid *gótok* and *korában*, which the lexicon cannot resolve (see section 5).

## 4. Doubtful
- **Disputed or overstated, named as "check" in the facts file:**
  - 895 as the date, and the Verecke pass route.
  - The "empty basin" idea (story 5 p3).
  - The order "first the Huns, then the Goths" (story 3 p2/p3).
  - The Migration Period beginning after the legions left (story 3 p1).
  - The Danube frontier reached in "the 1st century AD" (story 2 p1).
  - Viticulture and "forever" (story 2 p4/p5).
  - Aquincum as a "founding around AD 9" (it began as a camp c. 89).
  - The reason for the Roman withdrawal.
  - "Illyrian-related" Pannonians.
  - Spelling *Kr.e./Kr.u.* (standard is *Kr. e.*, *Kr. u.*).
- **L4 screen 04 and L5 screen 05:** they present no new grammar and the lessons carry little teaching. The míg skill is practised, but míg is used with an "until" sense in places (fixed where found).
- **Kept as is:**
  - 02.ex03 is a negative question ("Melyik város NEM …").
  - The listening items (`ex08`) have absurd English wrong options.
  - The avar/frank/hun peoples appear only as distractors in some items.
- **amikor:** *Az az időszak, amikor …* (03.ex07) and *Azt, amikor …* (05.ex07) use *amikor* as a relative after a noun or demonstrative. Unit 1 teaches *amikor* for an era, but the general `ahol-amikor` is B1 Unit 10 (unsure).
- **Unit 4 vocabulary:** adding the ordinary words *vidék*, *más*, *kor*, *egyetlen*, *időszak* to the lists is a judgement call; they are plain words, but the unmet-words script reports them.

## 5. Dictionary (story audit)
erődített | erődít | verb | to fortify |
fémmegmunkálással | fémmegmunkálás | noun | metalworking |
őslakosai | őslakos | noun | native, original inhabitant |
kőépítészet | kőépítészet | noun | stone architecture, stone building |
szőlőtermesztés | szőlőtermesztés | noun | viticulture, grape-growing |
terjeszkedett | terjeszkedik | verb | to expand |
Kr. | Kr. | expression | abbreviation of Krisztus (Christ), as in Kr. e. / Kr. u. = BC / AD |
gót | gót | noun | Goth, Gothic |
harcias | harcias | adjective | warlike, martial |
sztyeppékről | sztyeppe | noun | steppe |
népvándorlás | népvándorlás | noun | the Migration Period, great migration of peoples |
törzsszövetség | törzsszövetség | noun | tribal confederation |

Two lexicon problems found while checking, not on the audit list:
- *gót* and *gótok* have no dictionary reading at all, so after the import *gótok* resolves.
- *korában* resolves only to the adjective *kora* ("early"), not to *kor* ("age, era"), which is why the challenge targets avoid it.

**Unit 4 fix count: 113** (fixes-carpathian-basin-before-magyars.json). Challenges: 6.

---

**Fix counts: Unit 3 = 71, Unit 4 = 113.**