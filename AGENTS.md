# Instructions for AI coding agents (Antigravity, Gemini, etc.)

## Who does what

- **The user** is the creative authority: sets direction and gives final
  approval. Anything marked *(sign-off)* waits for the user.
- **Claude** is the project manager: plans and breaks down work, writes the
  briefs, assigns tasks, reviews output against the checks, and keeps
  ROADMAP.md, ACHIEVED.md, the docs, the rules and the checks.
- **Antigravity** does the bulk work from a brief: follows it exactly, runs
  the validator, stops at the brief's checkpoints for review, and keeps the
  records ("Project records" below). It does not change rules, skills, the
  curriculum or a task's scope on its own; it raises them instead.
- **ChatGPT** is for one-off jobs the user runs by hand (translation exports).

**Never more than 2 subagents running at once** (the user's rule). Count the
ones still running before launching another; queue the rest.

**No double work.** Nobody redoes another's task: review it and send the fixes back
through its brief. A small mistake (a few items, an obvious slip) the
reviewer may simply fix, directly or through a cheap Haiku subagent, instead
of a round trip. A fix to a class of problem lands together with its rule
in the docs and, where a machine can check it, a check, so it is never
fixed twice.

## Before every commit or push that touches `content/`

Run the schema validator and fix every failure it reports:

```
python scripts/validate-content.py --changed
```

`--changed` checks only files that differ from `origin/master` (seconds).
`python scripts/validate-content.py` checks everything (several minutes).

Then the content checks, on the units you changed:

```
python scripts/check-content.py --changed
```

It fails only on problems your change adds (give-away options, `hint == answer`, missing `english`, forms used before their screen, duplicate lemmas, bad `distractor_skills`, HU stem/article/suffix or `-ik` `*-k` errors, unmet challenge targets, copied items, glued blanks, bracketed English, wrong recurring-character gender, missing `keyVocabulary`; as suspects, B2+ meta/reader talk and `story-meta`; 6+ word quotations in non-fiction texts (`story-quote`)); pre-existing findings stay a report. `python scripts/check-content.py <course> [level] [unit id]` checks one scope (`--summary` counts it). The `.githooks/pre-push` hook runs both checks (`git config core.hooksPath .githooks`) — never bypass with `--no-verify`.

It also fails on non-course scripts (Cyrillic, Arabic, Hebrew, Thai, CJK slipped into words like `reдукció`) and duplicate story `id`s across files (keep the file a lesson's `"ref"` points to; delete or re-id the other).

**A1 story comprehension questions** are in the target language with `questionEnglish` and `optionsEnglish` (matching `options` length/order) for the Reader's "Show English" toggle (user, 2026-10-13). Stories and questions may include some untaught words since the Reader translates any word on tap.

## Project records: roadmap, achieved, docs (every agent, every session)

Stale records cost whole sessions. These rules apply to Claude, Antigravity and every subagent:

- `ROADMAP.md` ("Active & Parked Priorities"): **open work only** — never leave finished or `~~struck-through~~` text here.
- `ACHIEVED.md`: all finished work with its original item number (never reuse or renumber numbers).
- `docs/`, course guides and `AGENTS.md`: permanent specs and rules (commits and chat are not records).

**Finishing work (in the same commit as the work):**

1. **Move it to `ACHIEVED.md`** under "Completed queue items" (newest first), keeping its number and adding `— **Done <date>.**` + what changed. If only part of an item finished, delete that part from `ROADMAP.md` and log it in `ACHIEVED.md` under the item's number.
2. **Update every other entry listing the same work.** Search `ROADMAP.md` for touched skill slugs, unit/exercise ids and files; update or archive matching entries and fix any "see item N" now in `ACHIEVED.md`.
3. **Write the lesson into the docs** whenever a change fixes a class of content problem, exercise/lesson behaviour, or convention:
   - this file, § "Teaching and exercise principles" (all courses);
   - `content/es-latam/guides/editorial-style-guide.md` (Spanish) and `content/hu/HU_Content_Authoring_Template.md` (Hungarian);
   - `docs/skill-tagging-spec.md` § "Read-through conventions" and `docs/readthrough-brief.md` (tagging);
   - and a machine check in `scripts/validate-content.py` or `scripts/readthrough_check.py` where checkable.
4. **Queue unfixed findings** as a new numbered item with the exact list (ids, files, counts) — never "see the session log"; save subagent reports to `imports/review/` or `docs/` and link them.

**Shape of a queue item (model: Item 148):** Bold title with date added, 1–2 sentences of context (what, why, spec link), sub-points per open task (`*(sign-off)*`, **PARKED by the user**, **User: later**), and `State:` / `Next:` lines for multi-session work so the next chat starts without chat history.

**Verify on disk first:** Check the validator, counts or files before calling anything open or done.

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

- Every exercise in `content/<course>/exercises/*/*.json` MUST include `category`: `vocabulary | grammar | reading | dialogue | writing | listening` (HU lesson stages or domains belong in optional `stage`, never `category`).
Full spec: [docs/skill-tagging-spec.md](docs/skill-tagging-spec.md) (ROADMAP 125). In short:

- **The skill list is frozen.** Source of truth: `skills/<lang>.json` (`es-es` and `es-latam` share `skills/es.json`), with families in `skills/families.json`. Never hand-edit generated `content/<course>/indexes/skill-registry.json`, `grammar-titles.json`, or `skill-prereqs.json`; regenerate with `python scripts/build_skill_registry.py`. Adding, removing, merging, splitting, or renaming a skill requires user sign-off and an entry in `skills/frozen-<lang>.json`; after an approved merge/rename (old slug becomes an alias), run `python scripts/resolve_skill_aliases.py`.
- **`teaches`: one canonical slug** per non-`reading` exercise, chosen by **what a wrong answer shows** (tested form → grammar skill; tested word or "Which means …?" → unit vocabulary skill). Never an alias, retired slug, or skill above the exercise's level.
- **Vocabulary skills:** one per unit, named `<level>-<unit id>-vocab` from the unit's permanent `id` (never a unit number).
- **Grammar skills** carry `level`, `family`, a house-style `title`, `taught_in`, and `requires` (same/lower level, taught no later and not only on another track).
- **`distractor_skills`** (grammar choice items): record 0-based option indices that are real forms of another skill, e.g. `"distractor_skills": {"1": "ser"}`. Read-through conventions: `docs/skill-tagging-spec.md`.
- **Unit numbers in text** ("You know *X* from B1 Unit 11") follow the app's per-track numbering (`scripts/unit_numbers.py`): "<Level> Unit N" for the Nth core/only-track unit, or named track ("B1 Citizenship Unit 7"), checked by `python scripts/check_unit_refs.py <course> <level>`.
- **Titles** fit after "We recommend practicing ": lowercase unless a proper noun, plain English, <= 11 words, no colons, parentheses, separator dashes, ` / `, or unit numbers.
- **Thin skills** (< 6 exercises) warn unless `"thin_ok": "<reason, who, date>"` is in `skills/<lang>.json` and rebuilt.
- **Locked units:** `python scripts/lock_tags.py <course> <level>/<unit id> --reason "..."` records tags in `indexes/tags.lock.json`; edits fail validation and one-tag/level warnings (`python scripts/validate-content.py --warnings`) become errors.

## Wiring a new unit into the app

Authoring files alone leaves a unit invisible to the Learn tab:

1. Validate files (`python scripts/validate-content.py --changed`).
2. Append `{"id": "...", "title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}` to `content/<lang>/curriculum/units/<level>.json` (`id` is permanent lowercase-hyphenated English; add `"track"` only on multi-track levels; schema: `content/<lang>/schemas/units.schema.json`).
3. Add `<level>-<id>-vocab` to `skills/<lang>.json` (`kind`, `level`, `family` from `skills/families.json`, `title`, `unit`) and `skills/frozen-<lang>.json`, then run `python scripts/build_skill_registry.py`.
4. Run `python build-manifest.py` (or push for `sync-generated-content.yml`) to regenerate `curriculum.json`, `decks.json`, and indexes. Every level of every course uses a unit table.

## Teaching and exercise principles

- **Level tests, CEFR mock exams & placement diagnostic:** Full rules live in [docs/assessment-rules.md](docs/assessment-rules.md). In level tests, writing and speaking are feedback only (never pass/jump-ahead marks); offline production runs through `engine/production-check.js` (tests: `tests/test-leveltest-production.js`, `tests/test-cefr-exam-production.js`).
- **Placement diagnostic (`content/<course>/tests/diagnostic-test.json`):** Each core item tests one titled grammar skill at the tier's own level (`skills/<lang>.json` + `indexes/grammar-titles.json`); accents count; no `vosotros` in `es-latam`. See [docs/assessment-rules.md](docs/assessment-rules.md) and run `node tests/test-diagnostic-engine.js` before committing.

**Curriculum shape.** Level → unit → lesson (5–10 min) → exercise. Review lessons introduce nothing new. At most 20 new vocabulary items per unit, recurring naturally. Readings appear only once the learner has the language to follow them; reading-dependent exercises follow.

**Exercise progression & behaviour.** Recognise → manipulate → construct → retrieve → use; vary formats.
- Multiple choice: randomise option order; never leave the correct answer predictably on top.
- Sentence builder: tile-based, free movement; always include `english` (shown only as feedback after attempt or as an opt-in hint above 8 tiles in `engine/lessons.js`).
- Word match: natural casing (`la leche` → `milk`); capitalise only real sentences.
- Sentence-order: <= 2 per unit, natural sentences only.
- Conjugation prompts: explicit subject; accept valid alternatives (`answers` / `altAnswers`).
- `fill-blank`: `hint` goes in `hint` (only when unrecoverable, never repeating the answer; see `docs/course-generation-brief.md` § 6.4), never in `sentence`; translation goes in required `english`, never as a trailing `[English]` gloss.
- Never use a form before its `taught_in` screen (including examples and wrong options).
- Questions must be self-contained (no ambiguous pronoun without antecedent; never repeat the same question back-to-back).
- **Scenarios and written exchanges:** `content/<course>/writing-exchanges.json` and `conversation-scenarios.json` MUST define `requiredLemmas` from taught words at or before the scenario's level/units; Workshop shows readiness (`${readiness.percentage}% words learned`) and recommendations gate at capstone + >= 80% (`scripts/audit_scenario_vocabulary.py`).
- Lesson shape reference: `python scripts/audit-lesson.py a1|a2|b1` (guide, not a gate; older guides in `docs/archive/guides/`).

**Teaching style.** Short, natural grammar explanations explaining why a structure works; avoid awkward phrasing (`run on`). Context lives inside lessons/exercises.

**Latin American Spanish (`es-latam`).** No `vosotros` anywhere (readings, screens, exercises, drills, wrong options, challenges); use `ustedes`. Only `es-es` teaches `vosotros` (`check-content`: `latam-vosotros`).

**People in Spanish challenges.** Only course characters by name (`content/es-latam/characters/characters.md`: Carlos, Meg; Carlos's siblings Ana, Andreas; Meg's sisters Kaylee, Lauren) and the unit story's people; never a family member in another role; colleagues/neighbours/bosses stay unnamed (`check-content`: `character-role`, `character-extra`; `scripts/challenge_people.py`).

**Spanish regional variants.** `es-es` (*zumo, coche, ordenador, móvil, patata, billete, camarero, salón, aparcar, enfadado*) vs `es-latam` (*jugo, carro, computadora, celular, papa, boleto, mesero, sala, estacionar, enojado*; list in `scripts/course_variants.py`). `python scripts/fix_variant_vocab.py <course> <level> --write` converts a level and fixes gendered articles.

**Readings & Classics.** Keep readings concise and develop the Carlos & Meg arc naturally without untaught grammar or repeated crutches (*sonreir*). For texts with `author`, the Library prints "Adapted from <work> by <author>" unless `"about": true` (discusses writer/work) or `"inspired": true` (original story on themes). Never adapt authors dead < 70 years; `work` must be a real title, `author` in course name order (`check-content`: `story-attribution`; rulebook: `docs/unit-agent-rules.md` § 4).

**Grammar to Workshop & Product shape.** Route conjugation patterns into Workshop using shared grammar-skill IDs. Core tabs: Home, Lessons, Library, Workshop, Decks, Journey; visual rules in `DESIGN.md`.

## Adding a new course (Polish, Czech, Slovak, French, German, …)

- **Pre-lesson language infrastructure** (profiles, boot indexes, morphology contracts, dictionaries, verbs, studios, CEFR exams, live Chromium gate): follow **[docs/new-language-scaffolding.md](docs/new-language-scaffolding.md)** first so non-lesson subsystems work without defects on the first pass.
- **Generating lesson content** (units, screens, exercises, checks): read **[docs/course-generation-brief.md](docs/course-generation-brief.md)** first (supersedes older guides).

Every rule above applies everywhere and the validator enforces it. Before writing any lesson or exercise for `content/<code>/`:

1. **Schemas:** copy `content/es-es/schemas/` into `content/<code>/schemas/`, adjust only language-specific needs (e.g. extra POS), and keep the six-value `category` enum (put stage names in optional `stage`).
2. **Skills before content** (`docs/skill-tagging-spec.md`): plan permanent unit `id`s (`curriculum/units/`), define unit vocab + grammar skills in `skills/<lang>.json` + `skills/frozen-<lang>.json`, and run `python scripts/build_skill_registry.py`.
3. **Course guide:** write `content/<code>/guides/...` from `content/hu/HU_Content_Authoring_Template.md`, keeping its metadata rules pointing here.
4. **Validate after each unit:** run `python scripts/validate-content.py --changed` (fails if a course with lessons/exercises lacks schemas or `skill-registry.json`). Index scripts discover `content/` folders automatically.
5. **App wiring & challenges:** update `engine/lang.js` (`AVAILABLE`, names, locales), `build-manifest.py`, `scripts/build_translation_index.py`, and language branches in `engine/` (grep `'hu'`). Author `curriculum/challenges.json` (shape: `content/es-es/curriculum/challenges.json`) to avoid lesson-load 404 fallbacks.
