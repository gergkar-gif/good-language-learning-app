# es-es b1 rules-rights-responsibilities (B1 Unit 55)

Fixes: 92 (`fixes-rules-rights-responsibilities.json`), challenges: 6 (`challenges-rules-rights-responsibilities.json`). check-content: 0 errors / 0 suspects before and after. Unmet words (`unmet-words.js`, six stems): es-es 41 hits before, 0 after; es-latam 53 before, 0 after. Applied to a scratch copy of both courses; `check_fixes.py` 0 rejected. `validate-content` fails only on locked tags (b1-28-03.ex12, ex17; b1-28-04.ex13; b1-28-05.ex12; consolidation ex06, ex14, ex15): run `lock_tags.py`.

## 1. Found by reading
- b1-28-01 screen: "Use tener *que*, deber and *hay* que…" presents A1/B1 forms (*hay que*, *tener que*, *deber*, impersonal *se*) as new, broken italics. Recap added (A1 Unit 18, B1 Unit 7, B1 Unit 11); tip italics fixed. b1-28-02 (impersonal *se*, *poder*), b1-28-03 (*es importante que*, A2 Unit 27), b1-28-04 (*porque, por eso* A2 Unit 5; *debido a* B1 Unit 11), b1-28-05 (*creo que* B1 Unit 13; *aunque* A2 Unit 28) the same.
- b1-28-04 screen example, tip, ex03 (`answers` "por lo tanto"), ex11-14 and the old ex14 option use *por lo tanto* (B2): removed everywhere; ex03 now only *por eso*.
- Spanish metalanguage in stems, unmet: b1-28-01.ex02/ex06, b1-28-02.ex02/ex06, b1-28-03.ex02/ex06, b1-28-04.ex02/ex06, b1-28-05.ex02/ex06, consolidation ex02/ex06/ex09/ex16 (*expresa, obligación, expresión, derecho, correctamente, subjuntivo, palabra, posición, combina, integra, unidad, relaciona*). Asked in English.
- Gloss on the right option copies the question (give-away): b1-28-01.ex06, b1-28-02.ex06, b1-28-03.ex06, b1-28-04.ex06, b1-28-05.ex06. Glosses dropped.
- b1-28-03.ex06 option *consecuencia* and ex07 *derechos* are taught in b1-28-04 (later): replaced with *regla* and *las reglas*.
- *aparcar* (Spain-only; es-latam says *estacionar*) and unmet: b1-28-01.ex07, b1-28-02 screen example/ex05/ex07/ex11/ex16, consolidation ex08/ex17. Replaced by *fumar* / *correr* / *entrar con perros*, neutral in both courses; no variant fix needed.
- b1-28-01.ex13 two wrong options both "…hay que fumar" (same fault); b1-28-02.ex14 *prohibición* unmet; b1-28-04.ex13/ex14 nonsense and non-phrase options ("Por eso la situación."); consolidation ex14/ex15 non-phrases ("Por eso porque.", "La regla es un derecho porque regla."): all rewritten with one fault each and `distractor_skills`.
- sentence-order whose third sentence is the first two joined (so the order means nothing): b1-28-04.ex05, b1-28-05.ex05, consolidation ex05. Rewritten as three steps.
- b1-28-03.ex12 copies the options of ex02; b1-28-03.ex14 third option changes the meaning too (two faults); consolidation ex03/ex06 copy lesson items (28-03 ex03, 28-05 ex04/ex10). Varied.
- b1-28-05.ex02 wrong options are long and use *residenciales, normativa, tablón, anuncios, completo*; consolidation ex09 and ex16 right answers are 1.5-2x the wrong ones and use *aprobación, individuales, demás*. Rewritten with met words and balanced lengths.
- b1-28-05.ex20-23 ask about a council, a plaza and tourists, which are not in the story (generic stems "idea principal", "¿Qué elemento ayuda…?"). Rewritten about Martí's essay; 6 story words added to the 05 list (*nacer, propio, copiar, base, escuela, tierra*; *escuela, tierra* because es-latam lacked them).
- Story `b1-28-nuestraamerica`: imperfect subjunctive after a past verb (*era necesario que los gobernantes conocieran, enseñaran, hubiera, reflejaran, encontraran, parecieran*, all b1-38), literary comprehension questions (*admonición, tutela, autóctonos*). Retold in 5 paragraphs, ~230 words, in the present with infinitives and indicative / present subjunctive (*dice que…, hay que enseñar primero la historia de América, es necesario que los futuros políticos estudien…*). The ideas are the three in the brief: the government is born of its own country; the history of America first; learn from the world but keep one's own base (I left out the "trunk" image, which is Martí's own metaphor). No quotation. Source line: "Adaptación simplificada del ensayo «Nuestra América» (1891), de José Martí; no es una traducción ni una cita del texto original." Three comprehension questions rewritten.
- Vocabulary 28-05: *imponer* (used in the new ex22 option), *equilibrar* and *emergencia* are no longer used by any item (the old reading used them). *emergencia* must stay (scenario `es-b1-sc06-denuncia-policial` requiredLemmas); *equilibrar* is unused (no check fails) - drop or use at freeze.

## 2. Metadata
- b1-28-03.ex17 (open writing that really tests the subjunctive) retagged to `subjunctive-value-judgments`, `category` grammar; b1-28-04.ex13 -> `porque-y-por-eso`; b1-28-05.ex12 -> `porque-y-por-eso`; consolidation ex15 -> `porque-y-por-eso` with `distractor_skills` 2: concesivas-aunque; consolidation ex14 gets the same entry. All need `lock_tags.py`.
- structured-writing prompts that do not pin the stored answer ("State one obligation.", "Respond to an opposing view.") rewritten: 28-01 ex15-16, 28-02 ex15-17, 28-03 ex15-17, 28-04 ex15-17, 28-05 ex15-19, consolidation ex17-18.
- No registered grammar skill belongs to b1-28; the `teaches` slugs used (`hay-que`, `deber-vs-tener-que`, `se-impersonal`, `subjunctive-value-judgments`, `porque-y-por-eso`, `formal-cause-connectors`, `giving-opinions`, `concesivas-aunque`, `opinion-verbs-mood`) are all known-by-now skills.

## 3. Goals / checklists
- "Use four/three new … terms." in 28-01…28-05 -> "Use the new words for …" (goal and checklist).
- consolidation "Consolidate rules and obligation vocabulary." / "I can consolidate…" -> "Review the words for rules and obligation." / "I can use the words for rules and obligation."
- Challenges written for all six stems (the generic fallback was shown); `canDo` = first checklist line.

## 4. Doubtful
- Story claims for the web check (Martí, "Nuestra América", 1891; the Wikisource text in `sources/` supports the first four): the government has to be born of the country, its spirit and form fitted to it; the history of America must be taught thoroughly, before that of Greece, and the European university must give way to the American one; the world can be grafted onto our republics but the trunk must be ours; imitation is criticised (*se imita demasiado*, "crear es la palabra de pase"). Less certain (unsure): "muchas ideas importadas no funcionan en América" (paraphrase of the imported book being beaten by the natural man); "algunas personas creen que copiar es la forma más rápida de progresar" (the essay mocks those who imitate Europe, but this exact view is my reading); "escritor cubano del siglo XIX", "1891" (essay published January 1891, New York).
- Retags above need `lock_tags.py` with a reason.

## 5. Dictionary
None: the new story has no word flagged "literal compound guess" or "not in the dictionary" in either course.
