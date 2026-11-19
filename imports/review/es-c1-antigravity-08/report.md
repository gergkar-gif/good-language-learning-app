# ES C1 Unit 8 `data-demography` — Antigravity Trial Report

- **Model:** Gemini 4 Hydrogen (High)
- **Wall-clock time:** ~35 minutes (2026-11-19 07:15 to ~07:50 UTC+7; ~20 minutes spent waiting on three `build-manifest.py` runs across all courses)
- **Allowance used:** Not visible from agent tools (no quota/allowance readout is exposed in this environment)

## Files created and updated

Created (26 unit files in `content/es-latam/` + this report):
- Grammar screens (7):
  - `content/es-latam/grammar/c1/c1-08-01-a-gr.json`
  - `content/es-latam/grammar/c1/c1-08-02-a-gr.json`
  - `content/es-latam/grammar/c1/c1-08-02-b-gr.json`
  - `content/es-latam/grammar/c1/c1-08-03-a-gr.json`
  - `content/es-latam/grammar/c1/c1-08-04-a-gr.json`
  - `content/es-latam/grammar/c1/c1-08-05-a-gr.json`
  - `content/es-latam/grammar/c1/c1-08-05-b-gr.json`
- Vocabulary files (5, theme `"demography and data"`):
  - `content/es-latam/vocabulary/c1/c1-08-01-voc.json`
  - `content/es-latam/vocabulary/c1/c1-08-02-voc.json`
  - `content/es-latam/vocabulary/c1/c1-08-03-voc.json`
  - `content/es-latam/vocabulary/c1/c1-08-04-voc.json`
  - `content/es-latam/vocabulary/c1/c1-08-05-voc.json`
- Story (1):
  - `content/es-latam/stories/original/c1/c1-08.json`
- Exercises (6):
  - `content/es-latam/exercises/c1/c1-08-01-ex.json`
  - `content/es-latam/exercises/c1/c1-08-02-ex.json`
  - `content/es-latam/exercises/c1/c1-08-03-ex.json`
  - `content/es-latam/exercises/c1/c1-08-04-ex.json`
  - `content/es-latam/exercises/c1/c1-08-05-ex.json`
  - `content/es-latam/exercises/c1/c1-08-consolidation-ex.json`
- Lessons (6):
  - `content/es-latam/lessons/c1/c1-08-01.json`
  - `content/es-latam/lessons/c1/c1-08-02.json`
  - `content/es-latam/lessons/c1/c1-08-03.json`
  - `content/es-latam/lessons/c1/c1-08-04.json`
  - `content/es-latam/lessons/c1/c1-08-05.json`
  - `content/es-latam/lessons/c1/c1-08-consolidation.json`
- Report (1):
  - `imports/review/es-c1-antigravity-08/report.md`

Updated via project scripts:
- `skills/es.json`, `content/es-latam/indexes/skill-registry.json`, `content/es-es/indexes/skill-registry.json` (`set_planned_taught_in.py es c1 data-demography`)
- `content/es-latam/curriculum/challenges.json` (`add_challenges.py`, 6 challenges `c1-08-01`..`c1-08-consolidation`)
- `content/es-latam/indexes/tags.lock.json` (`lock_tags.py`, 55 exercises locked)

Generated decks, story manifests, and `curriculum.json` were reverted via `git checkout --` before committing per the trial rules. Pre-existing unrelated local changes (`tests/pwa/test-service-worker-manifest.js`, `content/hu/tests/b2-test.json`) and `.scratch/` were left out of the commit.

## Per-lesson summary

- **`c1-08-01` Quantity and Collective Subject Agreement**
  - Screen: `c1-08-01-a-gr` (`concordancia-ad-sensum`, new; 204 text+tip words)
  - Words (7): *la encuesta, el encuestado, la población, la mayoría, el resto, la minoría, el alumnado*
  - Items (8, 6 types): `matching` (1), `fill-blank` (1), `multiple-choice` (2), `sentence-builder` (1), `listening-choice` (1), `dialogue-complete` (1), `structured-writing` (1)
- **`c1-08-02` Describing Demographic Trends Over Time**
  - Screens: `c1-08-02-a-gr` (recap `gerund-periphrases` from B2 Unit 24; 170 words), `c1-08-02-b-gr` (recap `perifrasis-llegar-a-infinitivo` from B2 Unit 25; 139 words)
  - Words (8): *el envejecimiento, envejecer, la natalidad, el descenso, descender, el repunte, progresivamente, duplicarse*
  - Items (8, 6 types): `matching` (1), `fill-blank` (2), `multiple-choice` (1), `sentence-builder` (1), `dictation` (1), `dialogue-complete` (1), `structured-writing` (1)
- **`c1-08-03` Comparing Quantities and Expectations**
  - Screen: `c1-08-03-a-gr` (`comparativas-de-lo-que`, new; 212 words)
  - Words (8): *prever, la emigración, el municipio, rural, urbano, rebasar, la proyección, la localidad*
  - Items (8, 6 types): `matching` (1), `fill-blank` (2), `multiple-choice` (1), `sentence-builder` (1), `listening-choice` (1), `dialogue-complete` (1), `structured-writing` (1)
- **`c1-08-04` Percentages, Fractions and Approximations**
  - Screen: `c1-08-04-a-gr` (recap `numbers` from A1 and partitive agreement from Lesson 1; 194 words)
  - Words (8): *el porcentaje, aproximadamente, en torno a, alrededor de, un tercio, el promedio, la proporción, el índice*
  - Items (8, 6 types): `matching` (1), `fill-blank` (1), `multiple-choice` (2), `sentence-builder` (1), `dictation` (1), `dialogue-complete` (1), `structured-writing` (1)
- **`c1-08-05` Interpreting Data With Caution**
  - Screens: `c1-08-05-a-gr` (recap `hedging` from B2 Unit 21; 142 words), `c1-08-05-b-gr` (recap `perifrasis-modales-probabilidad-epistemica` from B2 Unit 26; 118 words)
  - Words (8): *el censo, la correlación, la causalidad, el factor, concluir, reflejar, apuntar a, la prudencia*
  - Items (11, 6 types): `matching` (1), `fill-blank` (2), `multiple-choice` (1 + 3 Reading), `sentence-builder` (1), `listening-choice` (1), `dialogue-complete` (1), `structured-writing` (1)
- **`c1-08-consolidation` Unit Review: Demography and the Language of Data**
  - Items (12, 7 types, 8 `teaches` tags): `matching` (1), `multiple-choice` (2), `listening-choice` (1), `fill-blank` (4), `dictation` (1), `dialogue-complete` (1), `sentence-builder` (1), `structured-writing` (1)

Tag totals across Unit 8 (52 tagged + 3 reading = 55): `c1-data-demography-vocab`: 12, `concordancia-ad-sensum`: 10, `comparativas-de-lo-que`: 10, `gerund-periphrases`: 5, `perifrasis-llegar-a-infinitivo`: 4, `hedging`: 4, `perifrasis-modales-probabilidad-epistemica`: 4, `numbers`: 3.

## Unit text (`c1-08.json`)

- **Genre:** Data report (`Informe demográfico de una región del interior`)
- **Word count:** 458 Spanish words
- **Factual claims and certainty:**
  - All entities and figures are invented for a fictional unnamed inland region (`una región del interior`) and fictional office (`Oficina Regional de Estadística`):
    - ~40 small/medium towns surveyed via municipal census + household sample survey (invented)
    - 10-year birth-rate decline with a brief uptick 4 years earlier that did not hold (invented)
    - Over-65 share doubled in several rural municipalities to ~30 % (invented)
    - Over 20 small towns lost more inhabitants than projected; 4 urban towns exceeded projections (invented)
    - Total regional population fell ~4 %; ~1/3 of municipalities lost >100 residents/year; average household size ~2.2 (invented)
    - Surveyed 20–35-year-olds mostly cited stable work or affordable housing, the rest higher education (invented)
  - Methodological claim ("correlation does not prove causation"): general statistical principle (certain).

## Norm claims (exact screen wording)

From `c1-08-01-a-gr.json`:
- "A collective noun on its own, such as *la gente*, *el público*, *la población*, *el alumnado* or *el equipo*, is grammatically singular and takes a singular verb: *La gente opina*, never *la gente opinan*."
- "By contrast, after a partitive or quantity phrase followed by *de* and a plural noun — such as *la mayoría de los encuestados*, *la mitad de los alumnos*, *el resto de los vecinos* or *el 40 % de los hogares* — standard Spanish accepts both a singular and a plural verb. Both *La mitad de los alumnos aprobó* and *La mitad de los alumnos aprobaron* are correct."
- "The singular puts the quantity or share as a unit in the foreground; the plural puts the individual people in the foreground."
- "Keep the definite article after *de*: *la mitad de los encuestados*, not *la mitad de encuestados*."
- "First, treating *la gente* or *la población* like English \"people\" and adding a plural verb (*la gente dicen* is rejected). Second, dropping the article after *de* in a partitive (*la mayoría de encuestados* instead of *la mayoría de los encuestados*): the noun after *de* needs its article."

From `c1-08-02-a-gr.json`:
- "With a reflexive verb like *duplicarse*, place the pronoun before *ir* or attach it to the gerund: *El número de mayores se va duplicando*."

From `c1-08-02-b-gr.json`:
- "Do not drop the preposition *a* before the infinitive: *llegó a superar*, never *llegó superar*."

From `c1-08-03-a-gr.json`:
- "When you compare against a whole clause (often with *esperarse*, *prever* or *calcular*), use *más de lo que* or *menos de lo que*: *La población descendió más de lo que se preveía*."
- "When a noun sits right before the comparison, the relative agrees with that noun in gender and number: *más dinero del que*, *más personas de las que*, *menos hogares de los que*, *menos ayuda de la que*."
- "When you compare two nouns, times or people directly, keep *que* (*más que el año pasado*, *más que Ana*, never *más de Ana*)."
- "Before a number in an affirmative sentence, use *de* (*más de cien municipios*, *menos de veinte hogares*)."
- "First, leaving *del que* unchanged before a feminine or plural noun: say *más personas de las que*, never *más personas del que*. Second, using *de* between two nouns or people (*más que Ana*, never *más de Ana*), or using *que* before a plain number (*más de cien*, not *más que cien*)."

From `c1-08-04-a-gr.json`:
- "Percentages normally take the masculine singular article *el* or *un* (*el 40 % de los hogares*, *un porcentaje del 15 %*), with a space before the *%* sign in Spanish."
- "Notice that *rondar* takes a direct object without *a* (*la tasa ronda los diez puntos*, not *ronda a los diez puntos*), whereas *en torno* and *alrededor* require *a* and *de* respectively."
- "learners sometimes drop *a* in *en torno a* or *de* in *alrededor de*, or add an extra *a* after *rondar* (*ronda a los veinte* is wrong; say *ronda los veinte*)."
- "after *el 40 % de los municipios*, both singular and plural verbs are accepted, while *un tercio de la población* (singular complement) takes a singular verb."

From `c1-08-05-a-gr.json`:
- "affirmative *parece que* and *todo apunta a que* take the indicative, whereas negated *no permiten concluir que* or *no significa que* take the subjunctive."
- "*los datos indican que hay* (indicative), but *los datos no permiten concluir que haya* (subjunctive)."

From `c1-08-05-b-gr.json`:
- "In careful writing, *deber de* + infinitive is preferred for probability (*debe de reflejar* = \"must reflect, judging by the evidence\"), while *deber* + infinitive without *de* is used for obligation. Although *deber* without *de* is also used for guesses, *deber de* for obligation is rejected."

## Check results

- `python scripts/check-content.py es-latam c1 data-demography`: `0 error(s), 0 suspect(s)`
- `node scripts/unmet-words.js es-latam c1 --stems c1-08-01,c1-08-02,c1-08-03,c1-08-04,c1-08-05,c1-08-consolidation --with-hidden`: `[]` (0 hits)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: `0 hit(s) before their screen`
- `python scripts/check_unit_refs.py es-latam c1 data-demography --bare --named`: `0 recap reference(s) to check`
- `node scripts/render_lesson.js es-latam c1-08-01 c1-08-02 c1-08-03 c1-08-04 c1-08-05 c1-08-consolidation`: all 6 lessons rendered cleanly, `0` `!!` errors
- `node scripts/audit-reader-coverage.js es-latam --story c1-08 --top 0`: `458 tokens, 247 unique words`, `0` not in dictionary, `0` literal compound guess only, `0` lookup throws
- `python scripts/validate-content.py --changed`: `es-latam: 26 passed, 0 failed`, `All content files match their schemas`
- `python scripts/lock_tags.py es-latam c1/data-demography --update --reason "new unit, written 2026-11 (ES C1 core)"`: `locked C1/data-demography: 55 exercise(s)`
- `tests/drills/`: `test-home-recommendation-profiles.js` (33/33), `test-learner-signals.js` (all passed), `test-scenario-learner-path.js` (all passed), `test-study-plan.js` (all passed)

## Spanish lines to review (`(unsure)`)

- `c1-08-02.ex07` (structured-writing answer): *"El descenso llegó a duplicarse."* — (unsure) whether a native reviewer prefers *"La caída / la tasa de envejecimiento llegó a duplicarse"* over *"El descenso llegó a duplicarse"*.
- `c1-08-03.ex07` (structured-writing answer): *"Más localidades rurales rebasaron el límite de las que preveía el estudio."* — (unsure) splitting `localidades rurales` and `de las que` around `rebasaron el límite` is grammatical, though *"Más localidades rurales de las que preveía el estudio rebasaron el límite"* or *"Rebasaron el límite más localidades rurales de las que preveía el estudio"* may read more smoothly.
- `c1-08-05.ex11` (fill-blank): *"La diferencia entre localidades debe de reflejar un sesgo en la muestra."* — (unsure) `debe de` vs `debe`: both are accepted by the RAE for probability, so a learner typing without `de` in a fill-blank only works here because the prompt supplies `debe ____` with hint `"preposition marking probability after deber"`.

## For the user

- **Where the plan did not fit:** Lesson 04's plan asks to recap "`numbers`-family skills the sheet lists (B1/B2)", but `skills/es.json` has no B1 or B2 `numbers-quantity` skills — only `numbers` (`A1`, `a1-12-01-numbers-gr`) and `concordancia-ad-sensum` (taught in Lesson 01 of this unit). Lesson 04 recaps `numbers` from A1 and partitive agreement from Lesson 01, and tags items with `c1-data-demography-vocab`, `numbers`, and `concordancia-ad-sensum`.
- **What cost the most in this brief & what to cut:**
  1. `python build-manifest.py` rebuilds all 8 courses/skeletons (~3–10 minutes per run; ~20 minutes total across the three runs needed for the knowledge sheet and unmet-words verification). Adding or documenting a `--course es-latam` flag for unit authoring would save most of the wall-clock time.
  2. `git pull --rebase origin master` fails if the checkout already has unrelated uncommitted changes (here `tests/pwa/test-service-worker-manifest.js`); specifying `git pull --rebase --autostash origin master` or checking `git merge --ff-only origin/master` first avoids friction.
  3. The "(B1/B2)" label on `numbers`-family skills in Lesson 04's unit notes can be cut/corrected to "A1 `numbers` + Lesson 1 `concordancia-ad-sensum`".
