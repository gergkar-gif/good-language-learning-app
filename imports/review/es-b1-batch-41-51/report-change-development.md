# es-es b1 change-development (B1 Unit 49): reader report

check-content: before 23 errors (19 length-giveaway, 9 tell-absolute incl. checklist-shared 1); after the fixes on a scratch copy: 0 errors, 0 suspects. validate-content: schemas pass; locked-tag items listed in group 2.
Unmet-word check (one --stems list of the six stems): **es-es 41 hits before, 3 after; es-latam 48 before, 3 after.** The 3 left in both courses are `adaptábamos` (04.ex15, 05.ex14, consolidation.ex14): the deliberate wrong imperfect form (distractor_skills imperfect) of *adaptarse*, listed in lesson 04.

## 1. Found by reading
- **b1-25-01 does not teach its skill.** `verbs-of-change` (*ponerse, volverse, hacerse, quedarse*) appears in no screen: the screen lists *hacerse, convertirse en, pasar de… a…, seguir* + gerund and the 4 examples contain none of the four verbs. Screen rewritten (one sentence per verb, italics one run per term, recap "you know *seguir* + gerund from A2 Unit 28"), four examples added (*se puso triste, se volvió serio, se hizo médico, se quedó sola*), tip now guides the choice of verb; the four verbs added to b1-25-01-voc.json; goal/checklist lines name them. Exercises: ex03 (fill-blank *se puso*), ex08 (builder *se hizo médico*), ex13 (dialogue *se quedó sola*), ex15 (writing *se volvió*) now test the skill; consolidation.ex03 tests *hacerse*.
- b1-25-02 grammar presents the imperfect / present perfect contrast (B1 Unit 9) as new, broken italics ("en *aquella* *época*"), and the tip says *todavía* and *ya* "work as a pair… pinpoint exactly when a shift happened" (wrong) -> recap, tip "*todavía* for what has not changed, *ya no* for what has".
- b1-25-03 grammar presents the future (A2 Unit 19), *ir a* (A1 Unit 25), *es posible que* (B1 Unit 25) as new; b1-25-04 presents necessity + subjunctive (A2 Unit 27, B1 Units 35 and 39) as new with stray italic runs ("es *necesario* *que*"); b1-25-05 has no recap -> recaps added.
- Story `b1-25-trafalgar`: draft told things the outline does not give (Gabriel becomes a soldier, then a cultured man who knew politicians; "miles de marineros murieron"; "España nunca ha vuelto a tener la misma fuerza naval"), never named don Alonso or the ship, and the comprehension questions were B2 Spanish ("simbolismo… del protagonista"). Rewritten in plain B1 Spanish, 234 words, same five paragraphs: old Gabriel remembers; Cádiz orphan serves captain don Alonso Gutiérrez de Cisniega; Trafalgar on the *Santísima Trinidad*; how he changed; the old man looks back. Shows *se pusieron, se quedó, se hizo, se volvió, pasó de ser… a ser…*. Label "Adaptación simplificada de «Trafalgar»…". Questions rewritten.
- Reading items b1-25-05.ex20-23 were about "un filósofo" (not the story); `nunca` tells in ex21/ex23 -> rewritten for the new story.
- Length give-aways fixed: 01.ex02, ex09, ex10; 02.ex06, ex12; 03.ex12; 04.ex09; 05.ex09, ex12; consolidation ex02, ex06, ex11. Tell-absolute fixed: 01.ex12, ex14 (*nunca*), 03.ex15 (*ninguna*), 05.ex20-23, consolidation.ex16.
- Non-phrase / absurd wrong options: 03.ex14 opt 3 "No, cambiará en el pasado." -> "Sí, probable que cambie."; 03.ex15 opt 3 -> "Creo que seguirás creciendo."; 05.ex13 opt 3 -> agreement fault; 01.ex14 opt 3 (meaning-only) -> "Se ha convertida…"; 02.ex14 opt 3 "En el futuro, … circulaba" (also unmet) -> "…se circula rápidamente".
- answers-alternatives: 02.ex03 *Antiguamente* (unmet) removed; english fits *Antes*.
- Unmet words replaced (examples): *palabra, significa* in stems (01.ex06, 02.ex02, 02.ex06, 03.ex02, 03.ex06, 04.ex02, 04.ex06, 05.ex02, 05.ex06, consolidation ex02, ex06, ex09, ex16: asked in English); *modernos, increíblemente, cualquier, circulaba, valoramos, globalizado, avanza, manera, radical, modificar, tecnológico, laboral, siglo, sistemas, marinero, rico*; *desarrollo* (03.ex06, listed only in lesson 05).
- Consolidation copies varied: ex04 and ex08 copied screen/04 sentences; ex12 copied 03.ex10.
- Story words listed in lesson 05: *huérfano, capitán, batalla* (used in the reading items). 05.ex19 now uses the listed *reflexionar* (it was `vocab-unused`).

## 2. Metadata
- Tag changes on locked exercises (run `python scripts/lock_tags.py es-es b1/change-development --update --reason "verbs-of-change items"`): b1-25-01.ex03 (was perifrasis-verbales -> verbs-of-change), ex08 (same), ex13 (perifrasis-verbales -> verbs-of-change), ex15 (b1-change-development-vocab -> verbs-of-change), b1-25-consolidation.ex03 (vocab -> verbs-of-change). 01.ex12 gets `distractor_skills` for the present (option 1) and the future (option 2).
- 01.ex16 and 01.ex14 stay `verbs-of-change`. No core item is tagged with a skill taught in a cultura or latam lesson.
- Open writing items carry grammar tags (AGENTS: open writing -> unit vocabulary); left (unsure).

## 3. Goals / checklists
- 01: "Use structures for development and transformation." -> "Use ponerse, volverse, hacerse and quedarse for different kinds of change."; "four new change-related terms" -> "the new words for change" (list is eight).
- 05: "Use three new discussion terms." (list had four, now seven; checklist-shared with b1-26-05 and b1-30-05) -> "Use the new discussion and story words." / checklist "I can use the new words for change and development."
- consolidation: "Consolidate change and development vocabulary." -> "Review the words for change and development." / "I can use the words for change and development."
- Six challenges written (`challenges-change-development.json`); canDo copied from each lesson's first checklist line after the fixes. Lauren (Meg's sister) is used in 01; Carlos's grandmother in Madrid in 02.

## 4. Doubtful
- Story, claims for the reviewer's web check (not verified from memory): that in Galdós's *Trafalgar* the old narrator Gabriel Araceli is a Cádiz orphan who as a boy serves don Alonso Gutiérrez de Cisniega (reviewer-confirmed outline); that he goes with him on the *Santísima Trinidad*; the battle in October 1805 off Cape Trafalgar; the Franco-Spanish fleet lost to the British; "Cádiz… un puerto alegre" becoming a place of fear.
- Added by the retelling, not checked: everyone "se pusieron muy nerviosos"; Gabriel "se quedó sin palabras"; afterwards he became "más serio… fuerte y tranquilo"; the old Gabriel by the window reflecting (the closing paragraph is the retelling's, from the draft).
- 05.ex13 opt 2 "No presenta ningún desafío." is a meaning-only fault; left (unsure).
- Examples use "mi amiga / mi vecino / un amigo mío" so no character fact is claimed.

## 5. Dictionary
cisniega | Cisniega | noun | surname (don Alonso Gutiérrez de Cisniega)

## Fix count
change-development: 68 fixes in `fixes-change-development.json` (es-es paths; mirror to es-latam by script, 0 unmatched). Challenges: 6.
