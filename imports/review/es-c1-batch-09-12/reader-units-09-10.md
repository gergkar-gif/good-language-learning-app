# Reader report: ES C1 core Units 9 and 10 (es-latam)

Files: `.scratch/fixes-economy-markets.json` (26 fixes), `.scratch/fixes-work-labour.json` (45 fixes), `.scratch/sheet-economy-markets.md`, `.scratch/sheet-work-labour.md`, `.scratch/build_fixes.py` (generator of both fix files). No content file edited, nothing committed.
Checks run: check-content 0 error / 0 suspect for both units; check_es_c1_forms core 0 hits; check_unit_refs prints "0 recap references" (it cannot read these), so every recap was checked by hand against the sheets and screens (all recaps name the right unit: B1 6, B2 10, B2 11, B2 8, B2 25, B2 23, B2 4, B1 2, B1 40, B2 21, B2 30). unmet-words (--with-hidden): [] before and after the fixes, for both units. Both fix files applied cleanly to a scratch copy (check_fixes: 0 rejected); validate-content then fails only on "locked tags changed" for the items whose distractor_skills or option order changed, so after applying run `python scripts/lock_tags.py es-latam c1/economy-markets --update --reason ...` and the same for work-labour.
Audit (both stories): not in the dictionary 0, literal compound guess 0.

## UNIT 9 economy-markets

### 1. Found by reading
- c1-09-01.ex08: two wrong options fail the same way (*Debido a la oferta es menor...* and *Como consecuencia de la oferta es menor...*, noun connector before a clause); second one replaced by *Dado la oferta es menor que la demanda...* (dado without que).
- c1-09-02.ex02: hint "to fall, infinitive" invites *caer* (valid) while the sentence already has *cayendo*; hint now "to go down (of rates), infinitive".
- c1-09-02.ex08: wrong option *De pedir el préstamo el año pasado, la empresa habría pagado menos.* is accepted Spanish (*De saberlo, habría venido*), a second right answer; replaced by *Si haber pedido el préstamo antes...* (si + compound infinitive).
- c1-09-02.ex07 prompt 2: "would have grown" fits *habría* and *hubiera crecido*; «habría crecido» added to the prompt.
- c1-09-03.ex08: *el año pasado* only in the wrong option *Si no aprobáramos...* is a tell; now in all three options.
- c1-09-04.ex07 prompt 2: "immediately" fits *inmediatamente / de inmediato / enseguida*; «de inmediato» added to the prompt.
- c1-09-05.ex09: Meg asks about "el deterioro del crédito que explicaba la columna", but the column never explains a credit deterioration; now "la subida de las tasas de interés", and Carlos's answer (all three options) says what the column states: *frenar el consumo y redujo la inversión privada*.
- c1-09-05.ex10 prompt 1: "Exports" with «la exportación» and *primer lugar / puesto* and "in the economy" unpinned; now «pasaron a ocupar», «las exportaciones», «el primer lugar»: "Exports moved into first place."
- c1-09-05.ex06 / ex07 / ex08 (reading): absolutes as tells (*exported all their production*, *rises automatically*, *permanent freeze*) removed; ex07's third option was much shorter than the right one, now matched.
- c1-09-consolidation.ex01: *Porque del encarecimiento...* is not a real string; now *Porque el encarecimiento del transporte, ...* (porque + noun phrase).
- c1-09-consolidation.ex07 (listening): options 1 and 3 changed two details; each now changes one.
- c1-09-consolidation.ex11: «caer» and «la deuda de las familias» added to the prompts (caerá/bajará; de las familias/de los hogares unpinned).
- Challenge c1-09-03: "central bank raised rates in time ... mortgages more affordable" is wrong economics (higher rates do not make mortgages cheaper); scenario, cue, target and english now speak of the bank "acted in time" (unsure about the economics only; the old text was the problem).
- c1-09-03 screen: "simple conditional (*sería*, *tendría*, *habría*)" next to "not *habría* + participle" confuses; *habría* replaced by *contaría*.

### 2. Metadata
- Answer position: 15 of 28 choice items had the right answer at index 0. Rotated by a script that remaps `distractor_skills` (kind "metadata"): 09-01.ex04, 09-02.ex03/ex06, 09-03.ex04, 09-04.ex05, 09-05.ex04, consolidation ex03/ex09; the rewritten items were placed at varied positions.
- (unsure) Missing `distractor_skills` on real imperfect-subjunctive forms used as wrong options: 09-02.ex03 *De mantuviera*, 09-02.ex06 *De no cambiara*, 09-03.ex08 *aprobáramos* -> `imperfect-subjunctive-forms`.
- All other tags (category follows tag, vocabulary tag on vocabulary items, reading items without `teaches`) are right. Consolidation: 12 items, 8 types, 7 tags, every lesson covered.

### 3. Goals / checklists
- Goals and checklists match one to one and every line is practised. canDo = first checklist line in all six challenges.
- 09-03 screen table: rows 1 and 2 have the identical label "Present result: si + hubiera/hubiese + participle, simple conditional"; give row 2 its own label (not fixed).
- 09-01 screen: the text says *a raíz de* takes a noun or an infinitive, the table row shows only "noun phrase" (minor, not fixed).

### 4. Doubtful
- (unsure) 09-02 screen: "*De* + simple infinitive expresses a possible condition; compound = unfulfilled past" is too strong (*De saberlo, ...*); fix adds "usually".
- (unsure) 09-02 screen: "A gerund can also state a condition when both clauses share a subject" with the example *Aumentando la inversión, se impulsaría el crecimiento*: the gerund's subject is not the subject of the main clause there.
- (unsure) 09-05 screen tip: "*pasar de* + infinitive is informal for 'not to bother doing'" is a Peninsular colloquialism; fine as a warning, odd for es-latam.
- (unsure) 09-02 challenge target *la economía podría entrar en estancamiento* (*caer en el estancamiento / entrar en recesión* are more usual).
- (unsure) Story c1-09 paragraph 3: *el crecimiento general pasó a avanzar a un ritmo mucho más lento* (clumsy double *a*) and *la presión sobre las hipotecas* (pressure on borrowers is meant).
- 09-02 ex03 and ex08 right answers repeat screen examples word for word (recall rather than test); not fixed.
- Story facts (checked): inflation from supply-chain and energy costs plus firm demand, central bank raising rates, effects on credit, consumption, investment, tax revenue, exports; all general, no real study, figure or person; ~500 words; hedged. Reading questions answerable from the column. True and general enough.

### 5. Dictionary
None (audit: 0 not in the dictionary, 0 literal compound guesses).

Fix count Unit 9: 26 (18 target, 8 metadata; 4 marked unsure).

## UNIT 10 work-labour

### 1. Found by reading
- c1-10-01.ex04 (listening): option 2 changed two details (*allows ... delay* and *long period*); now only *requires* -> *allows*.
- c1-10-02.ex02: hint "(agrees with feminine singular capacitación)" names the very agreement the item tests; now "relative quantity word, capitalised".
- c1-10-03.ex01: option 4 had two faults (*sino que mejorar* lacked *también* too); now *sino que también mejorar*.
- c1-10-03.ex04 (listening): option 3 changed two details; now only *reduces overload ... improves* -> *not only causes overload, but also improves*.
- c1-10-04.ex01: options 1 and 3 fail the same way (second person); now verb only (*debes pagar sus*) and possessive only (*debe pagar tus*).
- c1-10-04.ex05: unpinned: *Cuando despedimos a alguien ... la ley obliga a pagar* is natural from a manager, and *despide* with an implied subject is possible; the stem now says "general statement about what unnamed employers do, with the speaker not included".
- c1-10-04.ex06: *A veces pienso si convendría* is a calque; *me pregunto si*.
- c1-10-04.ex07: *organizar sus prestaciones* is not said (benefits are covered/paid); and "must" / "when" unpinned; now «Cuando uno» and «debe asumir», answer *Cuando uno trabaja por cuenta propia, debe asumir sus propias prestaciones.*
- c1-10-05.ex01: options 1 and 3 are both reversal markers (same fault); option 3 now *Por lo tanto* (the writer's own note).
- c1-10-05.ex09: option *Pero, algunas empresas ofrecen...* is a natural reply (only the comma is off) = second right answer; *Por el contrario* after a concession is also arguable. Now *Por lo tanto* / *Ahora bien* / *Además*.
- c1-10-05.ex04 (listening): option 2 changed two details; now only the marker.
- c1-10-05 screen example and speaking item: *modernizar las líneas de trabajo* -> *líneas de producción* (and the English).
- c1-10-05 story: *a medio plazo* is Peninsular -> *a mediano plazo* (unsure only because the story is exempt from word checks).
- c1-10-consolidation.ex07 (listening): options 1 and 2 changed two details each; now one.
- Challenge c1-10-01: scenario says management "wants", cue and target say "expects" (*espera*); scenario now "expects".
- Challenge c1-10-consolidation: scenario and cue say management "must" respect working hours, target says *conviene que* (advisable); *aunque* concedes nothing; "the labour-market unit" refers to the course. Now "your labour-market seminar", "it is advisable that management respect working hours", *..., y conviene que la dirección respete la jornada laboral.*
- 10-04.ex07 and consolidation.ex11 produced one stored answer each; prompts now pin the construction («Cuando una», «valora más»).

### 2. Metadata
- Answer position clustered at index 1 (about half of the choice items); rotated with ds remapped (kind "metadata"): 10-01.ex06/ex08, 10-02.ex01, 10-03.ex06/ex08, 10-04.ex05/ex08, 10-05.ex07/ex08, consolidation ex01/ex03/ex09/ex12; others moved with their text fixes.
- (unsure) 10-01.ex01: `distractor_skills` {2: opinion-verbs-mood} on *espera que la plantilla respeta*: the option is a plain present indicative after *esperar*, not an opinion-verb pattern; changed to `present-tense`.
- Tags otherwise right; consolidation has 12 items, 8 types, 6 tags.

### 3. Goals / checklists
- Goals and checklists match one to one, every line is practised, canDo = first checklist line in all six challenges.
- (unsure) 10-05 screen tip: "All four markers ... usually follow a full stop or a semicolon" contradicts the screen's own *en cambio* inside the clause (and B2 Unit 30); reworded.
- (unsure) 10-02 screen: "often inserts *tanto* before the second comparator" overstates (*cuanto más ..., tanto mejor* is careful-writing only and nothing drills it); "sometimes".
- Lesson plan against `notes/work-labour.md` and `level-plan.md`: all 20 domain words are listed; 05 omits the note's *por un lado ... por otro* and *si bien* (fine, B2 words). See 4 for the C1 fit.

### 4. Doubtful
- (unsure, for the user) C1 fit: lessons 02 and 03 (and the B2 material of 01, 04) re-teach B1/B2 screens almost whole. B1 Unit 2 and B1 Unit 40 already teach *cuanto más ..., más ...* (with *mejor* for *más bueno*, invariable before a verb), *a medida que*, *sino / sino que* with the conjugated-verb rule and *tanto ... como*; B2 Unit 21 already teaches the 3rd-plural/*uno* contrast in the same words (never includes the speaker). The only new content is agreement of *cuanto* before nouns (02) and register examples. At C1 density consider adding the unit's own new angle (e.g. *no solo ... sino que además/incluso*, *tanto si ... como si*) rather than recapping.
- (unsure) The interview names a researcher ("la doctora Elena Morales"); level plan says "No real person". A plausible name can match a real one. Fixes make her unnamed ("una investigadora", reading stems "the researcher").
- (unsure) 10-05.ex10: *El contrato indefinido da estabilidad; no obstante, la brecha salarial persiste.* has nothing for *no obstante* to concede; replaced by *La reestructuración terminó este año; no obstante, la rotación sigue siendo alta.*
- (unsure) Challenge c1-10-05 target *el ingreso básico* reads as universal basic income; *los ingresos básicos*.
- (unsure) 10-02 ex01 right answer *Cuanto más alta es la estabilidad laboral*: *mayor* is the natural adjective (the screen itself prefers it).
- (unsure) 10-04.ex03 *remuneran mejor la antigüedad*: *premian / reconocen* would be more natural, *remunerar la antigüedad* is acceptable.
- (unsure) 10-01.ex06: Carlos answers "will your company change the timetable?" with *la dirección espera que los jefes modifiquen la jornada*; odd that management expects the bosses to change it.
- (unsure) Story: unhedged judgements for a text that should hedge them (*el abuso del contrato temporal ... eleva la rotación y dificulta la inserción*, *mayor es la productividad*); the minimum-wage statement (*protege el piso de ingresos*) is contested; ~460 words; no figures or real institutions; invented magazine *Entorno Laboral* could match a real title.
- 10-03 screen tip: *sino que también el salario* called "ungrammatical" is stronger than usage (checked by the reviewer; left).
- Es-latam words checked: none Spain-only except *a medio plazo*; no *vosotros*.

### 5. Dictionary
None (audit: 0 not in the dictionary, 0 literal compound guesses).

Fix count Unit 10: 45 (31 target, 14 metadata; 16 marked unsure).
