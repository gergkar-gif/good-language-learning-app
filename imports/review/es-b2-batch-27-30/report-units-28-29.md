# Report: B2 Units 28 and 29 (es-latam), worktree /home/user/parlour-read-a

The harness refused the report file, so this reply is the report. Nothing is committed. The files are:
- `/home/user/parlour-read-a/challenges-discourse-markers-structuring-sequencing.json`
- `/home/user/parlour-read-a/challenges-discourse-markers-reformulation-precision.json`
- `/home/user/parlour-read-a/.scratch/` holds my generator scripts and is untracked. Delete it before committing.

Both units are done and the checks are clean apart from the suspects listed under each unit.

**Changes made to every lesson in both units.**
- All screens, goals and checklists are in English.
- Each lesson got a `goal` string and section, an `srs` section and a `checklist`. The checklist lines are the goal lines, and each challenge's `canDo` is the first checklist line.
- Vocabulary lists were replaced. The literary words (*preámbulo, dilucidar, soslayar* and the rest) are gone.
- All items were rewritten: English stems, no `hint` or `english` on multiple choice, whole-word blanks, `teaches` and `distractor_skills` set.
- Each lesson has six items and the consolidation has eight, ending with one reading item from the text.

## Unit 28: discourse-markers-structuring-sequencing

- **b2-28-01 "Putting Ideas in Order".**
  - Recaps *primero, luego, después, por último* (A1), *a continuación* (B1 Unit 24) and *por un lado* (B1 Unit 23).
  - New: *en primer lugar / en segundo lugar / en tercer lugar*.
  - Items ex01–ex06 use `ordering-markers`, except matching, which is vocabulary, and ex06, which is reading.
- **b2-28-02 "Adding a Side Remark".**
  - Teaches *por cierto, a propósito (de), dicho sea de paso, volviendo a lo que decíamos* and recaps *además* (A2 Unit 28).
  - Items use `marcadores-digresion`, with `distractor_skills` on the ordering and closing markers.
- **b2-28-03 "Moving On and Picking Up a Topic".**
  - Teaches *pues bien, en cuanto a, por lo que se refiere a* and recaps *en cuanto* (A2 Unit 27).
  - Items carry the unit vocabulary skill.
  - Vocabulary adds *oprimido* and *el exilio*, used by 28-03.ex06 and 28-05.ex06.
- **b2-28-04 "Two Sides of a Point".**
  - Teaches *por una parte … por otra* and recaps *mientras que* (B1 Unit 12), *por un lado* (B1 Unit 23), *sin embargo* (A2 Unit 28) and *mientras* (A2 Unit 13).
  - I removed the old false rule that *por un lado … por otra parte* must not be mixed.
- **b2-28-05 "Closing a Text".**
  - Teaches *en definitiva, en suma* and recaps *en resumen* (B1 Unit 13) and *en conclusión* (B1 Unit 17).
  - Items use `argument-markers`.
- **b2-28-consolidation.** The goals and checklist are in English, the text line names Roa Bastos, and there are 8 new items.

**Text** (`b2-28.json`, "Roa Bastos y Hijo de hombre", 262 words, 6 narration paragraphs, no asterisks). Every claim comes from your fact list.
- Roa Bastos was a Paraguayan writer. Sure.
- He was born in 1917 and died in 2005. Sure.
- He lived many years in exile. Sure.
- "Exile means living outside one's own country" is a definition, not a fact about him. Sure.
- *Hijo de hombre* was published in 1960. Sure.
- It is his first novel. Sure.
- "Whoever wants to read his novels from the first should start with it" follows from "first novel". Fairly sure.
- The novel is about the struggle between the rulers of Paraguay and its oppressed people. Sure.
- The struggle runs from 1912 to 1936. Sure.
- One sentence names the text's own three steps (author, novel, theme). Sure.
- One reading statement says that whoever knows these facts knows the country, the years and the two sides before opening the book. Sure.
- There are no scenes, names, quotations or prizes.

**Checks.**

| Check | Before | After |
|---|---|---|
| check-content errors | 6 | 0 |
| check-content suspects | 18 | 3 |
| unmet words | 103 | 0 |

- Unmet words include the challenge targets. I tested them by temporarily merging both challenge files into `curriculum/challenges.json`, then restored it byte for byte.
- `check_unit_refs --labels --bare` is clean.

**Remaining suspects, accepted.**
- `tell-opener` on 28-03.ex01 and consolidation.ex05. The item tests the opening marker *pues bien*, so the right option has to open differently from the wrong ones.
- `answers-alternatives` on 28-05.ex03. *definitiva, resumen, conclusión* and *suma* all complete the sentence in real Spanish, and the English cannot pin just one.

## Unit 29: discourse-markers-reformulation-precision

- **b2-29-01 "Saying It Another Way".**
  - Recaps *es decir* and *o sea* from B1 Unit 27, found on its screen b1-27-04.
  - New: *en otras palabras, dicho de otro modo*.
  - This is the lesson that teaches `reformulation-markers`.
- **b2-29-02 "Correcting Yourself".** Teaches *mejor dicho* and recaps *más bien* (B2 Unit 1) and *es decir* (B1 Unit 27).
- **b2-29-03 "Brushing Doubts Aside".**
  - Teaches *de todos modos, de todas formas, en cualquier caso* and recaps *sin embargo* (A2 Unit 28).
  - I treated the three markers as new: *de todas formas* appears only as an example sentence in A2 Unit 22.
- **b2-29-04 "Condensing What You Said".**
  - Recaps *en resumen* and *en definitiva* (B2 Unit 28).
  - New: *en pocas palabras, resumiendo*.
  - Consolidation.ex05 tests *en definitiva* (`argument-markers`).
- **b2-29-05 "Giving Examples".** Recaps *por ejemplo* (A2 Unit 30). New: *así, como, en concreto*.
- **b2-29-consolidation.** There are 8 new items, and the text line names Machado de Assis.

**Text** (`b2-29.json`, "Dom Casmurro", 439 words, 6 paragraphs, nothing in quotation marks, no asterisks).
- **Chapters used:** I, II and III of the Gutenberg text.
  - Chapter I: the train, the young man's verses, the nickname, and what *casmurro* and *Dom* mean.
  - Chapter II: the house copied from the Matacavalos house, the failed attempt to recover youth, the decision to write.
  - Chapter III: the November 1857 scene behind the door, with José Dias, the narrator's mother, and the ages of Bentinho and Capitu.
- **Marker lines:** *es decir, o sea, mejor dicho, en otras palabras, dicho de otro modo, por ejemplo, más bien, en cualquier caso*.
- **Source order and wording:** kept in the source's order, and retold in my own words, not translated.
- **Old text:** it contradicted the source and invented the rest of the novel (Escobar, Ezequiel, the seminary friendship, the ending). I replaced all of it.
- **Metadata:** `author`, `work` and `source` are as you ordered.
- **Departures from the source, kept deliberately:**
  - Two of the mother's utterances ("em todo caso, vae sendo tempo" and "é promessa") are merged into one sentence.
  - The busts that speak are told as "le pareció que los bustos le decían", because the source is figurative.
- **Questions:** the comprehension questions are in English with Spanish options.

**Checks.**

| Check | Before | After |
|---|---|---|
| check-content errors | 8 | 0 |
| check-content suspects | 21 | 1 |
| unmet words | 98 | 0 |

- `check_unit_refs --labels --bare` is clean.
- `validate-content --changed` passes, and the renders show no `!!`.
- **Remaining suspect, accepted:** `answers-alternatives` on 29-03.ex02. *en cualquier caso* and *en todo caso* are both correct Spanish, so I accept both rather than mark a right answer wrong. *Todo* is not taught.

## Unsure Spanish
- (unsure) 29-05 screen: *Así,* plus a clause as an example introducer ("Hay muchas formas de ahorrar. Así, puedes comprar menos y cocinar en casa."). It is standard in written Spanish but less common in speech.
- (unsure) 28-02 screen: *dicho sea de paso* is described as usually sitting between commas inside a sentence.
- (unsure) Wrong options built from other markers (28-05.ex05, 29-03.ex05, 29-05.ex01) are wrong by function, not by grammar. A native would reject them in context, but they are not ungrammatical.
- (unsure) 28-01.ex02 option "En el primer lugar, hablaré del precio.": acceptable Spanish in other senses, wrong only as the marker.

## For the user
- **Skill order:** I found no skill used before its screen. `reformulation-markers` is taught on b2-29-01 and used on 29-02 onwards. `ordering-markers`, `argument-markers` and `marcadores-digresion` are used only after their screens.
- **`ordering-markers` and *por un lado*:**
  - `ordering-markers` (A2 Unit 28) claims *por un lado*, but the A2 Unit 28 screen shows only *sin embargo, aunque, por lo tanto, además*.
  - B1 Unit 24's screen also credits A2 Unit 28 for *por un lado*.
  - The sheet first lists *por un lado* in B1 Unit 23 vocabulary, so my recaps say B1 Unit 23 (`check_unit_refs` agrees).
- **`reformulation-markers` scope:** I tagged every grammar-choice item in 29-02 to 29-05 with it. Its aliases cover all five lessons, but its title names only *es decir* and *o sea*.
- **Conversation scenarios:** `conversation-scenarios.json` mentions *transición* and *balance* in text only, not in `requiredLemmas`. `test-scenario-learner-path.js` passes.
- **Hidden-track skills:** I used nothing from a hidden track.
- **Builder side effects:** the builders modified `content/*/decks/decks.json`, the story manifests, `curriculum.json` and `indexes/word-lesson-index.json`. This is expected.