# ES C1 Core Unit 10 (`work-labour`) — Antigravity Report

- **Model / setting:** Antigravity (Gemini), default effort
- **Wall-clock time:** ~11 minutes
- **Allowance:** not visible from this environment

## Files created

- Notes: `imports/review/es-c1-plan/notes/work-labour.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-10-work-labour.md`
- Lessons: `content/es-latam/lessons/c1/c1-10-01.json` … `c1-10-05.json`, `c1-10-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-10-01-a-gr.json` … `c1-10-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-10-01-voc.json` … `c1-10-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-10-01-ex.json` … `c1-10-05-ex.json`, `c1-10-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-10.json`
- Updated via scripts: `content/es-latam/curriculum/challenges.json` (6 challenges via `add_challenges.py`), `content/es-latam/indexes/tags.lock.json` (55 exercises via `lock_tags.py`), `content/es-latam/indexes/word-lesson-index.json`

## Per-lesson summary

- **c1-10-01** — Screen: `c1-10-01-a-gr` (recap `infinitive-vs-que-subjunctive`, B2 Unit 4). Words (7): *el mercado laboral, la jornada laboral, la contratación, el despido, la indemnización, la conciliación, la negociación colectiva*. Items (8, 6 types): `multiple-choice` (2), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-10-02** — Screen: `c1-10-02-a-gr` (recap `cuanto-mas-tanto-mas`, B1 Unit 2). Words (7): *la automatización, la productividad, la rotación, la capacitación, la estabilidad laboral, la trayectoria, capacitar*. Items (8, 6 types): `multiple-choice` (2), `fill-blank` (2), `matching`, `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-10-03** — Screen: `c1-10-03-a-gr` (recap `correlativos-no-solo-sino`, B1 Unit 40). Words (7): *el teletrabajo, la modalidad híbrida, la remuneración, la retención, la flexibilidad horaria, el desempeño, la sobrecarga*. Items (8, 6 types): `multiple-choice` (2), `fill-blank` (2), `matching`, `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-10-04** — Screen: `c1-10-04-a-gr` (recap `impersonal-tercera-plural-uno`, B2 Unit 21). Words (7): *por cuenta propia, las prestaciones, la subcontratación, la nómina, la antigüedad, despedir, remunerar*. Items (8, 6 types): `multiple-choice` (3), `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-10-05** — Screen: `c1-10-05-a-gr` (recap `contrast-markers`, B2 Unit 30). Words (7): *la brecha salarial, el salario mínimo, la reestructuración, la inserción laboral, el contrato indefinido, el contrato temporal, conciliar*. Items (11, 6 types): `multiple-choice` (5 incl. 3 reading), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`. Story: `c1-10.json`.
- **c1-10-consolidation** — 12 items, 7 types (`multiple-choice` 3, `matching`, `fill-blank` 3, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`), covering all 5 recap skills + `c1-work-labour-vocab`.

## Unit text (`c1-10.json`)

- **Genre:** interview (invented magazine *Revista Entorno Laboral*, invented researcher Dra. Elena Morales, unnamed country)
- **Word count:** 458 Spanish words
- **Factual claims (all general, uncontroversial, hedged with *suele* / *tiende a*):**
  1. Remote work reduces commuting time and can help balance work and family life, but without clear limits it tends to prolong connection hours and cause overload. (certain — general observation)
  2. Professional/administrative services often allow flexible hours or remote work, whereas retail, logistics and in-person service still require physical presence. (certain — general observation)
  3. Permanent contracts tend to offer greater job stability and benefits, while overuse of temporary contracts and outsourcing increases turnover. (certain — general observation)
  4. Automation tends to replace repetitive tasks and reshape existing roles rather than wiping out entire professions overnight. (certain — hedged general observation)
  5. A minimum wage sets an income floor for vulnerable sectors, but by itself does not eliminate structural issues like pay gaps or lack of pay transparency. (certain — general observation)
  6. Self-employed workers gain scheduling autonomy but manage their own income and benefits. (certain — definitional)

## Norm claims (exact wording on screens)

- `c1-10-01-a-gr`: "verbs like *permitir*, *prohibir* and *aconsejar* with an indirect object pronoun (*les permite elegir* / *les permite que elijan*) allow both patterns."
- `c1-10-02-a-gr`: "Before an adjective or verb, *cuanto* is invariable (*cuanto más estable es la contratación, menor es la rotación*); before a noun, *cuanto* agrees in gender and number with that noun (*cuanta más capacitación reciben los equipos, mayor es su productividad*). Notice that formal prose prefers *mayor* and *menor* over *más grande* or *más pequeño*, and often inserts *tanto* before the second comparator." / "In Spanish, never put *el* or *la* before *cuanto* or before the second *más / menos*."
- `c1-10-03-a-gr`: "When the second half has its own conjugated verb, you must insert *que*" / "adding *que* when there is no second verb (*no solo afecta el horario, sino que también el salario*) is ungrammatical." / "When it [*tanto A como B*] forms the subject, the verb is plural."
- `c1-10-04-a-gr`: "Every verb, reflexive pronoun (*se*) and possessive (*su*) linked to *uno / una* stays in the third person singular." / "In formal Spanish, do not mix *uno* with second-person *tu* or *te*."
- `c1-10-05-a-gr`: "All four markers [*en cambio*, *por el contrario*, *no obstante*, *ahora bien*] are separated from the clause by commas and usually follow a full stop or a semicolon, unlike *pero*."

## Check results

- `python scripts/check-content.py es-latam c1 work-labour`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-10-01,c1-10-02,c1-10-03,c1-10-04,c1-10-05,c1-10-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `node scripts/render_lesson.js es-latam c1-10-01 ... c1-10-consolidation`: 0 `!!` errors; self-reviewed in full
- `python scripts/check_unit_refs.py es-latam c1 work-labour --bare --named`: 0 recap reference(s) to check
- `python scripts/validate-content.py --changed`: `es-latam: 24 passed, 0 failed`
- `python scripts/lock_tags.py es-latam c1/work-labour --update ...`: locked 55 exercise(s)

## Unsure Spanish lines

None.

## For the user

Nothing blocking. Unit 10 (`work-labour`) is a topic unit with no new C1 skill; all 5 recapped B1/B2 skills had 0 prior C1 items.
