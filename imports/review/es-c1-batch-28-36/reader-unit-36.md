# Reader report: es-latam C1 Unit 36 `own-voice-c1` (capstone)

Fixes file: /home/user/parlour-read-b/.scratch/fixes-own-voice-c1.json (64 fixes, 12 marked "sure": false). Applied to a scratch copy: all 64 apply, index rebuilt, `check-content` 0 errors / 0 suspects, `unmet-words --with-hidden` [], `check_es_c1_forms --track core` 0, render has no `!!`. Audit of c1-36: 0 not in dictionary, 0 literal compound guesses. check-content on the unfixed unit: 0 errors. `check_unit_refs --bare --named`: only "unchecked recap" for 03 (main phrase not italicised; the named unit 12 is right).
After applying: run `lock_tags.py es-latam c1/own-voice-c1 --update` (category, distractor_skills and one `teaches` change).
Recaps checked against skills/es.json `taught_in` and the screens: all unit numbers right (Units 1, 2, 3, 7, 8, 11, 12, 17, 18, 20, 21, 22), except 03's example list (below).

## 1. Found by reading
- c1-36-01.ex01: "la cual dio" can pick up the feminine *la oración* (second reading); fix: *el párrafo* in all four options, ds idx 2 = relativos-el-cual.
- c1-36-01.ex02 / consolidation.ex05: "la ___ permitió" also takes *que* (la que); hint → "which (formal relative, not que)".
- c1-36-01.ex06: Carlos's reply does not answer Meg's "¿Cómo queda más preciso?" and her line is garbled ("conectar la segunda para hablar de todo el cambio anterior"); prompt rewritten: "¿Cómo resumes en una sola frase que ajustaste la oración principal y que ese cambio dio mayor coherencia a todo el párrafo?"
- c1-36-01.ex07: "logramos una conclusión" is not said; → "llegamos a una conclusión precisa" (tiles, solution, english).
- c1-36-01.ex08: "la reorganizamiento" has two faults (suffix and article); → "el reorganizamiento".
- c1-36-02 screen, example 1 (also speaking step 1): "depuré un desliz" (depurar takes a text, not a slip); → "corregí un desliz" (+ english). Same in consolidation.ex11 part 2 ("Ese desliz lo depuré al editar" → "lo corregí").
- c1-36-02.ex04 (dictation): ", evitando así un desliz" is a gerund of consequence, in the lesson that teaches rewriting such gerunds; → "… el archivo y evitaron así un desliz muy común." (+ english).
- c1-36-02.ex07: part 2 tests an adjectival gerund but the item is tagged dequeismo-queismo; part 2 → queísmo ("Estamos seguros de que el borrador es claro").
- c1-36-02.ex08: wrong options "aprobando" / "aprobar" are not agreement faults; → "Los editores aprobó…", "El comité aprobamos…".
- c1-36-03 screen text: recap lists *decidir que*, which is not on the C1 Unit 12 screen (decir, sentir, entender, temer, suponer); → *entender que*.
- c1-36-03 screen text: "*A tus argumentos los respeto*" (personal *a* before an inanimate noun); → "*Tus argumentos los respeto*".
- c1-36-03 screen table: "*Dijo que llegues hoy*" (present subjunctive after a preterite; Unit 12 shows *Dice que vengas*); → *Dice que llega hoy* / *Dice que llegues hoy*.
- c1-36-03 screen example 1 (also speaking step 1): "aunque moldearía el cierre" (aunque + conditional; *moldear el cierre* odd); → "pero cambiaría el cierre" (unsure).
- c1-36-03 screen example 4: "da a tu español una destreza muy expresiva" unnatural; → "Con el dominio del modo y del orden, tu español gana destreza y se vuelve muy expresivo." (unsure).
- c1-36-03 tip: "Whenever you front a definite direct object … always" ignores Unit 11's contrastive focus without clitic; → "a known direct object as the topic" (unsure).
- c1-36-03.ex04: option "moldeara el título para hacerla" breaks clitic agreement as well (two faults); → "El profesor me dijo que moldeara la frase…".
- c1-36-03.ex07: "entiendo … con total destreza" unnatural; → "Ese matiz expresivo lo explica ella con total destreza." (keeps *destreza* used, else vocab-unused).
- c1-36-04 screen text: "*Con lo* + adj./noun + *que*" (no such structure; Unit 20 is adjective or adverb); → adj./adv.
- c1-36-04 screen text: *para lo … que* "against a low benchmark" (Unit 20: a benchmark, not a low one); → "against what you would expect".
- c1-36-04 screen table row 4: "Ironic *¡Ni que* + imp. subj.!* " unbalanced asterisk and trailing space; fixed.
- c1-36-04 screen tip: "always use the imperfect subjunctive" (Unit 21 also teaches the pluperfect); reworded (unsure).
- c1-36-04.ex07 part 1: "se lee de modo ágil" stiff; → "se lee con agilidad" (unsure).
- c1-36-04.ex08: *ágil* has one form for both genders, so a "feminine singular subject" item cannot test agreement; → *jocosa* (options: jocosa / jocoso / "Con la jocosa" / "jocosa cual").
- c1-36-05 screen table: "me pareció un textazo" (not an established form; Unit 22 tip says established forms only); → "enterito … me pareció buenísimo".
- c1-36-05 screen example 3 and c1-36-05.ex05: "¡Menudo exitazo …!" is Spain-only; → "¡Qué exitazo …!" (ex05 sentence).
- c1-36-05.ex01: "me leí la novela entera con total naturalidad" (nobody reads with "naturalness"); → "… en dos días" in all four options (unsure).
- c1-36-05.ex06: three absurd options with absolutes only they carry (*fastest*, *guarantees*, *only*); replaced by plausible ones the text contradicts.
- c1-36-05.ex07 (+ story questions): options absurd ("legal documents", "replace collective nouns", "any conjugated verbs"); question says "connectors" for relatives; rewritten.
- c1-36-05.ex08 (+ story): option "one single regional accent until nobody can tell" has absolutes; → "one regional accent as closely as possible".
- Story paragraph 2: "una preposición sobrante en un pienso de que" (verb form used as a noun) → "en construcciones como pienso de que"; "la uno con lo cual o con la cual" is not Spanish → "enlazo sus partes con un relativo como lo cual o la cual".
- consolidation.ex12 (para lo … que, second con-lo-que item) replaced by a collective-agreement item: lesson 02's skill and its goal line had no consolidation item ("La población apoyó / apoyaron / Los vecinos apoyó / apoyamos").
- c1-36-04.ex05 and consolidation.ex04: hint "(imperfect subjunctive)" names the one thing ¡ni que…! tests and only that form fits → hint is verb and person only ("tener (nosotros)", "ser (3rd person singular)"). Kept in 03.ex05 (both moods fit).
- Challenges: c1-36-03 prompt "regret that he could not attend" leaves the person open while the target says *hayas* → "tell Carlos directly that you are sorry he could not attend"; c1-36-05 prompt says "authenticity", cue and target "ease and authenticity" → prompt fixed.

## 2. Metadata
- c1-36-05.ex10: sentence-builder tagged c1-own-voice-c1-vocab but `category` grammar → vocabulary.
- c1-36-03.ex01: ds {"1": present-tense} on one of three indicative wrong options (all are wrong forms of the tested skill) → removed.
- c1-36-01.ex01 and consolidation.ex01: "la cual" is a real form of relativos-el-cual → ds idx 2 (consolidation: unsure).
- c1-36-03.ex08 idx 3 *llegue*, c1-36-04.ex01 idx 3 *sea*: real present-subjunctive forms → ds subjuntivo-morfologia (unsure).
- consolidation.ex12: now `teaches` concordancia-ad-sensum, category grammar.
- All other slugs exist; all `teaches` single; Reading items untagged as allowed.

## 3. Goals / checklists
- c1-36-01 goal and checklist line 3: "derived nouns and verbs"; only nouns are practised (ex05, ex08) → "a precise derived noun".
- c1-36-03 goal and checklist line 2: "direct or indirect object"; every item fronts a direct object → "a known direct object".
- consolidation goal and checklist line 1 (and challenge `canDo`, which is that line): "… and derivation" has no item → dropped. Alternative if the reviewer prefers: swap consolidation.ex06 (vocabulary) for a derivation item and keep the line.
- All checklists equal their goals in count and order; each challenge `canDo` = checklist[0]; each line is the lesson's own.

## 4. Doubtful
- c1-36-05: *vamos* as a summarising marker ("Vamos, que…", "Vamos, todos salieron…") is most at home in Spain; Unit 18 calls it pan-Hispanic (reviewer checked) (unsure).
- *exitazo* (05 example, ex05) is a regular augmentative but I could not confirm it in the DLE (unsure).
- c1-36-05.ex01/ex09/ex11 and consolidation.ex09 rest on "bare plural with aspectual se is wrong" (*me leí novelas*); Unit 17 says it sounds odd, some speakers accept it (unsure).
- c1-36-05 challenge target is word for word the right option of ex09 and of the story's last paragraph; consolidation.ex09 repeats ex01/ex11's four-option fault pattern.
- c1-36-03.ex06 wrong option "Esas dos propuestas comparto…" could be read as contrastive focus (Unit 11), but Meg's question makes the topic known; left.
- c1-36-02.ex05: the stem does not show the sentence being rewritten and the original is a wrong option; left.
- c1-36-02.ex07 and c1-36-04.ex07 give the whole answer in the prompt (same convention as Units 30-35).
- c1-36-05 goal 1 ("shift the same idea between formal prose and conversation") is only practised informally (ex09, ex11, challenge); goal line 3 and top-level goal say "C1 capstone essay" (level label in a goal).
- consolidation.ex10 "logramos gran soltura" (a demanding editor writes *una gran soltura*) (unsure).
- c1-36-04 screen table row 3 uses *soltura* before 05 lists it, and 01/02 use *frase* before 03 lists it; both are allowed (own screens / earlier use of a known word).
- 03 recap sentence names unit 12 correctly but italicises no word of the main phrase (check_unit_refs "unchecked").
- Facts: the text names no person, study or figure; its only claims are linguistic (dislocation keeps the content, formal vs spoken register) and true; the screens' norm claims were left to the reviewer's RAE check, except those flagged above.

## 5. Dictionary
None: the audit reports 0 "not in the dictionary" and 0 "literal compound guess" words for c1-36.

## Fix count
Unit 36 own-voice-c1: 64 fixes (42 target, 22 other; 12 unsure).
