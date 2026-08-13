# Hungarian A1 Content — Authoring Template for ChatGPT

You are writing content for **Parlour**, a language-learning app. The app already
teaches Spanish; you are producing the **Hungarian A1 course**, one lesson at a
time, as JSON files that plug directly into the existing engine. The engine does
not know or care what language it's rendering — it only cares that your files
match the schemas below exactly.

Use these four documents as your pedagogical source of truth (already written,
do not redesign them):

- `HU_Curriculum_Source_Notes.md` — reference sources and licensing rules
- `HU_A1_Curriculum_Blueprint.md` — the 30-lesson syllabus, unit by unit
- `HU_A1_Grammar_Progression.md` — the 19-point micro-grammar sequence and the
  required explanation shape (what it means → how it works → why it looks like
  this → examples → notice → practice)
- `HU_A1_Content_Generation_Spec.md` — sentence/vocabulary rules and the QC
  checklist

This document is the **fifth piece**: it tells you the exact file format the
app needs, which the four documents above don't cover.

---

## 1. What you produce, per lesson

For lesson N (two digits, `01`–`30`), produce **five JSON files**:

| File | Path | Schema section |
|---|---|---|
| Lesson | `content/hu/lessons/a1/a1-NN.json` | §2 |
| Grammar | `content/hu/grammar/a1/a1-NN-<slug>-gr.json` (one per grammar concept in the lesson — usually one file, occasionally two) | §3 |
| Exercises | `content/hu/exercises/a1/a1-NN-ex.json` | §4 |
| Vocabulary | `content/hu/vocabulary/a1/a1-NN-voc.json` | §5 |
| Story | `content/hu/stories/original/a1/a1-NN.json` | §6 |

`<slug>` is a short lowercase-hyphenated name for the grammar point, e.g.
`vowel-harmony`, `ban-ben`, `definite-conjugation`.

**Critical id rule:** ids never carry a language code. Use `a1-01`, not
`hu-a1-01`. The Hungarian course is Hungarian because it lives under
`content/hu/`, not because of a string in the id. (The blueprint's own
`HU_A1_Lesson_Map.json` uses `hu-a1-01` — that was fine as a planning
index, but do **not** carry that prefix into the actual content files, or
they will fail schema validation.)

Content ids are otherwise identical in shape to the Spanish course's — e.g.
`lesson.a1.01`, `grammar.a1.01.vowel-harmony`, `vocab.a1.01`.

Produce each file as its own fenced JSON code block, clearly labeled with its
path, so they can be saved directly.

---

## 2. Lesson file (`lessons/a1/a1-NN.json`)

```json
{
  "id": "lesson.a1.01",
  "title": "Hungarian Sounds and the Alphabet",
  "level": "A1",
  "goal": "Read Hungarian spelling aloud",
  "grammar": "alphabet",
  "sections": [
    { "type": "goal", "title": "Lesson Goals", "items": ["Pronounce the Hungarian alphabet, including long vs short vowels"] },
    { "type": "grammar", "ref": "grammar/a1/a1-01-alphabet-gr.json" },
    {
      "type": "exercise-group",
      "title": "Practice",
      "ref": "exercises/a1/a1-01-ex.json",
      "exerciseRefs": ["a1-01-practice-match", "a1-01-practice-choice", "a1-01-practice-blank", "a1-01-practice-build", "a1-01-practice-order"]
    },
    { "type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/a1/a1-01-voc.json" },
    { "type": "story", "ref": "stories/original/a1/a1-01.json" },
    { "type": "exercise-group", "title": "Reading", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-reading-choice", "a1-01-reading-order"] },
    { "type": "exercise-group", "title": "Dialogue", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-dialogue"] },
    { "type": "exercise-group", "title": "Writing", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-writing"] },
    { "type": "srs", "title": "Add to Review" },
    { "type": "checklist", "title": "Can you do this?", "items": ["I can pronounce the Hungarian alphabet, including long vs short vowels"] }
  ]
}
```

**Hard rules (schema-enforced):**
- `sections` order is fixed: `goal` → one `grammar` section per concept → the
  `Practice` `exercise-group` → `vocabulary` → `story` → `Reading`
  `exercise-group` → `Dialogue` `exercise-group` → `Writing`
  `exercise-group` → `srs` → `checklist`.
- Every `ref` and every `exerciseRefs` entry must resolve to a real id in the
  file it points at. Nothing checks this until you run `build-manifest.py`
  (§7) — a typo here fails silently in the running app otherwise.
- `goal.items` and `checklist.items` must be the same length, same order,
  same meaning — checklist items are the goal items rephrased as
  `"I can ..."`.

**Soft convention, carried over from the Spanish course (not yet
mechanically checked for Hungarian, but keep to it unless the lesson's own
content genuinely needs otherwise):**
- Exactly 4 goal items / 4 checklist items per lesson.
- 15 exercises total: Practice 6, Reading 4, Dialogue 3, Writing 2.
- The Practice group uses at least 5 *different* exercise types (see §4's
  type list) — not six multiple-choice questions in a row.
- One `grammar` section per concept. If a lesson's grammar genuinely needs
  more room than one screen comfortably holds, split the *lesson* into parts
  (`a1-01-01.json`, `a1-01-02.json`, ids `lesson.a1.01.01` etc., sharing one
  vocabulary/story slot) rather than stacking multiple grammar screens in
  one lesson. Given the blueprint already scopes each lesson to one
  principal mechanism, you likely won't need this — but it's there if a
  lesson turns out denser in practice than on paper.

There is no `"workshop-drill"` section type — don't invent one. A Workshop
drill happens automatically: any exercise tagged with `teaches` (§4) becomes
drillable there once the site owner reruns the index scripts. Just tag
consistently.

---

## 3. Grammar file (`grammar/a1/a1-NN-<slug>-gr.json`)

```json
{
  "id": "grammar.a1.01.alphabet",
  "title": "Hungarian Sounds and the Alphabet",
  "sections": [
    { "type": "text", "title": "What does it mean?", "content": "One clear sentence stating the concept." },
    { "type": "text", "title": "How does it work?", "content": "Two to four sentences of mechanism." },
    { "type": "table", "title": "Long vs short vowels", "rows": [["a", "short, open"], ["á", "long"]] },
    { "type": "examples", "title": "Examples", "items": [{ "spanish": "ház", "english": "house" }] },
    { "type": "tip", "content": "The one thing English speakers get wrong here." },
    { "type": "external-link", "topic": "Hungarian vowel length", "site": "HungarianReference", "url": "https://..." }
  ]
}
```

Follow `HU_A1_Grammar_Progression.md`'s six-part shape (what it means → how
it works → why it looks like this → examples → notice → practice) by mapping
it onto the five available part types:

- `text` (use it twice — once for "what/how", once for "why", each with its
  own `title`)
- `table` — for paradigms/patterns (vowel groups, endings)
- `examples` — **the field names are literally `spanish`/`english`** even
  though the sentence is Hungarian. That's a fixed schema field name, not a
  content instruction — put the Hungarian in `spanish` and the English gloss
  in `english`. 3–5 items.
- `tip` — the "Notice" — one pattern to watch for, or the mistake English
  speakers make.
- `external-link` — optional, last in `sections` if used. Point at
  HungarianReference or another source from `HU_Curriculum_Source_Notes.md`,
  never at MagyarOK content directly (licensing).

**Hard rule:** only these five part types render. Anything else is silently
dropped — no error, just a missing chunk of the screen.

**Soft convention:** keep prose to roughly 300 words total across `text`
parts — this is a mobile screen, not a grammar reference page.

---

## 4. Exercises file (`exercises/a1/a1-NN-ex.json`)

```json
{
  "lesson": "a1-01",
  "exercises": [
    { "id": "a1-01-practice-match", "type": "matching", "category": "vocabulary", "pairs": [["ház", "house"], ["asztal", "table"]], "teaches": ["alphabet"] },
    { "id": "a1-01-practice-choice", "type": "multiple-choice", "category": "grammar", "question": "Which is the long vowel?", "options": ["a", "á"], "correct": 1, "teaches": ["alphabet"] },
    { "id": "a1-01-practice-blank", "type": "fill-blank", "sentence": "H_z.", "answer": "ház", "teaches": ["alphabet"] },
    { "id": "a1-01-practice-build", "type": "sentence-builder", "tiles": ["Ez", "egy", "ház"], "solution": ["Ez", "egy", "ház"], "english": "This is a house.", "teaches": ["alphabet"] },
    { "id": "a1-01-practice-order", "type": "sentence-order", "sentences": ["Ez egy ház.", "A ház nagy."], "solution": [0, 1], "teaches": ["alphabet"] },
    { "id": "a1-01-reading-choice", "type": "multiple-choice", "category": "reading", "question": "...", "options": ["...", "..."], "correct": 0 },
    { "id": "a1-01-dialogue", "type": "dialogue-complete", "category": "dialogue", "prompt": [{ "speaker": "Anna", "text": "Szia!" }, { "speaker": "Péter", "text": "_____" }], "options": ["Szia!", "Köszönöm."], "correct": 0 },
    { "id": "a1-01-writing", "type": "structured-writing", "category": "writing", "template": [{ "prompt": "Greet someone.", "answer": "Szia!" }] }
  ]
}
```

**Available exercise types** (pick from these — `matching`, `multiple-choice`,
`fill-blank`, `sentence-builder`, `sentence-order`, `dialogue-complete`,
`structured-writing`, `listening-choice`, `dictation`; full field requirements
are in `content/es/schemas/exercises.schema.json` if you need the exact
shape of one you haven't used yet). **Do not use `error-correction`** — it's
in the schema but the lesson screen doesn't render it yet; only Workshop's
driller does, and only after separate wiring.

**`teaches` tags:** lowercase-hyphenated slugs naming the grammar point(s) an
exercise tests — e.g. `["vowel-harmony"]`, `["accusative", "food-vocab"]`.
This is what makes an exercise eligible for recycling in later lessons and
for Workshop's Grammar Driller, so **reuse the same slug every time the same
concept comes up** (the grammar file's own id suffix is a natural choice —
keep them matching). Omit `teaches` on reading-comprehension exercises; they
only make sense right after that lesson's own story.

**Answer-checking behavior to write for:** `fill-blank`/`dictation` compare
with accents, punctuation and case stripped — but Hungarian accents (á, é, í,
ó, ö, ő, ú, ü, ű) are *meaningful*, not decorative, so **do not rely on
accent-stripping to make two different words match**; write blanks where the
accent doesn't change the word's identity, or accept the ambiguity
deliberately.

---

## 5. Vocabulary file (`vocabulary/a1/a1-NN-voc.json`)

```json
{
  "id": "vocab.a1.01",
  "lesson": "a1-01",
  "title": "Hungarian Sounds and the Alphabet",
  "theme": "Everyday objects",
  "words": [
    { "lemma": "ház", "translation": "house", "pos": "noun" },
    { "lemma": "szia", "translation": "hi / bye (informal)", "pos": "interjection" }
  ]
}
```

- `lemma` is the dictionary form, lower case, exactly as it should be stored
  in the learner's review deck.
- `pos` must be one of: `noun`, `verb`, `adjective`, `adverb`, `pronoun`,
  `preposition`, `conjunction`, `article`, `interjection`, `expression`,
  `number`, `unknown` (or two joined with `/`, e.g. `noun/adjective`, only
  where both readings are actually taught).
- `theme` is a short freeform topic label (2–4 words) — there's no
  Hungarian equivalent of Spanish's `a1-vocabulary-themes.md` yet, so pick
  something sensible and **keep it consistent** across lessons that share a
  topic, since it groups words into a shared deck.
- **10–15 words**, per `HU_A1_Content_Generation_Spec.md`.
- **Hard rule:** every word here must appear in that lesson's story, and in
  at least one exercise. A word nothing uses doesn't belong here.

---

## 6. Story file (`stories/original/a1/a1-NN.json`)

```json
{
  "id": "story.a1.01",
  "title": "Egy Ház Budapesten",
  "level": "A1",
  "lesson": 1,
  "type": "original",
  "estimatedMinutes": 2,
  "characters": ["Anna"],
  "paragraphs": [
    { "type": "narration", "text": "Anna egy házban lakik." },
    { "type": "dialogue", "speaker": "Anna", "text": "Szia! Én Anna vagyok." }
  ]
}
```

- **Exactly 10 sentences**, per the blueprint — not the Spanish course's
  100–250 word band. One `paragraphs` entry per sentence is fine, or group a
  few narration sentences into one paragraph; either renders correctly.
- **Always set `"type"`** on every paragraph (`"narration"` or
  `"dialogue"`), and `"speaker"` on every dialogue line. The Spanish course
  left `type` off in 49 of 50 stories and lost all its speaker labels as a
  result — don't repeat that mistake.
- Mostly known/high-frequency vocabulary; the lesson's own new words should
  recur several times rather than appear once each.
- No copied textbook text (per the source notes) — original sentences only.

---

## 7. Per-lesson checklist before you hand a lesson back

Merge the QC checklist from `HU_A1_Content_Generation_Spec.md` with the
schema-level items below:

- [ ] All 5 files present, correctly named, correct paths
- [ ] Every id follows the patterns in §2–§6 (no `hu-` prefix anywhere)
- [ ] Lesson `sections` in the fixed order (§2)
- [ ] Every `ref` / `exerciseRefs` entry matches a real id you actually wrote
- [ ] `goal.items` and `checklist.items` same length, same order
- [ ] Only the five grammar part types used; `external-link` (if any) is last
- [ ] Only real exercise types used (not `error-correction`)
- [ ] Every `teaches` slug reused consistently with earlier lessons covering
      the same point
- [ ] Every vocabulary word appears in the story and in ≥1 exercise
- [ ] Story has exactly 10 sentences, every paragraph typed, every dialogue
      line has a speaker
- [ ] One main grammatical mechanism per lesson; nothing from the
      blueprint's "intentionally postponed" list has crept in
- [ ] Only one new lesson at a time — output it fully before starting the next

---

## 8. Validating what comes back

Once files are saved into `content/hu/...`, from the project root:

```bash
python -m pip install jsonschema   # once
python scripts/validate-content.py
python build-manifest.py
```

`validate-content.py` checks every file against its schema (§2–§6, hard
rules). `build-manifest.py` rebuilds the curriculum index and reports any
`ref`/`exerciseRefs` that don't resolve. `scripts/audit-lesson.py` is
Spanish-specific (it hardcodes Spanish articles and a Spanish stemmer) and
will not run correctly against Hungarian content yet — the "soft convention"
notes above exist to keep content close to what that auditor checks, in case
someone adapts it for Hungarian later.
