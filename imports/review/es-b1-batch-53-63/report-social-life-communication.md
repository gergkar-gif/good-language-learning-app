# es-es b1 social-life-communication (B1 Unit 53)

Fixes: 93 (`fixes-social-life-communication.json`), challenges: 6 (`challenges-social-life-communication.json`). check-content: 0 errors / 0 suspects before and after. Unmet words (`unmet-words.js`, six stems): es-es 31 hits before, 0 after (one name left, *Ramas*, and the inflected *aclaramos*); es-latam 36 before, 0 after. Applied to a scratch copy of both courses; `check_fixes.py` 0 rejected. `validate-content` fails only on the locked tags of ex03, ex13 (b1-27-01), b1-27-04.ex14, b1-27-consolidation.ex14 (the retags below): run `lock_tags.py` for them.

## 1. Found by reading
- b1-27-01 grammar screen: text is a stray word list ("decir, preguntar, contar, hablar con and ponerse en *contacto* con"), broken italics, A2 forms (*indefinido*, *le*) presented as new. Rewritten with a recap (A2 Unit 11, A2 Unit 25).
- b1-27-02 screen: reported speech (B1 Unit 25) and *preguntó si* (A2 Unit 14) presented as new ("Introduce reported speech…"). Recap added; same for b1-27-03 (*según*, B1 Unit 25) and b1-27-05 (screens opened as new).
- b1-27-03 screen: "*quiso* *decir* *que*" broken italics; b1-27-04 screen: "¿*Qué* *quieres* *decir*?" list with broken italics. Rewritten as one sentence each.
- Stems with Spanish metalanguage unmet at the lesson: b1-27-01.ex02/ex06 "[¿Cuál significa…]" (*significa* first b1-27-03), b1-27-02.ex02 (*transmite, correctamente*), ex06 (*palabra, indirecta*), b1-27-03.ex02 (*expresa*), ex06, b1-27-04.ex06 (*palabras*), b1-27-05.ex02 (*distingue, interpretación, realmente*), ex06, consolidation ex02/ex09/ex16. All asked in English.
- b1-27-01.ex06, b1-27-03.ex06, b1-27-04.ex06, b1-27-05.ex06: the option glossed "[to communicate]" / "[intention]" / "[in other words]" / "[to interpret]" repeats the question (give-away). Glosses dropped from those options.
- b1-27-01.ex13 option "Hablé a Ana con." and ex14 "Voy a mensaje mandarle." are non-phrases (word jumbles): replaced by "Hablé de Ana." and "Voy a mandarles un mensaje."
- b1-27-03.ex02 "Quiso decir con no estaba…", ex13 "Quería saber podemos ayudar." (two faults), b1-27-04.ex13 "Quiero decir si el problema." (fragment), b1-27-05.ex12 "No interpreté que nada.", ex14 "No tuve reacción porque reaccioné." (not a reply): each replaced with a one-fault real string.
- b1-27-03.ex05, 04.ex05, 05.ex05, consolidation ex05 (sentence-order): the third sentence is the first two joined, so the order is meaningless. Rewritten as three steps of a story.
- b1-27-03.ex14: right answer has no pronouns while the wrong ones test *le lo / lo se* (tag `pronombres-combinados`). Rewritten so the right answer is *se lo quería explicar*.
- b1-27-02.ex03: `answers` accepts *explicaba* although the English says "explained". Narrowed to *explicó*.
- b1-27-05.ex20-23: reading items ask about Elena, Marta and Carlos, who are not in the story; generic stems ("idea principal", "¿Qué elemento ayuda…?"). Rewritten about the retold story.
- b1-27-05.ex14/ex13/ex17: *reaccioné, reaccionaste* (first b1-37-02), *realmente*, *directamente* unmet. Rewritten or listed (*directamente* added to the 05 list).
- *enfadado/a* (Spain; es-latam says *enojado*) is used in b1-27-04 and 05 in both courses (screens, ex07, ex11, ex17, 05.ex02, ex05, ex09, ex12, ex15, ex19, consolidation ex09). Replaced by *preocupado/a*, met in both courses (A2), so no course variant fix is needed.
- b1-27-consolidation.ex02, ex03, ex06, ex10, ex11, ex13 copy lesson items (ex02 = 27-02.ex02, ex06 = 27-04.ex02, ex10 = 27-03 ex08/11, ex11 = 27-04.ex08, ex13 = 27-03.ex12, ex03 = 27-02.ex08). Varied.
- b1-27-consolidation.ex14: "le lo explicamos" non-phrase and "No aclaramos nada porque hablamos". Rewritten as le / la / missing *con* (`distractor_skills` 1: objeto-directo, tag `objeto-indirecto`).
- Story `b1-27-dondimas`: wrong people and ending (Angélica, rejuvenated Dimas, marriage, "el diablo" unnamed, moral about contracts invented). Retold from Palma's text in 5 paragraphs, 280 words: Dimas, an old rich miserly notary of Lima, loves Visitación, who takes his gifts and ignores him; on the hill of Las Ramas he says any devil may take his *almilla*; Lilit comes, contract for three years, Visitación loves him; after three years he hands over the *almilla*, Lilit takes him to hell, the judges read the contract and a dictionary, he is sent home; Visitación has entered a convent. One sentence explains *almilla* ("alma pequeña" vs a garment). Reported speech in the indicative only (*decía que, dijo que, le preguntó qué iba a hacer, contestó que*); no imperfect subjunctive after a past verb, no *después de que*. Source line now "Adaptación simplificada de «D. Dimas de la Tijereta», de las Tradiciones peruanas de Ricardo Palma (dominio público)"; characters and `grammar` list fixed; three comprehension questions rewritten (what Dimas says, what he does at the end, what Visitación does).
- b1-27-05 vocabulary: story words in no list added (notario, diablo, almilla, cerro, juez, infierno, convento, directamente); all are used in reading items or ex17 (no `vocab-unused`).

## 2. Metadata
- b1-27-01.ex03 and ex13 (*hablé con*) were tagged `verbos-regimen-preposicional`, a skill taught in b1-29-03: retagged to `b1-social-life-communication-vocab` (ex03 `category` grammar -> vocabulary). Needs `lock_tags.py`.
- b1-27-04.ex14 retagged `estilo-indirecto` -> unit vocab (the wrong option shows *lo que* vs *que*, not reported speech). b1-27-consolidation.ex14 retagged to `objeto-indirecto`, `category` grammar. Both need `lock_tags.py`.
- structured-writing prompts that did not pin the stored answer ("Describe a misunderstanding.", "Clarify an idea.") rewritten in 27-01 ex15-16, 27-02 ex15-17, 27-03 ex15-17, 27-04 ex15-17, 27-05 ex15-19, consolidation ex17-18.
- No skill is registered for the lessons themselves, as intended; all `teaches` slugs exist.

## 3. Goals / checklists
- "Use four/three new … terms." (all five lessons) -> "Use the new words for …" in goal and checklist. 27-05 now lists 11 words.
- 27-01 "Use common communication patterns accurately." (vague, repeated as checklist) -> "Say who you speak with and who you send a message to."
- consolidation "Consolidate communication vocabulary." / "I can consolidate…" -> "Review the words for communication and misunderstandings." / "I can use the words for communication and misunderstandings."
- Challenges: written for all six stems (was the generic "Put your Spanish skills into practice"); `canDo` = each lesson's first checklist line (consolidation: the reworded line).

## 4. Doubtful
- Story facts for the web check (all from the Wikisource text of Palma's "D. Dimas de la Tijereta", Tradiciones peruanas): Dimas an escribano (rendered *notario*) of Lima, old, rich, tricky; Visitación about twenty; the hill is "el cerro de las Ramas"; the devil is Lilit, sent by Satanás; contract for three years; "almilla" = jubón interior (garment); the judges decide with the "Diccionario de la lengua"; Visitación enters a *beaterio* (I wrote *convento*, a simplification; unsure); "es fama que desde entonces los escribanos no usan almilla" (I wrote "Se cuenta que… los notarios no llevan almilla"). The source's own ending (Dimas's soul refused in hell, Judas's soul) is left out.
- "alma pequeña" explanation of *almilla* is the brief's wording (-illa is a diminutive of *alma*); not in Palma's text.
- Retags above need `lock_tags.py` with a reason.

## 5. Dictionary
lilit | Lilit | noun | Lilit (the name of the devil in the tale; a name) |
