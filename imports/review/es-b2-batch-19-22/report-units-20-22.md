Both units are rewritten in /home/user/parlour-read-b, nothing committed. check-content, unmet-words, `render_lesson.js` (0 `!!`), `check_unit_refs.py` and `validate-content.py --changed` are clean for both. I could not write the report file, so this reply is the report.

Your fact list was too thin for a fully reliable Unit 20 text: several lines are my own wording or arithmetic (marked below). The four double-participle pairs I could not check against the RAE (DPD); the rae.es pages and the search tools returned 403. Two Unit 22 choices need your call: the `volverse` option in 22-01 ex05, and Unit 20's topic words put in earlier lessons because the consolidation has no vocabulary section.

## Check counts (before → after)

| | check-content errors | suspects | unmet words |
|---|---|---|---|
| Unit 20 (`analytical-resultative-passives`) | 10 → 0 | 7 → 0 | 97 → 0 |
| Unit 22 (`verbs-becoming-transformation`) | 1 → 0 | 20 → 0 | 86 → 0 |

- Unmet-words was rerun after the last edit with the challenge targets temporarily merged into `curriculum/challenges.json`. That file is restored, so the challenges are only in my two files.
- `build-manifest.py` and the word-lesson index were regenerated, which is why the manifest, deck and index files show as modified.
- The tags lock and `skills/*.json` are untouched.

## Unit 20 (analytical-resultative-passives)

Every grammar screen, lesson title, goal and checklist is now in English and opens with a recap. Each lesson has a matching, fill-blank, English multiple-choice, builder, dialogue and dictation item. Goal lines became `I can…`, and the missing `srs` and `checklist` sections were added.

- **b2-20-01**: the `ser` passive in the preterite, present perfect and future, plus participle agreement. The recap names B1 Unit 18 and the B1 Unit 6 `se` passive. Items ex01–ex06 are new, so the old jargon items are gone; `fundar`, `inaugurar`, `derribar` and `monumento` are listed.
- **b2-20-02**: when to name the doer with `por`, doer vs tool (`con`), and `por` as doer vs reason. The vocabulary became `alcalde`, `congreso`, `terrateniente`, `indígena` and `oprimir`.
- **b2-20-03**: `estar` + participle as the result, with `ya`, `ahora` and `desde` as cues. ex03 and ex05 carry `distractor_skills` for `ser-passive` and `progressive`.
- **b2-20-04**: `imprimido/impreso`, `freído/frito`, `proveído/provisto` and `elegido/electo`. The regular form goes with `haber`; the short form works as an adjective or after `estar`.
  - Every item has one forced right answer. I avoided any item where `he impreso` and `he imprimido` compete.
  - ex03 uses `está imprimido` as a wrong option. That rests on the rule that the regular form is not used as an adjective (unsure, see below).
- **b2-20-05**: choosing between the active verb, the `ser` passive, passive `se` and `estar` + participle. English speakers overusing the passive is said plainly, with no "prosa formal" jargon. ex02 is tagged `pasiva-refleja`, and ex03 carries `distractor_skills` for `pasiva-refleja` and `ser-passive`.
- **b2-20-consolidation**: the old text is replaced by an original 328-word text of 7 paragraphs. It has no scene, quote, character name or asterisk. Four reading questions (English stems, Spanish options) and eight items.

Text claims (confidence in brackets):
1. Arguedas was a Bolivian writer (fact list, sure).
2. He was born in 1879 and died in 1946 (fact list, sure).
3. The text names *Raza de bronce* as his novel (fact list, sure).
4. The novel was written by Arguedas (sure).
5. It was published in 1919 (sure).
6. The author was still alive when it was published (follows from 1946, sure).
7. Forty years passed between his birth year and 1919 (arithmetic, sure).
8. He died twenty-seven years after publication (arithmetic, sure).
9. More than a hundred years have passed since 1919 (arithmetic, sure).
10. The novel is set in an indigenous community of the Altiplano (fact list, sure).
11. "Ambientada" is defined as the story taking place in that place (definition, sure).
12. The theme is the oppression of indigenous people by landowners (fact list, sure).
13. "Terrateniente" is defined as a person with a lot of land (definition, sure).
14. It is considered the first text of Bolivian indigenismo (fact list, sure).
15. The text does not say who considers it so (true of the text, sure).
16. "Indigenismo" comes from "indígena" (etymology, outside your list, fairly sure).
17. The text recounts no scene and quotes nothing (true of the text, sure).
18. A short text cannot replace the novel (opinion, harmless).
19. Whoever wants to know what happens must read it (harmless).
20. After reading, the reader can compare the text with the book (harmless).

## Unit 22 (verbs-becoming-transformation)

All screens, titles, goals and checklists are in English. Every screen opens with a recap naming B1 Unit 25 or 39, checked against those screens.

- **b2-22-01**: `ponerse` is the change and `quedarse` the state that stays; a cause can be the subject (*La noticia nos puso tristes*). Includes a warning against confusing it with `ponerse a` (A2 Unit 32).
- **b2-22-02**: `hacerse` + noun for a profession or choice, `volverse` + adjective for what happens to someone, and `hacerse el` = pretend. The items are built so the wrong options are structurally wrong, because `hacerse` and `volverse` overlap with character adjectives.
- **b2-22-03**: `convertirse en` and `transformarse en` take `en` + noun, with a cause as subject (*La tormenta convirtió la calle en un río*).
- **b2-22-04**: `llegar a ser` only, as a long road, against `hacerse` and `convertirse en`. It stays off `llegar a` + other infinitives.
- **b2-22-05**: choosing by kind of change, plus one-word verbs of change (`palidecer`, `enrojecer`, `enmudecer`, `enriquecerse`, `empobrecerse`). The old `pasar a ser` is removed because it is Unit 23. ex02, ex04 and ex06 are tagged with the unit vocabulary skill.
- **Old material removed**: the grammar screens' claims about Valparaíso, Mistral and Lota coal are gone, and so are the old Spanish metalanguage vocabulary entries. The `tell-absolute`, `course-variant` (*billetes*) and `vocab-unused` flags cleared with the rewrite.

**Story** (b2-22-consolidation): rewritten against the Wikisource source, 447 words in 7 paragraphs, same order, no quotation marks, no asterisks.
- Removed from the old file: Lota, the Cousiño family, two small brothers, "Pedro" as a companion, the "vertical conduit", the mother "kneeling and jumping" on purpose and the closing praise.
- Added from the source: the dismissal and the Chiflón offer, the mother, the alarm, the three bodies, the vision, the fall.
- Verbs of change used: `se quedaron preocupados`, `se quedaban sin trabajo`, `se volvió más suave`, `se volvía porosa`, `se quedó callado`, `se quedó encantada`, `se quedó inmóvil`.
- Lota is not mentioned, because the source does not show it. `source` is set to the sentence you gave.
- Four reading questions and eight items.

## Spanish I am unsure of (unsure)
- **20-04 grammar tip and ex03**: I followed the brief's rule (regular after `haber`, short form as adjective or after `estar`) but could not check the DPD. The DPD may also accept `he impreso`, `he frito` and possibly `papas freídas`. I avoided them in all right answers and wrong options except the `está imprimido` wrong option in ex03. Please check that option.
- **20-04 `proveer`**: `provisto de` is the only use drilled.
- **22-01 ex05**: the `se volvieron callados` wrong option is grammatical, so it is wrong by meaning only. `se pusieron callados` would also be acceptable, so I left it out of the options.
- **22-04 ex05**: `se puso una estrella` and `se volvió una estrella` are wrong only because a noun follows. `se hizo una estrella` would be fine, so it is not offered.
- **20-02 tip**: the claim that `por` can mean either the doer or the reason, and that a tool takes `con`, is standard but I did not check it against a source.

## For the user
- **Skills used before their own screen**: none. Unit 20 items use `pasiva-refleja` (B1 Unit 6), `ser-passive` (B1 Unit 18) and `progressive` (A1); Unit 22 uses only `verbs-of-change` and the vocabulary skill.
- **Skills the sheet lists as later or hidden**: no lesson depends on one. I kept the impersonal third-person plural, `uno`, `pasar a`, `volver a` and `llegar a` + infinitive out of every screen and item.
- **Unit 20 topic words moved to earlier lessons**: the consolidation has no vocabulary section, so `indígena`, `terrateniente` and `oprimir` are in b2-20-02, `ambientada` and `altiplano` in b2-20-03, and `indigenismo` in b2-20-05. They are used in those lessons' items, but they sit slightly off-theme there.
- **Challenges**: written to the two files in the worktree, not merged into `curriculum/challenges.json`. Targets name no relatives of Carlos or Meg; where a third person is needed they say "el hombre" or "la noticia".
- **Not fixed**: nothing outstanding. The consolidation titles are English ("Unit Review: …").

Files are in /home/user/parlour-read-b:
- /home/user/parlour-read-b/challenges-analytical-resultative-passives.json
- /home/user/parlour-read-b/challenges-verbs-becoming-transformation.json
- /home/user/parlour-read-b/content/es-latam/stories/classics/b2/b2-20.json
- /home/user/parlour-read-b/content/es-latam/stories/classics/b2/b2-22.json