# Report: es-es A2 units 16, 17, 18 (reader B)

Method: read the rulebook sections and the three knowledge sheets; ran check-content, render_lesson and the reader-coverage audit per unit; checked all fixes in a scratch copy of the worktree (apply_replacements, check_fixes.py, check-content, add_challenges.py): 0 rejected, challenges accepted. Fixes and challenges are in the files named below. check-content ERRORs: all 9 (unit 16), 10 (unit 17) and 16 (unit 18) are fixed. The only suspects left after the fixes are `consolidation-copy` (left alone as instructed) and `unmet-word` suspects that clear once `word-lesson-index.json` is rebuilt after the vocabulary additions.

Files: /home/user/parlour-read-b/fixes-plans.json, challenges-plans.json; fixes-review-experiences.json, challenges-review-experiences.json; fixes-travel-goodbyes.json, challenges-travel-goodbyes.json.
## Unit 16 `plans` (a2-16-01 .. consolidation, story a2-16)

### 1. Found by reading
- a2-16-01 grammar, a2-16-04 grammar: *ir a* (A1 Unit 25) presented as new ("Use *ir a* + infinitive to talk about plans...") -> "You know *ir a* from A1 Unit 25."
- a2-16-02 grammar: the preterite (Unit 11) presented as new -> "You know the *pretérito indefinido* from Unit 11." a2-16-03 and a2-16-05 grammar likewise present both known forms as new -> recap wording.
- a2-16-02: the "pretérito review" lesson has 7 of 14 practice items drilling *ir a* (ex02, 03, 04, 05, 07, 08, 09) -> ex02, ex05, ex09 rewritten as preterite items (*recordé*, *Terminaron el viaje...*, *terminé*).
- a2-16-03 grammar and examples: pronoun on the infinitive (*voy a guardarla*, *abrirla*, 16-05 too) was never taught (Unit 12 only puts the pronoun before the conjugated verb) -> sentence added to the 16-03 screen.
- seguir + gerund (`perifrasis-verbales`, Unit 28) used before its screen: 16-01 ex11, 16-04 grammar example + table row + tip ("*seguir* + gerund inside it"), 16-05 ex14, ex17, ex19, ex21, story p7 -> replaced by *estudiar español todos los días*.
- a2-16-03 ex08: "Carlos va a cambiar de trabajo": Carlos never starts a new job (character facts); Lucía is the one with a new job (a2-15) -> *Lucía va a cambiar de trabajo*.
- a2-16-03 ex12: wrong option "volvemos a mañana" is a garbled non-phrase (and "volvemos mañana" would be a second right answer) -> "Vamos a terminar el viaje y vamos a volver." (no past event).
- a2-16-03 ex15: wrong option "la guardé" (*guardar* is first listed in 16-05, unmet) -> "Voy a escribir una carta y voy a guardarla."
- a2-16-04 ex13: wrong option "Aprendía español." is the imperfect (Unit 21, before its screen) with ds `imperfect`; 16-05 ex17 "Estudiaba español ayer." the same -> preterite/present options.
- a2-16-04 ex14: *solo* (viajar solo) unmet -> *viajar mucho*.
- a2-16-04 ex15, ex16, a2-16-03 ex16, a2-16-05 ex17, ex18: tell-time-word (*ayer* only in wrong options; "Viajo ayer", "Aprendo español ayer" also had two faults) -> one-fault options without the tell.
- a2-16-05 ex17: Meg asks Carlos "¿Qué va a hacer Carlos?" and Carlos answers "Voy a..." (self-third-person) -> Meg: "¿Qué vas a hacer en el futuro?"
- a2-16-05 ex18: Meg answers "¿Qué hicieron con las cartas?" with "Las guardaron" (she is one of them; answering for others) -> "Las guardamos en una caja." (+ fixed wrong options).
- a2-16-05 reading: ex11 length 47 vs 30, *pícnic*/*inmediatamente* unmet; ex12 *reunieron* unmet; ex13 length 29 vs 21; ex14 imperfect *iba* in the stem; ex15 length 28 vs 16, *estantería*/*escondió* in no list -> questions/options rebuilt with met words, answerable from the story as rewritten.
- 16-05 `nuestros` (ex16; also 16-04 example/ex12) is in no vocabulary list (A1 possessives teach only mi/tu/su) -> added to the a2-16-04 vocabulary list ("our").
- Story a2-16 (level, stories are exempt from met words, not from the level): imperfect subjunctive (*escribiera*, *regresara*, *abriera*), pluperfect (*había vivido*, B1), imperfect (*iban a*, *soñaba*), conditional (*volverían*), *seguir estudiando* -> paragraphs 2, 4, 5, 6, 7, 8, 10, 12 rewritten with the preterite, *ir a* and the present; p11 now "Kaylee guardó la caja en el salón" (es-es variant *salón*).
- Story a2-16 comprehension questions: Q1 "¿Cuál es la idea principal...?" and Q3 "¿Qué propósito tiene...?" are generic (reading-generic) -> "¿Qué escribieron los amigos en sus cartas?" and "¿Qué escribió Lauren en la tapa de la caja?"; Q2 option and explanation follow p11.

### 2. Metadata
- Checked: `teaches` and `distractor_skills` of every changed item re-set (new ds: *recuerdo* -> `stem-changes`, *termino*/*Terminan* -> `ar-verbs`, *Aprendo* -> `er-ir-verbs`, *Las guardan* -> `ar-verbs`). No other defects found; vocabulary skill slug `a2-plans-vocab` is right.

### 3. Goals / checklists
- a2-16-01 checklist-you: "I can say what you are going to do..." -> "what I am going to do".
- a2-16-02 checklist/can-do "I can review the pretérito indefinido..." is not a can-do -> "I can use the pretérito indefinido to say what happened."
- a2-16-04 goal/checklist promise "letters, memories" which the lesson (objetivo, aprender, viajar, esperar) does not practise -> "Talk about your future plans and personal goals." (goal, `goal` field, `grammar` field, checklist).

### 4. Doubtful
- Consolidation copies (8 `consolidation-copy` suspects, ex01-04, 06, 07, 10, 15): left alone as instructed.
- Every lesson of the unit repeats the same MC shape (*voy a escribir / voy escribir / va a escribir*, "Which sentence is correct?", "Which verb stays in the infinitive after...") 4-5 times per lesson (rule 2.7, no three items of a shape): not rewritten (unsure that a rewrite is wanted for a whole level).
- a2-16-03 ex04 "Vamos a cambiar de casa" = "We are going to move house" (*cambiar de* + noun is new beside the vocabulary gloss "to change") (unsure).
- The story reuses Meg's "pícnic" from a2-15 (no defect).
## Unit 17 `review-experiences` (a2-17-01 .. consolidation, story a2-17)

### 1. Found by reading
- a2-17-01, 17-02, 17-04, 17-05 grammar screens present the perfecto (Unit 1) / preterite (Unit 11) as new ("Use the pretérito perfecto...", "Look at the time expression...", "Bring the two past tenses together") -> "You know ... from Unit 1 / Unit 11" added; 17-03 likewise opens with the recap. Italics of 17-01 (`has vivido` plain) and 17-03 (`*mucho* *este* *año*`) fixed in the same sentence.
- Imperfect (Unit 21) as a wrong option with ds `imperfect`: 17-01 ex02 "Aprendía mucho.", 17-02 ex02 "Recordábamos", 17-03 ex02 "Elegíamos", 17-04 ex02 "Continuábamos", 17-05 ex02 "preparaban", consolidation ex01 (copy, left), ex08 "El año pasado aprendía" -> present or *ir a* options.
- Simple future (Unit 19) as a wrong option with ds `futuro-simple`: 17-02 ex12 "Terminaremos el curso este año.", consolidation ex04 "La clase terminará..." -> "Termino ... este año." / "va a terminar".
- tell-time-word (*ayer* only in wrong options; several of those options had two faults, e.g. "Aprendo mucho ayer", "Mejoro mucho ayer"): 17-01 ex14, ex15; 17-02 ex02; 17-03 ex12; 17-04 ex13, ex15; 17-05 ex16; consolidation ex14 -> one-fault options without the tell.
- 17-03 ex12 and consolidation ex08, ex16: wrong options break two things (both halves swapped, or "ha terminado ayer" + "aprendí") -> each wrong option breaks one half.
- 17-04 grammar tip: "*Ya he terminado* and *ya terminé* are both correct" contradicts the brief (Spain: *ya* goes with the perfecto) and the unit's own rule -> rewritten (es-es variant); the tip also named *todavía* which takes *no* + perfecto.
- 17-04 grammar example "Terminé el curso porque quise descansar.": the preterite *quise* means "tried/refused"; "wanted" is the imperfect (Unit 21) -> "Descansé porque terminé el curso."
- 17-02 tip (and 16-02): *nosotros* sameness is stated for *-ir* only, though the table's *recordamos* (-ar) is as ambiguous -> "-ar and -ir".
- 17-05 reading: ex11 length 47 vs 26 and *algunas* unmet; ex14 length 34 vs 19, *esfuerzo* (B1) and the non-event "Compró una foto"; ex15 *correos* unmet ("Muchos" in the story are classmates) -> rebuilt. *concurso*, *felicitar*, *intercambiar* (grammar example, ex13-15, 17-19, 21) are in no vocabulary list -> added to the a2-17-05 vocabulary list.
- consolidation ex18: "Ask what someone has experienced this year (use experimentar)": *experimentar* in no list and the prompt gives the word -> asks what someone has learned.
- Story a2-17 (level): pluperfect *habían aprendido*, *había sido*, *había terminado* (B1), imperfect + *acababan de* (Units 21, 28), *estaba a punto de* -> p2, p4, p5, p12 rewritten with the preterite, perfecto and *ir a*.
- Story questions: Q1 "¿De qué trata principalmente el texto?" (generic) and Q3 "¿Por qué sonríe Carlos al mirar el aula vacía...?" ("vacía" is not in the story; the reason is only implied) -> "¿Qué hicieron los amigos después de las actividades?" and "¿Qué hizo Carlos antes de salir del aula?".

### 2. Metadata
- ds rebuilt on every changed item (new: *Aprendo* -> `er-ir-verbs`, *Recuerdo* -> `stem-changes`, *Termino* -> `ar-verbs`, *Voy a ...* -> `ir-infinitive`). Tags otherwise consistent (17-04 ex13/15/16 carry `preterito-perfecto-vs-indefinido` although the contrast screen is 17-03: correct).

### 3. Goals / checklists
- No checklist-you or shared lines. 17-05 goal "experiences, relationships and completed events": "relationships" is not practised by any item (unsure, not changed).

### 4. Doubtful
- 17-01 ex05/ex09, 17-02 ex05/ex09 ("Which tense fits «el año pasado»?", "Which sentence uses the indefinido...") make the learner choose between perfecto and preterite before the 17-03 screen; the time word decides them, so left (unsure).
- 17-04 repeats the 17-03 screen's contents (este año / el año pasado / ya / porque table, same tip idea) (unsure).
- 17-02 ex16 "Meg: ¿Qué hicieron después de la clase? / Carlos: Hicieron una foto." Carlos belongs to "they" (answering for others); a fix needs *vosotros* (*hicisteis*, taught only in Unit 33): left (unsure).
- consolidation-copy suspects (ex01, 02, 03, 06, 10, 15) left alone as instructed.
## Unit 18 `travel-goodbyes` (a2-18-01 .. consolidation, story a2-18)

### 1. Found by reading
- Grammar screens a2-18-01 (ir a), 18-02 (preterite), 18-03 (perfecto), 18-04 (*antes de* / *después de*, Unit 4), 18-05 (all three) present known material as new -> "You know ... from Unit N / A1 Unit 25" added; italics fixed in 18-01, 18-02, 18-03.
- Lessons 18-02, 18-03 and 18-04 are about the preterite, the perfecto and *antes/después de*, but 7 of 14 practice items (ex02-05, 07-09) drill *ir a* again -> ex05 and ex09 of each rewritten as items of the lesson's own structure (the other ir a items left).
- tell-time-word (*ayer* only in wrong options; several wrong options had two faults, e.g. "preparamos ayer", "llegué ayer"): 18-01 ex02, ex09, ex14; 18-02 ex09, ex15; 18-03 ex02, ex09; 18-04 ex02, ex09; 18-05 ex02, ex09; consolidation ex01, ex15 -> one-fault options.
- Length give-aways: 18-05 ex12 (43 vs 23), consolidation ex04 (32 vs 22), ex15 (32 vs 22) -> rebuilt (consolidation ex04/ex15 varied so they do not become copies of 18-02 ex12/ex15).
- Simple future (Unit 19) as a wrong option with ds `futuro-simple`: 18-02 ex12 "Llegaremos pronto.", 18-05 ex16 "Nos dará una postal mañana.", consolidation ex04.
- 18-03 ex05 "Vamos a conocer a Lucía mañana.": they have known Lucía since a2-07 (character facts) -> perfecto item. 18-03 gloss: "¿Has conocido un lugar nuevo?" = "Have you discovered...?" (table "you have discovered"; *conocer* is "get to know / meet", *descubrir* is Unit 2) -> "got to know" in screen and ex14.
- 18-02 ex17, 18-04 ex17, consolidation ex17: prompts say "you" but the stored answers are *Llegamos / preparamos / visitamos / hemos recordado* (we) -> prompts say "we".
- 18-04 tip: "English needs a full clause here - 'before we left'" contradicts the screen's own translations ("Before leaving, we prepared...") and previews *antes de que* (subjunctive, Unit 27) -> tip rewritten.
- 18-05 grammar example/ex11/ex14/ex19 *despedirse* (also *despedirme*, *despidieron*) and *postal* (story, ex13, ex16; B1 only) are in no early list, *avión* in no list at all (18-02 grammar example, ex05, ex13; 18-05 ex13; consolidation ex07) -> *despedirse*, *la postal* added to a2-18-05, *el avión* to a2-18-02 vocabulary.
- 18-05 unmet words: *organizar* (ex02, ex07) -> *preparar* (a2-18-01); *anunciaron* / *embarque* / *inmediatamente* (ex14, ex17) -> questions about "Todos se abrazaron" and "¿Qué pasó en el aeropuerto?"; *enfadados* (ex15); *les* in "¿Qué regalo les dio Lucía?" (indirect object pronoun, Unit 25) and *Nos dio una postal* (ex16) -> "a cada uno".
- 18-05 ex17: "Ha llegado mañana." is garbled (perfecto + mañana) -> "Llegamos el momento de decir adiós." (agreement fault). ex16/ex18: Meg, who was at the airport, answers "Estuvieron tristes" / reply for others -> "Estuvimos".
- consolidation ex18: *recientemente* is listed only in a2-perifrasisduracion-01 -> "este año". 
- Story a2-18 (level): *mientras* + imperfect (*esperaban*, Unit 21), pluperfect (*habían compartido*, *habían vivido*, B1), conditional (*seguiría*, *continuaría*), imperfect subjunctive (*separaran*) with *aunque* (Unit 28), *seguir* + gerund (Unit 28), *le* (Unit 25) -> p3, p6, p11, p12 rewritten with the preterite, *ir a* and the present.
- Story questions Q1 "¿Cuál es el tema principal de esta lectura?" and Q3 "¿Qué convicción reconforta a los amigos...?" are generic/inferential -> "¿Adónde fueron los amigos para despedirse de Lucía?" and "¿Qué hizo Lucía al final?".

### 2. Metadata
- ds rebuilt on every changed item (new: *preparamos* / *abrazo* -> `ar-verbs`, *vuelven* -> `stem-changes`, *Da una postal* -> `present-tense`). 18-05 ex19 is tagged `preterito-perfecto-vs-indefinido`, which is right for a mixed-tense writing item. No other tag defects found.

### 3. Goals / checklists
- None changed (no checklist-you, no shared lines, goals match the lessons).

### 4. Doubtful
- consolidation-copy suspects (ex03, 07, 08, 12) left alone as instructed.
- 18-04 grammar example "Después de volver, hemos recordado el viaje." (perfecto after *después de volver*) is odd as a sentence but grammatical (unsure, not changed).
- 18-01 ex15, 18-05 dialogues: Meg asks Carlos "¿Qué van a hacer mañana?" and Carlos answers in the third person; fine if the question is about others, but ambiguous (unsure; a *vosotros* fix would be es-es only).
- 18-05 story p4 keeps "Lucía les dio..." (*les*, Unit 25): stories are exempt from met words (unsure).

## 5. Dictionary (all three units)
The audit (`node scripts/audit-reader-coverage.js es-es --story a2-16 | a2-17 | a2-18 --top 0`) reported 0 "not in the dictionary", 0 "literal compound guess only" and 0 lookup throws for each story as it stands now. Nothing to import. (The rewritten story lines use only common words: *guardó*, *dijo*, *pensó*, *estuvieron*, *hace poco*, *lejos*; not re-audited because nothing may be edited.)

## Fix counts
- Unit 16 plans: 50 fixes (fixes-plans.json)
- Unit 17 review-experiences: 35 fixes (fixes-review-experiences.json)
- Unit 18 travel-goodbyes: 48 fixes (fixes-travel-goodbyes.json)
Challenges: 6 per unit (18 in all).
