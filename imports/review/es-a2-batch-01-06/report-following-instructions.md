# Review report: es-es A2 Units 4, 5, 6 (reader B)

## UNIT 4 following-instructions (a2-04-01..05, consolidation, story a2-04)

Fixes: 36 in fixes-following-instructions.json; challenges: 6 in challenges-following-instructions.json. Fixes were run through check_fixes.py (0 rejected, 5 auto, 31 review). The vocabulary adds are what clear the unmet-word suspects (the word index must be rebuilt after applying them).

### 1. Found by reading
- a2.04.01.ex13 / ex15, a2.04.02.ex15 (check-content ERROR tell-time-word, and preterites *lavamos*, *preparamos*, *servimos* before a2-11-01): wrong options "...lavamos las manos ayer.", "Sí, preparamos los ingredientes ayer.", "Sí, servimos la comida ayer." -> one-fault options ("Antes de empezamos, hemos lavado las manos.", "Sí, hemos preparados los ingredientes.", "Sí, hemos servido la comida antes de cocinar.").
- a2.04.01.ex12, a2.04.02.ex12, a2.04.consolidation.ex01: preterite wrong options *cociné*, *cociné*, *empecé* (a2-11-01 forms) -> present *cocino*, *cocino*, *empiezo*.
- a2.04.05.ex11 / ex12 / ex15 (ERROR length-giveaway): shortened the right options ("Una clase de cocina.", "Se lavan las manos.", "Hacen una foto."); ex11 also drops *tradicional* (b1) and the stem *se han apuntado* (apuntarse is in no list) -> "¿Qué clase tienen los amigos?"; ex12 *marchan* -> "Salen de la clase."; ex14 *inmediatamente*, *otra* -> "Se van a Hanói en tren.", "Preparan la salsa."; ex15 *otra* -> "Preparan el arroz."
- a2.04.03.ex02 "Which sentence puts the first action before the second?": nothing says which action is first, so "Después de cocinar, hemos cortado las verduras." is also a valid order -> "You cut the vegetables, then you cook. Which sentence says this?"
- a2.04.04.ex02 ("the first cooking step") and ex05 ("the second action came later"): same, the prompt pins no order, and "Antes de cocinar, hemos servido la comida." is a valid sentence for another order -> prompts "You wash your hands, then you cook." / "You cook, then you serve the food."
- a2.04.03.ex15 is the same dialogue as ex14 (same prompt, same three options) -> new prompt "¿Qué han hecho después de lavar las manos?".
- a2.04.03.ex05 option *desde* (A2 Unit 7) -> *sin*.
- a2.04.consolidation.ex18: "Ask what someone has done..." does not pin *tú* -> "Ask a friend (use tú) ...".
- Grammar a2-04-01-gr tip: "Spanish *antes de* is always followed by the bare infinitive, no matter who is doing the action" is false (different subject: *antes de que* + subjunctive) and "Unlike English" is wrong (English says "before starting") -> rewritten. Text sentence "the perfect form shows the completed action, while antes de introduces the action that happened first" is muddled (and says "first" for what is the later action) -> rewritten with a recap (see 3).
- Grammar a2-04-02-gr tip: "Treat *de* before *antes* or *después*..." (the *de* comes after them) -> rewritten.
- Story a2-04: *Nunca había preparado* is the pluscuamperfecto (B1 family of this unit's skill); *cuando vuelva* is a present subjunctive (A2 Unit 27); *Al día siguiente ... se han apuntado* puts the perfecto with a past time (Spain: *Hoy*). Comprehension questions: Q1 "¿De qué trata el texto?" (reading-generic) -> "¿Qué hacen los amigos en la escuela de cocina?" with matching options; Q2's right answer "Cortar las verduras..." was the only infinitive among finite verbs -> "Corta..."; Q3 distractors *puso*, *perdió* are preterites -> *da*, *pierde*.
- Vocabulary: *verduras* in no list (consolidation.ex08; first used a2-04-01) -> added to a2-04-01-voc; *probar* (04-02 ex02/09/13/14) and *servir* (04-02 ex15) added to a2-04-02-voc; *marcharse* (used by the 04-05 example, ex07, ex09, ex18, ex19, ex20 and the consolidation) added to a2-04-05-voc.

### 2. Metadata
- No missing `teaches`/`category`, no `distractor_skills` needed; reading items carry none (allowed). Vocabulary tag `a2-following-instructions-vocab` is the right slug.
- a2.04.05.ex02 (unsure) tagged vocabulary, but it asks what the students did before the class, which the learner cannot know before the story; all three options are plausible and only world knowledge picks one. Left alone.

### 3. Goals / checklists
- a2-04-01 and a2-04-02 checklist/canDo: "I can say what *you* have done..." -> "what I have done" (both lesson files; the challenges use the new wording).
- Recap: antes de / después de + infinitive was taught in A1 Unit 7 (a1-reflexive-05, "You know ... from Unit 7") yet a2-04-01 and a2-04-02 present them as new. The rewritten texts open "You know *antes de* from A1 Unit 7 and the *pretérito perfecto* from Unit 1" / "You know *después de* from A1 Unit 7".
- The same three-row table (antes de / después de / he-hemos + participio) is repeated unchanged on all five grammar screens, and the screens of a2-04-03, -04 and -05 restate each other (repeated screens). Not rewritten (needs new teaching content).

### 4. Doubtful
- (unsure) Unit-wide: "He lavado las manos", "Hemos lavado las manos", "Han lavado las manos" (a2-04-01 screen, ex02/03/08/09/13/14, a2-04-02..04 and consolidation, dictation, writing) is unnatural Spanish: a native says *Me he lavado las manos* / *Nos hemos lavado las manos* (the unit even lists *lavarse*). The reflexive perfecto is never taught before a2-04-05 (ex16 "Nos hemos lavado", story, example "se han lavado"). Options: change the sentences to *He lavado las verduras* (no reflexive, natural) or add a reflexive-perfecto note to a2-04-01. Not written as fixes (about 40 items incl. sentence-builder tiles); reviewer decision.
- (unsure) Tip a2-04-04-gr "the action barely changes, only your viewpoint on it" is vague; left.
- (unsure) a2.04.02.ex15 fix depends on `servir` being added to the a2-04-02 list (check_fixes sees *servido* as an example phrase either way).
- *hacer una foto* (a2-04-05 example, ex07, ex19, ex20, story, consolidation) is Spain-only; es-latam says *sacar/tomar una foto*. Left (course variant, not mirrored).
- Consolidation copies (consolidation-copy suspects) left as instructed.

### 5. Dictionary
(none: audit-reader-coverage for story a2-04 reports 0 not in the dictionary, 0 literal compound guesses)


## UNIT 5 giving-reasons-opinions (a2-05-01..05, consolidation, story a2-05)

Fixes: 24 in fixes-giving-reasons-opinions.json; challenges: 6 in challenges-giving-reasons-opinions.json. check_fixes.py: 0 rejected.

### 1. Found by reading
- a2.05.05.ex11-ex15 (reading, 5 of 5): none of the questions can be answered from the story. They ask why the excursion changes (rain), about a cancelled trip, a new route, an airport, a teacher arriving late, lost tickets; the story a2-05 is a good-weather walk to a viewpoint with no rain and no change of plan. Also check-content ERROR length-giveaway on ex14 (35 vs 18) and suspects *perdido*, *inmediatamente*, *cancelado*, *aeropuerto*, *aburrida*, *imposible*. Replaced with five questions on what the story says ("¿Qué hacen después del desayuno?" / "¿Cómo es el camino?" / "¿Qué pueden ver desde arriba?" / "¿Qué hace Meg?" / "¿Quién habla de la región?"), with met words only.
- a2.05.03.ex02 suspect unmet *mojar* (the list has *mojarse*): option "Hemos vuelto porque nos hemos mojar." -> "Hemos vuelto porque mojarse."
- a2.05.03.ex09: options are pairs of sentences; the wrong pairs have 2-3 faults each (por eso without comma plus reversed logic; infinitive plus missing connector...). Rewritten as "It has rained, so we have changed the route. Which sentence says this?" with one fault per wrong option.
- a2.05.03.ex13: the "correct" sentence "Ha llovido, por eso hemos vuelto porque nos hemos mojado." is a muddled chain, and the third option has four faults (*Ha llover*, *hemos volver*, *mojamos*, ...). Replaced with a correct sentence using both connectors and one-fault wrong options.
- a2.05.03.ex16 (suspect option-language "both mean because"): the meta item sits in the Dialogue group and its options mix Spanish and English. Reworded: "In «Hemos vuelto porque ha llovido», what does «porque» introduce?" / a reason, a consequence, a question.
- a2.05.02.ex10: English inside a Spanish stem: "¿Qué significa «el tiempo» in this context?" -> "¿Qué significa «el tiempo» en «Ha cambiado el tiempo»?"
- a2.05.consolidation.ex18: "Ask why someone has returned" / "Ask what someone thinks..." do not pin *tú*; "Say that it has been fun." does not ask for *Pienso que* (stored answer "Pienso que ha sido divertido.") -> prompts reworded.
- Grammar a2-05-05-gr tip brings in *para que* (a subjunctive connector, Unit 27) -> replaced with a tip about telling the story in order.
- Story a2-05: *nunca había visto* is the pluscuamperfecto (B1) -> *nunca ha visto*. Last line "las mejores experiencias suelen ser las que no estaban planeadas" uses *mejores* (comparative, Unit 6) and an imperfect (Unit 21) -> "una excursión sin plan puede ser una experiencia muy buena" (unsure, the wording is mine); comprehension Q3 and its explanation changed with it. Q1 "¿Cuál es la idea principal de esta historia?" is reading-generic -> "¿Qué les recomienda el dueño del hotel a los amigos?" with four matching options; Q3 "¿Qué lección sacan..." -> "¿Qué comentan los amigos al volver al hotel?".

### 2. Metadata
- No missing `teaches`/`category`, no `distractor_skills` needed. a2.05.04.ex16 and a2.05.05.ex09 are tagged vocabulary but choose between whole sentences with different connectors (unsure; porque-y-por-eso would also be defensible). a2.05.04.ex18/ex19 (listening items on porque) are tagged with the unit vocabulary skill (unsure, same reason).

### 3. Goals / checklists
- Recap: a2-05-01 presents *porque* as new although A1 Unit 2 (`por-que-y-porque`) taught it; the text now opens "You know *porque* from A1 Unit 2".
- Goals/checklists are the lessons' own and promise what is practised. The same three-row table (porque / por eso / pretérito perfecto) is repeated unchanged on all five grammar screens (repeated screens; not rewritten).

### 4. Doubtful
- (unsure) Topic mismatch: the lessons drill rain, a changed route and getting wet; the story is a good-weather walk to a viewpoint and uses *porque* once and *por eso* never. The reader gets little of the unit's grammar from the story. Not changed.
- (unsure) Consolidation ex13 shows suspect unmet *mojado* (a copy of a2.05.03.ex12, where the lesson list has *mojarse*): a checker artifact of lemma matching, left.
- (unsure) a2.05.02.ex14/ex15 and a2.05.01.ex14/ex15 have the same wrong-option pattern (*Por eso ...* / infinitive) in neighbouring items.

### 5. Dictionary
(none: audit-reader-coverage for story a2-05 reports 0 not in the dictionary, 0 literal compound guesses)


## UNIT 6 comparing-trips-memories (a2-06-01..05, consolidation, story a2-06)

Fixes: 41 in fixes-comparing-trips-memories.json (1 marked `"variant": "es-es"`); challenges: 6 in challenges-comparing-trips-memories.json. check_fixes.py: 0 rejected.

### 1. Found by reading
- a2.06.02.ex10 (ERROR length-giveaway 11 vs 4) and a2.06.03.ex10 (10 vs 4): wrong options "more"/"less" are shorter than the right gloss -> ["comfortable","beautiful","interesting"], ["experience","unforgettable","short"].
- a2.06.05.ex14 (ERROR length-giveaway 52 vs 29): "¿Qué han hecho en Ninh Bình?" / "Han hecho muchas actividades durante las vacaciones." is generic and uses unmet *actividades*, *durante*, *escuela* -> "¿Qué hacen después de desayunar?" / "Hacen las maletas." (story line 2); options use *billetes*, so the fix is marked es-es.
- a2.06.05.ex15 (ERROR tell-absolute *Nunca*; unmet *nunca*, *lugares*, *olvidado*) -> "¿En qué piensa Kaylee?" / "En los arrozales y los pueblos." / "En el hotel y en el mirador." / "En la clase y en el paseo."
- a2.06.05.ex11 (unmet *algunos*, stem *subir* b1-19-02), ex12 and ex13 (stems with *actividad*, a2-13-04), ex16, ex17 (prompts with *actividad*) -> reworded with met words. ex13/ex17 asked for "la actividad más divertida", a relative superlative (`superlatives`, b1-07-04): ex17's right answer was "La clase de cocina ha sido la actividad más divertida." and a wrong option "tan divertida como la actividad" was nonsense; ex17 duplicated reading ex13 -> ex17 is now "¿Qué ha sido más divertido, la clase de cocina o el paseo en barco?" with a comparative answer.
- Superlative: the 06-05 tip ("once you are ranking three or more experiences ... you need más or menos again") hints at it without teaching it -> tip replaced; story line 7 "la actividad más divertida" -> "ha sido muy divertida".
- a2.06.01 (and 06-05, consolidation, 14 suspects): *el anterior* used from the first exercise but *anterior* is listed only at a2-imperfectocontraste-03; *otro* (06-02 ex16, 06-03 ex02/ex19, consolidation) only at b1-23-02 -> both added to a2-06-01-voc; *lugar/lugares* (06-02 ex15/ex16, 06-04 ex03, 06-05, consolidation) -> *el lugar* added to a2-06-02-voc.
- a2.06.03.ex03 and ex17 use *autobús* (b1-01-02) -> "que el paseo" / "tan largo como la excursión".
- "El hotel es menos cómodo que el alojamiento" (06-01 screen example, ex11, consolidation ex02, speaking): a hotel is a kind of *alojamiento*, so the comparison is nonsense -> "... que la casa".
- a2.06.01.ex15, a2.06.02.ex16, consolidation.ex15: "¿Han sido iguales los dos viajes?" answered "Sí, han sido tan interesantes como el otro." compares two trips with one of them -> "Sí, este ha sido tan interesante como el otro." (wrong options keep one fault each: *más ... como*, *tan ... que*, agreement).
- Consolidation ex18 item 1 "¿Han sido los dos viajes tan interesantes como el otro?" same flaw; item 3 "Ask which trip someone prefers." does not pin *tú* -> reworded.
- a2-06-04-gr tip is meaningless ("Spanish keeps the adjective after the noun even inside a comparison ... not a fronted 'more beautiful city'"); in the examples the adjective follows *es* -> replaced.
- Perfecto with *el año pasado* (a2.06.02.ex14, consolidation.ex06, 06-03 screen example/tip and its speaking line, 06-04 ex19, 06-05 screen example, ex19, consolidation ex17): "He viajado más que el año pasado." without a current-period marker is not natural Spain Spanish -> "Este año he viajado más que el año pasado." (unsure; ex14 got "más que Meg" instead). "Este mes hemos viajado menos que el mes pasado." (06-03 ex14) is fine, it has *Este mes*.
- Story a2-06: Q1 "¿Qué resume mejor el contenido del texto?" is reading-generic -> "¿Adónde vuelven los amigos?"; Q2 "¿Cuál fue la actividad favorita..." is a preterite stem (a2-11-01) -> "es".

### 2. Metadata
- No missing `teaches`/`category`; no `distractor_skills` needed. Fill-blanks that supply an adjective (06-01 ex03/ex11, 06-02 ex03, 06-04 ex03) are correctly tagged vocabulary.
- (unsure) a2.06.02.ex11/ex13, 06-03 ex11/ex13, 06-04 ex11/ex13 are `adjective-agreement` and wrong options mix agreement faults with *como* for *que* in the same item (ex13: "más interesantes como los viajes" is a comparative fault, not agreement). Left.

### 3. Goals / checklists
- a2-06-02 goal and checklist promise to compare "people": no item or example compares people -> "places and experiences" (three lines in the lesson file; the challenge canDo copies the new line).
- No screen of the unit teaches *mejor* / *peor*, although a2-06-01 lists them as vocabulary and the unit goal names the comparative family: the learner is never told *más mejor* is wrong. Added one sentence to the 06-01 text (unsure, wording is mine).
- The same three-row table is repeated unchanged on all five grammar screens.

### 4. Doubtful
- (unsure) Story a2-06 line 1 "llega más rápido de lo que todos esperaban" (*más ... de lo que*) and line 5 "Lo que más me ha gustado ha sido ..." are B1-style comparative/relative patterns; left (stories are exempt from met words; the level is borderline).
- (unsure) 06-01 ex03 "Este viaje es más __ que el anterior." (answer *interesante*) accepts any adjective grammatically; the `english` pins it, as the checker accepts.
- Consolidation copies left as instructed. Names *Ninh* and *Bình* in story a2-06 are names, not dictionary gaps.

### 5. Dictionary
(none: audit-reader-coverage for a2-06 reports only the names *Ninh*, *Bình*; a2-04 and a2-05 report none)

## Fix counts
- Unit 4 following-instructions: 36 fixes (fixes-following-instructions.json), 6 challenges
- Unit 5 giving-reasons-opinions: 24 fixes (fixes-giving-reasons-opinions.json), 6 challenges
- Unit 6 comparing-trips-memories: 41 fixes (fixes-comparing-trips-memories.json), 6 challenges
