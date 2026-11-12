# es-es B1 Unit 41 opinions-arguments (b1-21-01 … b1-21-consolidation, story b1-21-paliques)

Fixes: fixes-opinions-arguments.json (94 fixes; es-latam mirror: 94 of 94 match, none unmatched; all lesson, grammar, exercise and vocabulary files are identical in the two courses). Challenges: challenges-opinions-arguments.json (6).
Checks run: check-content (30 errors, 4 suspects before; 0 and 0 after, applied to a scratch copy), render_lesson, audit-reader-coverage (0 dictionary gaps before and after), check_fixes on a scratch copy (0 rejected).
Unmet words (scratch copy, both courses): es-es 24 hits before, 6 after; es-latam 32 before, 6 after. The 6 left in each are inflected forms of verbs listed in b1-21-01/03/04 (considero, consideremos, justifiquemos, evaluemos) in the consolidation.

## 1. Found by reading
- b1-21-01 grammar screen: presents *creo que* and *me parece que* (B1 Unit 13) as new, broken italics (*creo* *que*), *pienso que* named but never exemplified. Fix: recap "You know … from B1 Unit 13", one italic run per term.
- b1-21-01 example 2 (and speaking step): *ya que* before its screen (b1-21-04) -> *porque*.
- b1-21-01.ex02: "La propuesta existe." non-phrase, unmet *existe*, length give-away -> wrong options each lack one half (reason / opinion marker).
- b1-21-01.ex06: Spanish question stem uses unmet *significa* -> English only.
- b1-21-01.ex12 "El problema será una persona.", ex13 "La evidencia piensa que yo.", ex14 "La opción me considera.": nonsense options -> real single-fault options; ex13 wrong subjunctive gets `distractor_skills` subjuntivo-morfologia (same on ex14 "sea razonable").
- b1-21-01.ex14: *¿Qué opinas…?* unmet (*opinar* in no list) -> *¿Qué te parece…?*.
- b1-21-02 grammar screen: *pero*, *sin embargo* (B1 Unit 1), *aunque* (A2 Unit 28) presented as new; *a pesar de que* (b1-32-03) in text, example, ex08 and ex12 -> recap + *aunque*.
- b1-21-02.ex02 completamente / length 67 vs 43 / unmet *conclusiones* -> new wrong options. ex09, ex10, ex12 length give-aways -> longer wrong options with one fault each (so/because swaps).
- b1-21-02.ex03: answers *sin embargo*, *no obstante* vs one English -> narrowed to *sin embargo*.
- b1-21-02.ex14 "No hay ventajas porque las ventajas." non-phrase -> *Porque admito sus ventajas…*.
- b1-21-02.ex15: ninguna; *por lo tanto* (B2) as wrong option -> *por eso* / *porque* (ds porque-y-por-eso).
- b1-21-03 grammar screen: *es importante que* + subjunctive is A2 Unit 27, presented as new, italics broken -> recap; tip rewritten with a contrast.
- b1-21-03 ex09, ex10, ex12 length give-aways -> one-fault wrong options. ex16: unmet *demás*, *participantes* -> met words.
- b1-21-03 vocabulary: *discusión*, *respetuoso* used (03 examples, ex, 05, consolidation) and in no list -> added to b1-21-03 voc.
- b1-21-04 grammar screen: *porque / por eso / además* known (A2 Unit 5 / 28) presented as new; *por lo tanto* (B2) in text, example, ex03, ex05, ex06, ex11, ex13, ex15, ex16 -> *por eso*; *ya que* had no example -> added one; broken italics. ex03 is now the whole-word blank *por eso*.
- b1-21-04.ex07: answers porque / ya que -> narrowed to *porque* (*ya que* drilled in ex16). ex09, ex10, ex12, ex15 length give-aways, ex15 ninguna and "Por eso, ninguna propuesta…" -> fixed. ex13 "Porque apoyo que no apoyo." non-phrase. ex17 unmet *completa*. ex02 (es-latam) unmet *parlamento* -> *gobierno*.
- b1-21-05 reading items ex20-23 asked about a different text (a community debate, the b1-21.json story), not the lesson story *b1-21-paliques*: rewritten to the retold story; tell-absolute (Nadie, siempre, ninguna) and length give-aways removed.
- b1-21-05 grammar screen: first section is B1 Unit 25 / 33 material (*en mi opinión, aunque, además, en conclusión*) presented as new -> recap. The new *siempre que / con tal de que / a menos que* section is drilled by one item only: ex08 (builder), ex11 (dictation) and writing ex16, ex19 now drill it (with ex15).
- b1-21-05.ex03 answers conclusión / resumen vs "In conclusion" -> narrowed. ex06 length 13 vs 6 -> longer wrong options. ex14 unmet *límites*, "…ninguna propuesta tiene límites" -> single-fault connector options. ex17 unmet *justifican*. ex19 *por lo tanto* (B2) -> removed. ex02 (es-latam) unmet *técnicas*, *real*.
- b1-21-05 vocabulary: *distinción* unused (and *comunitario*) – both belonged to the old community-debate text -> replaced by *opinar*, *límite*, used in the retold story and the reading items.
- b1-21-05 story: rewritten (295 words, same five paragraphs and ideas, plain B1, no sentence of the original text), source label now "Pastiche … no es un texto suyo", questions rewritten to ask what people do; old questions attributed lines to Clarín.
- Consolidation: copies of lesson items varied (ex02, ex04, ex07, ex10, ex12, ex14, ex15); ex09 length 90 vs 46 and Spanish stem with unmet *contiene*; ex06 and ex18 *por lo tanto*; ex13 ninguna; ex16 and ex02 unmet *popular*, *técnicas*, *parlamento*, *legislativa* (es-latam); ex17 *existe*.

## 2. Metadata
- b1-21-04.ex15: teaches changed from the vocabulary slug to porque-y-por-eso (the options differ in the connector); its `distractor_skills` is empty.
- b1-21-05.ex08, ex11, ex16, ex19: teaches conditional-conjunctions (they now drill the skill this lesson teaches); ex08 category grammar.
- Added/kept `distractor_skills` on b1-21-01.ex13/ex14 (subjuntivo-morfologia), b1-21-02.ex15, b1-21-04.ex06, b1-21-05.ex06, b1-21-consolidation.ex06/ex09/ex14.
- Lock: run `scripts/lock_tags.py` after applying (the unit is not locked in this worktree; not checked).

## 3. Goals / checklists
- b1-21-01 goal/checklist "Use four new opinion terms" (list has five; checklist-shared with b1-34-01) -> "Use the new words for positions and limits."
- b1-21-02 "three new contrast terms" (shared with b1-23-02, b1-32-03) -> "the new words to admit a point and contrast it".
- b1-21-03 "three new evaluation terms" (list has four; now six; shared) -> "the new words for evaluating and discussing".
- b1-21-04 "three new argument terms" (shared with b1-28-05; the first reworded line was shared with b1-17-05) -> "the new words for justifying a view".
- b1-21-05 "Qualify claims when evidence is limited" was not practised and the lesson now teaches conditional conjunctions -> "Set a condition with siempre que, con tal de que or a menos que"; "three new debate terms" (five listed) -> "the new words for debating".

## 4. Doubtful
- b1-21-04: *ya que* and *en cambio* are not on the knowledge sheet; presented as new here. No skill exists for them; items stay tagged porque-y-por-eso / contrast-concession-connectors (unsure).
- b1-21-05 first checklist line (canDo) "I can take part in a sustained debate." sits oddly on a challenge that retells the story; kept as the rulebook requires.
- Story: it is a pastiche, no claim about Clarín's text is made; only the label "Paliques" / Leopoldo Alas "Clarín" as author of a column series by that name should be web-checked (unsure; not quoted from memory).
- The old file content/…/stories/classics/b1/b1-21.json (community debate) is now unused by the lesson; left alone.
- Recap unit numbers (B1 Unit 1, 13, 25, 33; A2 Unit 5, 27, 28) come from the knowledge sheet.

## 5. Dictionary
None: the audit lists no "not in the dictionary" and no "literal compound guess" words for b1-21-paliques, before or after the rewrite.

Fix count: 94 fixes (opinions-arguments).
