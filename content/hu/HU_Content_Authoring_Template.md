# Hungarian A1 Content — Authoring Template for ChatGPT

**Status: Hungarian A1 shipped in full (30 units, 179 lessons) — this is a
historical bootstrapping doc, not an active build brief.** The four
"pedagogical source of truth" documents it originally pointed at
(`HU_Curriculum_Source_Notes.md`, `HU_A1_Curriculum_Blueprint.md`,
`HU_A1_Grammar_Progression.md`, `HU_A1_Content_Generation_Spec.md`) don't
exist in this repo — they were the planning inputs used to kick off A1
authoring and were never committed. §2/§3 below have been corrected to
match what actually shipped (real files diverged from the original plan
during authoring); treat this doc as a format reference for revising an
existing A1 lesson, not a template for new Hungarian levels — check a
real file under `content/hu/lessons/` first regardless, since content
conventions have kept evolving since A1 shipped.

You are writing content for **Parlour**, a language-learning app. The app already
teaches Spanish; the Hungarian course lives alongside it as JSON files that plug
directly into the existing engine. The engine does
not know or care what language it's rendering — it only cares that your files
match the schemas below exactly.

---

## 1. What you produce, per lesson

For lesson N (two digits, `01`–`30`), produce **five JSON files**:

| File | Path | Schema section |
|---|---|---|
| Lesson | `content/hu/lessons/a1/a1-NN.json` | §2 |
| Grammar | `content/hu/grammar/a1/a1-NN-<letter>-gr.json` (one per grammar concept in the lesson — `a`, `b`, ... in teaching order, not a descriptive slug) | §3 |
| Exercises | `content/hu/exercises/a1/a1-NN-ex.json` | §4 |
| Vocabulary | `content/hu/vocabulary/a1/a1-NN-voc.json` | §5 |
| Story | `content/hu/stories/original/a1/a1-unit-NN.json` — **one per unit** (5 lessons), attached to the unit's last lesson only, not one per lesson | §6 |

Real shipped files use a plain letter suffix (`a1-01-a-gr.json`,
`a1-01-b-gr.json`), not a descriptive slug — check
`content/hu/grammar/a1/` before naming a new file.

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

This is the real shape, taken directly from the shipped `a1-01.json`
(check `content/hu/lessons/a1/` for a current example before writing a
new file — content conventions have kept evolving since A1 shipped):

```json
{
  "id": "lesson.a1.01",
  "title": "Hungarian Sounds and the Alphabet",
  "level": "A1",
  "goal": "Read Hungarian spelling aloud",
  "grammar": "alphabet",
  "sections": [
    { "type": "intro", "title": "Welcome", "body": ["One or two paragraphs introducing the level/unit — only the unit's first lesson has this."] },
    { "type": "goal", "title": "Lesson Goals", "items": ["I can greet someone and respond simply in Hungarian.", "I can recognise the key sounds and spellings from this lesson."] },
    { "type": "grammar", "title": "Hungarian Vowels", "ref": "grammar/a1/a1-01-a-gr.json" },
    { "type": "grammar", "title": "Hungarian Consonant Sounds", "ref": "grammar/a1/a1-01-b-gr.json" },
    { "type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/a1/a1-01-voc.json" },
    { "type": "exercise-group", "title": "Introduce", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-intro-1", "a1-01-intro-2"] },
    { "type": "exercise-group", "title": "Controlled", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-controlled-1", "a1-01-controlled-2", "a1-01-controlled-3", "a1-01-controlled-4"] },
    { "type": "exercise-group", "title": "Practice", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-practice-1", "a1-01-practice-2", "a1-01-practice-3", "a1-01-practice-4"] },
    { "type": "story", "title": "Reading: ...", "ref": "stories/original/a1/a1-unit-01.json" },
    { "type": "exercise-group", "title": "Dialogue", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-dialogue-1", "a1-01-dialogue-2"] },
    { "type": "exercise-group", "title": "Production", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-writing-1", "a1-01-writing-2"] },
    { "type": "srs", "title": "Add to Review" },
    { "type": "exercise-group", "title": "Check", "ref": "exercises/a1/a1-01-ex.json", "exerciseRefs": ["a1-01-check-1", "a1-01-check-2"] },
    { "type": "checklist", "title": "Can you do this?", "items": ["I can greet someone and respond simply in Hungarian.", "I can recognise the key sounds and spellings from this lesson."] }
  ]
}
```

**Hard rules (schema-enforced):**
- `sections` order: optional `intro` (unit's first lesson only) → `goal` →
  optional `recycle` (units after the first) → one `grammar` section per
  concept → `vocabulary` → `exercise-group`s named `Introduce` →
  `Controlled` → `Practice` (in that order) → optional `story` (unit's
  *last* lesson only — one story per unit, not per lesson) → `exercise-group`
  `Dialogue` → `exercise-group` `Production` → `srs` → `exercise-group`
  `Check` → `checklist`.
- Every `ref` and every `exerciseRefs` entry must resolve to a real id in the
  file it points at. Nothing checks this until you run `build-manifest.py`
  (§7) — a typo here fails silently in the running app otherwise.
- `goal.items` and `checklist.items` must be the same length, same order,
  same meaning — checklist items are the goal items rephrased as
  `"I can ..."`.

**Soft convention** (spot-check a recent real lesson before relying on an
exact number here — these drifted from the original plan during
authoring and may have moved again since):
- One `grammar` section per concept, usually 2 per lesson (`-a-`/`-b-`
  suffixed files).
- Exercise groups run Introduce → Controlled → Practice → Dialogue →
  Production → Check, each with a handful of exercises rather than a
  fixed total — check `content/hu/exercises/a1/` for current typical
  counts.
- A unit's story attaches only to its last lesson
  (`stories/original/a1/a1-unit-NN.json`), covering the whole unit, not
  one story per lesson.

There is no `"workshop-drill"` section type — don't invent one. A Workshop
drill happens automatically: any exercise tagged with `teaches` (§4) becomes
drillable there once the site owner reruns the index scripts. Just tag
consistently.

---

## 3. Grammar file (`grammar/a1/a1-NN-<letter>-gr.json`)

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

Map a "what it means → how it works → why it looks like this → examples →
notice → practice" progression onto the available part types:

- `text` (use it twice — once for "what/how", once for "why", each with its
  own `title`)
- `table` — for paradigms/patterns (vowel groups, endings). Real files also
  use `bothAudible`/`audioMap` fields on some tables for audio playback —
  check a recent example before assuming the plain `rows` shape above is
  the whole story.
- `examples` — **the field names are literally `spanish`/`english`** even
  though the sentence is Hungarian. That's a fixed schema field name, not a
  content instruction — put the Hungarian in `spanish` and the English gloss
  in `english`. 3–5 items.
- `tip` — the "Notice" — one pattern to watch for, or the mistake English
  speakers make.
- `external-link` — optional, last in `sections` if used. Point at a real,
  licensable Hungarian-reference source, never at MagyarOK content directly
  (licensing).

**Hard rule:** only these part types render (check
`content/hu/schemas/grammar.schema.json` for the current authoritative
list and field definitions, including `audioMap`/`bothAudible` on
`table`). Anything else is silently dropped — no error, just a missing
chunk of the screen.

**Soft convention:** keep prose to roughly 300 words total across `text`
parts — this is a mobile screen, not a grammar reference page.

**Italicize embedded Hungarian.** `text` and `tip` parts are English
explanatory prose — any bare Hungarian word or short phrase already
appearing in that prose must be wrapped in `*asterisks*` (e.g. "*Hol*?
asks where", "*dolgozik* is an *-ik* verb", "*Kell még valami*?"), which
the app renders as `<em>` at display time. Recognize Hungarian by its
accented vowels (á é í ó ö ő ú ü ű), the digraphs gy/ny/ty/sz/zs/cs/dzs, or
a case/possessive/verb ending you've already introduced — including short
2–3 letter words (*Hol*, *itt*, *ott*, *és*, *Van*, *Ki*), which are easy
to skip but just as much a target-language word as anything longer. Never
invent or translate a word just to have something to wrap — if a sentence
is pure English, leave it untouched. Never wrap English (including English
grammar terminology like "infinitive" or "definite object"), and never
touch `examples`/`table` parts — those already render in italics
automatically via CSS.

---

## 4. Exercises file (`exercises/a1/a1-NN-ex.json`)

```json
{
  "lesson": "a1-01",
  "exercises": [
    { "id": "a1-01-practice-match", "type": "matching", "category": "vocabulary", "stage": "practice", "pairs": [["ház", "house"], ["asztal", "table"]], "teaches": ["alphabet"] },
    { "id": "a1-01-practice-choice", "type": "multiple-choice", "category": "grammar", "stage": "practice", "question": "Which is the long vowel?", "options": ["a", "á"], "correct": 1, "teaches": ["alphabet"] },
    { "id": "a1-01-practice-blank", "type": "fill-blank", "category": "grammar", "stage": "controlled", "sentence": "H_z.", "answer": "ház", "english": "House.", "teaches": ["alphabet"] },
    { "id": "a1-01-practice-build", "type": "sentence-builder", "category": "grammar", "stage": "practice", "tiles": ["Ez", "egy", "ház"], "solution": ["Ez", "egy", "ház"], "english": "This is a house.", "teaches": ["alphabet"] },
    { "id": "a1-01-practice-order", "type": "sentence-order", "category": "grammar", "stage": "practice", "sentences": ["Ez egy ház.", "A ház nagy."], "solution": [0, 1], "teaches": ["alphabet"] },
    { "id": "a1-01-reading-choice", "type": "multiple-choice", "category": "reading", "question": "...", "options": ["...", "..."], "correct": 0 },
    { "id": "a1-01-dialogue", "type": "dialogue-complete", "category": "dialogue", "stage": "dialogue", "prompt": [{ "speaker": "Anna", "text": "Szia!" }, { "speaker": "Péter", "text": "_____" }], "options": ["Szia!", "Köszönöm."], "correct": 0, "teaches": ["alphabet"] },
    { "id": "a1-01-writing", "type": "structured-writing", "category": "writing", "stage": "production", "template": [{ "prompt": "Greet someone.", "answer": "Szia!" }], "teaches": ["alphabet"] }
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

**`category` vs `stage` (required):**
- `category` MUST be present on every exercise and MUST be one of the six shared values across all courses: `vocabulary | grammar | reading | dialogue | writing | listening`. Never put lesson stages (`controlled`, `practice`, `introduce`, `check`, `consolidation`, `review`, `recognize`, `recall`, `produce`, `production`, `context`, `in-context`) or content domains (`civics`, `citizenship`, `history`, `literature`, `law`, `culture`, `geography`) in `category`.
- Use the optional `stage` field (`content/hu/schemas/exercises.schema.json`) to record the lesson stage or content domain when needed.

**`teaches` tags (required for all non-reading exercises):** lowercase-hyphenated slugs naming the reusable grammar, vocabulary, or communicative skill(s) an exercise tests — e.g. `["vowel-harmony"]`, `["accusative", "food-vocab"]`. Every non-`reading` exercise MUST have a non-empty `teaches` array, and every slug MUST exist in `content/hu/indexes/skill-registry.json` (enforced by `scripts/validate-content.py`). Prefer an existing slug from `skill-registry.json`; if a genuinely new reusable skill is needed, add it to `skill-registry.json` (and `grammar-titles.json` for grammar skills) first. Omit `teaches` on `category: "reading"` exercises; they only make sense right after that lesson's own story.

**Answer-checking behavior to write for:** `fill-blank`/`dictation` compare
with accents, punctuation and case stripped — but Hungarian accents (á, é, í,
ó, ö, ő, ú, ü, ű) are *meaningful*, not decorative, so **do not rely on
accent-stripping to make two different words match**; write blanks where the
accent doesn't change the word's identity, or accept the ambiguity
deliberately.

**`fill-blank` hints:** when a blank is genuinely unrecoverable without a
nudge — a brand-new word, an ambiguous case/person choice, a fixed register
pick — append a short parenthetical hint to the end of `sentence`, e.g.
`"Az utcán látok egy ____. (bird)"`. Only when truly unguessable; most
blanks shouldn't have one. **This is scheduled to change**: a dedicated
`hint` field is planned (see `ROADMAP.md` → Workshop → "Fill-blank
exercises should carry a real, typed `hint` field") so it renders styled
and separate from the sentence instead of being silently part of the same
string. Once that field exists in `exercises.schema.json`, use it instead
— this note will be updated at that point.

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
- **10–15 words** per lesson (original target — not re-verified against
  every shipped lesson).
- **Hard rule:** every word here must appear in that lesson's unit story
  (see §6 below — stories are per-unit, so this means "somewhere across
  the 5 lessons' shared story"), and in at least one exercise. A word
  nothing uses doesn't belong here.

---

## 6. Story file (`stories/original/a1/a1-unit-NN.json`) — one per unit

Stories are **per-unit** (covering all 5 lessons), attached only to the
unit's last lesson's `story` section — not one file per lesson as
originally planned. Real files run ~20 paragraphs of narration/dialogue,
not a fixed sentence count:

```json
{
  "id": "story.a1.unit05",
  "title": "What Is This?",
  "level": "A1",
  "type": "original",
  "characters": ["Károly", "Meg"],
  "paragraphs": [
    { "type": "narration", "lang": "en", "text": "Meg is in Károly's apartment. They look around the room together." },
    { "type": "dialogue", "speaker": "Károly", "text": "..." }
  ]
}
```

- **Always set `"type"`** on every paragraph (`"narration"` or
  `"dialogue"`), and `"speaker"` on every dialogue line.
- A `narration` paragraph can carry `"lang": "en"` for English scaffolding
  narration alongside Hungarian dialogue — check a real file for how the
  two are mixed.
- Mostly known/high-frequency vocabulary; each lesson's own new words
  should recur several times across the unit's story rather than appear
  once each.
- No copied textbook text — original sentences only.

---

## 7. Per-lesson checklist before you hand a lesson back

- [ ] All files present, correctly named, correct paths (note: story file
      is per-unit, only needed/updated on that unit's last lesson)
- [ ] Every id follows the patterns in §2–§6 (no `hu-` prefix anywhere)
- [ ] Lesson `sections` in the order described in §2
- [ ] Every `ref` / `exerciseRefs` entry matches a real id you actually wrote
- [ ] `goal.items` and `checklist.items` same length, same order
- [ ] Only real grammar part types used (§3); `external-link` (if any) is last
- [ ] Only real exercise types used (not `error-correction`)
- [ ] Every `teaches` slug reused consistently with earlier lessons covering
      the same point
- [ ] Every vocabulary word appears in the unit's story and in ≥1 exercise
- [ ] Every paragraph typed, every dialogue line has a speaker
- [ ] One main grammatical mechanism per lesson
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
