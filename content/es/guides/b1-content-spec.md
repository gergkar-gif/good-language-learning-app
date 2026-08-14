# B1 Content Specification

This document defines the JSON shape every B1 lesson, grammar, exercise,
vocabulary and story file must have. It is the document to hand to a
generator (human or ChatGPT) alongside `B1_GUIDE.md` (curriculum design) and
`Parlour B1 Consolidated Unit List.md` (the 72-unit plan, both tracks) —
those two say *what* each unit teaches; this says *what file to write and in
what shape*.

It is grounded directly in the current schemas
(`content/es/schemas/*.schema.json`) and in the actual A1/A2 production
files, not in `a1-content-spec.md`, which describes an earlier one-file-per-
lesson layout the content has since moved on from. Where this spec disagrees
with `a1-content-spec.md`, this one is current — A1 itself no longer matches
its own spec document in several respects (see §8).

---

## 1. Unit → file layout

A unit is **six lesson files**: five teaching lessons and one consolidation.
This is the existing A1/A2 pattern, unchanged in shape for B1 — only the
per-lesson exercise and vocabulary counts grow (§4, §6).

```
content/es/lessons/b1/b1-{unit}-01.json   ...   b1-{unit}-05.json
content/es/lessons/b1/b1-{unit}-consolidation.json
```

Every lesson file has a matching exercise file, and every teaching lesson
(01–05) has a matching grammar file per grammar section (§5) and a matching
vocabulary file:

```
content/es/exercises/b1/b1-{unit}-01-ex.json   ... b1-{unit}-consolidation-ex.json
content/es/grammar/b1/b1-{unit}-01-{topic}-gr.json
content/es/vocabulary/b1/b1-{unit}-01-voc.json
```

The unit's one story lives in **lesson 05 only** (§7) — never repeated
across the other four teaching lessons, and never present in consolidation.

### 1a. The `{unit}` token differs by track

**Core Spanish** units are numbered `01`–`36`, matching their position in
the Consolidated Unit List (Part I).

**Latin America** units cannot also be numbered `01`–`36` — `lesson.b1.01.01`
would collide between "Core Unit 1, Lesson 1" and "Latin America Unit 1,
Lesson 1", because none of the id patterns in the schemas
(`lesson.schema.json`, `vocabulary.schema.json`, `exercises.schema.json`)
carry a track field. This is a real gap in the engine — there is no `track`
concept anywhere in `curriculum.json` or `journey.js` yet — and fixing it
properly is separate work. Until then, **Latin America units use a
lowercase word slug instead of a number** as `{unit}`, e.g.:

```
content/es/lessons/b1/b1-precolombina-01.json
content/es/lessons/b1/b1-conquista-01.json
content/es/lessons/b1/b1-independencia-01.json
```

This is legal today: the id patterns accept `[a-z]+` as an alternative to
`\d{2}[a-z]?` (the same escape hatch `a1-cafe-01` already uses). No hyphens
or digits inside the slug. Pick one short, distinctive word per Latin
America unit from its title in the Consolidated Unit List (Part II) — e.g.
Unit 1 "Pre-Columbian America" → `precolombina`, Unit 8 "La independencia" →
`independencia`. Keep a slug-to-unit-number lookup somewhere (a comment in
the unit list, or a small table in this file) so nothing has to be
reverse-engineered later; it does not need to be in this spec today, but
**do not generate content for a Latin America unit without first fixing its
slug**, since changing it later breaks every id, ref and SRS key derived
from it.

### 1b. ids

Every id follows the pattern already in the schema, substituting `b1` for
the level and the track's `{unit}` token from §1a:

| File | Pattern | Example (Core) | Example (Latin America) |
|---|---|---|---|
| Lesson | `lesson.b1.{unit}.{NN\|consolidation}` | `lesson.b1.01.01` | `lesson.b1.precolombina.01` |
| Vocabulary | `vocab.b1.{unit}.{NN\|consolidation}` | `vocab.b1.01.01` | `vocab.b1.precolombina.01` |
| Exercises file `lesson` field | `b1-{unit}-{NN\|consolidation}` | `b1-01-01` | `b1-precolombina-01` |
| Exercise id | `b1-{unit}-{NN}.exNN` | `b1-01-01.ex01` | `b1-precolombina-01.ex01` |
| Grammar | `grammar.b1.{unit}.{NN}.{topic}` | `grammar.b1.01.01.preterito-indefinido` | `grammar.b1.precolombina.01.geografia` |

---

## 2. Section order (per lesson)

Fixed by `lesson.schema.json`'s `sections` description, and the only order
the engine understands — there are exactly eight section types
(`goal`, `recycle`, `grammar`, `exercise-group`, `vocabulary`, `story`,
`srs`, `checklist`); anything else silently renders nothing (see §8).

**Teaching lesson (01–05):**

```
goal → recycle → grammar → exercise-group "Practice" → vocabulary
  → [story → exercise-group "Reading"]   (lesson 05 only)
  → exercise-group "Listening" → exercise-group "Dialogue"
  → exercise-group "Writing" → srs → checklist
```

**Consolidation lesson:**

```
goal → recycle → exercise-group "Review" → checklist
```

No grammar section, no vocabulary section, no srs section, no story — this
follows the settled A1 review-lesson rationale (`a1-content-spec.md` §4c):
nothing new is being taught, the block's words are already in Decks, and a
"review screen" would either repeat a screen already seen or become a new
grammar explanation, which is what the next lesson is for. A2's
consolidation lessons keep an `srs` section despite having no vocabulary —
that is drift, not a second convention; B1 consolidation should not carry
one.

---

## 3. Latin America lessons: no grammar section, a Focus screen instead

The schema has no "historical context" or "content" section type — only
`grammar`, which is generic underneath (`text`, `table`, `examples`, `tip`,
`external-link` parts; none of the field names are grammar-specific). Latin
America teaching lessons use the `grammar` section type to carry historical
or cultural content instead of a grammar rule:

- `text` — the historical/regional context (≤300 words, same limit as
  Core, §5)
- `examples` — Spanish/English pairs of the unit's key historical
  vocabulary in a sentence, not verb conjugations
- `tip` — a fact, distinction or common misconception worth flagging
- `external-link` — optional; when used, `site` should name the actual
  source (a museum, archive or reference work) rather than defaulting to
  Lingolia, which has nothing relevant to link to for this track

The Consolidated Unit List's "Focus:" line (as opposed to Core's "Grammar:"
line) is exactly this screen's subject — write the file's `title` and `text`
from it.

Latin America lessons still recycle Core grammar in their exercises (a
`fill-blank` about a colonial economy can still exercise the imperfecto),
but they introduce none. `recycle` in a Latin America lesson pulls from
**both** tracks' completed lessons — nothing in `engine/recycle.js`
restricts it by track, and the guide (§8) wants the two tracks reinforcing
each other.

---

## 4. Vocabulary

Per unit, across the six lessons: **16 new words**, split `4 / 3 / 3 / 3 / 3
/ 0` across lessons 01–05 and consolidation. This is now baked into the
Consolidated Unit List's per-lesson `New words:` counts for both tracks —
copy them directly rather than re-deriving a split.

Every word must:
- appear in the vocabulary file for its lesson (`vocabulary.schema.json`
  shape: `lemma`, `translation`, `pos`)
- appear in the lesson's exercises (at least one)
- appear in the unit's story if the word belongs to lesson 05, or — for
  words from lessons 01–04 — appear somewhere in the unit's story too,
  since it is the one text the whole unit shares (this is the existing
  A1 `audit-lesson.py` rule, applied per-unit rather than per-lesson: a
  part without its own story is still checked against the unit's story)

Latin America vocabulary should deliberately overlap with Core where the
guide calls for it (§9 of `B1_GUIDE.md`): a word taught in a Core unit does
not need to be re-taught in a Latin America unit to be used by it, but a
term specific to the historical content (*régimen*, *dictadura*,
*desaparecido*) is new vocabulary for that Latin America lesson regardless
of how many Core units come before or after it.

---

## 5. Grammar (Core) / Focus (Latin America)

One file per teaching lesson (lessons 01–05; consolidation has none).

- ≤300 words of prose across all `text`/`tip` parts
- 3–5 worked examples (`examples` part)
- one `external-link` recommended, not mandatory (a missing one is a
  warning, not a failure — same as the existing A1 rule)
- one concept per file. A unit whose grammar needs more room than one
  700-word-lesson screen can comfortably hold should be split the way A1
  splits an overloaded lesson into parts (`a1-content-spec.md` §4b) —
  prefer narrowing what lesson 3, say, tries to teach over cramming two
  grammar screens into one lesson

---

## 5a. Register floor: hitting the target isn't enough

Unit 1's first draft passed every structural rule in this document — right
word counts, right section order, right exercise-block split — and still
read as A2, sometimes A1, because nothing here said how *complex* a sentence
had to be, only what grammar point or topic it had to touch. That gap is
now closed.

**Isolated grammar drills are exempt.** A `fill-blank` or `sentence-builder`
in the Practice block that isolates one clause to test one form
(`"Ayer __ algo inesperado. (ocurrir)"`) is correct pedagogy, not a defect —
narrowing to one thing is the point of a drill.

**Everything that models how the language is actually used is not exempt.**
That means the Grammar/Focus screen's `examples`, the story, every
`Dialogue`-block exercise, `structured-writing` answers, and Consolidation's
`Review` block. In each of these, **at least half the Spanish must combine
two clauses** — a connector (*mientras, aunque, ya que, sin embargo, porque,
cuando, lo que*), a relative clause, or a comparison — not a run of isolated
simple declaratives. A Focus screen's four examples should not read like
four vocabulary flashcards stitched into sentences.

This is exactly what went wrong in Latin America Unit 1's Focus screens.
Concretely, from `b1-precolombina-01-geography-and-historical-context-gr.json`:

> ✗ *"La selva ofrecía recursos diversos."* — subject, verb, object. Nothing
> a learner couldn't produce at A2.
>
> ✓ *"La selva, que cubría gran parte del territorio, ofrecía recursos que
> las comunidades aprovechaban de formas distintas."* — same content, two
> relative clauses, and it now actually needs B1 syntax to parse.

And from the exercise file, where the dialogue-complete block used the
identical two-line template in every lesson without ever supplying a reason:

> ✗ *"¿Qué sabes sobre este tema?" → [fact] → "¿Por qué?" → [same fact
> repeated]* — the "why" question goes unanswered.
>
> ✓ *"¿Por qué es importante este período?" → "Porque explica cómo se
> formaron las sociedades que los europeos encontraron después."* — a real
> causal connector, doing real work.

Three more patterns from the same draft to specifically avoid, because each
one technically satisfies its exercise type's schema while testing nothing:

- **Multiple-choice that asks the learner to recognise a sentence they were
  just shown** (`"¿Cuál afirmación corresponde al tema «geography»?"`, with
  the correct option being the example sentence verbatim) is not a
  comprehension question. Write one that requires understanding the content,
  not matching strings.
- **`sentence-order` items need an actual sequence** — temporal, causal, or
  logical — that a learner can reason through. Three unrelated facts in
  arbitrary order (*"La cordillera atravesaba grandes territorios." / "Las
  comunidades se adaptaban a su entorno." / "Existían diferencias
  regionales."*) has no correct answer beyond the one the file happens to
  declare.
- **`dialogue-complete` wrong options must be plausible near-misses in the
  same register**, not absurd non-sequiturs (*"No lo sé mañana."*, *"Mañana
  había ocurrido."* — the latter isn't even grammatical). A wrong option a
  learner could imagine a real speaker saying is what makes the right one
  worth choosing.

---

## 6. Exercises

Nine exercise types render in a lesson today: `matching`,
`multiple-choice`, `fill-blank`, `sentence-builder`, `sentence-order`,
`dialogue-complete`, `structured-writing`, `listening-choice`, `dictation`.
**`error-correction` is defined in the schema but not yet rendered by
`engine/lessons.js`** — it only works in Workshop's Grammar Driller. Do not
put it in a lesson's `exerciseRefs`; it will be requested and silently
skipped.

Every `fill-blank` whose answer is an open verb choice (not a fixed phrase
with only one possible completion) needs a parenthetical hint baked into
`sentence`, e.g. `"Ayer __ en el festival. (bailar)"` — otherwise the
correct answer is unrecoverable from context. This was missed across
`a2-17-01` through `a2-17-consolidation` and only caught when a learner hit
it in the Grammar Driller; check for it explicitly at B1's volume rather
than relying on a later audit to catch it again.

### Block split, per lesson

| Lesson | Practice | Reading | Listening | Dialogue | Writing | Total |
|---|---:|---:|---:|---:|---:|---:|
| 01 | 9 | — | 2 | 3 | 2 | 16 |
| 02 | 9 | — | 2 | 3 | 2 | 16 |
| 03 | 9 | — | 2 | 3 | 2 | 16 |
| 04 | 9 | — | 2 | 3 | 2 | 16 |
| 05 | 8 | 4 | 2 | 3 | 2 | 19 |
| consolidation | — (single "Review" block) | | | | | 18 |

These totals sit inside the ranges already fixed per lesson in the
Consolidated Unit List (15–17 / 15–18 / 16–18 / 16–18 / 18–20 / 18) — the
table above is the concrete split to author against so 72 units come out
consistent rather than each improvising a different mix.

- **Practice must span at least 6 distinct exercise types** (raised from
  A1's 5, since B1 draws on a wider grammar range per lesson and there are
  9 usable types to draw from).
- **Reading** exists only in lesson 05, asks about the unit's shared story,
  and its exercises carry no `teaches` tag (same rule as A1: a reading
  question is about one specific text, not a recyclable concept).
- **Listening** exercises are `listening-choice` or `dictation`, spread
  across every teaching lesson rather than concentrated in one — this is
  what actually delivers `B1_GUIDE.md` §14's listening progression (clear
  short recordings early, natural multi-speaker speech late), since there
  is no single "Listening class" slot in the six-lesson unit.
- **Consolidation's "Review" block is one exercise-group of 18**, not a
  Practice/Reading/Dialogue/Writing split — following A1's `audit_review()`
  design rather than A2's (which just repeats the teaching-lesson split).
  A1's reasoning holds at B1's scale better than A2's: every Review exercise
  must carry `teaches`, the block must span **at least 6 distinct types**,
  and the union of `teaches` tags across the block must cover **at least 10
  distinct points** (raised from A1's 8, matching a richer unit) — that
  last rule is what stops a "consolidation" being eighteen drills of the
  same one thing.

---

## 7. Story

One per unit, referenced only from lesson 05's `story` section, followed
immediately by the "Reading" exercise-group.

- **Core** stories are adapted extracts from the real works already named
  in the Consolidated Unit List (*Don Quijote*, *The Odyssey*, etc.) — file
  under `content/es/stories/classics/b1/`, `type: "classic"`.
- **Latin America** stories are adapted historical/documentary material
  (chronicles, testimonies, speeches, reports) — file under
  `content/es/stories/world/b1/`, `type: "world"`.

Neither track uses `type: "original"` at B1 — `B1_GUIDE.md` §1 is explicit
that "literary, historical and world texts replace original Parlour
stories" from this level on.

Length band, escalating across the level per `B1_GUIDE.md` §13's
early/mid/late progression (this specific banding is new — no B1 target
existed before this document):

| Units | Words |
|---|---|
| 1–12 (early B1) | 150–250 |
| 13–24 (mid B1) | 200–300 |
| 25–36 (late B1) | 250–350 |

Only previously-taught grammar and vocabulary may appear in the text — same
rule as A1, unchanged at B1: a story is where the learner reads what they
already know, not a preview of what's coming.

---

## 8. What this spec deliberately does not inherit from A1

`a1-content-spec.md` describes A1 as it existed on 2026-08-09: one file per
lesson (`a1-01.json`), with lessons 18–20 as a separate "review" format.
Since then A1 itself was restructured into the six-lessons-per-unit shape
this document describes (`a1-01-01.json` … `a1-01-consolidation.json`).

`scripts/audit-lesson.py` has been rewritten (2026-08-13) to discover units
from that id shape directly rather than from a hardcoded old-format regex,
and to check each lesson against this document for B1, `a2-lesson-guide.md`
for A2, and structurally only (no plan document exists at lesson grain) for
A1. Running `python scripts/audit-lesson.py b1-{unit}` once a unit is
written is the actual gate — see the script's own docstring for exactly
what is and isn't checked per level. Two things worth knowing before relying
on it at volume:

- **Latin America units aren't cross-checked against the plan yet.** The
  Consolidated Unit List numbers Latin America units 1–36 the same as Core,
  but lesson files use word-slug ids (§1a) that the plan document has no way
  to key by. Title/word/exercise-count checks are silently skipped for
  Latin America lessons until a slug-to-unit-number mapping exists — the
  structural checks (section order, exercise-block presence, type diversity,
  word coverage, checklist form) still run and still matter.
- **The teaching-order check ("asked for before it was taught") is a coarse
  heuristic** — it stems Spanish tokens rather than parsing morphology, so
  irregular participles and gerunds (`escrito`, `visto`, `viendo`) routinely
  read as "unseen" even when the infinitive was taught, because the stem
  doesn't match. Treat its output as a worth-a-look list, not a hard
  contract, until that's tightened.

---

## 9. Known generation pitfalls

Unit 1's first draft failed `validate-content.py` on 27 of 46 files and
needed a second full fix pass after that — every item below is a bug that
actually shipped, not a hypothetical. A generator that avoids all eleven
gets much closer to a clean pass on the first try.

1. **Every lesson file needs a top-level `"level": "B1"` field.** The
   schema requires it; the first draft omitted it from all twelve lesson
   files in the unit.
2. **`recycle` is `{"type": "recycle"}`, optionally with `title`/`count` —
   never an `items` field.** Present (and wrong) in every lesson file.
3. **`srs` is `{"type": "srs"}`, optionally with `title` — never a `ref`
   field.** Present (and wrong) in every teaching lesson.
4. **Grammar files are `{"id", "title", "sections"}` only — no top-level
   `"lesson"` field.** Present (and wrong) in every grammar file, both
   tracks.
5. **`external-link` parts take `type`, `topic`, `url`, and optionally
   `site` — never `title`.** Present (and wrong) in every Core grammar
   file.
6. **`dialogue-complete`'s `options` array must contain only plain
   strings.** A `[word, translation, pos]` vocabulary triple was pasted
   into `options[0]` in five separate exercise files instead of a real
   alternative line of dialogue.
7. **`fill-blank` sentences place the blank *inside* the sentence, where
   the target word belongs — never appended after an already-complete
   sentence.** `"La cordillera atravesaba grandes territorios __.
   (cordillera)"` is nonsense; it has to be `"La __ atravesaba grandes
   territorios. (cordillera)"`. This exact pattern shipped in ten
   exercises across the Latin America track (`ex03` and `ex08` in every
   lesson).
8. **When a lesson's exercise file has a block inserted partway through**
   (Reading, only in lesson `.05`, sitting between Practice and
   Listening), **every exercise id after that block must be renumbered
   sequentially.** Reusing an earlier id (a second `ex10`/`ex11`/`ex12`
   after the real Reading block's own `ex10`–`ex12`) silently shadows the
   real exercise when the file is read as an id-keyed map — both tracks'
   lesson-`.05` files had exactly this bug, and it also produced a false
   failure on rule #10 below, since the shadowing entry happened to carry
   a `teaches` tag the real Reading exercise didn't.
9. **No exercise's full content (every field except `id`) may be
   identical to another exercise's in the same unit.** Two variants of
   this shipped: one exercise reused verbatim across all five (or all
   four) teaching lessons of a unit with only its `id` changed, and pairs
   of adjacent lessons sharing one exercise's exact sentence.
10. **Reading-block exercises carry no `teaches` tag** (§6) — but per
    pitfall #8, this can *look* satisfied while actually being violated by
    a shadowed duplicate id. Check the ids are unique before checking the
    tags.
11. **Run `python scripts/validate-content.py` and
    `python scripts/audit-lesson.py b1-{unit}` yourself and paste the
    literal terminal output alongside the files.** Every one of the ten
    pitfalls above was claimed "validated" in the first submission, and
    none of it had actually been checked.
