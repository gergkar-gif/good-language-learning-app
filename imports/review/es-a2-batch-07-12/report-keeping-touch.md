# Review report: es-es A2 Units 10, 11, 12 (reader B)

## Unit 10 keeping-touch (63 fixes in fixes-keeping-touch.json, 6 challenges in challenges-keeping-touch.json)

Unit 10 teaches no new grammar (perfecto / ya / todavía no / porque are known from Units 1, 2, 5). check-content: 8 errors and 12 suspects before; after the fixes (applied in a scratch copy, word-lesson index rebuilt) 0 errors and 0 suspects, and check_fixes.py rejects none.

### 1. Found by reading
- a2.10.01.ex02, ex09; a2.10.02.ex02, ex09; a2.10.03.ex02, ex09; a2.10.04.ex02, ex09; a2.10.05.ex02, ex09; a2.10.consolidation.ex01: the wrong option is a preterite before its screen (*Mi madre llamó.*, *envió ... el año pasado*, *llamó anoche porque necesitaba*, *llamaron hace diez años*, *llamó ayer*; Unit 11 teaches it). Fix: a one-fault perfecto option (*Mi madre has llamado.*) for the "uses the perfecto correctly" items; *ha llamado hace diez años* (perfecto with a finished-past marker, wrong in Spain) for the "recent action" items. 10-03 ex02 also had unmet *anoche*, 10-04 ex02 unmet *carta* (now *mensaje*), consolidation ex01 unmet *ayer* (and copied 10-01 ex02, so the words vary).
- a2.10.04.ex13: *Ya he contestado porque recibo el mensaje.* is a second right answer (the 10-03 tip itself says the porque clause may be present tense), and *Ya contesté* is a preterite. Fix: two one-fault participle options (*he recibir*, *he recibida*).
- a2.10.consolidation.ex08: wrong options *Ya contesté porque recibí* (preterite) and *Todavía contesto* (no *no*). Fix: options that each lack one structure (*Ya contesto porque recibo el mensaje.*, *Ya he contestado el mensaje.*).
- a2.10.05.ex11-ex15 (reading): not answerable from the story as written and invented people/things (*¿Quién llama desde casa? La madre*, *el protagonista*, *aeropuerto*, *excursión*, "la familia está enfadada"); the story has Carlos video-calling Ana and Andreas, Meg calling her parents, Lauren's line, the closing mood. Fix: five questions about what the people say and do (*¿Con quiénes habla Carlos por videollamada?*, *¿Qué quiere ver Ana?*, *¿Con quién habla Meg?*, *¿Qué dice Lauren?*, *¿Cómo se sienten los amigos después de las llamadas?*). ex12 and ex14 also had unmet *protagonista* / *aeropuerto*.
- a2-10 story comprehension (story JSON): Q1 *¿Cuál es el tema central de la historia?* is generic; Q3 asks *¿Por qué dice Lauren ...?* but the story gives no reason (the explanation invents "entusiasmaron"). Fix: *¿Cuándo llaman los amigos a sus familias?* and *¿Qué dice Lauren después de las llamadas?* with story-based options and explanations.
- a2.10.05.ex19 prompt 4 "Say that you have already had a conversation with your family." stores *Ya hemos tenido una conversación con la familia.* (we): prompt now "Say that we have already had a conversation with the family."
- a2.10.01.ex11: third fill-blank of the same shape (ex03, ex07, ex11 all answer *ha*, same hint). Now *Mis padres __ hablado conmigo.* / *han*.
- a2.10.03.ex15, ex16 (length 45 vs 25, 42 vs 22), a2.10.consolidation.ex04, ex11, ex15 (22 vs 14, 45 vs 25, 45 vs 25): right answers shortened to natural replies (*Porque he recibido una noticia.*) and wrong options reworded to similar length; ex04 question now "I have not called my mother yet" so the wrong options can reuse its words; ex11 and ex15 also copied 10-03 ex12 / ex15 and are now new sentences.
- a2.10.consolidation.ex12, ex13: consolidation-copy of 10-04 ex12 / ex14. Varied (*Mi hermano todavía no ha llamado porque está ocupado*; *ya ha llamado / todavía no ha escrito / ha contestado porque*).
- Grammar screens a2-10-01 to a2-10-05 present known material as new (the unit teaches nothing new): each now opens "You know ... from Unit N" (perfecto Unit 1, ya / todavía no Unit 2, porque Unit 5).
- a2-10-01 grammar tip: "the same five endings you would use for any -ar/-er/-ir verb" is false (he/has/ha/hemos/han are the auxiliary). Rewritten.
- a2-10-02 grammar tip says "no extra connecting words needed" while its own example uses *pero*. Rewritten.
- a2-10-04 grammar tip puts *ya* / *todavía no* after the auxiliary ("subject + auxiliary + ya/todavía no + participle"), contradicting every example and Spanish itself (*Ya he contestado*). Rewritten: marker right before *he/ha*.
- The same three-row table (ya / todavía no / porque) sits on every grammar screen of the unit, irrelevant to 10-01, 10-02, 10-03. Replaced: 10-01 haber forms, 10-02 two rows, 10-03 porque row, 10-05 question-and-answer table (10-04 keeps the three rows, which is its content).
- Words in no list: *conmigo* (first used a2-10-01) and *ocupado* (first used a2-10-04) added to those vocabulary lists; *preocupado* (the lesson uses preocupado/-a/-os but lists only *preocuparse*) added to a2-10-03 (unsure).
- Facts checked against the stories: Carlos calls Ana and Andreas (sister and brother), Meg's parents are in South Africa, Lucía met in a2-07: all consistent. Challenges use Carlos, Meg, Kaylee, Daniela in the flat in Hanoi.

### 2. Metadata
- distractor_skills removed with the preterite options (10-01 ex02/ex09, 10-02 ex02/ex09, 10-03 ex02/ex09, 10-04 ex02/ex09/ex13, 10-05 ex02/ex09, consolidation ex01).
- distractor_skills added for well-formed present-tense wrong options: 10-02 ex15 {2: present-tense}, 10-04 ex15 {2}, 10-05 ex16 {2}, ex18 {2}, consolidation ex14 {1}, ex04 {2}; consolidation ex08 {1: present-tense, 2: ya-todavia-no}.
- No other tag problem found (teaches match what a wrong answer shows; reading items carry none).

### 3. Goals / checklists
- a2-10-05 goal, goal-screen line and checklist: "using the Unit 10 grammar and vocabulary" (meta, promises nothing) -> "Talk about a recent call from home, saying what has happened, what has not happened yet and why." (canDo of its challenge copies it). Other five goals and checklists are the lesson's own and fine.

### 4. Doubtful
- a2.10.04.ex15: Meg answers *¿Has contestado el mensaje?* with *Ya he contestado porque he recibido el mensaje.*; the reason does not explain anything and the wrong option *Todavía no he contestado porque he recibido el mensaje* is odd rather than clearly wrong. Left (unsure).
- Story a2-10: Lauren and Kaylee are Meg's sisters, yet "Meg habla con sus padres" and "Daniela, Lauren y Kaylee también llaman a sus familias" lists them separately; also *mientras tanto* (Unit 13) and *no me extraña* in a story (exempt from met words) (unsure).
- All options have the correct answer at index 0 across the unit (assumed shuffled at run time).
- *preocupado* vocabulary addition (unsure).

### 5. Dictionary
No "literal compound guess" or "not in the dictionary" word except the name *andreas* (look-alike of a name; skipped).

Fix count Unit 10: 63 (17 auto, 46 for review per check_fixes.py; 0 rejected). Also the a2-10-05 goal is fixed in curriculum.json.

---

## Unit 11 what-happened (61 fixes in fixes-what-happened.json, 6 challenges in challenges-what-happened.json)

Unit 11 teaches the regular preterite (a2-11-01), irregular stems (a2-11-02), questions (a2-11-03), sequencing (a2-11-04). check-content: 3 errors and 40 suspects before; after the fixes (applied in a scratch copy, word-lesson index rebuilt) 0 errors, 0 suspects; check_fixes.py rejects none. validate-content then reports "locked tags changed" for every item whose distractor_skills the fixes change: run `scripts/lock_tags.py es-es a2/what-happened --update --reason ...` after applying.

### 1. Found by reading
- Futuro simple (Unit 19) as a wrong option, before its screen: a2.11.01.ex05 (*celebrará*), ex09 (*visitaremos*); a2.11.02.ex05 (*comprará*), ex09 (*probaremos*); a2.11.03.ex05 (*responderá*), ex09; a2.11.04.ex05 (*llegará*), ex09 (*hablaremos*); a2.11.05.ex05 (*comprará*), ex09 (*pasearemos*). Fix: a perfecto-with-*ayer* option (*Ayer Meg ha comprado un abanico.*, single fault in Spain) where that cannot also be right, *va a celebrar* (ir a, A1) in 11-01 ex05 (a perfecto would be a second right answer there), and real preterite forms of other persons for the "completes the sentence" items (*visitamos / visité / visitaron*). ex09 of 11-01 also had the garbled *visitamos hemos*.
- a2.11.01.ex15: *Meg: ¿Celebraron una tradición? / Carlos: Sí, celebraron una tradición.* Carlos would say *celebramos*; the right answer copies the question's form. Now *¿Celebraste ayer una tradición?* / *Sí, celebré una tradición.*
- Dialogues without a time word where the perfecto is a natural second answer: a2.11.01.ex14, a2.11.03.ex16, a2.11.05.ex16/ex17/ex18, a2.11.consolidation.ex15/ex16. Added *ayer* to the question.
- a2.11.01.ex11 *Nosotros __ en el festival.* / *bailamos*: the -ar nosotros form is also the present, and the sentence had no time word; no exercise uses an -er/-ir verb although the screen teaches -í, -ió, -imos. Now *El sábado pasado nosotros __ en el festival.* / *comer* / *comimos*. The 11-01 screen table lacked *bailamos* and any -er/-ir form, and had no -er/-ir example: table and example added; tip now says *bailamos* is both "we dance" and "we danced" (ayer decides).
- a2.11.01.ex10 *¿Qué significa «el festival»?* answer "festival" in the prompt (answer-in-prompt): asks *bailar* instead.
- a2-11-02 screen shows only yo forms, but ex15/ex16 prompts use *fuiste* / *hiciste* and a2-11-04 uses *fuimos* and a2-11-05 *estuvimos*: text and table now give the tú and nosotros forms.
- a2.11.02.ex12 wrong option *hací* is a garbled non-form (unmet): *hice / hizo / hiciste*. a2.11.03.ex12 *¿Dónde estuviste has?* is garbled and the stem gave no meaning (*¿Dónde estuve?* would also be right): stem "Which question means 'Where were you?'", options *estuviste / estuvistes / estás*.
- Character facts vs story a2-11: Meg buys the fan, Carlos tries the sweet, Daniela talks with the artists and takes photographs. a2.11.02.ex05 (*Carlos compró un abanico* -> Meg), a2.11.03.ex16 and a2.11.05.ex16/ex17 (speakers swapped), a2.11.04.ex07 (*Carlos habló con los artistas* -> Daniela).
- a2.11.04.ex17: three prompts say "you" but the stored answers are nosotros (*Primero visitamos el festival.*): prompts now say "we". ex11: hint "first" is the answer in English: removed.
- Story a2-11 (shown in a2-11-05): *hubo* ("hubo un festival"), imperfect *estaban llenas*, pluperfect *nunca había visto* (B1) in a Unit 11 story. Fixed to *los amigos fueron a un festival*, *estuvieron llenas*, *un dulce tradicional muy diferente*. Reading question a2.11.05.ex11 (*¿Dónde hubo un festival?*, options airport / hotel) now *¿Adónde fueron los amigos el fin de semana pasado?*; ex15 (unmet *participó*, *juego*) now *¿Con quiénes habló Daniela?* with similar-length options; ex14 (length 32 vs 19, unmet *mano*) now *Un pequeño abanico.*
- Story comprehension questions in a2-11.json: Q1 *¿De qué trata principalmente este texto?* and Q3 *¿Qué demuestra la experiencia del grupo...?* are generic / inference; now *¿Qué hizo Daniela en el festival?* and *¿Dónde cenaron los amigos antes de volver a casa?* (Q2 about Lauren's novel is fine).
- Unmet words: *ayer* (first listed a2-16-02, used from the a2-11-01 grammar) added to the a2-11-01 list (clears 12 suspects and the tell-time-word error with the rewritten consolidation ex11/ex16); *el día*, *bueno* added to a2-11-02 (grammar example *Tuve un buen día*, consolidation ex06); *mirar*, *el dulce*, *tradicional* added to a2-11-05 (ex03, ex08, ex13, ex16, ex19, ex20, story). *pasear / paseamos / pasearemos* (ex09) replaced by *caminar* forms; *asistieron / asisten / asistido, aire* (ex18) by *Fuimos a un concierto.*; *tarta* in the a2-11-03 tip by *fotografías*.
- Consolidation copies: ex02 (of 01.ex03), ex07 (of 04.ex12), ex10 (of 02.ex14), ex20 (of 03.ex19): words varied. ex11 (tell-time-word, 45 chars) rewritten with "yesterday" in the stem; length error a2.11.05.ex14 fixed (above).

### 2. Metadata
- distractor_skills: *futuro-simple* removed everywhere (options replaced); added/kept present-tense / preterito-perfecto on the new options (list in the fixes file); 11-01 ex05 gets {1: present-tense, 2: ir-infinitive}; 11-03 ex12 {2: present-tense}; new dialogue distractors tagged.
- All unit tags are locked (tags.lock.json): run `scripts/lock_tags.py es-es a2/what-happened --update --reason "..."` after applying (validate-content fails 6+ items otherwise).
- No wrong `teaches` found; a2.11.consolidation.ex14 (*Fui al festival*, irregular) is tagged preterito-indefinido while a2.11.03.ex15 (same answer) is tagged preterite-irregular-stems (minor, unsure).

### 3. Goals / checklists
- a2-11-consolidation checklist (error checklist-shared): word for word the line of a2-17-02. Goal item and checklist now "Use the pretérito indefinido to recount a day at the festival." / "I can use the pretérito indefinido to recount a day at the festival." (the lesson-level `goal` field "Review regular and irregular ..." left as is).
- Other goals and checklists are the lesson's own and match the practice.

### 4. Doubtful
- a2.11.04.ex15/ex16 and others use *hicieron* (3rd plural of hacer), which no Unit 11 screen shows (only hice, hiciste, hicimos). Left (unsure).
- Story a2-11: *les hizo muchas fotografías* uses *les* (indirect object, Unit 25); stories are exempt from met words, kept (unsure). Story still uses *asistieron*, *participó* (unmet, exempt).
- a2.11.01.ex09 / a2.11.03.ex09 / a2.11.04.ex09 / a2.11.05.ex09 now test the person of the preterite (*visitamos / visité / visitaron*): two wrong options fail in the same way (person); alternative would be present forms, which clash with the identical nosotros form (unsure).
- Every option list has the correct answer at index 0 (assumed shuffled at run time).

### 5. Dictionary
Nothing: the audit reports 0 words not in the dictionary and 0 literal compound guesses for story a2-11.

Fix count Unit 11: 61 (3 auto, 58 for review per check_fixes.py; 0 rejected).

---

## Unit 12 giving-receiving-things (64 fixes in fixes-giving-receiving-things.json, 6 challenges in challenges-giving-receiving-things.json)

Unit 12 teaches the direct object pronouns (a2-12-01). No lo/la/los/las occurs earlier in Units 10-11 (only *les hizo* in the a2-11 story). check-content: 2 errors and 11 suspects before; after the fixes (scratch copy, index rebuilt) 0 errors and 1 suspect (*envolvieron* in ex08: a form of the listed *envolver*, false positive); check_fixes.py rejects none. No tag changes.

### 1. Found by reading
- a2-12-03 grammar, ex03, ex05, ex11, ex14, ex15, ex16: *¿Qué compraste?* answered with *Lo compré.* (examples, table, fill-blanks with the noun as a hint, dialogues *¿Qué compraste? ¿El regalo?*). A "what" question asks for the thing, so "it" says nothing. Screen rewritten around yes/no questions (*¿Compraste el regalo? ¿Lo compraste? Sí, lo compré.*; *¿Qué compraste?* is answered with the noun), and the items now use yes/no questions with the noun in the question (hints removed).
- a2-12-02 and later lessons use *di* (ex04 *La di.*, a2-12-04 example *la di*) and *dieron* (a2-12-05 example, ex19) but no screen teaches dar in the preterite (Unit 11 has no dar). a2-12-02 screen now teaches di, diste, dio, dimos, dieron (text, example, table row); its fourth example's English also lacked the arrow half.
- a2.12.05.ex05 *Kaylee lo eligió* (e>i stem change, not taught): now *Lucía lo recibió.*
- Reading questions a2.12.05.ex12-ex15 invent things the story never says (*¿Qué envolvieron? El regalo*, *Lucía recibió ... El aeropuerto / La bicicleta*, a "regalo" bought, *Un libro* also possible since Kaylee chooses a book) and use unmet *reaccionó*. Now *¿Qué compró Meg?*, *¿Qué preparó Daniela?*, *¿Qué escribió Lauren?*, *¿Qué hizo Lucía?* (story p9 now says *se sorprendió, se alegró mucho*, which also keeps the listed words alegrarse / sorprenderse in use). ex15 length error 26 vs 14 fixed with similar-length options.
- Story a2-12 (shown in a2-12-05): pluperfect *habían vivido* (B1) and imperfect *era el mejor recuerdo* (Unit 21): now *han vivido*, *es el mejor recuerdo de este año*. Story comprehension: Q1 *¿Cuál es el tema principal del texto?* generic -> *¿Quién tuvo la idea de la sorpresa?*; Q3 options in pluperfect / imperfect (*había ayudado*, *era el cumpleaños*, *había pedido*) simplified; the Q1 explanation had the typo *dárselas gracias*.
- Titles/goals promising what the lesson does not practise: a2-12-02 *I Gave It to Her* / "Say who received an object" (indirect objects, Unit 25; the lesson only drills placement and agreement) -> *Where the Pronoun Goes* / "Place the direct object pronoun before the verb and choose lo, la, los or las."; a2-12-03 *What Did You Give Them?* / "what people gave" (no dar exercise) -> *Did You Buy It?* / "what people bought or received." (lesson, vocabulary file and curriculum.json).
- Unmet *carta*: a2.12.03.ex12 (flagged) and a2.12.01.ex12 (same sentence, not flagged) -> *tarjeta* / *regalo* / *caja*.
- Same lo/la/los/las table on a2-12-01, 04 and 05: 04 now a verb table (comprar -> lo compré ...), 05 a table of the story's verb forms.
- Prompts say "you" but the stored answer is nosotros: a2.12.04.ex17 (*Preparamos la sorpresa y la llevamos.*), a2.12.05.ex19 (*... a Lucía*): prompts now "we".
- a2.12.05.ex17 *¿Qué recibió Lucía? ¿El regalo?* / *Lo recibió.* -> *¿Recibió Lucía el regalo?* / *Sí, lo recibió.* a2.12.consolidation.ex15 same pattern -> *¿Recibiste la noticia?*
- Consolidation copies (8): ex01, ex02, ex03, ex04, ex06, ex07, ex13, ex16 copied a2-12-01 / 04 items: new nouns (mapa, noticia, cajas, flores). ex12 *We bought the gifts and bought them* is a nonsense sentence -> *Preparamos las cajas y las llevamos.* ex14 is a2-12-01 ex14 with swapped speakers -> *¿Compraste el mapa?*
- Character facts checked against story a2-12 (Meg buys flowers, Daniela makes a cake, Lauren writes a card, Kaylee chooses a book, Carlos has the idea, at Lucía's flat): consistent after the reading fixes.

### 2. Metadata
- All items teach objeto-directo (or vocabulary); the wrong options are wrong forms of the tested skill, so no distractor_skills are needed. No tag change in this unit.

### 3. Goals / checklists
- a2-12-01 checklist-you: *I can say what you bought...* -> *what I bought* (canDo of its challenge follows).
- a2-12-02 and a2-12-03 goal, goal screen, checklist and curriculum.json goal corrected (see above); other goals fine.

### 4. Doubtful
- a2-12-02 re-explains placement and agreement already taught in a2-12-01 (screen now says "You know from the last lesson" and adds dar); a2-12-04 and a2-12-05 screens also restate it (unsure).
- Story a2-12 *les dio un abrazo*, *darle las gracias* use indirect object pronouns (Unit 25); stories are exempt, kept (unsure).
- *camiseta* (a2.12.01.ex05) is not flagged but I could not find where it is taught (unsure).

### 5. Dictionary
Nothing: the audit reports 0 words not in the dictionary and 0 literal compound guesses for story a2-12.

Fix count Unit 12: 64 (15 auto, 49 for review per check_fixes.py; 0 rejected).

## Totals
Unit 10: 63 fixes, 6 challenges. Unit 11: 61 fixes, 6 challenges. Unit 12: 64 fixes, 6 challenges.
