# Review: A1 Units 6, 7, 8 (es-es)

Fix files: fixes-daily-routine.json (32), fixes-daily-routine-reflexive-verbs.json (57), fixes-home.json (26). Challenges: challenges-daily-routine.json, challenges-daily-routine-reflexive-verbs.json, challenges-home.json (6 each). All fixes verified to match once and run through check_fixes.py (0 rejected). Checker false positives left alone: conjugated forms of listed reflexives (*ducho, duchas, duchamos, sentamos, acostamos, acostarme, lavo, lavan*), flagged as "in no vocabulary list"; they are forms of ducharse/sentarse/acostarse/lavarse, which Unit 6 lists.

## UNIT 6 daily-routine

### 1. Found by reading
- a1.06.01.ex10 "(I walk)" english-in-target; also repeats ex06 "I walk". Now "Yo __ por la tarde." hint "I cook", options cocino/camino/estudio.
- a1.06.01.ex04 answer "hablo" (first taught 06-02): answers -> estudio.
- a1.06.01.ex05, ex15 answers "descanso" (06-02), "como" (-er, 06-03): answers -> trabajo/estudio/cocino/camino/leo.
- a1.06.01.ex11, ex12 and a1.06.02.ex12, 06.05.ex11, 06.06.ex14 use "¿Qué haces…?" (haces first taught a1-hobbies-04; 06.05.ex11 also hoy): questions rewritten with met words ("Trabajo por la mañana. ¿Y tú?"; "¿Qué escuchas por la tarde?"; "¿Trabajas por la mañana?" + "Sí, _____ y luego trabajo."; "¿Trabajas y estudias por la mañana?" with options "Sí, trabajo y estudio." etc.).
- a1.06.02.ex15 "Vosotros __ español" answers include "trabajáis" (not a sentence): removed (variant es-es).
- a1.06.03.ex12 Meg asks one person "¿Dónde viven ustedes?" and Carlos answers "vivimos": "¿Dónde viven Daniela y tú?" (unsure).
- a1.06.04.ex04 "todos los días" (todos a1-cafe-04): "por la mañana".
- a1.06.04.ex05/ex08/ex10/ex13/ex14, a1.06.05.ex08: stem-changing forms before a1-reflexive-02 (*se despierta, se acuestan, se visten, se acuesta, me despierto*; and *acuesta* 06.05.ex08): replaced with regular levantarse/peinarse/lavarse items ("Carlos se levanta temprano", "Ellos se levantan tarde", "María y Ana se peinan por la mañana", "¿Cuándo se levanta Daniela? Se levanta", "Me levanto a las seis", "Ella se levanta y trabaja"). The screen's own example *Me despierto a las siete* stays (own example, see Doubtful).
- a1.06.04.ex11 "¿A qué hora…?" (hora a1-12-03): "¿Cuándo te levantas? / Me levanto temprano."
- a1.06.04 grammar table "He/She/You(f) gets up": usted is formal you, not feminine: "He / she gets up (also formal you)"; "They/You all" -> "They / you all (ustedes)".
- a1.06.04 vocabulary: *tarde* only glossed "afternoon / evening" but used as "late" in ex08, 06.05.ex05, ex16: added tarde = late (unsure).
- a1.06.05 vocabulary: *desayunar* in no list (used in grammar example, ex03, ex07): added "to have breakfast".
- Story a1-06: Daniela "Descansar un poco después de trabajar…" (infinitive fragment answering ¿Cómo estás?) -> "Descanso un poco…".
- a1.06.06.ex10 "(My mother is calm.)" english-in-target -> hint.
- a1.06.06.ex17, ex18 writing prompts did not pin the stored answers ("Say what you do in the morning", "Describe your sister", "Give a short description…"): pinned.
- Story a1-06 narration: speaker Daniela has gender "male" (she is a woman, a1-03): set female (unsure).

### 2. Metadata
- No tag changes needed in Unit 6. 06.06.ex10 keeps its ds {"2":"articles"} (Una is a real article).

### 3. Goals / checklists
- a1-06-04 goal "Learn daily routine verbs / Use reflexive pronouns" are not can-dos and differ from the lesson goal/checklist ("I can talk about getting ready"): goal and checklist -> "Talk about my daily routine using reflexive verbs." + "Use the reflexive pronouns me, te, se and nos."
- a1-06-05 goal "Integrate regular and reflexive verbs" / checklist "I can describe a full daily routine.": -> "Describe a full day with regular and reflexive verbs." + "Order what I do with luego, después and antes de." (both goal and checklist).

### 4. Doubtful
- Vosotros is drilled in 06-02 (table, example "¿Vosotros trabajáis aquí?", ex10, ex15) and 06-03 (table, example "¿Dónde vivís vosotros?", ex10, ex14), 06-04 table, although `vosotros-indicativo` is taught at A2 (a2-vosotrospeninsular-01) and the sheet says to report it. es-es policy says it teaches both, so no fix written (unsure).
- 06-01 uses tú/él/ellos forms (*Estudias, Estudia, Estudian, caminas, Trabajas*) as wrong options before 06-02 teaches them (ex06, ex11, ex12, ex14); the tip announces them. Not fixed (unsure).
- Grammar example/speaking *Me despierto a las siete* in 06-04 is itself a stem-changing form and a clock time ("a las siete", siete not in any list); allowed as the lesson's own example, but Unit 7 then teaches stem changes. Also *a las ocho/seis* are clock times before telling-time (Unit 14); seis/ocho are in 06-04's vocabulary so kept.
- Consolidation 06.06 has no reflexive item and one goal line mentions "talk about a daily routine"; consolidation copies left alone as instructed.
- vocab-unused: leer (06-01; only "leo" in answers), lavarse/sentarse (only forms *lavas, sentamos* used), peinarse now used. Accepted.
- Story a1-06 has one generic comprehension question only.
- 06-01..03 fill-blank items accept alternative verbs while `english` fits one (e.g. "Yo __ en casa" / I work): accepted pattern.

## UNIT 7 daily-routine-reflexive-verbs

### 1. Found by reading
Errors (all 6 length-giveaway/tell-absolute, all fixed):
- a1.refl.02.ex11 38 vs 21; wrong options used quieren/pan/gusta/verano: options -> "Se despiertan a las ocho." / "Mis amigos son simpáticos." / "Mi madre es muy amable."
- a1.refl.03.ex11 40 vs 24 (hace, frío, afuera, hoy, entonces, abrigada, gustan, coches, lloviendo; "Está lloviendo café."): Carlos "Meg, ¿te quitas los zapatos en casa?" / "Sí, me quito los zapatos." / "Mi madre es muy amable." / "Mis amigos son simpáticos."
- a1.refl.04.ex10 32 vs 19 (personal a "despiertas a Juan", gusta, verano, nublado): "¿Por qué te despiertas tan temprano, Meg?" / "Porque tengo clase a las ocho." / two other-question replies.
- a1.refl.04.ex11 40 vs 24 + tell-absolute *siempre* (gusta, bailar): "Sí, lavo los platos y limpio la mesa." vs "Me lavo la cara y los dientes." / "Me peino y me pongo la camisa."
- a1.refl.05.ex10 37 vs 22 (cuál, veintiocho, jueves; "Mañana es jueves" plays on mañana): "¿cómo es tu rutina…?" with "Soy de Hungría, pero vivo en Hanoi." / "Mi padre es un hombre muy tranquilo." (true story facts).
- a1.refl.cons.ex12 48 vs 29 (hoy, salir, cómodos, camiseta, apartamento, cuatro, media): "¿Qué te pones por la mañana, Meg?" / "Me pongo los pantalones y la camisa." / "Tengo dos hermanas muy simpáticas." (Meg's sisters) / "Mis amigos son altos y simpáticos."

Presented as new / forms before screen:
- Lesson 01 grammar presents reflexive verbs and the pronoun paradigm as new (Unit 6 a1-06-04): now "You know reflexive verbs from Unit 6 …"; goal "Learn the reflexive pronoun paradigm" -> "Review the reflexive pronouns from Unit 6".
- Lesson 05 grammar presents primero (Unit 1) and luego/después/antes de/después de (Unit 6) as new: "You know … from Unit 6 … and add por último".
- Lesson 04 uses the personal *a* (a-personal, Unit 24): grammar bullet "Despierto a mi hijo", table row "La madre despierta al niño", tip "personal a (Despierto a Meg)", ex03 "a su amigo", ex07 "Lavo al perro", ex10 "despiertas a Juan". Rewritten with *La alarma me despierta* etc.; ex07 now "The alarm wakes me up" (La alarma me despierta / se despierta / me despiertan). The tip also said "never use me/te/se" while its own example has *me*.
- Lesson 02 grammar: "Just like regular stem-changing verbs" (not taught before) and "in all forms except nosotros" is false (vosotros os despertáis/os acostáis also don't change): reworded.
- Lesson 02 grammar example and first speaking step "a las seis y media" (*y media*, telling-time Unit 14): "…me levanto a las ocho." (and English).
- Numbers before a1-10-02: 02.ex05/ex06 *once*, *diez* (ex12), 03.ex03 *diez minutos*, 04.ex04 *siete* + *punto*, 05.ex10 *veintiocho*, cons.ex03 *once*, cons.ex11 *diez minutos*, cons.ex12 *cuatro y media*: replaced with *temprano/tarde/a las seis/ocho*.
- Unmet words fixed (all with met words): 01.ex07 jabón/lavan ("Ellos se lavan las manos."), 01.ex10 normalmente, 01.ex11 desayuno -> "antes de la clase", 02.ex07 domingos -> "los fines de semana" (own example), 02.ex10 siempre/normalmente, 03.ex03 diez minutos, 03.ex06 "Hace calor" (hace, calor; item now a hint "You take your jacket off."), 03.ex07 ropa cómoda domingos, 03.ex08 frente/espejo, 03.ex09 rápido, 03.ex10 fiesta/azul/negros, 04.ex05 plato, 04.ex06 abrigo, 04.ex09 desayuno (noun), 05.ex05 salgo, 05.ex06 dormir, 05.ex08 haces/salgo, 05.ex11 haces/dormir/poco/compro/fruta/mercado/alemán, cons.ex03, ex04 (ligera/calor), ex05 (azul), ex08 (todos), ex10 (hora/domingos), ex11 (siempre, quedo/quedas/queda, diez, minutos).
- 02.ex03 answers "despierta","levanta" for english "wakes up" (levanta is not a stem change): -> despierta only. 02.ex07 answers acuestas/levantas/despiertas for "go to bed": -> acuestas.
- 03.ex09 wrong option "Se vistan" is a subjunctive form (another level): -> "Se viste temprano." / "Visten temprano."
- 02.ex10 Carlos answers "me acuesto a medianoche", but story a1-06 says he goes to bed at ten; cons.ex11 Carlos "me despierto a las seis", story says eight: speakers swapped to Meg.
- cons.ex09 third option had three faults ("Después de acostar, leo."): "Antes de acostar, leo un libro."
- cons.ex13 second prompt did not pin "Después me visto": "Say that afterwards you get dressed."
- Story a1-reflexive: *jugo* is the es-latam word: zumo in line "preparo un vaso de zumo" and Q2/Q3 options and explanation (variant es-es). Q3 "¿Qué prepara Carlos…?" had an answer about getting dressed: "¿Qué hace Carlos…?".
- 05 grammar tip broken markdown (`duchar**me***`): fixed.

### 2. Metadata
- a1.refl.01.ex10, ex11; a1.refl.02.ex10; a1.refl.03.ex10; a1.refl.cons.ex11: dialogues whose wrong replies differ in a form are tagged `a1-daily-routine-reflexive-verbs-vocab`; -> `reflexives`.

### 3. Goals / checklists
- a1-reflexive-01 checklist "I can say what time I get up and shower using reflexive pronouns" -> "Use reflexive pronouns to talk about getting up, showering and washing." (unsure); goal 1 -> review wording (see above).
- a1-reflexive-04 checklist "I understand when to use a reflexive pronoun and when not to." -> "Tell actions done to myself (me lavo) from actions done to something else (lavo)." (unsure).
- a1-reflexive-02 goal "Distinguish between waking up (despertarse) and getting out of bed (levantarse)" is only in a tip/example, not practised: see Doubtful.

### 4. Doubtful
- Vosotros: 01 grammar table, example "¿A qué hora os levantáis vosotros?", tip and ex09; 02/03 tables (`vosotros-indicativo` is A2). No fix (unsure).
- 02 goal 2 (despertarse vs levantarse) is not exercised; ex03 no longer accepts levanta.
- 02 grammar example "Carlos se acuesta muy tarde porque trabaja mucho" clashes with story a1-06 (Carlos goes to bed at ten, is a student) (unsure).
- Story a1-reflexive: narration says "special seminar" but the end says "Vámonos a clase"; Carlos "lavarse las manos y apagar la alarma" is an infinitive used like an order; "Mientras tú te duchas, yo me pongo…" implies they get ready in one home. Not fixed.
- Story keyVocabulary (conocer, intercambio) does not occur in the story (also a1-06 "historia", a1-07 conocer/intercambio).
- vocab-unused: 01 tarde, 02 dormirse/el sueño/por la noche, 04 el perro (its only use was the personal-a item), 05 el vaso. Accepted.
- *ducho/duchas* are checker false positives (05.ex04, ex12).
- Several 01/02 items contain "a qué hora" (hora a1-12-03); kept because it is each lesson's own example phrase.

## UNIT 8 home

### 1. Found by reading
- a1.07.02.ex06 "(some)" english-in-target: question "Hay __ libros." hint "some".
- *está/es* as wrong options before a1-07-03 (estar), and some of them correct Spanish: a1.07.01.ex04 (hay/está/es -> hay/es/tiene), ex06 and ex16 ("__ dos/tres habitaciones." Hay/Está/Son: -> Hay/Son/Tiene with hint "There are two/three rooms."), ex09 ("Which is correct?" had *Es una cocina.* = also correct -> 'Which means "There is a kitchen"?' Hay/Es/Tiene una cocina), ex10, ex11, ex13 (Está -> Tiene).
- a1.07.02 grammar presents un/una/unos/unas as new (taught A1 Unit 3): "You know … from Unit 3".
- a1.07.02.ex10 wrong options with two faults each ("Hay una sofá y unos sillas", "Hay unos sofá y una sillas"): one gender fault each.
- a1.07.02.ex13 duplicated ex04 (seven article items of one shape): now 'Which means "There is a bed"?'.
- a1.07.04.ex17 option 2 "Está una cama. La cama hay…" two faults; a1.07.05.ex09, ex18 same: now "Hay … La cama/El baño/La cocina hay …".
- a1.07.05.ex13 garbled "Hay una habitación están" (and "Hay una habitación" would answer the question too): "Hay dos habitación."
- a1.07.05.ex12 "Está al lado de la cocina" contradicts story a1-07 (bathroom is *enfrente* of the kitchen): "Está cerca de la cocina." (unsure)
- a1.07.06.ex10 "Mi madre está amable." is acceptable Spanish (two right answers): third option "Mi madre es amables."; ds removed.
- a1.07.06.ex15 "Meg: ¿Dónde está tu madre? Carlos: Está en la sala": Carlos's mother is in Budapest (a1-05) -> "¿Dónde está tu teléfono?" (unsure).
- Structured-writing prompts that do not pin the stored answer: 07.03.ex13, 07.05.ex14, ex19, 07.06.ex17, ex18: pinned.
- Tips with italics split word by word (07-01, 07-03): fixed.
- Story a1-07 speaker Daniela "male": set female (unsure).

### 2. Metadata
- a1.07.06.ex10: `distractor_skills {"2":"estar"}` removed together with the option.
- 07.04.ex13, 07.05.ex14/ex19, 07.06.ex17/ex18 are tagged `a1-home-vocab` though their stored answers test hay/estar/ser; fine only if "open writing -> vocabulary" applies (unsure; not changed).

### 3. Goals / checklists
- None changed; each lesson's goal/checklist matches what it practises. 07-03: prepositions *encima, debajo, lejos, dentro* are only drilled as vocabulary, never inside an estar sentence.

### 4. Doubtful
- Vosotros row *estáis* in the 07-03 estar table (A2 `vosotros-indicativo`); no fix.
- *sala* (living room) throughout 07-01..06 and the story: Spain says *salón* (unsure; not a "variant" fix).
- Story keyVocabulary (conocer, intercambio) not in the story.
- 07-01 has four "__ … Hay" items of one shape (ex05, ex06, ex14, ex16).
- Consolidation copies 07.06.ex04/ex09/ex14 left alone as instructed.

## 5. Dictionary
Unit 6 (a1-06): none flagged ("literal compound guess": 0, not in dictionary: 0).
Unit 7 (a1-reflexive): 
vámonos | irse | verb | to go away, to leave (vámonos = let's go) |
Unit 8 (a1-07): none flagged.

## Fix counts
Unit 6 daily-routine: 32 fixes (3 marked unsure).
Unit 7 daily-routine-reflexive-verbs: 57 fixes (2 marked unsure).
Unit 8 home: 26 fixes (3 marked unsure).
