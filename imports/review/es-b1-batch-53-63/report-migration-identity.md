# es-es b1 migration-identity (B1 Unit 57)

Fixes: 92 (`fixes-migration-identity.json`), challenges: 6 (`challenges-migration-identity.json`). check-content: 0 errors / 0 suspects before and after. Unmet words (six stems): es-es 29 before, 1 after (*acostumbré*, inflected form of the listed *acostumbrarse*); es-latam 37 before, 1 after (same). Applied to a scratch copy of both courses; `check_fixes.py` 0 rejected. `validate-content` fails only on locked tags (retags below): run `lock_tags.py`.

## 1. Found by reading
- b1-29-03 does not teach `verbos-regimen-preposicional`: the screen only listed four verbs and a tip about "process"; no item tested a preposition (ex02 vocab MC, ex03 tested the preterite, ex13 future). Screen rewritten to teach the rule (*acostumbrarse a, adaptarse a, empezar a, darse cuenta de*; learn verb + preposition; English differs), third example now shows *darse cuenta de*, tip fixed. Items now testing it: ex02 (new MC), ex03 (blank is the preposition *a*), ex04, ex08, ex13 (wrong = *en* / missing *a*), ex16, consolidation ex04.
- b1-27-01 had tagged *hablé con* with this skill before its screen (see Unit 53 report).
- b1-29-01 ex13/ex14 wrong options *pertenezco de / pertenece de* test *pertenecer a*, which no screen teaches: replaced by faults on *sentirse parte de* / *forma parte de*. Examples/ex05 say "vivo en Vietnam", but they live in Budapest from B1: now Meg, South Africa/Budapest.
- Screens presenting known grammar as new, with recap added: 29-01 (*ser de, vivir en*, A1), 29-02 (*indefinido/imperfecto*, A2 Unit 22), 29-04 (*que, donde* B1 Unit 9; *lo que* B1 Unit 39), 29-05. Broken italics in tips of 29-01 and 29-04 fixed.
- Spanish metalanguage in stems (*expresa, palabra, mudanza, verbo, oración, relativa, combina, integra, unidad*) in 29-01…05 and consolidation: asked in English. Glosses on the right option copying the question (29-01 ex06, 29-02 ex06, 29-03 ex06, 29-05 ex06): dropped; 29-02 ex06 and 29-03 ex06 used later words (*adaptarse*, *hogar*).
- sentence-order with a third sentence that joins the first two: 29-01 ex05, 29-02 ex05, 29-04 ex05, 29-05 ex05, consolidation ex05. Rewritten.
- 29-02 ex04 tagged `imperfect` for *mudé* (preterite): retagged. 29-03 ex14 option "Era aprenderé mucho." two faults; ex12 *rápidamente* unmet; 29-05 ex12 two wrong options fail the same way, ex14 long wrong options (*tranquilidad, locales*); consolidation ex14/ex15/ex09/ex16 long options with *nació, aislada, intentar, únicamente, propia*. Fixed.
- *migrar* (no list) in 29-05 ex18/19 and consolidation ex17, *solamente* in ex18: replaced by *mudarse* / *solo*.
- Consolidation ex02, ex03, ex10, ex11, ex12 copy lesson items: varied.
- 29-05 reading ex20-23 are about "Daniel", not in the story: rewritten about Martí (1871, New York, 1895). *independencia* added to the 05 list (es-latam lacked it).
- Story `b1-29-exilio`: no hard labour, no Zaragoza, no 1880, *como si nunca se hubiera marchado* (pluperfect subjunctive), literary questions. Retold in 5 paragraphs, ~260 words, with the brief's facts: born in Havana 28 January 1853; sentenced to hard labour for his ideas, sent to Spain in January 1871 aged 17; law and philosophy in Madrid and Zaragoza; Mexico 1875, Guatemala 1877, Venezuela 1881; first in New York 1880, settled 1881; 1895 back in Cuba, died at Dos Ríos on 19 May, weeks after landing. Narrator (not Martí) draws the "two identities" point; no quotation. Source line "Adaptación biográfica simplificada de la vida de José Martí; no es una traducción ni una cita de sus textos."; three questions rewritten.

## 2. Metadata
- Retagged: 29-02.ex04 -> `preterito-indefinido`; 29-03.ex02 (grammar, `verbos-regimen-preposicional`), ex03 and ex13 -> `verbos-regimen-preposicional` (ex13 ds removed); 29-04.ex17 -> `relativas-preposicion-el-que`, grammar; 29-05.ex12 ds fixed. All need `lock_tags.py`.
- structured-writing prompts pinned in 29-01 ex15-16, 29-02 ex15-17, 29-03 ex15-17, 29-04 ex15-17, 29-05 ex15-19, consolidation ex17-18.

## 3. Goals / checklists
- "Use three/four new … terms." -> "Use the new words for …" in all five lessons; 29-03 goal line 2 now names the skill; consolidation first lines reworded. Challenges written for six stems.

## 4. Doubtful
- Story facts for the web check: all dates and places above come from the brief; unsure: "organizaba reuniones con otros cubanos", "escribió artículos sobre Cuba, América Latina y los Estados Unidos", "pocas semanas después de llegar", "lo condenaron a trabajos forzados" placed before the 1871 deportation.
- Core items tagged with `verbos-regimen-preposicional` elsewhere (b1-40-01, b1-40-05, b1-40-consolidation, cultura units b1-autonomias, b1-cortes): outside my units; their screens are not in b1-29-03 (group 4 note).

## 5. Dictionary
None: no word flagged in either course.
