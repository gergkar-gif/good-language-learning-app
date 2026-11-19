# Antigravity report: ES C1 core Unit 16 `cities-housing`

- **Self-read: 33 fixes** (`imports/review/es-c1-antigravity-16/self-read.md`, `imports/review/es-c1-antigravity-16/self-read-fixes.json`)
- **Model / setting:** Antigravity (Gemini), unattended C1 core run (`RUN.md`)
- **Wall-clock time:** ~11 minutes
- **Allowance:** not visible in this environment

## Files created / updated

- Unit notes: `imports/review/es-c1-plan/notes/cities-housing.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-16-cities-housing.md`
- Lessons: `content/es-latam/lessons/c1/c1-16-01.json` … `c1-16-05.json`, `c1-16-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-16-01-a-gr.json` … `c1-16-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-16-01-voc.json` … `c1-16-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-16-01-ex.json` … `c1-16-05-ex.json`, `c1-16-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-16.json`
- Challenges: 6 entries added to `content/es-latam/curriculum/challenges.json` (`c1-16-01` … `c1-16-05`, `c1-16-consolidation`)
- Locks: `content/es-latam/indexes/tags.lock.json` (`C1/cities-housing`, 55 exercises)
- Indexes: `content/es-latam/indexes/word-lesson-index.json`

## Per-lesson summary

- **c1-16-01** (`imperfect-vs-present-perfect`, recap B1 Unit 5): screen `c1-16-01-a-gr`; words: *el urbanismo, el casco histórico, la vivienda asequible, el alquiler vacacional, el tejido vecinal, la gentrificación, la densidad urbana*; 8 items (`multiple-choice` x2, `fill-blank` x2, `matching`, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-16-02** (`verbs-of-change`, recap B1 Unit 25): screen `c1-16-02-a-gr`; words: *el inquilino, el desalojo, la especulación inmobiliaria, el mercado inmobiliario, el área metropolitana, despoblado, insostenible*; 8 items (`multiple-choice` x3, `fill-blank` x2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-16-03** (`relativas-preposicion-el-que`, recap B1 Unit 20): screen `c1-16-03-a-gr`; words: *el plan urbanístico, la vivienda social, la zonificación, la segregación espacial, la habitabilidad, la renovación urbana, el parque de viviendas*; 8 items (`multiple-choice` x2, `fill-blank` x2, `matching`, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-16-04** (`sino-vs-pero`, recap B1 Unit 40): screen `c1-16-04-a-gr`; words: *rehabilitar, edificar, la rehabilitación, la vivienda digna, la expansión urbana, la ciudad compacta, la movilidad urbana*; 8 items (`multiple-choice` x3, `fill-blank` x2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-16-05** (`conectores-temporales-narrativos`, recap B2 Unit 2): screen `c1-16-05-a-gr`; words: *el suelo urbano, el alquiler regulado, la burbuja inmobiliaria, la plusvalía, asequible, residencial*; 11 items (`multiple-choice` x3 + Reading `multiple-choice` x3, `fill-blank` x2, `listening-choice`, `dialogue-complete`, `sentence-builder`) + story `c1-16.json`.
- **c1-16-consolidation**: 12 items (`multiple-choice` x3, `matching`, `fill-blank` x3, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`), 6 distinct `teaches` tags (`imperfect-vs-present-perfect`, `verbs-of-change`, `relativas-preposicion-el-que`, `sino-vs-pero`, `conectores-temporales-narrativos`, `c1-cities-housing-vocab`).

## Unit text (`c1-16.json`)

- **Genre:** feature report (*Reportaje urbano*)
- **Word count:** 399 Spanish words (400 tokens before 1-word self-read edit)
- **Factual claims:** none specific to any real city, country, person, institution or study; only general, widely accepted observations about urban gentrification, short-term rentals, urban sprawl and compact-city planning, hedged where judgements (`suelen`, `muchos especialistas coinciden`, `quienes defienden estas medidas sostienen`). High certainty.

## Norm claims

- `c1-16-02-a-gr`: "Avoid *ponerse* for long-term urban or economic trends: *ponerse* fits temporary states or sudden moods (*el tráfico se puso terrible*), not structural shifts. Use *volverse* or *hacerse* for lasting market changes, and *convertirse en* whenever a noun follows."
- `c1-16-03-a-gr`: "Spanish requires the preposition up front before *el que / la que / los que / las que* — and remember the contractions *del que* (*de + el que*) and *al que* (*a + el que*)."
- `c1-16-04-a-gr`: "When the second half introduces a new conjugated verb, Spanish requires *sino que*" and "using *sino* when the first clause is still true (*la vivienda es amplia, pero cara*, never *sino cara*)."
- `c1-16-05-a-gr`: "past reports take the indicative (*en cuanto se aprobó*, *conforme crecía*), while future policy projections take the present subjunctive (*en cuanto se apruebe*, *conforme avance la reforma*)."

## Check results

- `check-content.py es-latam c1 cities-housing`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (6 stems, `--with-hidden`): 0 hits (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hits
- `render_lesson.js` (6 stems): 0 `!!` errors
- `check_unit_refs.py es-latam c1 cities-housing --bare --named`: 0 wrong refs (1 unchecked non-word tense recap `You know *imperfecto* versus present perfect for change over time from B1 Unit 5`, verified against B1 Unit 5)
- `audit-reader-coverage.js --story c1-16 --top 0`: 0 not in dictionary, 0 literal compound guess, 0 lookup throws
- `validate-content.py --changed`: 24 passed, 0 failed

## Unsure lines

- None.

## For the user

- None.
