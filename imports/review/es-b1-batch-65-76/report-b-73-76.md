<!-- Reader B (Units 73, 74, 75, 76): 459,982 tokens, 32 min (completion notice). -->
# Review report: Spanish B1 Units 73-76 (es-es, mirrored to es-latam)

Common notes. No unit has a story (the four `stories/classics/b1/b1-37..40.json` files exist but no lesson references them: see group 4 of each unit), so the story audit (`audit-reader-coverage`) was not run and the Dictionary group is empty for all four units. Counts below come from a scratch copy of the worktree with the fixes applied (`mirror_fixes.py` for es-latam, index rebuilt, `check-content.py` and `unmet-words.js` rerun), baseline from the same scratch copy before the fixes. Tags changed: the reviewer must run `lock_tags.py --update` for each unit.

## B1 Unit 73 present-perfect-subjunctive (b1-37)

Counts (before -> after):
- check-content es-es: 8 errors / 19 suspects -> 0 errors / 1 suspect; es-latam: 11 / 20 -> 0 / 1 (the 3 extra latam errors were `latam-vosotros`: *hayáis* in b1-37-01 and the consolidation grammar, *os* in b1-37-04). The one suspect left is `vocab-unused` *perspectiva* (b1-37-05): it stays because a conversation scenario lists it in `requiredLemmas`.
- unmet words: es-es 15 -> 1, es-latam 15 -> 1. The 1 left is *completes* (b1-37-01.ex10), a wrong-option form of *completar*, which is listed in that lesson.
- fixes: 88 in the es-es list (3 marked `"variant": "es-es"`) + 2 explicit es-latam fixes = 90; 85 mirror.

### 1. Found by reading
- b1-37-01 grammar: presents the *pretérito perfecto* participles and the present subjunctive as new; no recap. Fix: opens "You know … from A2 Unit 1 and … A2 Unit 27" (es-es keeps *hayáis* and gets a *vosotros* table row, `variant es-es`; es-latam text without *hayáis*).
- b1-37-01.ex01: wrong options "hayis" (non-word, unmet) and "hubieras" (pluperfect subjunctive outside *si*, later). Fix: hayas / hayan / has / habías, ds on has and habías.
- b1-37-01.ex09: wrong option "Espero que llegábamos." carries two faults. Fix: "Me alegro de que llegamos bien." and "…lleguemos bien.", one fault each, ds added.
- b1-37-01.ex10: "Profesor: ¿Ha terminado todo el mundo…? / Alumnos: Sí profesor, nos alegra que hayamos terminado." is unnatural; wrong option "Ojalá terminamos." Fix: Meg / Carlos exchange ("¡Tengo una noticia! Ya he completado mi trabajo final." / "Me alegro de que lo hayas completado."), uses *noticia*, *completar*.
- b1-37-01.ex07: "fiesta de aniversario" and "Lamenta" unmet (*lamentar* is listed in the next lesson). Fix: "fiesta del sábado", "Siente que no hayan venido."
- b1-37-02 grammar: feelings + subjunctive presented as new; example "Me parece maravilloso que hayan encontrado esa oportunidad." (english said "you found"; speaking steps reuse it); tip said Spanish "requires" the perfect. Fix: recap from A2 Unit 27, example "…hayan encontrado trabajo.", softened tip.
- b1-37-02.ex03/05/07/08: *lastimado*, *enterado*, *publicación*/*estupendo*, *acertada* unmet. Fix: "te hayas caído", "nadie haya llegado tarde hoy", new listening item (uses *maravilloso*, *oportunidad*), "esta decisión".
- b1-37-02.ex04: options pena / lástima are feminine after "un gran" (two faults). Fix: alivio / lamentar / reaccionar / cancelar (also uses the two unused verbs).
- b1-37-02.ex09: only the right option had ¡ ! (`tell-punctuation`); wrong option "Siento que no las tengas." answered a different thing. Fix: three ¡Qué alegría que…! options.
- b1-37-02.ex10: length give-away; the right option said "no hayas llegado a tiempo" to a report that was not handed in. Fix: "Es una lástima que no lo hayas entregado." with two single-fault wrong options.
- b1-37-03 grammar and table: "¿Crees que haya salido ya el tren?" (not standard: ¿crees que + indicative) in the screen, and in ex06; recap missing. Fix: "Es posible que haya salido ya el tren." and a recap from B1 Units 13 and 25.
- b1-37-03.ex01: "hubieran" (later). Fix: hayas. ex04: "La explicación del tren … fue impecable" was a second right answer; stem rewritten. ex05 *promesa*, ex08 *extraviadas* unmet: *la reunión*, *perdidas*. ex09/ex10 length give-aways fixed by lengthening the wrong options with one fault each.
- b1-37-04 grammar: *después de que* (B2) in the screen, table, matching (ex06) and vocabulary list; tip appeals to the future perfect (not taught in core); cuando/en cuanto + subjunctive (A2 Unit 27) presented as new; *os mandaremos* (latam). Fix: recap, *después de que* removed everywhere (vocabulary entry replaced by *avisar*), tip rewritten.
- b1-37-04.ex01: wrong option "habrás" (future perfect, later), subject missing. Fix: "tú", options hayas / has / habías / hayan.
- b1-37-04.ex05: blank "_____ de llover" with answer *haya* gave "haya de llover". Fix: "_____ dejado de llover".
- b1-37-04.ex07: *pasajes*, *confirmación* unmet and length give-away. Fix: new sentence with *aviso*.
- b1-37-04.ex09: "En cuanto habré terminado" (future perfect) and "Cuando terminaré" as wrong options. Fix: firmar el acuerdo / revisado el documento with single-fault options (uses *acuerdo*, *documento*). ex10 uses *ordenar*.
- b1-37-05 screen: examples with "vs." and brackets ("Me alegro de que estés aquí (ahora) y … (pasado)"), ¿Crees que llueva…?, *anoche* and *ayer* with the perfect subjunctive (Spain uses the imperfect subjunctive for a finished-day marker; same rule as `perfecto-marker`), Spanish table labels. Fix: three natural examples, English labels, no *ayer*/*anoche* (ex01 and ex06 too).
- b1-37-05.ex01: stem "Espero que Pedro _____ ayer…", wrong option *compraría* (condicional), length give-away. Fix new stem and options.
- b1-37-05.ex03 *comprendido*, ex07 *muchísimo*, ex09 length: *entendido*, *mucho*, longer wrong options. ex10 third option mixed two faults.
- b1-37-05 vocabulary: simultáneo, concluido, distinguir, precisión, indicar (never used, jargon). Replaced by *disfrutar*, *estancia*, *listo*, *malentendido* (words the items need). *perspectiva* stays (scenario `requiredLemmas`).
- Consolidation: *hayen*/*hubieran* options, *superado*, listening item with *rápidamente*/*rapidez*/*elogia*/*tardanza*, length give-away, summary text in jargon, Spanish table labels, "saw the keys" english for *haya visto*. All fixed.
- Writing prompts in 6 lessons were Spanish instructions ("Escribe una frase…"); all now English and pin the person.

### 2. Metadata
- b1-37-01.ex01, 37-02.ex09, 37-03.ex01/ex09/ex10, 37-04.ex01/ex09/ex10, 37-05.ex01/ex09/ex10, cons.ex01/ex07: `distractor_skills` rebuilt for the new options (`preterito-perfecto`, `pluscuamperfecto`, `preterito-indefinido`, `futuro-simple`, `subjuntivo-morfologia`, `present-tense`, `imperfect`). The old `futuro-perfecto` and `condicional-regular` entries are gone with their options. Run `lock_tags.py es-es b1/present-perfect-subjunctive --update` for unit 73.
- All `teaches` stay `subjuntivo-perfecto` or the unit vocabulary skill; no grammar tag moved.

### 3. Goals / checklists
- All six checklist lines were "I understand how to use … in real B1 contexts." Rewritten as "I can …" lines.
- b1-37-01 goal named *hayáis* (latam-vosotros in the shared lesson) and was long; b1-37-03 and b1-37-04 goals had Spanish metalanguage; consolidation goal "fluid mastery". Reworded.
- Consolidation checklist was identical in Units 73-76 (`checklist-shared`). Each is now its own.

### 4. Doubtful
- stories/classics/b1/b1-37.json ("Sherlock Holmes y el hombre desconocido", Conan Doyle) exists but no lesson references it; not read or changed.
- b1-37-04: *tan pronto como* is listed in the vocabulary but taught nowhere before; kept as a listed word (unsure).
- 37-01.ex10 *completes* is flagged by `unmet-words` as a hit although it is a form of listed *completar*; left.
- Recap numbers used: A2 Unit 1 (`preterito-perfecto`), A2 Unit 27 (subjunctive after emotions, `cuando-subjuntivo`), B1 Units 13 and 25 (`opinion-verbs-mood`, `subjunctive-doubt`), taken from the knowledge sheet.
- `perfecto-marker` reasoning for *ayer* + perfect subjunctive is a Spain-usage judgement (unsure); the items are in any case better without it.

### 5. Dictionary
None (no story).

## B1 Unit 74 sequence-of-tenses (b1-38)

Counts (before -> after):
- check-content es-es: 10 errors / 15 suspects -> 0 / 0; es-latam: 10 / 18 -> 0 / 0.
- unmet words: es-es 16 -> 3, es-latam 15 -> 3. The 3 left are inflected forms of verbs listed in that lesson or earlier: *colaborásemos* (an `answers` alternative of b1-38-05.ex02, *colaborar* is listed in that lesson), *colabore* (wrong option, same verb), *reviso* (wrong option, *revisar* listed in b1-37-04).
- fixes: 84 in the es-es list + 1 explicit es-latam fix (*camarero* -> *mesero* in the b1-38-02 screen example) = 85.

### 1. Found by reading
- b1-38-01 screen: no recap of the imperfect subjunctive forms (B1 Unit 7) or the present subjunctive after wishes (A2 Unit 27); "(*-ra / -se*)" (the -se forms are later); grammar labels ("Present frame", "Indefinido frame"); tip "never mix … *Quería que venga*" too strong; jargon title "Past Framing". Fixed: recap, English glosses, softened tip, title "The Imperfect Subjunctive After a Past Verb".
- b1-38-01 vocabulary: *correlación, subordinada, gobernar, tiempo verbal* are grammar jargon (unused or only filler; no scenario lists them). Replaced by *empleado* (ex07); *aconsejar* now used (ex09).
- b1-38-01.ex04: "al pie de la letra la _____ del especialista" (idiom above B1), 13 vs 9 give-away, *ceremonia* fits grammatically. New stem on *guardar reposo*.
- b1-38-01.ex06 matching: right side was grammar metalanguage ("Past -> Imperfect subjunctive"); now meanings.
- b1-38-01.ex07: *aplazar* (listed only in b1-38-04) as a wrong option, give-away. ex09/ex10: wrong options with two faults ("Me recomienda que descansaba.") and length give-aways; ex10 third option changed the meaning. Rebuilt with single-fault options.
- b1-38-02 screen: reported statements (B1 Unit 25) and questions (A2 Unit 14) not recapped; tip imprecise (indicative = information, subjunctive = order). "«¡Ven aquí!» -> Me dijo que fuera allí" (also in ex06 matching, where *fuera* is both *ir* and *ser*): now *Me dijo que viniera*.
- b1-38-02.ex02 *guía*, ex04 *coche* (Spain-only; *vehículo* unused), ex07 *recepcionista*/*quejó*, ex10 *anfitriona* and "Invitados" as a speaker, ex09 give-away and two-fault option. All rebuilt. Vocabulary: *solicitar*, *petición* removed (unused); *vehículo*, *instrucción* now used.
- b1-38-03 is a recap lesson (reported statements and tense shifts are B1 Unit 25, `estilo-indirecto`): screen and goal now say "You know … from B1 Unit 25". ex07 *diseño*, ex09/ex10 give-aways, ex11 instruction in Spanish metalanguage ("Transforma a estilo indirecto"). Vocabulary: *explicar*, *posibilidad* unused, removed.
- b1-38-04 screen: "Spanish boasts a rich variety of communication verbs that modulate authority…", Spanish labels (**Recomendación**, **Autoridad**…), *demandar que, imponer que* (rare), "advertir que… (subj.)". Rewritten plainly. ex04 *prudencia* (unused jargon synonym) -> *resbaladizo*; ex06 "(subj.)"; ex07 *inspector*/*facturas*; ex09 *agencia* (unmet in es-latam) and give-aways; ex10 uses *aplazar*.
- b1-38-05: "B1 speakers articulate stories with multi-layered temporal depth", Spanish table labels, jargon title/grammar field ("Temporal Harmony"). ex04 "Carlos y Lucía celebrarán su boda" contradicts the character facts (Carlos is with Meg): "Mis primos celebrarán su boda". ex07: *mostrador*, *cancelación* unmet, `tell-absolute` *ninguna*/*nadie*, 70 vs 36 give-away (ex09). Vocabulary *articular, armonía, multi-cláusula, coherencia, fluidez* removed.
- Consolidation: table row "Aseguró que vendría mañana" contradicts the backshift rule of b1-38-03 (*al día siguiente*); jargon summary; Spanish table labels; cons.ex02 english lacked the *si* clause; cons.ex05 *guía/calzado*, cons.ex07 *pendientes*.
- Writing prompts in 6 lessons were Spanish instructions; all English now.

### 2. Metadata
- `distractor_skills` rebuilt where options changed: b1-38-01.ex09/ex10, 38-02.ex09/ex10, 38-04.ex09/ex10, 38-05.ex09, cons.ex07 (`present-tense`, `futuro-simple`, `preterito-indefinido`, `imperfect`, `subjuntivo-morfologia`).
- (unsure) b1-38-04 items about *aconsejar/sugerir/advertir/proponer* are tagged `correlacion-temporal-subjuntivo` although the lesson teaches reporting verbs (`estilo-indirecto-ordenes` fits as well); left, since a wrong answer there shows the tense/mood after a past verb. Run `lock_tags.py es-es b1/sequence-of-tenses --update`.

### 3. Goals / checklists
- Six "I understand how to use … in real B1 contexts" lines rewritten. Goals reworded: 38-01 (it named *pluscuamperfecto* main verbs, never practised), 38-02, 38-03 ("Review …", recap), 38-04, 38-05, consolidation. Consolidation checklist no longer shared with Units 73/75/76.

### 4. Doubtful
- stories/classics/b1/b1-38.json exists but no lesson uses it; not read.
- The -se alternatives (*escribiese, viniesen, colaborásemos* …) in `answers` of the fill-blanks are accepted input only, never shown; left (the prompt says the -se forms are later than B1, the knowledge sheet says b1-04-02 listed them but its screen shows only -ra). Remove them if the reviewer wants strict consistency.
- Lesson/screen titles changed for 38-01 and 38-05 only; other generator titles ("Nuanced Reporting Verbs…") left.
- "si terminaba" in cons.ex02 (reported *si termino*) is colloquial-but-accepted; left (unsure).

### 5. Dictionary
None (no story).

## B1 Unit 75 verbs-of-becoming (b1-39)

Counts (before -> after):
- check-content es-es: 14 errors / 15 suspects -> 0 / 0; es-latam: 14 / 18 -> 0 / 0.
- unmet words: es-es 21 -> 0, es-latam 26 -> 0.
- fixes: 85 in the es-es list, 0 explicit es-latam (all mirror; the converter changed *enfadó* -> *enojó* in b1-39-05.ex07).

### 1. Found by reading
- Every screen (b1-39-01 to 05) presents *ponerse*, *quedarse*, *volverse*, *hacerse* and *convertirse en* as new. All of them are taught in B1 Unit 49 (b1-25-01 `verbs-of-change`, which also has *convertirse en* and *pasar de ser … a ser …*). Each screen now opens "You know … from B1 Unit 49" and keeps only what is added; b1-39-04 states that *llegar a ser* is the only new item (b1-25-01 does not show it). Goals reworded to "Review …"; b1-39-05 and the consolidation say the verbs are known from B1 Unit 49 and this unit.
- Spanish grammar terms in screens (*adjetivo, sustantivo, participio*) and Spanish table labels in b1-39-05 ("Rápido y pasajero"…): English.
- b1-39-04 screen: *budista*, *superventas* (rare); vocabulary *budista, culminación, metamorfosis, ideología* never used. Removed/replaced.
- b1-39-05 vocabulary (*espectro, matiz, voluntario, involuntario, silencio, reflexivo, distinguir, maestría*): grammar jargon, six unused; replaced by *duradero, pasajero, saldo*. Screen example "se volvió reflexivo" rewritten.
- b1-39-01.ex01: *se queda nervioso* is possible Spanish (wrong option not clearly wrong): now three options. ex05: `answers` puso/quedó for "The pool water became cold" (both fit); *piscina* unmet. New sentence that only fits *ponerse*. ex07: *factura* (unmet in es-latam), give-away. ex08 *oral* unmet. ex09 give-away.
- b1-39-02: ex02 *billete*, ex03 *batería/móvil*, ex06 *sin blanca* (Spain-only or unlisted; unmet in es-latam) replaced with neutral words; ex07/ex09/ex10 give-aways; *consecuencia* unused.
- b1-39-03: ex04 "A pesar de su riqueza, tiene fama de ser muy ___" also fit *tolerante* and *insoportable* (and Carlos's character was not the subject): stem now describes stinginess. ex08 "nos volvimos muy buenos amigos" is not Spanish (*nos hicimos amigos*): rewritten with *se volvió más serio*. ex01 *desengaños*; ex02 *constante*; ex05 *distante*; ex10 *ladra*; ex07/ex09 give-aways; ex10 tell-punctuation.
- b1-39-04: ex04 give-away (13 vs 9) and *incansable*/*barreras*; ex07 `Nadie` tell-absolute and *invento/revolución/mundial* unmet; ex09 *arquitecto*; ex10 *banda* and the wrong option "se hizo un éxito total" (acceptable colloquial Spanish, nearly a second right answer); *nación, tecnológico, animales, ministro, universidad* unmet.
- b1-39-05: ex01 "nos pusimos helados" not clearly wrong; ex02 *decano*; ex08 "se volvió un experto" is not standard (*volverse* + noun): *se hizo experto*; ex07 `todo`/*nerviosismo* issues; ex09 give-away; ex10 *boutique*.
- b1-39-05.ex04: wrong options *espectro*, *maestría* were unlisted jargon. 
- Consolidation: cons.ex02 `answers-alternatives` (any adverb fits) -> single answer *sordo*; cons.ex03 *éticas*; cons.ex05 53 vs 28 give-away with *posición/destacada*; cons.ex07 give-away.
- Writing prompts in 6 lessons were Spanish instructions; English now.

### 2. Metadata
- No `teaches`/`category` changes needed; no `distractor_skills` (all wrong options are forms of the tested `verbs-of-change`). 39-02/39-03/39-05 vocabulary lists changed, so the vocabulary skill counts per lesson change (`validate-content --warnings` may report fewer than 6 vocabulary items in b1-39-05: the lesson's vocabulary items are ex02/04/06/07 only). Run `lock_tags.py es-es b1/verbs-of-becoming --update`.

### 3. Goals / checklists
- Six "I understand how to use … in real B1 contexts" lines rewritten as "I can …" lines; goals reworded (recap wording); consolidation checklist no longer shared. b1-39-05 title/grammar field "Mastering the Spectrum of Change" and "Comparative Synthesis" -> "Choosing the Right Verb of Change".

### 4. Doubtful
- stories/classics/b1/b1-39.json exists but no lesson uses it; not read.
- b1-39-02 contains idioms (*quedarse de piedra*, *boquiabierto*) listed as vocabulary; kept.
- b1-39-03 `loco` after *volver* in a transitive use (*Esa música me vuelve loco*) is shown on the screen next to the reflexive pattern; correct Spanish but a different construction (unsure whether to keep).
- *saldo* (phone credit) is used in two items; it is met in es-es and es-latam, listed now in b1-39-05 anyway.

### 5. Dictionary
None (no story).

## B1 Unit 76 connectors-prepositional-regimes (b1-40)

Counts (before -> after):
- check-content es-es: 14 errors / 19 suspects -> 0 / 0; es-latam: 14 / 20 -> 0 / 0.
- unmet words: es-es 12 -> 1, es-latam 18 -> 1. The 1 left is *impresionó* (b1-40-04.ex07), an inflected form of *impresionar*, which is listed in that lesson.
- fixes: 90 in the es-es list, 0 explicit es-latam (b1-40-01-ex.json differs between the courses only in ex10: *fuera* / *afuera*; the new ex10 options are the same in both, so one `set` fix serves both).

### 1. Found by reading
- b1-40-01 is a recap lesson (`verbos-regimen-preposicional`, b1-29-03, B1 Unit 57: *acostumbrarse a, adaptarse a, empezar a, darse cuenta de*) presented as new: screen now opens "You know from B1 Unit 57 …", goal says "Review … and learn more"; title had Spanish metalanguage ("Régimen Preposicional"). Vocabulary *régimen*, *preposición* (jargon, used as wrong options) replaced by *acordarse de* (on the screen, had no entry).
- b1-40-01.ex01 "Anoche soñé con que volaba" is not standard (*soñé que volaba*): now "soñé con mis abuelos". ex04 options were jargon words and an infinitive: now "Mi hermano se negó a pagar más" (only the reflexive *negarse* fits). ex07 invented "la boda de Carlos" (Carlos is with Meg): "la noticia del concierto". ex09/ex10 give-aways ("dependo con ti" had two faults; "Sueño con el tiempo" was not a reply). ex06 now holds *enterarse de, confiar en, negarse a, acordarse de* literally (they were unused).
- b1-40-02: *pero* (A1) not recapped; Spanish table labels; vocabulary *adversativo, sustituir, limitar* unused jargon. ex05 `answers` pero/aunque for an English "but" (`answers-alternatives`): narrowed to *pero*. ex08 *coche* (Spain-only): *camisa*. ex09: the wrong option "No fui, pero que me quedé" was a non-phrase and the natural "No fui a la fiesta, pero me quedé estudiando" must not be an option; length give-away. ex04: *afirmación* fit "una pequeña …" grammatically. ex07: `nada` only in a wrong option, give-away. *disfraz, misterio, tono* were unlisted words used in items: added to the vocabulary list.
- b1-40-03: Spanish metalanguage in the vocabulary (*abstracto, cualidad, sustantivar*, used as wrong options; *cualidad* also fit "una gran … para viajar"); *lo que* (B1 Unit 39) not recapped. ex02 (*bueno*, but *mejor* fits too) and ex05 (*malo*, but *peor/difícil* fit): hint added. ex07 `Nadie` tell-absolute; ex09/ex10 give-aways, *clave* unmet; ex08 *comprender* unmet.
- b1-40-04: screen and goal fine apart from Spanish terms (*adjetivo, adverbio*); vocabulary *enfático, intensidad, grado, complicado, darse cuenta de* unused (the last is B1 Unit 57). ex05 hint (*difícil* vs *duro, largo*); ex07 *muchísimo*; ex09 give-away + tell-punctuation + *física*; ex10 tell-punctuation; ex11 and cons.ex08 instructions in Spanish with the answer quoted.
- b1-40-05: "Fluency at the B1 threshold requires flawless handling of connecting tissue", *riquezas, aspirar a, rigurosa, complejo, planificación* (above B1 or unmet); Spanish table labels; vocabulary: six of ten unused. ex04 ("metodología sumamente rigurosa" with gender-mismatched options) became a fill-blank on *fascinante*; ex07 64 vs 37 give-away; ex10 give-away and *bienvenida*.
- Consolidation: Spanish summary and table labels; cons.ex05 *circunstancias externas, capacidad de superación*; cons.ex06 *preposiciones*; cons.ex07 two wrong options failed the same way and were short; *emocionante* unmet.
- Writing prompts in 6 lessons were Spanish instructions, four with the answer quoted in them; all English now.

### 2. Metadata
- `distractor_skills` unchanged in this unit (no wrong option is a form of another skill). b1-40-05.ex04 changes type to `fill-blank` (still `vocabulary`/`b1-connectors-prepositional-regimes-vocab`).
- All four units are locked in `tags.lock.json` ("read-through, all lessons", 2026-10-07). On the scratch copy `validate-content.py` reports "locked tags changed" for 23 items per course, all of them the `distractor_skills` I rebuilt in Units 73 and 74: b1-37-01.ex01/ex09/ex10, 37-02.ex09/ex10, 37-03.ex09/ex10, 37-04.ex01/ex09/ex10, 37-05.ex01/ex09/ex10, b1-37.cons.ex01/ex07, b1-38-01.ex09/ex10, 38-02.ex09/ex10, 38-04.ex09/ex10, 38-05.ex09, b1-38.cons.ex07. Nothing else fails. After applying: `lock_tags.py es-es b1/present-perfect-subjunctive --update --reason "…"` and the same for `b1/sequence-of-tenses` (and es-latam).

### 3. Goals / checklists
- Six checklist lines ("I understand how to use … in real B1 contexts") and the consolidation goal/checklist rewritten; goals of 40-01, 40-02, 40-03, 40-05 reworded, 40-05 and 40-01 titles/grammar fields cleaned.

### 4. Doubtful
- stories/classics/b1/b1-40.json exists but no lesson uses it; not read.
- b1-40-02 teaches *no solo … sino (que) también* in a table row and vocabulary entry (`correlativos-no-solo-sino` is taught in the cultura lesson b1-cambiosocial-05); no item is tagged with it, left as part of the *sino* pattern (unsure).
- b1-40-04 title "Emphatic Lo: Lo + Adjective + Que (How... It Was!)" left; its items are tagged `lo-neutro-abstraccion`, taught in b1-40-03 (same unit, earlier lesson).
- *impresionó* flagged by `unmet-words` although *impresionar* is listed in the lesson.

### 5. Dictionary
None (no story).

## Fix counts per unit
- Unit 73 present-perfect-subjunctive: 90 fixes (88 es-es incl. 3 `variant es-es`, 2 explicit es-latam); 6 challenges.
- Unit 74 sequence-of-tenses: 85 fixes (84 es-es, 1 explicit es-latam); 6 challenges.
- Unit 75 verbs-of-becoming: 85 fixes (all es-es, mirror to es-latam); 6 challenges.
- Unit 76 connectors-prepositional-regimes: 90 fixes (all es-es, mirror to es-latam); 6 challenges.
Files: `/home/user/parlour-read-b/fixes-<unit>.json` and `challenges-<unit>.json` for each unit above, plus this report.
