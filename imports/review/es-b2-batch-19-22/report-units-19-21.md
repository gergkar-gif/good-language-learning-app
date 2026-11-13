# Report: es-latam B2 Unit 19 `passive-se` and Unit 21 `impersonality-strategic-distance`

Both units are rewritten. Nothing is committed. I did not write `report-passive-se.md`; this reply is the full report. The two challenge files are written and the checks are clean (counts below).

Files touched, per unit, for lessons 01–05 and the consolidation:
- the lesson file;
- the `-a-gr` screen (lessons 01–05);
- the `-voc` file (lessons 01–05);
- the `-ex` file;
- the story file (`b2-19.json`, `b2-21.json`);
- `/home/user/parlour-read-a/challenges-passive-se.json`;
- `/home/user/parlour-read-a/challenges-impersonality-strategic-distance.json`.

`build-manifest.py` also rewrote generated files, as expected:
- `curriculum.json`;
- the `decks.json` files;
- the `stories/manifest.json` files;
- `word-lesson-index.json`.

## Checks (before → after)

| Check | Unit 19 | Unit 21 |
|---|---|---|
| `check-content` errors | 7 → 0 | 4 → 0 |
| `check-content` suspects | 7 → 0 | 17 → 0 |
| `unmet-words`, challenge targets included | 76 (hand-counted from the output) → 0, rerun after the last edit | 85 → 0, rerun after the last edit |
| `check_unit_refs --labels --bare` | 0 left | 0 left |

- `validate-content --changed`: es-latam 93 passed, 0 failed; all schemas match.
- `render_lesson`: no `!!` lines. I read every screen and item as rendered.
- To test the challenge targets I merged both challenge files into `curriculum/challenges.json`, ran `unmet-words.js`, then restored the file with `git checkout`. It is unchanged.
- The rendered challenge screens show generic placeholder text, because `challenges.json` was not changed. The reviewer merges the two challenge files.

## What I changed, all lessons

- **Screens and titles.** Each grammar screen, lesson title, goal and checklist is rewritten in English. Each screen opens with a recap in the "You know *X* from … Unit N" form.
- **Checklists.** Lessons 01–05 of both units got an `srs` section and a `checklist`.
- **Vocabulary lists.** Each is replaced by 4–5 words (matching in `ex01` uses all of them), with `pos` spelled out. The unit-19 lists lost the old technical words and the unit-21 lists lost the old abstract ones.
- **Items.**
  - Question stems are in English, and no multiple-choice item has a `hint` or `english`.
  - Each wrong option has one fault.
  - The right option's position varies.
  - `distractor_skills` are set where a wrong option is a real form of another skill (`futuro-simple`, `por-vs-para`, `preterito-indefinido`, `present-tense`, `imperfect`, `pasiva-refleja`, `se-impersonal`).
  - Ids are unchanged (`b2-21-con.exN` kept).
  - `teaches` follows the wrong answer: agreement items get `pasiva-refleja`, singular/plural contrast items get `se-pasivo-vs-impersonal` or `se-impersonal`, unit words get `b2-passive-se-vocab` or `b2-impersonality-strategic-distance-vocab`.

## Unit 19 (passive-se)

- **b2-19-01, "Passive Se: The Verb Agrees With the Thing".**
  - B1 Unit 6 already taught plural agreement, so the screen recaps it.
  - New content: agreement with two nouns, the noun before the verb, and *se* + *poder*/*deber* + infinitive.
  - Items ex01–ex06.
- **b2-19-02, "Passive Se or Impersonal Se?".** Recaps B1 Unit 6 and the personal *a* (A1 Unit 24). New content: person with *a* → singular verb, noun after a preposition → singular verb (*Se habla de los precios*). Items ex01–ex06.
- **b2-19-03, "Who Did It? Not With Passive Se".** Recaps the *ser* passive with *por* (B1 Unit 18). New content: passive *se* takes no *por* + doer; alternatives are the *ser* passive or an active sentence. A tip covers the other *por* (*por internet*). Items ex01–ex06.
- **b2-19-04, "Notices and Instructions With Se".**
  - It plainly teaches *Se ruega*, *Se alquilan departamentos*, *Se admiten*, and recipes.
  - A2 Unit 24 and B1 Unit 6 already taught *se prohíbe* and *se busca*, so the lesson recaps them.
  - Items ex01–ex06.
- **b2-19-05, "Which Se Is It?".**
  - It covers reflexive, reciprocal, passive, impersonal and "accidental" *se* (*Se me cayó el vaso*).
  - Accidental *se* is new here.
  - Items ex01–ex06.
- **Consolidation.** The title and goal are rewritten. The checklist's text line is "I can read a short text about Vargas Llosa and La ciudad y los perros." Items ex01–ex08 are new, with no copies of lesson items.

## Unit 21 (impersonality-strategic-distance)

- **b2-21-01, "They Say, One Knows".** Recaps *se dice que* (B2 Unit 18) and B1 Unit 6. Teaches *Dicen que…*, *Me robaron la bicicleta*, *Llaman a la puerta*, and *Uno nunca sabe* (singular verb, *su*).
- **b2-21-02, "Se, They or One?".** Recaps Unit 19. New content: choosing among *se*, a plural verb and *uno*, and impersonal *se* with *ser*/*estar* + adjective (*Cuando se está cansado, se trabaja peor*).
- **b2-21-03, "Turning an Action Into a Noun".** Gives everyday pairs (*subir → la subida*, *llegar → la llegada*, *crecer → el crecimiento*, *cambiar → el cambio*) and the endings.
- **b2-21-04, "Needed, Enough, Urgent".** Recaps A2 Unit 27 and B2 Unit 4. New content: *hace falta que*, *basta con que*, *urge que*, with the infinitive when the subject does not change.
- **b2-21-05, "Softening What You Say".**
  - Recaps *se dice que* and *al parecer* (B2 Unit 18), *por lo visto*, *tal vez* and *seguramente* (B2 Unit 3), and *me parece que* (B1 Unit 7).
  - New content: *parece que* + indicative, *según parece*, *podría decirse que*, *tal vez convendría*, and *no parece que* + subjunctive.
- **Consolidation.** Items ex01–ex08. `ex07` is a reading item about the text (category `reading`, no `teaches`).

## The texts

**b2-19.json** ("Vargas Llosa y La ciudad y los perros", 314 words, 6 narration paragraphs). `author` is now "Mario Vargas Llosa (Perú, 1936–2025)". The summary and `source` are rewritten and `characters` is empty. Claims:
1. Vargas Llosa was a Peruvian writer. Sure (fact list).
2. Born in Arequipa in 1936. Sure.
3. Died in Lima on 13 April 2025. Sure.
4. Nobel Prize in Literature, 2010. Sure.
5. *La ciudad y los perros* is his first novel, published in 1963. Sure.
6. The novel takes place among the cadets of the Leoncio Prado military school in Lima. Sure.
7. He studied at that school as a teenager. Sure.
8. A cadet is a young person who studies at a military school. A definition, sure.
9. It won the Biblioteca Breve prize in 1962, one year before publication. Sure.
10. The prize was awarded before readers could buy the book; when the novel was published it already had the prize. Derived from 9, sure.
11. A literary prize is recognition given to a book or an author. A definition, sure.
12. It is said (*se cuenta*) that the school's authorities burned copies. Sure (fact list).
13. The sentence with *se cuenta* does not say who tells it, so the information should be read as a story that is told, not as a certain fact. This is about the wording only, and fits the fact list's "it is said".
14. This text tells no scene and quotes no sentence. True of the text.
15. If you had read only this text, you would not know the novel yet. True of the text.
16. 47 years passed between 1963 and 2010. Arithmetic, sure.
17. Another text in this course talks about another Vargas Llosa novel. True of the course.

I left out "se ha traducido". The brief names it as a grammar example, but translation is not on the fact list. Say if you want it added.

**b2-21.json** ("Céspedes y El pozo", 322 words, 6 narration paragraphs). `author` unchanged ("Augusto Céspedes (Bolivia, 1904–1997)"). `work` is now "Sangre de mestizos: El pozo (1936)". The summary and `source` are rewritten and `characters` is empty. Claims:
1. Céspedes was a Bolivian writer and journalist, 1904–1997. Sure.
2. He fought in the Chaco War between Bolivia and Paraguay, 1932–1935. Sure.
3. *Sangre de mestizos* (1936) is his book of stories about that war. Sure.
4. The book came out one year after the war ended. Arithmetic, sure.
5. A story is a short story, and a book of stories gathers several. Definition, sure.
6. "El pozo" is the book's best-known story. Sure.
7. It is about soldiers who dig, desperate with thirst, looking for water in the Chaco. Sure. No scene, quotation or ending.
8. The text itself tells no scene and quotes no sentence. True of the text.
9. *Se dice que* and *Dicen que* present information without saying who gives it. True about the language.
10. The year of the book, 1936, can be checked. Sure.

The three reading questions in each text are in English, with Spanish options and English explanations. Every answer can be found in the text as written.

## Spanish I am unsure of (unsure)

- "Cuando se está cansado, se trabaja peor": a masculine adjective after impersonal *se* is the usual form, but a woman speaking might say *cansada* (21-02 ex02). (unsure)
- 19-01 ex03: the wrong option *Se publicó las reglas nuevas* is something people say in fast speech, so it may not feel wrong to a native. (unsure)
- 19-01 screen and tip: the "careful writing agrees" claim about *se puede(n) comprar boletos*. (unsure)
- "Aquí no dejan entrar a nadie" (21-01 example). (unsure)
- "Dicen de que…" (21-01 ex03) is used as a dequeísmo wrong option. (unsure)
- 21-05 ex05: *Parece que el plan funcione bien* is wrong after affirmative *parece que*. I am fairly sure of this. (unsure)

## For the user

1. **Skills used before their screen:** none that I found. `impersonal-tercera-plural-uno` and `hedging` appear only from Unit 21. In Unit 19 I used only the A1–B1 skills the sheet lists as known.
2. **Lessons whose point is already known or only partly new.**
   - B1 Unit 6 already taught plural agreement, so 19-01 adds only coordinated nouns, the noun-first order and *poder*/*deber* + infinitive.
   - 19-04 is mostly known (*se prohíbe*, *se busca*); *Se ruega* and the property/recipe notices are the new part.
   - 21-04 teaches no frozen skill of its own; it is tagged `subjunctive-value-judgments` (A2), as the brief intended.
   - 21-02 adds only choosing among forms and *se* + *ser*/*estar* + adjective, tagged `impersonal-tercera-plural-uno` or `se-impersonal`.
3. **19-03 overlaps B2 Unit 20.** It says "use a *ser* passive or an active sentence to name the doer". B2 Unit 20's `choosing-passive-type` is a later skill, so I recap only the B1 Unit 18 *ser* passive and do not teach the choice.
4. **Accidental *se* (19-05)** is presented as new, because no earlier screen covers it. *mutuamente* and *a sí mismos* appear only in that screen's tip.
5. **Stale known-word lists.** The Unit 21 knowledge sheet still lists the old Unit 19 vocabulary (*agente*, *decreto* and so on). That vocabulary is gone now.
6. **Word counts.** The unmet-words counts are 76 for Unit 19 and 85 for Unit 21, from the script's output. I hand-counted the 76.
7. **Nothing I could not fix.** I did not touch `skills/*.json`, `tags.lock.json` or generated files by hand.