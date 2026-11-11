# es-es B1 Unit 7 giving-advice (b1-04-01 … b1-04-consolidation, story b1-04): reader report

Fixes: 81 in fixes-giving-advice.json (scratch copy: check_fixes 0 rejected, check-content 0 errors / 0 suspects, unmet-words clean except two scanner artefacts, see group 4). Challenges: 6 in challenges-giving-advice.json.

## 1. Found by reading
- b1-04-01 grammar: tener que (A1), commands (A1/A2 Units 23–24) and deberías (A2 Unit 26) were presented as new -> recap opening; the screen now states what the lesson contrasts.
- b1-04-02 grammar: the conditional for advice is A2 Unit 26 (recap); the only new item is the phrase *Si yo fuera tú*; examples with *que fuera más segura* (relative que + imperfect subjunctive) and *Si tuviera más información* (tuviera, b1-38) rewritten; the screen now says *fuera* is learnt as a ready-made phrase. ex15 answer 2 had *que fuera más segura* -> "Buscaría una alternativa más segura."
- b1-04-03 grammar: present subjunctive is A2 Unit 27 -> recap. *alguien que conozca / tenga* (relative que before b1-05-04) in grammar ex1 (+ speaking), ex03, ex11 (dictation), ex15 answer 2, and in 04-01 ex03/ex06 and 04-04 ex14/ex16: all reworded (con tu profesor, con un amigo de confianza, una alternativa con menos consecuencias, una solución para resolver). *mientras estés enfadado* (mientras + subjunctive is not taught) -> *cuando estés enfadado* in grammar, ex10.
- b1-04-01 ex06 prompt line "quizá sea mejor" (quizá + subjunctive, b1-13) -> "es mejor". Option 2 "Tienes que haber hablado…" and the three options with "alguien que tenga experiencia" rewritten (one fault each).
- B2 reproach form *Deberías haber comprobado* (regrets-reproaches b2-10-03) as a wrong option/gloss in 04-01 ex07 and consolidation ex10 -> replaced by *Deberías comprobar* / *Vas a hacerlo*.
- b1-04-05 grammar: *de lo que parece* (neuter lo que, b1-20/b1-40) and *de lo contrario … asumir un riesgo innecesario* (asumir, innecesario in no list) -> rewritten; also in ex13 (listening), consolidation ex12 and the speaking step. 04-05 ex15 asked "si el resultado no fuera el esperado" (fuera outside the set phrase) -> "si el plan no sale bien".
- Unmet words: frase/obligación/estricta/hipotético/forma/verbal/significa/directa/finalidad/combina/expresa/subjuntivo (in Spanish glosses of English question stems; removed), prudente (04-01 ex13, listed only in 04-02), cometer, error, demasiado, revisarlo, asumir, innecesario, esfuerzo (consolidation ex09), revises (consolidation ex11), pico/cuervo/zorro (04-05 questions). New vocabulary entries: revisar (b1-04-01), esfuerzo (b1-04-04), cuervo, zorro, pico (b1-04-05).
- Wrong options with two faults / by meaning only / natural replies: 04-04 ex06 opt 3 (no que + future), ex12 opt 2 (*a pesar de que* + future differs by meaning only), 04-01 ex06 (past forms), 04-01 ex12 (changed content).
- 04-02 ex06: last line "¿Por qué esperarías?" did not follow "leería el contrato primero" -> "¿Por qué lo leerías primero?".
- 04-02 ex10: garbled wrong English "I had waited before deciding" -> "I waited before deciding."
- check-content errors fixed: length give-aways 04-01 ex02, ex12; 04-02 ex07; 04-05 ex02, ex07; consolidation ex10, ex11 (also removed "yesterday" that appeared only in a wrong option). Suspects: 04-01 ex08 (answers revisar/comprobar for "check": narrowed to revisar, english "review"); consolidation ex15 (precaución/cuidado: narrowed to precaución).
- Story b1-04 rewritten (227 words, same four paragraphs and events) in plain Spanish of my own: the fox's flattery is not Samaniego's verse and the moral is paraphrased in the fox's last line (casi siempre quiere algo). The fox now gives advice with the unit's forms (*Si yo fuera usted*, *Le recomiendo que cante para que yo pueda oírlo*, *Debería pensar más*). Comprehension questions (story file) and 04-05 ex09–ex12 rewritten to ask what the animals want, say and do (the old ex11/ex12 asked what the crow "understood" and what advice "the crow gave": neither is in the story).

## 2. Metadata
- b1-04-01.ex03: `category` vocabulary -> grammar and `teaches` b1-giving-advice-vocab -> deber-vs-tener-que (the blank is the infinitive after deberías).
- distractor_skills added/changed: 04-01 ex06; 04-02 ex06; 04-04 ex06, ex12; 04-05 ex15 unchanged; consolidation none new.
- 04-04 ex13 has `distractor_skills` {"1": "porque-y-por-eso"} for an option that fails only by meaning (purpose vs reason); left (unsure).
- Locked tags changed on 04-01.ex03 (and any exercise whose distractor_skills I set): `lock_tags.py es-es b1/giving-advice --update --reason …` after applying.
- No item is tagged with a skill whose screen is in a culture or latam lesson (checked every `teaches`/distractor in b1-04).

## 3. Goals / checklists
- Word counts: 01 "four" -> six (consejo, aconsejar, deber, precaución, contrato + revisar); 02 "three" -> six; 03 "three" -> five; 04 "three" -> five (esfuerzo added); 05 "three" -> nine (riesgo, aplicar, resultado, propuesta, alabar, analizar + cuervo, zorro, pico). Goal and checklist line both changed.
- 04-05 goal "Understand an adapted Aesop fable about poor judgement" still fits. canDo of each challenge = first checklist line.

## 4. Doubtful
- ORDER PROBLEM (reported, not solved): b1-04-02 (`hypothetical-structures`, "si + imperfect subjunctive") teaches only A2 conditional advice plus the phrase *Si yo fuera tú*; no screen of the unit teaches the imperfect subjunctive forms (`imperfect-subjunctive-forms` is B2, b2-15-01; `correlacion-temporal-subjuntivo` b1-38-01 teaches their use). b1-08-04 (`si-clauses`, Unit 15) teaches both realistic *si* + present + future (examples *Si perdemos el tren, cogeremos el siguiente*) and hypothetical *si* + imperfect subjunctive + conditional (*Si perdiéramos…, tendríamos…*, *Si tuviera más tiempo, viajaría…*), still without a forms screen. A learner would need first: the -ra forms (fuera, tuviera, perdiéramos), then si-clauses. I made b1-04-02 honest by presenting *Si yo fuera tú* as a set phrase and removing other imperfect-subjunctive forms; the skill title still promises more.
- *si* + present + future (`si-clauses`, b1-08-04) is used in 04-04 (grammar example 3, ex07, ex08, ex10), 04-05 (ex03, ex19), consolidation ex09 and the speaking steps. Left; same point as Unit 5 (unsure whether to treat as known A2 usage).
- *ya que* (04-04 grammar example 4, ex09, ex12) is a causal connector not taught elsewhere before b1-06-04/b1-16; left as an example phrase (unsure).
- 04-02 ex09 `arriesgaría` and 04-02 ex12 English glosses ("would wait", "few days") are reported by unmet-words.js; both look like scanner artefacts (the builder has `solutions`, so the reflexive check misses *me arriesgaría*; arriesgarse is listed in this lesson), not defects (unsure).
- Bracketed glosses ("Spanish [English]") on multiple-choice options are the course's accepted gloss format, not English-in-target; kept, and my replacement options carry them too.
- Consolidation items copy lesson items (ex06 = 04-03 ex06, ex14 = 04-03 ex13, ex13 ~ 04-05 ex06, ex08/ex12/ex16 ~ lesson items); left alone.
- Story metadata: `source` says "Adapted from public-domain fables by Aesop and Félix María Samaniego" and `work` "Fábulas morales (1781)". The retold text uses neither author's wording; for the reviewer's web check: Samaniego's *Fábulas morales* date (1781), and that the cheese-and-flattery fable is attributed to Aesop (also Phaedrus/La Fontaine). Suggest the source line "Adapted from the fable of the crow and the fox (Aesop)".
- Story details to check against the fable: crow steals cheese from a farm window (original text, kept); fox cannot climb; flattery makes the crow sing; cheese falls and fox eats it. My version has the cheese fall to the ground rather than being caught in the air.
- ex13 (04-01) wrong options "Deberías…" vs "Sería mejor…": both are advice, only "most direct" separates them; fine for the question (unsure).

## 5. Dictionary
oírlo | oír | verb | to hear
