# ES C1 core Unit 34 (`globalisation-geopolitics`): Antigravity report

- **Model & setting:** Antigravity (remote agent, standard)
- **Wall-clock time:** ~11 minutes
- **Allowance used:** not visible in this environment

## Files created / updated

- `imports/review/es-c1-plan/notes/globalisation-geopolitics.md` (drafted unit notes)
- `imports/review/es-c1-plan/antigravity/unit-34-globalisation-geopolitics.md` (unit brief)
- `content/es-latam/lessons/c1/c1-34-01.json` … `c1-34-05.json`, `c1-34-consolidation.json`
- `content/es-latam/grammar/c1/c1-34-01-a-gr.json` … `c1-34-05-a-gr.json`
- `content/es-latam/vocabulary/c1/c1-34-01-voc.json` … `c1-34-05-voc.json`
- `content/es-latam/exercises/c1/c1-34-01-ex.json` … `c1-34-05-ex.json`, `c1-34-consolidation-ex.json`
- `content/es-latam/stories/original/c1/c1-34.json`
- `content/es-latam/curriculum/challenges.json` (6 `tier1` challenges added via `add_challenges.py`)
- `content/es-latam/indexes/tags.lock.json` (55 exercises locked via `lock_tags.py`)
- `content/es-latam/indexes/word-lesson-index.json`
- `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-34-01** (`cuanto-mas-tanto-mas`, recap B1 Unit 2): screen `c1-34-01-a-gr` (`grammar.c1.34.01.a`); 7 words (*la interdependencia, la globalización, el bloque, la integración, la vulnerabilidad, comercial, unilateral*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-34-02** (`formal-cause-connectors`, recap B1 Unit 6 / B2 Unit 27 / C1 Unit 9): screen `c1-34-02-a-gr` (`grammar.c1.34.02.a`); 7 words (*el tratado, la soberanía, la aduana, el flete, la represalia, arancelario, marítimo*); 8 items (`multiple-choice` ×2, `fill-blank` ×2, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-34-03** (`pasiva-refleja`, recap B1 Unit 6 / B1 Unit 18): screen `c1-34-03-a-gr` (`grammar.c1.34.03.a`); 7 words (*la alianza, el corredor, el convenio, la cooperación, bilateral, multilateral, suscribir*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-34-04** (`estilo-indirecto-informacion`, recap B1 Unit 13 / B2 Unit 27): screen `c1-34-04-a-gr` (`grammar.c1.34.04.a`); 7 words (*la diplomacia, la geopolítica, la potencia, el observador, la influencia, estratégico, fronterizo*); 8 items (`multiple-choice` ×3, `fill-blank`, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-34-05** (`futuro-perfecto`, recap B1 Unit 22): screen `c1-34-05-a-gr` (`grammar.c1.34.05.a`); 7 words (*el abastecimiento, la logística, la mercancía, el contrapeso, diversificar, reconfigurar, consolidar*); 11 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `reading` ×3, `dialogue-complete`, `sentence-builder`) + analysis essay `c1-34.json`.
- **c1-34-consolidation**: 12 items (`multiple-choice` ×5, `fill-blank` ×2, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`) covering all 5 grammar skills + `c1-globalisation-geopolitics-vocab` (6 tags).

## Unit text

- **Genre:** analysis (`story.c1.34`, *Corredores marítimos y autonomía estratégica*)
- **Word count:** 467 Spanish words (5 paragraphs, 3 English comprehension questions)
- **Factual claims:** none about real countries, living people, governments, politicians, companies, institutions, dates, or statistics; general economic and geopolitical observations about maritime corridors, inland transit agreements, and weighing efficiency against strategic autonomy in an invented setting (high certainty, hedged where judgements).

## Norm claims

- `c1-34-01-a-gr`: "Do not leave *cuanto* invariable before a feminine or plural noun (*cuanto más socios* is avoided in formal writing; use *cuantos más socios*), and never use *entre más* in formal analysis where *cuanto más* is standard."
- `c1-34-02-a-gr`: "Never follow *debido a* directly with a conjugated verb (*debido a subió el flete* is ungrammatical: use *debido a que*). Conversely, *debido a que* cannot introduce a bare noun (*debido a que el flete* is wrong)."
- `c1-34-03-a-gr`: "Standard formal writing avoids adding a *por* agent to passive *se*. When the diplomatic actor must be named, switch to *ser* + participle: *el convenio fue suscrito por ambos bloques*, not *se suscribió por ambos bloques*."
- `c1-34-04-a-gr`: "Never insert *que* after *según* before a verb (*según que señala el informe* is wrong; write *según señala el informe*). Similarly, *a juicio de* and *conforme a* take a noun phrase, not a conjugated clause."
- `c1-34-05-a-gr`: "The past participle stays invariable (*se habrán reconfigurado*, never *reconfiguradas*)."

## Check results

- `check-content.py es-latam c1 globalisation-geopolitics`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (`--with-hidden`): 0 hit(s) (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `check_unit_refs.py es-latam c1 globalisation-geopolitics --bare --named`: 0 recap reference(s) to check (1 unchecked recap line on `c1-34-05-a-gr` verified by hand against `b1-22-04-hypothetical-structures-gr`)
- `c1_known_forms.py globalisation-geopolitics`: 3 non-recapped hits (`*cuantos*`/`*cuantas*` from B2 Unit 14 universal relatives, not proportional correlatives; `*según el informe*` example phrase from C1 Unit 14); all lesson-level structures recapped
- `render_lesson.js`: 0 `!!` errors
- `validate-content.py --changed`: 24 passed, 0 failed
- `lock_tags.py`: locked `C1/globalisation-geopolitics` (55 exercises)

## Unsure lines

- `c1-34-01-a-gr` tip: "and never use *entre más* in formal analysis where *cuanto más* is standard." (unsure — DPD accepts *entre más* in parts of Latin America while noting *cuanto más* is preferred in formal register; reviewer may wish to soften "never use" to "avoid in formal analysis").

## For the user

- None. All checks pass and the unit is ready for review.
