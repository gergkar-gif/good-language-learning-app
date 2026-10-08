# Course generation brief

The one document to read before generating course content for Parlour: a new language, a new level, or a regenerated unit. It replaces `content/hu/HU_Content_Authoring_Template.md` and the archived guides in `docs/archive/guides/` as instructions (those stay as history). The decisions behind it are in [course-generation-audit.md](course-generation-audit.md) § 6 (signed off 2026-10-08, ROADMAP 149).

Tags follow [skill-tagging-spec.md](skill-tagging-spec.md); this brief only summarises them. Where this brief and an older doc disagree, this brief wins. Where this brief and a validator disagree, stop and report it.

**Scope.** Content only: unit tables, skills, grammar screens, vocabulary, stories, lessons, exercises, wiring. Audio recordings, dictionary import, morphology and `engine/` changes are separate work.

**Before you start.** Read § 1–§ 8, then the language appendix (§ 9). For a new language, write its appendix first (§ 9.3).

---

## 1. Order of work

Work in this order. Stop and show the user at each **[stop]**.

1. **Course setup** (new language only): copy `content/es-es/schemas/` to `content/<code>/schemas/` and adjust only what the language needs (an extra part of speech, an id pattern). Never loosen `category`. Add the optional `stage` field from `content/hu/schemas/exercises.schema.json` (`baseFields.stage`), since the es-es schema has none and the lesson shape (§ 2.2) needs it. Write `curriculum/challenges.json` (shape: `content/es-es/curriculum/challenges.json`) in the course's own setting. The `engine/lang.js` profile is engine work: list what the language needs (orthography, accent-sensitive grading, speech locale) for the user. **[stop]**
2. **Level plan**: the unit table `curriculum/units/<level>.json` (permanent unit ids: one to four English words, lowercase, hyphenated, never changed). In `skills/<lang>.json`, add one vocabulary skill per unit and the level's grammar skills, each with `family`, `title`, `taught_in` and `requires`. List every skill in `skills/frozen-<lang>.json`, then run `python scripts/build_skill_registry.py`. Write the plan per unit: topic, grammar points by lesson, and roughly which words go in which lesson. **[stop]** The skill list is frozen after this stop.
3. **Per unit**, in this order:
   1. grammar screens (§ 3)
   2. vocabulary files (§ 4)
   3. the unit story (§ 5)
   4. lessons and exercises (§ 2, § 6, § 7)
   5. checks (§ 8): fix everything they report
4. **Read** (§ 8.2): a second model reads the unit against the read checklist. Apply its fixes, run the checks again, then lock: `python scripts/lock_tags.py <course> <level>/<unit id> --reason "generated, checked and read"`.
5. **Wire**: add the unit to the unit table (if it isn't there yet), run `python build-manifest.py`, and commit one unit per commit. Commit in the worktree, `git pull --rebase origin master`, then `git push origin HEAD:master`. The first unit of a new level or language is a **[stop]**.

Never write a later unit before an earlier one is finished. Units build on each other (§ 2.3).

---

## 2. Shape

### 2.1 Unit

A unit is five teaching lessons and one consolidation:
- files: `<level>-<unit>-01` … `-05` and `<level>-<unit>-consolidation`
- one story, on lesson 05
- one grammar point per lesson; a lesson that teaches two things gets two screens

Every lesson file appears in exactly one unit of the unit table.

| Level | New words per unit | Exercises per teaching lesson | Consolidation | Unit story (target-language words) |
|---|---|---|---|---|
| A1 | about 20 | 16–18 | 20 | 80–150 |
| A2 | about 20–25 | 16–18 | 20 | 120–200 |
| B1 | about 20 | 16–18 | 20 | 300–400 |

Word counts are a guide, not a target. They vary with level and topic. Never add words to reach a number, and never leave out a word the topic needs. Exercise counts exclude the Reading group on lesson 05.

### 2.2 Teaching lesson

Sections, in this order:

| Section | Notes |
|---|---|
| `intro` | Only the first lesson of the course: a short "Welcome". |
| `goal` | 2–4 items. |
| `recycle` | `{"type": "recycle", "title": "Quick Review"}`. The engine fills it. Leave it out of the course's very first lesson. |
| `grammar` | One per screen, `ref` to the screen file. |
| `vocabulary` | `ref` to the lesson's vocabulary file. |
| `exercise-group` **Introduce** | 2: recognise the new form or words, using only the screen's own examples. |
| `exercise-group` **Controlled** | 4: manipulate one form at a time (fill-blank, choice). |
| `exercise-group` **Practice** | 5 at A1, 4 from A2: mixed types, at least 3 of them. |
| `story` + `exercise-group` **Reading** | Lesson 05 only: the unit story, then 3 reading items. |
| `exercise-group` **Listening** | From A2: 2 (`listening-choice`, `dictation`). None at A1. |
| `exercise-group` **Dialogue** | 2 (`dialogue-complete`). |
| `exercise-group` **Production** | 2 (`sentence-builder`, `structured-writing`). |
| `srs` | `{"type": "srs", "title": "Add to Review"}`. |
| `exercise-group` **Check** | 2: retrieve the lesson's point with no support. |
| `checklist` | The `goal` items as "I can …", in the same count and order. |

- **Exercise count:** A1 is 2+4+5+2+2+2 = 17. From A2 it is 2+4+4+2+2+2+2 = 18.
- **Types:** every teaching lesson uses at least 5 exercise types.
- **`stage` field:** each exercise's group goes in `stage` (`introduce`, `controlled`, `practice`, `reading`, `listening`, `dialogue`, `production`, `check`), never in `category`.
- **Lesson fields:** `id`, `title` (the topic, never the story's name), `level`, `goal`, `sections`. Copy the field names from a passing lesson of the same course; never invent fields.

### 2.3 Consolidation

Sections: `goal`, `recycle`, then four `exercise-group`s, then `checklist`:
- **Recognize** 5
- **Recall** 5
- **In Context** 5
- **Produce** 5

Rules:
- The consolidation teaches nothing new: no grammar, vocabulary, srs or story sections.
- Its 20 exercises mostly reuse or lightly vary the unit's own items. They run from easy to hard and cover every lesson.
- It uses at least 5 types and at least 6 different `teaches` tags.
- Every exercise is tagged.

### 2.4 What a unit may use

A unit may use only what earlier units and its own earlier lessons have taught. Never use a form before the screen that teaches it (its skill's `taught_in`). That applies to correct answers, wrong options, screen examples, dialogues and the story. Until a form is taught, repeat the noun, choose a simpler structure, or put the line in English narration.

Unit N is not unit N−1 with the nouns swapped. Each unit's identity comes from its own topic, words and situations.

---

## 3. Grammar screens

One file per concept: `grammar/<level>/<lesson>-<a|b>-gr.json`, shape `{"id", "title", "sections"}` (no `lesson` field). Part types are only those in `grammar.schema.json`; anything else silently disappears.

- **Order:** a `text` part on what it means and how it works, a `table` for any paradigm, an `examples` part with 3–5 items, a `tip` with the one mistake English speakers make, and optionally `external-link` last (`type`, `topic`, `url`, `site`; never `title`).
- **Paradigms go in a `table`**, never in prose. A conjugation, a set of case endings or a pronoun set is a table.
- **At most 300 words** across `text` and `tip`. This is a phone screen.
- **Explain why** the structure works, not only which form to use. Give a concept that doesn't exist in English enough explanation before it is drilled.
- **Italicise target-language words** in `text` and `tip` prose with `*asterisks*`, including 2–3-letter words. Never italicise English, never touch `examples` or `table`, and never invent a word just to have something to italicise.
- **Examples** use only taught words and forms. The `examples` fields are named `spanish`/`english` in every course; the target language goes in `spanish`.
- **Sound and letter tables:** never send a bare letter to TTS (it comes back silent). Such a table sets `audioOnly: true` and needs recordings. List them for the user; don't generate audio.

---

## 4. Vocabulary

One file per teaching lesson: `vocabulary/<level>/<lesson>-voc.json`.

- Every entry has `lemma` (dictionary form, lowercase unless a proper noun), `translation` (short, British English) and `pos` (from the schema list).
- Use the same `theme` label for every lesson that shares a topic, because it groups the deck.
- **Check the course's words first** (`generated/` decks or the vocabulary files). A word already taught isn't new: use it, but don't list it again.
- **Include chunks and fixed expressions** where they are how the language says it (*Mennyibe kerül?*, *¿Qué tal?*).
- Don't list a proper noun whose translation is itself (*Maya → Maya*).
- **Every listed word is used** in at least one exercise of its own lesson, and in the unit story where it fits naturally.

---

## 5. The unit story

One story per unit: `stories/original/<level>/<level>-unit-NN.json`, referenced only from lesson 05. Every paragraph has `type` (`narration` or `dialogue`), and every dialogue paragraph has a `speaker`.

- **Length:** within the level band (§ 2.1), counting target-language words. At A1, `narration` paragraphs may be English scaffolding (`"lang": "en"`) around target-language dialogue.
- **Language:** only grammar already taught and mostly known words. Each lesson's new words should recur in the story rather than appear once each.
- **Writing:** realistic dialogue, no filler scenes. The course's characters and their story move forward from unit to unit.
- **Originality:** original text only. Never copy a textbook, and never splice sentence templates.
- **Facts:** dates, names and numbers only when you're sure of them. Never invent details about real people or events.
- **Comprehension:** 3 questions at `narration.pedagogical.comprehensionQuestions`. Each needs a specific fact from the story, not general knowledge.

---

## 6. Exercises

One file per lesson: `exercises/<level>/<lesson>-ex.json`, shape `{"lesson": "<lesson id>", "exercises": [...]}`.

- Ids are `<lesson>-<stage>-<n>`, unique in the course. If you insert an exercise, renumber.
- Every exercise has `id`, `type`, `category` (`vocabulary | grammar | reading | dialogue | writing | listening`), `stage` and `teaches` (§ 7).

### 6.1 Types

Only these nine render in lessons. Never use `error-correction` or `substitution` in a lesson.

| Type | Fields | Rules |
|---|---|---|
| `multiple-choice` | `question`, `options`, `correct` | Options are shuffled at runtime, but don't always put the answer first in the file either. |
| `matching` | `pairs` [[target, English]] | At most 5 pairs. The two sides of a pair are never identical. Always `category: vocabulary`. |
| `fill-blank` | `sentence` (one `____`), `answer` or `answers`, `english`, optional `hint` | § 6.4. |
| `sentence-builder` | `tiles`, `solution` (or `solutions` when more than one order is natural), `english` | Proper nouns capitalised, everything else lowercase. `english` is the learner's only feedback, so it is always present. |
| `sentence-order` | `sentences`, `solution` | A2 and up only, at most 2 per unit, and only for a real time, cause or logic sequence. |
| `dialogue-complete` | `prompt` [{speaker, text}], `options` (plain strings), `correct` | § 6.3. |
| `structured-writing` | `template` [{prompt, answer}] | The prompt's person, tense and meaning match the model answer. |
| `listening-choice` | `sentence`, `options`, `correct` | A2 and up. `sentence` is a line the learner can follow, often from the story. |
| `dictation` | `sentence`, `english` | A2 and up. |

### 6.2 Every exercise

- **Answerable on its own.** No pronoun without its referent (*ő*, *él*, *És ők?*), and no "this exchange" or "this conversation" unless it is printed in the item.
- **One right answer.** Every other natural answer goes in `answers`, or rewrite the item. If two forms are both correct and the item can't pin one, rewrite it.
- **The correct option answers exactly what is asked.** *Hány/Cuántos* → a number, *Mikor/Cuándo* → a time, *Miért/Por qué* → a reason, *Ki/Quién* → a person, *Hogyan/Cómo* → a manner. A yes/no question gets *Igen/Sí/Nem/No*; an open question never does.
  - Bad: *Mikor érkezik a villamos?* → *Tíz percenként jön.*
  - Good: *Mikor érkezik a villamos?* → *Öt perc múlva.*
- **The stem never contains the tested form**, and the answer never appears in the prompt, hint, English line or another option (cognates aside).
- **Tests this lesson.** It uses only this lesson's words, screen and earlier material, and needs the lesson to answer. Never ask something general knowledge answers (*What is the main purpose of their conversation?*).
- **No copies.** No exercise repeats another exercise of the same unit (everything except id and tags), except consolidation items reusing lesson items. No two adjacent exercises share a question line.
- **English lines translate the target text literally and correctly**, and pin the one intended answer.
- **Language:** UTF-8, the course's own script only.

### 6.3 Wrong options

The commonest defects in shipped content. Each rule is here because a review found hundreds of breaches.

1. **A wrong option is wrong because of the taught point**, and otherwise matches the correct one: same structure, register, length and topic. Build it by breaking the tested form (person, case, tense, mood, agreement), not by changing the content.
2. **Reply items (`dialogue-complete`):** a wrong reply is wrong in *form* (the correct reply with an error on the taught point) or contradicts itself (*Igen, még nem jártam Japánban.*). It is never a different sensible reply.
   - Bad: *Nem tudom.* (it answers anything)
   - Bad: *Szívesen!* under *Köszönöm*, when the item tests something else
3. **No second right answer.** Before keeping a wrong option, ask whether a native teacher would accept it in the full sentence. Free word order, a conditional, a past tense, a synonym, an archaic form or an "also true but less complete" option is not automatically wrong.
4. **Length: every option is within 1.3× the length of the others** and equally specific. The correct answer is never the longest, the fullest, or the only one with a detail.
5. **No tells.** Nothing may appear only in the wrong options, or only in the correct one:
   - a time word (*tegnap*, *holnap*, *ayer*, *mañana*)
   - an absolute (*kizárólag*, *teljesen*, *soha*, *nunca*, *siempre*)
   - an opener or marker (*Sajnos*, *Mert*, *Porque*)
   - a " / " join
   - a capital letter, final punctuation or ending that sets one option apart
6. **Plausible and real.** No absurd, rude or cartoonish options, and no non-words (unless the item is about spelling). Options use only taught words and forms, in the item's language. Glosses go in brackets: if one option has a gloss, all do.
7. **Fact items:** wrong options are real, plausible, false facts of the same kind (another real city, another real year). The question asks only what the lesson's text contains.
8. **Word-order items:** a wrong order must break an unambiguous rule of the language (the focus slot, verb position). If another order is also natural, accept it.
9. After writing or replacing options, **re-read the question and each option in full**. Never carry options over from a neighbouring item.

### 6.4 Fill-blanks and the `hint` field

- **The blank:** exactly one `____`, inside the sentence where the word belongs, never appended after a complete sentence. The answer never repeats letters printed next to the blank (`meg____` → the answer has no *meg*).
- **The hint goes in the `hint` field, never in `sentence`.** (The field is being added to the schemas and the engine under ROADMAP 149; it lands before the first generation run.) Give a hint only when the blank can't be recovered without one: a new word, an ambiguous person, case or tense, or a register choice. Most blanks need none.
- **A hint is never the answer.** Give the lemma plus the grammar (`válik, past`; `halál + -hoz`; `bailar, yo`) or English (`meanwhile`). Never the inflected form.
- **Pin the person.** A person- or possessor-marked answer, or a sentence with the subject dropped, names the person in the hint (`I`, `his family`) or in the sentence.
- **English-only hints need synonyms.** When the hint is English only, list every correct target word in `answers` (*consent* → *beleegyezését*, *hozzájárulását*).
- **Function words and correlatives** get a structural hint (`az + -nak`, `minél … ____`), not English.
- **`english`** translates the whole sentence with the blank filled. It must not fit a second answer.

---

## 7. Tags

Full rules: [skill-tagging-spec.md](skill-tagging-spec.md). In short:

- **`teaches`: exactly one slug** from `skills/<lang>.json`, chosen by what a wrong answer shows:
  - a tested form → its grammar skill
  - a tested word, including "Which means …?" → the unit's vocabulary skill `<level>-<unit id>-vocab`
- **`category` follows the tag** on choice, fill-blank, builder and matching items. Matching is always vocabulary.
- **Reading items** (about the story) are `category: reading` with no `teaches`.
- **Skill level:** never a skill above the exercise's level, or taught after its lesson.
- **No new skills.** Never invent, rename or split a skill. The list is frozen after § 1 step 2.
- **`distractor_skills`:** on grammar choice items, record a wrong option that is a real form of *another* grammar skill, by 0-based option index: `{"1": "ki-and-mi"}`. Nothing for ungrammatical options, for the item's own skill, or for vocabulary skills.
- **Coverage:** every grammar skill the unit's screens teach gets at least 6 exercises in the level.

---

## 8. Checks before handing back

### 8.1 Scripts

Run these after each unit and fix everything they report:

```
python scripts/validate-content.py --changed
python scripts/check-content.py <course> <level> <unit id>
```

`check-content.py` is being built (ROADMAP 149). Until it exists, also run:
- `python scripts/dup_report.py <course> <level> <unit id>`
- `python imports/review/check-slash-giveaway.py --length <course> <level> --list`
- for Hungarian, `python imports/review/check-hu-exercises.py <level> --list`

Paste their output into the hand-back.

### 8.2 The read

A second model reads every item of the unit, with the screens and story beside it, and answers each question per item:

1. Does the correct answer answer exactly what is asked?
2. Would a native teacher accept any wrong option? (A second right answer.)
3. Is any wrong option odd in length, tone, opener, absolute or shape?
4. Is everything used already taught: words, forms and the wrong options too?
5. Does the English line or gloss translate the text correctly, and pin one answer?
6. Is every fact in the item in the screen or the story? Is every story fact right?
7. Does it sound like a native speaker? Doubtful phrasing goes to the course's native-speaker questions file (`imports/review/<lang>-review-questions.txt`), with a proposal. Never guess.
8. Is the tag right by what a wrong answer shows?

The reader lists each fix as id → full new content. The fixes are applied, the scripts run again, and the unit is locked.

---

## 9. Language appendices

Each appendix holds only what differs from the rules above.

### 9.1 Hungarian (`hu`)

- **Accents are letters.** a/á, e/é, o/ó/ö/ő and u/ú/ü/ű are different letters, and grading keeps them. Never write a blank whose answers differ only by accent.
- **Cases:** use the right case family per noun. The *-n/-ra/-ról* nouns (*posta*, *állomás*, *pályaudvar*, *piac*, *egyetem*, *repülőtér*, *munkahely*, *hely*, *sziget*, *strand*, *Magyarország*, *Budapest*, events) never take *-ban/-ba/-ból*.
- **Agreement:** check definite or indefinite conjugation against the object, vowel harmony on every suffix, and *a/az* before the following sound, in the prompt, the correct answer and every wrong option.
- **Focus:** a word-order wrong option must clearly break the focus rule. *Ma otthon vagyok* and *Otthon vagyok ma* are both fine.
- **Natural frames:** *Mennyibe kerül?* (not *Mennyi az ár?*), *Milyen méretek vannak?*, *balra van* (not *bal van*), *Hogy vagy?* (not *Hogyan vagy?*).
- **No archaic forms:** no *-tatik/-tetik* passive anywhere, not even as a wrong option (decided by the native speaker).
- **Yes/no replies:** a *Nem* reply that affirms is tagged `yes-no-questions`.
- **Lesson ids:** HU A1/A2 shipped flat-numbered (`a1-01`). New HU levels use the unit shape of § 2.1.

### 9.2 Spanish (`es-es`, `es-latam`)

- **The two courses share skills** (`skills/es.json`) and most A1–B1 exercises. A shared exercise is identical in both files: apply every change to both.
- **es-latam:** no *vosotros* anywhere (readings, screens, examples, exercises). Use *ustedes*. Shared items avoid words that differ by region (*zumo/jugo*), or list both in `answers`. Pronunciation items avoid c/z.
- **es-es:** *vosotros* is taught and may be used once taught.
- **Pin the person** when the subject is dropped, especially *haber* forms (`(tú)`, `(estar, nosotros)`).
- **Clitics:** *lo/la/los/las* are first taught at `a2-12-01-gr`. Before that, repeat the noun.
- **Close contrasts:** ser/estar/hay, preterite/imperfect, present/*ir a*/future. A wrong option must be clearly ungrammatical or contradict a cue in the item (a time marker, "one completed event").

### 9.3 A new language

Write its appendix at § 1 step 2, before any content, and show it to the user. It covers:
- what grading must keep (accents, diacritics, letter case)
- agreement and morphology an author must check per item
- word-order freedom, and so what a word-order wrong option may be
- the course's natural frames for greetings, prices and directions, where learners' first guesses are unnatural
- region or variant choices, and forms the course avoids
- anything the TTS can't say (bare letters, abbreviations: `speechAbbreviations` in `engine/lang.js`)
