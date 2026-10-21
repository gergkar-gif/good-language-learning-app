# Reader A report: units 19-21 (es-es A1)

## Unit 19: present-continuous (a1-continuous-01..05, consolidation; story a1-continuous)

Start: 15 errors, 69 suspects. With `fixes-present-continuous.json` applied (tested on a scratch copy): 0 errors, 6 suspects (all accepted below). 55 fixes, tested with `check_fixes.py` (0 rejected). Challenges: `challenges-present-continuous.json` (6).

### 1. Found by reading
- a1.cont.01.ex10: options "Tengo dolor de muelas." / "Ayer fue domingo." give away by length (37 vs 22) and use dolor, muelas, ayer, domingo, sopa, verduras (unmet) -> right "Estoy cocinando arroz con pollo.", wrong "Tengo mucho frío en este momento." / "Mi hermano es muy alto y simpático."
- a1.cont.01.ex11: "¿Puedes hablar un momento?" (puedes: poder is Unit 24) -> "Meg, ¿tienes un minuto?"; option "Ayer estuve estudiando mucho para el examen final." (past tense, ayer, examen, final) -> "Ahora mismo está estudiando, ¿te llamo después?" (second wrong form of estar).
- a1.cont.02.ex03 "una ensalada deliciosa" -> "una ensalada grande"; ex04 "café vietnamita" -> "café en la terraza" (also uses the unused word la terraza); ex05 "un correo electrónico" (A2/B1) -> "un artículo para la clase" (uses the unused word el artículo).
- a1.cont.02.ex10: "un plato de arroz con verduras", "El metro llega a las ocho." (plato, verduras, metro unmet; 50 vs 26 give-away) -> "Sí, estoy comiendo arroz con pollo." / "Tengo mucho frío en la habitación." / "La estación está cerca de la plaza."
- a1.cont.02.ex11: "Escribo cartas en mi cuaderno todos los domingos." is a natural reply to the question (habit answer) and uses cartas/domingos; "un resumen" unmet -> options "Estoy escribiendo una lista de comida." / "Estás escribiendo una lista de comida." / "Estoy escribir una lista de comida."
- Lesson 02 title "Reading & Writing" and goal "eating, drinking, reading, and writing": reading (leer) is lesson 03 -> "Eating, Drinking & Writing"; goal "eating, drinking, writing, and learning".
- a1.cont.03.ex03 "las noticias" (A2) -> "un mensaje"; ex04 "Silencio, por favor; el bebé está" -> "El gato de mi hermana está ___ en el sofá" (silencio, bebé unmet; uses the unused words gato and sofá); ex08 "un libro interesante" -> "una novela interesante" (unused word la novela).
- a1.cont.03.ex06: wrong option "decando" has two faults (stem and ending) -> options "diciendo" / "deciendo" / "decir".
- a1.cont.03.ex10: "Te estamos esperando" (esperando is lesson 05 vocabulary) -> "Estamos en el restaurante."; wrong options "Ayer compré pan." (past, ayer, compré) and "Me gusta el color verde." (gusta is Unit 22), 37 vs 24 give-away; final "!" on the right option only -> "Ya estoy yendo hacia el restaurante." / "Mi padre es alto y trabaja en un banco." / "Mi madre vive en una casa muy grande."
- a1.cont.03.ex11: "¿Podemos hablar con Juan?" (podemos: Unit 24) -> "¿Hablamos con Juan?"
- Lesson 03 goal "spelling changes with double vowels" is wrong (the i sits between two vowels) -> "when an i falls between two vowels".
- a1.cont.04.ex02: option "estoy levantándome" uses a pronoun attached to the gerund, which only the tip of lesson 05 shows -> question "Todos los días yo __ en la oficina." with "trabajo" / "estoy trabajando" / "trabajando".
- a1.cont.04.ex03: "duerme siempre" (tell-absolute) and "¡Silencio!" (unmet) -> "Carlos __ en su habitación ahora mismo." with "duerme todos los días".
- a1.cont.04.ex04: "un zumo de naranja" (naranja unmet) -> "un café". Marked es-es: the es-latam text says "jugo de naranja", so es-latam needs `old` "jugo de naranja" -> "café" and the same `new`.
- a1.cont.04.ex09: tell-absolute "siempre"; and "Carlos trabaja en un banco": Carlos works in an office (a1-15), not a bank -> "Carlos __ en una oficina..." with "trabaja" / "estar trabajando" / "trabajando" (remove `distractor_skills`: both wrong options are ungrammatical).
- a1.cont.04.ex10: "¿a qué te dedicas?" (dedicas unmet), "Soy profesor" (Carlos is not a teacher: Daniela is, a1-03; he works in an office, a1-15), "vacaciones" unmet -> Meg "Carlos, ¿qué haces normalmente por la tarde?"; options "Normalmente estudio español, pero hoy estoy descansando." / "...hoy estás descansando." / "Normalmente estoy estudiando español, pero hoy descanso."
- a1.cont.04.ex11: "Casi siempre... té caliente... ayer tomé té negro" (casi, caliente, negro unmet; ayer past) -> "Sí, siempre, pero hoy estoy tomando té verde." / "...estás tomando..." / "...tomando té verde." (the same word *siempre* in all three, so no tell).
- a1.cont.05.ex02: "Salgo ayer" (a present form with a past time word) and "Estoy salido" -> "Estoy saliendo" / "Estoy salgo" / "Estoy salir"; stays `progressive` (every wrong option is a progressive fault, none a wrong form of salir).
- a1.cont.05.ex08: "Salí ayer." (past, ayer) and "Salgo mañana." (a correct sentence) -> "Estoy saliendo ahora." / "Estás saliendo ahora." / "Estoy salir ahora."; remove the stale `distractor_skills`.
- a1.cont.05.ex06: english "I cannot hear you" for "no te estoy oyendo" -> "I am not hearing you"; sentence now "Hay mucho ruido en la llamada" (uses the unused word la llamada).
- a1.cont.05.ex10: "cierra" (A2) -> "El museo abre a las nueve y está cerca de la plaza."; "llego en cinco minutos" -> "llego pronto" (unused word pronto).
- a1.cont.05.ex11: 42 vs 23 give-away, "el periódico" unmet -> "Estoy tomando café y leyendo un mensaje." / "Es de noche y hace mucho frío aquí." / "Tengo veinticinco años y soy simpática."
- a1.cont.05 grammar screen: example "Estoy saliendo del metro." (metro is A2; it is also the lesson's speaking line) -> "Estoy saliendo del hotel."; example "Te mando un mensaje, estoy conduciendo." (mandar, conducir not in any A1 list) -> "Te llamo luego, estoy cocinando." (unsure)
- a1.cont.cons.ex01: `distractor_skills` {"2": "present-tense"} on "caminan" ("están caminan" is ungrammatical) -> remove.
- a1.cont.cons.ex02 "un café muy agradable" (agradable unmet; also the speaking line and challenge target) -> "muy bonito"; ex04 "tranquilamente" (unmet; also a speaking line) -> "El perro está ___ en el jardín."; ex10 "Hay interferencia." -> "Hay mucho ruido."
- a1.cont.cons.ex03 copies a1.cont.03.ex02 (leer, same options) -> gerund of "pedir": "pidiendo" / "pediendo" / "pido" (`distractor_skills` {"2": "stem-changes"}).
- a1.cont.cons.ex06: the question "¿Cuál oración describe una acción que ocurre en este instante?" is unmet Spanish metalanguage (the unmet-word check does not read multiple-choice stems) -> English question; "Escribí una carta." (past tense, A2), correo/carta unmet -> "Estoy escribiendo un mensaje." / "Escribo mensajes los viernes." / "Estoy escribir un mensaje."
- a1.cont.03.ex02, ex09: stems "¿Cuál es el gerundio correcto del verbo \"leer\"?" / "del verbo \"ir\"?" use unmet metalanguage (verbo, correcto) -> "¿Cuál es el gerundio de \"leer\"?" / "de \"ir\"?"
- a1.cont.cons.ex11: 44 vs 24 give-away; casi, dolor, estómago, ayer unmet; "Hace viento ayer." -> "Un momento; me estoy poniendo los zapatos." / "...me estás poniendo..." / "...me poniendo..."
- a1.cont.cons.ex12: "¿Qué hace la gente en la plaza?" also takes a simple-present answer (habit), and gente, otros, árboles are unmet -> "¿Qué están haciendo los chicos en la plaza?" / "Dos chicos están bailando y tres están tomando fotos." / "Dos chicos bailan y tres toman fotos todos los días." / "Dos chicos son bailando y tres son tomando fotos."
- a1.cont.cons.ex13: prompt "They are eating lunch." but the stored answer has no "lunch" -> "They are eating."
- Writing items (all six lessons, ex12/ex13): prompts such as "Say: 'I am studying.'" also fit "Estudio." -> "Say (happening now): ..." (unsure; a1.cont.03.ex12 second prompt: "Say with estar + a gerund: 'I am going to the park.'", since "Voy al parque" fits).
- Grammar 01 does not recap estar -> "Spanish uses **estar** (you know it from Unit 9) followed by the gerund". Grammar 04 does not say the simple present is known -> "You know the simple present from Unit 7 ..." (unsure).
- Story a1-continuous: `keyVocabulary` conocer/intercambio are placeholders (not in the story) -> cocinar / terraza.

### 2. Metadata
- a1.cont.01.ex11, a1.cont.03.ex11: wrong options are wrong forms of estar -> `teaches` ["estar"] (was the unit vocabulary skill).
- a1.cont.02.ex11, a1.cont.04.ex10, a1.cont.04.ex11, a1.cont.cons.ex11, a1.cont.cons.ex12: wrong options fail on the progressive -> ["progressive"].
- a1.cont.04.ex12 (structured writing contrasting present and progressive): vocabulary skill -> ["progressive"] (unsure).
- a1.cont.04.ex09, a1.cont.05.ex08, a1.cont.cons.ex01: remove `distractor_skills` (ungrammatical or stale).
- No salgo/present-irregular-yo retag needed: after the fix no wrong option in a1.cont.05.ex02 or ex08 is a wrong form of salir.

### 3. Goals / checklists
- Lesson 02 goal (reading) and title: see above. Lesson 03 goal (double vowels): see above.
- Lesson 04 checklist "I know when to use the simple present..." is not a can-do line -> "I can tell when to use the simple present and when to use the present continuous." (the challenge `canDo` uses the new wording).

### 4. Doubtful
- "Estoy yendo" / "Ya estoy yendo hacia..." (a1.cont.03.ex05, ex10, ex12, cons.ex07, grammar 03): *ir* + gerund sounds unusual in Spain (*Ya voy*, *voy de camino*); it is taught as a gerund form, so left (unsure).
- Grammar 04 tip: "¿Qué haces? can mean What do you do (for a living)?" (in Spain ¿A qué te dedicas? is the job question) (unsure, no fix).
- Story a1-continuous: narration says Meg reads "a magazine", Meg says "un artículo de viaje" (unsure, no fix).
- Participles *caminado*, *esperado* as wrong options (a1.cont.01.ex02, 05.ex05) are A2 forms; left as one-fault real forms.
- Accepted suspects: the non-word wrong options *caminiendo*, *pediendo*, *aprendado* (one fault each: wrong gerund ending or stem), vocab-unused *dormir* and *oír* (used only as the irregular gerunds *durmiendo*, *oyendo*), *la diferencia* (a label word of the screen). Character "Juan" (a1.cont.03.ex11) left alone.
- es-latam: only a1.cont.04.ex04 needs its own text (see above); no other fix holds only in Spain.

### 5. Dictionary
None: the audit for story a1-continuous reports 0 words not in the dictionary and 0 literal compound guesses.

Fix count unit 19: 55 (55 tested clean).

## Unit 20: health (a1-health-01..05, consolidation; story a1-16)

Start: 0 errors, 5 suspects. With `fixes-health.json` applied (tested on a scratch copy): 0 errors, 0 suspects. 45 fixes, `check_fixes.py` 0 rejected. Challenges: `challenges-health.json` (6).

### 1. Found by reading
- a1.health.05.ex10: "Me duele la cabeza." (doler is Unit 21; *duele* is a form before its screen) and "aspirina" (unmet) -> Carlos "Tengo dolor de cabeza. ¿Qué hago?", options "Toma la medicina." / "Tomo la medicina." / "Toman la medicina." The infinitive "Tomar una aspirina." was also a natural piece of advice (an answer to ¿Qué hago?), and "Tomas una aspirina." too.
- a1.health.05.ex11 / ex16 / ex17 / ex18 / ex19 and a1.health.06.ex15: the infinitive options ("Descansar y tomar agua.", "Tomar agua.", "Ir al médico.", "Descansar y dormir bien.") are normal spoken or written advice, so a second right answer (same finding as the Unit 14 recipes) -> replaced with yo / 3rd-plural forms ("Descanso y tomo agua.", "Descansan y toman agua.", "Tomo agua.", "Descanso y duermo bien."); `distractor_skills` updated. (`Descansas y tomas agua.` can also be a colloquial instruction: kept in ex16/ex17 because the question says "command" / translation; left as unsure.)
- a1.health.06.ex15: speakers reversed: the doctor says "¿Qué hago?" and the patient gives the advice -> Paciente "¿Qué hago?" / Médico gives it; options varied so the item no longer copies a1.health.05.ex11.
- a1.health.05.ex05: "Drink water." with answer "Toma" also fits "Bebe agua." (beber is Unit 7) -> hint "tomar, tú". ex12 second prompt gets "(use tomar)"; a1.health.06.ex18 "Give two simple pieces of health advice." does not pin its stored answer -> "Tell someone to rest and drink water (use tomar)."; a1.health.06.ex17 "Say that you have two symptoms." -> "Say that you have a fever and a cough."
- Copies and near-copies (shape repeated within a lesson): a1.health.01.ex16 = ex04 (identical options) -> "Mi madre está enferma."; a1.health.02.ex16 ~ ex09 -> "Which means 'Do you have a fever?'"; a1.health.03.ex13 = a1.health.02.ex13 -> "Ella tiene tos."; a1.health.03.ex17 = dialogue ex10 -> "¿Tienes gripe o un resfriado?"; a1.health.04.ex16 ~ ex06 -> "Tengo una cita con el médico."; a1.health.04.ex17 ~ ex11 -> "¿Desde cuándo tienes fiebre?"; a1.health.05.ex13 = ex09 -> "Come algo."; a1.health.05.ex18 = ex06, ex19 ~ ex07/ex11 -> new advice items. check-content copies: a1.health.06.ex02 (copy of a1.health.04.ex02) -> "appointment" / cita; a1.health.06.ex16 (copy of a1.health.01.ex10) -> Carlos "¿Cómo estás, Meg?" / "Estoy cansada y tengo tos."
- Garbled wrong options with two verbs: a1.health.02.ex17 "Tengo tos y tengo está fiebre.", a1.health.03.ex09 / ex10 "Tengo fiebre está tos.", ex16 "Tengo dolor de cabeza está fiebre.", ex17 "Hay tos y tengo." -> real one-fault options ("Hay tos y fiebre.", "Tengo fiebre y soy tos.", "Hay fiebre y tos.", "Hay dolor de cabeza y fiebre.").
- Grammar 03: the table repeats the lesson 02 table row for row -> five new rows (symptom pairs, *gripe*, *un resfriado*).
- Recaps missing: grammar 01 ("You know *estar* from Unit 9 and *tener* from Unit 5"), grammar 02 ("You know *tener* from Unit 5"), grammar 05 ("You know affirmative *tú* commands from Unit 14 and *ve* from Unit 16").
- Story a1-16 (stories are exempt from met words, not from the level): preterite "fuiste", "fui", "recetó", "dijo" (A2), subjunctive "cuides", "Que te mejores" (B1), "voy a dormir" (ir a, Unit 25), and "¿Cómo te sientes del cuerpo?" (unnatural) -> present-tense rewrite of four lines (Meg "¿Tienes cita con el médico?", Carlos "Sí, tengo cita en la clínica por la tarde. Hoy tomo esta medicina y debo descansar.", "Muchas gracias por venir. Me tomo la medicina y duermo un rato.", Meg "Descansa mucho, amigo. Hasta pronto."); comprehension question 2 "¿Qué le recetó el médico a Carlos?" (preterite) -> "¿Qué debe hacer Carlos hoy?" (same options, new explanation); question 3 options in the subjunctive ("Que beba agua, duerma muchas horas y deje el trabajo por hoy") -> infinitives. All 11 story fixes are unsure; the audio must be re-narrated after the text change.

### 2. Metadata
- No tag changes needed after the fixes. Checked: `distractor_skills` kept where the wrong option is a well-formed form of another skill (descansas, vas, duermes); re-set on every changed option of a1.health.05 and a1.health.06.ex15. a1.health.04.ex09 (which question asks about the problem) stays vocabulary.

### 3. Goals / checklists
- Consolidation goal and checklist line "give basic advice using cumulative A1" -> "using what I know from A1".
- Checklist lines of lessons 01-05 ("Name basic body and health vocabulary.") are imperatives, not "I can" lines; left as they are in the other older units (the challenge `canDo` copies them).

### 4. Doubtful
- Doctor and patient use tú ("¿Qué tienes?") in lessons 04-06: a doctor in Spain says *usted* (A2): left (unsure).
- Structured writing "Say that you are tired." stores *cansado* only; a woman learner writes *cansada* (unsure; no fix).
- "¿Qué tienes?" for "What's wrong?" (usual: *¿Qué te pasa?*): acceptable, left.
- Story metadata: `location` "Centro médico en Hanói" while Meg visits Carlos at home (unsure, no fix).
- a1.health.05.ex15 flagged `medicine` (an English option) as unmet: false positive, accepted.
- *clínica* in a1.health.06.ex12 passes the checker; left.

### 5. Dictionary
None: the audit for story a1-16 reports 0 words not in the dictionary and 0 literal compound guesses.

Fix count unit 20: 45 (45 tested clean).

## Unit 21: what-hurts (a1-doler-01..05, consolidation; story a1-doler)

Start: 9 errors, 33 suspects. With `fixes-what-hurts.json` applied (tested on a scratch copy): 0 errors, 4 suspects (all accepted below). 45 fixes, `check_fixes.py` 0 rejected. Challenges: `challenges-what-hurts.json` (6). The screens never call *doler* "like *gustar*" (checked); no *gusta* outside two wrong options (fixed).

### 1. Found by reading
- a1.dol.02.ex10: 35 vs 22 give-away; "Tengo diez lápices." (lápices unmet), "Mañana voy a estudiar." (ir a + infinitive, Unit 25) -> options "Me duele mucho el hombro izquierdo." / "Tengo una hermana y un hermano." / "Vivo en Hanói y trabajo en una oficina." (Carlos: one brother and one sister, Hanoi, office job).
- a1.dol.02.ex11: 38 vs 24, "Compramos manzanas ayer." (ayer, compramos) -> prompt "¿Qué le duele a su hijo?" (the old word order is unnatural), options "Mi hijo tiene nueve años y es muy alto." / "Vivimos cerca del centro y de la plaza."
- a1.dol.03.ex06: tell-absolute "ninguno", and "No me duelen ninguno." has two faults -> "No me duele nada." / "No me duele algo." / "No me duele mucho."
- a1.dol.04.ex08: 36 vs 26 give-away -> wrong options "¿Tiene algo con el dolor de cabeza?" / "¿Tiene algo por el dolor de cabeza?" (one preposition fault each).
- a1.dol.04.ex10: 40 vs 22; "No me gusta la música." (gusta, Unit 22), "Son las tres." -> "Sí, este jarabe es para la garganta." / "Son las tres y media de la tarde." / "Mi hermano vive cerca de la plaza."
- a1.dol.05.ex10: 48 vs 25 -> "Me recupero bien, gracias. Ya no me duele la espalda." (uses recuperarse) / "Mi madre vive en Budapest y es muy amable." / "Trabajo en una oficina y vivo en Hanói."
- a1.dol.05.ex11: "Me gusta el helado de fresa." (gusta, helado, fresa), "Son las cinco de la tarde." -> "Tienes que cuidarte; ve al dentista hoy mismo." (uses cuidarse) / "Mi hermana tiene un gato muy grande." / "Hoy hace mucho calor y no hay nubes."
- a1.dol.cons.ex11: 43 vs 24, "Ayer comí arroz.", "El tren sale a las diez." -> "Mi madre vive en Budapest y es muy amable." / "Hoy hace mucho calor y no hay nubes."
- Usted commands (A2, `imperativo-formal-usted`) in A1: a1.dol.04.ex04 "Tome una pastilla con agua.", ex11 "Tome una pastilla cada ocho horas después de comer." (with *debo*, *cuestan*, *euros* unmet), a1.dol.cons.ex10 "Tome estas pastillas con un vaso de agua.", and the grammar 04 example (also the lesson's speaking line) -> *hay que* + infinitive (Unit 18): "Hay que tomar una pastilla cada ocho horas con agua."; ex11 "¿Cuántas pastillas tomo?" / "Hay que tomar una pastilla cada ocho horas." / "Hay tomar una pastilla cada ocho horas." / "Tomo una pastilla cada ocho horas." (tag `hay-que`).
- *poder* forms before Unit 24: a1.dol.03.ex02 "casi no puedo caminar" (also casi, in no list), ex13 "pero puedo trabajar", a1.dol.cons.ex12 "¿En qué puedo ayudarle?" -> "Me duele __ la espalda y necesito descansar." / "pero trabajo" / "Buenos días, ¿qué necesita?". Note for the knowledge sheet: it lists `querer-poder` as known from a1-08-03-querer-gr, but that screen teaches only *querer* (no *puedo/puedes/podemos*; they are a1-abilities-01). The same applies to a1.cont.01.ex11 and a1.cont.03.ex11 (fixed above). *In a1.dol.01.ex07 "No puedo comer..." is left: the lesson's own grammar example has "No puedo leer bien".*
- Unmet words: a1.dol.01.ex03 *paseo* -> "Después de caminar me ___ los pies."; ex08 *pantalla* -> "Me duelen los ojos después de leer."; a1.dol.03.ex04 (stem "Siento que la habitación da vueltas", contento, ocupado) -> 'Which word means "dizzy"?' mareado / cansado / enfermo; ex10 *todavía*, *rápido*, ex11 *veo*, *pálida* -> "¿te duele el pie hoy?" / "Solo me duele un poco cuando camino." and "¿Tienes calor?"; a1.dol.04.ex05 *helado* -> "un libro"; ex09 *farmacéutico* -> "El médico me recomienda descansar dos días."; a1.dol.cons.ex01 *cargar*, *maletas*, and *duela* (subjunctive, A2) -> "después de trabajar" with options duele / duelen / duelo; ex02 *tanto* -> "después de caminar" (also the lesson's speaking line); ex07 *fuerte* -> "Tengo mucho dolor de cabeza."; grammar 01 examples *desde ayer* and *caminar tanto* (the first and second speaking lines) -> "desde esta mañana", "Después de caminar,".
- Spanish metalanguage in multiple-choice stems (the unmet-word check does not read stems): a1.dol.01.ex04 "¿Cuál opción es correcta para las piernas (plural)?", ex09 "Con sustantivos en plural ... se usa:" -> English questions.
- a1.dol.cons.ex06: options "mareada mente" (garbled) and "marear", and the stem allows "mareada" -> "Carlos está un poco __ por el calor." with mareado / mareada / mareados (tag `adjective-agreement`).
- a1.dol.cons.ex09: "¿Dónde tienes dolor tú?" is a natural second right answer; "¿Qué te duele dónde?" garbled -> "¿Dónde me duele?" / "¿Dónde te duelen?"
- a1.dol.cons.ex04 copies the lesson 02 table row and a1.dol.02.ex04 -> "A mi madre ___ duelen las rodillas." (answer *le*; also the second speaking line).
- a1.dol.02.ex01: "el oído" / "ear" is ambiguous with *la oreja* (unused) -> pair "la oreja" / "outer ear".
- Grammar 03: the table presents *estoy cansado / enfermo* (Unit 20) as new -> tip opens "You know *estoy cansado* and *estoy enfermo* from Unit 20; *mareado* and *resfriado* are new." Grammar 05 presents *tener dolor de* (Unit 20) as new -> "You know *tengo dolor de cabeza* from Unit 20 and *me duele la cabeza* from this unit."
- Writing items: a1.dol.03.ex12 / a1.dol.cons.ex13 do not pin gender or verb ("I feel dizzy" / "I feel sick") -> "(you are a man)", "(use estar)" (unsure).
- Story a1-doler: Meg "Vamos a entrar para pedir..." is *ir a* + infinitive (Unit 25) -> "Entramos para pedir una pastilla y agua fresca." (and the explanation of comprehension question 2); unsure; audio must be re-narrated. Reading questions are answerable from the story.

### 2. Metadata
- Dialogues whose wrong options differ in the form of doler: a1.dol.01.ex10, ex11, a1.dol.03.ex10, a1.dol.cons.ex12 -> `teaches` ["doler"] (was the unit vocabulary skill). a1.dol.03.ex11 (wrong options "Estar..." / "Estás...") -> ["estar"]. a1.dol.04.ex04, ex11 -> ["hay-que"]. a1.dol.cons.ex06 -> ["adjective-agreement"].
- a1.dol.04.ex02 ("¿Tiene algo __ el dolor de cabeza?" para/por/de) is tagged vocabulary but tests a preposition (por/para is A2): left (unsure).

### 3. Goals / checklists
- No change: goals and checklist lines match what each lesson practises. Lesson 04's goal "Understand basic instructions: tomar una pastilla con agua." is now met by *hay que tomar*.

### 4. Doubtful
- a1.dol.03.ex02: "poco" as a wrong option is wrong by meaning only (rule 2.2); no single-fault alternative (unsure, left).
- a1.dol.03.ex03 "Meg es mujer; ella dice: ..." is a clumsy way to pin the gender; left (works, no error).
- Grammar 02's tip "add *a* at the start" (*A María le duele...*) is the indirect-object *a*, not the personal *a* (Unit 24): correct, but a learner may confuse them (unsure).
- Story paragraph 6 ("Entran en la farmacia pequeña...") is Spanish narration while paragraph 0 is English narration (unsure; no fix).
- Accepted suspects: vocab-unused *doler* (used as the forms *duele/duelen*), *sentirse* (used as *me siento*), *recomendar* (used as *recomienda*), *el cuerpo* (no natural sentence at this level; screen label).
- es-latam: no fix holds only in Spain (no *zumo*, *vosotros*, *coche*, *ordenador* touched).

### 5. Dictionary
None: the audit for story a1-doler reports 0 words not in the dictionary and 0 literal compound guesses.

Fix count unit 21: 45 (45 tested clean).

## Totals and process notes
- Fixes: unit 19: 55, unit 20: 45, unit 21: 45 (all tested with `scripts/check_fixes.py`, 0 rejected; applied to a scratch copy: 0 errors in all three units).
- The unmet-word check does not read multiple-choice question stems, so Spanish metalanguage and unmet words in stems (*silencio*, *oración*, *sustantivos*, *casi*, *puedo*, *cargar*) were found by reading only.
- Non-word wrong options (*diciando*, *salendo*, *pidando*) bring a new `unmet-word` finding and are rejected by `check_fixes.py`; real forms (*deciendo*, *decir*, *Estoy salir*, *pido*) pass.
