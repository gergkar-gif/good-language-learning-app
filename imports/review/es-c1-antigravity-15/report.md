# ES C1 Core Unit 15 (`ai-digital-ethics`) — Writer Report

- **Model / setting:** Antigravity (remote agent)
- **Wall-clock time:** ~7 minutes (20:38–20:45)
- **Allowance:** Not visible in environment

## Files created
- Notes: `imports/review/es-c1-plan/notes/ai-digital-ethics.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-15-ai-digital-ethics.md`
- Lessons (6): `content/es-latam/lessons/c1/c1-15-{01,02,03,04,05,consolidation}.json`
- Grammar screens (5): `content/es-latam/grammar/c1/c1-15-0{1,2,3,4,5}-a-gr.json`
- Vocabulary (5): `content/es-latam/vocabulary/c1/c1-15-0{1,2,3,4,5}-voc.json` (30 new lemmas, theme `AI & Digital Ethics`)
- Exercises (6): `content/es-latam/exercises/c1/c1-15-{01,02,03,04,05,consolidation}-ex.json` (55 exercises total)
- Story (1): `content/es-latam/stories/original/c1/c1-15.json`
- Challenges (6): added to `content/es-latam/curriculum/challenges.json` via `add_challenges.py`
- Lockfile: `content/es-latam/indexes/tags.lock.json` updated via `lock_tags.py` (55 exercises)

## Per-lesson summary
- **c1-15-01** (`opinion-verbs-mood`): screen `c1-15-01-a-gr`; vocab: *la inteligencia artificial, el algoritmo, el sesgo algorítmico, la opacidad, el modelo predictivo, la neutralidad*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-15-02** (`prepositional-phrases`): screen `c1-15-02-a-gr`; vocab: *los datos biométricos, la vigilancia masiva, la protección de datos, el reconocimiento facial, el cifrado, la filtración de datos*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-15-03** (`oraciones-hendidas-enfasis`): screen `c1-15-03-a-gr`; vocab: *la desinformación, el contenido sintético, la moderación de contenidos, la cámara de eco, la veracidad, la verificación*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-15-04** (`estilo-indirecto-ordenes`): screen `c1-15-04-a-gr`; vocab: *la auditoría algorítmica, el marco regulatorio, la ciberseguridad, la supervisión humana, la regulación tecnológica, auditar*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-15-05** (`perifrasis-dar-por-participio`): screen `c1-15-05-a-gr`; vocab: *la propiedad intelectual, el derecho al olvido, la ética tecnológica, la responsabilidad algorítmica, la discriminación algorítmica, el código abierto*; types (6): `multiple-choice` (incl. 3 Reading), `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (11 items) + story `c1-15.json`.
- **c1-15-consolidation**: 12 items, 8 types (`multiple-choice`, `listening-choice`, `matching`, `fill-blank`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing`), 6 distinct `teaches` tags.

## Unit text (`stories/original/c1/c1-15.json`)
- **Title:** *El mito de la máquina neutral*
- **Genre:** analytical essay / op-ed
- **Word count:** 429 Spanish words (5 paragraphs)
- **Factual claims (all general, uncontroversial, hedged where judgements):**
  - Predictive models learn from human-generated data that can carry historical inequalities, and opacity can amplify algorithmic discrimination (standard AI-ethics principle — high certainty).
  - Data leaks and widespread facial recognition have raised concerns about mass surveillance and data-protection rights such as the right to be forgotten (general contemporary policy debate — high certainty).
  - Synthetic content can produce convincing images, voices and text, and echo chambers reduce resistance to misinformation (general media-literacy observation — high certainty).
  - Open-source code helps detect flaws but does not by itself replace public regulation or human oversight in sensitive domains such as health, employment and justice (clearly framed as an analytical argument — high certainty).
  - No real person, company, law, study, statistic or country named.

## Norm claims (exact wording from screens, for RAE check)
- `c1-15-01-a-gr`: "Match the tense of the subjunctive to the time of the claim. After present *no considero que*, use *haya* + participle for a completed past action (*no considero que haya resuelto*); after past *no creía que*, shift to the imperfect subjunctive (*no creía que pudiera*)."
- `c1-15-02-a-gr`: "Watch the fixed prepositions: write *mediante* + noun (never *mediante de*), *en virtud de* (never *en virtud a*), and *a raíz de* (never *a raíz a* or *a raíz con*)."
- `c1-15-03-a-gr`: "Keep agreement and prepositions intact across both halves of a cleft: write *Son las plataformas las que deciden* (plural *ser* + plural *las que*) and *Es en la cámara de eco donde...* (keep *en* before the place, and use *donde* rather than *que* in careful writing)."
- `c1-15-04-a-gr`: "Check both tense sequence and plural agreement: after a past reporting verb (*ordenó*, *exigió*, *pidió*), shift to the imperfect subjunctive (*ordenó que se auditaran los sistemas*, not *se auditen* or *se auditaron*), and match the verb to a plural passive *se* subject."
- `c1-15-05-a-gr`: "Remember the two agreement traps: with *que*, *hecho* and *sentado* stay invariable (*No damos por sentado que...*); with a direct noun, the participle must agree in gender and number (*dar por cerradas las dudas*, never *cerrado las dudas*)."

## Check results
- `check-content.py es-latam c1 ai-digital-ethics`: **0 error(s), 0 suspect(s)**
- `unmet-words.js` (`--with-hidden`, all 6 stems): **0 hit(s)** (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s)**
- `check_unit_refs.py es-latam c1 ai-digital-ethics --bare --named`: **0 hit(s)**
- `render_lesson.js` (all 6 stems): **0 `!!` errors**, self-reviewed in full
- `validate-content.py --changed`: **24 passed, 0 failed**
- `lock_tags.py`: **locked C1/ai-digital-ethics: 55 exercise(s)**

## Unsure Spanish lines
None.

## For the user
Note for the RAE norm check on `c1-15-03-a-gr`: *Es en la cámara de eco que...* (so-called *que galicado*) is widely attested in Latin American speech, so the tip frames *donde* as preferred "in careful writing" rather than declaring *que* ungrammatical outright, and exercises test clear agreement/preposition faults (*Es las cámaras de eco...*, *lo que* for a plural feminine noun, missing *en*).

---

## Summary of Units 13–15 (batch of 3 units)

| Unit | Slug | Commit | Exercises locked | Story words | `check-content` | `unmet-words` | `check_es_c1_forms` | `check_unit_refs` | `validate-content` |
|---|---|---|---|---|---|---|---|---|---|
| 13 | `health-bioethics` | `0165ee10` | 55 | 455 | 0 err / 0 susp | 0 | 0 | 0 | 24 passed, 0 failed |
| 14 | `environment-climate` | `def0eda1` | 55 | 403 | 0 err / 0 susp | 0 | 0 | 0 | 24 passed, 0 failed |
| 15 | `ai-digital-ethics` | *(this commit)* | 55 | 429 | 0 err / 0 susp | 0 | 0 | 0 | 24 passed, 0 failed |

### Items flagged for the user across Units 13–15
- **Unit 13 (`health-bioethics`):** None beyond standard RAE norm review of the 5 tips (especially passive *se* agreement and *deber / deber de*).
- **Unit 14 (`environment-climate`):** `c1-14-04-a-gr` notes *informar de que* (standard) without penalising Latin American *informar que* in any exercise.
- **Unit 15 (`ai-digital-ethics`):** `c1-15-03-a-gr` notes *donde* over *que* in place clefts as preferred "in careful writing" rather than banning *que galicado* outright.
- Stopping here after 3 units per `RUN.md`. Ready for a new chat starting at Unit 16.
