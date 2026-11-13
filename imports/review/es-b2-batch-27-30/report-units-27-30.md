# Report: es-latam B2 Unit 27 (prepositional-regimes-locutions) and Unit 30 (discourse-markers-contrast-restriction)

Nothing committed. The harness refused the report file, so this reply is the whole report. Both units are fully rewritten in /home/user/parlour-read-b. Every check you listed ends clean except one allowed hit (see Checks).

## Unit 27

**Text** (`content/es-latam/stories/classics/b2/b2-27.json`): 440 words, 6 narration paragraphs, no asterisks, no quotation marks. It is a retelling of Wikisource chapters I to VI, with chapter IV condensed into the Ñacaniná paragraph. `work` is "Anaconda (1921)". `author` and `source` are as briefed.

The old file was wrong throughout. It had Anaconda presiding over the congress, a "Lanceolata", metal screens, Lanceolata killed, and Anaconda caged for Buenos Aires. None of that is in chapters I to VI. Anaconda herself does not appear in the stretch I chose.

Every claim in the text, all checked against the source:
- A hot night. Lanceolada, a yarará (venomous, 1.5 m), goes hunting (ch. I). Sure.
- She waits five hours at a crossing of paths and nothing passes (ch. I). Sure.
- At dawn she goes toward the Casa, an old building long empty. For days she has heard strange noises there (ch. I). Sure.
- A man comes out. She strikes his boot with her head. He sees nothing and walks on (ch. I). Sure.
- She returns to her den, sure it is only the beginning of something serious (ch. I). Sure.
- Next day she thinks of the danger to the whole family (ch. II). The snakes fear the machete (it turns over the forest) and fire (it burns the forest and the dens). Sure.
- That night she warns the others. At 2 a.m. most species are in a cave (ch. II). Sure.
- Terrífica, a very old rattlesnake, presides because her species is abundant in the country (ch. II). Sure.
- Terrífica proposes war without truce, but nobody has a plan (ch. II). Sure.
- Cruzada (called "víbora de la cruz" in the south) says they need the culebras, their cousins without venom. The others dislike the idea (ch. II). Sure.
- Cruzada says someone must go to the Casa to see what the man does, and culebras are more agile. She proposes the Ñacaniná, and the assembly agrees reluctantly (ch. II). Sure.
- Cruzada finds the Ñacaniná climbing a tree (ch. III). The Ñacaniná agrees after Cruzada reminds her she looks like the venomous snakes and defends herself by defending them. Sure.
- She hides under the roof of the Casa and listens to four men at a table (ch. IV). Sure. "Bajo el techo" simplifies "entre pared y techo".
- The Casa is a Government institute preparing serums against viper venom. The men talk of hunting vipers (ch. V). Sure.
- On leaving she is found, the men laugh, and one throws a stick (ch. V). Sure.
- In the cave she reports that the men want to catch the vipers alive and take venom every twenty days (ch. VI). Sure.
- The vipers understand the serum protects people and animals, and their family would starve (ch. VI). Sure.
- Cruzada offers to start the campaign with no plan. The Ñacaniná warns about the black dog following a viper's trail. Terrífica says she will deal with it (ch. VI). Sure.

**Per lesson.** Screens, lesson titles, goals and checklists are in English. All items are rewritten with the same ids, and shapes vary so no lesson has three of one shape. Every lesson got a goal, an srs step and a checklist. Lessons 01 to 05 now have top-level `goal` and `grammar` strings, copied from the b2-22 shape. The consolidation lacked srs, which I added.
- **b2-27-01** "Cause and Occasion" teaches *a raíz de*, *con motivo de*, *en virtud de*. It recaps *debido a* and *a raíz de* from B1 Unit 6.
  - Items: ex01 matching, ex02 fill (*raíz*), ex03 MC (*en virtud de*), ex04 builder, ex05 reading (machete and fire), ex06 dictation.
  - Vocabulary: added *el machete*, *el alcalde*, *el aniversario*. Removed the legalese (*propiciar*, *desencadenar*, *emanar*, *fundamento*, *atribución*, *precepto*, *coyuntura*).
- **b2-27-02** "According to and In Line With" teaches *de acuerdo con*, *conforme a*, *según*. It recaps *según* (B1 Unit 13), *estar de acuerdo con* (B1 Unit 18) and *conforme* (B2 Unit 2).
  - Items: matching, fill (*con*), MC (*conforme al* / *del* / *el*), builder, dialogue (*conforme a*), dictation.
- **b2-27-03** "Aim and Cost" teaches *en aras de* and *a costa de*. It recaps *con miras a* and *con vistas a* (B2 Unit 12) and *con el fin de* (B1 Unit 32). *En pos de* is dropped.
  - Items: matching, fill (*costa*), MC, builder, dialogue with `distractor_skills` {"2": "purpose-connectors"}, dictation.
- **b2-27-04** "Opinion and Limits" teaches *a juicio de* and *al margen de*. *So pretexto de* and *sin perjuicio de* are dropped.
  - Items: matching, fill (*margen*), MC, builder, dialogue (*a mi juicio*), dictation.
- **b2-27-05** "Verbs with Fixed Prepositions" teaches *consistir en*, *derivar en*, *tratarse de*, *abogar por*, plus *derivar de* versus *derivar en* and *tratar de* versus *tratarse de*. *Estribar en*, *versar sobre* and the other legal verbs are dropped.
  - Items: matching, fill (*en*), MC (*consiste en* / *de* / *a*), builder, dialogue (*trata de*), dictation.
- **b2-27-consolidation** has 8 new items: matching, two fills, two reading MCs on the text, builder, dialogue, dictation. Its checklist line names Quiroga.
- **Tags** are now only `prepositional-phrases`, `verbos-regimen-preposicional` and the unit vocabulary skill. I removed `formal-cause-connectors` and `purpose-connectors` as the brief says.

## Unit 30

**Text** (`b2-30.json`): 260 words, 6 paragraphs, no asterisks, no quotation. It is a text about the work, with no scene and no judgement. It shows *en cambio*, *sin embargo*, *ahora bien* and *aun así*. Every claim comes from your fact list:
- Da Cunha was a Brazilian writer and journalist, 1866 to 1909. Sure.
- *Os sertões* was published in 1902, in Spanish *Los sertones*. Sure.
- It is the account of the war of Canudos, 1896 and 1897, in the sertão of Bahía. "Es decir, en el interior de Bahía" is my gloss of "backlands". Sure.
- He wrote it from what he saw as correspondent of *O Estado de S. Paulo*. Sure.
- "A correspondent usually writes articles for his paper; Da Cunha turned what he saw into a book." Sure; this is a general remark plus the list.
- "A book about a war could talk only about battles; this one joins three subjects: the land, its people, the war." Sure; the first half is a hypothesis, not a claim.
- Canudos was led by Antônio Conselheiro. The book does not speak only of that community but also of the land and its people. Sure.
- Vargas Llosa, "whom you already know from other texts of this course", published *La guerra del fin del mundo* in 1981. It tells the same war and draws on *Os sertões*. The two are different books: a novel, and an account of what Da Cunha saw. Sure.
- A reader who had read the novel would recognise the same war in Da Cunha's book. Sure; it follows from "same war".

**Per lesson.** Screens, titles, goals and checklists are in English, and srs is added. The story stays on lessons 01 to 05. The old academic vocabulary (*antagonismo*, *resiliencia* and so on) is replaced by plain words. Dropped as outside the briefed list: *antes bien*, *pese a ello*, *aun con todo*, *por contra*, *en contrapartida*, *bien es verdad que*.
- **b2-30-01** "Contrast Markers" teaches *en cambio*, *por el contrario*, *al contrario*, *no obstante*, *ahora bien* and how they differ from *pero*. It recaps *pero* (A1), *sin embargo* (A2 Unit 28), *no obstante* (B1 Unit 1) and *en cambio* (A2 Unit 28 word list).
  - Items: matching, fill, MC, builder, dialogue, reading.
- **b2-30-02** "Replacing One Thing with Another" covers *sino*, *en vez de*, *en lugar de*. It recaps *sino* (B1 Unit 40) and *no es que… sino que* (B2 Unit 5).
  - Items: matching, fill (*sino*, tagged `sino-vs-pero`), MC (*en vez de* + infinitive), builder, dictation, reading.
- **b2-30-03** "Even So" covers *con todo* and *aun así*. It recaps *aunque* (A2 Unit 28) and *a pesar de que* (B1 Unit 32). It states the *aun*/*aún* accent rule.
  - Items: matching, fill, MC, builder, dialogue, reading.
- **b2-30-04** "Two Sides of a Question" covers *por un lado … por otro* and *por una parte … por otra*. It recaps *por un lado* (B1 Unit 23).
  - Items: matching, fill (*otro*), MC, builder, dictation, reading.
- **b2-30-05** "Softening an Objection" covers *eso sí*, *de todos modos*, *ahora bien*. It recaps *ahora bien* from lesson 01.
  - Items: matching, fill (*sí*), MC, builder, dialogue, reading.
- **b2-30-consolidation** has 8 new items: matching, two fills, two readings, builder, dialogue, dictation. Its checklist line names Da Cunha.
- Wrong options that are real markers of another skill carry `distractor_skills` {"porque-y-por-eso"}.

## Checks
| | before | after |
|---|---|---|
| Unit 27 check-content | 1 error, 19 suspects | 0 errors, 0 suspects |
| Unit 27 unmet words | 103 | 1 |
| Unit 30 check-content | 8 errors, 17 suspects | 0 errors, 0 suspects |
| Unit 30 unmet words | 104 | 0 |

- The one remaining Unit 27 hit is *consiste* in consolidation ex05. It is a form of the listed *consistir en*, which your rules allow.
- `check_unit_refs.py` reports 0 recaps to check for both units.
- Both renders have no `!!`.
- `validate-content.py --changed` passes: es-latam 47 passed, 0 failed.
- `build-manifest.py` and `build_word_lesson_index.py` regenerated curriculum, decks, manifests and the word-lesson index. That is expected.

## Challenges
The two files are `/home/user/parlour-read-b/challenges-prepositional-regimes-locutions.json` and `/home/user/parlour-read-b/challenges-discourse-markers-contrast-restriction.json`. Each has six entries in the B1 shape, with `canDo` equal to the lesson's first checklist line. I merged them temporarily into `curriculum/challenges.json` to run `unmet-words.js`, then restored that file. Result: 0 hits. They are not merged into the real file.

## Spanish lines I am unsure of
- 27-02 ex02 accepts only *con* after *de acuerdo*. The screen says careful writing prefers *con*, but *de acuerdo a* is common in speech.
- 30-03 ex03 uses *aún así* as a wrong option for spelling only. RAE writes *aun así*; a native might not mark it wrong.
- 30-05 ex03 uses *eso si* without the accent as a wrong option, for spelling only.
- I believe the wrong options in 27-01 ex03 and in the Unit 30 dialogues are real markers with a wrong meaning, and that each context pins one answer.

## For the user
- **Skills before their screen:** none. Unit 27 teaches no registry skill. In Unit 30, `contrast-markers` is taught on 30-01 and used from there on.
- **Lesson 30-04:** its whole point, *por un lado … por otro*, is the known skill `ordering-markers`. The skill title says A2 Unit 28, but the first italic appearance is B1 Unit 23. I tagged the items `contrast-markers`.
- **`prepositional-phrases`:** B1 Unit 24's screen shows only *mediante*, so Unit 27 effectively teaches this skill. The brief tags it that way.
- **Consolidations:** both consolidation lessons carry reading items on the text but have no story section. The text is on 27-01 and on 30-01 to 05. Add the story to the consolidations if you want it re-readable there.
- **Generated files:** besides the build outputs above, the challenge files are the only extra files.
- **Scratch files:** my scratch generators are in `/home/user/parlour-read-b/.scratch/` (untracked).