# Instructions for AI coding agents (Antigravity, Gemini, etc.)

## Before every commit or push that touches `content/`

Run the schema validator and fix every failure it reports:

```
python scripts/validate-content.py --changed
```

`--changed` checks only files that differ from `origin/master` (seconds).
`python scripts/validate-content.py` checks everything (several minutes).

Why: the "Sync generated content" GitHub workflow runs the same validator as
its first step. If it fails, nothing is regenerated and the repo owner gets a
failure email per push. A `pre-push` hook in `.githooks/` runs it for you
(enable with `git config core.hooksPath .githooks`) — do not bypass it with
`--no-verify`.

## Content rules the validator enforces

- Follow the schemas in `content/<lang>/schemas/`. Do not invent ids, fields
  or shapes; copy an existing passing lesson as your template.
- Lesson ids look like `lesson.b1.01.01`, levels are uppercase (`B1`),
  vocabulary words use `lemma`, exercise files need a `lesson` field.
- Every `fill-blank`, `dictation`, and `sentence-builder` exercise MUST include
  an `english` translation field (shown to the learner once the exercise is solved).
- Do not commit empty stub lessons (`"sections": []`) or wire unfinished
  lessons into `curriculum/units/*.json` — the app would show them as empty.
- Do not hand-edit generated files (`curriculum.json`, `decks.json`,
  `stories/manifest.json`, `indexes/*` except hand-maintained `skill-registry.json`,
  `grammar-titles.json`, `verb-tense-skills.json`, `skill-prereqs.json`); the workflow regenerates them.

## Exercise metadata (`category` + `teaches`)

- Every exercise in `content/<course>/exercises/*/*.json` MUST include `category`, restricted to the six shared values: `vocabulary | grammar | reading | dialogue | writing | listening`. (In Hungarian, lesson stages such as `controlled`, `practice`, `introduce`, `check`, or content domains such as `civics` belong in the optional `stage` field, never in `category`.)
- Every non-`reading` exercise MUST include a non-empty `teaches` array of lowercase-hyphenated skill slugs (e.g. `["preterito-indefinido"]`).
- Every `teaches` slug MUST exist in `content/<course>/indexes/skill-registry.json`. Prefer existing slugs; only add a new reusable skill slug to `skill-registry.json` (and `grammar-titles.json` for grammar skills) deliberately when no existing slug fits.

