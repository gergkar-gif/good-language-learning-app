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
- **Course variants are deliberate:** es-latam *jugo* for es-es *zumo*,
  *tomar* accepted beside *beber*, *ustedes* tables without the *vosotros*
  row. A fix to such a line is per course: mark it `"variant": "es-es"`
  (or `"es-latam"`) in the fix JSON so it is not mirrored.
- **Forms before their screen** (`taught_in` in `skills/es.json`; the
  knowledge sheet's "later" list): past tenses are A2 (`preterito-perfecto`
  a2-01-01, `preterito-indefinido` a2-11-01), yet *ayer* sentences occur in
  A1; `numbers` is taught in a1-10-02 (A1 unit 12) while *diez*, *siete*,
  *nueve* appear from a1-08-02; *gusta/gustan* before a1-gustar-01.
- **Prerequisite order (ROADMAP 148(i), user's sign-off pending):** five A1
  pairs are exempted in `KNOWN_PREREQ_ORDER` (`adjective-agreement` ←
  `plural`, `doler` ← `gustar`, `hay` ← `estar`, `ser` ←
  `subject-pronouns`, `tener` ← `present-tense`). Report a lesson that
  depends on the order; don't move `taught_in` or edit `skills/es.json`.
- **Function words count as met** (articles, prepositions, conjunctions,
  clitics, *muy/más/ya/tan*: Spanish vocabulary lists leave them out;
  `scripts/unmet-words.js` FUNCTION_WORDS). Every other word must be met:
  *otro*, *durante*, *alguien* are in no list, so replace them with met
  words, or list them in the vocabulary of the first lesson that needs
  them.
- **English inside target fields** ("Complete the greeting: Buenos ___.",
  "(Meg answers about her own sister.)", a scene line before " / ") is
  the existing Spanish format; the unmet-word check skips it. Report it
  only when it gives the answer away or contradicts `english`.
- **Stems are not uniform** (`a1-01-01`, `a1-03c-03`,
  `a1-demonstrative-01`); unit numbers for "You know … from Unit N" come
  from `content/es-es/curriculum/units/<level>.json` (the knowledge sheet
  prints them). es-es A2 has one unit more than es-latam
  (unit 33 `vosotros`, the last), so unit numbers match in both courses.
