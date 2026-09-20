# Content schemas

Draft-07 JSON Schema for every content file the lesson engine reads. Each file
documents itself through `description` fields and carries a complete `examples`
block, so it doubles as the template to copy when authoring.

| Schema | Describes | Written by hand |
|---|---|---|
| `lesson.schema.json` | A lesson: the ordered playlist of sections | yes |
| `grammar.schema.json` | One grammar concept, rendered on one screen | yes |
| `exercises.schema.json` | All exercises for a lesson, all nine types | yes |
| `vocabulary.schema.json` | The words a lesson teaches | yes |
| `story.schema.json` | A reading text | yes |
| `drill-bank.schema.json` | A skill-organised practice bank for Workshop drillers, not tied to any one lesson | yes |

Two files in `content/es/` are **generated** and should never be edited by hand —
`python build-manifest.py` rebuilds both:

- `curriculum/curriculum.json` — the Learn tab's index, built from each lesson's
  `id`, `title`, `grammar` and `goal`. Edit those in the lesson file and rebuild.
- `stories/manifest.json` — the Library index. A story's shelf comes from the
  directory it sits in, not from any field inside it.

## Running the checks

```bash
python scripts/validate-content.py      # every file against its schema
python scripts/audit-lesson.py          # lessons against their level's content spec
python build-manifest.py                  # rebuilds indexes, reports broken refs
python scripts/build_grammar_index.py     # rebuilds Workshop's Grammar Driller pool
python scripts/build_translation_index.py # rebuilds Workshop's Translation Driller pool
```

`validate-content.py` needs `jsonschema` (`python -m pip install jsonschema`).
Both scripts exit non-zero on failure, so either can gate a commit.

Any `category:"grammar"` exercise with a `teaches` tag automatically becomes
drillable in Workshop's Grammar Driller — there is no separate registration
step — but only after `build_grammar_index.py` has been re-run, since it
reads `generated/indexes/grammar-index.json` rather than scanning content
live. Run it whenever a lesson's exercises change, same as `build-manifest.py`.

Likewise, any grammar file's `examples` items or `sentence-builder` exercise
with an `english` field automatically becomes drillable in the Translation
Driller (and, through the same sentence pool, the Vocabulary Driller's
Context mode) once `build_translation_index.py` is re-run.

`a1-01-01` (Unit 1, Lesson 1) is a reasonable lesson-file shape to copy — a
unit is six lesson files (`{level}-{unit}-01.json` … `-05.json` plus
`-consolidation.json`), not one. `scripts/audit-lesson.py` discovers units
from that id shape directly and checks each lesson against whichever
per-lesson plan document exists for its level (`a2-lesson-guide.md`, the B1
Consolidated Unit List) — see the script's own docstring for what's checked
per level and what isn't yet.

## What the schemas cannot check

JSON Schema validates one file at a time, and cannot compare two files or count
across them. Those are exactly the rules that break when authoring at volume.

| Rule | Enforced by |
|---|---|
| Each file matches its shape, required fields, known types | ✅ `validate-content.py` |
| A lesson has a non-empty `sections` array | ✅ `validate-content.py` |
| Section and grammar-part types are ones the engine renders | ✅ `validate-content.py` |
| Every `sections[].ref` resolves to a file that exists | ✅ `build-manifest.py` |
| Every `exerciseRefs` id exists in the exercises file it points at | ✅ `build-manifest.py` |
| Goal items and checklist items are one-to-one | ✅ `audit-lesson.py` |
| Exactly 4 checklist items, each beginning "I can" | ✅ `audit-lesson.py` |
| 15 exercises split Practice 6 / Reading 4 / Dialogue 3 / Writing 2 | ✅ `audit-lesson.py` |
| The practice group uses at least five *different* exercise types | ✅ `audit-lesson.py` |
| Vocabulary hits the per-lesson new-word target | ✅ `audit-lesson.py` |
| Every vocabulary lemma appears in the story | ✅ `audit-lesson.py` |
| Every vocabulary lemma appears in an exercise | ✅ `audit-lesson.py` |
| Story length is within the band for its lesson | ✅ `audit-lesson.py` |
| Grammar prose ≤ 300 words, 3–5 examples, one reference link | ✅ `audit-lesson.py` |
| No exercise is used by two groups | ✅ `audit-lesson.py` |
| Every goal is served by something between the goal and checklist screens | ❌ (judgement) |
| No two exercises in one file share an `id` | ❌ |
| `sentence-builder` `solution` holds exactly the same strings as `tiles` | ❌ |
| `sentence-order` `solution` indices are a permutation of `sentences` | ❌ |
| `multiple-choice` / `dialogue-complete` `correct` is a valid option index | ❌ |
| `fill-blank` `answer` actually fits the blank in `sentence` | ❌ |
| A lesson file's `title` matches its curriculum entry | ✅ generated, cannot drift |

## Content the engine silently drops

Three types appear in content files but are not implemented, so they render as
nothing at all — no error, just a missing screen or a missing paragraph.

| Type | Where | What happens |
|---|---|---|
| `grammar-inline` | `lessons/a1/a1-07.json` | Unknown section type; produces no screen |
| `example-inline` | `lessons/a1/a1-07.json` | Unknown section type; produces no screen |
| `reference` | `grammar/a1/a1-02,03,04-gr.json` | Not in the grammar part allowlist; the Lingolia link never renders |

`reference` overlaps with the implemented `external-link` part, which takes
`url` and an optional `title`. The two inline types predate the move to
data-only content files and have no current equivalent.

## Authoring order

The sequence a lesson's sections should follow, and why, is in
`lesson.schema.json`'s `sections` description. In short:

```
goal → grammar (one section per concept) → practice (5 different exercise
types) → vocabulary → story → reading → dialogue → writing → srs → checklist
```

Goals and the checklist bracket the lesson and must mirror each other. The
vocabulary file is the single source for both the vocabulary screen and the SRS
step — there is no separate card list.

## Known inconsistency: story paragraphs

49 of 50 stories use `{ "id": …, "text": … }` paragraphs with no `type`. One
(`original/a1/a1-01.json`) uses `{ "type": …, "speaker": …, "text": … }`.

The reader renders a paragraph as dialogue only when `type` is exactly
`"dialogue"`, so **every conversation in those 49 stories renders as narration
with no speaker labels**. The engine handles both shapes without erroring, which
is why this has gone unnoticed.

Deciding which shape is canonical is a content decision, not a code one, so the
schema currently accepts both and marks the typed shape as preferred.
