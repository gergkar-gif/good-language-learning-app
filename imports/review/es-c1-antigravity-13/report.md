# ES C1 Core Unit 13 (`health-bioethics`) — Writer Report

- **Model / setting:** Antigravity (remote agent)
- **Wall-clock time:** ~10 minutes (20:20–20:31)
- **Allowance:** Not visible in environment

## Files created
- Notes: `imports/review/es-c1-plan/notes/health-bioethics.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-13-health-bioethics.md`
- Lessons (6): `content/es-latam/lessons/c1/c1-13-{01,02,03,04,05,consolidation}.json`
- Grammar screens (5): `content/es-latam/grammar/c1/c1-13-0{1,2,3,4,5}-a-gr.json`
- Vocabulary (5): `content/es-latam/vocabulary/c1/c1-13-0{1,2,3,4,5}-voc.json` (30 new lemmas, theme `Health & Bioethics`)
- Exercises (6): `content/es-latam/exercises/c1/c1-13-{01,02,03,04,05,consolidation}-ex.json` (55 exercises total)
- Story (1): `content/es-latam/stories/original/c1/c1-13.json`
- Challenges (6): added to `content/es-latam/curriculum/challenges.json` via `add_challenges.py`
- Lockfile: `content/es-latam/indexes/tags.lock.json` updated via `lock_tags.py` (55 exercises)

## Per-lesson summary
- **c1-13-01** (`deber-vs-tener-que`): screen `c1-13-01-a-gr`; vocab: *la bioética, el comité de ética, la confidencialidad, la objeción de conciencia, la deontología, el código ético*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-13-02** (`antes-despues-de-que`): screen `c1-13-02-a-gr`; vocab: *el consentimiento informado, el ensayo clínico, el fármaco, el diagnóstico, prescribir, diagnosticar*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-13-03** (`a-pesar-de`): screen `c1-13-03-a-gr`; vocab: *el efecto secundario, la terapia génica, el placebo, la investigación biomédica, la eficacia, la prevención*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-13-04** (`relativas-universales-quiera`): screen `c1-13-04-a-gr`; vocab: *la patología, los cuidados paliativos, el trasplante, el donante, la equidad sanitaria, la intervención quirúrgica*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-13-05** (`pluscuamperfecto-subjuntivo-si`): screen `c1-13-05-a-gr`; vocab: *la negligencia, la salud pública, el dilema ético, la transparencia, la beneficencia, la inmunización*; types (6): `multiple-choice` (incl. 3 Reading), `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (11 items) + story `c1-13.json`.
- **c1-13-consolidation**: 12 items, 8 types (`multiple-choice`, `listening-choice`, `matching`, `fill-blank`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing`), 6 distinct `teaches` tags.

## Unit text (`stories/original/c1/c1-13.json`)
- **Title:** *Innovación médica y límites éticos*
- **Genre:** bioethics essay
- **Word count:** 455 Spanish words (5 paragraphs)
- **Factual claims (all general, uncontroversial, hedged where judgements):**
  - Gene therapy, transplants and new drugs allow treatment of conditions that previously appeared untreatable (general biomedical fact — high certainty).
  - Informed consent requires patients to understand diagnosis, possible side effects and alternatives before a clinical trial or surgery, though lengthy technical forms can turn it into a rushed formality (hedged with *suele* — high certainty).
  - Modern health systems handle large volumes of clinical and genetic data useful for prevention and public health, which creates privacy risks without strict controls (general fact — high certainty).
  - High prices of innovative treatments tend to limit access to a minority, requiring public-health systems with finite resources to balance experimental therapies against prevention and immunisation (hedged with *tiende a* — high certainty).
  - Palliative care focuses on dignity and quality of life once curative options are exhausted (general bioethical definition — high certainty).
  - No real person, institution, study, statistic or country named.

## Norm claims (exact wording from screens, for RAE check)
- `c1-13-01-a-gr`: "In careful normative usage, *deber* without *de* expresses obligation (*debe cumplir el código ético*), whereas *deber de* expresses probability or conjecture (*debe de estar en consulta* = 'must be in consultation')."
- `c1-13-01-a-gr`: "In very formal codes, *haber de* + infinitive appears as a solemn synonym of *deber*."
- `c1-13-02-a-gr`: "*antes de que* always takes the subjunctive, whether present (*antes de que se administre el fármaco*) or imperfect in a past report (*antes de que se iniciara el ensayo clínico*)."
- `c1-13-03-a-gr`: "Never drop *que* before a conjugated verb (*pese a el fármaco funciona* is wrong: write *pese a que el fármaco funciona*) and never add *que* before a noun or infinitive (*a pesar de que los riesgos* is wrong: write *a pesar de los riesgos*)."
- `c1-13-04-a-gr`: "Remember the two common slips with *cualquiera*: using singular *cualquiera que sean* before a plural noun (formal standard prefers plural *cualesquiera que sean*), and writing *cualquier que* instead of *cualquiera que* when no noun follows directly."
- `c1-13-05-a-gr`: "Never place *habría* inside the *si* clause (*Si habría actuado con transparencia* is always wrong). Both *hubiera* and *hubiese* are equally standard in formal Spanish; never treat one as incorrect against the other."

## Check results
- `check-content.py es-latam c1 health-bioethics`: **0 error(s), 0 suspect(s)**
- `unmet-words.js` (`--with-hidden`, all 6 stems): **0 hit(s)** (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s)**
- `check_unit_refs.py es-latam c1 health-bioethics --bare --named`: **0 hit(s)**
- `render_lesson.js` (all 6 stems): **0 `!!` errors**, self-reviewed in full
- `validate-content.py --changed`: **24 passed, 0 failed**
- `lock_tags.py`: **locked C1/health-bioethics: 55 exercise(s)**

## Unsure Spanish lines
None.

## For the user
Nothing blocking. Unit 13 is ready for Claude's review, RAE norm check, freeze and planting in es-es.
