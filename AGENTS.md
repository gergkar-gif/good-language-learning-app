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


## Wiring a new unit into the app

Authoring a unit's lesson, grammar, exercise and vocabulary files is not enough: a level's unit titles, order and lesson-stem groupings are a separate list, and a lesson file nothing points at is invisible to the Learn tab (Phase 2 imperfecto content validated cleanly for a while before anyone wired it in).

1. Author and validate the files as usual (`python scripts/validate-content.py --changed`).
2. Append one entry to `content/<lang>/curriculum/units/<level>.json`: `{"title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}`. Add `"track": "core"` / `"latam"` / etc. only for a level that runs more than one parallel track. Schema: `content/<lang>/schemas/units.schema.json`.
3. Run `python build-manifest.py` (or push: `sync-generated-content.yml` does it for anything under `content/**`) to regenerate `curriculum.json`, `decks.json` and the story and grammar indexes.

No `build-manifest.py` edit is needed. A level with no units file (Hungarian A1/A2) auto-groups plain-numbered lesson files from disk (`auto_group_units()` in `build-manifest.py`), so there is nothing to hand-wire there either.

## Teaching and exercise principles

Carried over from `docs/archive/PLANNING.md`; the rules that still apply to content and exercise behaviour.

**Curriculum shape.** Level, then unit, then lesson, then exercise. A lesson takes roughly 5 to 10 minutes. Review lessons introduce nothing new (grammar, vocabulary or reading); earlier material returns through them. At most 20 new vocabulary items per unit, recurring naturally rather than mechanically repeated. A reading appears only once the learner has the language to follow it, and reading-dependent exercises come after it.

**Exercise progression.** Recognise, manipulate, construct, retrieve, use. Vary exercise types rather than testing one grammar point in one format.

**Exercise behaviour.**
- Multiple choice: randomise option order; never leave the correct answer predictably on top.
- Sentence builder: tile-based, free movement; do not show the English before the learner submits, then show it as feedback and say whether the sentence is right.
- Word match: natural casing (`la leche` to `milk`); capitalise only real sentences.
- Sentence-order exercises: at most 2 per unit, and they must produce natural sentences, never artificial word-order demonstrations.
- Conjugation prompts: never ask for a form when the subject is unclear; make it explicit.
- Accept every grammatically valid alternative (interchangeable names and nouns, and similar).
- `fill-blank` hints: add a short parenthetical to `sentence` only when the blank is genuinely unrecoverable (a brand-new noun, an ambiguous verb person or tense), and never let it repeat the answer: for the answer `mientras que` the hint is `(meanwhile)`, not `(mientras que)`. There is no typed `hint` field yet.
- A question must be answerable from the exercise itself: a pronoun with no antecedent (`ő`, `él`) makes two options equally valid, and the same question must not appear twice in a row.
- Per-level exercise shape (types per block, the review-lesson shape) is checked by `python scripts/audit-lesson.py a1|a2|b1`. Many older lessons predate it and do not all pass, so treat it as a guide, not a gate. The old prose guides are in `docs/archive/guides/`.

**Teaching style.** Grammar explanations are short, explicit and natural, and explain why a structure works, not only which form to memorise. Give concepts unfamiliar to English speakers enough explanation before drilling. Prefer natural wording (`uses`, `is used to`, `means`) over awkward phrasing such as `run on`. Context lives inside lessons and exercises, not in a separate tab.

**Latin American Spanish (`es-latam`).** No `vosotros` in readings, grammar explanations, examples or normal course content; use `ustedes` for plural "you". `vosotros` may remain in the dedicated verb drill as optional recognition. Keep vocabulary and examples broadly suitable for Latin America.

**Readings.** Early readings are short and simple. The Carlos and Meg narrative should visibly develop, including the relationship. Avoid vocabulary and grammar not yet taught, and avoid repeating the same word (`sonreir`, `sonrisa`) across readings.

**Grammar to Workshop.** After teaching a conjugation pattern, give a clear route into Workshop practice where the architecture supports it, and use the same grammar-skill IDs across lessons, exercises, Workshop and the grammar reference.

**Product shape.** Core navigation is Home, Lessons, Library, Workshop, Decks, Journey. Library is for reading, Workshop for active manipulation and production, Decks for review, and the grammar reference is a permanent lookup resource, not another lesson sequence. Visual rules live in `DESIGN.md`.

## Adding a new course (Polish, Czech, Slovak, French, German, …)

Every rule above applies to every course, and the validator enforces it the same way everywhere. A new course starts inside those rules, not outside them. Before writing any lesson or exercise for a new course `content/<code>/` (e.g. `pl`, `cs`, `sk`, `fr`, `de`):

1. **Copy the full schema set** from `content/es-es/schemas/` (the reference set) into `content/<code>/schemas/`. Adjust only what the language itself needs, such as extra parts of speech (Hungarian added `postposition`) or id patterns. **Never loosen the metadata rules:** keep the six-value `category` enum. If the course's lesson shape has stage names, put them in an optional `stage` field, as Hungarian does, never in `category`.
2. **Create `content/<code>/indexes/skill-registry.json`** (`{ "skills": {} }`) and `grammar-titles.json` (`{}`). Add each skill to the registry as you write the content that teaches it. Grammar skills should be reusable CEFR-inventory points (`genitive-plural`, `aspect-pairs`), never unit- or topic-specific slugs. Where a concept already exists in another course, reuse its naming style. Every grammar skill gets a house-style title (see above).
3. **Write a course authoring guide** (start from `content/hu/HU_Content_Authoring_Template.md`) and keep its exercise-metadata section, pointing back to this file.
4. **Run `python scripts/validate-content.py --changed` after each unit.** Once a course folder has any lesson or exercise file, the validator **fails** if its schemas or `skill-registry.json` are missing, so a course can't slip through unchecked. The build scripts (`build_grammar_index.py`, `build_grammar_guide_index.py`, `build_translation_index.py`, `audit_exercise_metadata.py`) pick up every folder under `content/` automatically.
5. **App wiring** is separate from content, and done deliberately: `engine/lang.js` (`AVAILABLE`, display names, speech locales), the course's curriculum entry in `build-manifest.py`, `_SLUG_TRACK_NAME` in `scripts/build_translation_index.py` if the course has a second B1 track, and language-specific branches elsewhere in `engine/` (grep for `'hu'` to find them: accent-sensitive grading, morphology, drillers).
