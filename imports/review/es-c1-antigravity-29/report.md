# ES C1 core Unit 29 (`human-rights`) — Antigravity report

- **Model & setting:** Gemini 4 Neon (Medium)
- **Wall-clock time:** ~7 minutes (09:34–09:41)
- **Allowance:** not visible in environment

## Files created / updated

- Notes: `imports/review/es-c1-plan/notes/human-rights.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-29-human-rights.md`
- Lessons: `content/es-latam/lessons/c1/c1-29-01.json` … `c1-29-05.json`, `c1-29-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-29-01-a-gr.json` … `c1-29-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-29-01-voc.json` … `c1-29-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-29-01-ex.json` … `c1-29-05-ex.json`, `c1-29-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-29.json`
- Challenges: 6 `tier1` entries added to `content/es-latam/curriculum/challenges.json`
- Tag lock: 55 exercises locked in `content/es-latam/indexes/tags.lock.json`
- Index: `content/es-latam/indexes/word-lesson-index.json`

## Per-lesson summary

- **c1-29-01** (`ser-passive`, recap B1 Unit 18 + B1 Unit 6): screen `c1-29-01-a-gr`; words: *el debido proceso, vulnerar, la vulneración, la ratificación, la imparcialidad, imparcial*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-29-02** (`purpose-connectors`, recap B2 Unit 12 + B1 Unit 4): screen `c1-29-02-a-gr`; words: *la salvaguardia, la defensoría, el amparo, el acceso a la justicia, la igualdad ante la ley, la tutela*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-29-03** (`concesivas-aun-cuando`, recap B2 Unit 8): screen `c1-29-03-a-gr`; words: *la arbitrariedad, arbitrario, la denuncia, la indefensión, irrenunciable, la libertad de expresión*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-29-04** (`subjuntivo-perfecto`, recap B1 Unit 37 + B2 Unit 7): screen `c1-29-04-a-gr`; words: *la apelación, la reparación, la restitución, el fallo, el cumplimiento, la presunción de inocencia*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-29-05** (`discurso-indirecto-interrogativas`, recap B2 Unit 17): screen `c1-29-05-a-gr`; words: *indagar, la indagación, el perito, la jurisdicción, la recomendación, el seguimiento*; 11 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, Reading `multiple-choice` ×3, `dialogue-complete`, `structured-writing`).
- **c1-29-consolidation**: 12 items covering all 5 grammar skills + `c1-human-rights-vocab` (`multiple-choice` ×3, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing` ×2).

## Unit text

- **Genre:** institutional oversight report
- **Title:** *Informe anual sobre acceso a la justicia y garantías ciudadanas*
- **Word count:** 492 words
- **Factual claims:** none (entirely invented regional ombudsman office and jurisdiction; general, uncontroversial legal-protection principles hedged where they are judgements; no real person, country, government, party, law quotation, date, or statistic).

## Norm claims

- `c1-29-01-a-gr`: *The auxiliary participle *sido* NEVER changes form; only the lexical participle agrees in gender and number with the subject (*las garantías han sido respetadas*).* / *use *por* (never *de*) to introduce the body that acts: *evaluada por un comité imparcial*.*
- `c1-29-02-a-gr`: *Never use the indicative after *a fin de que*, *con el objeto de que* or *con el fin de que*: purpose clauses always take the subjunctive. And do not insert *que* when the subject does not change: write *a fin de garantizar la tutela*, not *a fin de que garantizar la tutela*.*
- `c1-29-03-a-gr`: *Keep *aun cuando* free of an accent mark: *aún cuando* is a spelling error in standard Spanish. Check whether the word can be replaced by *todavía* ('still'): if yes, write *aún*; if it means 'even' (*incluso*), write *aun*.*
- `c1-29-04-a-gr`: *In *hasta que* and *cuando* clauses referring to a future completed step, do not use the indicative (*hasta que se ha resuelto*): future reference requires the subjunctive (*hasta que se haya resuelto*).*
- `c1-29-05-a-gr`: *Never drop the written accent on the question word in an indirect question (*examinó en qué medida*, *determinó a quién*, *aclaró por qué*), even though there are no question marks. And keep *si* ('whether') unaccented, unlike *sí* ('yes').* / *write *verificó si habían cumplido*, never *verificó que si habían cumplido*.*

## Checks

- `python scripts/check-content.py es-latam c1 human-rights`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-29-01,c1-29-02,c1-29-03,c1-29-04,c1-29-05,c1-29-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `python scripts/check_unit_refs.py es-latam c1 human-rights --bare --named`: 0 recap reference(s) to check
- `python scripts/c1_known_forms.py human-rights`: 5 basic forms not separately recapped (*sido*, *todavía*, *cuando*, *haya*, *before*)
- `node scripts/render_lesson.js es-latam c1-29-01 ... c1-29-consolidation`: 0 `!!` errors; targeted review caught and fixed 6 defects (B2 Unit 12 recap coverage on `c1-29-02-a-gr`, `antes de que` unit ref on `c1-29-04-a-gr`, valid-conjecture distractor in `c1-29-05.ex09`, current-relevance distractor in `c1-29-05.ex11`, two-fault distractor in `c1-29-03.ex08`, absolute word `all` in Reading Q1 option 3).
- `python scripts/lock_tags.py es-latam c1/human-rights --update`: locked 55 exercise(s)
- `python scripts/validate-content.py --changed`: es-latam 24 passed, 0 failed

## Unsure Spanish lines

- None.

## For the user

- None.
