REPORT: es-latam B2 Unit 9 (conditionals-potential-scenarios) and Unit 10 (conditionals-counterfactuals-regrets). Nothing committed. I did not write a report file; this reply is the report.

CHECKS (before -> after)
- check-content, Unit 9: 10 errors, 20 suspects -> 0 errors, 1 suspect.
- check-content, Unit 10: 8 errors, 17 suspects -> 0 errors, 0 suspects.
- The one remaining suspect is `answers-alternatives` on b2-09-02.ex03. *quisiera* and *querría* are both right and both fit the `english`. This is the true-alternatives case the rule allows.
- unmet-words: Unit 9 before: about 70 hits. After: 1, the name "Luna" (Eva Luna) in a reading option.
- unmet-words: Unit 10 before: about 40 hits. After: 0.
- render_lesson on all 12 stems: 0 `!!` lines.
- check_unit_refs `--labels --bare`: 0 recaps to check in both units.
- validate-content `--changed`: es-latam 47 passed, 0 failed.
- `build-manifest.py` and `build_word_lesson_index.py` were run, so generated files (curricula, decks, manifests, word-lesson-index) show as modified.
- Challenges files, six entries each, keyed by lesson stem: `/home/user/parlour-read-b/challenges-conditionals-potential-scenarios.json` and `/home/user/parlour-read-b/challenges-conditionals-counterfactuals-regrets.json`. They are not merged into `curriculum/challenges.json`. In the render, each lesson's challenge screen still shows the auto-generated placeholder scenario until you merge them.
- I could not check challenge targets against the met-words list. The word index is by lemma and the targets use inflected forms; I only checked for obvious unmet words.

WHAT CHANGED IN BOTH UNITS
- All grammar screens are rewritten in English, with "You know *X* from Unit N" recaps.
- Lesson titles, goals, checklists and vocabulary titles are in English. Every lesson now has an `srs` section and a `checklist`. Lesson 1 of each unit has a rewritten intro; the other intros were removed.
- All question stems are in English. Every multiple-choice item takes neither `hint` nor `english`.
- Old `ex05` multiple-choice items that were copied across lessons became real `dialogue-complete` items.
- Vocabulary lists are cut to the 5 words each lesson uses. The matching item has 5 pairs.
- Wrong options have one fault each. I set `distractor_skills` only where the wrong option is a real form of another skill. Exercise ids are unchanged; the consolidations got a ninth item (ex09), listed in their lesson files.
- Both texts are rewritten as original texts. I set `lesson` 5 and added `order` 9 / 10 in the story files, to match the finished B2 stories.

UNIT 9, lesson by lesson
- 01, `hypothetical-structures`: screen contrasts open *si* + present (B1 Unit 8) with imagined *si* + imperfect subjunctive (B1 Unit 4). Items ex02-ex06 rewritten. The old claim that the conditional is "stigmatised" after *si* is now a plain tip.
- 02, `apodosis-condicional-literaria`: the screen teaches *quisiera*, *pudiera* and *debiera* as softer forms of *querría*, *podría* and *debería*, and says plainly that the conditional is the normal form. *Hubiera* is not taught. The old literary example "Si tuviera alas, volara" is gone. Items ex02-ex06 rewritten.
- 03, `polite-softening`: the screen covers *si fuera tan amable de* + infinitive, *Si tuviera un momento…*, *Le agradecería que* + imperfect subjunctive, and *Sería mejor que* + imperfect subjunctive. Items ex02-ex06 rewritten.
- 04, `conditional-conjunctions`: the screen recaps *con tal de que* (B1 Unit 21) and *siempre que* (B2 Unit 7). It adds *a condición de que*, the infinitive after *con tal de* / *a condición de* (same subject, B2 Unit 4), and the imperfect subjunctive after a past or conditional main verb. I dropped the old *a poco que* and *en caso de que* rows. Items ex02-ex06 rewritten.
- 05, `conditional-conjunctions`: the screen recaps *a menos que* (B1 Unit 21) and adds *a no ser que*, *salvo que* and *salvo si* + indicative. Items ex02-ex06 rewritten.
- Consolidation: 9 items. Two reading items are answerable from the text.

UNIT 10, lesson by lesson
- 01, `pluscuamperfecto-subjuntivo-si`: recap of *si hubiera…, habría…*. The B2 nuance is clause order, negatives in both clauses, and *si no hubiera sido por* + noun. Items rewritten.
- 02, `apodosis-condicional-literaria`: recap of Unit 9, then *hubiera* + participle in the result clause for every verb. Items rewritten.
- 03, `regrets-reproaches`: *debería haber*, *tendría que haber*, *me arrepiento de*. No *ojalá* and no *si al menos*. Items rewritten.
- 04, `implicit-conditionals`: *de* + infinitive (*De tener tiempo…*, *De haberlo sabido…*, *De ser necesario…*, *De no…*) and the gerund (*Estudiando más, aprobarías*). I removed the absolute participles and *habiendo*, because the participle absolutes are taught only on a hidden-track screen. Items rewritten.
- 05, `inversiones-condicionales-de-haber`: *Hubiera salido antes, habría llegado* without *si*, and *aun cuando* / *aunque hubiera* for "even if". I removed *hubiérase*. Items rewritten.
- Consolidation: 9 items, including an English-prompt `structured-writing` item.
- The Vargas Llosa file's `author` field now reads "(Perú, 1936–2025)".

TEXTS: every factual claim, with how sure I am
Unit 9, Allende, 329 words, 7 paragraphs
1. Allende is a Chilean writer. Given in the brief. Certain.
2. Born 1942. Given. Certain.
3. First novel *La casa de los espíritus*, 1982. Given. Certain.
4. *Cuentos de Eva Luna*, 1989, is a collection of short stories. Given. Certain.
5. Eva Luna tells them. She is the narrator of the earlier novel *Eva Luna* (1987). Given. Certain.
6. "One voice goes through the book from start to finish." Follows from 5. Fairly sure.
7. Reading in publication order is 1982, 1987, 1989. Derived from the dates. Certain.
8. "A story is usually a complete text" and "in a collection you can almost always move on to the next text". These are generic claims about story collections, hedged. They are opinion about the book. Reviewer to accept or cut.
9. The text says it does not tell her life. No private-life claims.

Unit 10, Vargas Llosa, 332 words, 7 paragraphs
1. Peruvian writer. Given. Certain.
2. Born in Arequipa in 1936. Given. Certain.
3. Died in Lima on 13 April 2025. Given. Certain.
4. Nobel Prize in Literature 2010. Given. Certain.
5. *Conversación en La Catedral*, 1969. Given. Certain.
6. Santiago Zavala meets Ambrosio, his father's former driver. They talk for hours in a bar in Lima called La Catedral. Given. Certain.
7. The novel shows Peru under Odría's military dictatorship (1948–1956) through the conversation and many voices and times. Given. Certain.
8. "The title picks up the bar's name." Follows from 5 and 6. Certain.
9. "13 years after the end of the dictatorship" (1969 minus 1956). Derived. Certain.
10. "Reading it calmly, a few pages a day, is advisable" and "a reader who knew only the conversation would see the book is about a country and an era". Hedged hypotheticals and advice. Opinion. Reviewer to accept or cut.
11. The counterfactuals are about readers and the dictatorship in general. Nothing about Santiago.

SPANISH I AM UNSURE OF
- b2-09-02 screen tip: "*quisiese* does not replace the conditional" (the *-se* form is not used for this).
- b2-09-02: "Pudiera ser" as an everyday reply (Latin American use).
- b2-09-02 tip: "older literary texts sometimes use *-ra* in the result of other verbs".
- b2-09-03: *Le agradecería que me enviara…* and *Si tuviera un momento, me gustaría…* as polite formulas.
- b2-09-05: *salvo si* + indicative.
- b2-10-02: the claim that *hubiera* in the result is common across Latin America.
- b2-10-04.ex05: the wrong option "Tener tiempo, iría, …" (a bare infinitive condition, which I believe is not standard). Reviewer to confirm or swap.
- b2-10-03.ex05: the wrong option "no haber viajar" is a non-word with one fault.

FOR THE USER
1. Skills used before their screen:
   - *quisiera*: the A2 Unit 26 `polite-softening` screen does not contain it, although the skill title promises it. It first appears on a B1 Unit 35 screen. My b2-09-02 recap cites B1 Unit 35.
   - *siempre que* is shown on the B1 Unit 21 screen as well as B2 Unit 7. I cited B2 Unit 7 as the brief said.
   - *hubiese* (the *-se* pluperfect) is B2 Unit 16, so I did not teach it and removed it from accepted answers. A learner who types *hubiésemos* in b2-10-01.ex03 or b2-10-05.ex03 is marked wrong.
2. A lesson whose whole point is a skill the sheet lists as later or hidden: none.
3. b2-10-02 has no skill of its own. It tests `apodosis-condicional-literaria`, which is taught in Unit 9 (its alias is `pluscuamperfecto-subjuntivo-apodosis`).
4. Not fixed or left for you:
   - The challenge screens still show placeholder scenarios until you merge my challenges files.
   - b2-09-01.ex03, b2-10-01.ex03 and b2-10-05.ex03 have blanks whose hint names the verb and person (for example "haber, we"). The hint is not the answer.