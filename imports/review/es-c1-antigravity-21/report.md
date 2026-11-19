# ES C1 core Unit 21 (`irony-humour`) — Writer Report

- **Self-read:** 8 fixes (`imports/review/es-c1-antigravity-21/self-read.md`, `imports/review/es-c1-antigravity-21/self-read-fixes.json`)
- **Model / setting:** Antigravity (Gemini 3.1 Pro, default)
- **Wall-clock time:** ~5 min
- **Allowance:** not visible in environment

## Files created
- Lessons: `content/es-latam/lessons/c1/c1-21-01.json` … `c1-21-05.json`, `c1-21-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-21-01-a-gr.json` … `c1-21-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-21-01-voc.json` … `c1-21-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-21-01-ex.json` … `c1-21-05-ex.json`, `c1-21-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-21.json`
- Updated via scripts: `content/es-latam/curriculum/challenges.json` (+6), `content/es-latam/indexes/tags.lock.json` (55 exercises), `skills/es.json` + generated skill indexes (`ni-que-exclamativo -> c1-21-01-a-gr`).

## Per-lesson summary
- **c1-21-01** (`ni-que-exclamativo`, NEW): screen `c1-21-01-a-gr`; words: *irónico, tomar el pelo, burlarse de, el chiste, el millonario, el fantasma, el milagro* (7); types: `multiple-choice` (2), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `sentence-builder` (1).
- **c1-21-02** (vocabulary-led understatement & overstatement, `c1-irony-humour-vocab`): screen `c1-21-02-a-gr`; words: *la exageración, no está mal, un poquito, nada menos que, para colmo, la hazaña, en broma* (7); types: `multiple-choice` (2), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-21-03** (`subjunctive-emotion` recap + B2 Unit 6 exclamations): screen `c1-21-03-a-gr`; words: *sarcástico, qué casualidad, qué gracia, qué maravilla, a buena hora, faltaría más, el disparate* (7); types: `multiple-choice` (2), `fill-blank` (2), `dictation` (1), `matching` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-21-04** (`como-si` recap at C1 density): screen `c1-21-04-a-gr`; words: *fingir, como si nada, hacerse el tonto, la sonrisa, la risa, gracioso, en serio* (7); types: `multiple-choice` (2), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `sentence-builder` (1).
- **c1-21-05** (`rhetorical-devices` recap + satirical column + Reading): screen `c1-21-05-a-gr`; words: *la sátira, satírico, mordaz, ridiculizar, el despropósito, burocrático, la convocatoria, la agenda* (8); types: `multiple-choice` (2 + 3 reading), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-21-consolidation**: 12 items across 6 `teaches` tags (`ni-que-exclamativo`, `subjunctive-emotion`, `como-si`, `rhetorical-devices`, `futuro-concesivo`, `c1-irony-humour-vocab`); types: `multiple-choice` (2), `matching` (1), `fill-blank` (3), `listening-choice` (1), `dialogue-complete` (1), `dictation` (1), `sentence-builder` (1), `structured-writing` (2).

## Unit text (`c1-21.json`: *La reunión para reducir reuniones*)
- **Genre:** Satirical newspaper column (original, fictional unnamed company and office).
- **Word count:** 436 Spanish words.
- **Factual claims:** None about any real person, company, or institution; all figures (90-minute prep session, 14-page agenda, 32 attendees, 40-minute cable delay, 5 collective hours across two days) are fictional satirical details (100% fictional).

## Norm claims (exact screen wording, for RAE check)
- `c1-21-01-a-gr`: "Because *¡ni que...!* always presents the idea as blatantly unreal, it takes **only** the imperfect or pluperfect subjunctive—never the indicative (*¡Ni que es millonario!* ✗) and never the present subjunctive (*¡Ni que sea millonario!* ✗)."
- `c1-21-01-a-gr`: "Both *-ra* and *-se* forms are standard (*fuera / fuese*, *hubiera / hubiese*), with *-ra* much more common in everyday conversation."
- `c1-21-03-a-gr`: "Do not drop into the indicative when a *¡Qué maravilla que...!* or *¡Me encanta que...!* remark is sarcastic (*¡Qué maravilla que olvidaron el informe!* ✗ → *¡Qué maravilla que hayan olvidado el informe!* ✓). Sarcasm flips the meaning, never the subjunctive."
- `c1-21-04-a-gr`: "English \"as if he has done\" tempts learners into *como si haya hecho* (present perfect subjunctive), which is wrong in standard Spanish. Always use *hubiera* or *hubiese* after *como si* for an earlier unreal action."

## Check results
- `check-content.py es-latam c1 irony-humour`: 0 errors, 0 suspects.
- `unmet-words.js` (`--with-hidden`): 0 hits.
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hits.
- `render_lesson.js`: 0 `!!` errors.
- `check_unit_refs.py`: 0 recap references to check.
- `audit-reader-coverage.js --story c1-21`: 0 not in dictionary, 0 literal compound guesses, 0 lookup throws.
- `validate-content.py --changed`: 24/24 es-latam passed, 0 failed.
- `lock_tags.py`: 55 exercises locked.

## Spanish lines marked (unsure)
- None.

## For the user
- None.
