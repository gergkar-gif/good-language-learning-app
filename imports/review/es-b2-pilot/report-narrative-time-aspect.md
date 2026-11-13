DONE for es-latam b2 narrative-time-aspect, not committed. All edits are in /home/user/parlour-read-b. The report file at /home/user/parlour-read-b/report-narrative-time-aspect.md has only the counts, so this reply is the full report.

## Check counts, before -> after
- check-content: 5 errors, 17 suspects -> 0 errors, 0 suspects. The old errors were length-giveaway, tell-time-word (*Ayer*), three tell-absolute and a course-variant (*billete*). The old suspects were mostly vocab-unused.
- unmet-words, six stems in one list: about 80 hits -> `[]`. I also checked the six challenge targets by temporarily merging them into curriculum/challenges.json and then restoring that file. They are clean.
- render_lesson: 0 `!!` lines.
- check_unit_refs: one line left, a false alarm. It says *en cuanto* "first appears B1 Unit 4" because it reads vocabulary lists only. The A2 Unit 27 screen (a2-subjuntivobasico-04) has *en cuanto* in its table.
- validate-content --changed: es-latam 24 passed, 0 failed.
- `python3 build-manifest.py` and `build_word_lesson_index.py` were run, so generated files changed: curriculum.json, decks, manifests, word-lesson-index.

## Per lesson
All six screens, lesson titles, goals and goal lines are rewritten in English. Every question stem is in English, and no multiple-choice item has `hint` or `english`. Lessons 01 to 05 have no checklist section, so each challenge's `canDo` is the lesson's first goal line. The consolidation uses its first checklist line.

- **b2-02-01** (events and background).
  - Screen: recap from A2 Units 11, 21 and 22; why the tenses work (closed block vs from the inside); a table of plot and scenery; four examples; a quick-test tip. I dropped the old "imperfecto de ruptura" row.
  - Vocabulary: now 5 words (penumbra, murmullo, quietud, desvanecerse, amanecer); removed vestigio, relato, estremecer and remoto.
  - Items: ex01 to ex06 all rewritten. The unmet words and Hacienda-style scenes are gone. ex05 has `distractor_skills` {2: present-tense}.
  - Intro: rewritten in English.
- **b2-02-02** (pluperfect).
  - Screen: recap of B1 Unit 1, the step behind the story's "now", a three-row table, and a flashback tip (do not repeat *había* in every sentence).
  - Vocabulary: acontecimiento, trasfondo, huella, preceder, desentrañar.
  - Items: ex01 to ex06 rewritten. ds on ex02 (preterito-perfecto, imperfect) and ex05 (preterito-indefinido, futuro-simple).
- **b2-02-03** (`verbos-cambio-significado-pasado`, new).
  - Screen: recap of A1 Unit 10 (*querer*, *poder*) and A1 Unit 24 (*saber*, *conocer*); a table of imperfect vs preterite pairs; four examples; a tip on *no quise* (refusal) vs *no pude* (tried and failed). I removed the old claim that *quiso* is "a deliberate attempt" and now say "tried".
  - Vocabulary: dilema, desenlace, empeño ("determination, effort", replacing "endeavor"), rehusar, flaquear.
  - Items: ex01 to ex06 rewritten. ds on ex05: {2: preterito-perfecto}.
- **b2-02-04** (connectors).
  - Screen and connectors: recap of *cuando*/*mientras* (A2 Unit 13), *en cuanto* (A2 Unit 27, table) and *a medida que* (B1 Unit 2). Taught as new: *apenas* ("as soon as"; the "barely" sense is noted), *al cabo de*, *conforme*. I dropped *no bien* and *de improviso* as unmet and rare.
  - Hidden track: no *antes de que* or *después de que*.
  - Table fix: the old "apenas + verb is always instant" claim is replaced by "as soon as when a second clause follows; on its own it can mean barely".
  - Vocabulary: apenas, conforme, al cabo de, súbitamente, sobresalto, paulatino.
  - Items: ex01 to ex06 rewritten. The *billete* item is gone. ds on ex02 ({1: cuanto-mas-tanto-mas}) and ex05 ({2: futuro-simple}).
- **b2-02-05** (polite imperfect).
  - Screen: recap of the A2 Unit 26 conditional (*podría*, *me gustaría*, as that screen shows). The imperfect is presented as a further polite form: *quería pedirle*, *venía a preguntar*, *llamaba para*, *me preguntaba si*. The old conative, play and plan rows are removed. The "universal in Latin America" claim is corrected to "across the Spanish-speaking world".
  - Vocabulary (7 words): disculpar, plus the text words escritor, cuento, fotógrafo, siglo, fragmento, muerto.
  - Items: ex01 is a 6-pair matching of the text words (all 6 text words are used there). ex02 to ex06 are rewritten. ds on ex02 and ex05.
- **b2-02-consolidation**.
  - Text and story file: new text, summary, `characters: []`, source as specified, and 3 comprehension questions with English stems and Spanish options.
  - Items: ex02 (reading, premise of the novel), ex05 (sentence-order of Rulfo's life), ex06 (dialogue about why the novel matters) and ex07 (dictation from the text) were rewritten to agree with the text. ex01, ex03, ex04 and ex08 were rewritten too. ex09 is new (reading: Rulfo as photographer) and is listed in the lesson's exercise group.
  - Lesson file: goal, goal items and checklist are in English.

## The unit text
Title "Juan Rulfo y las voces de Comala". 6 narration paragraphs, 309 words. It uses preterite for life and book history, imperfect for background (*vivía*, *tenía*, *escribía*, *era*, *se leía*) and 2 pluperfects (*ya había publicado sus cuentos*, *había publicado muy poco*). *Conocer* is in the preterite (*los lectores conocieron una voz nueva*). I did not use *saber* in the preterite: it was not natural without an invented detail. The plot sentences are in the present. There is no scene, no dialogue and no quotation.

Every factual claim, one per line (the reviewer checks each on the web):
1. Rulfo was born in 1917 in the state of Jalisco. Very sure; the exact birthplace is disputed, so only the state is named.
2. Jalisco is in the west of Mexico. Very sure.
3. In 1917 the country was still living through the years of the Revolution. Very sure.
4. He published very little. Very sure.
5. His writing had great influence on literature in Spanish. Very sure, an opinion.
6. Today many readers consider him one of the great authors of the twentieth century. Very sure, an opinion.
7. *El llano en llamas*, a collection of stories, appeared in 1953 and was his first book. Very sure.
8. With it, readers got to know a new voice in Mexican narrative. Fairly sure, a critical opinion.
9. *Pedro Páramo*, a novel, was published in 1955, two years later. Very sure.
10. When it came out he had already published the stories and was under forty (born May 1917). Very sure.
11. He was also a photographer in those years. Very sure.
12. His photographs of landscapes, villages and people of Mexico were later shown in many exhibitions. Very sure.
13. The novel tells of a young man, Juan Preciado, who goes to a village called Comala. Very sure.
14. He goes to look for his father, Pedro Páramo, and finds a village of the dead, full of voices. Very sure.
15. There is no single voice explaining everything; many voices speak. Very sure.
16. Rulfo did not tell the story in order; he built the book from short fragments and the reader has to put the pieces together. Very sure.
17. The form of the novel differed from many novels of its time. Fairly sure, a critical consensus.
18. Today it is one of the most important novels of the twentieth century in Spanish. Very sure, an opinion.
19. Many later Latin American writers learned from it to tell a story with voices and fragments. Very sure.
20. He died in 1986 in Mexico City. Very sure.
21. By then he had published very little but his work was already read in many countries (translations). Very sure.
22. He left a great mark on the literature of Latin America, and his name is still one of the most important in Mexico. Very sure, an opinion.

## Challenges
`/home/user/parlour-read-b/challenges-narrative-time-aspect.json` has six entries keyed `b2-02-01` to `b2-02-05` and `b2-02-consolidation`, with the B1 fields. Each scenario starts with the role, using Meg and Carlos only. The only things I invented are small situations (a rainy walk, a lost umbrella, the last bus). I did not merge them into curriculum/challenges.json.

## Unsure Spanish
- (unsure) b2-02-02.ex02, option "su hermana ya se iba". It is a well-formed imperfect, and the English stem pins "had already left".
- (unsure) b2-02-04.ex02, option "Al cabo de la tormenta, se fue la luz". It is grammatical but a little odd, and I read it as a real wrong-meaning option.
- (unsure) b2-02-04.ex05 option "En cuanto llegarán, ...". It is a deliberately wrong future after *en cuanto*.
- (unsure) b2-02-01.ex05, option "de pronto, oía un ruido extraño". I treat the narrative imperfect after *de pronto* as wrong at this level.

## For the user
- **Skills used before their screen:** none.
- **No registry skill for two lessons.**
  - b2-02-04 has none; its items use the closest known skills by what a wrong answer shows: `secuencia-narrativa`, `cuanto-mas-tanto-mas` (for *a medida que*) and `cuando-subjuntivo`. The teaching of *apenas*, *al cabo de* and *conforme* has no slug.
  - b2-02-05's polite imperfect is also unregistered: `polite-softening` covers only the conditional on its screen. I tagged the items `polite-softening`.
- **A2 Unit 26 screen:** the skill title for `polite-softening` mentions *quisiera*, but the screen a2-condicionalsimple-03 does not show it. I did not recap *quisiera*.
- **Hidden-track skills:** none used. No *antes de que* or *después de que*, no *ir/venir/andar* + gerund (*venía a preguntar* is *venir a* + infinitive), no *por más que*, *si bien* or *aun cuando*, no reporting verbs, no absolute participles. Nothing had to be rewritten away.
- **Grammar-screen titles:** B1 titles on the `grammar` lesson field are now English. The skill registry is untouched.
- **Rulebook risks:** the word *conocer* appears once in the preterite in the text. *Saber* is not in the text.
- **Not fixed:** nothing outstanding.