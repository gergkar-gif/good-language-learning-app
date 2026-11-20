# ES C1 core Unit 35 (`public-speaking`): Antigravity report

- **Model & setting:** Antigravity (remote agent, standard)
- **Wall-clock time:** ~6 minutes
- **Allowance used:** not visible in this environment

## Files created / updated

- `imports/review/es-c1-plan/notes/public-speaking.md` (drafted unit notes)
- `imports/review/es-c1-plan/antigravity/unit-35-public-speaking.md` (unit brief)
- `content/es-latam/lessons/c1/c1-35-01.json` … `c1-35-05.json`, `c1-35-consolidation.json`
- `content/es-latam/grammar/c1/c1-35-01-a-gr.json` … `c1-35-05-a-gr.json`
- `content/es-latam/vocabulary/c1/c1-35-01-voc.json` … `c1-35-05-voc.json`
- `content/es-latam/exercises/c1/c1-35-01-ex.json` … `c1-35-05-ex.json`, `c1-35-consolidation-ex.json`
- `content/es-latam/stories/original/c1/c1-35.json`
- `content/es-latam/curriculum/challenges.json` (6 `tier1` challenges added via `add_challenges.py`)
- `content/es-latam/indexes/tags.lock.json` (55 exercises locked via `lock_tags.py`)
- `content/es-latam/indexes/word-lesson-index.json`
- `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-35-01** (`sociolinguistica-tratamiento-cortesia`, recap B2 Unit 34): screen `c1-35-01-a-gr` (`grammar.c1.35.01.a`); 7 words (*el orador, el auditorio, el asistente, el estrado, distinguido, cortés, atento*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-35-02** (`inversion-enfasis-fronting`, recap B2 Unit 1): screen `c1-35-02-a-gr` (`grammar.c1.35.02.a`); 7 words (*la oratoria, la retórica, el énfasis, la apertura, la tribuna, firme, pausado*); 8 items (`multiple-choice` ×2, `fill-blank` ×2, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-35-03** (`oraciones-hendidas-enfasis`, recap B2 Unit 1): screen `c1-35-03-a-gr` (`grammar.c1.35.03.a`); 7 words (*la elocuencia, la dicción, el gesto, la mirada, la presencia, conciso, elocuente*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-35-04** (`marcadores-digresion`, recap B2 Unit 28 / B2 Unit 27): screen `c1-35-04-a-gr` (`grammar.c1.35.04.a`); 7 words (*la digresión, el paréntesis, la alocución, fluido, espontáneo, recapitular, sintetizar*); 8 items (`multiple-choice` ×3, `fill-blank`, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-35-05** (`consecutivas-de-tal-manera`, recap B2 Unit 31): screen `c1-35-05-a-gr` (`grammar.c1.35.05.a`); 7 words (*la persuasión, el aplauso, persuasivo, persuadir, cautivar, conmover, captar*); 11 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `reading` ×3, `dialogue-complete`, `sentence-builder`) + speech with commentary `c1-35.json`.
- **c1-35-consolidation**: 12 items (`multiple-choice` ×5, `fill-blank` ×2, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`) covering all 5 grammar skills + `c1-public-speaking-vocab` (6 tags).

## Unit text

- **Genre:** speech with commentary (`story.c1.35`, *El arte de hablar para que escuchen*)
- **Word count:** 418 Spanish words (6 paragraphs: 3 speech sections interleaved with 3 brief analytical commentaries; 3 English comprehension questions)
- **Factual claims:** none about real speakers, politicians, institutions, quotations, dates, or statistics; general, uncontroversial principles of public speaking and listening in an invented civic-forum setting (high certainty).

## Norm claims

- `c1-35-01-a-gr`: "Always check that every verb, clitic (*les/los*) and possessive (*su/sus*) stays in *ustedes*: never mix *ustedes* with *tú* (*les pido que revises tus notas* is an abrupt register break). In formal openings, place a comma after the vocative (*Estimados asistentes,*)."
- `c1-35-02-a-gr`: "Never add *no* after a fronted negative (*jamás no debemos* and *en ningún caso no conviene* are ungrammatical). And place the explicit subject after the verb (*solo así logrará el orador…*, not *solo así el orador logrará…*)."
- `c1-35-03-a-gr`: "When the spotlighted element is a preposition + noun (*al auditorio*, *en la pausa*), repeat the preposition or use *donde / cuando* (*es al auditorio a quien hablamos*, *es en la pausa donde respiramos*); avoid dropping the preposition (*es al auditorio quien hablamos* is ungrammatical)."
- `c1-35-04-a-gr`: "Never use *además* to signal a side remark — *además* adds a main point."
- `c1-35-05-a-gr`: "Never write *de tal modo a que* — there is no *a* before *que*."

## Check results

- `check-content.py es-latam c1 public-speaking`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (`--with-hidden`): 0 hit(s) (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `check_unit_refs.py es-latam c1 public-speaking --bare --named`: 0 recap reference(s) to check
- `c1_known_forms.py public-speaking`: 3 basic/incidental hits (`*ustedes*` A1 Unit 8, `*además*` B1 Unit 1 contrast note, English `*before*` false positive); all lesson-level structures recapped
- `render_lesson.js`: 0 `!!` errors
- `validate-content.py --changed`: 24 passed, 0 failed
- `lock_tags.py`: locked `C1/public-speaking` (55 exercises)

## Unsure lines

- `c1-35-03-a-gr` tip: "avoid dropping the preposition (*es al auditorio quien hablamos* is ungrammatical)." (unsure — while dropping *a* with *quien* is rejected in careful formal Spanish, some colloquial varieties use *que* without repeating the preposition; reviewer may confirm wording).

## For the user

- None. All checks pass and the unit is ready for review.
