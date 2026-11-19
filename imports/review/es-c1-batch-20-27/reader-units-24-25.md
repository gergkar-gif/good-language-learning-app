# Reader report: Units 24 (negotiation-mediation) and 25 (language-variation), es-latam C1

Fix files: `.scratch/fixes-negotiation-mediation.json` (25 fixes, 3 unsure), `.scratch/fixes-language-variation.json` (53 fixes, 6 unsure). Both applied cleanly (all `old` unique) to a scratch copy; after the fixes `check-content` shows 0 errors for both units, `check_es_c1_forms` 0, `check_unit_refs` 0, no `!!` in the render, and `unmet-words` (index rebuilt in the scratch copy) shows only inflected forms of listed verbs plus the false positives listed under Doubtful.

# UNIT 24 negotiation-mediation (25 fixes)

## 1. Found by reading
- c1-24-01-a-gr example 3 | «Les instamos a que acerquen posturas» is plural leísmo (*instar* takes a direct object; the course's own Unit 25 norm rejects *les* for people except singular male *le*; es-latam) | «Los instamos a que acerquen posturas».
- c1-24-01.ex04 | option «A verbal counter-proposal …»: "verbal" also means written, so it overlaps the right option «A written…» | «A spoken counter-proposal …».
- c1-24-03-a-gr | recap «You know the *imperfecto* from A2 Unit 13»: the imperfect is A2 Unit 21 (sheet) | «from A2 Unit 21».
- c1-24-03.ex06 | prompt «¿Qué dejó constancia el comité…?» is ungrammatical (*dejar constancia de*) | «¿De qué dejó constancia el comité…?». Option «…advirtió que no aceptará ningún ultimátum» is a second right answer (an open refusal may stay in the future, per the lesson's own tip, and nothing closes it) | «…advirtió que no habría aceptado ningún ultimátum.»; ds fixed (index 2 no longer futuro-simple).
- c1-24-02.ex08 | «para que el servicio mantenga la calma» is not natural (a service keeping calm) in all four options | «las delegaciones mantengan/mantienen/mantendrán». Option 2 «con el fin de que zanjemos la disputa» (same-subject *que* + subjunctive) is only dispreferred, so a possible second right answer | replaced by «…para las delegaciones mantengan la calma» (missing *que*) (unsure).
- c1-24-02-a-gr | «maintaining a strict split between…» overstates the norm (infinitive is preferred, not obligatory) | «the usual split» (unsure).
- c1-24-04.ex04 (listening) | options are fragments («Smoothing over rough edges before…») that do not say what was heard (a counterfactual); «Ignoring rough edges…» is arguably the better reading of «de no haber limado» | four full clauses («Without smoothing over rough edges before the list of demands, the meeting would not have secured the truce») with one detail changed each (after / still / budget).
- c1-24-04.ex06 | «El encuentro privado del martes»: *encuentro* is listed only in c1-27-02 (unmet) | «La reunión del martes cambió por completo…» (*privado* is also unmet, so dropped).
- c1-24-05 story | «Les insto a que firmen hoy» (plural leísmo) | «Los insto a que firmen hoy».
- c1-24-05 story question 1 | «had stalled the talks … for three weeks?»: the text says the deadlock was three weeks ago, not that it lasted three weeks | «three weeks earlier?».
- c1-24-05-a-gr tip | «never mix *por una parte* with *por otro*» overstates (*por una parte … por otro lado* is current) | «Keep the pair parallel and make *otra* agree with feminine *parte* … never *por otro parte*» (unsure).
- c1-24-consolidation.ex09 | «en junio» is not anchored: with a future June, «sostuvo que ya desbloquearán el fondo en junio» is readable | «en junio del año pasado» in all four options.

## 2. Metadata
- c1-24-04.ex06 | ds missing on «ninguna de las partes habrá transigido hoy» | set {2: futuro-perfecto, 3: condicional-regular}.
- c1-24-consolidation.ex09 | ds missing on «hubiera seguido abierta hoy» | {1: present-tense, 2: pluperfect-subjunctive-forms, 3: futuro-simple}.
- c1-24-03.ex06 | ds after the option change (see above) | {1: preterito-perfecto, 3: present-tense}.
- All other `teaches`/`category`/ds read correctly. Consolidation has 6 distinct tags. Run `lock_tags` after the ds changes.

## 3. Goals / checklists
- Every goal and checklist line is practised; checklists copy the goals in order; all six challenges have `canDo` = first checklist line and tier1; characters fit (Carlos office, Meg student). Consolidation's «thirty-seven terms» is correct (8+7+8+7+7). No change.

## 4. Doubtful
- (unsure) Pattern: in 24-01 ex02/ex06, 24-02 ex02/ex06, consolidation ex01/ex02 two wrong options share the fault «indicative (present / future) instead of subjunctive». Left; the faults are different tenses.
- (unsure) «insta a que la contraparte presente…» (24-01 table, challenge, consolidation ex11) has no direct object; press uses it, DPD builds *instar a alguien a que*. 24-01 ex08 option «señala que el mediador convoque…» can be read as a directive, i.e. not clearly wrong.
- (unsure) 24-04 repeats the B2 Unit 10 screen (*de haber*, si-less *hubiera*, *aun cuando* + pluperfect subjunctive) and 24-02 mostly B2 Unit 12; the "C1" addition is only the domain and register. The lessons-learned file asks for more than a recap.
- (unsure) 24-04.ex08 option «Habrían limado asperezas…, habrían evitado…» is a grammatical juxtaposition, only not a condition; the stem «grammatically sound» is loose.
- (unsure) 24-03.ex02 «desbloqueará» after «En aquella reunión» is tolerated by the lesson's own open-anchor rule.
- (unsure) The story names three invented people with full names (Elena Vargas, Martín Soler, Lucía Méndez); Lucía clashes with the course character; earlier readers asked for unnamed people.
- Story facts: the figures (60 %, 36 hours) and the centre are invented and general; nothing names a real study or person. 513 words, 3 questions answerable (paragraph numbers 2, 3, 5 in ex06–08 are correct counting the intro as 1).
- Unmet-words leftovers after fixes are only *redujera*, *seguido*, *mantenido* (forms of listed verbs).

## 5. Dictionary
- (none: the audit for c1-24 reports 0 words not in the dictionary and 0 compound guesses)

# UNIT 25 language-variation (53 fixes)

## 1. Found by reading
- c1-25-01.ex03 | «Al director del museo ___ vimos»: answer only *lo*, but *le* is the accepted leísmo for a male person, so a second right answer | female referent: «A la directora del museo ___ vimos…», hint «feminine singular direct object pronoun», answer *la* (*le* would be rejected leísmo).
- c1-25-01.ex05 (listening) | option 3 changes two details (americano pair and the España pronoun) | «…se usa «le» o «les» para el objeto, mientras que en el centro de España es habitual usar «le» para un hombre…» (only the first pair changed).
- c1-25-01-a-gr example 4 | «conviene sustituir por un nombre femenino: «La ayudé» o «Le di las gracias»» does not describe the test (it substitutes a pronoun, not a noun) | «sustituir el complemento por un pronombre femenino: «La ayudé» (directo) frente a «Le di las gracias» (indirecto)»; English matched (unsure).
- c1-25-01 challenge | cue 2 quotes the Spanish answer sentence; *secretaria* is unmet | cue «…give the standard version of the whole sentence»; «la directora» in scenario, target and English.
- c1-25-02-a-gr | recap «*tú* from A1 Unit 2»: *tú* is first shown in a1-01-04 (Unit 1) | «from A1 Unit 1» (*usted* from A1 Unit 5 is right: a1-05-01).
- c1-25-02.ex02 | options carry 2–3 faults each (*revisaste tu … te avisaste*; *tu … avisaste*) | one fault each: possessive *tu*; verb person (*revisaste/avisaste*); subject *tú* (kept). ds reset {1: possessives, 2: preterito-indefinido, 3: subject-pronouns}.
- c1-25-02.ex05 (listening) | options 2 and 4 change several details («se evita … distancia fría»; «fuera de la familia y entre desconocidos … jerarquía») and *fría* is unmet | option 2 «…como muestra de distancia y respeto»; option 4 «En varias regiones de Argentina y de Uruguay, el ustedeo se usa dentro de la familia y entre amigos…».
- c1-25-02.ex08 | «En la mayoría de las conversaciones entre jóvenes predomina el ___»: false for the River Plate (*voseo* fits too) and *encuentro* is unmet | «…entre jóvenes de México predomina el ___ desde el primer momento» + English.
- c1-25-02 challenge | «En cambio … también» contradicts itself | «En algunas regiones de Colombia el ustedeo también transmite…» (and English).
- c1-25-03.ex05 (listening) | options 2 and 3 change two details | option 2 only «sí es un error», option 3 only «conviene mezclar».
- c1-25-03.ex06 | *guía* unmet | «En el manual publicado en Madrid dice…».
- c1-25-03.ex08 | «Las mayores diferencias … se observan en el ___»: unsupported superlative (phonetic differences are at least as large) and *vocabulario* fits as well | «Muchas diferencias…», `answers` [léxico, vocabulario], English widened. `check-content` still lists it as `answers-alternatives`: accepted (two true synonyms).
- c1-25-03 challenge | prompt demands «a formal text should maintain lexical consistency», which neither the cues nor the target say | prompt now «State that the words of both regions function as educated synonyms and that the dictionary records them without marking either one as an error.»
- c1-25-04.ex05 (listening) | all three wrong options change two details | one each: «se escriben de forma igual», «ceceo», «en el norte de España».
- c1-25-04.ex06 | «sonaba muy poco clara» (*clara* unmet) | «se oía muy poco».
- c1-25-04.ex08 | «en algunas zonas del sur» (*algunas* unmet) | «en el sur de Andalucía» + English.
- c1-25-04 challenge | *escucha* | «se nota la aspiración» + English («one notices»).
- c1-25-05.ex01 | wrong options carry three faults each (*debes* + *tu* + register; *redacta* + *deberás* + *su*; *Si cualquiera redactas…*), and the indicative *todo aquel que redacta* is acceptable Spanish | single faults: *debes*; *todo aquel quien*; *redactes*. ds {1: present-tense, 3: subjuntivo-morfologia}.
- c1-25-05.ex02 | wrong options carry two faults and one is acceptable (*quienes desean … deberán*) | *tendrás que* (person); *deberán consultar tu diccionario* (possessive); *Quien deseen* (number). ds {1: futuro-simple, 2: possessives}.
- c1-25-05.ex05 (listening) | options 3 and 4 change two details; *antigua* unmet | option 3 only «registro coloquial hablado», option 4 only «norma local».
- c1-25-05.ex06 | «is polycentric» but the unit says *pluricentric* | «pluricentric».
- c1-25-05.ex08 | stem «in science, literature, and diplomacy» and «final paragraphs» are not in the essay (it names scientific, judicial and journalistic writing; spelling is in paragraph 2) | «According to the essay, what allows some twenty Spanish-speaking nations to keep up fluent communication despite their regional variants?» (unsure on "twenty", see 4).
- c1-25-05.ex09 | options 2 and 4 carry two faults and absurd content | one fault each (*debes*; *quienes escribe*), same sensible content; ds {1: present-tense, 2: leismo-laismo-reconocimiento, 3: present-tense}.
- c1-25-05 challenge | cues quote the Spanish words («Todo aquel que redacte», «deberá», «se reconoce que») | cues describe what to include.
- c1-25-05 story / screen | «más de veinte naciones», «twenty-plus countries» vs «twenty countries» in 25-04: Spanish is official in 20 states | «una veintena de países», «some twenty countries» (unsure).
- c1-25-consolidation.ex01 | *ministra* unmet | «A la nueva directora le recibieron…».
- c1-25-consolidation.ex07 (listening) | wrong options change 2–3 details | one each: *acepta*; *loísmo*; pronoun *la*.
- c1-25-consolidation.ex09 | wrong options carry 2–3 faults (*colaboran … deberás … tus*) | one each: *deberás*; *tus*; *Cualquier académico que colaboren*. ds {1: futuro-simple, 2: possessives}.

## 2. Metadata
- c1-25-consolidation | only 5 distinct `teaches` tags (leismo, voseo, vocab, sociolinguistica, formal-register); the brief wants 6 | ex05 («le ruego que usted nos confirme») retagged `subjunctive-influence` (unsure; needs the reviewer's lock_tags update).
- ds changes listed in group 1 (25-02.ex02, 25-05.ex01/02/09, consolidation.ex09). The rest (including 25-02 ex01/ex06 ds) read correctly.

## 3. Goals / checklists
- Goal and checklist lines all practised; `canDo` = first checklist line in all six; consolidation covers each lesson. Nothing to change. Cues of c1-25-01 and c1-25-05 quoted the target (fixed above).

## 4. Doubtful
- (unsure) unmet-words false positives left: *nuestra* (possessive, siblings *nuestro/nuestros* pass), *leímos*, *dígame* (forms of listed verbs).
- (unsure) 25-02 and 25-03 largely re-present B2 Unit 34 (voseo forms, *don/doña*, ustedeo in Colombia and Costa Rica, *carro/auto*). The 25-02 recap lists the vos forms but not that ustedeo was already shown there; new content is the terms and the distribution.
- (unsure) 25-03: «el carro (Mexico, Colombia, Caribbean)» and «un hablante mexicano dirá el carro» (also the essay): Mexicans say *coche* too; it matches B2 Unit 34, so not changed.
- (unsure) 25-05 table has no column heads and row 2 («En mi país decimos…» → «Se observa que cada comunidad…») is not a rewrite of the left sentence.
- (unsure) 25-05 ex03 and consolidation.ex05 hints name «present subjunctive»: needed to pin (the indicative also reads), left.
- (unsure) consolidation.ex01 «palacio presidencial» in a Madrid newspaper (Spain has none).
- Cosmetic: 25-04 speaking item 2 English loses the glosses of *taza*/*tasa* (double spaces).
- Factual claims in the screens and essay checked as true and general: seseo majority; aspiration regions; leísmo norm; "more than five hundred million speakers" is a round figure, unsourced; texts name no study or person.

## 5. Dictionary
pluricéntrica | pluricéntrico | adjective | pluricentric, having several centres of educated usage |

# Fix counts
- Unit 24: 25 fixes (22 target, 3 metadata); Unit 25: 53 fixes (47 target, 6 metadata; 5 are challenge sets).
