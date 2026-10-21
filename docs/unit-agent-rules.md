# Unit agent rules (one sheet)

The only rules file a unit agent (Sonnet reader, regenerator or fixer) reads.
It condenses `docs/unit-finish-brief.md`, `docs/course-generation-brief.md`
§ 2/6/7, `AGENTS.md` § "Exercise metadata" and `docs/skill-tagging-spec.md`
§ "Read-through conventions", plus every defect reviewers keep finding.
Open those files only to settle a point this sheet doesn't cover.
Maintained by the reviewer (Claude) at each process review
(`docs/unit-pipeline-log.md`); a new recurring defect goes into § 6 the
same day.

## 1. Met words and forms

A word or form is **met** when it is in a vocabulary list, or is the subject
of a grammar screen, at or before the lesson. A lesson may also use whole
phrases from its *own* grammar examples. A word seen only in another
lesson's example, a tip or a story is not met. This applies to exercises
(prompts, right answers, wrong options) and challenge targets. **Stories
are exempt:** they should be a little challenging, and the learner taps
unknown words in the Reader (user, 2026-10-13). `check-content.py` (`unmet-word`, A1–A2 in every
course) checks lemmas, not forms: a form taught later (*-ba/-be*, *-on*, plural
possessed *-im*, a noun possessor *Anna kulcsa*) is yours to catch.
`skills/<lang>.json` `taught_in` says where each grammar skill is taught.
When your prompt gives a knowledge sheet (`scripts/prior_knowledge.py`),
use it for what earlier units taught instead of opening them; anything on
it is known and is never presented as new.

## 2. Exercises

1. Exactly **one right answer**. Watch for "wrong" options a native would
   accept: elliptical replies (*Harminc éves.* to *Hány éves vagy?*),
   the other order of a free word order, *és* where *de* is wanted with
   only the English to pin it.
2. Each wrong option breaks **exactly one thing**, the thing the item
   tests. Not two (*Ő Meg van*: person and copula), not by meaning alone
   (*Nagyon kedves vagyok.* as a reply about grandma), not two options
   failing the same way (two negatives where an affirmative is wanted).
   A wrong option is a real phrase or form, or a single-fault non-word.
3. No give-aways: correct option ≤ 1.3× the longest wrong one (checker);
   no option mentioning something absent from the prompt (*The chair.*
   when the sentence has a door and a window); no answer copied from the
   question; no wrong option ruled out by the prompt's *Igen/Nem*.
4. Dialogue replies answer the line before. "Which line comes before?"
   items never offer the reply itself.
5. Fill-blanks: blank a **whole word**. Never glue a blank to a stem
   (*hálószoba____* + *ban* teaches *hálószobaban*: final *-a/-e*
   lengthens). `hint` only when the blank can't be recovered, never the
   answer, names the person for person-marked forms (*live, I*). `english`
   on every fill-blank and builder, fitting only the right answer;
   `answers` (an array that replaces `answer`) lists every correct
   alternative (*Hová* / *Hova*). The grader ignores case and
   punctuation.
6. Builders produce a natural sentence, not a bare noun phrase.
7. Vary items: no three items of the same shape in one lesson, no list
   entry repeated in a vocabulary file.

## 3. Metadata

Examples are Hungarian; the rules hold for every course (Spanish: a choice
between *yo/tú/él* or *este/ese/aquel* is that paradigm's grammar skill;
*ser*/*estar* choices are the skill the wrong answer shows).

- `teaches`: exactly one slug, the skill **a wrong answer shows**. Tested
  form → its grammar skill; tested word → unit vocabulary skill
  `<level>-<unit id>-vocab`. Required unless `category` is `reading`.
- Word meaning (Which means…, matching, a fill-blank supplying a noun, or
  a bare pronoun or question word: *ki*, *mi*, *ő*) → vocabulary. Matching is
  always vocabulary. An inflected pronoun or question word (*kivel*, *vele*,
  *neki*, *hova*) is a form: it keeps the skill of its ending
  (`verb-government-val-vel`, `case-inflected-pronouns`, …).
- A choice between paradigm members (*én/te/ő*, *ki/mi*, number words) →
  that paradigm's grammar skill; a choice between whole sentences differing
  in a form → that form's skill.
- A choice between harmony variants of one suffix (*-ban/-ben* only) →
  `vowel-harmony`; with a missing-suffix or lengthening option, or a
  fill-blank producing the whole word → the suffix's own skill.
- `category` follows the tag on choice, fill-blank and builder items;
  dialogue-complete, structured-writing and listening keep theirs.
- Dialogues: wrong replies answering a different question → unit
  vocabulary; differing in a form → that form's skill; a *Nem, …* that
  affirms → `yes-no-questions`.
- `distractor_skills` (by 0-based option index): only for a wrong option
  that is a **well-formed** form of **another** skill (*három székek* →
  `plural-nouns-k`). None for an ungrammatical option (*a nagyok asztalok*,
  *Itt nem lámpa.*), none for a wrong form of the tested skill itself.
  Whenever an option changes, re-check its entry. The entry goes on the
  option that *is* the other skill's form (*Nincs kulcs.* → `van-and-nincs`),
  never on a wrong form of the tested skill (*Van kulcsom.* for "I don't
  have a key"). Fix lists naming an option index quote the option's text;
  check that the text matches before editing.
- Review items keep the skill they review. Open writing → unit vocabulary.
- After any tag change: `python scripts/lock_tags.py <course>
  <level>/<unit id> --update --reason "..."`. The skill list is frozen: never edit
  `skills/*.json` or generated registries; if no skill fits, report it.

## 4. Screens, story, challenges

- Grammar screens: each lesson has its own two; the rule must be true and
  match its examples; a replacement example follows the rule the screen
  states; exceptions are named as such (*könyvek*, *régiek*, *anyja*);
  no comparisons with languages other than English; a recap states what
  the earlier unit actually taught.
- Story: natural lines (no odd negative questions); narration matches the
  lines. HU A1 comprehension questions are in Hungarian with `questionEnglish`
  and `optionsEnglish` (same order as `options`) on each question; the
  Reader shows an English toggle.
- Glosses read right to an English speaker (*terem* = "large room", not
  "hall").
- Challenge per lesson in `content/<course>/curriculum/challenges.json`:
  one scenario with the story's people, nobody else answers for the
  learner, the scenario mentions what the target talks about; cues say
  what to include, never the words; target answers the prompt with met
  words, 1–3 sentences at A1; "yours" in the prompt only when the target
  is *a tiéd* (for *az enyém* write "mine"); `canDo` = the lesson's first
  checklist line, copied. Every lesson's checklist and goal lines are its
  own; goals promise only what the lesson practises.

## 5. Process rules

- Work only in your assigned folder. Never disable or bypass git hooks
  (`core.hooksPath`, `--no-verify`) or change git/tool config; if a hook
  blocks, fix its cause or stop and report its output.
- Edit JSON text in place, keeping each file's formatting; don't change
  `id`, `type`, `stage`.
- Commands: `python scripts/check-content.py <course> <level> <unit id>` (fix every
  error; suspects fixed or accepted with a reason);
  `node scripts/render_lesson.js <course> <stems>` (read every screen; `!!`
  lines are errors; substitution items showing `[object Object]` is a known
  render-script issue); `node scripts/audit-reader-coverage.js <course> --story
  <story stem> --top 0` (it names every "literal compound guess" word:
  report each with a gloss, `word | lemma | pos | gloss |`, for
  `scripts/fill-dictionary-gaps.py import`; the gloss is the lemma's
  meaning, never the inflected form's, as it is stored under the lemma); `python scripts/validate-content.py --changed`.
- Parked, don't report or fix: sentence-builder alternative orders
  (ROADMAP 148(b)); vocabulary lists re-listing earlier words.

## 6. Defects found before (check each one)

Read § 6a and the section for your course.

### 6a. Any course

Taught misspelling via a glued blank · words from a later unit in options or
challenge targets (*szép* before a1-32, *kérem* before a1-65) · repeated
screens or checklists across lessons · duplicated vocabulary entries ·
`distractor_skills` left on a replaced option · `ds` on an ungrammatical
option · two right answers through ellipsis · a recap screen contradicting
its unit · comma splices in goal/checklist/canDo · scenario not mentioning
the target's object · lesson titles using forms not yet taught (*dolgaim*) ·
a verb whose meaning needs an object not yet taught (*hallgat* alone = "is
silent") · false spelling claims (*hova* and *Hová* are the same word) · a
screen rule its own tip contradicts · an English gloss that lets two verbs
or conjugations fit ("take" for *kérem*/*veszem*: write "buy") · a question
in reported speech ("Anna asks Meg where she is going") that lets the
third-person option fit: quote the direct question · a screen presenting a word or
form an earlier unit taught as new (check `taught_in` and the earlier
screens; say "You know …") · a consolidation item copying a lesson item
(vary the words) · a wrong option whose fault is the person, not the form
the item tests · a grammar pattern taught in a lesson but tagged with a
neighbouring skill (a2-140's hypothetical *ha* was tagged `nek-conditional`
while its skill sat at B1): check that the pattern's own skill is taught
where the lesson teaches it · a review unit's screens presenting the units
they review as new (open with "You know … from Unit N") · a story or
comprehension question drilling a B1 form (*megkérte volna*): stories are
exempt from met words, not from the level · Wrong options and fixes: a wrong
option must be a real error of one kind, not a second option with the same
fault (*Látlak nem* / *Látlak téged nem*) · Text fixes in JSON: escape a
double quote inside a string (`\"`); `apply_replacements.py` refuses a fix
that leaves invalid JSON · "You know … from Unit N": N is the unit number in
`content/<course>/curriculum/units/<level>.json`, not the lesson number
(a2-13 is in Unit 3, a2-105 in Unit 21; A1 material: "from A1"). Readers in
units 39–44 wrote "from Unit 13" for a2-13 · A hint naming the tested ending
(*buli + -ra*, *anya + -nak/-nek*) gives the answer away: name the word and
its role (*buli, for*); `check-content` flags it at A1–B1 (`hint-suffix`;
unit 47 had six) · A new unit that recaps an earlier one must check the
earlier screens for the same chunks: unit 47 presented *Boldog névnapot!*,
*Isten éltessen!* (a2-184, Unit 37) and *meghívlak vacsorára* (a2-189, Unit
38) as new.

### 6b. Hungarian

*-ba/-be* before a1-56 · *utcában* for *utcán* · harmony rule misstated
(*fürdőszoba*, *i* as a front vowel) · *az a* + noun (not taught in A1) ·
plural possessed (*könyveim*) at A1 · *is* before a1-80 · *kell* glossed
"must" · Readers' wrong Hungarian (HU A2): *amit olvasok* is right (a
relative *amit* takes the indefinite verb; never "fix" it to *olvasom*);
*ki* as a relative (*kollégám, ki …*) is literary-correct, so never use it
as a wrong option; *Szabad vagy foglalt vagy?* is natural · *fog* +
infinitive word order: with nothing in focus the infinitive comes first
(*valószínűleg pihenni fogok*, not *valószínűleg fogok pihenni*); *fog*
comes first only when a focused word sits right before it (*Holnap fogok
dolgozni*) · *meg-* is a perfective prefix, not a definiteness marker
(*Vettem a kabátot* is right) · *El nem fogok menni* is acceptable emphatic
Hungarian, so never use it as a wrong option · Plural possessed (HU A2):
a2-13 teaches only the 3rd person singular (*szülei*, *testvérei*);
*-aim/-eim*, *-aid*, *-aink*, *-aitok*, *-aik* first come in a2-191, so
don't use them earlier (*barátaim*, *szüleimet*, *tetteinkért*, *szavaidat*
were found in units 35–38) · *segít* takes the dative (*segítek neked*):
*segítelek* is not standard, never teach it as a -lak/-lek example · A
foreign character keeps their own name order in Hungarian (*Carlos García*);
only Hungarian names go family name first · Time *-ig* at A1–A2 is known,
not a B1 defect (user, 2026-10-15): *-tól … -ig* is taught in a1-154, and
time words such as *sokáig*, *estig*, *vasárnapig*, *három hétig* are
accepted; flag *-ig* only for a spatial end-point (*a hídig*) or when a
screen presents it as new (`terminative-case-ig` is B1) · B1 participles
hide in everyday service language (units 42–44 had ~40): *lévő*, *kapott*,
*megadott*, *felírt*, *lepecsételt*, *vitatott*, *nyomtatott*, *-va/-ve*
(*belépve*, *felírva*), *-andó* (*tárolandó*, *elzárva tartandó*). Use a
finite verb or drop the modifier. A fixed word that a lesson lists in its
vocabulary (*fájdalomcsillapító*, *lázcsillapító*, *szopogató*, *kapható*,
*ellopott*) is A2 vocabulary, not a defect (user, 2026-10-15); forming
participles from verbs stays B1 · Plain *X miatt* is A2 (user, 2026-10-15):
taught with *miattam* on a2-199-a as a postposition; before a2-199 it is a
defect, after it known. `causal-postpositions` (B1) covers *emiatt* and
*következtében* · A word listed in a lesson's vocabulary with its case
(*büszke valamire*, *vigyáz valamire*) is an A2 chunk (user, 2026-10-15);
the general verb-government pattern (`verb-government-ra-re` and siblings)
stays B1, so don't drill new verbs with it · Experiential *már* ("Have you
ever …?": *Foglaltál már asztalt online?*) is B1 (`mar-experiential`); at A2
ask *Mikor …?* or use *már* = "already" with a plain past fact.

### 6c. Spanish (es-es, es-latam; written 2026-10-16 before the Spanish pass, from the files and ROADMAP 148/150; add what the pass finds)

- **es-latam has no *vosotros*** (AGENTS.md): no *vosotros*/*os* forms in
  readings, screens, examples, exercises or challenges; *ustedes* for
  plural "you" (`check-content` flags it: `latam-vosotros`). Only the verb
  drill may keep *vosotros* for recognition. es-es teaches both.
- **Course variants are deliberate:** each course uses its own words
  (user, 2026-10-16; `scripts/course_variants.py`, check `course-variant`):
  es-es *zumo, coche, ordenador, móvil, patata, billete, camarero, salón*;
  es-latam *jugo, carro, computadora, celular, papa, boleto, mesero, sala*.
  es-latam also accepts *tomar* beside *beber* and has *ustedes* tables
  without the *vosotros* row; **es-latam has no *vosotros* at all**, not even
  as a wrong option or in a screen's aside ("except *nosotros* and
  *vosotros*" is es-es only). A fix to such a line is per course: mark it
  `"variant": "es-es"` (or `"es-latam"`) in the fix JSON so it is not
  mirrored, and give the other course its own fix.
- **Forms before their screen** (`taught_in` in `skills/es.json`; the
  knowledge sheet's "later" list): past tenses are A2 (`preterito-perfecto`
  a2-01-01, `preterito-indefinido` a2-11-01), yet *ayer* sentences occur in
  A1; *gusta/gustan* before a1-gustar-01. **Unit order (2026-10-16):**
  `numbers-time-schedules` moved from Unit 14 to Unit 6 (numbers and clock
  times before daily routine, home, supermarket and café use them); Units
  6–13 became 7–14 (daily routine 7, reflexives 8, home 9, supermarket 10,
  demonstratives 11, café 12, birthdays 13, kitchen 14). `numbers` is taught
  in a1-12-01 (Unit 6), `telling-time` in a1-12-03; birthdays' a1-10-02 age
  screen recaps numbers. Unit numbers in this sheet's older notes are the
  old ones where marked. Use `scripts/move_unit.py` for any later move.
- **Prerequisite order (resolved by the user 2026-10-16):** the five A1
  requirements taught out of order were dropped (`adjective-agreement` ←
  `plural`, `doler` ← `gustar`, `hay` ← `estar`, `ser` ←
  `subject-pronouns`, `tener` ← `present-tense`). *doler* (Unit 21) now
  explains its own pattern and *gustar* (Unit 22) opens "You know this
  pattern from *doler* in Unit 21": a screen presenting that pattern as new,
  or calling it "like *gustar*" before Unit 22, is a defect.
- **Function words count as met** (articles, prepositions, conjunctions,
  clitics, *muy/más/ya/tan*: Spanish vocabulary lists leave them out;
  `scripts/unmet-words.js` FUNCTION_WORDS). Every other word must be met:
  a word in **no** vocabulary list (*otro*, *durante*, *alguien*) is
  **added to the vocabulary list of the first lesson that uses it**, with
  its gloss (user, 2026-10-16); a word listed only in a later lesson is
  an unmet word as in any course (replace it, or the use waits).
- **English inside a target-language line is a defect** (user,
  2026-10-16): an instruction before a colon ("Complete the greeting:
  Buenos ___."), a bracketed stage direction ("(Meg answers about her own
  sister.)"), a scene line before " / ". TTS reads it in the Spanish
  voice. Context goes in `hint` (fill-blank and dialogue-complete show it
  in brackets) or `english`; `check-content` errors on it
  (`english-in-target`). The 81 items per course in A1–A2 were fixed
  2026-10-16 (`scripts/fix_english_in_target.py`). **A multiple-choice
  item takes neither `hint` nor `english`** (the schema rejects both:
  units 2–5 and 6–11, seven items): put the meaning in the question and
  make the options whole sentences ("My mother is calm. Which sentence
  says this?" / *Mi madre es tranquila.*); `check_fixes.py` now rejects
  such a fix.
- **Character facts** in challenges and items match the stories (Meg is
  from South Africa, *No soy de España*; Carlos from Hungary, in Hanoi;
  Daniela is the new teacher in story a1-03; Meg's sisters are Lauren and
  Kaylee; Carlos has one brother and one sister): unit 1's first draft
  made Meg Spanish. **Reading questions** must be answerable from the
  story as written: units 4 and 5 had seven that invented scenes (a video
  call), people's roles or traits (2026-10-16). From units 6–11: Carlos
  wakes at eight and goes to bed at ten, Daniela wakes at six and works at
  a school (story a1-06); Carlos's new flat has the kitchen on the right,
  the bathroom opposite and his bedroom upstairs (a1-07); Carlos's mother
  lives in Budapest (a1-05); at the café Meg has green tea, a salad and a
  chicken sandwich, Carlos a black coffee, mineral water and chocolate
  cake, and Carlos asks for the bill (a1-02); Meg buys the silk bag as a
  gift for Lauren (a1-demonstrative). Units 6–11 had six items against
  these (Carlos *se levanta temprano*, *a las siete*, *a medianoche*; the
  bathroom *al lado de la cocina*; *¿Dónde está tu madre?* / *en la sala*;
  "Tacos." as Meg's order).
- **Found in units 2–5 (2026-10-16), each now a `check-content` check:**
  a blank glued to a stem (*simpátic__* + *a*: blank the whole word, hint
  the masculine base; `glued-blank`); a speaker talking about themselves in
  the third person (Carlos asked "¿Cómo es Carlos?", Meg answering "Meg
  es…"; `self-third-person`); a one-word English gloss in brackets in a
  Spanish line or choice question (*(older)*, *(brothers)*;
  `english-in-target`). Also seen: wrong options with two faults (*Es
  divertido y amables.*), garbled non-phrases as wrong options (*Porque
  grupo.*), *está* (estar, now Unit 9) used before its unit, *este/esta*
  (demonstratives, now Unit 11) taught as new in Unit 5, and structured-writing
  prompts that don't pin their one stored answer ("Describe a woman" →
  pin it: "Say that Lauren is funny.").
- **Found in units 6–11 (2026-10-16; old numbers, now 7–12):** a fill-blank's `answers`
  accepting other verbs than its `english` (*I work at home* accepting
  *estudio*, *cocino*, *como*: 13 items, check `answers-alternatives`);
  a wrong option that is a natural right answer (*Tiene una cocina y un
  baño.* to *¿Qué hay en tu casa?*, *Sí, tiene un jardín.*, *Mi madre está
  amable.*); demonstratives answered from the wrong place (the seller says
  *esta bolsa*, so Meg takes *esa*); *gusta*, stem-changing forms (*me
  despierto*, *se acuesta*), *está*, numbers (*siete*, *diez*, *once*) and
  clock times (*y media*) before their units; the personal *a* (Unit 24)
  in Unit 7 (*Despierto a mi hijo*); *jugo* and *ordenar* (Latin American)
  in es-es stories (mark the fix `"variant": "es-es"`); story metadata left
  as placeholders: `keyVocabulary` *conocer*/*intercambio* in most A1
  stories (`story-key-vocab`), es-latam comprehension questions copied from
  another story in 26 A1 stories (`story-questions-copy`; nobody reads
  es-latam stories unless the reviewer does), Daniela's narration voice
  "male" (`story-voice-gender`). A recap screen in the next unit must say
  "You know …": Unit 7 presented Unit 6's reflexive verbs as new, Unit 8
  the articles of Unit 3. Fixing a listed word's only items leaves it
  unused (`vocab-unused`), and retagging items can leave a vocabulary skill
  under 6 exercises (`validate-content.py --warnings`; Unit 10).
- **Found in units 13–18 (2026-10-21):** reading questions about "the
  character" or the text type ("What kind of text is the story?", "the
  diary"), in five of six units: the story is a dialogue between named
  people, so ask what they say and do (`reading-generic`, 13 hits); usted
  and subjunctive forms (*corte*, *mezcle*, *mezcles*, *Coma la
  ensalada.*) and negative commands (*No cortes*) as wrong options in the
  Unit 14 imperative lessons: they are A2 forms, and a correct usted
  command is a second right answer; an infinitive option (*Primero, cortar
  los tomates.*) is a normal written recipe instruction, so it is a right
  answer too; *hay que* used in the *tener que* lesson before its own
  screen (a1-work-03), *ir*/*voy*/*vamos* (Unit 16) and *ir a* +
  infinitive (Unit 25) in Units 13 and 15, *venir* (no A1 list before
  Unit 24) in Unit 16; weather items tagged `ar-verbs` whose wrong options
  differ only in the weather phrase (*Está calor*): every wrong option
  must show the tagged skill's fault; *Hace nublado* is regional, so use
  *Es nublado* as the wrong option. **New skill `present-irregular-yo`**
  (user, 2026-10-21): *hago*, *pongo*, *salgo*, taught in a1-kitchen-02
  (Unit 14); an item whose wrong answer is a wrong yo form (*salo*,
  *haco*) gets this tag; before Unit 14 these forms are before their
  screen.
- **Found in units 19–24 (2026-10-21):** infinitive wrong options that
  are natural replies or advice (*Leer en casa.* to *¿Qué haces?*,
  *Descansar y tomar agua.* to *¿Qué hago?*; 20 items; check
  `infinitive-reply`): make the wrong option another person (*Lee en
  casa.*); usted commands (*Tome una pastilla*, A2) at the pharmacy: use
  *hay que* + infinitive (Unit 18); *poder* (*puedo*, *podemos*) before
  Unit 24: the `querer-poder` screen a1-08-03 (Unit 10) teaches only
  *querer*, so *poder* is new in a1-abilities-01 (the knowledge sheets
  list it as known: don't trust that line); subjunctive and conditional
  forms in options and stories (*duela*, *Que te mejores*, *me
  encantaría*); preterites in stories (a1-16 *fui*, *recetó*); words in
  no list (*clínica*, *mexicana*, *picante*, *latina*, *venir*); unmet
  Spanish metalanguage in multiple-choice question stems (*¿Cuál opción
  es correcta…?*, *oración*): `unmet-word` doesn't read MC question
  stems, so read them; ask in English. es-latam has no *pedir* in A1
  lists (es-es lists it in a1-cafe-04): an item using it in es-latam
  needs the word listed there.
- **Character facts set by the user (2026-10-21), every level from A1:**
  Carlos works in an office from the first story on (he studies Spanish at
  the language exchange; he is not a student and never starts a "new" job);
  Meg is a student; from the end of A1 (story a1-20) Carlos and Meg are a
  couple, and A2 and later treat them as one (a2-06: they move in
  together). A story, item or challenge that contradicts this is a defect
  (A2 to check: a2-educacionyestudios has Carlos accepted at a university).
  es-es says *fuera*/*dentro*, es-latam keeps *afuera*/*adentro* (user,
  2026-10-21; `course-variant` flags *afuera*/*adentro* in es-es). *poder*
  is taught with *querer* in a1-08-03 (Unit 10), so it is known from Unit
  10 on.
- **Challenges:** es-latam uses the same setting and people as es-es
  (user, 2026-10-16). Write them once in es-es; es-latam gets the same
  entries with only the course variants changed (*ustedes*, *jugo*).
- **Stems are not uniform** (`a1-01-01`, `a1-03c-03`,
  `a1-demonstrative-01`); unit numbers for "You know … from Unit N" come
  from `content/es-es/curriculum/units/<level>.json` (the knowledge sheet
  prints them). es-es A2 has one unit more than es-latam
  (unit 33 `vosotros`, the last), so unit numbers match in both courses.
