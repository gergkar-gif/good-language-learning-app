# Report: B2 Unit 13 `relatives-unknown-antecedents` and Unit 14 `universal-indefinite-relatives` (es-latam), reader B

Nothing is committed. The full report went to the final reply because the repo file is only a short stub (`/home/user/parlour-read-b/report-relatives-unknown-antecedents.md`). Every screen, item, vocabulary list, lesson title, goal, checklist and unit text of the two units was rewritten, and each lesson's exercise ids and sections are unchanged. Every screen is now in English. Every question stem is in English. No multiple-choice item has `hint` or `english`.

## Check counts (final run, after the last edit, including the challenge targets)

| Check | Unit 13 before | Unit 13 after | Unit 14 before | Unit 14 after |
|---|---|---|---|---|
| `check-content` errors | 8 | 0 | 10 | 0 |
| `check-content` suspects | 16 | 0 | 20 | 0 |
| `unmet-words` hits | about 108 (hand count) | 0 | 96 | 0 |

- **Other checks:** `check_unit_refs --labels --bare` reports 0 and `render_lesson` shows 0 `!!` in both units. `validate-content --changed` passes (es-latam 47 passed, 0 failed).
- **Manifest:** `build-manifest.py` also regenerated `es-es/decks/decks.json`, `es-es/stories/manifest.json`, `es-latam/curriculum/curriculum.json`, `es-latam/decks/decks.json` and `es-latam/stories/manifest.json` as expected, and `build_word_lesson_index.py` rewrote `es-latam/indexes/word-lesson-index.json`.
- **Challenge files:** `/home/user/parlour-read-b/challenges-relatives-unknown-antecedents.json` and `/home/user/parlour-read-b/challenges-universal-indefinite-relatives.json` hold six challenges each. I did not merge them into `curriculum/challenges.json`. In each, `canDo` is the lesson's first checklist line.

## Unit 13

All screen rules are tagged `relativas-subjuntivo` and vocabulary is `b2-relatives-unknown-antecedents-vocab`. Every lesson is rewritten the same way: new vocabulary list (4 words each, all used in the matching item), new `srs` + `checklist` sections (lines = goal lines), ex01–ex06 rewritten. The consolidation keeps its checklist and has no `srs`.

- **b2-13-01 "Looking for Something That May Not Exist":** the screen teaches `relativas-subjuntivo` fully.
  - *Busco un apartamento que tenga balcón* against *Tengo un apartamento que tiene balcón*, and the negative antecedent *No hay nadie que sepa la respuesta*.
  - Recaps *que* (B1 Unit 5), the subjunctive (A2 Unit 27), *nadie* / *ningún* (A2 Unit 31) and the personal *a* (A1 Unit 24).
  - Vocabulary: *amplio, ascensor, mascota, estacionamiento*.
  - Items ex01–ex06. ex02 is a negative sentence, so only the subjunctive fits. ex03 has `distractor_skills` on *aceptara*. ex05 is a dialogue whose right answer is indicative.
- **b2-13-02 "Nobody, Nothing, No Such Thing":** *nadie / nada / ningún / ninguno* + `que` + subjunctive, plus questions (*¿Hay alguien que sepa…?* against *Hay alguien que sabe*). The tip says a negative verb alone does not force the subjunctive (*No me gusta la casa que compraste*).
  - Vocabulary: *plomero, arreglar, fuga, herramienta*.
  - ex03 has a wrong option with the missing `no`. ex05 has a `preterite-irregular-stems` distractor.
- **b2-13-03 "Real or Only Wanted?":** recaps 13-01 and adds only two things.
  - The article is a clue (*el / la* against *un / una*), not a rule.
  - The past: imperfect subjunctive (B1 Unit 4) against imperfect indicative.
  - Vocabulary: *cargador, enchufe, servir, pantalla*. The `preterito-indefinido` distractor is on ex03.
- **b2-13-04 "A Person to Talk To":** preposition + relative + subjunctive.
  - Recaps *quien* (B1 Unit 5) and *el que* (B1 Unit 20).
  - Spanish never strands the preposition (*una persona con la que pueda hablar*). *Donde* replaces *en el que* for places.
  - Vocabulary: *confiar en, apoyo, compartir, consejo*.
  - ex03's distractor *de la que* carries `relativas-preposicion-el-que`; ex05's *confiaré* carries `futuro-simple`.
- **b2-13-05 "Job Ads and Requirements":** plain lesson on *Buscamos a alguien que hable inglés*. It covers several requirements joined by *y*, the job seeker's side (*Quiero un trabajo que pague bien*) and the indicative for the person already hired.
  - The old generalising-relative content (*cualquiera que*, *todo aquel que*) is gone; it belongs to Unit 14.
  - Items are now tagged `relativas-subjuntivo` (they were `relative-clauses`).
  - Vocabulary: *vacante, sueldo, turno, currículum*.
- **b2-13-consolidation:** 8 new items (ex08 stays category `writing`), no copies of lesson items. It has an English goal and a 4-line checklist whose last line names the text: "I can read a short text about García Márquez and Cien años de soledad." I changed it from the usual wording because the standard line already exists in b2-03-consolidation (`checklist-shared`).

### Text (`stories/classics/b2/b2-13.json`)
It is a new original text, "García Márquez y Cien años de soledad": 6 paragraphs, 321 words. It has an original summary and source line, and no characters. It has 3 English comprehension questions with Spanish options, and every answer is in the text. Claims, one per line:

- García Márquez was a Colombian writer. (certain, from your list)
- He was born in 1927 and died in 2014. (certain)
- He received the Nobel Prize in Literature in 1982. (certain)
- *Cien años de soledad* was published in 1967; it is one of his best-known novels. (certain; "one of his best-known" follows from your wording "one of the best-known novels of magical realism")
- It tells the story of several generations of the Buendía family. (certain)
- A generation is the group of family members of roughly the same age: grandparents, parents, children. (definition)
- The family lives in Macondo, a town the author invented; the reader knows Macondo only through the author's words. (certain for "invented"; the second half follows from it)
- The novel is one of the best-known of magical realism. (certain)
- In magical realism extraordinary things are told in the same way as everyday things, not as something strange but as one more part of life. (certain, paraphrase of your wording)
- *Quien busque…encontrará un buen ejemplo*: a recommendation, not a fact about readers. (opinion, hedged)
- For someone who does not know magical realism the novel may be a good introduction. (opinion, "puede ser")
- Because it follows one family over several generations, it is worth reading attentively and unhurriedly; whoever is patient can follow each person and see time pass from one generation to the next. (advice; follows from "several generations")
- This text contains no scene and no sentence from the novel; "we talk about the book but do not retell it". (true of this text)
- The novel was published fifteen years before the Nobel Prize (1967 and 1982). (arithmetic, certain)
- Whoever wants more about García Márquez can read the course's other texts on his work. (true: B2 Units 3 and 7)

Grammar: *Quien busque…que cuente*, *Para quien no conozca*, *quien quiera…tiene que*, *antes de que…recibiera*, *ninguna escena…*. The text avoids the other books' points, the first sentence, and *como si* and *cualquiera que*.

## Unit 14

Rewrote the rest of the lesson files the same way as Unit 13.

- **b2-14-01 "Whoever, Whichever, Wherever":** teaches `relativas-universales-quiera`. It covers *cualquiera que* / *quienquiera que* / *dondequiera que* + subjunctive and *cualquiera* against *cualquier* + noun. It recaps *pase lo que pase* (B2 Unit 8) and `que` + subjunctive (B2 Unit 13).
  - Vocabulary: *timbre, recado, molestar, atender*.
  - ex03's wrong options are *cualquiera que es* and *cualquier que*.
- **b2-14-02 "However Much, However Hard":** recaps *por más que* / *por mucho que* / *por muy… que* (B2 Unit 8) and adds only *por más / por mucho + noun + que* and its agreement, plus the contrast "how much?" (*por más que*) against "which one?" (*cualquiera que*). Tag `concesivas-por-mas-que`.
  - Vocabulary: *prisa, cansancio, ahorrar, gastar*.
  - ex06 is *Cualquiera que sea el precio…*, tagged `relativas-universales-quiera`.
- **b2-14-03 "Whoever It Is, Whatever It Is":** recaps *pase lo que pase* and *diga lo que diga* (B2 Unit 8) and adds *sea quien sea*, *sea cual sea*, *sean cuales sean* and *llame quien llame*. Tag `reduplicated-subjunctive`.
  - Vocabulary: *chisme, criticar, opinar, apoyar*.
  - ex02 blanks the relative word *quien*, not the verb.
- **b2-14-04 "Everything That, Everyone Who":** *todo lo que*, *todos los que*, *todo aquel que* and *cuanto(s)*, indicative for a real group and subjunctive for an open one. Recaps *lo que* (B1 Unit 20), `que` + subjunctive (B2 Unit 13) and *cuanto más… más* (B1 Unit 2).
  - Tags by what a wrong answer shows: mood `relativas-subjuntivo` (ex02–04, ex06), pronoun choice `relative-clauses` (ex05).
  - Vocabulary: *repartir, aprovechar, invitado, regalar*.
  - The *vosotros* error `os` in the old screen is gone.
- **b2-14-05 "Formal Written Spanish":** plain lesson on notices, rules and official letters: *Todo aquel que desee participar deberá…*, *Se ruega a…*, *Estimados vecinos:* and *Atentamente,*. It shows everyday against formal in a table. Tag `formal-register`.
  - Vocabulary: *formulario, estimado, atentamente, rogar*.
  - The dialogue wrong options are one with an informal opening and closing, and one with a formal opening but informal closing.
- **b2-14-consolidation:** 8 new items. The first checklist line is "I can say that it makes no difference who, which or where, in several ways", because the usual line clashed with b2-14-01 (`checklist-shared`). The last line names Rivera and *La vorágine*.

### Text (`stories/classics/b2/b2-14.json`)
It is a new original text, "Rivera y La vorágine": 6 paragraphs, 330 words. Characters are Arturo Cova and Alicia only. It has 3 English comprehension questions and every answer is in the text. Claims, one per line:

- Rivera was a Colombian writer, born 1888, died 1928 in New York. (certain, from your list; no mention of how he died)
- *La vorágine* was published in 1924. (certain)
- The reader will not find a summary of everything that happens; the text presents the novel and does not retell it. (true of this text)
- The narrator is, almost all the time, Arturo Cova, a poet. (certain, "mostly")
- Cova flees Bogotá with Alicia, goes first to the plains of Casanare, then into the jungle. (certain)
- All this happens in the time of the rubber boom; a boom is a moment when an activity grows a lot. (certain, plus a definition)
- The novel draws on real crimes against the rubber workers in the Putumayo region. (certain)
- It is a novel, not a report; many readers learned of those crimes through it; it is a case where a work of fiction made a real problem known to many readers. (certain, restates your wording)
- Whoever opens the book follows a poet who leaves Bogotá, crosses the plains and reaches the jungle. (certain)
- Anyone who wants to understand the background can look for information on rubber and the Putumayo. (advice)
- Today's reader may wonder which part is fiction and which is reality; what we do know is that the author used crimes that really happened as a base. (certain for the second half; the first is a hedged remark)
- The novel's journey is the same wherever it is read: Bogotá, the plains, the jungle. (certain)
- Between the novel's publication (1924) and the author's death (1928) only four years passed. (arithmetic, certain)
- Whatever each reader thinks, the data are the same: a 1924 novel, a poet fleeing Bogotá, real crimes as a base. (restatement)

Grammar: *quien busque…no lo va a encontrar*, *Todo aquel que…*, *Cualquiera que quiera…*, *Quienquiera que lea…*, *dondequiera que se lea*, *Cualquiera que sea…*, *antes de que* is not used.

## Spanish lines I am unsure of (unsure)
- (unsure) 13-04 ex03 option "Necesito una persona con la que puedo hablar": a native might accept it when the person is already known. The stem says "I need…", which pins the subjunctive.
- (unsure) 13-02 ex05 option "No conozco a ninguno que puede venir hoy" is used as wrong in 13-02 ex03; colloquial speech sometimes uses the indicative after a negative.
- (unsure) 14-04 ex02 "Invita a cuantos amigos __" accepts only *quieras*. *quieres* is rare there but not impossible.
- (unsure) 14-02 ex03 wrong option "Por más dinero que ahorras…": generic present could be read as indicative; the English "however much you save" pins the open reading.
- (unsure) 14-05 ex05 uses « » quotation marks inside answer options.
- (unsure) "Piden a alguien que hablara…" in 13-05 ex05 is wrong for a present frame, but past frames use it.
- (unsure) Present-day claims: none (no offices, laws or figures).

## For the user
- **Skills used before their screen:** none of the unit's own. `relativas-subjuntivo` is met in 13-01. Unit 14 relies on it and on `concesivas-por-mas-que` and `reduplicated-subjunctive` (B2 Unit 8), `relative-clauses` (B1 Unit 5) and `relativas-preposicion-el-que` (B1 Unit 20). All are met earlier.
- **Distractor skills used:** `imperfect-subjunctive-forms`, `preterito-indefinido`, `preterite-irregular-stems`, `futuro-simple`, `imperfect`, `present-tense`, `relativas-preposicion-el-que`. All are known by the unit they appear in, and the validator accepts them.
- **A lesson whose whole point is a later or hidden skill:** none. The sheet lists nothing relevant as hidden or later.
- **Skill assignment:** b2-13-05 was tagged `relative-clauses` and is now `relativas-subjuntivo`. b2-14-02/03 keep their earlier-unit tags. b2-14-04 is split by what the wrong answer shows, as the brief asked. I made no skill-list change.
- **Knowledge sheet for Unit 14:** it still lists the old Unit 13 words (*acreditar, baremo…*). Those are gone from the Unit 13 lists, so Unit 14's recap relies on the new ones.
- **Not done:**
  - I did not run `audit-reader-coverage.js`, so Reader-gap words in the two texts are not reported.
  - I did not touch `lock_tags.py` because the units are not read and locked.
  - Challenge files are not merged into `curriculum/challenges.json`.
  - The challenge scenarios invent no facts about Carlos or Meg beyond the brief.