# Antigravity report: ES C1 core Unit 17 `everyday-aspect`

- **Self-read: 20 fixes** (`imports/review/es-c1-antigravity-17/self-read.md`, `imports/review/es-c1-antigravity-17/self-read-fixes.json`)
- **Model / setting:** Antigravity (Gemini), unattended C1 core run (`RUN.md`)
- **Wall-clock time:** ~7 minutes
- **Allowance:** not visible in this environment

## Files created / updated

- Brief: `imports/review/es-c1-plan/antigravity/unit-17-everyday-aspect.md`
- Skills & generated indexes: `skills/es.json`, `content/es-latam/indexes/skill-registry.json`, `content/es-latam/indexes/grammar-titles.json`, `content/es-latam/indexes/skill-prereqs.json` (updated by `set_planned_taught_in.py` for `se-aspectual -> c1-17-01-a-gr`)
- Lessons: `content/es-latam/lessons/c1/c1-17-01.json` … `c1-17-05.json`, `c1-17-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-17-01-a-gr.json` … `c1-17-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-17-01-voc.json` … `c1-17-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-17-01-ex.json` … `c1-17-05-ex.json`, `c1-17-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-17.json`
- Challenges: 6 entries added to `content/es-latam/curriculum/challenges.json` (`c1-17-01` … `c1-17-05`, `c1-17-consolidation`)
- Locks: `content/es-latam/indexes/tags.lock.json` (`C1/everyday-aspect`, 55 exercises)

## Per-lesson summary

- **c1-17-01** (NEW `se-aspectual`, `c1-17-01-a-gr`): words *el bocado, de un trago, entero, el sorbo, de una sentada, de memoria*; 8 items (7 tagged `se-aspectual`, 1 `c1-everyday-aspect-vocab`; `multiple-choice` x2, `fill-blank` x2, `matching`, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-17-02** (accidental *se*, `c1-17-02-a-gr`, recapping `pronombres-combinados` A2 Unit 25): words *derramarse, quemarse, echarse a perder, el despiste, la bandeja, el mantel, el caldo*; 8 items (`multiple-choice` x3, `fill-blank` x2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-17-03** (colloquial reactions, recap `subjunctive-emotion` A2 Unit 27, `c1-17-03-a-gr`): words *atragantarse, merendar, el antojo, el picoteo, el bizcocho, el guiso*; 8 items (`multiple-choice` x2, `fill-blank` x2, `matching`, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-17-04** (habits & changes, recap `habitos-soler` B1 Unit 5 & B1 Unit 9 and `dejar-de-infinitivo` B1 Unit 12, `c1-17-04-a-gr`): words *el café cargado, al pie de la letra, de corrido, el condimento, improvisar, el apuro*; 8 items (`multiple-choice` x3, `fill-blank` x2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-17-05** (anecdotes, recap `estar-a-punto-de` B1 Unit 1 and `volver-a-infinitivo` A2 Unit 28 & B2 Unit 23, `c1-17-05-a-gr`): words *por los pelos, al instante, salir mal, salir redondo, salvar la noche, sacar de un apuro*; 11 items (`multiple-choice` x3 + Reading `multiple-choice` x3, `fill-blank` x2, `listening-choice`, `dialogue-complete`, `sentence-builder`) + story `c1-17.json`.
- **c1-17-consolidation**: 12 items (`multiple-choice` x3, `matching`, `fill-blank` x3, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`), 7 distinct `teaches` tags (`se-aspectual`, `pronombres-combinados`, `subjunctive-emotion`, `habitos-soler`, `dejar-de-infinitivo`, `estar-a-punto-de`, `volver-a-infinitivo`, `c1-everyday-aspect-vocab` — 8 distinct tags total; `se-aspectual` has 10 items across the unit).

## Unit text (`c1-17.json`)

- **Genre:** short story with dialogue (*Relato con diálogo*)
- **Word count:** 414 Spanish words
- **Factual claims:** none (fictional everyday story with Meg, an unnamed friend *su amiga*, and Carlos in Budapest; Meg is a student, Carlos works in an office). High certainty.

## Norm claims

- `c1-17-01-a-gr`: "Without a definite or quantified object, aspectual *se* sounds odd: you say *Comió pan* (some bread), not *Se comió pan*, whereas *Se comió todo el pan* is completely natural. It is very common in speech across all varieties of Spanish and less usual in formal writing."
- `c1-17-02-a-gr`: "*se* always comes first before *me / te / le / nos / les*, and the verb agrees with the **thing** that was dropped or forgotten, not with the person (*Se me rompió el vaso* vs *Se me rompieron los vasos*)."
- `c1-17-03-a-gr`: "*menos mal que* ('thank goodness') always takes the **indicative** (*¡Menos mal que trajiste el guiso!*)."
- `c1-17-04-a-gr`: "*soler*: it is defective and is used almost exclusively in the present and imperfect (*suele*, *solía*), never in the preterite (*solió* is not used) or future (*solerá* is avoided)." and "avoid doubling it with *normalmente* or *usualmente* (*Normalmente suele tomarse…* is redundant)."
- `c1-17-05-a-gr`: "Never drop the preposition *de* in *estar a punto de* or *a* in *volver a* (*Estuve a punto cancelar* and *Volvió probarlo* are both wrong)."

## Check results

- `check-content.py es-latam c1 everyday-aspect`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (6 stems, `--with-hidden`): 0 hits (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hits
- `render_lesson.js` (6 stems): 0 `!!` errors
- `check_unit_refs.py es-latam c1 everyday-aspect --bare --named`: 0 recap references to check
- `audit-reader-coverage.js --story c1-17 --top 0`: 0 not in dictionary, 0 literal compound guess, 0 lookup throws
- `validate-content.py --changed`: 25 passed, 0 failed

## Unsure lines

- None.

## For the user

- **Accidental *se* (`c1-17-02-a-gr`):** checked `.scratch/sheet-everyday-aspect.md` and grepped all of `content/es-latam/grammar/` — the course has never taught accidental *se* (*Se me olvidaron las llaves*, *Se le cayó el vaso*) before. Lesson 02 therefore presents it as new (recapping *se* + pronoun order from A2 Unit 25 `pronombres-combinados`) and tags pronoun/agreement items `pronombres-combinados` and vocabulary items `c1-everyday-aspect-vocab`.
