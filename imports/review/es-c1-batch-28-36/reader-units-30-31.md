# Reader report: es-latam C1 Units 30 and 31

Fixes: Unit 30 = 44 (`.scratch/fixes-politics-democracy.json`), Unit 31 = 50 (`.scratch/fixes-art-criticism.json`). No challenges file written (existing challenges read; one fix, in Unit 31).
Checked on a scratch copy with the fixes applied: `check-content` 0 errors / 0 suspects in both units, `unmet-words` [] for both units, `check_es_c1_forms --track core` 0 hits, `check_unit_refs --bare --named` 0. Story audits: 0 "not in the dictionary", 0 "literal compound guess" (both stories), so group 5 is empty.

## UNIT 30 politics-democracy

### 1. Found by reading
- c1-30-01-a-gr: "In parliamentary and civic speeches, this stylistic option extends to two high-register patterns." Point 2 (*hubiera* + participle in the result clause) is taught in B2 Unit 10 (b2-10-02-a "Habría or Hubiera?") and is presented as new without a recap. Fix: intro adds "You also know *hubiera* + participle in the result clause of a past counterfactual from B2 Unit 10."
- c1-30-04-a-gr: intro recaps only *sea cual sea* (B2 Unit 14); points 2 (plural agreement *sean cuales sean*) and 3 (imperfect-subjunctive past) are taught in B2 Unit 14 (b2-14-03) and B2 Unit 32 (b2-32-03; also C1 Unit 9 c1-09-04) and are presented as new. Fix: intro names *sean cuales sean* (B2 Unit 14) and *costara lo que costara* (B2 Unit 32).
- c1-30-03-a-gr example 3: "En respeto a la separación de poderes" is not natural. Fix: "Por respeto a la separación de poderes".
- c1-30-03.ex07 builder: "Tras la derogación, la norma pasó a ser revisada." is illogical (a repealed rule is not then reviewed). Fix (tiles/solution/english): "Tras el veto, la norma pasó a ser revisada." / "After the veto, the rule moved on to be reviewed."
- c1-30-05.ex09 dialogue: right answer "Cerró con «en suma» ... tarea cívica diaria", but the unit speech closes with "En definitiva, ... se construye cada semana". Fix all four options to «en definitiva» / "se construye cada semana".
- c1-30-05.ex06/07/08 (and the same three questions in stories/original/c1/c1-30.json): wrong options are absurd or absolute ("replace the plenary session ... without public debate", "fines on non-voters", "avoid raising objections during the first half"); right options overstate the text ("dissent strengthens ... democracy"; "open committee review": the text says technical committee). Fixes: right options aligned with the text, wrong options replaced by plausible one-fault options (12 options, both files).
- c1-30-01.ex06 dialogue: options 3 and 4 are absurd, not real answers ("«aprobáramos» en cualquier verbo sin necesidad de «haber»", "«hayamos» en la consecuencia"). Fix: "se acepta «hubiéramos» en la condición, pero no en la consecuencia." / "No, ... solo se acepta «habríamos» en la consecuencia, no «hubiéramos»."
- c1-30-02.ex06 and c1-30-consolidation.ex08 (dialogue): "además," is acceptable Spanish in the slot (second right answer) (unsure); fix: "por ejemplo,". (*por eso* in the same items is a borderline causal reading, left; its distractor_skills stay.)
- Rendering (all five grammar screens with nested emphasis, 6 lines in this unit): `**Compound *hubiera* + ...:**`, `***Con todo* (...):**` etc. render with inverted italics and stray asterisks in the app (`escMd` cannot nest). Fix: outer `**` dropped on those lines, italics kept (6 fixes). Systemic in C1 (17 grammar files contain `***`); worth a script.

### 2. Metadata
- c1-30-04.ex03 hint "cual (plural)" names the tested number. Fix: hint "cual".
- c1-30-03.ex05 hint "to (preposition)" translates the answer *a*. Fix: hint "preposition" (unsure).
- Tags, categories, distractor_skills otherwise consistent (checked each item; ds on *debía*, *Son cuales sean*, *sería*, *fue*, *por lo tanto/por eso*, *es decir* all well-formed forms).

### 3. Goals / checklists
- All goal and checklist lines are practised; canDo = first checklist line in all six challenges; challenge scenarios, cues, targets agree; people correct (Meg student, Carlos office). No fix.

### 4. Doubtful
- c1-30-01: the claim that *-se* (*hubiese aprobado*, *quisiese*) does not replace the conditional is on the screen, ex01 and ex06; reviewer says checked, not re-raised.
- c1-30-05.ex05 accepts only *referendo*; *referéndum* (the RAE headword spelling) is as right, but adding it to `answers` made `unmet-words` flag it as an unlisted word, so not fixed (unsure).
- Consolidation speaking 1 and 2 repeat the sentences of ex05 and ex06 exactly (unsure whether wanted).
- c1-30-05.ex11 wrong options 2 and 4 share a fault (a synthesis marker opens the sequence).
- c1-30-04.ex06: "¿aceptaron todos los grupos ...?" answered "Sí, prometieron antes del voto" (promising is not accepting): mild mismatch, left.
- `la participación ciudadana` (lesson 05 list) and `la agenda pública` appear earlier (04, 03) only as transparent cognates; left.
- Facts: the speech and all screens are about an invented municipal assembly; no real person, party, law or statistic; general statements only, all true and general enough. Recaps (B2 Unit 9, B1 Unit 1, B2 Unit 30, B2 Unit 23, B2 Unit 8, B1 Unit 13, A1 Unit 8, B2 Unit 28) match the knowledge sheet except the three fixed above.

### 5. Dictionary
(none: audit reports 0 not in the dictionary and 0 literal compound guesses)

## UNIT 31 art-criticism

### 1. Found by reading
- c1-31-05-a-gr: recap names only B1 Unit 6, but the plural human object + personal *a* + singular verb pattern (*Se invitó a los vecinos*; the tip's "plural verb with a is a common mistake") is taught in B2 Unit 19 (b2-19-02-a). Fix: intro adds "... and *se* with a singular verb before a person marked by personal *a* (*Se invitó a los vecinos*) from B2 Unit 19", drops "frequently trip up advanced learners".
- c1-31-01.ex02 wrong option "Resulta imposible de ignorar el claroscuro de la sala principal." is good Spanish (*el claroscuro* is the subject): a second right answer. Same in c1-31-consolidation.ex01 "Resulta difícil de ignorar la maestría de este grabado." Fix: "Resulta imposible a ignorar ..." / "Resulta difícil a ignorar ..." (one real fault).
- c1-31-01-a-gr table: "Resulta evidente admirar el claroscuro." glossed "It is natural to admire" (*evidente* is "obvious"; sentence is odd). Fix: "Resulta difícil ignorar el claroscuro." / "It is hard to ignore the chiaroscuro."
- c1-31-01.ex05: hint "light-and-shadow contrast" also fits *contraste*, which the sentence accepts (unpinned blank). Fix: hint "chiaroscuro".
- Words used before their lesson: *sumamente* (listed c1-31-03) in c1-31-01 screen example 1, ex04 and speaking 1; *trazo* (listed c1-31-03) in c1-31-02 screen. Fix: *muy* in 01 (example, english, ex04 sentence and options); "con líneas firmes" in 02.
- c1-31-03.ex05: "La textura oscura del papel ... trazo oscuro" (a texture is not dark; repeats *oscuro*). Fix: sentence "La _____ del papel refuerza el contraste del trazo oscuro." and english.
- c1-31-consolidation.ex08: "los grabados están protegidos por una luz muy clara" (light does not protect prints). Fix: "están organizados por etapas" in all four options.
- Story c1-31, paragraph 4 vs 2: the route ends in the courtyard with large installations (para 2), but the "cuarta y última sala" with a "espacio estrecho" is not placed. Fix: "en la cuarta y última sala, la del patio interior, que resulta ..."
- Story: "cerámica cocida a mano" (firing is not by hand). Fix: "cerámica modelada a mano". "cartelas" is a Spain/Argentina word, Mexico says *cédula* (unsure); fix: "textos de sala".
- c1-31-05.ex06/07/08 and the story file's own 3 comprehension questions (different wording from the exercises): wrong options absurd or absolute ("randomly", "strictly by colour palette", "closed for restoration", "repeats the exact same", "only paintings"). Fixes: plausible one-fault wrong options (12 in the exercise file, 9 in the story file).
- Rendering (12 lines in lessons 01-05): bold spans containing italics (`***Estar* + participle**`, `**Subject + *resultar* + ...**`) show inverted italics and stray asterisks; `~~es~~`, `~~de~~` and backticks (`*ricísimo*`, `*se invitan a los visitantes*`) are not rendered and appear literally. Fixes: outer bold dropped; tildes and backticks removed with rewording.

### 2. Metadata
- c1-31-consolidation.ex11 (teaches se-impersonal) and ex12 (teaches manner-clauses) each hold two prompts testing different skills (superlative + se; tal como + resultar): one slug cannot show both (unsure). Not changed.
- All other tags and distractor_skills checked (*es articulada* ser-passive, *que ha acogido* preterito-perfecto, *según se observa* present-tense, *como si* como-si, *se invitan* se-pasivo-vs-impersonal): consistent.

### 3. Goals / checklists
- All lines practised. Challenge c1-31-02: prompt says "with directed lighting" but target says "una iluminación muy cuidada". Fix (challenges.json, key c1-31-02): "with careful lighting". Other challenges, canDo lines, characters (Carlos/Meg) correct.

### 4. Doubtful
- c1-31-04.ex02: *según se observa* (indicative) and *tal como se observe* are acceptable Spanish; the question pins "según + subjunctive", so fine as written (unsure). Same for 03.ex02 *que ha acogido*.
- c1-31-02.ex06: Meg asks about the installation, Carlos's second clause is about the canvas: acceptable.
- Facts: invented museum and artists throughout, no real person, work or date; general aesthetic statements only. Screen facts (*riquísimo*, *amplísimo*, *ricísimo* not used) are right. Recaps (B1 Unit 15, B2 Unit 20, B1 Unit 18, B1 Unit 7, B2 Unit 32, B1 Unit 6, B2 Unit 19) match the sheet.

### 5. Dictionary
(none: audit reports 0 not in the dictionary and 0 literal compound guesses)
