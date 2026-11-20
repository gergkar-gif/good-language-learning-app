# ES C1 core Unit 32 (`literary-analysis`): Antigravity report

- **Model & setting:** Antigravity (remote agent, standard)
- **Wall-clock time:** ~6 minutes
- **Allowance used:** not visible in this environment

## Files created / updated

- `imports/review/es-c1-plan/notes/literary-analysis.md` (drafted unit notes)
- `imports/review/es-c1-plan/antigravity/unit-32-literary-analysis.md` (unit brief)
- `content/es-latam/lessons/c1/c1-32-01.json` … `c1-32-05.json`, `c1-32-consolidation.json`
- `content/es-latam/grammar/c1/c1-32-01-a-gr.json` … `c1-32-05-a-gr.json`
- `content/es-latam/vocabulary/c1/c1-32-01-voc.json` … `c1-32-05-voc.json`
- `content/es-latam/exercises/c1/c1-32-01-ex.json` … `c1-32-05-ex.json`, `c1-32-consolidation-ex.json`
- `content/es-latam/stories/original/c1/c1-32.json`
- `content/es-latam/curriculum/challenges.json` (6 `tier1` challenges added via `add_challenges.py`)
- `content/es-latam/indexes/tags.lock.json` (55 exercises locked via `lock_tags.py`)
- `content/es-latam/indexes/word-lesson-index.json`
- `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-32-01** (`discurso-indirecto-libre`, recap B2 Unit 17): screen `c1-32-01-a-gr` (`grammar.c1.32.01.discurso-indirecto-libre`); 7 words (*el monólogo, omnisciente, confiable, la prosa, la ficción, narrativo, delatar*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-32-02** (`estar-a-punto-de`, recap B1 Unit 1): screen `c1-32-02-a-gr` (`grammar.c1.32.02.estar-a-punto-de`); 7 words (*la trama, el suspenso, el clímax, la tensión, irrumpir, ocultar, revelar*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-32-03** (`dejar-de-infinitivo`, recap B1 Unit 12): screen `c1-32-03-a-gr` (`grammar.c1.32.03.dejar-de-infinitivo`); 7 words (*la elipsis, la concisión, verosímil, literario, el género, omitir, condensar*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-32-04** (`volver-a-infinitivo`, recap B2 Unit 23): screen `c1-32-04-a-gr` (`grammar.c1.32.04.volver-a-infinitivo`); 7 words (*el símbolo, la relectura, releer, resonar, entrelazar, la cadencia, el espejo*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-32-05** (`terminar-por-infinitivo`, recap B2 Unit 25): screen `c1-32-05-a-gr` (`grammar.c1.32.05.terminar-por-infinitivo`); 7 words (*el epílogo, la alegoría, la fábula, la verosimilitud, la polifonía, dosificar, evidenciar*); 11 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `reading` ×3, `dialogue-complete`, `sentence-builder`) + genre essay `c1-32.json`.
- **c1-32-consolidation**: 12 items (`multiple-choice` ×3, `fill-blank` ×3, `listening-choice`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing` ×2) covering all 5 grammar skills + `c1-literary-analysis-vocab` (6 tags).

## Unit text

- **Genre:** essay on a genre, not one work (`c1-original-32`, *El arte de callar a tiempo: notas sobre el cuento breve*)
- **Word count:** 449 Spanish words (5 paragraphs, 3 English comprehension questions)
- **Factual claims:** none about real authors, real works, dates, or statistics; general literary observations on the short story genre built on invented schematic examples (high certainty).

## Norm claims

- `c1-32-01-a-gr`: "Do not mix a reporting verb (*pensó que*) with free indirect discourse: once you write *pensó que*, you are back in standard reported speech. Equally, keep the verb in a past tense (*estaba*, *había cometido*, *explicaría*): using the present tense (*¿Por qué nadie le cree ahora?*) breaks the past-tense narrative frame."
- `c1-32-02-a-gr`: "Never drop the preposition *de* or put a conjugated verb after *a punto de*: always use the infinitive (*estuvo a punto de revelar*, never `*estuvo a punto revelar*` or `*estuvo a punto de que revelara*`)."
- `c1-32-03-a-gr`: "Always include *de* before the infinitive (*no deja de ser*, never `*no deja ser*`), and note that *no dejar de* + infinitive never takes the subjunctive."
- `c1-32-04-a-gr`: "Never use *volver sobre* + infinitive."
- `c1-32-05-a-gr`: "Watch the preposition after *terminar* and *acabar*: *terminar por* + infinitive means 'to end up doing', while *terminar de* + infinitive means 'to finish doing' (and *acabar de* + infinitive from A2 Unit 32 means 'to have just done')."

## Check results

- `check-content.py es-latam c1 literary-analysis`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (`--with-hidden`): 0 hit(s) (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `check_unit_refs.py es-latam c1 literary-analysis --bare --named`: 0 recap reference(s) to check (1 unchecked English-prose recap note on `c1-32-01-a-gr` verified by hand against B2 Unit 17)
- `c1_known_forms.py literary-analysis`: 8 common/already-recapped forms checked (*acabar de* recapped as A2 Unit 32; *ahora*, *aquí*, *mañana*, *estaba*, *pensó que* covered by B2 Unit 17)
- `render_lesson.js`: 0 `!!` errors
- `validate-content.py --changed`: 24 passed, 0 failed
- `lock_tags.py`: locked `C1/literary-analysis` (55 exercises)

## Unsure lines

- `c1-32-01.ex02` option 3: *Cerró la puerta. Mañana lo explicaba todo allá.* (unsure — imperfect *explicaba* in place of conditional is colloquial/acceptable in some varieties, though changing *aquí* to *allá* also shifts the deictic; reviewer may prefer a single-fault distractor if needed).

## For the user

- Nothing blocking; all checks pass cleanly.
