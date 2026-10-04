# Skill tagging spec (ROADMAP 125)

Status: **decided with the user 2026-10-04; built and enforced the same day**
(ROADMAP 125 step 2). This is the language-independent format every course
(es, hu, and any future language) must follow. `scripts/validate-content.py`
enforces it for every author, and AGENTS.md § "Exercise metadata" points here.
Rules the existing exercises can't meet until the read-through (step 3) are
warnings for now and become errors for each unit once it's locked: one tag
per exercise, no skill above the exercise's level, no retired slug, at least
6 exercises per skill.

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

## Registry (`skills/<language>.json`)

The source of truth is `skills/<language>.json`, with the shared families in
`skills/families.json` and the frozen list in `skills/frozen-<language>.json`.
`scripts/build_skill_registry.py` generates each course's
`indexes/skill-registry.json`, `grammar-titles.json` and `skill-prereqs.json`
from it, and the validator fails if they drift. Old slugs live on as
`aliases`; slugs that aren't skills (topics, functions, catch-alls) are kept
under `retired` only until the read-through retags their exercises.

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

Exactly one per unit, slug `<level>-<unit id>-vocab`, e.g.
`a1-greetings-introductions-vocab`. Generated from the curriculum, so a
new course produces them mechanically. No per-lesson skills.

**Every unit has a permanent `id`** in `curriculum/units/<level>.json`: a
short kebab-case name for its topic (`greetings-introductions`), unique
within the level. It's set once and never changes, even if the unit moves
or its title is reworded. A unit's position in the list is *not* its
identity. Unit-number slugs (`a1-unit07-vocab`, `b1-01-vocab`) are
banned: inserting or moving a unit silently changes what they mean, and a
wrong tag can't be spotted by reading it. With a topic slug,
`a1-greetings-introductions-vocab` on a weather sentence is visibly wrong.
The old slugs become aliases. The validator fails a unit with no `id`, a
duplicate `id`, and a unit without exactly one vocabulary skill.

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
  language-only family needs the user's sign-off. Draft: 37 families,
  `docs/grammar-families-draft.md`, with the rules for choosing one.

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
  from "doesn't know Y yet". The index is 0-based, into `options` as written
  in the file (the app shuffles on render).

### Read-through conventions (settled on HU A1 unit 1, 2026-10-05)

So every unit is tagged the same way:

- **Word meaning is vocabulary.** "Which means …?", "Which word is a
  greeting?", matching pairs and fill-blanks that supply a noun get the unit
  vocabulary skill, even when the word is a pronoun or question word (*te*,
  *ki*). A choice between whole sentences whose options differ in a form
  ("Which means *You are Meg*?": *Te Meg vagy* / *Én Meg vagyok* / *Ő Meg
  van*) gets the grammar skill.
- **A choice between paradigm members** (*én / te / ő*, *ki / mi*) gets that
  paradigm's grammar skill.
- **Category follows the tag** on choice, fill-blank and builder items: a
  vocabulary tag means `category: vocabulary`, a grammar tag `grammar`.
  `dialogue`, `writing` and `listening` keep their category whatever the tag.
- **An item any answer passes** (a fill-blank accepting both *Igen* and
  *Nem*) and **open writing with no single target** take the unit vocabulary
  skill.
- **Review items keep the skill they review**, not the lesson's new skill.
- `distractor_skills` only for a wrong option that is a well-formed form of
  another grammar skill; an ungrammatical option (*Nem van Meg*) gets none.
- Applying a unit's decisions: write `{"<exercise id>": {"teaches": "<slug>",
  "category": "<only if it changes>", "ds": {...}}}` for every exercise in
  the unit and run `python scripts/apply_tags.py <course> <level>
  <decisions.json>`; it refuses a file with an exercise left undecided. Then
  `lock_tags.py`.

## Coverage

Every skill should have at least **6 exercises** (per variant for Spanish),
enough to colour a map cell reliably and run a 3-item test-out with fresh
items left over. The validator warns below 6. A thin skill gets exercises
written, not merged away.

## Locking

When a unit has been reviewed, its `teaches` and `distractor_skills` go into
`content/<course>/indexes/tags.lock.json`, written by
`python scripts/lock_tags.py <course> <level>/<unit id> --reason "..."`,
which refuses a unit that still breaks a rule. The validator fails any change
to a locked tag that isn't recorded there (re-locking takes `--update` and a
reason). New content enters unlocked and is locked once reviewed.

## What this enables: the skill map

A Kwiziq-Brainmap-style map: one cell per fine skill, grouped by family ×
level, coloured by the learner model's states (`not-yet-seen`, `weak`,
`developing`, `strong`, plus "mislearned" from `distractor_skills`).
Clicking a cell opens `taught_in`. Unlike Kwiziq's, it covers vocabulary too
(unit vocabulary skills, grouped by topic family × level). `requires` adds
test-out and inference ("strong on X, so its prerequisites are probably
known"). The map screen is a separate build (ROADMAP 131).

## A new language

Before any content: families (reuse the shared lists), a permanent `id`
on every planned unit, the registry with one vocabulary skill per unit,
grammar skills with `level`,
`family`, `taught_in` and `requires`, and the frozen list. The validator
fails a course folder that has content but none of these.

## Migration (one time)

- All renames happen in this pass; each old slug becomes an alias.
- es-es and es-latam registries merge into one Spanish registry.
- Learner skill stats: decided as a reset, built as alias folding
  (2026-10-04). Skill mastery is computed from exercise-level history joined
  through the *current* tags, so it rebuilds itself on the new skills as
  exercises are retagged, and wrong-tag noise disappears with it. The few
  stores keyed by skill slug (production evidence, level-test flags) map old
  slugs to their canonical skill through the aliases. A literal wipe would be
  undone by cloud sync, which merges stores key by key.
- Every exercise in es-es, es-latam and hu (~48,000) is read and given its
  single tag and its `distractor_skills`, in unit-sized batches, A1 first,
  then locked.
