# ES C1 core Unit 27 (`history-memory`) — Antigravity report

- **Model / setting:** Antigravity (Gemini), unattended run (Unit 27 — final unit of the Units 16–27 block)
- **Wall-clock time:** ~15 minutes
- **Allowance used:** not shown in environment

## Files created / updated

- Notes: `imports/review/es-c1-plan/notes/history-memory.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-27-history-memory.md`
- Grammar screens (5): `content/es-latam/grammar/c1/c1-27-01-a-gr.json` … `c1-27-05-a-gr.json`
- Vocabulary files (5): `content/es-latam/vocabulary/c1/c1-27-01-voc.json` … `c1-27-05-voc.json`
- Exercise files (6): `content/es-latam/exercises/c1/c1-27-01-ex.json` … `c1-27-05-ex.json`, `c1-27-consolidation-ex.json`
- Lessons (6): `content/es-latam/lessons/c1/c1-27-01.json` … `c1-27-05.json`, `c1-27-consolidation.json`
- Unit essay: `content/es-latam/stories/original/c1/c1-27.json`
- Challenges (6 entries via `add_challenges.py`, all `tier1`): `content/es-latam/curriculum/challenges.json`
- Tag lock (55 exercises via `lock_tags.py`): `content/es-latam/indexes/tags.lock.json`
- Indexes: `content/es-latam/indexes/word-lesson-index.json`
- Writer's notes: `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-27-01** (`pluscuamperfecto`, recap B1 Unit 1): screen `c1-27-01-a-gr` (historical layering, passive pluperfect *había sido* / *se había*); 7 words (`el inventario, catalogar, la cronología, la demolición, demoler, archivar, el solar`); 8 items (`matching`, `fill-blank` ×2, `multiple-choice` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-27-02** (`verbos-cambio-significado-pasado`, recap B2 Unit 2): screen `c1-27-02-a-gr` (standing knowledge vs archival discovery, deliberate refusal *no quiso* vs failed attempt *no pudo*); 7 words (`el manuscrito, la hemeroteca, testimoniar, desenterrar, el pergamino, el antepasado, la genealogía`); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-27-03** (`subjuntivo-imperfecto-estilistico-ra`, recap B2 Unit 15): screen `c1-27-03-a-gr` (historiographical indicative *-ra* vs true subjunctive *-ra*); 6 words (`la placa, la inscripción, el recinto, el obituario, la semblanza, la efeméride`); 8 items (`matching`, `multiple-choice` ×3, `fill-blank`, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-27-04** (`pluperfect-subjunctive-forms`, recap B2 Unit 16): screen `c1-27-04-a-gr` (counterfactual historical conditions and past-tense regret/doubt); 7 words (`la historiografía, la conmemoración, conmemorar, trascender, legar, la posteridad, el anacronismo`); 8 items (`matching`, `fill-blank` ×2, `multiple-choice` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-27-05** (`discurso-indirecto-libre`, recap B2 Unit 17): screen `c1-27-05-a-gr` (witness voice vs narrator voice in historical chronicles); 6 words (`evocar, rememorar, homenajear, la lápida, el bronce, la memoria colectiva`); 11 items (`matching`, `multiple-choice` ×4, `listening-choice`, 3 Reading `multiple-choice`, `dialogue-complete`, `sentence-builder`) + essay `c1-27.json`.
- **c1-27-consolidation**: 12 items covering all 6 tags (`pluscuamperfecto`, `verbos-cambio-significado-pasado`, `subjuntivo-imperfecto-estilistico-ra`, `pluperfect-subjunctive-forms`, `discurso-indirecto-libre`, `c1-history-memory-vocab`) across 7 types (`matching`, `multiple-choice` ×3, `fill-blank` ×3, `listening-choice`, `dialogue-complete`, `sentence-builder`, `structured-writing`, `dictation`).

## Unit text

- **Title:** *Lo que queda tras la demolición: archivos, placas y memoria colectiva*
- **Genre:** essay
- **Word count:** 502 Spanish words (5 paragraphs, 0 asterisks)
- **Factual claims:** none specific to any real place, person, institution, study, or statistic; all statements are general, hedged reflections on urban demolition, municipal archives, oral testimony, and public commemoration (high confidence / uncontroversial).

## Norm claims

- `c1-27-01-a-gr`: *"Remember that in *había sido demolido*, *sido* stays invariable, while the final participle agrees with the subject (*las casas habían sido demolidas*). Keep adverbs like *ya* before the auxiliary, never between the auxiliary and the participle."*
- `c1-27-03-a-gr`: *"Only the *-ra* form carries this indicative past value; *-se* cannot replace it in *el edificio que albergara el archivo*. In your own speech and everyday writing, the standard indicative (*había albergado* or *albergó*) is always natural"*
- `c1-27-04-a-gr`: *"Both *-ra* and *-se* forms are fully accepted in every subjunctive clause here."* / *"Never put the conditional (*habría*) inside the *si* clause: write *si hubiera conservado*, never *si habría conservado*. Remember also that *hubiera* and *hubiese* are interchangeable here, and the participle stays invariable (*hubieran recogido*, never *hubieran recogidos*)."*

## Checks

- `python scripts/check-content.py es-latam c1 history-memory`: **0 error(s), 0 suspect(s)**
- `node scripts/unmet-words.js es-latam c1 --stems c1-27-01,c1-27-02,c1-27-03,c1-27-04,c1-27-05,c1-27-consolidation --with-hidden`: **0 hits (`[]`)**
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s)**
- `python scripts/check_unit_refs.py es-latam c1 history-memory --bare --named`: **0 recap reference(s) to check**
- `python scripts/c1_known_forms.py history-memory`: **2 common auxiliary hits** (`*había*` on 01, `*habría*` on 04 — both already recapped via `*había salido*` from B1 Unit 1 and `*habría llegado*` from B2 Unit 10)
- `node scripts/render_lesson.js es-latam c1-27-01 ... c1-27-consolidation`: **0 `!!` errors**; targeted review caught and fixed two-fault dialogue distractors (`c1-27-01.ex06`, `c1-27-consolidation.ex08`), asymmetric phrasing (`c1-27-02.ex06`), and an under-pinned passive fill-blank (`c1-27-consolidation.ex04`).
- `python scripts/lock_tags.py es-latam c1/history-memory --update`: **55 exercise(s) locked**
- `python scripts/validate-content.py --changed`: **24 passed, 0 failed**

## Unsure Spanish lines

- none

## For the user

- Unit 27 (`history-memory`) is complete, validated, and locked; per `RUN.md`, the unattended Units 16–27 block is now finished and ready for Claude's review, freeze, and es-es planting.
