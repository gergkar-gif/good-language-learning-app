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

It fails only on problems your change adds (give-away options, hint == answer, missing `english`, forms used before their screen, duplicate lemmas in one vocab file, bad `distractor_skills`, HU stem/article/suffix mismatches or `-ik` verb `*-k` answers, unmet words in challenge targets, copied consolidation/comprehension items, glued blanks, bracketed English in target-language lines, wrong recurring-character gender, missing `keyVocabulary` words); pre-existing findings stay a report. `python scripts/check-content.py <course> [level] [unit id]` checks one scope (`--summary` counts it). The `.githooks/pre-push` hook runs both checks (`git config core.hooksPath .githooks`) — never bypass with `--no-verify`.

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

- Every exercise in `content/<course>/exercises/*/*.json` MUST include `category`, restricted to the six shared values: `vocabulary | grammar | reading | dialogue | writing | listening`. (In Hungarian, lesson stages such as `controlled`, `practice`, `introduce`, `check`, or content domains such as `civics` belong in the optional `stage` field, never in `category`.)
The full format is [docs/skill-tagging-spec.md](docs/skill-tagging-spec.md) (ROADMAP 125). In short:

- **The skill list is frozen.** The source of truth is `skills/<lang>.json` (one per language: es-es and es-latam share `skills/es.json`), with the families in `skills/families.json`. `content/<course>/indexes/skill-registry.json`, `grammar-titles.json` and `skill-prereqs.json` are **generated** by `python scripts/build_skill_registry.py`; never edit them by hand. Adding, removing, merging, splitting or renaming a skill needs the user's sign-off and an entry in `skills/frozen-<lang>.json`; the validator fails a skill that isn't listed there. After an approved merge or rename (the old slug becomes an alias), run `python scripts/resolve_skill_aliases.py`.
- **`teaches`: exactly one canonical slug** per non-`reading` exercise, chosen by **what a wrong answer shows**, in every category: a tested form gets the grammar skill, a tested word gets the unit's vocabulary skill. A "Which means …?" question is vocabulary (`category: vocabulary`). Never an alias, a retired slug, or a skill above the exercise's level.
- **Vocabulary skills: one per unit**, named `<level>-<unit id>-vocab` from the unit's permanent `id` (e.g. `a1-greetings-introductions-vocab`). Never invent a vocabulary slug; never use a unit number.
- **Grammar skills** carry `level`, `family`, a house-style `title`, `taught_in` (the grammar screen that teaches it) and `requires` (direct prerequisites at the same or a lower level, taught no later than the skill and not only on another track). Two exercises share a skill only if the same short explanation fixes a wrong answer on either.
- **`distractor_skills`** (grammar choice items): when a wrong option is a real form of another skill, record it by option index (0-based, as written in the file), e.g. `"distractor_skills": {"1": "ser"}`. The read-through conventions (word meaning is vocabulary, category follows the tag, …) are in docs/skill-tagging-spec.md § "Read-through conventions".
- **Titles** fit mid-sentence after "We recommend practicing ": lowercase unless a proper noun, plain English, at most 11 words, no colons, parentheses, separator dashes, ` / ` or unit numbers.
- **Thin skills.** A skill with fewer than 6 exercises is a warning. If the user decides a skill may stay thin (e.g. introduced lightly, taught in depth later), add `"thin_ok": "<reason, who, date>"` to its entry in `skills/<lang>.json` and rebuild the registry.
- **Locked units.** Once a unit has been read, `python scripts/lock_tags.py <course> <level>/<unit id> --reason "..."` records its tags in `indexes/tags.lock.json`; the validator then fails any change to them, and the one-tag and level rules become errors for that unit. Until the read-through reaches a unit they're warnings (`python scripts/validate-content.py --warnings` lists them all).


## Wiring a new unit into the app

Authoring a unit's lesson, grammar, exercise and vocabulary files is not enough: a level's unit titles, order and lesson-stem groupings are a separate list, and a lesson file nothing points at is invisible to the Learn tab (Phase 2 imperfecto content validated cleanly for a while before anyone wired it in).

1. Author and validate the files as usual (`python scripts/validate-content.py --changed`).
2. Append one entry to `content/<lang>/curriculum/units/<level>.json`: `{"id": "...", "title": "...", "stems": ["<level>-<slug>-01", ..., "<level>-<slug>-consolidation"]}`. `id` is the unit's **permanent** id: one to four English words naming its topic, lowercase and hyphenated, unique within the level, never changed afterwards. Add `"track": "core"` / `"latam"` / etc. only for a level that runs more than one parallel track. Schema: `content/<lang>/schemas/units.schema.json`.
3. Add the unit's vocabulary skill `<level>-<id>-vocab` to `skills/<lang>.json` (`kind`, `level`, `family` from `skills/families.json`, `title`, `unit`) and to `skills/frozen-<lang>.json`, then run `python scripts/build_skill_registry.py`. A new unit is the one skill addition that doesn't need separate sign-off: the unit itself is the deliberate act.
4. Run `python build-manifest.py` (or push: `sync-generated-content.yml` does it for anything under `content/**` or `skills/**`) to regenerate `curriculum.json`, `decks.json` and the story and grammar indexes.

No `build-manifest.py` edit is needed. Every level of every course has a unit table (Hungarian A1/A2 since 2026-10-04).

## Teaching and exercise principles

Carried over from `docs/archive/PLANNING.md`; the rules that still apply to content and exercise behaviour.

- **Level tests** (\content/<course>/tests/\): every \	eaches\ slug is a registered skill at or below the test level (never an ad-hoc slug); one correct option per item (check that the other options are really wrong, e.g. *befejezve* vs *befejezvén*); no item above the level's taught skills; recurring characters only (HU: Károly, Meg).

**Curriculum shape.** Level, then unit, then lesson, then exercise. A lesson takes roughly 5 to 10 minutes. Review lessons introduce nothing new (grammar, vocabulary or reading); earlier material returns through them. At most 20 new vocabulary items per unit, recurring naturally rather than mechanically repeated. A reading appears only once the learner has the language to follow it, and reading-dependent exercises come after it.

**Exercise progression.** Recognise, manipulate, construct, retrieve, use. Vary exercise types rather than testing one grammar point in one format.

**Exercise behaviour.**
- Multiple choice: randomise option order; never leave the correct answer predictably on top.
- Sentence builder: tile-based, free movement; do not show the English before the learner submits, then show it as feedback and say whether the sentence is right.
- Word match: natural casing (`la leche` to `milk`); capitalise only real sentences.
- Sentence-order exercises: at most 2 per unit, and they must produce natural sentences, never artificial word-order demonstrations.
- Conjugation prompts: never ask for a form when the subject is unclear; make it explicit.
- Accept every grammatically valid alternative (interchangeable names and nouns, and similar).
- `fill-blank` hints go in the exercise's `hint` field, never in `sentence` (the engine shows it in parentheses after the blank; `validate-content.py` fails a hint written into the sentence). Add one only when the blank is genuinely unrecoverable (a brand-new noun, an ambiguous verb person or tense), and never let it repeat the answer: for the answer `mientras que` the hint is `meanwhile`, not `mientras que`. Full rules: docs/course-generation-brief.md § 6.4.
- A fill-blank's translation goes in its `english` field (required in every course, Hungarian included since 2026-10-09), never into `sentence` as a trailing `[English]` gloss (that shows the meaning before the learner tries; the validator fails it).
- Never use a form before the screen that teaches it: check the skill's `taught_in` in `skills/<lang>.json`. Example: Spanish *lo / la / los / las* are first taught at `a2-12-01-gr`, so earlier dialogues repeat the noun (*Sí, ya hemos visto el río*, not *Sí, ya lo he visto*); that goes for grammar-screen examples and wrong options too. Fixed in ES A2 units 2–6 on 2026-10-08.
- Every `sentence-builder` carries `english`. The engine shows it only as feedback after the attempt and as an opt-in hint above 8 tiles (`engine/lessons.js`), so a builder without it gives the learner no feedback.
- A question must be answerable from the exercise itself: a pronoun with no antecedent (`ő`, `él`) makes two options equally valid, and the same question must not appear twice in a row.
- **Scenarios and written exchanges:** every written exchange (`content/<course>/writing-exchanges.json`) and spoken scenario (`content/<course>/conversation-scenarios.json`) MUST define `requiredLemmas` consisting only of canonical words taught in the curriculum at or before the scenario's level/units. Scenarios are never locked in Workshop, but their cards display live vocabulary readiness (`${readiness.percentage}% words learned`). The recommendation engine dynamically gates milestone recommendations until the learner has reached the prerequisite capstone unit AND acquired $\ge 80\%$ of the required vocabulary (`scripts/audit_scenario_vocabulary.py`).
- Per-level exercise shape (types per block, the review-lesson shape) is checked by `python scripts/audit-lesson.py a1|a2|b1`. Many older lessons predate it and do not all pass, so treat it as a guide, not a gate. The old prose guides are in `docs/archive/guides/`.

**Teaching style.** Grammar explanations are short, explicit and natural, and explain why a structure works, not only which form to memorise. Give concepts unfamiliar to English speakers enough explanation before drilling. Prefer natural wording (`uses`, `is used to`, `means`) over awkward phrasing such as `run on`. Context lives inside lessons and exercises, not in a separate tab.

**Latin American Spanish (`es-latam`).** No `vosotros` anywhere in es-latam: readings, grammar explanations, examples, exercises, drills (not even as wrong options) and challenges; use `ustedes` for plural "you". Only es-es teaches `vosotros` (user, 2026-10-16). `check-content` reports it (`latam-vosotros`, exercises, screens and stories).

**Each Spanish course uses its own words (user, 2026-10-16).** es-es: *zumo, coche, ordenador, móvil, patata, billete, camarero, salón* (living room), *aparcar, enfadado*; es-latam: *jugo, carro, computadora, celular, papa, boleto, mesero, sala, estacionar, enojado*. The list is `scripts/course_variants.py`; `check-content` reports the other course's word (`course-variant`, suspect); `python scripts/fix_variant_vocab.py <course> <level> --write` converts a level and fixes the article when the gender changes (*el salón* → *la sala*), refusing what it can't place. Words both use (*conducir, chaqueta, autobús, apartamento, sándwich*) stay. Shared es-latam files written from one Spanish source (conversation scenarios, writing exchanges) are converted by their generators.

**Placement diagnostic (`content/<course>/tests/diagnostic-test.json`; rules set 2026-11-10 after the Spanish audit, ROADMAP 155).** **These rules apply to every course's diagnostic, present and future** (user, 2026-11-10): the engine and the review list are the same for all languages. Its job is to place a learner quickly, so every item must separate the tier's level from the one below. The exercise rules apply to it in full (one right answer, each wrong option breaks one thing, no answer copied from the passage, each course's own words, no `vosotros` in es-latam), plus:
- **Each core item tests one grammar skill registered at the tier's own level** in `skills/<lang>.json` (`teaches`, an array of one slug here because the learner model reads it that way). An A2 skill in the B1 tier lets an A2 learner clear B1.
- **Spread a tier over its level:** no more than three of the ten items on one family (the old B1 tier had six on the present subjunctive).
- **Typed items are closed:** give the lemma in brackets (`(tener) _____`) unless only one word can fit, and check that no better learner would write something else (*haya dicho* for *diga*). `altAnswers` holds real alternatives only. **Accents count** in typed answers (user, 2026-11-10), as in lessons and level tests; only case and spacing are ignored, so never list an unaccented spelling as an alternative. In Hungarian, never accept the *-k* form of an *-ik* verb (*lakok*), and never ask for a form that is the same in both conjugations (*láttam*) to test one of them.
- **The "Situación" line never contains the tested form.**
- **Reading:** options paraphrase the passage, wrong options are things the passage could have said, and "not stated" is the right answer at least once per course. No invented news about a named real place; a real place gets only facts that do not change (no prices, no opening hours unless checked that day).
- **Changing an item's skill means a new id**, so evidence stored under `diag:<id>` is not credited to the wrong skill. Correcting a wrong tag on an unchanged sentence keeps the id.
- **No two items in a file test the same form in the same frame**, and a stem never needs grammar from a later level (no past tense in an A1 stem).
- **Result:** pass and "nearly there" are shown as counts: 10 of 12 passes a tier (`passRatio` 0.83; user, 2026-11-10), 9 of 12 is nearly there. Nearly there places one level up with up to three missed skills as a review list, which `LearnerModel.troubleSkills()` feeds to practice suggestions for 14 days. Placement never goes to a level with no units.
- **The review list needs every core item to carry one registered grammar skill that has a title in `indexes/grammar-titles.json`**; an item without one cannot be reviewed and fails the test.
- `node tests/test-diagnostic-engine.js` finds every course with a `diagnostic-test.json` and checks these rules (one registered, titled grammar skill of the tier's level, unique ids, `altAnswers`, "not stated", `vosotros` in es-latam) plus the placement logic against the real engine. Run it before committing a diagnostic. Its `KNOWN_OPEN` list of exempt items is empty since 2026-11-10 and stays empty. `validate-content.py` still skips the file.

**Readings.** Early readings are short and simple. The Carlos and Meg narrative should visibly develop, including the relationship. Avoid vocabulary and grammar not yet taught, and avoid repeating the same word (`sonreir`, `sonrisa`) across readings.

**Grammar to Workshop.** After teaching a conjugation pattern, give a clear route into Workshop practice where the architecture supports it, and use the same grammar-skill IDs across lessons, exercises, Workshop and the grammar reference.

**Product shape.** Core navigation is Home, Lessons, Library, Workshop, Decks, Journey. Library is for reading, Workshop for active manipulation and production, Decks for review, and the grammar reference is a permanent lookup resource, not another lesson sequence. Visual rules live in `DESIGN.md`.

## Adding a new course (Polish, Czech, Slovak, French, German, …)

**Generating content (a new course, a new level or a regenerated unit): read [docs/course-generation-brief.md](docs/course-generation-brief.md) first.** It holds the lesson shape, the content rules and the checks in one place, and wins over the older guides.

Every rule above applies to every course, and the validator enforces it the same way everywhere. A new course starts inside those rules, not outside them. Before writing any lesson or exercise for a new course `content/<code>/` (e.g. `pl`, `cs`, `sk`, `fr`, `de`):

1. **Copy the full schema set** from `content/es-es/schemas/` (the reference set) into `content/<code>/schemas/`. Adjust only what the language itself needs, such as extra parts of speech (Hungarian added `postposition`) or id patterns. **Never loosen the metadata rules:** keep the six-value `category` enum. If the course's lesson shape has stage names, put them in an optional `stage` field, as Hungarian does, never in `category`.
2. **Plan the skills before any content** (docs/skill-tagging-spec.md § "A new language"): a permanent `id` for every planned unit (unit tables in `content/<code>/curriculum/units/`), and `skills/<lang>.json` with one vocabulary skill per unit and the course's grammar skills, each with `level`, `family` (reuse `skills/families.json`; a language-only family needs the user's sign-off), a house-style `title`, `taught_in` and `requires`. Grammar skills are reusable inventory points (`genitive-plural`, `aspect-pairs`) split by the one-explanation test, never unit- or topic-specific. List every skill in `skills/frozen-<lang>.json`, add the course to the source's `courses`, and run `python scripts/build_skill_registry.py` to generate the course's registry, titles and prerequisites.
3. **Write a course authoring guide** (start from `content/hu/HU_Content_Authoring_Template.md`) and keep its exercise-metadata section, pointing back to this file.
4. **Run `python scripts/validate-content.py --changed` after each unit.** Once a course folder has any lesson or exercise file, the validator **fails** if its schemas or `skill-registry.json` are missing, so a course can't slip through unchecked. The build scripts (`build_grammar_index.py`, `build_grammar_guide_index.py`, `build_translation_index.py`, `audit_exercise_metadata.py`) pick up every folder under `content/` automatically.
5. **App wiring** is separate from content, and done deliberately: `engine/lang.js` (`AVAILABLE`, display names, speech locales), the course's curriculum entry in `build-manifest.py`, `_SLUG_TRACK_NAME` in `scripts/build_translation_index.py` if the course has a second B1 track, and language-specific branches elsewhere in `engine/` (grep for `'hu'` to find them: accent-sensitive grading, morphology, drillers). The lesson engine also asks every course for `curriculum/challenges.json`, the curated Communicative Challenges (shape: `content/es-es/curriculum/challenges.json`). Write one set in the course's own setting; without the file every lesson requests it, gets a 404, and falls back to a challenge generated from the lesson's goals.
