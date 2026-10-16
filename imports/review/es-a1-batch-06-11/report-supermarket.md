# Report: A1 Units 9-11 (es-es)

## UNIT 9 supermarket (a1-08-*): 40 fixes in fixes-supermarket.json

### 1. Found by reading
- a1.08.01.ex10: dialogue "¿Qué quieres comprar?" uses unmet quieres (a1-08-03) and comprar (a1-20-01); fix: "Carlos: ¿Qué hay en la cocina?", options Hay una manzana. / Hay un manzana. / Hay unas manzana.
- a1.08.01.ex11: "¿Qué hay en la lista?" lista first taught a1-08-05; right option had no article, wrong options "Hay unos pan y unas leche." two faults; fix: "¿Qué hay en la mesa?" / Hay un pan y unos tomates. / Hay una pan y unos tomates. / Hay unos pan y unos tomates.
- a1.08.01.ex04, ex09: "unos manzana", "unos botella" have two faults (number and gender); fix: "unas manzana", "unas botella". ex06: "una" (gender+number) -> "un".
- a1.08.01.ex14: "Necesito __ leche." english "I need a carton of milk" ("una leche" is not natural Spanish); fix: "Necesito __ tomate." / un / "I need a tomato."
- a1.08.02.ex04, a1.08.05.ex06: answers list includes siete, nueve (first taught a1-10-02) and contradicts english "two"; fix: answer dos only.
- a1.08.02.ex05: "una"/"un" fail the same way (singular before plural); fix options cuatro / un / unas.
- a1.08.02.ex09: "tres tomatos" non-word in no vocab list; fix: "dos tomates". ex16 "tres botellos" non-word, and "Which is correct?" would not pin a real replacement; fix: question "five bottles", options cinco botellas / cinco botella / dos botellas. a1.08.04.ex13 same ("botellos"): question "We need two bottles", third option "Necesitamos tres botellas."
- a1.08.02.ex10, ex11: prompts use unmet quieres (a1-08-03) and necesitas (a1-08-04); fix: "¿Cuántas manzanas hay?", "¿Cuánto arroz hay?".
- a1.08.02.ex17: answer "kilo" copied from the question; fix: ask about "diez".
- a1.08.03.ex11: "¿Qué quiere Ana?" Ana is no character of the stories; fix Daniela (unsure).
- a1.08.05.ex03, ex04, consolidation ex12/ex19: comprar (a1-20-01) unmet; replaced (pagar/necesitar/querer; "Quiero dos."; "Mi hermano necesita pan."; ex19 "_____ dos botellas de agua.").
- a1.08.05.ex12: "¿Vamos a la caja?" / "Sí, vamos a pagar." is ir (Unit 16) and ir a + infinitive (Unit 25), plus todo unmet (a1-cafe-04); fix: "¿Dónde pagamos?" / Pagamos en la caja. / Pagan... / Pagas...; teaches ar-verbs.
- a1.08.05.ex13 and vocab: "Voy a pagar" (ir a + inf., Unit 25) and voy "I go (from ir)" in a1-08-05-voc; fix: "Pago en la caja." and remove voy from the vocabulary list.
- a1.08.05.ex19: right answer repeats ex04/ex09 ("Quiero dos manzanas."); fix: "I want five tomatoes".
- a1.08.05.ex14, ex16: length give-aways (errors); lengthened wrong options. ex15 "What happens first? They start with a shopping list": story opens with walking in; ex18 "Shopping list -> supermarket -> checkout": they are already in the supermarket. Fixed to bread and milk first / order of purchases.
- a1.08.06.ex02, ex05: copies of a1.08.02.ex02, a1.08.03.ex02; varied ("list", "Mi hermano").
- a1.08.06.ex03: "una"/"un" fail alike; "dos/una/unos". ex04: "unos leche"/"unas leche" fail alike and "no article" untaught; fixed to "Necesito __ pan." un/una/unos.
- a1.08.06.ex17: two prompts copy a1.08.02.ex12 / a1.08.05.ex13; varied. ex18: "Give a short shopping request using querer, necesitar and a quantity." does not pin the stored answer; pinned.
- a1.08.06.ex20: "cuestan" (costar, a2-porpara-04), teaches stem-changes; also speaking prompt "¿Cuánto cuestan las manzanas?" comes from it. Fix: "¿Qué _____ ustedes?" / necesitar / necesitan, teaches ar-verbs.
- No past tense, clock time or gusta found in this unit. Numbers: dos/tres (Unit 5), seis/ocho (Unit 6) met; cuatro, cinco, diez are taught in a1-08-02 vocabulary (a "numbers" lesson before a1-10-02: see 4); siete, nueve removed. No prices appear (all "price" talk is only in the old challenge text).

### 2. Metadata
- a1-08-02-voc: uno, dos have pos "adverb"; fix: "number".
- Story a1-08.json (id story.a1.09): pedagogical.keyVocabulary is the course-wide placeholder (conocer, intercambio); fix to paquete / carrito (unsure).
- Existing challenge screens for a1-08-01..05 and consolidation are generic ("ask about the price") and a1-08-02's is a stub ("Put your Spanish skills into practice"); six new entries in challenges-supermarket.json.

### 3. Goals / checklists
- Goals and checklists are identical per lesson and distinct across lessons; no defect. a1-08-03 grammar screen says "forms are irregular" without linking to Unit 7 stem-changing: fix adds "You know stem-changing verbs from Unit 7: ... e to ie" (unsure).

### 4. Doubtful
- a1-08-02 teaches cuatro, cinco, diez (and uno/dos/tres) in its vocabulary before `numbers` (a1-10-02, Unit 12); their exercises are tagged `plural` / `gender` (no number skill fits yet).
- Lesson "querer-poder": poder is not taught anywhere in the unit; the screen tip says infinitive "later", yet the consolidation used querer + infinitive (removed).
- Story: Carlos wants "un kilo de tomates", Meg later says "Ya tenemos cuatro tomates"; exercises 08-05 ex11 ("cuatro tomates") follow it. Changing the line would desync the audio (left alone).
- a1.08.04.ex11: Daniela answers about Carlos, but Daniela is not in the shopping story (unsure).
- a1.08.06.ex10 "Mi madre está amable." is acceptable Spanish in some uses (unsure).
- Many identical "Which is correct?" items per lesson (a1-08-01 ex04/09/16).

### 5. Dictionary
(audit: 0 not in the dictionary, 0 literal compound guesses)

## UNIT 10 demonstratives (a1-demonstrative-*): 89 fixes in fixes-demonstratives.json

All 8 errors and 75 suspects are fixed: applied to a scratch copy, check-content gives 0 errors, 0 suspects. Almost every item was written with adult vocabulary; the fixes keep each item's skill and swap in met words (este/ese/aquel forms, tener, querer, necesitar, hay, bonito, grande, caro/barato, casa, libro, bolsa...).

### 1. Found by reading
- Grammar examples (and the speaking steps that read them) use *gusta* (Unit 22) in 01 "Me gusta este café.", 04 "No me gusta esto.", 05 "¿Te gusta esta taza?"; *cuestan/cuesta* (a2-porpara-04) in 01 and 05 table "¿Cuánto cuesta este?"; imperatives and *poder* (Units 13/-) in 02 "¿Puedes pasarme ese libro?", 03 "Mira aquel edificio antiguo allí.", 04 "¿Puedes explicarme eso otra vez?"; *quedar* (A2) in 02 "te quedan bien"; *ver + a personal* in 03; comparative *más cómodos que* (a2-06-01) in 05. Replaced by Quiero este libro. / Esta manzana es muy grande. / Estos pantalones son nuevos.; Quiero ese libro. / Esos pantalones son muy bonitos. / Quiero esas manzanas de ahí.; Aquel edificio es muy grande. / Aquella torre es muy alta. / Aquellos puentes... / Aquellas casas...; ¿Qué es esto? Es una llave. / Eso es muy interesante. / Esto es muy importante.; ¿Quieres esta bolsa? No, prefiero aquella. / Estos zapatos son grandes y esos son pequeños. / ¿Es caro este?
- a1.dem.04.ex11: "He aprobado el examen de español." is the present perfect (a2-01-01, past tense at A1); replaced by "Hanói es una ciudad muy grande." / "Sí, eso es verdad."
- Comparatives/superlatives: a1.dem.05.ex07 "más bonitas que esas" (A2), a1.dem.cons.ex10 "el más largo" (B1); goal of lesson 05 "Compare prices and features" promises it. Fixed to y-sentences, "Aquel puente es muy grande.", goal "Say whether an item is cheap or expensive using demonstratives."
- Numbers and clock time as wrong options: "Tengo veinticinco años" (01.ex10), "Son las tres" (01), "Son las cinco de la tarde" (03.ex10), "Son las ocho" (05.ex10), "El tren sale a las nueve" (cons.ex11), "Me ducho a las siete" (02.ex11): removed with the dialogues rewritten. "Mañana" is fine.
- All dialogues (a1.dem.01.ex10/11, 02.ex10/11, 03.ex10/11, 04.ex10/11, 05.ex10/11, cons.ex11/12) used off-topic wrong replies (length give-away errors in 01.ex10/11, 03.ex10/11, 04.ex11, 05.ex10, cons.ex11) and unmet words (sombrero, queda, dólares (euros in Spain), nadar, teatro, ópera, gustan, colores, paraguas, biblioteca, postre, tradicional, vietnamita, maravillosa, noticia, examen, bufanda, hermosa, compremos, mangos, melones, frescos, precioso, fiebre, tren). Rewritten as form items: one demonstrative fault per wrong option, teaches `demonstratives`.
- 03.ex04: length give-away and "mi / tu" off topic; now "aquel / este / ese". 03.ex09 "otro" (b1-23-02): replaced.
- Spanish instructions with grammar words for an English-only learner (01.ex02, 02.ex04, 03.ex02, cons.ex01, cons.ex06: "sustantivo masculino singular", "pronombre neutro", "demostrativo corresponde"): English prompts.
- Unmet nouns/adjectives in drills (tienda, buenos, cómodos, dulces, famoso, iglesia, antigua, montañas, hermosa, mano, mí, nada, azul, roja, paja, taza, vitrina, flores, huelen, cuadernos, fruta, largo, mira): replaced item by item.
- a1.dem.02.ex10 (new): Carlos asks about "esa bolsa", Meg answers "Esta bolsa..." (same bag, near her), which shows the este/ese contrast; a1.dem.03.ex08 builder now "Aquel coche es muy grande."
- a1.dem.cons.ex13 / ex-"Point out this book (here)." did not pin the stored sentence; pinned ("Say that this book is here.").
- No Unit 9 material is presented as new; nothing in Unit 9 drills este/ese/aquel (checked). The unit's vocabulary lists unused words (aquí, el precio, caro, ahí, el cuadro, la verdad, el puesto, el regalo): the rewritten items now use each.

### 2. Metadata
- Dialogues were tagged `a1-demonstratives-vocab`; rewritten as form items, now `demonstratives`.
- Story a1-demonstrative.json: keyVocabulary is the placeholder (conocer, intercambio); fix to puesto / seda (unsure).
- Existing challenge screens are generic ("Put your Spanish skills into practice...", truncated titles); six new entries in challenges-demonstratives.json.

### 3. Goals / checklists
- a1-demonstrative-consolidation goal and checklist line 3 "in shopping and spatial navigation contexts": the unit has no navigation (Unit 16); reworded in both places.
- a1-demonstrative-05 goal 3 reworded (see above). Lessons 01-05 have one checklist line against two or three goals (acceptable).

### 4. Doubtful
- a1.dem.cons.ex06 ("Eso es muy interesante." / "Eso libro es..." / "Eso casa es...") two wrong options fail the same way (neuter before a noun); left as it tests exactly that (unsure).
- a1.dem.01.ex06 / 05.ex02 keep non-word wrong options (*estes*, *eses*) as single-fault non-words.
- a1.dem.05 grammar tip about the RAE and accent marks is heavy for A1 (unsure).
- Lesson 04 grammar tip is written in capitals ("CRITICAL RULE").
- L3 ex06: "Estas casas están muy lejos" as a wrong option is wrong by meaning rather than form (unsure).

### 5. Dictionary
(audit: 0 not in the dictionary, 0 literal compound guesses)

## UNIT 11 ordering-cafe (a1-cafe-*): 34 fixes in fixes-ordering-cafe.json

All 7 errors and 9 suspects are fixed: applied to a scratch copy (after rebuilding word-lesson-index), check-content gives 0 errors, 0 suspects.

### 1. Found by reading
- a1.cafe.04.ex11 and a1.cafe.05.ex11: wrong option "Son las tres." is clock time (telling-time, Unit 14); "Sí, gracias. Eso es todo." contradicts itself; the two items were identical. Fix: 04.ex11 becomes an article item (Camarero: "¿Quiere un café o un té?" / Un té, por favor. / Una té... / Unos té...), teaches gender; 05.ex11 "Son las tres." -> "Como un sándwich."
- a1.cafe.05.ex16: the marked right answer is "Tacos." but the story has a salad, a chicken sandwich and chocolate cake. Fix: "What does Meg order to eat?" / A salad and a sandwich. / Tacos and rice. / An apple and bread.
- a1.cafe.05.ex15 "What does the customer order first? A drink.": Meg orders tea, salad and sandwich in one line; fits nobody. Fix: "What does Meg order to drink?" / A green tea. / A black coffee. / A mineral water.
- a1.cafe.05.ex17 "What does the waiter ask after the order?": the waiter never speaks in the story; Meg asks Carlos "¿Quieres algún refresco o jugo también?". Also length give-away ERROR. Fix: "What does Meg ask Carlos at the end of the order?" / If he wants a soft drink. ...
- a1.cafe.05.ex18 "The customer thanks the waiter and finishes the order.": Carlos asks for the bill and Meg thanks Carlos, not the waiter; length give-away ERROR. Fix: "How does the visit end?" / Carlos asks for the bill. / Meg asks for the bill. / They order more coffee.
- Story a1-02 (es-es): "¿Quieres algún refresco o jugo también, Carlos?" -> "zumo" (variant es-es). "¿podemos ordenar?" -> "¿podemos pedir?" (variant es-es, unsure).
- Vocabulary a1-cafe-04 "ordenar = to order": in Spain ordenar means to tidy; ordering is pedir. Fix: vocab entry "pedir = to order / ask for" and matching a1.cafe.04.ex01 pair (variant es-es, unsure; check_fixes rejects it only because word-lesson-index is stale, so rebuild the index after applying).
- Garbled non-phrases as wrong options: a1.cafe.03.ex16 "Quiero café un, por favor."; 04.ex15 "Quiero café por." / "Por favor quiero un."; 05.ex05 "Quiero un café por." / "Café quiero un." (length ERROR); cons.ex06 "Quiero un café por." / "Café quiero." (length ERROR). Replaced by one-fault options (una café / Quieres...), varied nouns (café, sándwich, ensalada, té).
- a1.cafe.04.ex04 length ERROR (29 vs 15): wrong options now "Quiero un café, por favor." / "Quiero un té y un sándwich." 04.ex09 length ERROR (25 vs 12): "Sí, quiero un té también." / "Sí, un café más, por favor."
- a1.cafe.01.ex15 length ERROR (10 vs 6): options soft drink / hot coffee / green tea.
- a1.cafe.05.ex09: wrong options "¿Desea algo más para tomar hoy?" / "Eso es todo lo que tenemos hoy." use unmet desea (A2), hoy (a1-weather-03); replaced with met-word replies.
- a1.cafe.05.ex12: "Sí, ahora mismo." mismo first taught a1-continuous-01; fix "Sí, aquí tiene la cuenta."
- a1.cafe.06.ex20: "Ella _____ un bocadillo en la barra." bocadillo, barra in no vocabulary list; fix "Mi hermana _____ un sándwich en el café." (speaking step reads it).
- a1.cafe.06.ex03, ex04, ex14: copies of 01.ex04, 02.ex04, 04.ex10; varied (Nosotros __ agua; Ella __ una ensalada; té y una ensalada).
- a1.cafe.06.ex18 "Give a short café order using at least three target verbs." does not pin the stored answer; pinned. a1.cafe.05.ex13 "Greet the waiter" does not pin buenas tardes; added "(good afternoon)".
- a1.cafe.01.ex11, 02.ex11, 03.ex09: "¿Qué toma/come/quiere Ana?" Ana is no character of the stories; Daniela (unsure).
- No past tense or gusta in the unit; numbers only dos/tres (met).

### 2. Metadata
- a1.cafe.04.ex11 now teaches `gender` (was `a1-ordering-cafe-vocab`). The tag changes in all three units (a1.08.05.ex12, a1.08.06.ex20, the Unit 10 dialogues, a1.cafe.04.ex11) hit locked tags: run scripts/lock_tags.py with a reason when applying (validate-content fails otherwise).
- Story a1-02.json: keyVocabulary placeholder (conocer, intercambio); fix to camarero / cuenta (unsure).
- Existing challenge screens are generic ("You are at a café in Madrid", "Put your Spanish skills into practice"); the story is in Hanoi. Six new entries in challenges-ordering-cafe.json.

### 3. Goals / checklists
- a1-cafe-03 grammar: "You've already met *querer*" -> "You know *querer* (to want) from Unit 9."
- a1-cafe-01 / 02 grammar: "It is a regular -ar/-er verb" -> "You know regular -ar/-er verbs from Unit 6, and *tomar*/*comer* is one of them." (unsure)
- a1-cafe-03 vocabulary lists más but nothing used it; ex14 now asks "¿Qué significa "más"?".
- Goals and checklists otherwise distinct and fine.

### 4. Doubtful
- a1.cafe.06.ex09/ex10 ("Tengo dos hermanos", "Mi madre está amable") are the same items as a1.08.06.ex09/ex10 in Unit 9's consolidation; "Mi madre está amable." can be acceptable Spanish.
- Story: "¿podemos ordenar?" and "jugo" changes desync nothing structural but the story audio may need regenerating.
- a1.cafe.01.ex14 / 02.ex14 / 03.ex12 English "You drink/eat/want..." for ustedes does not show the plural.

### 5. Dictionary
(audit: 0 not in the dictionary, 0 literal compound guesses)

Fix count: Unit 9 supermarket 40, Unit 10 demonstratives 89, Unit 11 ordering-cafe 34.
