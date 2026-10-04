# Skill tagging spec (ROADMAP 125)

Status: **decided with the user 2026-10-04, not yet enforced.** This is the
language-independent format every course (es, hu, and any future language)
must follow. Once the validator checks land, `scripts/validate-content.py`
enforces it and AGENTS.md § "Exercise metadata" points here.

Goal: tag once, correctly, and never redo it. Every rule below is chosen so a
new language can reproduce it mechanically and a bulk pass can't silently
make tags worse.

## The model

Three things describe what an exercise teaches:

| Axis | Where it lives | Who writes it |
|---|---|---|
| **Fine skill** | `teaches` on the exercise, exactly one slug | the author, checked by review |
| **Family** | `family` on the skill in the registry | the registry, never the exercise |
| **Level** | the exercise's folder and lesson id (`exercises/a2/…`, `a2-05`), and `level` on the skill | derived, never typed on the exercise |

Anything that can be derived is not hand-written on exercises, so it can't
drift.

## Registry (`content/<language>/indexes/skill-registry.json`)

One registry per **language**, not per course. Spanish has one registry for
es-es and es-latam. A skill that only one variant uses carries
`variant: "es-es"` or `"es-latam"`. The same pattern applies to any future
variant pair (pt-PT/pt-BR, fr-FR/fr-CA).

Every skill has:

- `kind`: `grammar` or `vocabulary`.
- `level`: the CEFR level where it's introduced (`A1` … `C1`).
- `family`: one family slug, or at most two for a vocabulary skill whose
  unit mixes topics (main one first).
- `aliases`: old slugs that resolve to this one (kept forever for stored data).
- Grammar only: `taught_in`, the grammar screen that teaches it
  (`a1-05-a-gr`). Every grammar skill is taught somewhere.
- Grammar only: `requires`, the direct prerequisites. Each one must be at the
  same or a lower level, and the graph must have no cycles.
- Optional: `variant`.

### Vocabulary skills

Exactly one per unit, slug `<level>-unitNN-vocab`, with NN as the real unit
number. Generated from the curriculum, so a new course produces them
mechanically. No named slugs (`b1-orszagma-vocab`), no per-lesson skills.

### Grammar skills: how fine

**One-explanation test:** two exercises share a skill only if the same short
explanation fixes a wrong answer on either. Too coarse = one skill needs two
explanations. Too fine = two skills share one explanation.

### Families

- **Vocabulary:** 26 topic families, `docs/skill-families-draft.md`
  (PCIC *nociones específicas* 1–20 + `daily-life`, `town-places`,
  `language`, `history`, `basics`, `ideas`). Shared by all languages.
- **Grammar:** one shared backbone of grammar areas (verb tenses, noun cases,
  pronouns, word order, clauses, …), drafted from the Council of Europe
  Reference Level Descriptions. Each language uses the subset it needs. A
  language-only family needs the user's sign-off. *Still to be drafted.*

Families get display names alongside `grammar-titles.json`.

### Frozen list

After this pass, adding, removing, merging, splitting or renaming a skill
needs the user's sign-off and a hand-checked sample of the retagged
exercises. The validator fails a registry change that isn't recorded in the
frozen list in the same commit.

## Exercises

- `teaches`: **exactly one** slug, required unless `category` is `reading`.
- **What a wrong answer shows** decides the tag, in every category
  (dialogue, listening and writing included): a tested form gets the grammar
  skill, a tested word gets the unit vocabulary skill. A "Which means …?"
  question is vocabulary, with `category: vocabulary`. Open free writing with
  no single target takes the unit vocabulary skill.
- The skill's `level` must be at or below the exercise's level (recycling
  older skills is fine; tagging a skill not yet introduced is not).
- `distractor_skills` (grammar choice items only): when a wrong option is a
  real form belonging to another skill, record it by option index, e.g.
  `"distractor_skills": {"1": "ser"}`. Random wrong words get no entry. It
  lets the learner model tell "mislearned: uses X where Y is needed" apart
  from "doesn't know Y yet".

## Coverage

Every skill should have at least **6 exercises** (per variant for Spanish),
enough to colour a map cell reliably and run a 3-item test-out with fresh
items left over. The validator warns below 6. A thin skill gets exercises
written, not merged away.

## Locking

When a unit has been reviewed, its `teaches` and `distractor_skills` go into
a generated `content/<language>/indexes/tags.lock.json`. The validator fails
any change to a locked tag unless the lock is updated in the same commit
with a reason line. New content enters unlocked and is locked once reviewed.

## What this enables: the skill map

A Kwiziq-Brainmap-style map: one cell per fine skill, grouped by family ×
level, coloured by the learner model's states (`not-yet-seen`, `weak`,
`developing`, `strong`, plus "mislearned" from `distractor_skills`).
Clicking a cell opens `taught_in`. Unlike Kwiziq's, it covers vocabulary too
(unit vocabulary skills, grouped by topic family × level). `requires` adds
test-out and inference ("strong on X, so its prerequisites are probably
known"). The map screen is a separate build (ROADMAP 131).

## A new language

Before any content: families (reuse the shared lists), the registry with
one vocabulary skill per planned unit, grammar skills with `level`,
`family`, `taught_in` and `requires`, and the frozen list. The validator
fails a course folder that has content but none of these.

## Migration (one time)

- All renames happen in this pass; each old slug becomes an alias.
- es-es and es-latam registries merge into one Spanish registry.
- Learner skill stats reset after the switch (XP, word decks, lesson
  completion and My Dictionary stay). Old stats were partly computed from
  wrong tags.
- Every exercise in es-es, es-latam and hu (~48,000) is read and given its
  single tag and its `distractor_skills`, in unit-sized batches, A1 first,
  then locked.
