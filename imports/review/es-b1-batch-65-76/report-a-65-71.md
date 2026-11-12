<!-- Reader A (Units 65, 67, 69, 71): 481,357 tokens, 28 min (completion notice). -->
# es-es B1 Unit 65 reported-speech (b1-33-01 … b1-33-consolidation, story b1-33-elrumor)

Fixes: `/home/user/parlour-read-a/fixes-reported-speech.json` (86 fixes); challenges: `/home/user/parlour-read-a/challenges-reported-speech.json` (6).
Checked on a scratch copy (fixes applied to es-es, mirrored and applied to es-latam, index rebuilt, `check_fixes.py` 86 fixes, 0 rejected).

| | es-es before | es-es after | es-latam before | es-latam after |
|---|---|---|---|---|
| check-content errors / suspects | 9 / 1 | 0 / 0 | 9 / 1 | 0 / 0 |
| unmet-words hits (6 stems) | 24 | 0 | 33 | 0 |

## 1. Found by reading
- b1-33-01/02/03/04/05 grammar screens: every one presents reported speech as new (*estilo indirecto* is B1 Unit 25, reported questions A2 Unit 14, *preguntó si* shown again B1 Unit 53, *al día siguiente* already in b1-13-02). Each screen now opens "You know … from B1 Unit 25 / A2 Unit 14 / B1 Unit 53" and adds only the lesson's own point.
- b1-33-01 tip "dijo *que* *estaba* cansada" (stray italics) -> one natural sentence. b1-33-04 tip "al *día* *siguiente*" likewise. b1-33-05 tip had "*had* *visto*" -> rewritten with *había visto*.
- b1-33-03 tip "me preguntó dónde vivía, not dónde vivía yo" is false (*dónde vivía yo* is correct Spanish): replaced by the true point (question word keeps its accent, *si* has none).
- b1-33-01.ex03, b1-33-02.ex03, b1-33-04.ex03, b1-33-consolidation.ex07: `answers` accepted *estuvo/vivió/tuvo* for "was/lived/did not have" (answers-alternatives): narrowed to the imperfect.
- b1-33-01.ex06 option *averiguar* (taught in b1-33-05): -> *decir*. Stems with unmet Spanish in brackets (*reproduce, correctamente, correcto, palabra, combina, verbo*): bracket removed, asked in English (33-02.ex02/ex06, 33-03.ex02/ex06, 33-04.ex02/ex06, 33-05.ex02/ex06, 33-01.ex06, consolidation ex02/ex06/ex16).
- b1-33-01.ex10 (42 vs 30), b1-33-02.ex10 (41 vs 31): wrong options lengthened with one fault each (question; conditional). 33-02.ex10 English "She assured that" -> "She stated firmly that"; 33-02.ex09 and consolidation ex10 had a time word (*tomorrow*) only in a wrong option: removed.
- b1-33-01.ex11 dictation repeated builder ex08 -> new sentence. b1-33-03.ex11 dictation repeated builder ex08 -> *Me preguntó quién había llamado*. b1-33-04.ex08 "La conversación cambió de perspectiva" (not a natural sentence) -> *Ana contó la conversación desde su perspectiva*. 33-05.ex08 changed to use *reconstruir* (else `vocab-unused`).
- Non-phrase wrong options replaced by one-fault real forms: 33-01.ex13 "Preguntó un hombre.", ex14 "Preguntó la calle."; 33-02.ex12 "Me preguntó si tiempo.", "Me dijo que no tener tiempo."; ex13 "Explicó si vivía."; ex14 "Preguntó a nadie."; 33-03.ex12 "Me preguntó que tiempo.", ex13 "Sí, me dijo dónde."; 33-05.ex14 "Averiguó el testigo en la calle."; consolidation ex14 "Afirmó si vivía."
- b1-33-04.ex13 used *convirtió* (taught B1 Unit 75) and "No cambió nunca" (tell-absolute): rebuilt as "¿Cómo se cuenta «Estoy en mi habitación»?" with possessive and pluperfect distractors (ds added).
- b1-33-04.ex14 and consolidation ex15: wrong option "Porque no cambia la perspectiva" was the negation of the right one, other was silly ("cambia el clima"): two real wrong reasons.
- b1-33-04.ex09/ex10 listening: every wrong option had two faults and *yesterday/tomorrow* only in wrong ones: rebuilt with one fault each.
- b1-33-05.ex20–23 (reading) asked about a detective text that is not on the screen, with 4 tell-absolutes (*nunca/nadie/ninguna*) and 3 length errors: replaced with four questions about the story *El rumor de la calle del Correo*.
- b1-33-05.ex15–19 and 33-01/02/03/04 writing prompts did not pin their stored answer ("Report something someone said."): pinned.
- b1-33-consolidation.ex09: *Ayer* in two wrong options (tell-time-word), unmet *rápidamente, incidente, integra*: rewritten ("Which sentence is reported speech?"). *detective* is in no vocabulary list (first used b1-33-03 screen and ex14): added to b1-33-03-voc.json and used in 33-03.ex14.
- b1-33-05 story: unlisted story words the new reading items need added to b1-33-05-voc.json: *rumor, sacristán, bolsa, vela, virrey, iglesia, oro* (all used in ex20–23). es-latam hits *ambulancia* (33-05.ex02 option) -> *un médico*.
- Story *El rumor de la calle del Correo*: retold in plain B1 (255 tokens), same five paragraphs and events, reported speech with indicative shifts only; the last paragraph no longer says "Ricardo Palma cerraba su tradición…" or what "los limeños decían": the narrator draws the lesson. `source` -> "Relato escrito para Parlour a la manera de las Tradiciones peruanas de Ricardo Palma; no es un texto suyo." (author/work already "Ricardo Palma"/"Tradiciones peruanas", as in b1-21-paliques; kept). Comprehension questions were full of rare words (*desopilante, desencadena, moraleja, rubrica*) and had a quotation attributed to Palma: rewritten to ask what the people do, answers true to the text.
- Consolidation copies of lesson items left alone (rule).

## 2. Metadata
- No retags. New distractor_skills: 33-01.ex13 [2] condicional-regular; 33-02.ex12 [1] and ex14 [2] preguntas-indirectas; 33-04.ex13 [1] possessives, [2] pluscuamperfecto; 33-05.ex14 [1] futuro-simple, [2] present-tense. the unit's exercises are in `tags.lock.json`, so `lock_tags.py … --update` is needed after applying.
- (unsure) 33-02 mixes `estilo-indirecto` (ex03) with `estilo-indirecto-informacion` (rest); the lesson teaches plain *decir que*, not *según* sources, so `estilo-indirecto-informacion` fits loosely.

## 3. Goals / checklists
- Goals and checklist lines "Use four/three new … terms" (counts wrong: 02, 04, 05 list four words) -> "Use the new words for …" in all five lessons; 01 and 02 lines kept distinct (checklist-shared). 33-05 goal "Distinguish different witness perspectives" (not practised; the story shows a rumour changing) -> "Follow how a rumour changes as people retell it."

## 4. Doubtful
- (unsure) b1-33-04 drills *aquí -> allí* and *mañana -> al día siguiente*: same family as B2 `discurso-indirecto-deicticos` (b2-17-04). Only *al día siguiente* is shown at B1 (b1-13-02); *aquí/allí* is A1 vocabulary. Kept; reviewer decides whether the skill level is right.
- (unsure) The A2 Unit 14 screens show only question words; *preguntó si* appears first as a "you know" in b1-27-02 (B1 Unit 53). The recap says "*preguntó si* from B1 Unit 53".
- Story has no claims about a real author or event; the Palma attribution is only the pastiche label (reviewer found no such *tradición*).
- Challenge scenarios use Ana (Carlos's sister), Andreas (his brother), Lauren and Kaylee (Meg's sisters), Carlos's grandmother in Madrid.

## 5. Dictionary
Audit of the new story b1-33-elrumor (es-es and es-latam): 0 "literal compound guess", 0 "not in the dictionary". Nothing to import.

# es-es B1 Unit 67 complex-opinions (b1-34-01 … b1-34-consolidation, story b1-34-dudasrazonables)

Fixes: `/home/user/parlour-read-a/fixes-complex-opinions.json` (78 fixes); challenges: `/home/user/parlour-read-a/challenges-complex-opinions.json` (6). `check_fixes.py`: 78 fixes, 0 rejected.

| | es-es before | es-es after | es-latam before | es-latam after |
|---|---|---|---|---|
| check-content errors / suspects | 13 / 4 | 0 / 0 | 13 / 3 | 0 / 0 |
| unmet-words hits (6 stems) | 27 | 0 | 39 | 0 |

## 1. Found by reading
- All five grammar screens (b1-34-01 … 05) present B1 Unit 13 (*creo que / no creo que*), B1 Unit 25 (*quizás, dudo que*) and A2 Unit 27 (*es importante que*, emotions) as new. Each now opens "You know … from B1 Unit 13 / B1 Unit 25 / A2 Unit 27" and adds only the lesson's own point (*no pienso que, es posible que, puede que, estoy seguro de que, es necesario que, me parece bien que*; 05 recaps the unit). Tips with stray italics ("*creo* *que* *es*", "es *posible* *que*", "no *estoy* *seguro* *de* *que*") rewritten as natural sentences.
- b1-34-02.ex06 (11 vs 7 chars) and b1-34-03.ex06: options *certeza* (taught in 03) and *matiz* (taught in 05) used before their lesson; replaced by met words (*oportunidad, diferencia, problema*).
- b1-34-02.ex07: `answers` ["probable","posible"] for "likely": narrowed to *probable*. b1-34-04.ex07: *valorar/evaluar* for "assess" (suspect): sentence changed to "Es importante ___ el trabajo de otras personas" ("to value"), answer *valorar* only.
- b1-34-02.ex14: wrong options "Quizá si tengan razón" (a missing accent only, *quizá sí* is real) and the right answer was the only one starting with *quizá* (tell-opener); rebuilt with *Puede que* + one fault each.
- Double-fault wrong options (*Sí, no creo que es…*; *Sí, dudo que es…*; *No, es posible que llega…*; *No, tengo la certeza de que funcione*; *Estoy seguro que existan*): rebuilt with one fault each (34-01.ex12/13/14, 34-03.ex12/13/14, 34-05.ex13, consolidation ex13). Non-phrase options (*Deberíamos que valorar.*, *Valoremos que las consecuencias.*, 34-04.ex14) rebuilt. 34-04.ex13 wrong *afecta* (unmet form) -> *afectó* with distractor skill.
- 34-01.ex12 and ex14 gave the same reply; 34-02.ex11/ex08, 34-03.ex11/ex08 and 34-04.ex11/ex03 dictations repeated a builder or fill sentence: dictations changed. 34-04.ex12 repeated the sentence of ex02/ex09: new sentence.
- Length/absolute errors rebuilt: 34-05.ex02 (*totalmente*), 34-05.ex09 (70 vs 50), consolidation ex09 (*completamente*), ex11 (70 vs 43), ex16 (*totalmente*, *completamente*). The wrong options *técnica / equipo / mala / inútil / generará / solucionar / integra* (unmet or later) replaced.
- Stems with unmet Spanish in brackets (*correctamente, palabra, requiere, matizada, subjuntivo, verbo*) asked in English only (34-01.ex02/ex06, 34-02/03/05.ex06, 34-04.ex02/ex06, 34-05.ex02, consolidation ex02/ex06/ex09/ex16).
- Words in no list added: *correcto, explicación* (34-01-voc.json, first use), *afectar* (34-04-voc.json), *crítico, talento* (34-05-voc.json, story words the reading items need). *absoluto* was `vocab-unused`: used as an option in 34-05.ex06.
- Writing prompts that did not pin the stored answer ("Express certainty using estoy seguro de que.", "Contrast certainty and doubt.") pinned in 34-01 … 34-05 and consolidation ex17/18.
- 34-05.ex20–23 (reading) asked about a "Marco" who is not in the story, had three tell-absolutes (*nadie, ninguna, totalmente*) and length errors: replaced with four questions about the story (what is discussed in the cafés, what the writer finds strange, what annoys him, what he thinks at the end).
- Story *Dudas razonables*: told by Clarín in the third person with `Clarín comentaba…`, readers' letters (invented), imperfect subjunctive after past verbs (*no creía que fuera, dudaba de que fueran, mereciera*), *No es que dude … sino que* and quotation marks around words attributed to him. Rewritten as the narrator's own article in the present tense (231 words, same five paragraphs and ideas, no readers' letters, no *sino*, no imperfect subjunctive, nothing attributed to Clarín), `source` as b1-21-paliques; comprehension questions had rare words (*suscitada, dramaturgia, ensalzaban, certidumbre*) and are rewritten to ask what the narrator says and thinks.
- Consolidation copies of lesson items left alone.

## 2. Metadata
- No retags. New distractor_skills: 34-04.ex13 [1] preterito-indefinido. Items on 34-01 are split between `opinion-verbs-mood` and `subjunctive-doubt` as before (b1-13-03 teaches both *dudo que* and *quizás*; fine).

## 3. Goals / checklists
- "Use four/three new … terms" -> "Use the new … words" in all five lessons (and their checklists). checklist-shared: 34-02 ("I can use the new words for what is likely or possible.") and 34-05 ("…for building an argument") no longer match b1-22-02 / b1-36-02. checklist-you: 34-04 "what you value" -> "what I value".

## 4. Doubtful
- (unsure) Unit 67 teaches no new skill by the registry; the lessons' items are tagged `opinion-verbs-mood`, `subjunctive-doubt`, `subjunctive-value-judgments`, `subjunctive-emotion`, all taught earlier. The only phrases that may be new are *estoy seguro de que / convencido de* and *puede que* (no earlier screen found); recapped as extensions, not as known.
- The new story is a pastiche with no claim about Clarín or any real event; the debate over old and new theatre in Madrid's cafés is invented, not a historical claim.
- Challenge scenarios use Meg and Carlos in Budapest and Carlos's sister Ana.

## 5. Dictionary
Audit of the new story b1-34-dudasrazonables (es-es and es-latam): 0 literal compound guesses, 0 not in the dictionary. Nothing to import.

# es-es B1 Unit 69 hypotheticals-possibilities (b1-35-01 … b1-35-consolidation, story b1-35-ojosverdes)

Fixes: `/home/user/parlour-read-a/fixes-hypotheticals-possibilities.json` (95 fixes); challenges: `/home/user/parlour-read-a/challenges-hypotheticals-possibilities.json` (6). `check_fixes.py`: 95 fixes, 0 rejected.

| | es-es before | es-es after | es-latam before | es-latam after |
|---|---|---|---|---|
| check-content errors / suspects | 11 / 1 | 0 / 0 | 11 / 1 | 0 / 0 |
| unmet-words hits (6 stems) | 23 | 0 | 28 | 0 |

## 1. Found by reading
- b1-35-01, 02, 04, 05 grammar screens present `hypothetical-structures` (*si* + imperfect subjunctive + conditional, B1 Unit 7) as new; 35-05's own text was a generic "combine hypothetical language". All now open "You know … from B1 Unit 7 / B1 Unit 15 / A2 Unit 26" and add their point. 35-01 tip (form from the *ellos* preterite) is a true recap and stays.
- b1-35-03 (`pluscuamperfecto-subjuntivo-si`): the screen only said "use *hubiera / hubiese* + participle" and gave no explanation of the *habría* + participle result, and it taught the *-se* form (*hubiese*, "fully interchangeable"), which is later. Rewritten: recap (B1 Unit 7, B1 Unit 1, A2 Unit 26), *si* + *hubiera* + participle / *habría* + participle, "never *habría* after *si*", plus a paradigm table (*hubiera tenido* …, with *vosotros* in es-es as an es-es-variant fix; the es-latam file gets its own fix without that row). *hubiese* removed from the lesson goal/checklist, from 35-03.ex03 `answers` (*hubiesen sido*) and from consolidation ex03 (*hubiese tenido*).
- Later forms as wrong options: *Habré aceptado*, *Habrá cambiado* (future perfect, B2), *Haya aceptado / cambiado / elegido / vuelto* (present perfect subjunctive, b1-37) in 35-03.ex13/14, 35-04.ex12, 35-05.ex13/14, consolidation ex13/14/15: replaced by real forms of known skills (*Había aceptado*, *He aceptado*, *Cambié*, *Volví*, *Elegí*) with `distractor_skills`.
- 35-04 screen example 3 (*preferiría la que me permitiera aprender algo nuevo*: relative clause + imperfect subjunctive): replaced by *preferiría la más sencilla*.
- 35-01.ex02 (36 vs 18), 35-02.ex09 (54 vs 40), 35-05.ex06 (12 vs 8), 35-05.ex20–23 (tell-absolute *ninguna, nunca*; length), consolidation ex09 (*Ayer*), ex11 (47 vs 36): rebuilt. 35-05.ex02 (*Ayer por la tarde …*) rebuilt without the time word.
- Stems with unmet Spanish in brackets (*hipotética, palabra, refiere, irreal, reflexión, contrasta, tipos, lenguaje, integra, correctamente, verbo*) asked in English only (35-01/02/03/04/05.ex02 and ex06, consolidation ex02/ex06/ex09/ex16). 35-02.ex02 options *contingencia, inicial* replaced. 35-05.ex19 *Aun así* -> *Sin embargo*. Consolidation ex03 *de otra manera* -> *otra decisión*.
- Dictations that repeated the unit's builder/listening sentence (35-01.ex11, 35-02.ex11, 35-03.ex11, 35-04.ex11, 35-05.ex11) given new sentences.
- Writing prompts that did not pin the answer ("Describe an unreal past choice.") pinned in all lessons and consolidation ex17/18.
- 35-05.ex20–23 asked about an "Alicia" who is not in the story: replaced with four questions about the story (what Fernando does, what Íñigo says, what Fernando tells Íñigo, how it ends). Words in no list added to b1-35-05-voc.json: *ciervo, espíritu*.
- Story *Si hubiera vuelto la mirada* (retelling of Bécquer's "Los ojos verdes"; checked against `sources/becquer-los-ojos-verdes-es.txt`): the old text invented a fiancée (*su prometida*) who asks him to stop, a promise "no volvería", a line "si él quería estar con ella para siempre, tendría que entrar en el agua", "los campesinos dijeron…", *como si algo lo llamara* and a closing "Bécquer terminaba así su leyenda…". Rewritten as an honest outline: Fernando follows a wounded deer on the Moncayo to the spring of Los Álamos; Íñigo warns him of an evil spirit; Fernando returns alone every day, pale and silent, and tells Íñigo of a woman with green eyes; at the spring she says she is not a woman like the others but a spirit of the water and calls him; he steps towards her, feels a cold kiss, falls, the water closes over him. Five *si hubiera …, habría …* sentences kept (taught in b1-35-03), no *como si*, no imperfect subjunctive after a past verb, the last paragraph is the narrator's reflection (no attribution). 5 paragraphs, ~270 words. `characters` and manifest list now include Íñigo; `source` says "Adaptación simplificada de la leyenda … contada con otras palabras". Comprehension questions had rare words and mentioned the fiancée; rewritten.
- Consolidation copies of lesson items left alone.

## 2. Metadata
- Retagged to `pluscuamperfecto-subjuntivo-si` (from `si-clauses`; the wrong answer shows the pluperfect subjunctive or the conditional perfect): 35-03.ex02–05, ex08–17; 35-05.ex02, ex04, ex05, ex09, ex11, ex13, ex15, ex17, ex19; consolidation ex03, ex04, ex05, ex08, ex09, ex11, ex12, ex14, ex16, ex18. 35-05.ex10, ex12, ex14, ex16 and consolidation ex10, ex13, ex15, ex17 stay `hypothetical-structures`.
- New/changed `distractor_skills`: pluscuamperfecto and preterito-perfecto on the replaced options of 35-03.ex13/14, 35-05.ex13, consolidation ex14; futuro-simple/si-clauses on 35-04.ex02; present-tense and preterito-indefinido on 35-01.ex02, 35-02.ex02, 35-05.ex02; subjuntivo-morfologia / preterito-indefinido on 35-04.ex12, 35-05.ex14, consolidation ex13/15; the old `futuro-perfecto` entries are gone with the options. All 108 exercises of this unit are in `tags.lock.json`: after applying, the reviewer must run `python scripts/lock_tags.py es-es b1/hypotheticals-possibilities --update --reason "…"` (and es-latam).

## 3. Goals / checklists
- "Use four/three new … terms" -> "Use the new … words" in all five lessons; 35-01 checklist-you ("what you would do" -> "what I would do"); 35-02 line reworded so it no longer matches b1-32-02 (checklist-shared). 35-03 goal/checklist lost *hubiese*.

## 4. Doubtful
- Story facts about a real work (all checked against the Gutenberg source text of Bécquer, "Los ojos verdes", in `imports/review/es-b1-batch-65-76/sources/`; the reviewer should still web-check the attribution): (1) the legend is by Gustavo Adolfo Bécquer and belongs to his *Leyendas* (the `work` field says "Leyendas"; the source file is from "Obras escogidas", so the collection name is unchecked: unsure); (2) Fernando de Argensola is the eldest son (*primogénito*) of the marquises of Almenar; (3) Íñigo is the family's chief huntsman; (4) the deer is wounded and runs to the spring of Los Álamos on the Moncayo; (5) Íñigo warns that an evil spirit lives in its water; (6) Fernando afterwards goes alone every day and comes back pale; (7) he tells Íñigo he has seen a woman with green eyes; (8) the woman says she is a spirit living in the water and calls him; (9) he feels a cold kiss, falls and the water closes over him. The brief's outline agrees with the text on all nine.
- (unsure) 35-03.ex12 keeps the wrong option *Sí, si habría tenido más tiempo* (conditional perfect after *si*): a real learner error, tagged now `pluscuamperfecto-subjuntivo-si`.
- (unsure) The vocabulary entry *hubiera = had / were to have* in b1-35-03-voc.json is a verb form, not a word; kept (it carries the lesson's point), reviewer may drop it.
- The mixed conditional (*si hubiera … , hablaría …*) is B2 (`mixed-conditionals`): kept out of items and the consolidation challenge.

## 5. Dictionary
Audit of the new story b1-35-ojosverdes (es-es and es-latam): 0 literal compound guesses; 2 "not in the dictionary", both names: `Argensola | Argensola | noun | family name of the hero, Fernando de Argensola (proper name) |` and `Moncayo | Moncayo | noun | mountain range in northern Spain between Aragón and Soria (proper name) |`.

# es-es B1 Unit 71 independent-spanish (b1-36-01 … b1-36-consolidation, story b1-36)

Fixes: `/home/user/parlour-read-a/fixes-independent-spanish.json` (79 fixes); challenges: `/home/user/parlour-read-a/challenges-independent-spanish.json` (6). `check_fixes.py`: 79 fixes, 0 rejected.

| | es-es before | es-es after | es-latam before | es-latam after |
|---|---|---|---|---|
| check-content errors / suspects | 18 / 1 | 0 / 0 | 18 / 1 | 0 / 0 |
| unmet-words hits (6 stems) | 30 | 0 | 35 | 0 |

## 1. Found by reading
- All five grammar screens present the whole earlier course as "integrated" new material without a recap (36-01 narrative, 36-02 opinion/certainty/doubt, 36-03 cause/consequence, 36-04 future/conditional/subjunctive, 36-05 cumulative). Each now opens with a recap naming the units: *indefinido / imperfecto* A2 Units 11 and 21, *antes de / después de* A2 Unit 4, *pluscuamperfecto* B1 Unit 1; *no creo que* B1 Unit 13, *dudo que* B1 Unit 25, *es importante que* A2 Unit 27, *aunque* A2 Unit 28, *estoy seguro de que* B1 Unit 67; *porque / por eso* A2 Unit 5; future A2 Unit 19, *si* + imperfect subjunctive B1 Unit 7, *es posible que* B1 Unit 67; 36-05 adds B1 Unit 69 (*hubiera*). Tips rewritten as natural sentences (they were meta commentary: "Layering is the skill being tested here", "If one thing is worth rechecking…", "Two unrelated 'ifs' live in this unit").
- Later forms as wrong options: *Haya cambiado de opinión* (36-01.ex12), *hayan perdido* (36-03.ex13), *Haya preparado* (36-04.ex13), *Haya buscado* (36-05.ex14): present perfect subjunctive (b1-37). Replaced by real forms of known skills (*Cambiaba, Preparé, Busqué, pierde*) with distractor skills.
- Length/absolute errors rebuilt: 36-01.ex02 (44 vs 26), ex09 (50 vs 37), 36-02.ex02 (62 vs 36), 36-03.ex02, ex09, ex10, 36-04.ex09, 36-05.ex02 (*absolutamente*; length), ex09, ex20–23 (*nunca, ninguna, completamente*; length), consolidation ex13 (62 vs 31), ex16 (*ninguna*). Time words only in wrong options (*tomorrow, yesterday*) removed from the listening items 36-01.ex09/10, 36-03.ex09/10, 36-04.ex09.
- Non-phrase and double-fault wrong options: 36-03.ex12 "Porque información.", 36-01.ex13 "Sea difícil, pero aprendí mucho." (two faults), consolidation ex13 "Es posible que es la opción." rebuilt with one fault each.
- Repeated sentences: dictations that duplicated a listening/builder/fill sentence changed (36-01.ex11, 36-02.ex11, 36-03.ex11, 36-04.ex11).
- Unmet words: *frase, inicia, narración, secuencia, claramente, acumulativa, combina, correctamente, demuestra, nivel, detallada, departamentos, conecta, solucionarlo, grave, miembros, relacionado, perfectamente, elemento, encaja, complejo, desarrollar* (*desarrollar* -> *crear* in 36-04.ex08 and consolidation ex14) and *afecta* (writing answers in 36-02.ex16, 36-05.ex19: rewritten with *es importante para muchas personas*) removed; Spanish bracket glosses on question stems dropped (36-01/02/03/04/05.ex02/ex06, consolidation ex02/ex06/ex09/ex16). I used *bicicleta* and *su jefe* rather than *coche* and *autoridades*, so no es-es/es-latam variant is needed.
- 36-05.ex20–23 (reading) were the generic "idea principal / detalle / elemento / conclusión" stems with tell-absolutes; replaced with four questions on what Marta does and thinks (reading-generic).
- Story *Cinco voces, una historia* (original Parlour text about Marta, 307 words): level and forms are fine (present subjunctive after *no cree que, es importante que, es necesario que*; *si hubiera más recursos … podría*; *si tuviera que elegir … invertiría*; no present perfect subjunctive, no b1-38 forms) and it agrees with 36-02/03/04 (position, transport problem, possibilities). The comprehension questions were full of rare words (*maduración, paliar, consistorio, carruajes, fructífera analogía*) and invented options; rewritten in plain Spanish and true to the text. The story text is unchanged.
- Consolidation copies of lesson items left alone.

## 2. Metadata
- No retags. New distractor_skills: 36-01.ex12 [1] subjuntivo-morfologia, [2] imperfect; ex13 [1] imperfect-subjunctive-forms, [2] subjuntivo-morfologia; 36-03.ex12 [1] subjuntivo-morfologia; 36-04.ex13 [1] subjuntivo-morfologia, [2] preterito-indefinido; 36-05.ex14 same. (36-03.ex13 initially had a distractor skill equal to its own tag: `ds-own-skill`; removed.) After applying, the reviewer must run `lock_tags.py … --update` for Units 65, 67, 69 and 71 (all their exercises are in `tags.lock.json`).

## 3. Goals / checklists
- "Use four/three new … terms" -> "Use the new … words" in all five lessons. checklist-shared fixed in 36-02 ("…words for explaining a position", was equal to b1-34-05) and 36-04 ("…words for future possibilities", was equal to b1-34-02). checklist-you: 36-01 "what you learned" -> "what I learned".

## 4. Doubtful
- (unsure) story metadata of `b1-36.json`: `"type": "classic"` (the other stories use `"classics"`) and `"lesson": 5`; left alone. The core-unit story pairs in the manifest also keep older original stories: `b1-33.json` (*Los testimonios*, a detective and witnesses), `b1-34.json` (*Una opinión cuidadosa*, Marco, with *no creía que hubiera…* and *sino que*), `b1-35.json` (*El camino de Alicia*) and the classic `b1-36-pazosdeulloa.json`; the lesson-05 screens point at the classic (or at `b1-36.json`), but the old reading items asked about those other stories. They are outside this task; the reviewer should decide whether they stay in the manifest, and note that `b1-34.json` contains imperfect subjunctive after past verbs and *sino que* (later forms) in its text.
- (unsure) 36-04 recaps *es posible que* "from B1 Unit 67", which is also the batch's own unit; fine in course order (67 < 71).
- Challenge scenarios: Carlos at his office in Budapest, Meg as student, Daniela in Chile, Carlos's grandmother in Madrid; no invented relatives.

## 5. Dictionary
Audit of b1-36 (es-es and es-latam): 0 "literal compound guess", 0 "not in the dictionary".

# Fix counts per unit
- Unit 65 reported-speech: 86 fixes (58 `kind: target`), 6 challenges.
- Unit 67 complex-opinions: 78 fixes (58 `kind: target`), 6 challenges.
- Unit 69 hypotheticals-possibilities: 95 fixes (57 `kind: target`; 2 are the paradigm table: one `variant: es-es` with *vosotros*, one `variant: es-latam` without), 6 challenges.
- Unit 71 independent-spanish: 79 fixes (55 `kind: target`), 6 challenges.

# Notes for the reviewer
- Checked on a scratch copy of the worktree (fixes applied to es-es, mirrored with `mirror_fixes.py` and applied to es-latam, challenges merged into both `challenges.json`, `build_word_lesson_index.py` rebuilt). The unmet-words numbers need `imports/dictionary/` (the tool reads `imports/dictionary/coverage-ignore.json`); with it present the baselines are the "before" counts above.
- The "before" unmet counts are from the unmodified worktree: Unit 65 24/33, Unit 67 27/39, Unit 69 23/28, Unit 71 30/35 (es-es / es-latam).
- `lock_tags.py` must be re-run (`--update --reason`) for the four units after applying (tags and distractor_skills changed; Unit 69 retags many items to `pluscuamperfecto-subjuntivo-si`).
- The unit 69 *vosotros* row in the new *hubiera* paradigm table is an es-es-only fix; the es-latam fix adds the same table without it. `mirror_fixes.py` lists the pair as "unmatched" (by design).
