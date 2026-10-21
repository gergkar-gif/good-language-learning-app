# Report es-es A1 batch 19-24, prompt B (units 22, 23, 24)

## Unit 22 likes-dislikes (a1-gustar-*, story a1-gustar)

check-content: 4 errors (all length give-aways), 30 suspects; all fixed in `fixes-likes-dislikes.json` (29 fixes, verified with check_fixes.py: 0 rejected, no new findings). Audit: 0 dictionary gaps. Recap opening in gustar-01 is present and correct (Unit 21, doler). No ir a / past / saber-conocer / personal a / estar+gerund in the unit; story is clean.

### 1. Found by reading
- a1.gustar.01.ex06: wrong options have two faults each ("No yo gusto la música." pronoun+verb, "Me no gusta música." order+article). Fix: "No me gusto la música." / "No me gusta música." (one fault each).
- a1.gustar.01.ex07 / 02.ex04 / cons.ex13: "mexicana/mexicanos" in no list. Fix: "Me _____ la comida." / "Me _____ los tacos." / "Say that we like apples."
- a1.gustar.01.ex10, 03.ex10, 05.ex10: "Tengo hambre."/"No tengo hambre." (hambre first taught b1-38-03). Fix: "Tengo una hermana." / "No, no tengo tiempo." / "No tengo tiempo."
- a1.gustar.02.ex08: "A mí me ... los libros de historia" uses "a mí" (listed in gustar-03) and "historia" (gustar-05) before their lessons. Fix: "Me _____ los deportes y las películas."
- a1.gustar.02.ex10: "¿Qué te parecen estos tacos?" (parecer is B1); only the right option had "!" (tell-punctuation). Fix: "¿Te gustan estos tacos?" / "Me gustan mucho." / "Me gusta mucho." (unsure: "Me gusta mucho." can pass as a loose natural reply).
- a1.gustar.02.ex11: "películas de acción" (acción b1). Fix: "¿Te gustan las películas?"
- a1.gustar.03.ex03: "comida picante" (no list). Fix: "la comida".
- a1.gustar.03.ex04: option "os" is a vosotros form (A2 unit 33; never allowed in es-latam). Fix: options nos / les / le.
- a1.gustar.03.ex08: English "Do you like music?" fits singular "te" but the sentence says "a ustedes". Fix: "Do you all like music?"
- a1.gustar.03.ex10: "vietnamita" unmet, "No, no tengo hambre." Fix: "la comida de Vietnam", "No, no tengo tiempo."
- a1.gustar.03.ex11: length give-away (20 vs 13) and "viajar" (gustar + infinitive is gustar-04). Fix: "¿A ustedes les gusta la música?" / "Sí, nos gusta mucho." / "Sí, te gusta mucho." / "No, somos de Hanói."
- a1.gustar.04.ex03: "los fines de semana" (fines first in hobbies-03). Fix: "por la noche", English "at night".
- a1.gustar.04.ex04: "mundo" unmet. Fix: "Me gusta viajar por España."
- a1.gustar.04.ex10: "los domingos" (hobbies-05) and give-away (24 vs 15). Fix: "en casa"; "Tengo veintiocho años." / "Soy estudiante de español."
- a1.gustar.04.ex11: "bailar salsa" (salsa unmet), "me encanta" used before gustar-05, give-away (23 vs 14), "!" tell. Fix: "¿Te gusta bailar?" / "Sí, me gusta bailar." / "No, me llamo Meg." / "Sí, vivo en Hanói."
- a1.gustar.05.ex02: "música latina" (latina in no list; MC questions are not scanned by the checker). Fix: "¡Me __ la música!"
- a1.gustar.05.ex08: "arte moderno". Fix: "¿A ti te _____ el arte?" / "Are you interested in art?"
- a1.gustar.05.ex11: "parece", "pintura" unmet and give-away 29 vs 16. Fix: "¿Qué te interesa?" / "Me interesa la historia." / "Tengo dos hermanas." / "Vivo en una casa."
- a1.gustar.cons.ex08: "culturas asiáticas". Fix: "las ciudades grandes", "big cities."
- a1.gustar.cons.ex11: jazz/latina/clásica unmet; wrong option 2 differs from the right one in two ways. Fix: "¿Qué te gusta escuchar?" / "Me gusta la música." / "Te gusta la música." / "Yo gusto la música."
- a1.gustar.cons.ex12: "comida picante". Fix: "el café".
- a1-gustar-03 vocabulary: "a mí" had no item (vocab-unused). Fix: ex09 now "A mí me gusta Hanói." (a1.gustar.03.ex09).
- a1-gustar-02 grammar tip: "*yo* does not change the ending ... always gusta or gustan" brings in yo, which the pattern never uses (unsure). Fix: tip reworded about the pronouns.
- a1-gustar-05 grammar tip: "Do NOT say *Me encanta mucho*" overstates; the form is heard and accepted (unsure). Fix: "Avoid ... adds nothing."
- Repetition (not fixed): gustar-02 has four gusta/gustan multiple-choice items (ex02, 03, 07, 09) of one shape.

### 2. Metadata
- a1.gustar.cons.ex11: teaches a1-likes-dislikes-vocab, but the wrong options (after the fix) differ in a gustar form. Fix: teaches ["gustar"].
- Rest checked: matching = vocab, dialogues with off-topic wrong replies = vocab, ex09 (el/un/del) = articles, writing = gustar. No distractor_skills needed.

### 3. Goals / checklists
- a1-gustar-01 goal 2 "Understand that the thing you like is the subject of the sentence." is practised by no item (unsure). Fix: "Use the definite article with the thing you like: *el café*, *la música*." (ex09, tip).
- a1-gustar-05 checklist 1 "I can express strong passion with encantar." Fix: "I can say what I love with me encanta." (unsure; canDo copied from it).
- The challenge screens currently show the generic "Put your Spanish skills into practice" scenario; the six new entries are in challenges-likes-dislikes.json.

### 4. Doubtful
- a1.gustar.01.ex09 options el / un / del: "Me gusta un chocolate." is conceivable Spanish (unsure); left.
- a1.gustar.04.ex02 distractor_skills on "leo"/"leemos" (er-ir-verbs): the sentence is ungrammatical, the forms are real (unsure; left).
- Story a1-gustar: summary says "courtyard café", narration "tea garden", location "Café en Hanói" (cosmetic).
- Tables in gustar-03 show ustedes only (no vosotros row); fine for A1, noted only.

### 5. Dictionary
(none: audit reported 0 not in the dictionary, 0 literal compound guesses)

Fix count unit 22: 29 (+ 6 challenges)

## Unit 23 hobbies-free-time (a1-hobbies-*, story a1-11)

check-content: 7 errors, 7 suspects; all addressed in `fixes-hobbies-free-time.json` (47 fixes, verified with check_fixes.py: 0 rejected, no new findings; the added item a1.hobbies.05.ex20 and its lesson reference apply cleanly). Audit: 0 dictionary gaps. Consolidation copy a1.hobbies.06.ex06 left alone (instruction). Story reading questions (ex14-ex18) are about what Carlos, Meg, Lauren and the friends say and do and are answerable from a1-11; only their option lengths were wrong.

### 1. Found by reading
- a1.hobbies.03.ex09: "Ayer" / "El año pasado" as wrong options (tell-time-word, past markers at A1; "pasado" first taught a1-abilities-01). Fix: "Cada semana" / "Ahora mismo" / "En este momento".
- a1.hobbies.03.ex16: "El sábado jugué al fútbol." (pretérito indefinido, A2) and "Ayer juego al fútbol." (tell-time-word). Fix: "Hoy juego al fútbol." / "Ahora mismo juego al fútbol."
- a1.hobbies.01.ex06 (and the lesson's own table): "juega/jugar" are used in hobbies-01 but first listed in hobbies-02. Fix: add "jugar = to play" to a1-hobbies-01-voc.json.
- a1-hobbies-01 vocabulary: "bailar" listed, no item uses it (vocab-unused). Fix: a1.hobbies.01.ex03 third option "bailar".
- a1.hobbies.01.ex09 "Which describes a free-time activity?" also fits "Lees por la tarde." (two right answers). Fix: question 'Which means "I read in the afternoon"?'
- a1.hobbies.05.ex09 "Which combines a day and a hobby?" also fits "El miércoles juegas al fútbol." Fix: 'Which means "On Wednesday I play football"?'
- a1.hobbies.06.ex11 "Which combines time and a hobby?" also fits "Lees a las ocho." Fix: 'Which means "I read at eight o'clock"?'
- a1.hobbies.05.ex19: duplicates ex05 (same sentence, same options) and "Which combines…" has two right answers. Fix: 'Which means "On Sunday I go out with my family"?' / salgo / salo / sale.
- Infinitive as wrong reply (a1.hobbies.01.ex10, 01.ex11, 02.ex10, 02.ex11, 03.ex10, 03.ex11, 04.ex10, 05.ex11, 06.ex13, 06.ex14, 06.ex16): "Leer en casa.", "Bailar.", "Descansar." answer ¿Qué haces…? naturally (elliptical), so they are a second right answer. Fix: third-person forms (Lee/Escucha/Baila/Camina/Juega/Descansa …).
- a1.hobbies.05.ex10: same, plus wrong options now salo / sale (see Metadata).
- a1.hobbies.02.ex16: near-duplicate of ex04 ("I dance on Fridays" with Baila/Bailar). Fix: 'Which means "I study at home"?' / Estudio / Estudias / Estudiar en casa.
- a1.hobbies.04.ex04: question ends '?"?'. Fix: 'How do you say "What do you do in your free time?"'
- a1.hobbies.04.ex16: wrong option differs only by the final period (grader ignores it). Fix: 'Which question asks "What do you do on Saturdays?"' / "¿Qué hacer los sábados?" / "¿Qué haces a los sábados?"
- a1.hobbies.04.ex09: length give-away 30 vs 16. Fix: wrong options "¿Dónde trabajas los sábados?" / "¿Qué tienes en tu casa?"
- a1.hobbies.05.ex14/16/17/18: reading options length give-aways (27/16, 20/8, 30/16, 29/18). Fix: "Play football." / "Lauren." / wrongs "Cook new dishes at home." "Dance salsa with friends." / wrongs "To go to a museum in Hanoi." "To cook together at home."
- a1.hobbies.05.ex12: "¿Te gusta tu semana?" is not a natural question. Fix: "¿Te gusta caminar en el parque?"
- a1.hobbies.03.ex12, 05.ex13, 06.ex17, 06.ex18: writing prompts do not pin the stored answer ("Say what you do on Mondays."). Fix: pinned prompts ("Say that you read at home on Mondays." etc.).
- a1.hobbies.06.ex09: "Mi madre está amable." is acceptable Spanish (a second right answer, rulebook § 6c). Fix: "Mi madre es amables." and remove distractor_skills.
- Grammar screens a1-hobbies-01, 02, 04 open with no recap although they review Unit 7 (present), Unit 22 (¿Qué te gusta?, ¿Te gusta…?) and Unit 14 (¿Qué haces?). Fix: "You know … from Unit N" openings; hobbies-02's tip ("rather than learning a new tense") reworded.
- a1-hobbies-05 grammar: *salgo* appears with no mention that it is an irregular yo form. Fix: tip adds "like hago and pongo (Unit 14)".

### 2. Metadata
- a1.hobbies.05.ex05, ex10, ex19: wrong options are wrong forms of salir (tag present-tense) -> teaches ["present-irregular-yo"].
- New item a1.hobbies.05.ex20 (fill-blank "Los sábados _____ con mi familia." -> salgo, teaches present-irregular-yo), added to the Practice group of a1-hobbies-05.
- After these changes the skill has 4 items in this unit (ex05, ex10, ex19, ex20). Run lock_tags for the unit after applying.
- a1.hobbies.06.ex11 teaches "numbers" but its tested form is *a las ocho* (telling-time) (unsure; not changed).
- Items tagged stem-changes (01.ex06, ex14, 03.ex05, ex10, 05.ex07, ex09, 06.ex04) have wrong options that differ in person or infinitive, not in the stem (unsure; left).

### 3. Goals / checklists
- a1-hobbies-01 title "What Do You Like Doing?" repeats the title of Unit 22's a1-gustar-04 and promises "like"; the lesson is about what you do. Fix: "Free-Time Activities" (unsure).
- Checklist first lines of hobbies-01 to 05 are imperatives, not can-dos ("Talk about…", "Name…", "Describe…", "Ask…"). Fix: "I can …" (unsure; the challenges' canDo copy the fixed lines).
- a1-hobbies-01 grammar section title "Talk about what you like doing" -> "Talk about what you do".
- a1-hobbies-consolidation goal/checklist line 2 "… using cumulative A1." is not a learner action (unsure; the line occurs in both goal and checklist so no single-occurrence fix was written).

### 4. Doubtful
- Story a1-11: Daniela addresses the group with ustedes forms (*verlos*, *hacen*); in es-es among friends a Spaniard would say *veros/hacéis*. Stories are exempt; mentioned only (unsure).
- Hobbies-01..03 are thin review lessons (the same verbs in every lesson); several MC items repeat one shape ("Which means 'I …'?" with wrong person + infinitive) six or more times per lesson (rule 7); left.
- a1.hobbies.04.ex04 / ex16 tag `questions` while the wrong options differ in a preposition (unsure).

### 5. Dictionary
(none: audit reported 0 not in the dictionary, 0 literal compound guesses)

Fix count unit 23: 47 (+ 6 challenges)

## Unit 24 skills-abilities (a1-abilities-*, story a1-abilities)

check-content: 8 errors, 39 suspects; all addressed in `fixes-skills-abilities.json` (52 fixes, verified with check_fixes.py: 0 rejected, no new findings). Applied temporarily to the tree (then reverted): check-content leaves only 3 suspects (`conozce`, a deliberate non-word wrong option; and two stale-index/other items the fixes cover). Audit: 0 dictionary gaps. Story a1-abilities: reading questions are about what Meg and Carlos say and do and are answerable from the text; keyVocabulary is real. The es-latam files differ only in the vosotros rows (not touched; the ex06 fix gives es-es the same option set es-latam already has).

### 1. Found by reading
- Past tenses at A1: a1-abilities-04 grammar example and speaking step "Ayer conocí a Meg en la escuela." (pretérito indefinido, A2); a1.abi.cons.ex04 + its speaking step "Ayer conocí _ Carlos en el centro."; a1.abi.01.ex10 "Ayer fue martes."; a1.abi.02.ex11 "iba mucho a la playa" (imperfect); a1.abi.02.ex02 "yo supe"; a1.abi.03.ex10 "me encantaría" (conditional). Fixes: "Conozco a Meg de la escuela." (+ English); "Hoy veo _ Carlos en el centro."; "Hoy es lunes por la tarde."; "Sí, sé nadar muy bien." ; "yo sabe"; "No, todavía no conozco Sudáfrica."
- Character fact: a1.abi.02.ex10 has Carlos play "la guitarra acústica", but the story says Carlos plays the piano (Lauren plays the guitar, a1-11). Fix: Meg "¿qué sabes tocar?" / "Sé tocar el piano." (also uses the listed but unused "el piano").
- Personal a before a1-abilities-04: a1.abi.03.ex09 wrong option "Conozco Carlos." tests the personal a one lesson early. Fix: "Conozco con Carlos."; the 03 grammar shows "Conozco a Carlos" unexplained (fix: tip adds "explained in the next lesson", unsure).
- Saber/conocer contrast before a1-abilities-03: a1.abi.02.ex11 wrong option "No, no conozco nadar muy bien…" Fix: "Sí, sé nado muy bien." (single fault). Same in 04 and cons: "sé a Lucía" (verb contrast) / "conoces a Lucía" (person) tested instead of the personal a: a1.abi.04.ex10, a1.abi.04.ex11, a1.abi.cons.ex11. Fix: wrong options "conozco Lucía" / "conozco de Lucía" (omitted a / wrong preposition).
- Recaps missing: a1-abilities-01 presents poder as new ("is an o -> ue stem-changing verb"). NB: the Unit 10 screen a1-08-03 teaches only *querer*, not *poder* (skill querer-poder is described as "querer and poder"): so poder is NOT known from Unit 10, and a "You know poder from Unit 10" recap would be false. Fix: "You know stem-changing verbs from Unit 8 and *querer* from Unit 10 … *poder* changes the same way." a1-abilities-02 presents saber + infinitive as new (taught in a1-10-05, Unit 13, with "yo sé is irregular — not sabo"). Fix: "You know *saber* + infinitive from Unit 13"; goal "Learn the irregular yo form" -> "Review …".
- *venir* is in no vocabulary list (the brief expected it in a1-abilities-01) although ex06, ex11 and the grammar screen use it. Fix: add "venir = to come" to a1-abilities-01-voc.json. New item a1.abi.01.ex13 (fill-blank "Hoy no _____ a clase porque estoy enfermo." -> vengo, present-irregular-yo), added to the Practice group (unsure).
- a1-abilities-04 grammar table: "Llamo al taxi (special case)." sits in the "no a" column and contradicts the rule. Fix: "Pido la cuenta."
- Answer given away: a1.abi.04.ex04 "Which sentence requires the personal 'a'?" — the right option is the one containing "a". Fix: "Which sentence is correct?" / Llamo a / Llamo (no a) / Llamo de. a1.abi.04.ex12 prompt "(al)" gives the answer; a1.abi.03.ex12 prompts "(conocer)" / "(saber)" name the verb in the lesson that tests the choice. Fixes: pinned English prompts.
- Two right answers: a1.abi.cons.ex06 "Yo __ nadar, pero hoy no puedo ir…" also fits "puedo". Fix: options sé / sabes / conozco. a1.abi.05.ex02 "¿__ puedes hacer un favor?" has no English; "Te/Se" give real sentences. Fix: "Can you do me a favor? Which sentence says this?" with whole sentences (unsure).
- a1.abi.05.ex12 "Ask: 'Can you help me?'" -> "¿Me puedes ayudar?" while "¿Puedes ayudarme?" is equally correct (the tip says both). Fix: prompt pins the pronoun position.
- Wrong options with two faults / non-phrases: a1.abi.01.ex09 ("¿Ayudas me?", "¿Poder tú ayudar?"; also question ends '?"?'), a1.abi.01.ex11 option 3 (saber and 2nd person), a1.abi.03.ex10 (three differences), a1.abi.02.ex11, a1.abi.cons.ex11. Fixed with one-fault options (see the fixes file).
- Wrong option "sabéis" (a1.abi.02.ex06) is an A2 vosotros form; es-latam's file already has "sabe". Fix: sabemos / sabe / saben.
- a1.abi.04.ex02 "desde hace un mes" (A2 time construction). Fix: "Conozco __ Carlos en la clase."
- a1.abi.04.ex11 "para avisarle que llego tarde" (para + infinitive, A2 por/para) and mamá/avisarle unmet. Fix: "Estoy llamando a mi madre." (Carlos's mother is in Budapest, a1-05).
- Length give-aways (all errors): 01.ex10, 02.ex10, 03.ex11, 05.ex05, 05.ex08, 05.ex10, cons.ex12; plus tell-opener "claro" and first-letter case (01.ex10, 05.ex05, 05.ex10, cons.ex12). Fixed with matched-length options.
- Unmet words fixed with met ones: ejercicio (01.ex03 -> tarea), frase (01.ex07 -> pregunta), palabra (01.ex10 -> regla), mar (02.ex03), mexicana (02.ex05), salsa (02.ex07), agradable (03.ex02 -> bonita), dato (03.ex06), Cabo (03.ex10), cierra (03.ex11 -> empieza), maletas (05.ex03 -> bolsas), supuesto (05.ex10), cargador (05.ex11 -> teléfono), explicación (cons.ex02 -> pregunta), excelente/buen (cons.ex11), piscina (cons.ex06), doctora (04.ex09 -> profesora).
- inglés is in no list: added "el inglés = English" to a1-abilities-02-voc.json (first lesson that uses it) and used in 02.ex03.
- vocab-unused: pasar (01.ex05 now "¿Puedo pasar, por favor?"), el piano (02.ex10), la información (03.ex06), la gente (04.ex08 "Quiero conocer a la gente de Hanói.").

### 2. Metadata
- present-irregular-yo (unsure, 02.ex02 and 02.ex03: the item tests *sé* against *sabo*/*sabe*; currently saber-infinitivo): retagged; new a1.abi.01.ex13 (*vengo*). No item in this unit tests *conozco* against *conoco*; left as saber-vs-conocer.
- a1.abi.01.ex11: teaches a1-skills-abilities-vocab but the wrong options are poder/saber forms -> querer-poder, with distractor_skills {"2": "saber-infinitivo"} on "Sí, sé llegar…".
- a1.abi.04.ex10, ex11 and a1.abi.cons.ex11: teaches vocabulary, but the options differ in the personal a -> a-personal.
- a1.abi.05.ex02: category vocabulary / vocab -> grammar / querer-poder (unsure).
- a1.abi.cons.ex06: distractor_skills {"2": "querer-poder"} removed with the "puedo" option.
- a1.abi.05.ex08 (pronouns attach to infinitives) is tagged vocabulary but is a grammar question; no skill covers it exactly (unsure; left).
- Because these units are locked, run `python scripts/lock_tags.py es-es a1/<unit id> --update --reason "…"` after applying (validate-content --changed lists 13 locked-tag changes across the three units).

### 3. Goals / checklists
- a1-abilities-04 checklist "I always use the personal 'a' when a direct object is a specific person." is not a can-do and over-claims. Fix: "I can use the personal a before a specific person." Goal "Master the obligatory personal 'a'…" -> "Use the personal 'a'…" (unsure).
- a1-abilities-03 checklist "I can distinguish between saber and conocer accurately." -> "I can use saber for facts and conocer for people and places." (unsure).
- a1-abilities-02 goal 1 "Learn the irregular yo form of saber" -> "Review …" (Unit 13).
- Challenge screens currently show the generic "Put your Spanish skills into practice" scenario with garbled prompts ("i always use…"); the six new entries are in challenges-skills-abilities.json.

### 4. Doubtful
- The grammar tables of 01, 02, 03 carry vosotros rows (podéis, sabéis, conocéis): es-es only, deliberate per brief, but vosotros-indicativo is an A2 skill (a2-vosotrospeninsular-01) (unsure).
- a1.abi.02.ex09 ("Does Spanish require a word for 'how'?") is metalinguistic; "Sé cómo cocinar" is valid Spanish, so the option is a plausible wrong answer (unsure; left).
- "ayudarme/ayudarle" (pronouns attached to infinitives) are used from lesson 01 and only explained in lesson 05 (a1.abi.05.ex08).
- a1.abi.03.ex02 "conozce" is a deliberate single-fault non-word (check-content lists it as unmet; left).
- Story a1-abilities: location "Centro de Hanói" vs narration "library" (cosmetic).
- The brief names "a1-abilities-01 lists venir"; it does not (see group 1).

### 5. Dictionary
(none: audit reported 0 not in the dictionary, 0 literal compound guesses)

Fix count unit 24: 52 (+ 6 challenges)

## Totals
Unit 22: 29 fixes; Unit 23: 47 fixes; Unit 24: 52 fixes; 18 challenges (6 per unit).
Files: fixes-likes-dislikes.json, fixes-hobbies-free-time.json, fixes-skills-abilities.json; challenges-likes-dislikes.json, challenges-hobbies-free-time.json, challenges-skills-abilities.json; report-likes-dislikes.md.
