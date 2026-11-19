# ES C1 Core Unit 14 (`environment-climate`) — Writer Report

- **Model / setting:** Antigravity (remote agent)
- **Wall-clock time:** ~7 minutes (20:31–20:38)
- **Allowance:** Not visible in environment

## Files created
- Notes: `imports/review/es-c1-plan/notes/environment-climate.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-14-environment-climate.md`
- Lessons (6): `content/es-latam/lessons/c1/c1-14-{01,02,03,04,05,consolidation}.json`
- Grammar screens (5): `content/es-latam/grammar/c1/c1-14-0{1,2,3,4,5}-a-gr.json`
- Vocabulary (5): `content/es-latam/vocabulary/c1/c1-14-0{1,2,3,4,5}-voc.json` (30 new lemmas, theme `Environment & Climate Policy`)
- Exercises (6): `content/es-latam/exercises/c1/c1-14-{01,02,03,04,05,consolidation}-ex.json` (55 exercises total)
- Story (1): `content/es-latam/stories/original/c1/c1-14.json`
- Challenges (6): added to `content/es-latam/curriculum/challenges.json` via `add_challenges.py`
- Lockfile: `content/es-latam/indexes/tags.lock.json` updated via `lock_tags.py` (55 exercises)

## Per-lesson summary
- **c1-14-01** (`futuro-perfecto`): screen `c1-14-01-a-gr`; vocab: *las emisiones, la neutralidad climática, la transición energética, la eficiencia energética, la red eléctrica, la electrificación*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-14-02** (`hypothetical-structures`): screen `c1-14-02-a-gr`; vocab: *el impuesto al carbono, los combustibles fósiles, la mitigación, la adaptación climática, la cuota de emisión, incentivar*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-14-03** (`pasiva-refleja`): screen `c1-14-03-a-gr`; vocab: *el humedal, el vertido, la tala, la conservación, el reciclaje, la restauración ecológica*; types (6): `multiple-choice`, `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (8 items).
- **c1-14-04** (`estilo-indirecto-informacion`): screen `c1-14-04-a-gr`; vocab: *la desertificación, el ecosistema, el calentamiento global, el incendio forestal, la escasez hídrica, la huella ecológica*; types (6): `multiple-choice`, `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `sentence-builder` (8 items).
- **c1-14-05** (`lo-neutro-abstraccion`): screen `c1-14-05-a-gr`; vocab: *la sostenibilidad, la resiliencia, la economía circular, el acuerdo climático, la fiscalización, la gestión hídrica*; types (6): `multiple-choice` (incl. 3 Reading), `matching`, `fill-blank`, `listening-choice`, `dialogue-complete`, `structured-writing` (11 items) + story `c1-14.json`.
- **c1-14-consolidation**: 12 items, 8 types (`multiple-choice`, `listening-choice`, `matching`, `fill-blank`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing`), 6 distinct `teaches` tags.

## Unit text (`stories/original/c1/c1-14.json`)
- **Title:** *Informe de evaluación sobre la transición climática*
- **Genre:** policy report
- **Word count:** 403 Spanish words (5 paragraphs)
- **Factual claims (all general, uncontroversial, hedged where judgements):**
  - Modernising electricity grids is a central technical condition for supporting growing electrification (general energy-policy observation — high certainty).
  - Carbon pricing tends to provoke social backlash unless paired with direct support for lower-income households (hedged with *suelen* — high certainty).
  - Global warming tends to lengthen dry seasons, worsen water scarcity and raise wildfire and desertification risks (hedged with *tiende a* — high certainty).
  - Wetlands help regulate the water cycle and protect nearby communities (general ecological fact — high certainty).
  - Circular-economy goals involve durable design, lower industrial waste and coordinated water management (general policy definition — high certainty).
  - No real person, institution, study, statistic or country named.

## Norm claims (exact wording from screens, for RAE check)
- `c1-14-01-a-gr`: "Remember two agreement rules: the past participle after *haber* never changes (*se habrán reducido las emisiones*, never *reducidas*), and *habrá/habrán* agrees with the plural noun in passive *se* (*se habrán reducido las emisiones*, not *se habrá reducido las emisiones*)."
- `c1-14-02-a-gr`: "Never use the conditional after *si* (*Si se aplicaría un impuesto* is always wrong). Also watch plural agreement in passive *se* clauses: *si se eliminaran los combustibles fósiles* (plural), not *si se eliminara los combustibles fósiles*."
- `c1-14-03-a-gr`: "In *Se prohíbe fumar en el parque*, the subject is the infinitive action (singular). In *Se prohíben las talas en el parque*, the subject is the plural noun *las talas*, so the verb must be plural."
- `c1-14-04-a-gr`: "Never insert *que* directly after *según* (*según que dice el informe* is wrong: write *según dice el informe* or *según el informe*). Also remember that *informar* takes *de que* (*informó de que*), whereas *advertir* and *concluir* take *que* directly when stating a finding."
- `c1-14-05-a-gr`: "Never use *lo* before a noun (*lo acuerdo climático* is always wrong: write *el acuerdo climático*). Neuter *lo* combines only with masculine singular adjectives, past participles or adverbs, and when the predicate is a plural noun, *ser* becomes plural (*Lo más difícil son los controles*, not *es los controles*)."

## Check results
- `check-content.py es-latam c1 environment-climate`: **0 error(s), 0 suspect(s)**
- `unmet-words.js` (`--with-hidden`, all 6 stems): **0 hit(s)** (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s)**
- `check_unit_refs.py es-latam c1 environment-climate --bare --named`: **0 hit(s)**
- `render_lesson.js` (all 6 stems): **0 `!!` errors**, self-reviewed in full
- `validate-content.py --changed`: **24 passed, 0 failed**
- `lock_tags.py`: **locked C1/environment-climate: 55 exercise(s)**

## Unsure Spanish lines
None.

## For the user
Note for the RAE norm check on `c1-14-04-a-gr`: *informar que* without *de* is widely accepted in Latin America (DPD allows both *informar de que* and *informar que*), so we did not use *informar que* as a wrong option in any item; the tip states only the standard *informar de que* pattern alongside *advertir/concluir + que*.
