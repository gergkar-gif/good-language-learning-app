# ES C1 Core Unit 12 (`interpretation-meaning`) — Antigravity Report

- **Model / setting:** Antigravity (Gemini), default effort
- **Wall-clock time:** ~5 minutes
- **Allowance:** not visible from this environment

## Files created / updated

- Brief: `imports/review/es-c1-plan/antigravity/unit-12-interpretation-meaning.md`
- Lessons: `content/es-latam/lessons/c1/c1-12-01.json` … `c1-12-05.json`, `c1-12-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-12-01-a-gr.json` … `c1-12-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-12-01-voc.json` … `c1-12-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-12-01-ex.json` … `c1-12-05-ex.json`, `c1-12-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-12.json`
- Updated via scripts: `skills/es.json` + generated skill registries (`set_planned_taught_in.py`), `content/es-latam/curriculum/challenges.json` (6 challenges via `add_challenges.py`), `content/es-latam/indexes/tags.lock.json` (55 exercises via `lock_tags.py`)

## Per-lesson summary

- **c1-12-01** — Screen: `c1-12-01-a-gr` (**NEW** `verbos-doble-modo`, recapping *sentir que* from B2 Unit 6). Words (7): *la interpretación, sobrentender, la suposición, el contexto, implícito, explícito, la confusión*. Items (8, 6 types; 7 tagged `verbos-doble-modo`): `multiple-choice` (2), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-12-02** — Screen: `c1-12-02-a-gr` (recap `subjunctive-doubt`, B1 Unit 13). Words (6): *sospechar, la ambigüedad, ambiguo, deducir, inferir, presuponer*. Items (8, 6 types): `multiple-choice` (2), `matching`, `fill-blank` (2), `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-12-03** — Screen: `c1-12-03-a-gr` (recap `discurso-indirecto-interrogativas`, B2 Unit 17; `reporting-verbs`, B2 Unit 18). Words (6): *insinuar, la insinuación, aludir, el doble sentido, la lectura, el subtexto*. Items (8, 6 types): `multiple-choice` (2), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-12-04** — Screen: `c1-12-04-a-gr` (recap `hedging`, B2 Unit 21; `stance-adverbs`, B2 Unit 1). Words (6): *leer entre líneas, en apariencia, aparentemente, sutil, la connotación, la franqueza*. Items (8, 6 types): `multiple-choice` (3), `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-12-05** — Screen: `c1-12-05-a-gr` (recap `como-si`, B2 Unit 15). Words (6): *literal, el equívoco, la ironía, el sarcasmo, el sobreentendido, el guiño*. Items (11, 6 types): `multiple-choice` (5 incl. 3 reading), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`. Story: `c1-12.json`.
- **c1-12-consolidation** — 12 items, 7 types (`multiple-choice` 3, `matching`, `fill-blank` 3, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`), covering `verbos-doble-modo` (3 items, 10 total across the unit) plus all recapped skills and `c1-interpretation-meaning-vocab`.

## Unit text (`c1-12.json`)

- **Genre:** essay on why misunderstandings happen in written messages (invented everyday examples; no study or person named)
- **Word count:** 412 Spanish words
- **Factual claims (all general everyday observations):**
  1. Face-to-face conversation provides voice, pauses and visual cues such as a wink, which are absent in written messages. (certain — general observation)
  2. Unspoken assumptions and hurried replies make written irony or brief phrasing easy to misread. (certain — general observation)
  3. Providing explicit context or making a brief call helps reduce ambiguity on delicate matters. (certain — practical observation)

## Norm claims (exact wording on screens)

- `c1-12-01-a-gr`: "*decir que*: + indicative = report a fact (*Dice que llueve*); + subjunctive = tell someone to do something (*Dice que vengas*)." / "*sentir que*: + indicative = sense or perceive; + subjunctive = regret." / "*entender / comprender que*: + indicative = realise or grasp a fact; + subjunctive = find a reaction understandable." / "*temer(se) que*: + indicative = suspect an unwelcome fact, often with *me temo*; + subjunctive = fear something may happen." / "*suponer que*: + indicative = assume; + subjunctive = imply or entail a consequence."
- `c1-12-02-a-gr`: "affirmative *dudo que* triggers the subjunctive, while negative *no dudo (de) que* expresses certainty and takes the indicative." / "affirmative *sospechar que* takes the indicative (*Sospecho que miente*), while *no creer que* takes the subjunctive (*No creo que mienta*)."
- `c1-12-03-a-gr`: "Keep the written accent on indirect question words (*No sé qué dijo*, *Preguntó por qué lo hizo*), even though there are no question marks. Also remember *si* ('whether') never takes an accent, unlike *sí* ('yes'), and *aludir* always takes *a* before its object."
- `c1-12-04-a-gr`: "Place a comma after sentence-initial stance markers (*Aparentemente, ...*, *En apariencia, ...*, *En el fondo, ...*, *Francamente, ...*)."
- `c1-12-05-a-gr`: "Never use the present indicative (*como si no sabe*) or the present subjunctive (*como si no sepa*) after *como si*. Choose between imperfect subjunctive (same time as the main verb) and pluperfect subjunctive (earlier than the main verb)."

## Check results

- `python scripts/check-content.py es-latam c1 interpretation-meaning`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-12-01,c1-12-02,c1-12-03,c1-12-04,c1-12-05,c1-12-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `node scripts/render_lesson.js es-latam c1-12-01 ... c1-12-consolidation`: 0 `!!` errors; self-reviewed in full
- `python scripts/check_unit_refs.py es-latam c1 interpretation-meaning --bare --named`: 0 recap reference(s) to check (1 unchecked non-italicised reference to hedging from B2 Unit 21, verified against `b2-21-05-a-gr`)
- `python scripts/validate-content.py --changed`: `es-es: 1 passed, 0 failed`, `es-latam: 24 passed, 0 failed`
- `python scripts/lock_tags.py es-latam c1/interpretation-meaning --update ...`: locked 55 exercise(s)

## Unsure Spanish lines

None.

## For the user

Nothing blocking. `verbos-doble-modo` has 10 tagged items across Lesson 01 (7) and Consolidation (3); every item pins the intended meaning in the prompt or context so only one mood fits.

---

## Summary of 3-Unit Block (Units 10–12)

| Unit | ID | New skill | `check-content` | `unmet-words` | `check_es_c1_forms` | `check_unit_refs` | `validate-content` | Locked tags |
|---|---|---|---|---|---|---|---|---|
| 10 | `work-labour` | – (topic unit; notes drafted) | 0 err / 0 susp | 0 | 0 | 0 | 24/24 pass | 55 |
| 11 | `debate-information` | `dislocacion-clitica` (10 items) | 0 err / 0 susp | 0 | 0 | 0 | 25/25 pass | 55 |
| 12 | `interpretation-meaning` | `verbos-doble-modo` (10 items) | 0 err / 0 susp | 0 | 0 | 0 | 25/25 pass | 55 |

- **Anything for the user:** All three units are pushed to `master` cleanly (es-latam only, ready for Claude's review, freeze, and es-es planting). Stopping here after 3 units per `RUN.md`; start a fresh chat to pick up from Unit 13 (`health-bioethics`).
