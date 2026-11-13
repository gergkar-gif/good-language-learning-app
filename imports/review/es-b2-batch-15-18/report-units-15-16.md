Both units (15 and 16) are rewritten and both challenges files are written. All checks were rerun after the last edit and are clean except one suspect in Unit 15, explained below. Nothing is committed.

I could not write the report file (the brief says to try). The report is this reply.

**Files**
- Challenges: `/home/user/parlour-read-a/challenges-imperfect-subjunctive-forms-nuances.json` and `/home/user/parlour-read-a/challenges-pluperfect-subjunctive.json` (six entries each, `canDo` is the first checklist line). They are not merged into `curriculum/challenges.json`; I checked their targets for unmet words by merging them temporarily and restoring the file.
- Rewritten per lesson: lesson file, grammar screen, vocabulary list, exercises, and the unit text. The generated indexes and manifests changed through `build-manifest.py` and `build_word_lesson_index.py`, as expected.

**Check counts**

| Check | Unit 15 before | Unit 15 after | Unit 16 after |
|---|---|---|---|
| check-content errors | 14 | 0 | 0 |
| check-content suspects | 7 | 1 | 0 |
| unmet words | about 90 | 0 | 0 |

- I did not record the Unit 16 counts before I started.
- `check_unit_refs` reports 0 recaps to check for both units. `validate-content --changed` passes (es-latam 93 passed, 0 failed). The renders show no `!!`.
- The one remaining Unit 15 suspect is `answers-alternatives` on b2-15-05.ex02. The answers *nació* and *había nacido* are both correct for *donde naciera*, so I kept both.

**Unit 15: changes per lesson** (all exercises are ex01 to ex06; all screens, titles, goals and question stems are now in English; no multiple-choice item carries `hint` or `english`)
- **b2-15-01, stem and endings.** The screen recaps B1 Unit 4 and Unit 38. It adds the *-se* column and the irregular groups (*dijera*, *trajera*, *leyera*, *pidiera*, *diera*). Items ex02 to ex06 are rewritten. ex03 has one wrong option per fault: present subjunctive, preterite, and missing accent.
- **b2-15-02, -ra or -se.** Same meaning; *-ra* is far more common in Latin America and *-se* is mostly read. Items ex02 to ex06 are rewritten; fill-blanks accept both forms.
- **b2-15-03, polite forms.** Recaps *quisiera*, *pudiera* and *debiera* from B2 Unit 9. The only addition is *quisiera que* + imperfect subjunctive. Items ex02 to ex06 are rewritten and tagged `polite-softening`.
- **b2-15-04, como si and ojalá.** Items are tagged `como-si`. The *ojalá* items are tagged `subjuntivo-deseos`. Items ex02 to ex06 are rewritten. The pluperfect mention is gone.
- **b2-15-05, formal -ra.** Recognition only. Items are tagged `subjuntivo-imperfecto-estilistico-ra`. ex06 is now a `listening-choice` with English options, so nothing has to be typed in the formal form.
- **b2-15-consolidation.** All 8 items are rewritten. ex08 is a reading item, and the checklist names Gallegos.
- All six lessons have new vocabulary lists (4 words each, all used in ex01 at least) and new goal and checklist lines. Lessons 01 to 05 now have `srs` and `checklist` sections.

**Unit 16: changes per lesson** (same structure; fill-blanks accept both *hubiera* and *hubiese* through `answers`)
- **b2-16-01.** Full paradigm with both variants, irregular participles, and pronouns before *hubiera*.
- **b2-16-02.** *ojalá hubiera* and *¡quién hubiera!*, contrasted with the present and imperfect *ojalá*. Tagged `counterfactual-wishes`.
- **b2-16-03.** Recap of *si hubiera*, *hubiera* without *si* and *de haber*. New: *de no haber* and pronouns on *haber*. Tagged `implicit-conditionals`.
- **b2-16-04.** Plain judging lesson: *Habría sido mejor que…*, *Me sorprendió que…*, *No creía que…*, contrasted with the present perfect subjunctive. Tagged `pluperfect-subjunctive-forms`, with `distractor_skills` on the *haya* and *había* options.
- **b2-16-05.** *hubiese* as recognition, with no jargon.
- **b2-16-consolidation.** 8 items, one of them reading. ex08 asks for the publication year, because the word *diario* is first listed in b2-19.

**Text of b2-15** (Gallegos, 336 words, 7 paragraphs; no asterisks). Every claim is from your fact list or is plain arithmetic or a definition.
1. Novelist, Venezuelan: sure.
2. Born 1884, died 1969: sure.
3. *Doña Bárbara* published in 1929: sure.
4. President of Venezuela in 1948 (the formal *que fuera presidente*): sure.
5. Presidency began February 1948, military coup in November of the same year: sure.
6. Presidency lasted less than a year: derived.
7. Novel published "casi veinte años" before he was president: derived (about 18 to 19 years).
8. A military coup is the military taking power by force: definition.
9. Set in the *llanos*, which are plains, flat land: sure.
10. The title is the name of a character: derived.
11. Santos Luzardo returns from the city to his land in the plains, and faces Doña Bárbara, a powerful woman of the plains: sure.
12. The novel is often read as a conflict between civilisation and barbarism: sure ("often"). The sentence "treats the confrontation *como si* it were more than a conflict between two people" follows from that reading.
13. No scene or quote in the text, and a short text cannot replace the book: about the text itself.

**Text of b2-16** (de la Parra, 309 words, 7 paragraphs; no asterisks; the subtitle is written plainly, without quotation marks).
1. Venezuelan writer, 1889 to 1936: sure.
2. *Ifigenia*, 1924: sure.
3. Her second novel is *Memorias de Mamá Blanca* (1929), so *Ifigenia* is her first: derived.
4. Subtitle *Diario de una señorita que escribió porque se fastidiaba*: sure.
5. Protagonist María Eugenia Alonso: sure.
6. The novel is built from a long letter, "dirigida primero a una amiga llamada Cristina", and a diary: fairly sure. I kept your wording and dropped the possessive, because "her friend" could mean either woman.
7. It won a prize for American novelists in Paris in 1924: sure.
8. 1924 is also its publication year, so it won the prize the year it appeared: fairly sure. This rests on your "(1924)" being the publication year.
9. The subtitle names a diary but not a letter: true of the subtitle.
- The remaining sentences are hypotheticals about readers, definitions of diary and letter, and meta statements about the text.

**Spanish lines I am unsure of** (unsure)
- *¿Pudiera decirme dónde está la ventanilla tres?* (ex03) is natural in formal Latin American Spanish, but I would ask a native speaker.
- *¡Quién hubiera estado allí!* is explained as *quién* meaning "I". That is the usual reading but it is literary.
- *Debieras descansar un poco* is a bare *tú* form of *debiera*, which is rarer than *debieras*-style advice with *deberías*.

**For the user**
- **Brief premise corrected.** B1 Unit 4 (b1-04-02) already teaches the stem from the *ellos* preterite and the irregular table, so 15-01 recaps them as known. What is new there is the *-se* column and the *j*, *y* and *-ir* verb groups. In the same way, B1 Unit 35 and B2 Unit 10 already use *hubiera* + participle, so 16-01 is mostly a recap. Its new content is *hubiese*, the full paradigm, and preview uses after *que*.
- **No mismatch between lessons and skills.** No lesson's whole point is a later or hidden skill, and the 15/16 text and exercises use no unmet word.
- **Reader and asterisks.** The Reader shows `*...*` literally in story text, so both story files have none.
- **One new vocabulary entry.** `olvidarse de` in 16-01. None of the removed old lemmas appears in `requiredLemmas`.
- **Tags not locked.** I did not run `lock_tags.py`, as the brief said to do nothing outside the unit's files.
- **Not fixed.** Nothing I could not fix.