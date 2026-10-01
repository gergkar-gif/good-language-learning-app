# A1 Exercise Catalogue

> **Exercise metadata (required, validator-enforced):** every exercise needs a `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and, unless it is `reading`, a `teaches` array of canonical slugs from `content/<course>/indexes/skill-registry.json`. Vocabulary exercises take the unit's vocabulary-theme slug. Reuse existing skills; don't invent unit- or topic-specific slugs. Full rules: `AGENTS.md` § "Exercise metadata". Check with `python scripts/validate-content.py --changed`.

The canonical list of exercise types is `content/es/schemas/exercises.schema.json`
— this is a readable mirror of it, not a separate source of truth. All 11
schema types are documented below; not all of them are in use in A1 content
today (A1 predates the Listening block, and a couple of types exist for
other levels/languages only — noted per type).

## In use in A1 today

### 1. Matching

Tap a Spanish item, then its translation from a shuffled second column.
Solved when every pair is matched; on failure the full pair list is
revealed.

```json
{ "type": "matching", "category": "vocabulary",
  "pairs": [["hola", "hello"], ["adiós", "goodbye"]] }
```

---

### 2. Multiple Choice

One question, one right option. On failure the correct option is
highlighted. The most-used type across every A1 exercise category
(vocabulary, grammar, reading, dialogue).

---

### 3. Fill in the Blank (`fill-blank`)

Type the missing word into a sentence. Compared with punctuation stripped
and case ignored, but accents are checked directly (`que` does not match
`qué`). On failure the answer is filled in. See `a1-content-spec.md` §4 for
the hint convention when a blank can't be inferred from context alone.

```json
{ "type": "fill-blank", "sentence": "Yo _____ Carlos.", "answer": "soy" }
```

---

### 4. Sentence Builder (`sentence-builder`)

Assemble a sentence from shuffled word tiles. On failure the finished
sentence is shown.

```json
{ "type": "sentence-builder", "tiles": ["Carlos", "soy", "Yo"] }
```

---

### 5. Complete the Dialogue (`dialogue-complete`)

An exchange with one line missing; pick the reply that fits from several
options. On failure the correct option is highlighted.

```json
{ "type": "dialogue-complete",
  "prompt": [{ "speaker": "Carlos", "text": "Hola." }],
  "options": ["Mucho gusto.", "Tengo veinte años.", "Está lloviendo."] }
```

---

### 6. Structured Writing (`structured-writing`)

Free writing against English prompts, one line per prompt. There's no
single right answer, so nothing is auto-graded: once every line has text
the learner presses Check and a model answer appears beneath each line to
compare against.

```json
{ "type": "structured-writing",
  "template": [{ "prompt": "Say hello.", "answer": "Hola." }] }
```

---

## In the schema, not yet (or not always) used in A1

### 7. Sentence Order (`sentence-order`)

Put shuffled sentences into the correct sequence; on failure the correct
order is listed. Used at A2/B1; no A1 content uses it yet.

---

### 8. Listening Choice (`listening-choice`)

Audio plays a Spanish sentence with no Spanish text on screen; the learner
picks its meaning from English options (reuses the multiple-choice
interaction). Belongs to the **Listening** exercise-group block, which A1
doesn't have — introduced at A2 (see `listening-plan` in project memory).

---

### 9. Dictation

Audio plays a Spanish sentence; the learner types what they heard. Checked
the same way as `fill-blank`. Same Listening-block dependency as above —
not present in A1.

---

### 10. Substitution

Swap one word into a base sentence and see the resulting sentence — a
pattern drill, not a graded question (same non-graded shape as
`structured-writing`: tapping each option reveals its result, Continue
unlocks once every option has been seen). Built specifically for
Hungarian's case/agreement marking, where the swapped-in word needs its own
already-inflected form supplied in the content (the engine never inflects
Hungarian itself). **No Spanish content uses this type.**

---

### 11. Error Correction (`error-correction`)

A Spanish sentence with one deliberate mistake; the learner retypes it
correctly, checked the same way as `fill-blank`. **Not rendered by
`engine/lessons.js` at all yet** — only Workshop's Grammar Driller supports
it today. Do not reference this type from a lesson's `exercise-group` until
`lessons.js` gains a renderer for it.

---

## Exercise blocks (how types are grouped in a lesson)

A1 lessons don't group exercises by category the way this catalogue does —
they group by `exercise-group` **block** (Practice, Reading, Dialogue,
Writing), each block mixing whichever types fit. See `a1-content-spec.md`
§4 for the real per-block rules (Practice must span 5+ distinct types;
Reading only exists on the lesson carrying that unit's story) and real
current exercise counts per block — this document no longer states a fixed
lesson-wide exercise count, since none is enforced for A1.
