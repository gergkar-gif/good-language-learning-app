# Review: es-es A1 batch 13-18, prompt B

## Unit 16 directions (a1-directions-01 .. consolidation, story a1-13)

check-content: 3 errors (04.ex09, 05.ex14, 05.ex18 length give-aways, plus 05.ex18 again fixed below), 5 suspects. Every item below has a fix in fixes-directions.json (38 fixes, check_fixes: 0 rejected).

### 1. Found by reading
- a1.directions.02.ex06 / ex14 / screen 02 example: *Vengo del parque* uses *venir*, which no A1 vocabulary list has before abilities-01 (Unit 24), and *vengo* is a yo form. Items and example rebuilt with *ir*: *Voy del parque al centro.* (unmet-word check does not see it.)
- screen a1-directions-02 table: rows `a | into` (duplicate of `a`) and `por | up` (false); text promises "into". Rows removed, text reworded.
- a1.directions.05.ex14-18 (reading): invented scene, not the story: "starts in the centre of Hanoi", "trying to find a market", "eventually arrive". Story: Kaylee is lost in the old quarter and looks for the café; she has not arrived ("Ya estoy llegando"). All five rewritten (also fixes the 05.ex14 and 05.ex18 length errors).
- a1.directions.04.ex09 (ERROR 27 vs 13): lengthened the wrong options, and the vague prompt "locates a specific place" became "gives the location of a known place".
- a1.directions.04.ex13: identical to ex06 (same sentence, same options). Rebuilt (*Camina por la calle y cruza en la esquina.*).
- a1.directions.02.ex16: duplicate of ex04. Rebuilt (*Camino hacia el parque.*).
- a1.directions.02.ex11: *Camino del calle.* has two faults (gender, contraction) -> *Camino de la calle.*
- a1.directions.03.ex06: *Sigue derecha.* is not a phrase -> *Sigue a la derecha.*
- a1.directions.03.ex09: *Giras en la derecha.* two faults; new item on *izquierda* (the old triple also equals ex17 and 06.ex05).
- a1.directions.04.ex16: wrong options carried two or three faults (*Vas al museo. El museo hay a la derecha.*, *Hay al museo. El museo está derecha.*) -> one fault each, `distractor_skills` {1: ir}.
- a1.directions.06.ex13: *Voy en el museo... hay* two faults -> one each.
- a1.directions.06.ex05, ex06, ex14, ex15: consolidation copies of 03.ex17 / 05.ex05 / 05.ex10 / 04.ex11 (ex15 is word for word 04.ex11). Varied with met words.
- a1.directions.06.ex09: "Which is correct?" with *Mi madre está amable.* (real Spanish) as an option -> pinned with "My mother is a kind person."
- a1.directions.06.ex17, ex18: structured-writing prompts did not pin the stored answer; ex18 used *giro* (unmet-word) and a first-person route. Prompts and answers rewritten (*Ve al centro. Sigue recto por la calle y gira a la izquierda...*).
- a1.directions.05.ex06: answers *Ve, Vaya* (answers-alternatives): *Vaya* (usted, A2) does not go with the tú *gira* in the same sentence -> `answers: ["Ve"]`.
- Screens: a1-directions-01 presents *estar* as if new and never gives *vas/va* or explains *al* (a + el); a1-directions-03 does not say "You know commands from Unit 14" and *ve* is an irregular command (Unit 14 said irregulars are not introduced); a1-directions-05 lacks the recap. Texts reworded (03 and 05 unsure).
- Vocabulary a1-directions-01: `hacia` (listed again and used in 02) and `camino` (never used, clashes with the verb *camino*) unused -> removed from 01.
- Story a1-13 (all unsure; audio must be re-narrated): *cruza el semáforo* (not natural: "cruza la calle en el semáforo"), *Vas a ver* (ir a + infinitive, Unit 25 -> *Ves*), *Ya estoy llegando* (estar + gerund, Unit 19 -> *Ya llego*). *No te preocupes* (negative command, A2) also stays in the story: left alone, a fixed phrase.
- Challenge screens in lessons 05 and consolidation: the prompt says "thank them" / "directions to a station, hotel, or pharmacy" but the targets (*¿Dónde está la farmacia?*, *El banco está a la derecha de la farmacia.*) do neither; the new challenges file replaces them.

### 2. Metadata
- a1.directions.04.ex05, a1.directions.05.ex07: `preposiciones-movimiento` -> `estar` (*está a la izquierda* is a location phrase, not movement; unsure).
- No other mismatch found: 01-03 tags, `distractor_skills` and the `present-irregular-yo` rule checked (after the fix no yo form of venir remains).

### 3. Goals / checklists
- No defect. Goal and checklist lines are the lesson's own and unique. Canonical canDo copied unchanged into the challenges file.

### 4. Doubtful
- *ve* (irregular tú command of *ir*, `imperativo-afirmativo-irregular` is A2) is taught in 03 as an ordinary command in ~10 items, vocab `ve = go`, `gira = turn` (inflected forms as lemmas). No fix: needs the user (unsure).
- *por* ("along/through", 02 and 03.ex10 *¿Por dónde voy?*): `por-vs-para` is an A2 skill and the tag `preposiciones-movimiento` covers a/de/en/hacia only. No fix (unsure).
- Lesson 03/04 have 5-6 items of one shape ("pick the command among indicative forms"), lesson 02 five "Which means ..." items on the same three sentences. Not rewritten.
- The `en` of `preposiciones-movimiento` is not taught by the screens (only a, por, de, hacia).

### 5. Dictionary
None: audit-reader-coverage for a1-13 reports 0 not-in-dictionary and 0 literal compound guesses.

Fixes: 38 (directions).

## Unit 17 weather (a1-weather-01 .. consolidation, story a1-14)

check-content: 1 error (05.ex15), 13 suspects. Fixes in fixes-weather.json (59 fixes, check_fixes: 0 rejected).

### 1. Found by reading
- Screen a1-weather-02 repeats screen 01 (same six phrases, same examples, tip lists them again) and never says what *tiempo* means. Rewritten around *¿Qué tiempo hace?*, *hace fresco*, *hay nubes en el cielo* (unsure; heavy rewrite).
- Screen a1-weather-01 text promises *hay* for weather but no row or example shows it -> reworded.
- a1.weather.05.ex14-18 (reading): invented text type and facts ("weather diary", "the character records", "goes to the beach", "orders a drink", "plan activities"). The story is a Meg/Carlos dialogue on a rainy Sunday (no park, tea, sun and heat return on Monday, they stay at home). All five rewritten (also fixes the 05.ex15 length ERROR).
- a1.weather.01.ex09: *Hace lluvia.* / *Está lluvia.* use *lluvia*, listed only in lesson 02 -> options are other weather phrases.
- a1.weather.01.ex10 (suspect *tiempo*): question -> *¿Hace sol o llueve?*. a1.weather.03.ex02 (suspect *semana*): option -> *noche*. a1.weather.06.ex20 (suspect *abrigo*): -> *me pongo la chaqueta* (chaqueta known from Unit 8).
- a1.weather.06.ex19: *Hoy hay mucho viento* — *hay + weather* is never taught (the unit shows *hace viento*), and *hace* was a second right answer -> *Hoy llueve mucho en la ciudad.* (blank *llueve*). The speaking screens follow the exercise.
- Duplicates inside lessons: 03.ex13 = 03.ex04 verbatim; 04.ex17 = 04.ex06; 04.ex11 = 03.ex10; 02.ex13 = 01.ex16; 02.ex16 = 01.ex13. All rebuilt.
- Wrong options with a different kind of fault from the item (the main retag issue, see 2): *Está calor*, *Hace lluvia*, *Cuando está sol*, *Estudio la casa*, *Camino al parque en.* (garbled), *Tomo el agua en.* (garbled), *Cuando lluvia* (garbled), *voy en parque* (two faults).
- *Hace nublado* as a wrong option (01.ex13, 02.ex11, 02.ex16, 06.ex02): it is heard in some regions -> *Es nublado*.
- Bare prompts "Which is correct?" / "Which combines ...?" that fit every option: 01.ex16 (*Está frío* is right for cold soup), 03.ex09, 05.ex09, 06.ex09 (*Mi madre está amable*), 06.ex11.
- Consolidation copies (suspects): 06.ex03, ex05, ex06, ex14, ex15, ex16; 06.ex04 also varied. All with met words.
- Writing prompts that did not pin the answer: 05.ex13, 06.ex17, 06.ex18.
- Vocabulary: `llover` (01.ex03 now), `tiempo` (02.ex11), `fresco` (02.ex13) used again; `plan` (04) used nowhere -> removed (unsure). `quedarse` was unused in exercises too: 04.ex16 now uses it.
- Story a1-14 (unsure, audio must be re-narrated): *La temperatura bajó* is a preterite (A2) in the text and in the question explanation -> *baja*; *nos quedamos en casa leyendo y descansando* (gerunds, Unit 19) -> *leemos y descansamos*.

### 2. Metadata
- Weather-phrase items correctly stay `a1-weather-vocab`. Items tagged `ar-verbs` whose wrong options differed in the weather phrase were repaired by making every wrong option an -ar person fault (03.ex04, ex06, ex09, ex13, ex16, ex17; 04.ex04, ex06, ex09, ex13, ex17; 05.ex12; 06.ex04). No retag needed there.
- a1.weather.05.ex19: `a1-weather-vocab` (category vocabulary) -> `ar-verbs` (category grammar): after the fix the wrong options show the verb form.
- a1.weather.04.ex16 and a1.weather.06.ex15: new items on *quedarse* -> `reflexives`.
- a1.weather.06.ex19: `hay` -> `a1-weather-vocab`, category vocabulary.

### 3. Goals / checklists
- Lesson 02 goal/checklist ("Describe different weather conditions", "Use common weather structures for heat, cold, rain, sun, wind and clouds") restates lesson 01 line for line; with the screen repeated the lesson teaches little that is new. Not rewritten: needs the user (unsure).
- No other defect; canDo copied unchanged into the challenges file.

### 4. Doubtful
- *afuera / adentro* (04 vocabulary, items, story *aquí adentro*, *afuera*) are Latin American; Spain says *fuera / dentro* (*dentro* is known from Unit 9). es-es variant, not fixed (unsure).
- *cuando* is used in 03.ex10/ex11 dialogues before its vocabulary entry in lesson 04 (a conjunction counts as a function word, so the checker accepts it). Not fixed (unsure).
- 05 story: *Hace un poco de fresco*, *pronóstico del tiempo*, *Qué lástima*: fine for a story.

### 5. Dictionary
None: audit-reader-coverage for a1-14 reports 0 not-in-dictionary and 0 literal compound guesses.

Fixes: 59 (weather).

## Unit 18 work-obligations (a1-work-01 .. consolidation, story a1-15)

check-content: 2 errors (05.ex02, 05.ex03), 12 suspects. Fixes in fixes-work-obligations.json (52 fixes, check_fixes: 0 rejected).

### 1. Found by reading
- **hay que before a1-work-03**: lesson 02 wrong options used it in seven items (02.ex04 *Hay que trabajo.*, ex06 *Hay que vamos a la oficina.*, ex10 *Hay que trabajar.*, ex11, ex13 *Hay que estudia.*, ex16, ex17) and two carry `distractor_skills: hay-que`. Replaced by person/missing-*que* faults with `tener que`; ds removed. (*Tengo que* does not occur before a1-work-02.) ex10 and ex16 had a second right answer (*Hay que trabajar.* answers ¿Qué tienes que hacer hoy? naturally; *Tengo que trabajar.* fits "You have to work").
- Wrong options that are natural replies: 03.ex10 (*Tengo que trabajar.* to ¿Qué hay que hacer hoy?), 04.ex11, 05.ex11, 06.ex15 (*Tengo que preparar/terminar el informe.* to ¿Qué hay que hacer …?). Replaced with *Hay trabajar.*-type faults.
- 04.ex05: *__ que llegar temprano* with English "You have to arrive early" also takes *Tienes* -> English "It is necessary to arrive early."
- Two wrong options with the same fault (finite verb after *hay que*): 03.ex06, ex13, ex16, ex17 -> one now misses *que*.
- Two or three faults in one option: 01.ex04 *Estoy trabajo en una oficina.*, 01.ex10 *Estoy una oficina.* (garbled), 05.ex09 *Hay que trabajar y escribes informes.*, 05.ex19 (both wrong options), 06.ex06 *Hay que trabajo a las ocho.*
- 01.ex11 and 05.ex12-type bare infinitive *Escribir informes.* is a plausible reply to ¿Qué haces?; 01.ex11 -> *Escribimos informes.* (05.ex12 left: its question ¿Qué haces después? is the same, unsure).
- 01.ex16 repeated ex04 for the fifth time and no item used a job in a sentence although the goal is "Name common jobs": now *Soy periodista.* (also uses `periodista`); 01.ex02 now `trabajador` and no longer uses the unmet *reunión*; 02.ex15 now `necesitar` (vocab-unused).
- Reading 05.ex14-18: all five invented ("what kind of text", "arrives at work", "type of obligation", "starts a holiday", "birthday party"). Rewritten from the story (first day interesting; engineer, journalists, translator; tomorrow report + meeting at ten; Meg: *muy trabajador*; he wants to rest).
- 05.ex02, ex03 ERROR: wrong options shorter than the answer; lengthened.
- Consolidation copies: 06.ex01, ex02, ex05, ex14, ex15, ex16 (suspects) varied; 06.ex19 *entregar* and 06.ex20 *puntual* (A2 words) replaced by *terminar* / *temprano*.
- Writing prompts that do not pin the answer: 05.ex13, 06.ex17, 06.ex18 (rewritten).
- Screens: a1-work-01 text ("familiar present-tense verbs") lacks "You know … from Unit 7"; a1-work-02 and -03 do not recap *tener* (Unit 5) and *hay* (Unit 9); the a1-work-03 tip has an unclosed asterisk ("not *tienes que trabajar when you mean …") and reads as broken markup. Reworded.
- Story a1-15 (unsure, audio re-narration): *¿Cómo fue tu primer día …?* is a preterite (A2) -> *¿Qué tal …?*; *lo vas a hacer genial* (ir a + infinitive, Unit 25) -> *lo haces genial*. Character check: a1-01 has Carlos as *un chico estudiante*; a1-15 gives him a new office job on Monday. Consistent only if the story is read as a new job (no fix; nothing in the exercises depends on it).

### 2. Metadata
- a1.work.01.ex16 `ar-verbs` -> `ser`; a1.work.06.ex02 `a1-work-obligations-vocab` -> `tener` (category grammar); after the fixes the faults are of one kind per item.
- Dialogue distractor_skills removed where the option left the item: 02.ex10, 02.ex11, 03.ex10, 04.ex11, 05.ex11, 06.ex14, 06.ex15. 05.ex09 keeps `{1: hay-que}` on *Hay que trabajar y escribo informes.*

### 3. Goals / checklists
- Lesson 01 goal "Name common jobs and workplaces": the lesson practised only *oficina*; now one job sentence. Workplaces other than *oficina* are still not practised (unsure whether to add).
- Otherwise none; canDo copied unchanged into the challenges file.

### 4. Doubtful
- Structured-writing items carry different tags by lesson (01.ex12 `present-tense`, 02.ex12 `tener-que`, 03.ex12 `hay-que`, 04.ex12/05.ex13 unit vocabulary); rulebook says open writing -> unit vocabulary. Left (unsure).
- Lesson 04 has five "Which is personal / general?" items of one shape (ex06, ex09, ex13, ex16, ex17). Not rewritten.
- *traductora*, *asistir*, *toca descansar* in the story: fine for a story.

### 5. Dictionary
None: audit-reader-coverage for a1-15 reports 0 not-in-dictionary and 0 literal compound guesses.

Fixes: 52 (work-obligations).

---
## Fix counts
- directions: 38 fixes (fixes-directions.json), challenges-directions.json (6)
- weather: 59 fixes (fixes-weather.json), challenges-weather.json (6)
- work-obligations: 52 fixes (fixes-work-obligations.json), challenges-work-obligations.json (6)
