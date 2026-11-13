# es-latam B2 Unit 1 (nuance-precision-emphasis): reader A report

Nothing is committed, and the report file could not be written, so this reply is the report. `build-manifest.py` also regenerated curriculum.json, word-lesson-index.json, the decks and the stories manifests, as expected. The challenges are in `/home/user/parlour-read-a/challenges-nuance-precision-emphasis.json`: six entries, with `canDo` copied from each lesson's first checklist line.

## Checks
- **check-content:** 12 errors and 11 suspects before, 6 errors and 2 suspects after.
  - All 6 errors are the expected `taught-later` on `stance-adverbs`: b2-01-02 ex02, ex03, ex04, ex07, ex09 and consolidation ex03.
  - The 2 suspects are `answers-alternatives` on b2-01-02.ex05 (*rotundamente* / *categóricamente*) and b2-01-03.ex03 (*fueron* / *resultaron*, the screen teaches *ser / resultar*). Both are true alternatives, so I kept them.
- **unmet-words:** 60 hits before, 0 after. I checked the challenge targets with a copy of the script that reads my challenges file, also 0.
- **Other checks:** render_lesson has no `!!`. `check_unit_refs --labels --bare` is clean. `validate-content --changed` passes for es-latam (24 passed) with no es-latam warnings.

## Per lesson
**All lessons.**
- All five grammar screens are rewritten in English. Recaps use the "You know *X* from B1 Unit N" form:
  - *lo que*: B1 Unit 20.
  - *lo importante*, *lo mejor*, *sino*, *sino que*, *no solo*: B1 Unit 40.
  - *resultar*: B1 Unit 15.
  - *ser*: A1 Unit 1.
- Titles, goals and checklists are in English, and no checklist or goal sections were added.
- Every multiple-choice stem is in English with no hint or english.
- Writing items now carry a single tag.

**b2-01-01.**
- The old tip called *Fue en 1990 que* a queísmo error. I replaced it with a hedged note (unsure, see below).
- I dropped the goal line about plural agreement, since no item practises it; agreement stays on the screen only.
- Items ex01–ex08 are all rewritten:
  - ex02: cleft vs non-cleft, using *radicar*.
  - ex03: *los que*.
  - ex04: the builder.
  - ex05: *precisamente*.
  - ex06: listening, using *crucial*.
  - ex07: who/where/when clefts answering "who".
  - ex08: writing, using *enfatizar*.
- I fixed the length-giveaway error and removed the unmet *ambas, intentamos, comisión, directiva, impulsó, hendida, focalizar*.

**b2-01-02 (stance adverbs).**
- The screen teaches `stance-adverbs` fully: what they do, where they go, commas, and stance vs manner. It covers *francamente, sinceramente, afortunadamente, lamentablemente, indudablemente, en realidad, en rigor, propiamente dicho, precisamente, apenas*.
- I added *sinceramente, afortunadamente, lamentablemente, en realidad* to the vocabulary list, as otherwise they are met only through the screen.
- The items are ex01–ex09. New items are ex08 (fill) and ex09 (listening), both listed in the lesson.
  - ex02, ex03, ex04, ex07 and ex09 keep `stance-adverbs`.
  - ex05, ex06 and ex08 are vocabulary.
- I removed the *Ayer* tell, the unmet words, and *negó* (hidden-track `reporting-verbs`).

**b2-01-03.**
- I dropped the "direct object fronting" row (*Tres cartas escribió el autor* is archaic). The screen now shows an adjective, a place or time phrase, or *de* + noun phrase first.
- The items are ex01–ex08, with new ex07 (MC) and ex08 (listening):
  - ex03: plural agreement.
  - ex04: builder.
  - ex05: a dialogue with three fronted answers to "where".
- I used *concluyente* (ex02), *premisa* (ex07), *subyacer* (writing ex06) and *prevalecer* (ex08).
- I removed the *Ayer* tell and the unmet words.

**b2-01-04.**
- The screen recaps `sino-vs-pero` and `correlativos-no-solo-sino` and adds only three things: the contrastive cleft *No fue X, sino Y lo que*, *No fue X quien … sino Y*, and *sino más bien*. It also covers *sino* vs *si no*.
- The items are ex01–ex09, with new ex08 (fill, *más bien*) and ex09 (second matching: *antagónico, sutileza, contraponer, más bien*).
- The dialogue ex06 offers *sino que* / *sino* / *pero que*.
- I removed the unmet words.

**b2-01-05.**
- The story is replaced (see the text below). The screen is rewritten as a synthesis built on the new text.
- Reading items ex02 and ex03 are rewritten (category reading, no `teaches`); ex04–ex08 are rewritten too. New ex09 is a second matching, so the kept words *conjetura, indicio, vislumbrar, resolución* are used.
- I removed the *ninguna* tell.
- I kept the vocabulary list (reason in "For the user").

**b2-01-consolidation.**
- All 8 items are revised so none copies a lesson item. ex07 is now a real dialogue-complete.
- I removed the *Ayer* tell and the unmet words.

## The text (336 words, 7 narration paragraphs)
It has no scene, no dialogue and no quotation. Title: "Borges y el jardín de los caminos que se dividen". `characters` is `[]`. I also rewrote the summary, the source, the three comprehension questions and their explanations. «» marks only titles. Factual claims:
1. Borges was born in Buenos Aires in 1899 (sure).
2. He died in Geneva in 1986 (sure).
3. He was an Argentine writer (sure).
4. He wrote stories, essays and poems (sure).
5. His books have been translated into many languages (sure).
6. Many readers consider him one of the most important authors in Spanish (an opinion; sure it is widely held, but check the wording).
7. "El jardín de senderos que se bifurcan" is one of his best-known stories (sure).
8. It first appeared in 1941, in a book with the same title (sure).
9. Three years later that book became part of *Ficciones*, published in 1944 (sure).
10. At first sight it is a spy story (sure).
11. It is set in England during the First World War (sure).
12. The protagonist is a Chinese professor working for Germany (sure).
13. He must send one secret word (sure).
14. The story is about secrets, danger, tension and also ideas (general).
15. Its distinctive idea is time as a garden of paths that divide (sure).
16. On that idea the future is not one path: each decision opens several possible paths, all existing at once (sure; framed as "según esa idea").
17. The title comes from that image; *sendero* is a narrow path and *bifurcarse* means to divide in two (dictionary senses, sure).
18. The title speaks of a garden whose paths divide again and again, "como en un laberinto" (fairly sure).
19. Readers find the image of a labyrinth made of time unusual, and the story keeps attracting readers (general).

## Spanish I am unsure of
- **(unsure)** Screen 1 tip: *Fue en 1990 que nació* is common in conversation, especially in Latin America. I could not reach the web to verify, so I hedged it; please check.
- **(unsure)** Screen 1: the register wording of the plural-agreement note and the examples *Fue con Ana con quien hablé* and *Fueron los vecinos quienes llamaron*.
- **(unsure)** Screen 3: "*Decisiva la intervención fue* sounds unnatural".
- **(unsure)** The challenge targets *Decisivo fue practicar cada día* (b2-01-03) and *Lo que más les gusta a los lectores es…* (b2-01-05).
- **(unsure)** b2-01-02.ex08, *Te agradezco ____ tu ayuda con el proyecto*: the answer is pinned to *sinceramente* only.

## For the user
- **Skill used before its screen:** `stance-adverbs` is drilled in b2-01-02 and the consolidation while `taught_in` is still b2-brasilsudeste-04-a-gr. Please move it to `b2-01-02-a-gr`.
- **Other skills:** `sino-vs-pero`, `correlativos-no-solo-sino` and *resultar* + adjective are all known and recapped. No other lesson's main point is a later or hidden skill.
- **Vocabulary lists were kept, not trimmed.** Several words are first listed in this unit and used by later units without being listed there (*radicar, premisa, subyacer, antagónico, sutileza, contraponer, concluyente, conjetura* and others). I fixed the 11 `vocab-unused` suspects by using the words, which is why the b2-01-04 and b2-01-05 lists each have a second matching item.
- **Challenges** invent only minimal activities: Carlos's office timetable, his "last project", Meg's course.
- Nothing is left unfixed beyond the two `answers-alternatives` suspects above.