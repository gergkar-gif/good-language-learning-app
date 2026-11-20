# ES C1 core Unit 36 (`own-voice-c1`): Antigravity report

- **Model & setting:** Antigravity (remote agent, standard)
- **Wall-clock time:** ~5 minutes
- **Allowance used:** not visible in this environment

## Files created / updated

- `imports/review/es-c1-plan/antigravity/unit-36-own-voice-c1.md` (unit brief; notes were reviewer-written)
- `content/es-latam/lessons/c1/c1-36-01.json` … `c1-36-05.json`, `c1-36-consolidation.json`
- `content/es-latam/grammar/c1/c1-36-01-a-gr.json` … `c1-36-05-a-gr.json`
- `content/es-latam/vocabulary/c1/c1-36-01-voc.json` … `c1-36-05-voc.json`
- `content/es-latam/exercises/c1/c1-36-01-ex.json` … `c1-36-05-ex.json`, `c1-36-consolidation-ex.json`
- `content/es-latam/stories/original/c1/c1-36.json`
- `content/es-latam/curriculum/challenges.json` (6 `tier1` challenges added via `add_challenges.py`)
- `content/es-latam/indexes/tags.lock.json` (55 exercises locked via `lock_tags.py`)
- `content/es-latam/indexes/word-lesson-index.json`
- `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-36-01** (`infinitivo-compuesto-nominal`, `relativos-el-cual`, `derivacion-nominal-verbal`, recapping C1 Units 1, 7, 3): screen `c1-36-01-a-gr` (`grammar.c1.36.01.a`); 6 words (*la precisión, la oración, preciso, esmerado, combinar, ajustar*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-36-02** (`dequeismo-queismo`, `gerundio-normativo`, `concordancia-ad-sensum`, recapping C1 Units 2, 8): screen `c1-36-02-a-gr` (`grammar.c1.36.02.a`); 6 words (*el desliz, editar, depurar, reescribir, afinar, equilibrar*); 8 items (`multiple-choice` ×3, `fill-blank`, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-36-03** (`verbos-doble-modo`, `dislocacion-clitica`, recapping C1 Units 12, 11): screen `c1-36-03-a-gr` (`grammar.c1.36.03.a`); 6 words (*la frase, el dominio, la destreza, incisivo, expresivo, moldear*); 8 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-36-04** (`futuro-concesivo`, `con-lo-que-para-lo-que`, `ni-que-exclamativo`, recapping C1 Units 20, 21): screen `c1-36-04-a-gr` (`grammar.c1.36.04.a`); 6 words (*el humor, la complicidad, jocoso, ágil, alternar, dominar*); 8 items (`multiple-choice` ×2, `fill-blank` ×2, `matching`, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-36-05** (`marcadores-conversacionales`, `sufijos-apreciativos`, `se-aspectual`, recapping C1 Units 18, 22, 17): screen `c1-36-05-a-gr` (`grammar.c1.36.05.a`); 6 words (*la voz propia, la naturalidad, la soltura, la autenticidad, expresarse, versátil*); 11 items (`multiple-choice` ×3, `fill-blank` ×2, `listening-choice`, `reading` ×3, `dialogue-complete`, `sentence-builder`) + capstone essay `c1-36.json`.
- **c1-36-consolidation**: 12 items (`multiple-choice` ×5, `fill-blank` ×2, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`) covering 9 distinct C1 grammar skills + `c1-own-voice-c1-vocab` (10 tags).

## Unit text

- **Genre:** capstone essay (`story.c1.36`, *Encontrar una voz propia en otra lengua*)
- **Word count:** 478 Spanish words (5 paragraphs, 3 English comprehension questions)
- **Factual claims:** none about real people, studies, works, quotations, dates, or statistics; a personal reflection by an unnamed student (*una estudiante*, not Meg) on developing one's own voice in Spanish across formal and informal registers (high certainty).

## Norm claims

- `c1-36-01-a-gr`: "Keep the participle invariable after *haber* (*tras haber revisado las notas*, never *revisadas*)."
- `c1-36-02-a-gr`: "First, test every *que* clause with *eso* to avoid *dequeísmo* and *queísmo*: *pienso eso* → *pienso que* (never *pienso de que*), *estoy seguro de eso* → *estoy seguro de que* (never *estoy seguro que*)." / "verify that collective nouns without a plural complement (*la gente*, *el comité*) take a singular verb."
- `c1-36-03-a-gr`: "Whenever you front a definite direct object (*ese libro*, *esta idea*, *las notas*), always double it with *lo, la, los* or *las* before the verb (*esta idea la defiendo*, never *esta idea defiendo*)."
- `c1-36-04-a-gr`: "After ironic *ni que*, always use the **imperfect subjunctive** (*¡Ni que fuera fácil!*, never indicative *¡Ni que es fácil!* or present subjunctive *¡Ni que sea fácil!*)."
- `c1-36-05-a-gr`: "Aspectual *se* (*leerse*, *comerse*, *saberse*) requires a **specific, bounded** direct object (*me leí el libro entero*, never *me leí libros*)."

## Check results

- `check-content.py es-latam c1 own-voice-c1`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (`--with-hidden`): 0 hit(s) (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `check_unit_refs.py es-latam c1 own-voice-c1 --bare --named`: 0 recap reference(s) to check (1 unchecked recap line on `c1-36-03-a-gr` verified by hand against C1 Unit 12)
- `c1_known_forms.py own-voice-c1`: all lesson-level C1 skills recapped in their openers; remaining hits are basic words (`haber`, `decir`, `sentir`) or terms already covered by the unit's C1 recap openers
- `render_lesson.js`: 0 `!!` errors
- `validate-content.py --changed`: 24 passed, 0 failed
- `lock_tags.py`: locked `C1/own-voice-c1` (55 exercises)

## Unsure lines

- None. All norm claims recap rules already vetted in C1 Units 1–22.

## For the user

- **Block summary (Units 34–36 — ES C1 core complete):**
  - **Unit 34 (`globalisation-geopolitics`)**: drafted notes + 6 lessons + 467-word analysis essay + 6 `tier1` challenges; `check-content` 0/0, `unmet-words` 0, `validate-content` 24/24, 55 exercises locked.
  - **Unit 35 (`public-speaking`)**: drafted notes + 6 lessons + 418-word speech with commentary + 6 `tier1` challenges; `check-content` 0/0, `unmet-words` 0, `validate-content` 24/24, 55 exercises locked.
  - **Unit 36 (`own-voice-c1`, capstone)**: reviewer-written notes + 6 lessons synthesizing C1 Units 1–22 + 478-word capstone essay + 6 `tier1` challenges; `check-content` 0/0, `unmet-words` 0, `validate-content` 24/24, 55 exercises locked.
  - **ES C1 core (all 36 units) is now written** and ready for Claude's review, freeze, and planting in `es-es`.
