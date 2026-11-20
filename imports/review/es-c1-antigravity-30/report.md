# ES C1 core Unit 30 (`politics-democracy`) — Antigravity report

- **Model & setting:** Gemini 4 Neon (Medium)
- **Wall-clock time:** ~12 minutes (09:44–09:57, including stream reconnect)
- **Allowance:** not visible in environment

## Files created / updated

- Notes: `imports/review/es-c1-plan/notes/politics-democracy.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-30-politics-democracy.md`
- Lessons: `content/es-latam/lessons/c1/c1-30-01.json` … `c1-30-05.json`, `c1-30-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-30-01-a-gr.json` … `c1-30-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-30-01-voc.json` … `c1-30-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-30-01-ex.json` … `c1-30-05-ex.json`, `c1-30-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-30.json`
- Challenges: 6 `tier1` entries added to `content/es-latam/curriculum/challenges.json`
- Tag lock: 55 exercises locked in `content/es-latam/indexes/tags.lock.json`
- Index: `content/es-latam/indexes/word-lesson-index.json`

## Per-lesson summary

- **c1-30-01** (`apodosis-condicional-literaria`, recap B2 Unit 9): screen `c1-30-01-a-gr`; words: *la deliberación, deliberar, el pleno, la moción, el quórum, el bien común*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-30-02** (`contrast-concession-connectors`, recap B1 Unit 1 + B2 Unit 30): screen `c1-30-02-a-gr`; words: *el disenso, la coalición, la oposición, la polarización, el diálogo social, la alternancia*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-30-03** (`perifrasis-pasar-a`, recap B2 Unit 23): screen `c1-30-03-a-gr`; words: *la legislatura, legislar, el proyecto de ley, el veto, la derogación, la separación de poderes*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-30-04** (`reduplicated-subjunctive`, recap B2 Unit 8 + B2 Unit 14): screen `c1-30-04-a-gr`; words: *el electorado, el escrutinio, la abstención, el escaño, el concejal, la representación*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-30-05** (`argument-markers`, recap B1 Unit 13 + A1 Unit 8 + B2 Unit 28): screen `c1-30-05-a-gr`; words: *la participación ciudadana, el referendo, la consulta popular, cívico, la convivencia democrática, la agenda pública*; 11 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, Reading `multiple-choice` ×3, `dialogue-complete`, `structured-writing`).
- **c1-30-consolidation**: 12 items covering all 5 grammar skills + `c1-politics-democracy-vocab` (`multiple-choice` ×3, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing` ×2).

## Unit text

- **Genre:** civic opening speech
- **Title:** *Discurso de apertura ante la asamblea municipal*
- **Word count:** 452 words
- **Factual claims:** none (entirely invented municipal assembly and civic address; general, uncontroversial democratic principles hedged where they are judgements; no real person, living politician, party, government, country, quotation, date, or statistic).

## Norm claims

- `c1-30-01-a-gr`: *in formal oratory and essays, *hubiera* + past participle can stand in place of *habría* + past participle in the result clause of a past counterfactual: *Si el pleno hubiera tenido quórum, hubiera aprobado la moción aquella misma tarde*. The conditional perfect (*habría aprobado*) remains the most common form.*
- `c1-30-01-a-gr`: *in standard Spanish, the *-se* form (*quisiese*, *debiese*, *hubiese aprobado*) does not replace the conditional in a result clause or polite opening.* / *Outside *querer*, *poder*, *deber* and compound *haber*, use the regular conditional (*aprobaría*, not *aprobara*).*
- `c1-30-02-a-gr`: *Set parenthetical *no obstante*, *con todo* and *ahora bien* off with commas (and usually a semicolon or full stop before them when linking two independent clauses).*
- `c1-30-03-a-gr`: *Always keep the preposition *a* after *pasar* (*pasa a ser debatido*, *pasemos a examinar*), and remember that *pasar a* marks a step that follows an earlier stage—never use it for a brand-new beginning where nothing came before (there, use *empezar a* or *comenzar a*).*
- `c1-30-04-a-gr`: *Check number agreement in *sea cual sea*: with a plural noun, ALL three words become plural (*sean cuales sean las diferencias*, never *sea cual sea las diferencias* or *sean cual sean*). Also keep both halves in the same subjunctive tense: *gane quien gane*, never *gane quien gana*.*
- `c1-30-05-a-gr`: *set each marker off with a comma and never stack two closing markers together (write *En definitiva, …*, never *En definitiva, en suma, …*).*

## Checks

- `python scripts/check-content.py es-latam c1 politics-democracy`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-30-01,c1-30-02,c1-30-03,c1-30-04,c1-30-05,c1-30-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `python scripts/check_unit_refs.py es-latam c1 politics-democracy --bare --named`: 0 recap reference(s) to check
- `python scripts/c1_known_forms.py politics-democracy`: 9 basic/English forms not separately recapped (*deber*, *haber*, *poder*, *querer*, *empezar a*, *cual*, *primero*, *only*, *after*); all substantive connectors/frames recapped with exact unit numbers
- `node scripts/render_lesson.js es-latam c1-30-01 ... c1-30-consolidation`: 0 `!!` errors; targeted review caught and fixed 4 defects (B2 Unit 30 / B2 Unit 14 / B2 Unit 28 recap openers, missing accent in `Destacaramos` -> `Destacáramos`, duplicate consequence-marker distractors in `c1-30-02.ex06` and `c1-30-consolidation.ex08`, two-fault distractor `fueron cual fueran` -> `fueran cual fueran` in `c1-30-04.ex06`).
- `python scripts/lock_tags.py es-latam c1/politics-democracy --update`: locked 55 exercise(s)
- `python scripts/validate-content.py --changed`: es-latam 24 passed, 0 failed

## Unsure Spanish lines

- None.

## For the user

- None.

---

## Block summary (Units 28–30, 3-unit chat block)

| Unit | Slug | Genre (words) | `check-content` | `unmet-words` | `unit_refs` | `validate-content` | Locked |
|---|---|---|---|---|---|---|---|
| 28 | `migration-identity` | testimony / *crónica* (567) | 0 err, 0 susp | 0 | 0 | 24 pass, 0 fail | 55 |
| 29 | `human-rights` | oversight report (492) | 0 err, 0 susp | 0 | 0 | 24 pass, 0 fail | 55 |
| 30 | `politics-democracy` | civic speech (452) | 0 err, 0 susp | 0 | 0 | 24 pass, 0 fail | 55 |

- All three units are committed and pushed to `master` (es-latam only, before Claude's read/freeze/es-es plant).
- All 18 challenges (6 per unit) are `"tier1"`.
- No blockers or open questions for the user. Next chat block starts at **Unit 31 (`art-criticism`)**.
