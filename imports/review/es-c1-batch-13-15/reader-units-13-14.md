# Reader report, es-latam C1 Units 13 and 14

Commands run per unit (from /home/user/parlour-read-a): check-content 0 errors / 0 suspects (both units); check_unit_refs --bare --named 0 hits; check_es_c1_forms --track core 0 hits; unmet-words --with-hidden [] (before and after fixes, on a scratch copy with the index rebuilt); story audit: 0 not in the dictionary, 0 literal compound guesses. All fixes applied to a scratch copy: apply_replacements clean; check-content 0/0 after; validate-content fails only 7 "locked tags changed" (reviewer runs lock_tags after the metadata/option fixes).
Story word counts: c1-13 480, c1-14 428 (both within 400-600).

## UNIT 13 health-bioethics  (fixes file .scratch/fixes-health-bioethics.json, 32 entries)

### 1. Found by reading
- c1-13-01-a-gr text: opens "You know deber, deberías and tener que from B1 Unit 4" but presents *debería haber* (B2 Unit 10), *haber de* and *deber* vs *deber de* (B2 Unit 26) as new; also says "debería haber ... (rather than tendría que haber ...)", which contradicts B2 Unit 10 ("Tendría que haber works the same way") and is an unsupported norm claim. Fix: recap all three with the right units, drop the "rather than" clause.
- c1-13-01.ex03: answer "debería" only; "debió haber consultado" / "debía haber" are equally right for "should have consulted" (second right answers). Fix: answers [debería, debió, debía].
- c1-13-01.ex04: "…debe respetar la confidencialidad, aunque el hospital tiene que remitir…" aunque ("although") makes no sense and contradicts the English "while". Fix: "mientras que".
- c1-13-02.ex01: option "Antes de administrar el fármaco, el paciente debe firmar…" is acceptable Spanish (agent left open) = second right answer; the stem also never said which action comes first. Fix: stem "The patient signs the consent first, and only afterwards do the staff administer the drug. Which sentence says this?", option 4 -> "Antes de que se administraría…".
- c1-13-02.ex05: "formally authorise a specific medication" suggests autorizar. Fix: "officially order a medicine for a patient".
- c1-13-02.ex06: option "…antes de iniciarse la primera fase el laboratorio" is garbled. Fix: "…antes de que se iniciar la primera fase del estudio".
- challenge c1-13-02: "after the committee has evaluated the diagnosis" (a committee evaluates results, not a diagnosis). Fix: "los resultados" in scenario, cue, target, english.
- c1-13-03.ex06: options 2 and 4 fail the same way (que dropped). Fix: option 4 "a pesar de que tardar años…".
- c1-13-03.ex08: options 2 and 3 same fault (que before a noun). Fix: option 3 "Pese de las limitaciones…".
- c1-13-04.ex01: options 3 and 4 both fail on indicative *son*. Fix: option 4 "cualesquiera que sea las patologías…" (ds only on option 3).
- c1-13-04-a-gr tip calls *cualquiera que sean* a "slip"; it is a formal-preference point. Fix: reworded as preference (unsure).
- c1-13-05 story: "Pese a haber conquistado herramientas extraordinarias" is not a natural collocation. Fix: "desarrollado" (unsure).
- c1-13-05.ex07 and story Q2: right option "might widen inequalities in health equity if only a small minority can afford them" is incoherent and not what the text says (price tends to limit access to a minority); wrong option "completely replaced" (absolute only in a wrong option; the story file says "largely"). Fix: "That their high price tends to limit access to a small minority of patients."; "largely replaced".
- c1-13-05.ex08 and story Q3: "regardless of the patient's condition" is an absolute tell. Fix: "over the patient's comfort."
- challenge c1-13-05: scenario and english say "accusation of negligence", target "el caso de negligencia". Fix: "la acusación de negligencia".
- c1-13-consolidation.ex02: copies c1-13-03.ex01 (same sentence and options, pese a -> a pesar de), and its option 4 repeats lesson ex08's fault. Fix: new sentence (aparezcan riesgos nuevos) with four one-fault options.
- c1-13-consolidation.ex07: option 4 "…después de revisar los datos el fármaco" garbled. Fix: "…después de que el comité de ética revisar los datos…".
- challenge c1-13-consolidation: "if a centre had not consulted the ethics committee, it would have caused a serious ethical dilemma" (not consulting does not cause a dilemma). Fix: "habría actuado con negligencia" in scenario, cue, target, english.

### 2. Metadata
- c1-13-01.ex01: teaches deber-vs-tener-que but the item tests deber vs deber de (B2 Unit 26); ds "future-probability" on *debe de* / *debía de* is wrong (not future forms). Fix: teaches perifrasis-deber-obligacion-conjetura, ds removed (unsure).
- c1-13-01.ex06: ds {1: future-probability} on *debe de revisar*. Fix: perifrasis-deber-obligacion-conjetura (unsure).
- c1-13-consolidation.ex01: ds {1: future-probability} -> perifrasis-deber-obligacion-conjetura; option 3 *tiene que haber informado* -> perifrasis-modales-probabilidad-epistemica (unsure). ex12: same slug for *debe de proteger*.
- c1-13-02.ex01: ds for the replaced option 4 -> condicional-regular.
- After these, run lock_tags (7 locked-tag failures are expected).

### 3. Goals / checklists
- All goal and checklist lines are practised (haber de by 01.ex07). canDo of all six challenges equals the first checklist line. Nothing to change.

### 4. Doubtful
- c1-13-02 screen: "After *después de que*, formal writing uses the present perfect subjunctive (*haya* + participle) to mark a future milestone" overstates: the present subjunctive (B2 Unit 7) stays the normal form; *haya* adds "completed". (unsure)
- Unit rule vs items: lesson 01 says procedural requirements take *tener que*, yet 02 and the challenges use "el paciente debe firmar el consentimiento" (a procedural step). (unsure)
- c1-13-05 re-teaches B2 Unit 11 (mixed conditional with simple conditional, row 3 and goal 2) and B2 Unit 16 (*hubiese* = *hubiera*); the only new element is passive *se* in the *si* clause. A recap that adds nothing; no fix possible without new content.
- c1-13-03 screen names only B1 Unit 32; *a pesar de que* + indicative/subjunctive is also in A2 Unit 28 (concesivas-aunque).
- c1-13-03.ex03: "…de ayer, provocó" with hint "past": *mostraba* might also fit. (unsure)
- c1-13-01.ex06 option 2 (*debe de revisar*) differs in tense as well as in *de*. c1-13-02.ex08 option 4 (*Antes de que … entregó*) is wrong on both connector and mood.
- Story c1-13 para 5: "medir el éxito únicamente por cada día añadido" is slightly odd. All factual claims are general (innovation raises ethical questions; consent forms are long; health data are useful and sensitive; costly treatments limit access; palliative care protects dignity) and true.

### 5. Dictionary
none (audit: 0 not in the dictionary, 0 literal compound guesses)

Fix count Unit 13: 32 entries (26 sure, 6 flagged unsure).

## UNIT 14 environment-climate  (fixes file .scratch/fixes-environment-climate.json, 32 entries)

### 1. Found by reading
- c1-14-01-a-gr: says B1 Unit 22 "practised simple deadlines" and presents the guess *habrá* + participle as wholly new; B1 Unit 22 already showed *Habrá salido ya*. Fix: recap it.
- c1-14-01.ex08: hint "future of probability" gives away the tested point. Fix: "haber (3rd person singular)" (the English "has probably" pins the reading).
- c1-14-01.ex05: "la red eléctrica nacional" (extra word only in a wrong option). Fix: "la red eléctrica".
- c1-14-02-a-gr: -ra/-se forms (B1 Unit 4) and passive *se* (B1 Unit 6) shown as new. Fix: recap line.
- c1-14-02.ex01 option 4 and ex06 option 3: "Si se reducen/aprueban …, … disminuiría/tendrían" (present + conditional) is heard and not clearly wrong, so a possible second right answer (unsure). Fix: ex01 option 4 -> "…redujeran…, disminuirá el uso…" (ds futuro-simple); ex06 option 3 -> "Si se aprobase medidas graduales…" (plural agreement is the lesson's goal).
- challenge c1-14-02: "if a carbon tax were applied and climate adaptation were incentivised, mitigation would advance faster" answers a question about cutting fossil-fuel use with adaptation; illogical. Fix: "…and mitigation were incentivised, fossil-fuel use would fall faster" (scenario, cues, target, english).
- c1-14-03-a-gr: recaps only B1 Unit 6; B2 Unit 19 (passive vs impersonal *se*) taught the infinitive/person cases. Fix: recap added (unsure).
- c1-14-03.ex08: option 2 "Se prohíben iniciar…; se prohíbe los vertidos…" has two faults. Fix: "…; se ha prohibido los vertidos cerca del río."
- c1-14-04-a-gr: *advertir* is a B2 Unit 18 reporting verb, shown as new. Fix: recap.
- c1-14-04.ex08: "la escasez hídrica había reducido el agua" is circular (scarcity is the shortage). Fix: "…había obligado a limitar el consumo de agua en varias zonas" in all four options (checked as met words).
- story c1-14 para 1: "habrá transformado buena parte de la generación limpia" (the transition transforms the generation mix, clean generation is already clean). Fix: "generación eléctrica". Para 2 "sectores más intensivos" lacks its complement: "en emisiones" (unsure).
- c1-14-05.ex07 and story Q2: question "Why does the report recommend pairing a carbon tax with social compensation?" (the text warns of social rejection, it does not recommend) and right option adds "while discouraging fossil-fuel use" (not given). Fix: "Why does the report say carbon-tax measures need direct support for low-income households?" / "To avoid social rejection and keep mitigation from increasing inequalities."
- c1-14-05.ex08 and story Q3: right option "clear rules for real action" is not in the text (it says rules that guide public and private investment). Fix: "clear rules to guide investment."
- c1-14-05.ex11: stem does not ask for plural agreement, so "es las mejoras" could be read as right. Fix: stem pins "with the verb agreeing with the plural noun" (unsure; the reviewer has accepted the plural norm).
- c1-14-consolidation.ex02: option 2 "Se debe proteger los humedales y se prohíben dejar basura…" has two faults. Fix: "Se deben protegidos los humedales y se prohíbe dejar…".
- challenge c1-14-consolidation: canDo ("futuro perfecto") is not practised by its target, and sentence 1 copies c1-14-consolidation.ex11. Fix: target "Para 2040 se habrán reducido las emisiones. Lo prioritario es ampliar la fiscalización y la economía circular." (scenario, prompt, cue, english updated).

### 2. Metadata
- c1-14-04.ex01 {1,2}, ex08 {3}, c1-14-consolidation.ex07 {2}: ds dequeismo-queismo on ungrammatical options (según que, según de que, concluyó de que, concluye de que). Fix: removed (unsure; the rulebook says no ds on ungrammatical options).
- c1-14-02.ex01 / ex06: ds updated for the replaced options (futuro-simple; the "present-tense" entry on ex06 option 3 removed).
- Run lock_tags afterwards.

### 3. Goals / checklists
- Every goal and checklist line is practised; canDo equals the first checklist line in all six (consolidation fixed above). Nothing else.

### 4. Doubtful
- Story c1-14 opens "Este informe técnico evalúa…" and later "el documento advierte": the text refers to itself as a report (template: "never about itself"; story-meta is 0). (unsure)
- c1-14-02 and c1-14-05 recap screens add little beyond domain vocabulary (-ra/-se and *lo* + participle and plural agreement with *ser* (*Lo difícil … son las conjugaciones*) are already B1 Unit 4 / Unit 40 material).
- c1-14-consolidation.ex06 (*lo más difícil … son*), 05.ex01, 05.ex11: plural agreement is the reviewer-checked norm; singular *es* is also common (not re-raised).
- c1-14-01 table: "Para cuando cierre la década" is slightly odd.
- All story facts are general and hedged (global warming tends to lengthen dry seasons; wetlands regulate the water cycle; carbon pricing can meet social rejection; recycling is incomplete) and true. "los registros de los últimos cinco años" refers to the invented agency.

### 5. Dictionary
none (audit: 0 not in the dictionary, 0 literal compound guesses)

Fix count Unit 14: 32 entries (24 sure, 8 flagged unsure).
