# ES C1 core Unit 20 (`concession-evaluation`) — Writer Report

- **Self-read:** 18 fixes (`imports/review/es-c1-antigravity-20/self-read.md`, `imports/review/es-c1-antigravity-20/self-read-fixes.json`)
- **Model / setting:** Antigravity (Gemini 3.1 Pro, default)
- **Wall-clock time:** ~10 min
- **Allowance:** not visible in environment

## Files created
- Lessons: `content/es-latam/lessons/c1/c1-20-01.json` … `c1-20-05.json`, `c1-20-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-20-01-a-gr.json` … `c1-20-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-20-01-voc.json` … `c1-20-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-20-01-ex.json` … `c1-20-05-ex.json`, `c1-20-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-20.json`
- Updated via scripts: `content/es-latam/curriculum/challenges.json` (+6), `content/es-latam/indexes/tags.lock.json` (55 exercises), `skills/es.json` + generated skill indexes (`futuro-concesivo -> c1-20-01-a-gr`, `con-lo-que-para-lo-que -> c1-20-03-a-gr`).

## Per-lesson summary
- **c1-20-01** (`futuro-concesivo`, NEW): screen `c1-20-01-a-gr`; words: *valer la pena, el lujo, exagerado, costoso, compensar, el defecto, no es para tanto* (7); types: `multiple-choice` (2), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `sentence-builder` (1).
- **c1-20-02** (`a-pesar-de`, `concesivas-aun-cuando`, contrasted with `futuro-concesivo`): screen `c1-20-02-a-gr`; words: *el sobrecosto, el desembolso, el despilfarro, el capricho, rentable, el sacrificio, así y todo* (7); types: `multiple-choice` (3), `fill-blank` (2), `listening-choice` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-20-03** (`con-lo-que-para-lo-que`, NEW): screen `c1-20-03-a-gr`; words: *desproporcionado, la tarifa, dejar mucho que desear, decepcionante, irrisorio, el reclamo, las obras* (7); types: `multiple-choice` (2), `fill-blank` (2), `dictation` (1), `matching` (1), `dialogue-complete` (1), `sentence-builder` (1).
- **c1-20-04** (`subjunctive-value-judgments` recap): screen `c1-20-04-a-gr`; words: *absurdo, lamentable, indignante, discutible, desacertado, el mérito, pasar por alto* (7); types: `multiple-choice` (3), `fill-blank` (2), `listening-choice` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-20-05** (`contrast-markers` recap + column + Reading): screen `c1-20-05-a-gr`; words: *el tranvía, el trazado, la rentabilidad, sopesar, la balanza, a fin de cuentas, todo hay que decirlo, congestionado* (8); types: `multiple-choice` (2 + 3 reading), `fill-blank` (2), `listening-choice` (1), `matching` (1), `dialogue-complete` (1), `structured-writing` (1).
- **c1-20-consolidation**: 12 items across 7 `teaches` tags (`futuro-concesivo`, `con-lo-que-para-lo-que`, `a-pesar-de`, `concesivas-aun-cuando`, `subjunctive-value-judgments`, `contrast-markers`, `c1-concession-evaluation-vocab`); types: `multiple-choice` (2), `matching` (1), `fill-blank` (3), `listening-choice` (1), `dialogue-complete` (1), `dictation` (1), `sentence-builder` (1), `structured-writing` (2).

## Unit text (`c1-20.json`: *El tranvía en la balanza*)
- **Genre:** Newspaper opinion column (original, invented unnamed city, no real city or person).
- **Word count:** 453 Spanish words.
- **Factual claims:** None about any real place, person, or study; all figures (6 months since opening, 2 years of works, 18% cost overrun, 40 min vs 14 min journey, 2 southern neighbourhoods) are fictional column details (100% fictional).

## Norm claims (exact screen wording, for RAE check)
- `c1-20-01-a-gr`: "Without the *pero* clause (or an equivalent contrast such as *sin embargo*), the verb reads as probability rather than concession."
- `c1-20-02-a-gr`: "Before a full clause, *a pesar de que* takes the indicative for a known fact and the subjunctive for an unconfirmed or hypothetical obstacle."
- `c1-20-02-a-gr`: "Never drop *que* before a conjugated verb (*pese a hubo problemas* ✗ → *pese a que hubo problemas* ✓ or *pese a los problemas* ✓). And keep *aun* unaccented in *aun cuando*: with an accent, *aún* means \"still\"."
- `c1-20-03-a-gr`: "Because both structures refer to a known, real degree, they take the **indicative**."
- `c1-20-03-a-gr`: "Adverbs like *poco*, *bien* and *mal* stay invariable."
- `c1-20-04-a-gr`: "Do not switch to the indicative just because the event really happened: *Es lamentable que subieron la tarifa* is non-standard in careful Spanish; use *Es lamentable que hayan subido* (or *subieran/subiesen*). By contrast, expressions of plain fact (*Es verdad que*, *Está claro que*) keep the indicative." (unsure — RAE NGLE notes rare regional spoken indicative with factive predicates; worded as "non-standard in careful Spanish").
- `c1-20-05-a-gr`: "And avoid putting a comma after *pero* or dropping the comma after *ahora bien* and *no obstante*."

## Check results
- `check-content.py es-latam c1 concession-evaluation`: 0 errors, 0 suspects.
- `unmet-words.js` (`--with-hidden`): 0 hits.
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hits.
- `render_lesson.js`: 0 `!!` errors.
- `check_unit_refs.py`: 0 recap references to check.
- `audit-reader-coverage.js --story c1-20`: 0 not in dictionary, 0 literal compound guesses, 0 lookup throws.
- `validate-content.py --changed`: 24/24 es-latam passed, 0 failed.
- `lock_tags.py`: 55 exercises locked.

## Spanish lines marked (unsure)
- None beyond the norm-wording note on `c1-20-04-a-gr` above.

## For the user
- None.
