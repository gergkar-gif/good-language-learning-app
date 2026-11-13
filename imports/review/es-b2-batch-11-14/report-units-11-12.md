# Report: es-latam B2 Units 11 (mixed-restrictive-conditionals) and 12 (purpose-clauses)

Both units are finished in `/home/user/parlour-read-a`, nothing committed. I did not write a report file, because my instructions forbid subagent report files. The challenges files are written:
- `/home/user/parlour-read-a/challenges-mixed-restrictive-conditionals.json`
- `/home/user/parlour-read-a/challenges-purpose-clauses.json`

## Checks (before → after)

| | Unit 11 | Unit 12 |
|---|---|---|
| check-content errors | 9 → 0 | 9 → 0 |
| check-content suspects | 16 → 1 | 23 → 1 |
| unmet words (my count for Unit 11 is by hand from the first run) | about 111 → 0 | 109 → 0 |
| `check_unit_refs --labels --bare` | 0 left | 0 left |
| `validate-content.py --changed` | passes, es-latam 47 files | same run |
| `render_lesson.js` | no `!!` lines | no `!!` lines |

I reran unmet-words and check-content after my last edit. `build-manifest.py` and the word index were rerun too.

The one remaining suspect in each unit is an `answers-alternatives` hit that I accept:
- **b2-11-02.ex02:** `habría` and `hubiera` are the same verb in the same slot (hubiera for habría, B2 Unit 10).
- **b2-12-03.ex02:** `miras` and `vistas` are synonyms (*con miras a* and *con vistas a*).

## Unit 11

All six lessons: lesson title, goal, goal lines, grammar screen and vocabulary list are now in English, and every question stem is in English. Lessons 01–05 had no checklist, so each got an `srs` section and a `checklist` section whose lines match the goal lines. I rewrote all the vocabulary lists, because the old words (*prerrogativa*, *anuencia*, *perentorio* and so on) were unmet or unused. Every listed word now appears in its lesson's matching item.

**b2-11-01, past condition with a present result** (screen: A Past Cause, a Present Result)
- The screen recaps B1 Units 35 and 4, then explains why the result takes the simple conditional.
- ex02 is a fill-blank on `sería`.
- ex03 has the ds tags on the *habría vivido* option (`pluscuamperfecto-subjuntivo-si`) and the *aceptara* option (`hypothetical-structures`).
- ex04 and ex06 are rewritten.
- ex05 is a new dialogue with ds `pluscuamperfecto-subjuntivo-si`.

**b2-11-02, lasting trait with a past result** (screen: A Lasting Trait, a Past Result)
- The vocabulary is now personality traits: *terco*, *despistado*, *sensato*, *desconfiado*, *derrochador*.
- ex02 accepts `habría` and `hubiera`.
- ex03 has ds `imperfect` on the *Si era* option.
- ex04, ex05 and ex06 are rewritten with simple contexts.

**b2-11-03, strict conditions** (screen: Strict Conditions: Siempre y Cuando and More)
- The screen recaps *con tal de que* (B1 Unit 21), *siempre que* (B2 Unit 7) and *a condición de que* (B2 Unit 9). New: *siempre y cuando* and *con la condición de que*.
- Items teach `conditional-conjunctions`, with ds `present-tense` and `futuro-simple` on the indicative and future options.

**b2-11-04, exceptions** (screen: Unless: Adding Excepto Que and Excepto Si)
- The screen recaps *a menos que* (B1 Unit 21) and *a no ser que*, *salvo que*, *salvo si* (B2 Unit 9). New: *excepto que* and *excepto si*.
- ex03 tests equivalence with *si no* (ds `concesivas-aunque` on the *aunque* option and `por-que-y-porque` on the *porque* option).
- ex05 contrasts *salvo si* (indicative) with *salvo que* (subjunctive).

**b2-11-05, polite conditions** (screen: If I May: Polite Conditions)
- New: *si no me equivoco*, *si mal no recuerdo*, *si me permite*, *si no es molestia*.
- It recaps A2 Unit 26 (*quisiera*, *me gustaría*) and B2 Unit 9 (*si tuviera un momento*).
- Items are tagged `polite-softening`, the only fitting skill.
- ex03 has ds `imperfect-subjunctive-forms` on the *equivocara* option and `subjuntivo-morfologia` on the *equivoque* option.

**b2-11-consolidation** (the exercise file is rewritten)
- ex01 to ex08 are rewritten.
- ex05 is a sentence-order on the text's dates.
- ex06 is a reading item.
- **New ex09** is a reading item (*when did La tregua come out*), listed in the lesson's `exerciseRefs`.
- Checklist and goal lines are English. The checklist's fourth line names Benedetti.

### Text: b2-11.json, rewritten as an original text about Benedetti and *La tregua*

- **Length:** 307 words, 6 narration paragraphs.
- **Reading questions:** 3, with English stems and explanations, answerable from the text.
- **Story fields:** `order` 11, `characters` empty, `source` "Texto original de Parlour…" (same as b2-02 and b2-10).

Every factual claim in it, with my confidence:
1. Benedetti was an Uruguayan writer — sure (your list).
2. He was born in 1920 and died in 2009 — sure (your list).
3. *La tregua* is one of his novels, published in 1960 — sure (your list).
4. The text will not give the ending — sure (it is about the text, not the book).
5. *La tregua* is written as a diary, the diary of Martín Santomé — sure (your list).
6. The reader knows the story through Santomé's words — high (follows from the diary form).
7. The novel has no outside narrator, so the reader "reads the pages of a diary" — high. Reviewer please check: this assumes the whole book is the diary.
8. Santomé is a widower with three children — sure (your list).
9. He works in an office and is close to retirement — sure (your list).
10. The reader could know nothing of his life unless he wrote it in the diary — high (follows from the diary form).
11. In that same office a young woman, Laura Avellaneda, starts working, and Santomé falls in love with her — sure (your list).
12. The reader follows that love through the diary, as Santomé writes it — high (follows from the diary form).
13. If the book were not Santomé's diary, readers in 1960 would not have known Laura from his point of view — high (follows from the diary form).
14. If Benedetti had not published it, today's readers could not open Santomé's diary — sure (trivially true).
15. The three counterfactuals in 6, 13 and 14 are my wording. They only restate the diary form and the publication, so they are logically safe.
16. Whoever wants the ending can get it by reading the whole book, and the text does not say what happens to Santomé and Laura — sure.

## Unit 12

All six lessons: same treatment as Unit 11 (English throughout, new checklists), with new vocabulary lists. Items were rewritten with everyday contexts, and the legal and political ones are gone. Except for the consolidation, I rewrote every screen and item set from scratch.

**b2-12-01, two subjects, formal** (screen: Formal Purpose: A Fin de Que and Con el Objeto de Que)
- The screen recaps *para que* (B1 Unit 4) and the imperfect subjunctive after a past verb (B1 Unit 38).
- New: *a fin de que* and *con el objeto de que*.
- ex02 accepts `conocieran` and `conociesen`.

**b2-12-02, one subject, infinitive** (screen: One Person, One Verb: Purpose with the Infinitive)
- It recaps B2 Unit 4 and *con el fin de* (B1 Unit 32).
- New: *a fin de* and *con el objeto de* + infinitive.
- Items are tagged `subjuntivo-de-finalidad-para-que` or `infinitive-vs-que-subjunctive`.

**b2-12-03, `purpose-connectors`** (screen: Looking Ahead: Con Miras A and Con Vistas A)
- It teaches *con miras a* and *con vistas a* with an infinitive or a noun, plus *de modo que* + subjunctive for purpose.
- The old indicative-result contrast is deleted, so the consequence skill is not taught.
- ex03 has ds `antes-despues-infinitive` and `a-pesar-de` on the two wrong options.

**b2-12-04, negative purpose** (screen: Preventing Something: Para Que No and No Sea Que)
- It covers *para que no*, *a fin de que no*, *para no* + infinitive and *no sea que*.

**b2-12-05, purpose inside a hypothetical sentence** (screen: Purpose Inside a Hypothesis)
- It covers the imperfect subjunctive after a conditional or past conditional.
- The old *al solo efecto de* and the *El túnel* plot examples are removed.

**b2-12-consolidation**
- ex01 to ex08 are rewritten.
- ex06 is now a reading item on the year of *El túnel*, because the Castel facts used words that are still unmet.
- **New ex09** is a reading item on the report's other name. It is listed in the lesson's `exerciseRefs`.

### Text: b2-12.json, rewritten as an original text about Sabato and *El túnel*

- **Length:** 341 words, 6 narration paragraphs.
- **Reading questions:** 3, with English stems and explanations, answerable from the text.
- **Story fields:** `order` 12, `characters` empty, `source` "Texto original de Parlour…" (same as b2-02 and b2-10).
- **Purpose clauses:** all of them describe this text or the reader, never Sabato's wishes.

Every factual claim in it, with my confidence:
1. Sabato was an Argentine writer, born in 1911 and died in 2011 — sure (your list).
2. He trained and worked as a physicist before he became a writer — sure (your list).
3. *El túnel* appeared in 1948 and was his first novel — sure (your list).
4. A painter, Juan Pablo Castel, tells it in the first person — sure (your list).
5. From the first page, Castel explains that he killed the woman he loved, and explains why — sure (your list).
6. So the reader does not need to reach the end to know what Castel did — high (follows from 5).
7. The reasons are given by the painter himself, not found outside the text — high (follows from 5). Reviewer please check.
8. Whoever reads *El túnel* reads the painter's own explanation and not someone else's — high (follows from the first-person form).
9. Sabato later presided over the CONADEP, the commission that investigated what happened to the people disappeared during the Argentine dictatorship — sure (your list).
10. The commission's report, from 1984, is called *Nunca más* and is also known as the *Informe Sabato* — sure (your list).
11. *El túnel* is a novel from 1948 and *Nunca más* is a report from 1984 — sure.
12. "There are two paths to know Sabato: reading *El túnel* or *Nunca más*" — an opinion about reading, not a fact about the author. I'd soften it if you object.
13. The text itself does not tell the whole story — sure (about the text, not the book).

## For the user

- **The brief says "adds *a condición de que*" (11-03) and "adds *a no ser que*" (11-04), but both are already taught.** *A condición de que* and *siempre que* are in B2 Unit 9 lesson 4, and *a no ser que*, *salvo que* and *salvo si* are in B2 Unit 9 lesson 5. I therefore recap them and added the forms that no earlier screen teaches: *siempre y cuando*, *con la condición de que*, *excepto que* and *excepto si*. Tell me if the brief meant something else.
- **Skills used before their screen:** none found. Both units use only skills from the knowledge sheets.
- **Lesson whose whole point is a skill the sheet lists as later or hidden:** none. 12-03 teaches `purpose-connectors`, which is this unit's own skill.
- **Skill choices:**
  - 11-05 items are tagged `polite-softening` (A2 Unit 26) because there is no skill for the parenthetical *si* phrases. A real fit needs a user decision, since the skill list is frozen.
  - The consolidation sentence-orders use `secuencia-narrativa` (A2), as the other consolidations do.
- **Moved lesson:** *con el fin de* is taught in B1 Unit 32, so b2-12-03 recaps it. The brief's "with a noun" for *con el fin de* is not shown, since it is rare. The noun examples use *con miras a* and *con vistas a* only, and the screen says *con el fin de* normally takes an infinitive. Tell me if you want a noun example anyway.
- **Hidden-track screens** (`b1-democratizacion-02-con-miras-a`, `b1-integracionregional-01-a-fin-de-que`, `b1-represionpolitica-02-con-el-fin-de`, `b1-conosur-01-en-aras-de`) also teach these connectors. I treated them as not met.
- **Challenges for the reviewer to merge:** the real `challenges.json` has no b2-11 or b2-12 entries yet, so the render shows its placeholder text. Both challenge files carry the full entries, with `canDo` copied from each lesson's first checklist line.

## Spanish lines I am unsure of

None that I think are wrong. Native-speaker review would still help on these:
- **(unsure)** 11-05 screen example *Usted, si no me equivoco, ya trabajó con nosotros*: grammatical, but the placement of the parenthetical is a style choice.
- **(unsure)** 12-04 ex05: *Hablo bajo para que no despierto al bebé* is a wrong option, but a native reader may find the mood error less obvious than the intended one.
- **(unsure)** 12-03 *con vistas a las vacaciones de julio*: natural, though *con miras a* is more common with plans than with a date.

## Files touched

- Everything is under `content/es-latam/`: `grammar/b2/`, `exercises/b2/`, `lessons/b2/`, `vocabulary/b2/` and `stories/classics/b2/`, for `b2-11-*` and `b2-12-*`.
- The two challenges files are in the worktree root.
- `build-manifest.py` also regenerated the usual curriculum, deck and manifest files for all courses, as expected.
- I ran `git diff` only to review, never `git add` or `commit`.