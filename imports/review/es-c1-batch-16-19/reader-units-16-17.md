# Reader report: es-latam C1 Units 16 and 17

Fixes files: `.scratch/fixes-cities-housing.json` (35 fixes), `.scratch/fixes-everyday-aspect.json` (39 fixes). Both pass `check_fixes.py` (0 rejected) and, applied to a scratch copy, leave check-content at 0, `unmet-words.js ... --with-hidden` at `[]`, `check_es_c1_forms.py` at 0. Nothing in the worktree was edited (fixes were applied only in scratch copies; the generated `word-lesson-index.json` was rebuilt in the worktree and is ignored by git).

Commands as run: check-content 0 errors/0 suspects for both units; unmet-words `[]` for both; audit-reader-coverage 0 gaps for both stories (so group 5 is empty); `check_unit_refs --bare --named` found only the italics false positive (16-01); `check_es_c1_forms` 0.

## UNIT 16 cities-housing (35 fixes)

### 1. Found by reading
- c1-16-01-a-gr: "*mientras que* from B2 Unit 28" -> B1 Unit 12 (b1-12-04 teaches it; B2 Unit 28 only recaps). Fixed.
- c1-16-01.ex02: "Durante décadas el barrio ___ ..." (hint mantener 3sg) takes *mantuvo* as well as *mantenía* (two right answers). Fixed: "Antes el barrio ___ ...", English "used to maintain".
- c1-16-02-a-gr: recap says "from B1 Unit 25 for personal changes" but the five verbs were taught again in B1 Unit 39 and B2 Unit 22; says *volverse* "marks a gradual structural shift" and *hacerse* "gradual", contradicting B2 Unit 22 (volverse = happens to a thing, hacerse = builds up/effort); "formal *hacerse*" is unfounded; tip "*convertirse en* whenever a noun follows" is false (*se hizo médico*). Fixed (opener, text, two table rows, tip).
- c1-16-02-a-gr example / c1-16-02.ex06 / c1-16-consolidation.ex11: "dos edificios ... despoblados", "muchos edificios se han quedado despoblados esperando precios más altos": *despoblado* is said of places, not buildings; "edificios ... esperando precios" has a dangling subject. Fixed to *calles* (story and challenge already say *calles*) (unsure).
- c1-16-02.ex04 dictation: "Mantener el alquiler ..." (keeping up the rent) not a natural collocation -> "Pagar el alquiler ..." (unsure).
- c1-16-03.ex07 builder: "La vivienda social es el proyecto con el que cuenta el municipio" calls a kind of housing a project -> "La renovación urbana es el proyecto con el que cuenta..." (unsure).
- c1-16-04-a-gr tip is garbled ("sino before a conjugated verb (... is fine with an infinitive ...)"). Rewritten.
- c1-16-04.ex01 option 3 "..., sino exige ..." has two faults (sino after affirmative, no *que*), duplicating options 1 and 2 -> "..., pero que exige ...".
- c1-16-04.ex08 option 2 "..., sino reduce ..." two faults -> "..., sino que reduce ...".
- c1-16-05.ex02: "___ crecía la plusvalía" is also right with *Según* and *Mientras* (an `answers` list is rejected by `answers-alternatives`); hint named the connector type. Replaced by an *Apenas* item ("___ se aprobó la norma del alquiler regulado, los precios dejaron de subir").
- c1-16-05 story, paragraph 3: "Conforme aumentaba la plusvalía ..., pagar el alquiler se ha hecho insostenible" mixes past and perfect -> "se hacía cada vez más insostenible".
- c1-16-05 story is 399 words (brief: 400-600): added "con firmeza" and the change above (now 403).
- c1-16-05 reading Q1 and story file: "coastal avenue renovation" but the text says *paseo marítimo* (seafront promenade). Fixed in question and explanation, both files.
- c1-16-05.ex07 (reading Q2), both files: right option says "Long-time tenants", the text says nothing of the kind (evicted or unable to renew). Fixed, kept within 1.3x length.
- c1-16-consolidation.ex05: "expulsar al turismo" unnatural -> "frenar el turismo" (unsure).
- c1-16-consolidation.ex11: second prompt/answer pins (see 3).

### 2. Metadata
- c1-16-01.ex01 and consolidation.ex01: option *ofrezca* / *mantenga* is a real subjunctive form: add `distractor_skills` 3 `subjuntivo-morfologia`.
- c1-16-01.ex06: *mantendrá* real future form: `distractor_skills` {"2":"futuro-simple"}.
- c1-16-05.ex03 and c1-16-consolidation.ex06 (*apruebe*, *entre* after *en cuanto*): `teaches` conectores-temporales-narrativos -> `cuando-subjuntivo` (wrong answers show the mood skill). c1-16-05.ex09 same (unsure, mixed options).
- c1-16-02.ex07 / 04.ex07 / consolidation.ex11 structured-writing prompts unpinned (area/zone/luxury, housing/vivienda, tenant, raises/worsens, current homes, price rise, paying the rent): the nouns/verbs are now named in «».

### 3. Goals / checklists / challenges
- Goals and checklists: every line is practised; first checklist line = challenge `canDo` in all six. No fix.
- Challenge c1-16-consolidation scenario: "that before the neighbourhood used to offer" garbled -> reworded. All other challenges read correctly (roles, Meg student, Carlos office, one or two sentences, met words).

### 4. Doubtful
- Lessons 02, 03, 05 re-present B1/B2 screens almost whole (02 = B2 Unit 22 choosing verbs; 05 = B2 Unit 2 incl. the same mood tip); the only new content is the urban domain. Topic unit, so left; the writer's call whether to add a C1 contrast.
- c1-16-01.ex08 (*la densidad urbana* as a distractor for "ha debilitado ___ del casco histórico") borderline plausible (unsure).
- c1-16-05.ex11 distractor "en cuanto se aprueba ... podrá mejorar": present indicative with future is a standard learner error but not impossible (unsure).
- c1-16-04.ex06 Carlos's reply does not address "encarece el barrio".
- *casco histórico* (Spain-leaning; Mexico says *centro histórico*) used through lessons 01-05 and consolidation (unsure).
- c1-16-02-a-gr example "centro comercial de alto precio" odd; c1-16-05 consolidation.ex08 dictation repeats lesson 04's challenge target.

### 5. Dictionary
(none: audit reports 0 for c1-16)

## UNIT 17 everyday-aspect (39 fixes)

### 1. Found by reading
- c1-17-02-a-gr: "You know pronoun combinations with *se* from A2 Unit 25. New here is the accidental *se*": accidental *se* with agreement with the thing is taught in B2 Unit 19 (b2-19-05, "Se me cayó el vaso", "Se nos olvidó el boleto", the tip). Recap now names B2 Unit 19. The lesson then has little new (see 4).
- c1-17-04-a-gr: *no dejar de* ('keep on doing') is taught in B2 Unit 25 (b2-25-01-a), not just *dejar de* B1 Unit 12; "works as an emphatic 'cannot help'" is not a meaning of *no dejar de*; table "*normalmente* + future for future habits" not a way to say a future habit; tip calls *normalmente suele* a rule violation. Fixed.
- c1-17-04.ex01: option "Antes solía normalmente tomarse ..." is acceptable (pleonastic) Spanish, a second right answer -> "solía tomándose". Goal 1, checklist 1 and challenge `canDo` drop "and redundancy" (no longer tested) (unsure).
- c1-17-04.ex03: "De estudiante, Meg ___" puts Meg's studies in the past (Meg is a student) -> "El año pasado, Meg ___".
- c1-17-01-a-gr: "consuming, learning and perceiving" (no perceiving verb) -> knowing; "across all varieties of Spanish" stronger than the checked claim -> dropped (unsure); table row "Reflexive misread to avoid ... *Se comió el bocado* ... 'ate the whole bite up'" -> "Not reflexive ... *Se comió el pastel*" (unsure).
- c1-17-01.ex07 English "memorised the whole recipe by heart" -> "learned ... by heart".
- c1-17-02.ex08: "dejarlas fuera del frío" not said -> "al sol", in all four options.
- c1-17-02.ex05: all three wrong options carry a modifier the right one lacks (*del todo, entero, de golpe*): tell -> real phrases (*echarse a reír, ponerse a cocinar, quedarse sin sal*) (unsure).
- c1-17-03.ex01, ex08, c1-17-consolidation.ex02: all (or two of) the wrong options fail the same way (indicative where subjunctive is wanted) -> distinct faults (*de que*, agreement) (unsure).
- c1-17-05 story: "Era sábado ... llegó Carlos directo de la oficina" -> viernes.
- c1-17-05-a-gr example: *encontró el fallo* (Spain) -> *la falla* (unsure).
- c1-17-consolidation.ex10: "No vuelvo a repetir" is a pleonasm -> "a cometer" (unsure; *cometer* is met in C1 Unit 2).
- Challenge c1-17-01: scenario "a cup of tea ... while reading" vs target *la taza de té*, no reading -> aligned.
- Challenge c1-17-05: target "salió redonda por los pelos" mixes "perfect" and "barely" -> "nos salvamos por los pelos"; scenario, cues, English aligned.
- c1-17-01.ex02/ex03 hint "aspectual pronoun" names the tested point -> "pronoun (...)".

### 2. Metadata
- c1-17-02 ex01-04, 06, 08: `teaches` pronombres-combinados (the A2 *se lo* skill) -> `desambiguacion-valores-se` (accidental *se* is taught there, B2 Unit 19); no new skill needed (unsure).
- c1-17-03.ex02, ex07: `subjuntivo-perfecto` (the tested form) instead of subjunctive-emotion (unsure).
- `distractor_skills` missing on real forms: c1-17-03.ex06 (*tuvieras* imperfect-subjunctive-forms, *tenías* imperfect), ex08, consolidation.ex02 (*quede* subjuntivo-morfologia).
- c1-17-02.ex07 and c1-17-04.ex07 prompts did not pin «en la mesa», «por la mañana», «los apuntes»: pinned.

### 3. Goals / checklists
- Only the 17-04 goal/checklist/canDo edit above. All other lines are practised; canDo = first checklist line everywhere.

### 4. Doubtful
- Lesson 17-02 is mostly a recap of B2 Unit 19 plus vocabulary; the writer may want a new element (e.g. *a mí se me...* with the stressed pronoun, a person affected in 3rd person).
- c1-17-03: *picoteo* and *bizcocho* lean to Spain/Peru; no single Latin American word exists, so left (unsure). *Menos mal que* "ALWAYS indicative": reviewer already checked.
- c1-17-01.ex08 option 1 "Nos sabemos canciones del concierto para el viaje": plural bare noun with *saberse* may be acceptable (unsure).
- c1-17-05.ex11 option "Volvimos a la cocina ..." is correct Spanish, wrong only by meaning (the question says repetition).
- c1-17-05.ex03 (*volvería* in "prometió que no ___ a cocinar"): *volverá* is also acceptable after *prometió* if the vow still holds; the hint pins the conditional.
- c1-17-consolidation challenge: Carlos narrates a dinner whose near-cancellation was Meg's in the story; scenario is self-contained, left.

### 5. Dictionary
(none: audit reports 0 for c1-17)

## Fix counts
- Unit 16 cities-housing: 35 fixes (21 sure, 14 marked unsure).
- Unit 17 everyday-aspect: 39 fixes (13 sure, 26 marked unsure).
