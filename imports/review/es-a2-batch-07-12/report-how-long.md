# Report: es-es A2 batch 07-12, reader A (units 7, 8, 9)

## Unit 7 how-long (a2-07-01 .. a2-07-consolidation, story a2-07)

Fixes file: fixes-how-long.json (45 fixes, all pass scripts/check_fixes.py, 0 rejected; applied to a scratch copy check-content gives 0 errors). Challenges: challenges-how-long.json (6).

### 1. Found by reading
- a2.07.01.ex12, a2.07.05.ex13, a2.07.05.ex15: check-content length give-aways. ex12: "desde el año" was also not clearly wrong; options now "desde hace dos años" / "desde dos años" / "desde hace enero". ex13: right option cut to "Para ser profesora de español." (met words; removes enseñar, universidad, vietnamita) with two equal-length wrong options. ex15: wrong options lengthened ("Viajan a Ninh Bình en tren.", "Estudian español en casa.").
- Wrong options that are natural answers: a2.07.01.ex14/ex15, a2.07.02.ex15/ex16, a2.07.03.ex16, a2.07.04.ex15, a2.07.05.ex16, consolidation ex14/ex15/ex16. "Desde enero" / "desde el año pasado" answer ¿Cuánto tiempo…? naturally and "Desde hace un año / tres meses" answer ¿Desde cuándo…? naturally. Each wrong option now has one clear fault (*desde un año*, *desde hace enero*, *desde hace el año pasado*, *desde tres meses*).
- Self-third-person dialogues (a speaker asks the partner in the plural about the two of them): a2.07.01.ex15, a2.07.02.ex16, a2.07.04.ex15/ex16, a2.07.05.ex18, consolidation ex16. Reassigned to Kaylee, Daniela, Lauren or Lucía asking a singular question.
- a2.07.03.ex15 and consolidation ex15: "¿Desde cuándo conoces a Lucía? / Desde el año pasado" contradicts the story (they meet Lucía for the first time in 07-05). Now Daniela asks about Meg / Carlos.
- a2.07.05.ex09: "Lucía practica español con nosotros desde hace tres semanas" contradicts the story (they meet her that afternoon); now about Meg (a year). a2.07.05.ex05 said two months for Lucía; the story says three.
- a2.07.05.ex17: in the story Meg tells Lucía, not Carlos; Lucía now asks.
- a2.07.03.ex13: both wrong options have two faults; now one fault each.
- a2.07.03.ex17 / ex19: *practicado* first listed at a2-07-04: use *estudiado*.
- a2.07.04.ex17: English prompts do not fit the answers ("practise … for two weeks", "speak … since January"): now "have been practising / speaking".
- a2.07.05.ex08: *vietnamita* in no vocabulary list: added to a2-07-05-voc.json.
- Consolidation copies/duplicates: ex02 (copy of 01.ex03), ex08 (02.ex12), ex19 (03.ex18), ex20 (05.ex21) varied; ex12 was identical to ex07 (same builder), changed.
- Grammar a2-07-02/04/05: the same two-row table on all five screens: 02, 04 and 05 now have their own. a2-07-05 text says "combine the pretérito perfecto" but its 4th example was present tense (and repeated 07-04): now *Hemos viajado juntos desde hace tres meses.*
- Story a2-07: *deberían visitar* (conditional, Unit 26) → *pueden visitar*; «Espero que nos volvamos a ver pronto» (subjunctive, Unit 27) → «¡Hasta pronto!». Comprehension: Q1 "¿De qué trata principalmente la historia?" is generic → asks what Carlos and Meg do that afternoon; Q2 *vino* (preterite) → *ha venido*; Q3 options *hablaba* (imperfect) and *perdieron* (preterite) → present / perfecto.
- No perfecto + finished-past marker found: every *el año pasado / el mes pasado / la semana pasada* in the unit follows *desde*.

### 2. Metadata
- No defects found: every item has category and one `teaches`; reading items (07-05 ex11-15) carry none; no `distractor_skills` needed.

### 3. Goals / checklists
- a2-07-01 checklist and a2-07-04 checklist "…how long **you** have…" (checklist-you) → "…how long **I** have…". Challenge canDo copied after the fix.
- Doubtful: a2-07-05 goal "Talk about recent experiences and how long…" promises "recent experiences", which the lesson only practises through *desde*; left.

### 4. Doubtful
- (unsure) The unit repeats the same shapes (five or six "Which sentence is correct?" items per lesson, matching ex06 re-listing ex01 pairs, "Nos conocemos desde hace tres meses" in screens and items while 07-04 says "desde el año pasado" for the same pair); not fixed, a rewrite.
- (unsure) a2.07.05.ex02 stem mixes a Spanish sentence with English ("Lucía vive en Hanói ___ enero. Which expression fits?"); check-content does not flag it.
- (unsure) Story a2-07 lists Daniela, Lauren, Kaylee as characters but they do not appear; the story uses *le/les* (indirect object pronouns, Unit 25) and *ya han viajado*; story left.
- (unsure) *llevar* is listed in a2-07-03 but first used in 07-05 questions (*lleva*), never practised in 07-03.

### 5. Dictionary
- The audit lists no "literal compound guess" and no "not in the dictionary" word apart from 2 names (Ninh Bình). None to import.

## Unit 8 making-responding-invitations (a2-08-01 .. a2-08-consolidation, story a2-08)

Fixes file: fixes-making-responding-invitations.json (75 fixes, 0 rejected by scripts/check_fixes.py; on a scratch copy check-content has 0 errors and one suspect, *tortilla*, which only clears when the word-lesson index is rebuilt after the vocabulary fix is applied). Challenges: challenges-making-responding-invitations.json (6).

### 1. Found by reading
- Taught-later (12 ERRORs): the unit teaches *¿Te gustaría…?* / *Me gustaría* (`polite-softening`, Unit 26, conditional) in a2.08.01 ex07, ex08, ex09, ex11, ex13, ex15, a2.08.02 ex02, ex03, ex08, ex09, a2.08.03 ex08, ex09, a2.08.04 ex07, ex08, ex09, a2.08.05 ex08, ex09 and the a2-08-01 grammar screen. Replaced by *¿Puedes + infinitive?* / *Puedo ir* (poder, taught with querer in Unit 10) and *quiero*; the 08-01 screen is rewritten with *quieres / puedes* and a "You know querer and poder from Unit 10" line.
- The unit's grammar screens 08-02, 08-03, 08-04, 08-05 present *ya* and *todavía no* + pretérito perfecto (Unit 2) as new: each now opens "You know … from Unit 2". The 08-02 text said *ya* goes "before the participle or after the auxiliary" while its example puts it before *he*: fixed. The 08-05 tip claimed that *Ya he preparado la comida* answers an invitation "without needing a separate sí": false, replaced.
- The 08-01 screen carried the ya/todavía no table and the same table was on all five screens: each lesson now has its own.
- a2.08.02.ex15: "¿Quieres venir a cenar? / Ya he preparado la cena." is a non sequitur; now Daniela invites, Meg answers *Lo siento, ya he hecho un plan.* (person-form distractors kept).
- a2.08.01.ex15 wrong options "Sí, todavía no." and "Sí, ya he." were garbled; replaced.
- a2.08.04.ex02/04/05: *tradicional* unmet (b1): *típica/típico*. ex12: English "drinks" for *la bebida*. ex17: prompt "you have already prepared the food" but the stored answer is *Ya hemos preparado…*: prompt now "you and your friends".
- Length give-aways: a2.08.05 ex05, ex12, ex14, ex15, ex16; consolidation ex08 (also tell-time-word *ayer*: a wrong option "He cocinado ayer" with the perfecto; options rebuilt with *la cena*).
- Unmet words: a2.08.05.ex12 *tortilla* (added to the a2-08-05 vocabulary list: the story and the question need it; *paella*, *sopa*, *enseña* removed), ex13 *veces* (a2-09-01), ex14 *enseña*, ex15 *dan* (a2-12-02). ex13 is now "¿Ha probado Kaylee este plato?" (it was a yes/no reply to an open question).
- tell-punctuation on ex02 of every lesson (only the right option begins with ¿): wrong options are now questions of the same shape and similar length.
- es-es dialogue with *ustedes* between friends: a2.08.03 ex05, ex07 → *vosotros* (`"variant": "es-es"`); es-latam keeps *ustedes*. Story: «¿Habéis probado ya este plato?» (es-es only) after a shared fix that drops *alguna vez* (Unit 9 skill) from the story line.
- Duplicate dialogues with the speakers swapped: a2.08.05.ex17/ex18 (= 04.ex16/ex15) and consolidation ex16: replaced. Consolidation copies ex03, ex19, ex20 varied.
- Story a2-08: Q1 "¿Cuál es el acontecimiento principal del relato?" is generic (reading-generic) → "¿Dónde cenan los amigos?"; Q3 had *llegaron* (preterite), *se habían equivocado* (pluperfect, B1), *tenían* (imperfect): present tense. *Mientras cocinan* (cuando-mientras, Unit 13) → "Cocinan juntos y hablan" (unsure).

### 2. Metadata
- Items whose wrong options are sentences of another function (invitation vs *ya*/*todavía no* sentences) were tagged `querer-poder`; per the rulebook (replies answering a different question → unit vocabulary) retagged `a2-making-responding-invitations-vocab`: ex02, ex05, ex14 (08-01), ex02 (08-03), ex02, ex05 (08-04), ex02, ex05 (08-05), ex14 (consolidation). The items that moved from `polite-softening` to *puedes* keep `querer-poder` (builders, word-order choice) or the vocabulary skill (acceptance choices).
- a2.08.01.ex15 was tagged `ya-todavia-no` although nothing in it tested that.
- consolidation ex15: "Ya preparo la cena." is a well-formed present: `distractor_skills` {"2": "present-tense"} added; ex16 keeps its entry.
- a2.08.01.ex16 structured-writing: with *quieres* and *puedes* both natural, prompts now pin the stored answers.

### 3. Goals / checklists
- Checklists "I can say that **you** have …" (a2-08-02, a2-08-03, a2-08-04; check-content flagged only 08-04) → "I can say that I have …". Challenge canDo copied after the fix.
- The unit's goal lines promise no grammar that the lessons do not practise.

### 4. Doubtful
- (unsure) The unit teaches no skill of its own (the registry lists no grammar for Unit 8): lessons 02-05 recycle Unit 2's *ya*/*todavía no* items. The invitation skill (`querer-poder`) is A1; nothing was added, the skill list is frozen.
- (unsure) Carlos and Meg are a couple living together, yet 08-01 and 08-05 dialogues have Meg invite Carlos to a party/celebration; left.
- (unsure) Story a2-08 uses *les enseña*, *les muestra*, *le dan* (Unit 25 pronouns), *Lucía promete enseñarles*; left.
- a2.08.05.ex16 wrong options are both unrelated to the invitation; a2.08.04.ex13 option 2 contains two oddities (*ya no*, order); left.
- After applying, rebuild the word-lesson index (*tortilla* is still reported unmet until then).

### 5. Dictionary
- Audit: not in the dictionary 0, literal compound guess 0. Nothing to import.

## Unit 9 experiences (a2-09-01 .. a2-09-consolidation, story a2-09)

Fixes file: fixes-experiences.json (39 fixes, 0 rejected by scripts/check_fixes.py; on a scratch copy check-content gives 0 errors and 0 suspects). Challenges: challenges-experiences.json (6).

### 1. Found by reading
- tell-absolute (16 ERRORs): *Nunca* / *nunca* appeared only in wrong options (a2.09.01 ex02, ex14, ex15; 09-02 ex02; 09-03 ex02, ex15; 09-04 ex02, ex15; 09-05 ex02, ex18; consolidation ex01, ex14). Wrong options are now one-fault non-phrases (*Sí, visitado la playa.*, *Sí, he visto muchos.*) or, in the ex02 items, other questions (*¿Quieres visitar la playa mañana?*, *¿Cuándo vas a visitar la playa?*), which also removes the tell-punctuation suspect (only the right option started with ¿).
- Length give-aways: a2.09.04.ex10 (*restaurant* 10 vs *never* 5: wrong options now *excursion*, *fisherman*), a2.09.05.ex12, ex13, ex14. Unmet words: ex11 *propone*, ex12 *ninguno*, *pesquero*, ex13 *tantas*, *juntas*, ex16 *tantas*, *juntas*.
- a2.09.05.ex13 asked "¿Qué pregunta Daniela…?" with options in reported speech ("Si han visto…", Unit 14): options are now the direct questions. es-es gets *¿Habéis…?* (`"variant": "es-es"`, a second `set` after the shared one); the story line is also *¿Habéis visto…?* in es-es.
- a2.09.05.ex16/ex17: in the story Daniela asks and Carlos has never been to such a port; ex16 had Meg ask Carlos with plural *¿Han visto…?* and ex17 gave Carlos's answer to Meg. Now Daniela asks Carlos (ex16), Meg asks Carlos (ex17).
- a2.09.consolidation.ex11: wrong option *Nunca probé el marisco.* is a preterite (Unit 11) and a correct sentence (a second right answer); its `distractor_skills` ({"1": "preterito-indefinido"}) removed with it.
- Tips that are false: 09-03 "repeating *alguna vez* in the answer just sounds unnatural" and 09-04 "the answer never repeats it" (*Alguna vez he visitado ese pueblo* is fine, and a2.09.02.ex12 uses it): reworded.
- The same *alguna vez* / *nunca* table is on all five screens: 02 to 05 now have their own (09-01 keeps it, because it lists *nunca*, see Doubtful).
- Consolidation copies/duplicates: ex01, ex02 (flagged), and ex14, ex15, ex16 (the 09-01, 09-01 and 09-05 dialogues with the speakers swapped) varied.
- Story a2-09: *olvidarán* (future, Unit 19) → *van a olvidar*; *mientras todos contemplan* (Unit 13) → "todos contemplan" (unsure); Q1 "¿De qué trata principalmente la lectura?" is generic (reading-generic) → "¿Adónde van los amigos en la excursión?".

### 2. Metadata
- No tag defects found. (All retags in Unit 8 and the removed `distractor_skills` in consolidation ex11 change locked tags: run `scripts/lock_tags.py es-es a2/<unit> --update --reason …` after applying; validate-content fails the 24 locked exercises until then, nothing else.)
- (unsure) Items that test *nunca* itself (builders, fill-blanks) are tagged `alguna-vez`; the skill for negative words (`negation`, Unit 31) is later, so no better tag exists.

### 3. Goals / checklists
- a2-09-02 checklist "I can say that **you** have never…" → "I have never…" (challenge canDo copied after the fix).
- Doubtful: 09-04 goal "familiar experience questions" is vague but promises nothing the lesson does not practise.

### 4. Doubtful
- (unsure) *nunca* is drilled in a2-09-01 (ex05, ex08, ex09, correct options) before its own screen and vocabulary entry in a2-09-02; it is met through the 09-01 table row, so no unmet-word is raised. Replacing the 09-01 *nunca* items with *No, no he…* would be cleaner.
- (unsure) 09-01 text says *alguna vez* goes "after the auxiliary or near the end"; the examples put it after the participle (*¿Has alguna vez visitado…?* is rare).
- (unsure) Story: *las comparan* / *les explica* (object pronouns, Units 12 and 25); left.
- The 09 negative-answer items repeat one pattern (Sí / No, … / Sí, nunca …) in about thirty items.

### 5. Dictionary
- Audit: not in the dictionary 0, literal compound guess 0. Nothing to import.

## Fix counts
- Unit 7 how-long: 45 fixes (challenges 6)
- Unit 8 making-responding-invitations: 75 fixes (challenges 6)
- Unit 9 experiences: 39 fixes (challenges 6)

Notes for the applier: the es-es-only fixes carry `"variant": "es-es"` (a2.08.03 ex05 / ex07, the a2-08 and a2-09 story lines, a2.09.05.ex13 second `set`); es-latam keeps *ustedes*. After applying the vocabulary additions (*vietnamita* in a2-07-05, *la tortilla* in a2-08-05) rebuild the word-lesson index, or check-content keeps reporting them as unmet.
