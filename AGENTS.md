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

## Exercise metadata (`category` + `teaches` + `grammar-titles.json`)

- Every exercise in `content/<course>/exercises/*/*.json` MUST include `category`, restricted to the six shared values: `vocabulary | grammar | reading | dialogue | writing | listening`. (In Hungarian, lesson stages such as `controlled`, `practice`, `introduce`, `check`, or content domains such as `civics` belong in the optional `stage` field, never in `category`.)
- Every non-`reading` exercise MUST include a non-empty `teaches` array of lowercase-hyphenated skill slugs (e.g. `["preterito-indefinido"]`).
- Every `teaches` slug MUST be a canonical skill in `content/<course>/indexes/skill-registry.json` (`validate-content.py` rejects unknown slugs as well as retired `"aliases"` slugs). Prefer existing canonical slugs; only add a new reusable skill slug when no existing slug fits.
- Every `category: "vocabulary"` exercise MUST be tagged with a `kind: "vocabulary"` unit theme slug (e.g. `["a1-unit01-vocab"]`), never a `kind: "grammar"` skill (`validate-content.py` enforces this).
- Every grammar skill in `grammar-index.json` MUST have a curated title in `content/<course>/indexes/grammar-titles.json` that fits mid-sentence after `"We recommend practicing "` (starts lowercase unless a proper noun, plain CEFR English, `<= 11` words, no colons `:`, parentheses `()`, separator dashes, ` / `, or unit numbers; `"reading"` for non-grammar skills). Run `python scripts/build_grammar_index.py --strict` when updating grammar skills.
- Every canonical skill and alias in `skill-registry.json` MUST match `^[a-z0-9]+(-[a-z0-9]+)*$`, and no single grammar skill should exceed `150` grammar exercises or `25` aliases (`build_grammar_index.py` warns on oversized catch-all skills).

