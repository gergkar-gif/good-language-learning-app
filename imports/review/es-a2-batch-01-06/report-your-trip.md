# Review of es-es A2 Units 1-3 (reader A)

## Unit 1 your-trip (a2-01-01 … a2-01-consolidation, story a2-01)

### 1. Found by reading
- a2.01.01.ex06 (a2-01-01-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «viajar» mean?
- a2.01.01.ex12 (a2-01-01-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.01.ex13 (a2-01-01-ex.json): Same builder as ex08 (hemos llegado al hotel, only the capital differs): vary the item. Fix: tiles -> ["a", "Hemos", "Vietnam", "viajado"]; solution -> ["Hemos", "viajado", "a", "Vietnam"]; english -> We have travelled to Vietnam.
- a2.01.01.ex15 (a2-01-01-ex.json): "¿Han llegado al hotel?" is read as "you all" in 01-03/01-04 (answer hemos), so "Sí, han llegado" is only right for a third-person reading; name the third persons. Fix: prompt -> [{"speaker": "Meg", "text": "¿Han llegado Daniela y Lauren al hotel?"}, {"speaker": "Carlos", "text": "_____"}]
- a2.01.01.ex16 (a2-01-01-ex.json): Prompts do not pin the stored answers (somewhere / a hotel). Fix: template -> [{"prompt": "Say that you have travelled to Vietnam.", "answer": "He viajado a Vietnam."}, {"prompt": "Say that you have arrived at the hot…
- a2.01.02.ex06 (a2-01-02-ex.json): "significa" unmet; ask in English. Fix: question -> What does «ver» mean?
- a2.01.02.ex09 (a2-01-02-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.02.ex16 (a2-01-02-ex.json): "¿Han visto el hotel?" can be "you all": then "he visto" (Meg alone) or "hemos visto" fits; name the third persons. Fix: prompt -> [{"speaker": "Carlos", "text": "¿Han visto Daniela y Lauren el hotel?"}, {"speaker": "Meg", "text": "_____"}]
- a2.01.03.ex06 (a2-01-03-ex.json): "significa" unmet; ask in English. Fix: question -> What does «preguntar» mean?
- a2.01.03.ex07 (a2-01-03-ex.json): montañas is first taught at a2-01-05. Fix: sentence -> ¿__ visto el hotel?; english -> Have they seen the hotel?
- a2.01.03.ex09 (a2-01-03-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> In Spain, which question is correct for vosotros (informal)?
- a2.01.03.ex12 (a2-01-03-ex.json): ¿Viajarás? is the future (a2-19-01), before its screen; ir a + infinitive is known (A1 Unit 25). Fix: options -> ["¿Has viajado?", "¿Viajas?", "¿Vas a viajar?"]; distractor_skills -> {"1": "ar-verbs", "2": "ir-infinitive"}
- a2.01.03.ex14 (a2-01-03-ex.json): "durante" is in no vocabulary list; este fin de semana is a Spain perfecto marker and met. Fix: sentence -> ¿Qué __ hecho este fin de semana?; english -> What have they done this weekend?
- a2.01.03.ex16 (a2-01-03-ex.json): Friends in Spain say vosotros, not ustedes (unit teaches habéis in the same lesson). Fix: prompt -> [{"speaker": "Carlos", "text": "¿Qué habéis hecho?"}, {"speaker": "Meg", "text": "_____"}] (unsure) [variant es-es]
- a2.01.04.ex04 (a2-01-04-ex.json): "significa" unmet; ask in English. Fix: question -> What does «la habitación» mean?
- a2.01.04.ex06 (a2-01-04-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.04.ex10 (a2-01-04-ex.json): "forma" is first taught at b1-37-consolidation; ask in English. Fix: question -> Which form of haber goes with «nosotros»?
- a2.01.04.ex11 (a2-01-04-ex.json): "significa" unmet; ask in English. Fix: question -> What does «reservar» mean?
- a2.01.04.ex14 (a2-01-04-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.04.ex16 (a2-01-04-ex.json): Meg asks her friends informally: in Spain vosotros, not ustedes. Fix: prompt -> [{"speaker": "Meg", "text": "¿Habéis llegado bien?"}, {"speaker": "Carlos", "text": "_____"}] (unsure) [variant es-es]
- a2.01.04.ex17 (a2-01-04-ex.json): Third answer is present tense (Tengo) inside an item tagged preterito-perfecto; make it a perfecto sentence (puesto, taught in 01-02). Fix: template -> [{"prompt": "Say that you have arrived at the hotel.", "answer": "He llegado al hotel."}, {"prompt": "Say that you have booked a room.", "a…
- a2.01.05.ex03 (a2-01-05-ex.json): Perfecto with esta mañana (Spain); "por la mañana" is a past/habitual morning. Fix: sentence -> Hemos __ esta mañana.; english -> We have arrived this morning. (unsure)
- a2.01.05.ex04 (a2-01-05-ex.json): "significa" unmet; ask in English. Fix: question -> What does «la montaña» mean?
- a2.01.05.ex06 (a2-01-05-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.05.ex10 (a2-01-05-ex.json): "forma" is first taught at b1-37-consolidation; ask in English. Fix: question -> For «ellos», which form of haber do we use?
- a2.01.05.ex11 (a2-01-05-ex.json): "escuela" unmet (first b1-historiaantigua-02); museo is met. Fix: options -> ["En un pequeño hotel.", "En una estación.", "En un museo."]
- a2.01.05.ex12 (a2-01-05-ex.json): "bicicleta", "barco" unmet, and the story never says how they travelled; Meg says they slept in the train. Fix: question -> ¿Dónde han dormido un poco los amigos?; options -> ["En el tren.", "En el hotel.", "En el parque."]
- a2.01.05.ex13 (a2-01-05-ex.json): arrozales (first a2-02-02) and aeropuerto (a2-18-01) are unmet. Fix: options -> ["Ríos y montañas.", "Una playa y un banco.", "Un museo y una farmacia."]
- a2.01.05.ex14 (a2-01-05-ex.json): arrozales, enormes, piedra, caliza are unmet or in no list. Fix: sentence -> Los amigos han visto ríos y __ muy grandes.; english -> The friends have seen rivers and very big mountains.
- a2.01.05.ex15 (a2-01-05-ex.json): propone, día, siguiente, alquilar, bicicletas, otro are all unmet; Lauren buys a map in the story. Fix: question -> ¿Qué compra Lauren?; options -> ["Un mapa.", "Un libro.", "Una maleta."]
- a2.01.05.ex17 (a2-01-05-ex.json): arrozales unmet (first a2-02-02). Fix: options -> ["Hemos visto ríos y montañas.", "Han visto ríos y montañas.", "He visto ríos y montañas."]
- a2.01.05.ex18 (a2-01-05-ex.json): Lauren asks her friends informally: in Spain vosotros, not ustedes. Fix: prompt -> [{"speaker": "Lauren", "text": "¿Habéis reservado el hotel?"}, {"speaker": "Carlos", "text": "_____"}] (unsure) [variant es-es]
- a2.01.05.ex19 (a2-01-05-ex.json): Prompts do not pin the stored answers ("stayed" vs He reservado; "a mountain or river"). Fix: template -> [{"prompt": "Say that you have travelled to a new region.", "answer": "He viajado a una región nueva."}, {"prompt": "Say that you have book…
- a2.01.05.ex20 (a2-01-05-ex.json): arrozales unmet (first a2-02-02). Fix: sentence -> Hemos visto ríos y montañas.; options -> ["We have seen rivers and mountains.", "We have seen rivers and regions.", "We have travelled through rivers and mountains.", "We have phot…
- a2.01.consolidation.ex01 (a2-01-consolidation-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which sentence is correct?
- a2.01.consolidation.ex08 (a2-01-consolidation-ex.json): "correcta" is in no vocabulary list; ask in English. Fix: question -> Which question is correct for ustedes?
- a2-01 comprehension (a2-01.json): Comprehension question about the "text type/story" (reading-generic): ask what the people do. Fix: "¿De qué trata principalmente esta historia?" -> "¿Qué hacen los amigos después de dejar las mochilas?"
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "De cómo los amigos llegan a Ninh Bình y comienzan su viaje." -> "Salen a dar un paseo por el pueblo."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "De una clase de cocina en un restaurante vietnamita." -> "Vuelven a la estación para tomar otro tren."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "De la compra de billetes de tren para volver a Hanói." -> "Van a una clase de cocina."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "De una excursión difícil por una montaña peligrosa." -> "Se quedan en el hotel hasta la noche."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "La historia describe la llegada del grupo de amigos a Ninh Bình, su instalación en el hotel y sus primeros planes de va…" -> "Después de dejar las mochilas, los amigos salen a dar un paseo por el pueblo y ven arrozales, ríos y montañas."
- a2-01 comprehension (a2-01.json): Preterite (descansaron, durmieron) in a Unit 1 question: the preterite is first taught in a2-11-01; use the perfecto the unit teaches. Fix: "¿Cómo descansaron los amigos durante el viaje hacia Ninh Bình?" -> "¿Cómo han descansado los amigos durante el viaje hacia Ninh Bình?"
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "Durmieron en un hotel cerca de la estación." -> "Han dormido en un hotel cerca de la estación."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "Durmieron un poco en el tren." -> "Han dormido un poco en el tren."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "No durmieron nada durante toda la noche." -> "No han dormido nada durante toda la noche."
- a2-01 comprehension (a2-01.json): Part of the rewritten question (same question block as above). Fix: "Descansaron en una cafetería junto a la carretera." -> "Han descansado en una cafetería junto a la carretera."
- a2-01 comprehension (a2-01.json): Preterite (perdió, compró) in an option; use the perfecto. Fix: "Porque Lauren perdió el mapa que compró en el pueblo." -> "Porque Lauren ha perdido el mapa que ha comprado en el pueblo."
- (a2-01-05-voc.json): durante is in no vocabulary list but is used in a2-01-05 (dialogue from the story), a2-02-05 and a2-03-05: add it to the first lesson that uses it. Fix: ""lemma": "el río",
      "translation": "river",
      "pos": "noun"
    }" -> ""lemma": "el río",
      "translation": "river",
      "pos": "noun"
    },
    {
      "lemma": "durante",
      "translation": "during",
…"

### 2. Metadata
- a2.01.01.ex04 (a2-01-01-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}
- a2.01.01.ex09 (a2-01-01-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}
- a2.01.02.ex02 (a2-01-02-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}
- a2.01.02.ex04 (a2-01-02-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}
- a2.01.02.ex12 (a2-01-02-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}
- a2.01.consolidation.ex11 (a2-01-consolidation-ex.json): Gerund option is a well-formed progressive form (A1 Unit 19), so it takes distractor_skills. Fix: distractor_skills -> {"2": "progressive"}

### 3. Goals / checklists / screens
- (a2-01-01.json): Title promises "Have you ever" (alguna vez, Unit 9 experiences), which the lesson does not teach. Fix: ""title": "Have You Ever...?"" -> ""title": "Recent Travel"" (unsure)
- a2-01-05-integrated-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "spanish": "Hemos llegado por la mañana." -> "spanish": "Hemos llegado esta mañana."; "english": "We have arrived in the morning." -> "english": "We have arrived this morning."

### 4. Doubtful
- a2-01-01 title "Have You Ever...?": promises alguna vez (Unit 9); retitled "Recent Travel" (fix is unsure).
- a2.01.02.ex02 / a2.01.consolidation.ex03 *veído* (and *reservido*, *llegido* in a2.01.01.ex04/ex09, a2.01.04.ex02): non-words as wrong options; each is the over-regularised participle the item is about, so kept (the brief names veído as a defect: unsure). consolidation.ex03 is a copy of a2.01.02.ex02 and was left alone.
- Dialogues where Meg, Lauren or Carlos use *ustedes* (*¿Han llegado bien?*) to friends (a2.01.03.ex16, a2.01.04.ex16, a2.01.05.ex18, consolidation ex15): in Spain friends say *¿Habéis…?*. Changed in the three lesson items (variant es-es, unsure); consolidation copies left; formal receptionist lines are right.
- a2.01.03.ex04 and ex09 both ask for *habéis* (vosotros); one could go. es-latam has no vosotros: those two items and the grammar tip need a latam version.
- a2-01-04 grammar text: "say where you have stayed": no item practises staying (*quedarse*).
- a2.01.04.ex18 listening: "I have booked accommodation" is close to "a room" (alojamiento is only a word apart): fine as a vocabulary item, tell me if you want it changed.
- a2-01-01 grammar has no Spain time-marker note (*hoy*, *esta mañana*, *este fin de semana*); suggest one tip sentence, since Units 1-3 never say why *ayer* is not used with the perfecto.
- Lesson challenge screens in all six lessons show the placeholder "Put your Spanish skills into practice for this goal" (challenges.json has no a2-01 entries); the six entries in challenges-your-trip.json replace them.
- Consolidation copies left alone as instructed: ex03, ex05, ex09, ex14, ex16.

## Unit 2 what-you-have-done (a2-02-01 … a2-02-consolidation, story a2-02)

### 1. Found by reading
- a2.02.01.ex10 (a2-02-01-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «el mapa» mean?
- a2.02.02.ex10 (a2-02-02-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «el tráfico» mean?
- a2.02.02.ex13 (a2-02-02-ex.json): length-giveaway 30 vs 22: the right option is longest; wrong options now as long (one fault each). Fix: options -> ["Todavía no hemos llegado.", "Ya hemos llegado al hotel.", "Hemos llegado al hotel."]
- a2.02.02.ex16 (a2-02-02-ex.json): Same item as ex02 (not seen the temple yet, same three options). Fix: question -> Which sentence says that they have not visited the rice field yet?; options -> ["Todavía no han visitado el arrozal.", "Ya han visitado el arrozal.", "Todavía han visitado el arrozal."]
- a2.02.03.ex05 (a2-02-03-ex.json): "No, todavía." is a natural short answer in Spain too (second right answer); the wrong option is now a word-order fault. Fix: options -> ["No, todavía no.", "No, ya.", "No, no todavía."]
- a2.02.03.ex09 (a2-02-03-ex.json): "No, ya sí." is a garbled non-phrase. Fix: options -> ["No, todavía no.", "Sí, todavía no.", "No, ya hemos alquilado."]
- a2.02.03.ex10 (a2-02-03-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «navegar» mean?
- a2.02.03.ex12 (a2-02-03-ex.json): Uses the pronoun lo (direct object pronouns, a2-12-01) before its screen. Fix: english -> No, I have not seen the river yet.; tiles -> ["No", "todavía", "no", "el", "he", "río", "visto"]; solution -> ["No", "todavía", "no", "he", "visto", "el", "río"]
- a2.02.03.ex13 (a2-02-03-ex.json): recorrer is listed only in a2-02-04, after this lesson. Fix: options -> ["¿Ya has visto el camino?", "¿Ya has ver el camino?", "¿Ya visto has el camino?"]
- a2.02.03.ex16 (a2-02-03-ex.json): Same item as ex02 (already seen the mountains, same options). Fix: question -> How do you ask 'Have they already rented the bicycles?'; options -> ["¿Ya han alquilado las bicicletas?", "¿Ya han alquilar las bicicletas?", "¿Ya alquilado han las bicicletas?"]
- a2.02.04.ex02 (a2-02-04-ex.json): "Han ya recorrer la zona." has two faults (position of ya and infinitive). Fix: options -> ["Ya han recorrido la zona.", "Todavía no han recorrido la zona.", "Ya han recorrer la zona."]
- a2.02.04.ex10 (a2-02-04-ex.json): length-giveaway 16 vs 7 (and "significa" unmet): wrong options as long as the right one. Fix: question -> What does «recorrer» mean?; options -> ["to travel around", "to rent bicycles", "to stop and rest"]
- a2.02.04.ex15 (a2-02-04-ex.json): length-giveaway 29 vs 22: wrong options as long as the right one. Fix: options -> ["No, todavía no hemos llegado.", "No, ya hemos llegado al pueblo.", "No, todavía no hemos llegar."]
- a2.02.05.ex02 (a2-02-05-ex.json): The question points to "the bike ride story", which comes later in the lesson. Fix: question -> Which sentence says that they have already rented five bicycles?
- a2.02.05.ex05 (a2-02-05-ex.json): length-giveaway 43 vs 32: wrong options as long as the right one. Fix: options -> ["Todavía no han navegado entre las montañas.", "Ya han visto los arrozales y los templos.", "Ya han alquilado cinco bicicletas hoy."]
- a2.02.05.ex10 (a2-02-05-ex.json): Same item as ex02 (already rented five bicycles, same options). Fix: question -> Which sentence says that they have already seen the temples?; options -> ["Ya han visto los templos.", "Todavía no han visto los templos.", "Ya han ver los templos."]
- a2.02.05.ex11 (a2-02-05-ex.json): búfalos is in no list, aeropuerto is first taught at a2-18-01, mar at a2-09-01; length-giveaway 38 vs 28. Fix: options -> ["Arrozales y pequeños templos.", "El museo y la estación.", "La playa y el parque."]
- a2.02.05.ex12 (a2-02-05-ex.json): varias, veces, otra, detenido are unmet; length-giveaway 38 vs 28; the right answer is now the photographs from the story. Fix: question -> ¿Qué ha hecho Meg durante el paseo?; options -> ["Ha hecho fotografías del paisaje.", "Ha navegado entre las montañas.", "Ha escrito muchos mensajes."]
- a2.02.05.ex14 (a2-02-05-ex.json): propone, día, siguiente, barco unmet; the story says they rest by a river at midday. Fix: question -> ¿Dónde descansan los amigos al mediodía?; options -> ["Cerca de un río.", "En el hotel.", "En un templo."]
- a2.02.05.ex15 (a2-02-05-ex.json): length-giveaway 50 vs 27; idea/aceptan unmet. (Exercise is not in any section of the lesson file: put it in the Reading group or delete it.) Fix: question -> ¿Por qué quieren navegar los amigos?; options -> ["Porque todavía no han navegado.", "Porque ya han visto el río.", "Porque hay mucho tráfico."]
- a2.02.05.ex19 (a2-02-05-ex.json): "Ha sido un día inolvidable": día is unmet and the participle sido is not among the irregular participles Unit 1 teaches. Fix: template -> [{"prompt": "Say that you have already rented a bicycle.", "answer": "Ya he alquilado una bicicleta."}, {"prompt": "Say that you have alrea…
- a2.02.05.ex20 (a2-02-05-ex.json): Ha sido un día: día unmet, sido not taught (see ex19). Fix: sentence -> Hemos vivido una aventura inolvidable.; options -> ["We have experienced an unforgettable adventure.", "We have experienced a boring adventure.", "We have seen an unforgettable adventure.", …
- a2.02.consolidation.ex01 (a2-02-consolidation-ex.json): "Hemos ya ver el paisaje." has two faults (position of ya and infinitive). Fix: options -> ["Ya hemos visto el paisaje.", "Todavía no hemos visto el paisaje.", "Ya hemos ver el paisaje."]
- a2.02.consolidation.ex12 (a2-02-consolidation-ex.json): Uses the pronoun lo (a2-12-01) before its screen (copy of a2.02.03.ex12, fixed the same way). Fix: english -> No, I have not seen the river yet.; tiles -> ["No", "todavía", "no", "el", "he", "río", "visto"]; solution -> ["No", "todavía", "no", "he", "visto", "el", "río"]
- a2-02 story (a2-02.json): Perfecto with "el día anterior" is wrong in Spain (preterite, Unit 11): drop the past marker. Fix: "Carlos guía al grupo con el mapa que Lauren ha comprado el día anterior." -> "Carlos guía al grupo con el mapa que Lauren ha comprado en el pueblo." (unsure)
- a2-02 story (a2-02.json): Perfecto goes with esta mañana in Spain. Fix: ""text": "Al mediodía descansan junto a un río y comen la comida que han preparado por la mañana."" -> ""text": "Al mediodía descansan junto a un río y comen la comida que han preparado esta mañana."" (unsure)
- a2-02 story (a2-02.json): Explanation follows the story line. Fix: ""El texto dice que al mediodía descansan junto a un río y comen la comida que han preparado por la mañana."" -> ""El texto dice que al mediodía descansan junto a un río y comen la comida que han preparado esta mañana."" (unsure)
- a2-02 story (a2-02.json): Generic comprehension question (reading-generic): ask what the people do. Fix: "¿Cuál es el tema principal de esta lectura?" -> "¿Qué hacen los amigos después del desayuno?"
- a2-02 story (a2-02.json): Options of the rewritten question 1. Fix: "La preparación de una cena tradicional en el hotel." -> "Han preparado una cena tradicional en el hotel."
- a2-02 story (a2-02.json): Right option of the rewritten question 1. Fix: "Un recorrido en bicicleta por los campos de Ninh Bình." -> "Han alquilado cinco bicicletas para recorrer la zona."
- a2-02 story (a2-02.json): Options of the rewritten question 1. Fix: "La reparación de varias bicicletas rotas en un taller." -> "Han reparado varias bicicletas rotas en un taller."
- a2-02 story (a2-02.json): Options of the rewritten question 1. Fix: "Un viaje en barco hacia una isla lejana." -> "Han tomado un barco hacia una isla lejana."
- a2-02 story (a2-02.json): Explanation of the rewritten question 1. Fix: "El texto relata la excursión en bicicleta que hacen los amigos por los caminos rurales y paisajes de Ninh Bình." -> "Después del desayuno, los amigos han alquilado cinco bicicletas para recorrer la zona."
- a2-02 story (a2-02.json): Preterite (prepararon) before Unit 11: use the perfecto. Fix: "La comida que prepararon por la mañana." -> "La comida que han preparado esta mañana." (unsure)
- a2-02 story (a2-02.json): Preterite (compraron) before Unit 11: use the perfecto. Fix: "Pescado fresco que compraron a unos pescadores." -> "Pescado fresco que han comprado a unos pescadores."
- a2-02 story (a2-02.json): Preterite (recogieron) before Unit 11: use the perfecto. Fix: "Frutas exóticas que recogieron en los templos." -> "Frutas exóticas que han recogido en los templos."
- a2-02 story (a2-02.json): Preterite (se rompieron) before Unit 11: use the perfecto. Fix: "Porque sus bicicletas se rompieron al final del día." -> "Porque sus bicicletas se han roto al final del día."

### 2. Metadata
- a2.02.05.ex13 (a2-02-05-ex.json): Fill-blank producing a participle (navegado) is the participle skill, as in Unit 1 (Hemos __ al hotel); it was tagged vocabulary. Fix: category -> grammar; teaches -> ["past-participles"] (unsure)

### 3. Goals / checklists / screens
- (a2-02-01.json): Checklist says "I can say what you have ..."; first person. Fix: ""I can say what you have already done using ya + pretérito perfecto."" -> ""I can say what I have already done using ya + pretérito perfecto.""
- (a2-02-02.json): Checklist says "I can say what you have ..."; first person. Fix: ""I can say what you have not done yet using todavía no + pretérito perfecto."" -> ""I can say what I have not done yet using todavía no + pretérito perfecto.""
- (a2-02-04.json): Checklist says "things you have ..."; first person. Fix: ""I can talk about things you have already done and things you have not done yet while travelling."" -> ""I can talk about things I have already done and things I have not done yet while travelling.""
- (a2-02-01-gr.json): Rule contradicts itself and its examples: it says ya sits between auxiliary and participle, then calls that order (He ya viajado) incorrect. Fix: "*Ya* normally appears between the auxiliary verb and the participle: *He ya viajado* is incorrect; *Ya he viajado* is t…" -> "*Ya* normally goes before the auxiliary verb: *Ya he viajado* is the natural form, and *He ya viajado* sounds wrong."
- (a2-02-03-gr.json): A question does not change the subject; only the auxiliary agrees. Fix: "The question form changes the subject and auxiliary as needed, but the participle stays the same." -> "The auxiliary changes for the subject as needed, but the participle stays the same." (unsure)
- (a2-02-04-gr.json): The perfecto forms come from Unit 1; the first three lessons of this unit taught ya and todavía no. Fix: "forms you learned in the first three lessons." -> "forms you know from Unit 1."

### 4. Doubtful
- a2.02.01 ex02/ex13/ex14/ex15/ex17: *todavía no* + perfecto is a wrong option in a2-02-01 although its screen is a2-02-02 (the skill ya-todavia-no names a2-02-01-gr). Real forms and the contrast is useful: kept, unsure.
- *recorrer*/*recorrido* is listed only in a2-02-04 but used in a2-02-02 (grammar example, ex03, ex04, ex15) and a2-02-03 ex13. Own-screen examples are allowed in 02-02; I replaced the a2-02-03 item; suggest adding recorrer to the a2-02-02 vocabulary list (not done).
- check-content suspects *recorrido* in a2.02.consolidation.ex02, ex08, ex17, ex19 (and a2.03.05.ex09): false positives, recorrer is listed in a2-02-04; the word index maps the participle to a B1 noun *recorrido*. Accepted.
- a2.02.05.ex15 is in no section of lesson a2-02-05 (never shown); fixed its options (length 50 vs 27, unmet idea/aceptan), but it should join the Reading group or be deleted.
- Contrast items "ya = never; todavía no = always" (a2.02.04.ex05, consolidation ex04, a2.03.03.ex05, a2.03.consolidation.ex04) break both halves at once; left.
- *detenerse* is listed in a2-02-03 and appears only in matching (its participle *detenido* is B1 in the lexicon); the verb is not drilled.
- Friends addressed with *ustedes* in every Unit 2 dialogue (*¿Han alquilado las bicicletas?*, Meg to Carlos): unnatural in Spain, not changed (one item per lesson would need a variant).
- Story a2-02 *Nunca he visto montañas…* is an experiential perfecto (Unit 9); stories are exempt, so left.
- 02-05 ex13 retag (past-participles) is unsure: the item sits in the Reading group and was tagged vocabulary on purpose.

## Unit 3 day-out (a2-03-01 … a2-03-consolidation, story a2-03)

### 1. Found by reading
- (a2-03-03-voc.json): probar (probado) is used in this lesson (grammar example, ex07, ex09, listening) and in the consolidation but is listed only in a2-04-03: add it where the lesson needs it. Fix: ""lemma": "descansar",
      "translation": "to rest",
      "pos": "verb"
    }" -> ""lemma": "descansar",
      "translation": "to rest",
      "pos": "verb"
    },
    {
      "lemma": "probar",
      "translation": "to tr…"
- a2.03.01.ex02 (a2-03-01-ex.json): "Llegamos al embarcadero." is the preterite (a2-11-01) or the present, before the screen; replaced by a known form. Fix: options -> ["Hemos llegado al embarcadero.", "Hemos llegar al embarcadero.", "Vamos a llegar al embarcadero."]; distractor_skills -> {"2": "ir-infinitive"}
- a2.03.01.ex10 (a2-03-01-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «el río» mean?
- a2.03.01.ex13 (a2-03-01-ex.json): ayer + preterite (tell-time-word): the preterite is first taught in a2-11-01 and is not a perfecto marker; wrong options use known forms instead (ir a + infinitive, A1 Unit 25). Fix: options -> ["Hemos comprado los billetes.", "Vamos a comprar los billetes.", "Compro los billetes."]; distractor_skills -> {"1": "ir-infinitive", "2": "ar-verbs"}
- a2.03.01.ex14 (a2-03-01-ex.json): ayer + preterite (tell-time-word): the preterite is first taught in a2-11-01 and is not a perfecto marker; wrong options use known forms instead (ir a + infinitive, A1 Unit 25). Fix: options -> ["Hemos visto las cuevas.", "Hemos ver las cuevas.", "Vamos a ver las cuevas."]; distractor_skills -> {"2": "ir-infinitive"}
- a2.03.01.ex15 (a2-03-01-ex.json): ayer + preterite (tell-time-word): the preterite is first taught in a2-11-01 and is not a perfecto marker; wrong options use known forms instead (ir a + infinitive, A1 Unit 25). Fix: options -> ["Sí, hemos llegado.", "Sí, hemos llegar.", "Sí, vamos a llegar."]; distractor_skills -> {"2": "ir-infinitive"}
- a2.03.02.ex10 (a2-03-02-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «la barquera» mean?
- a2.03.02.ex12 (a2-03-02-ex.json): Uses the pronoun lo (direct object pronouns, a2-12-01) before its screen. Fix: english -> Yes, I have already seen the entrance.; tiles -> ["Sí", "ya", "visto", "he", "la", "entrada"]; solution -> ["Sí", "ya", "he", "visto", "la", "entrada"]
- a2.03.03.ex10 (a2-03-03-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «descansar» mean?
- a2.03.03.ex11 (a2-03-03-ex.json): ex08 and ex11 are the same sentence (Todavía no __ descansado), only the person differs. Fix: sentence -> Ya __ hablado con los vendedores.; hint -> nosotros; answer -> hemos; english -> We have already spoken with the sellers.
- a2.03.04.ex01 (a2-03-04-ex.json): Matching shows la puesta de sol (a2-02-04) and never tests la terraza, which this lesson lists. Fix: pairs -> [["el mercado", "market"], ["la terraza", "terrace"], ["recordar", "to remember"], ["la mañana", "morning"]] (unsure)
- a2.03.04.ex10 (a2-03-04-ex.json): Spanish metalanguage "significa" is unmet (first b1-27-03); ask in English. Fix: question -> What does «la mañana» mean?
- a2.03.04.ex12 (a2-03-04-ex.json): ex04, ex08 and ex12 all drill "Ya hemos/han recorrido el mercado"; vary ex12. Fix: english -> They have already seen the sunset.; tiles -> ["la", "Ya", "puesta", "han", "de", "visto", "sol"]; solution -> ["Ya", "han", "visto", "la", "puesta", "de", "sol"] (unsure)
- a2.03.05.ex02 (a2-03-05-ex.json): Points to "the boat trip", a story that comes later in the lesson. Fix: question -> Which sentence says 'We have already seen very beautiful places'?
- a2.03.05.ex04 (a2-03-05-ex.json): Uses antes de + infinitive (a2-04-01) before its screen, has no subject for the English "Kaylee", and 11 tiles; use the lesson's own example. Fix: english -> I still want to try more typical food.; tiles -> ["probar", "Todavía", "típica", "quiero", "comida", "más"]; solution -> ["Todavía", "quiero", "probar", "más", "comida", "típica"]
- a2.03.05.ex10 (a2-03-05-ex.json): Same item as ex02 (same three options). Fix: question -> Which sentence says that the holidays have already started?; options -> ["Las vacaciones ya han empezado.", "Las vacaciones todavía no han empezado.", "Las vacaciones ya han empezar."]
- a2.03.05.ex11 (a2-03-05-ex.json): demasiado, lugar unmet. Fix: question -> ¿Qué dice Meg sobre el paseo?; options -> ["Es su favorito.", "Es muy tranquilo.", "Todavía no ha visto el río."]
- a2.03.05.ex12 (a2-03-05-ex.json): carta unmet; "Compra fruta" is true of everyone in the story (second right answer). Fix: options -> ["Toma fotografías.", "Escribe un mensaje.", "Va a una clase de cocina."]
- a2.03.05.ex14 (a2-03-05-ex.json): junto, inmediatamente unmet. Fix: options -> ["Visitan un pequeño mercado.", "Vuelven a Hanói en tren.", "Van a una clase de cocina."]
- a2.03.05.ex15 (a2-03-05-ex.json): length-giveaway 37 vs 27; algunas, notas unmet. Fix: options -> ["Escribe en su cuaderno.", "Toma fotografías sin parar.", "Va a una clase de cocina."]
- a2.03.05.ex20 (a2-03-05-ex.json): "The trip has started in the worst possible way" has two faults (trip and worst). Fix: options -> ["The holidays have started in the best possible way.", "The holidays have ended in the best possible way.", "The holidays have started in …
- a2.03.consolidation.ex12 (a2-03-consolidation-ex.json): lugares is unmet (first a2-condicionalsimple-02). Fix: english -> We have already seen the caves and the river.; tiles -> ["las", "Ya", "y", "hemos", "el", "cuevas", "visto", "río"]; solution -> ["Ya", "hemos", "visto", "las", "cuevas", "y", "el", "río"]
- a2-03 story (a2-03.json): Preterite (empezó) in a Unit 3 story line; the preterite is first taught in a2-11-01. Fix: "desde que empezó el viaje" -> "desde el principio del viaje"
- a2-03 story (a2-03.json): Generic comprehension question (reading-generic): ask what the people do. Fix: "¿Qué describe principalmente la historia?" -> "¿Qué hacen los amigos en el embarcadero de Tam Cốc?"
- a2-03 story (a2-03.json): Options of the rewritten question 1. Fix: "La visita a un museo histórico de Hanói." -> "Visitan un museo histórico de Hanói."
- a2-03 story (a2-03.json): Options of the rewritten question 1. Fix: "La compra de regalos en una tienda de ropa." -> "Compran regalos en una tienda de ropa."
- a2-03 story (a2-03.json): Right option of the rewritten question 1. Fix: "Una excursión en barca por Tam Cốc y la visita a un mercado local." -> "Compran los billetes y suben a una pequeña barca."
- a2-03 story (a2-03.json): Options of the rewritten question 1. Fix: "Un curso intensivo para aprender a remar en ríos rápidos." -> "Hacen un curso para aprender a remar."
- a2-03 story (a2-03.json): Explanation of the rewritten question 1. Fix: "La historia relata el paseo en barca de los amigos por Tam Cốc, su conversación con la barquera y la visita posterior a…" -> "En el embarcadero de Tam Cốc, los amigos compran los billetes y suben a una pequeña barca."
- a2-03 story (a2-03.json): Imperfect (estaba, a2-imperfectobasico-01) in an option. Fix: "porque el mercado estaba cerrado" -> "porque el mercado está cerrado"

### 2. Metadata
- none

### 3. Goals / checklists / screens
- (a2-03-01.json): Checklist reads "what you have seen"; first person. Fix: ""I can talk about what you have seen and done during a recent outing using the pretérito perfecto."" -> ""I can talk about what I have seen and done during a recent outing using the pretérito perfecto.""
- (a2-03-03.json): Checklist reads "what you have"; first person. Fix: ""I can say what you have and have not experienced using ya and todavía no."" -> ""I can say what I have and have not experienced using ya and todavía no.""
- (a2-03-05.json): Checklist reads "what you have"; first person. Fix: ""I can describe a boat trip and discuss what you have already experienced and what you have not done yet."" -> ""I can describe a boat trip and discuss what I have already experienced and what I have not done yet.""
- (a2-03-01-gr.json): Screen presents the perfecto as new; it is Unit 1 (recap: "You know ... from Unit 1"). Fix: "Use the *pretérito perfecto* to talk about experiences during a recent outing. The form is *haber* + past participle." -> "You know the *pretérito perfecto* from Unit 1: *haber* + past participle. Use it to talk about a recent outing."
- (a2-03-02-gr.json): Repeats Unit 2 (a2-02-03, "Questions with Ya and Todavía No") as new; recap it. Fix: "Use *ya* in questions when asking whether something has happened already. A short negative answer can use *No, todavía …" -> "You know *ya* and *todavía no* from Unit 2. Use *ya* in questions to ask whether something has happened already; a short negative answer is…"
- (a2-03-02-gr.json): Tip is false and contradicts its own example: ¿Has visto ya el río? is ordinary Spanish, and in ¿Ya has visto...? ya is before the auxiliary, not "between the auxiliary and the participle". Fix: "Resist putting *ya* at the end of the question — *¿Has visto ya el río?* sounds like an afterthought. Keep it snug betw…" -> "*Ya* usually comes before the auxiliary: *¿Ya has visto el río?* Putting it after the participle (*¿Has visto ya el río?*) is also possible…"
- (a2-03-03-gr.json): Repeats Unit 2 (a2-02-01 / a2-02-04) as new; recap it. Fix: "Use *ya* + *pretérito perfecto* for completed experiences" -> "You know *ya* and *todavía no* from Unit 2. Use *ya* + *pretérito perfecto* for completed experiences"
- (a2-03-04-gr.json): Repeats Unit 2 (a2-02-04, "Ya y Todavía No While Travelling") as new; recap it. Fix: "Combine the *pretérito perfecto* with *ya* and *todavía no* while talking about tourism and nature. Use the same forms" -> "You know *ya* and *todavía no* from Unit 2. Combine them with the *pretérito perfecto* while talking about a day out, using the same forms"
- (a2-03-05-gr.json): Repeats Unit 2 as new; recap it. Fix: "Use the *pretérito perfecto* with *ya* and *todavía no* to describe a recent boat trip." -> "You know *ya* and *todavía no* from Unit 2. Use them with the *pretérito perfecto* to describe a recent boat trip."
- (a2-03-04.json): Goal promises "nature vocabulary", which the lesson (market, terrace, remember, morning) never practises. Fix: ""goal": "Describe a recent day out using the pretérito perfecto with tourism and nature vocabulary."" -> ""goal": "Describe a recent day out using the pretérito perfecto with ya and todavía no.""
- (a2-03-04.json): Goal item promises "nature vocabulary" (see above). Fix: ""Describe a recent day out using the pretérito perfecto with tourism and nature vocabulary."
      ]" -> ""Describe a recent day out using the pretérito perfecto with ya and todavía no."
      ]"
- (a2-03-04.json): Checklist promises "nature vocabulary" (see above); the challenge canDo copies this line. Fix: ""I can describe a recent day out using the pretérito perfecto with tourism and nature vocabulary."" -> ""I can describe a recent day out using the pretérito perfecto with ya and todavía no.""
- a2-03-01-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "ya + perfecto" -> "he / has / ha + participio"; "already + perfect" -> "I have / you have / he or she has + participle"; "todavía no + perfecto" -> "hemos / han + participio"; "not yet + perfect" -> "we have / they have + participle"; "¿Ya has + participio?" -> "¿Has + participio?"; "Have you already + participle?" -> "Have you + participle?"
- a2-03-02-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "¿Ya has + participio?" -> "No, todavía no."; "Have you already + participle?" -> "No, not yet."; "ya + perfecto" -> "¿Ya has + participio?"; "already + perfect" -> "Have you already + participle?"; "todavía no + perfecto" -> "¿Ya han + participio?"; "not yet + perfect" -> "Have they already + participle?"
- a2-03-03-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "¿Ya has + participio?" -> "ya hemos visitado"; "Have you already + participle?" -> "we have already visited"
- a2-03-04-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "¿Ya has + participio?" -> "hemos recordado"; "Have you already + participle?" -> "we have remembered (no marker)"
- a2-03-05-gr.json: table repeats the other Unit 3 screens / shows the wrong pattern. Fix cells: "¿Ya has + participio?" -> "todavía + presente"; "Have you already + participle?" -> "still + present"

### 4. Doubtful
- Unit 3 teaches no grammar (the sheet's "Grammar this unit teaches" is empty): all five screens re-present Unit 1-2 material (ya + perfecto, todavía no, questions with ya) with the same three-row table. I turned each opening into a recap ("You know … from Unit 2") and replaced the table rows, but the unit still has no new point: decide whether to recast it (e.g. perfecto with hoy / esta mañana / este fin de semana vs ayer, which Spain needs) or merge it.
- Heavy repetition inside the unit: a2.03.03 ex03/ex04/ex13 (same sentence three times), a2.03.04 ex02/ex04/ex08/ex12 (explored the market), the "Which pair" item four times across Units 2-3. I varied ex11 (03-03) and ex12 (03-04) only.
- "No, ya." (a2.03.02.ex05, a2.03.consolidation.ex11, a2.02.03.ex05) is an incomplete non-phrase as a wrong option; "No, ya sí" (a2.02.03.ex09) was replaced, these three left (unsure).
- a2.03.05 story and Q: *antes de volver a Hanói* is the Unit 4 form, in the story only (exempt).
- Friends addressed with *ustedes* (*¿Han visto la puesta de sol?* Meg to Carlos): see Unit 2.
- a2.03.01 grammar tip (*Hemos llegado* signals you are still at the pier) is right for Spain but sits beside no perfecto/preterite contrast; fine.

## 5. Dictionary (audit-reader-coverage, stories a2-01, a2-02, a2-03)

Only a2-01 has misses, both place names (no "literal compound guess" words in any of the three stories):

ninh | Ninh | proper noun | Ninh (first part of Ninh Bình, a province and city in northern Vietnam) |
bình | Bình | proper noun | Bình (second part of Ninh Bình) |

a2-02 and a2-03: 0 not in the dictionary, 0 literal compound guess, 0 lookup throws.

## Fix counts

- your-trip: 58 fixes (7 unsure)
- what-you-have-done: 44 fixes (6 unsure)
- day-out: 60 fixes (2 unsure)
- Challenges: 6 per unit (challenges-*.json).
