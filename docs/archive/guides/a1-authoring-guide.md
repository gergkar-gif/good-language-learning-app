# A1 Authoring Guide

How to write, check and review A1 content. This one document replaces
`a1-content-spec.md`, `a1-exercises.md`, `a1-lesson-template.md` and
`a1-srs-srategy.md` (archived in `docs/archive/guides/`, along with three
generated tables that only mirrored data: the unit list, the vocabulary themes
and the grammar progression). Facts that live in data are not repeated here:
read the data.

> **Exercise metadata (required, validator-enforced):** every exercise needs a `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and, unless it is `reading`, a `teaches` array of canonical slugs from `content/<course>/indexes/skill-registry.json`. Vocabulary exercises take the unit's vocabulary-theme slug. Reuse existing skills; don't invent unit- or topic-specific slugs. Full rules: `AGENTS.md` § "Exercise metadata". Check with `python scripts/validate-content.py --changed`.

## 0. What is enforced, and where the facts live

| Question | Source of truth |
|---|---|
| Is this lesson valid and well-formed? | `python scripts/validate-content.py --changed` (schemas in `content/<course>/schemas/`) |
| Does it meet the A1 content rules below? | `python scripts/audit-lesson.py a1`. **The script is the real spec**; this guide explains it in prose and the script wins any disagreement |
| Which units exist, in what order, with what titles | `content/<course>/curriculum/units/a1.json` (then `python build-manifest.py`); see `AGENTS.md` "Wiring a new unit into the app" |
| A lesson's grammar points, goal, story | the lesson and grammar files themselves |
| Vocabulary and its theme | `content/<course>/vocabulary/a1/*.json` (`theme` field) |
| Which exercise types a lesson can use | the renderer table in `engine/lessons.js` and `content/<course>/schemas/exercises.schema.json` |
| How the learner is scheduled | `engine/srs.js` (`SRS_CONFIG`) and `engine/recycle.js` |

Title rule: a unit or lesson title is the topic, never the story ("Ordering at
a Café", not "Café con Meg"). The story has its own name in its own file.

## 1. The shape of A1

A1 is units of **six lessons**: five teaching lessons (`a1-01-01` to `a1-01-05`)
and one consolidation (`a1-01-consolidation`). A unit slot is keyed by a word
slug instead of a number where a number would collide with an older slot
(`a1-cafe-01`, `a1-abilities-01`); `a1.json` lists the exact stems. The same
files exist per course (`es-latam`, `es-es`).

`a1-01-02` is a reasonable structural example to copy, but check any
candidate template against the audit script first: not every shipped lesson
passes it (see Consolidation lessons).

### Lesson flow

Sections in the order a learner meets them:

```
goal -> recycle -> grammar -> vocabulary -> Practice -> [story -> Reading] -> Dialogue -> Writing -> srs -> checklist
```

- **recycle** is a section type with no content to author; the engine fills it
  at runtime (section 6).
- The **story** and its **Reading** group appear only on the lesson that carries
  the unit's story (usually one per unit).
- A consolidation is different (section 4).

## 2. A teaching lesson

### Goal and can-do checklist

`goal.items` and `checklist.items` have the same length (enforced). Every
checklist item starts literally with **"I can"** (enforced). No fixed count;
shipped lessons carry 2 to 4.

### Grammar

- One explanation per concept: a lesson teaching two things gets one file each,
  and the engine shows one screen per file.
- At most **300 words** of prose per file (`GRAMMAR_MAX_WORDS`).
- **3 to 5** worked examples when an `examples` part is present (`GRAMMAR_EXAMPLES`).
- A reference to Lingolia as the last part (`external-link`); the script only
  warns if it is missing (a Latin America focus screen may legitimately skip it).
  Write it as a closing sentence, not a bare link: give the part a `topic` that
  completes "Read more about ___ on Lingolia." and only the site name is linked.
  ```json
  { "type": "external-link", "topic": "the use of 'ser'", "site": "Lingolia",
    "url": "https://www.lingolia.com/en/grammar/verbs/irregular-verbs/ser" }
  ```
- Every bare Spanish word or phrase inside a `text` or `tip` part's prose is
  wrapped in `*asterisks*` (`*hay*`, `*ir a* + infinitive`); see
  `editorial-style-guide.md`. Don't wrap `examples` or `table` content (CSS already
  italicises it), and don't invent a Spanish word to wrap in a purely English sentence.
- Conjugations and other forms go in a table, never buried in prose.

### Vocabulary

Per-unit totals are in the vocabulary files; units run from about 20 to 55 new
words across their five teaching lessons. The audit does **not** enforce a fixed
per-lesson count for A1, so treat any per-lesson number as a planning guide.

- Every word comes from the Core Lexicon.
- Every new word appears in that lesson's own exercises (enforced).
- Every new word is offered to the SRS deck, and appears in the unit's story where
  it fits naturally (do not force 100% concordance into a short text).
- A vocabulary file has a `theme`: a short topic label (2 to 4 words, e.g.
  "Basic greetings"). Keep it identical across lessons that share a topic, since it
  groups words into one topic deck. Vocabulary exercises are tagged with the
  unit's `kind: "vocabulary"` skill slug (`a1-unitNN-vocab`).

### Original story

On the lesson that carries the unit's story. **100 to 250 words**, flat across A1:
beginners reading tap-to-translate gain nothing from length. Only previously
introduced grammar. A Reading group follows it, and its exercises carry **no**
`teaches` tag (they are about the story just read, not a recyclable point).

### Exercises

Exercises are grouped into `exercise-group` sections, checked in this order:

| Block | Required when | What is checked |
|---|---|---|
| Practice | always | spans **4 or more** distinct exercise types |
| Reading | only on the lesson carrying the story | no `teaches` tag |
| Dialogue | always | nothing structural |
| Writing | always | nothing structural |

The lesson as a whole must also span **5 or more** distinct exercise types across its blocks (enforced).
A1 has no Listening block. There is no enforced total or per-block count;
shipped lessons run 12 to 19 exercises (Practice 8 to 16, Reading 1 to 5,
Dialogue 2 to 4, Writing 1 to 3). That is the current shape, not a target.

**`fill-blank` hints.** When a blank is genuinely unrecoverable without a nudge
(a brand-new noun, an ambiguous verb person or tense, a fixed register choice),
append a short parenthetical to `sentence`: `"Ayer __ en el festival. (bailar)"`
or `"¿Y ___? (and you?)"`. Only when the blank is truly unguessable; most blanks
should have none. **The hint must never repeat the answer**: if the answer is
`mientras que`, the hint is its English gloss, `(meanwhile)`, not `(mientras que)`.
(That mistake was found in 258 exercises and fixed in October 2026.) A dedicated
typed `hint` field is planned but does not exist in `exercises.schema.json` yet;
when it does, use it and update this note.

**Dialogue and multiple choice.** A question must be answerable from the
exercise itself: a pronoun with no antecedent (`ő`, `él`) makes two options
equally valid, and the same question must not appear twice in a row across
adjacent exercises.

## 3. Exercise types

The canonical list is `exercises.schema.json`. Below is what each does and
whether A1 uses it today.

| Type | What the learner does | A1 today |
|---|---|---|
| `multiple-choice` | one question, one right option; the right one is shown on failure | the most used type |
| `matching` | tap a Spanish item, then its translation; solved when all pairs match | yes |
| `fill-blank` | type the missing word; case and punctuation ignored, **accents checked** (`que` is not `qué`) | yes |
| `sentence-builder` | assemble a sentence from shuffled tiles; the English shows only after submitting | yes |
| `dialogue-complete` | an exchange with one line missing; pick the reply | yes |
| `structured-writing` | write against English prompts; not auto-graded, a model answer appears after Check | yes |
| `sentence-order` | put shuffled sentences in order | A2 and B1; maximum 2 per unit, natural sentences only |
| `listening-choice` | hear a sentence, pick its meaning from English options | belongs to a Listening block, which starts at A2 |
| `dictation` | hear a sentence, type it; checked like `fill-blank` | same: not in A1 |
| `substitution` | swap a word into a base sentence and see the result; not graded | built for Hungarian case marking; no Spanish content uses it |
| `error-correction` | retype a sentence that contains one deliberate mistake | **no lesson renderer exists**: Workshop's Grammar Driller only. Do not use it in an `exercise-group` until `engine/lessons.js` can render it |

Behaviour rules that apply to every type: multiple-choice options are shuffled
(the right answer is never predictably first); never ask for a conjugation when
the subject is unclear; accept every grammatically valid alternative; keep ordinary
vocabulary lower case (`la leche`) and capitalise real sentences only.

## 4. Consolidation lessons

Every unit's sixth lesson is a consolidation: no new grammar, no new vocabulary,
nothing for the deck. The audit enforces one shape for A1
(`CONSOLIDATION_SHAPE["a1"] == "single"`):

- **No** `grammar`, `vocabulary` or `srs` section.
- Exactly one `exercise-group`, titled exactly **"Review"**.
- That group spans **5 or more** distinct exercise types.
- **Every** exercise in it carries a `teaches` tag. That is what makes a review
  auditable.
- The union of `teaches` tags covers **8 or more** distinct points, so the review
  ranges across the unit instead of drilling one thing.

Why no new screens in a review: nothing new is being taught, the block's words are
already in the deck, and a "review screen" would either repeat a screen already
seen or become a new lesson in disguise. `b1-content-spec.md` carries the same rule.

**Not yet true of every shipped consolidation.** At the last count only 6 of the
26 consolidations (`a1-01`, `a1-02`, `a1-03`, `a1-03c`, `a1-04`, `a1-10`) use the
"Review" shape; the other 20 ship Practice, Dialogue and Writing blocks like a
teaching lesson (the shape the audit calls `"split"`) and so fail the "Review
group" check. This is a content gap tracked on its own, not a documentation
question; run `python scripts/audit-lesson.py a1` for the current picture.

## 5. Lesson skeleton

A teaching lesson, in the order of the flow above. Copy a passing lesson file for
the real JSON; this is the outline to fill.

1. **Metadata:** lesson id (`a1-01-02`, or `a1-cafe-01` for a slug unit), title (the
   topic), CEFR A1, estimated time, grammar concepts.
2. **Goal:** "By the end of this lesson you will be able to…", one item per
   checklist item.
3. **Grammar:** one file per concept (explanation, 3 to 5 examples, the Lingolia line).
4. **Vocabulary:** Spanish and English, no fixed row count; the unit's total is
   split across its five teaching lessons.
5. **Story:** only on the lesson that carries it (100 to 250 words).
6. **Exercises:** Practice (4+ types), then Reading (story lesson only), Dialogue,
   Writing.
7. **SRS:** the lesson's core vocabulary is offered automatically.
8. **Checklist:** "I can…" items, same count as the goals.

## 6. How learners are scheduled

Two different things need two different mechanisms. Reviewing words alone is not
enough: a learner can know that `soy` means "I am" and still be unable to say where
they are from.

| What | Mechanism | Where the learner meets it |
|---|---|---|
| **Words** | SRS deck, one card per word | the Decks section, any time |
| **Grammar and skills** | exercises recycled from earlier lessons | a recycle block at the start of each lesson |

### Words: the deck

- Each new core word is offered to the deck at the end of its lesson; the learner
  ticks which to add. A word exists once in the deck; words already there are skipped.
- Story-only words are **not** added automatically; they can be tapped and added
  from the reader.
- Cards use **SM-2** (`engine/srs.js`, constants in `SRS_CONFIG`): ease starts at
  2.5, clamped to 1.3 to 3.0. Again lowers it by 0.20 and resets the interval;
  Hard lowers it by 0.15 (interval x 1.2); Good keeps it (interval x ease); Easy
  raises it by 0.15 (interval x ease x 1.3). The first two successes use a fixed
  ramp (1 day, then 6). Intervals cap at 365 days. Reviewing early earns a smaller
  step and can never shorten the schedule, so cramming does not inflate a deck.
- A word is never finally "done". `reviews >= 3` is what marks it mastered in the reader.

### Grammar and skills: recycling

A lesson's exercises are answered once; without recycling, `ser` taught in Lesson 1
would never deliberately return. Every lesson opens with a short **recycle block**
(2 to 3 exercises from earlier lessons) between the goal and the first grammar
screen. It is **not** part of the lesson's own exercises and nothing is authored for
it: `engine/recycle.js` assembles it at run time from lessons the learner has
completed, scheduled per exercise with the same SM-2 logic, so it surfaces what that
learner actually got wrong. Lesson 1 has nothing to recycle and shows no block.

An exercise is eligible only if it carries a `teaches` tag. That rule exists mainly
for reading exercises, which ask about one specific story. Practice, dialogue and
writing exercises are skill-based and travel well.

```json
{ "id": "a1-01-practice-blank", "type": "fill-blank", "teaches": ["ser"], "...": "..." }
```

`teaches` values are lowercase hyphenated slugs from the course's
`skill-registry.json`. Keep them consistent across lessons: `ser` tagged in Lesson 1
is what lets Lesson 5 recycle it. The validator now enforces the tag on every
non-reading exercise.

### Lesson requirements (vocabulary)

Every core vocabulary item must appear in the vocabulary list, in at least one
exercise, and be offered to the deck (and in the original story where natural).
`scripts/audit-lesson.py` checks the vocabulary rules.
