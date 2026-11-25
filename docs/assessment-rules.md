# Assessment Rules (Level Tests, CEFR Mock Exams, Placement Diagnostic)

Rules moved from `AGENTS.md` to keep the root agent instructions within context limits.

## Level tests & CEFR mock exams

- **Level tests** (`content/<course>/tests/`): every `teaches` slug is a registered skill at or below the test level (never an ad-hoc slug); one correct option per item (check that the other options are really wrong, e.g. *befejezve* vs *befejezvén*); no item above the level's taught skills; recurring characters only (HU: Károly, Meg).
- **Writing and speaking tasks** (level tests and CEFR mock exams; user, 2026-11-25): in level tests they are feedback only and never count towards the pass or jump-ahead mark. Offline they go through `engine/production-check.js`: a `targetKeywords` entry matches from the start of a word, and a word of 5+ letters may take an ending (write Hungarian/Polish/Czech targets as the stem, e.g. *tapasztalat*); 4 letters or fewer must match exactly, so don't use short words (*era*, *si*, *és*) as the only targets. Repeated words, repeated three-word runs, text copied from the test and English answers earn nothing. Tests: `tests/test-leveltest-production.js`, `tests/test-cefr-exam-production.js`.

## Placement diagnostic (`content/<course>/tests/diagnostic-test.json`)

Rules set 2026-11-10 after the Spanish audit (ROADMAP 155). **These rules apply to every course's diagnostic, present and future** (user, 2026-11-10): the engine and the review list are the same for all languages. Its job is to place a learner quickly, so every item must separate the tier's level from the one below. The exercise rules apply to it in full (one right answer, each wrong option breaks one thing, no answer copied from the passage, each course's own words, no `vosotros` in es-latam), plus:

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
