# ES B1 core Units 5–15 (2026-11-11)

Units (es-es numbers): 5 `plans-ambitions`, 7 `giving-advice`, 9 `relationships` (reader A); 11 `work-professional-life`, 13 `education-learning`, 15 `travel-mobility` (reader B). Two Sonnet readers, three units each; es-es read once and mirrored.

| Reader | Tokens, minutes | Fixes proposed (per unit) | Rejected | Changed by the reviewer |
|---|---|---|---|---|
| A | 420,688, 28 min (~140k a unit) | 246 (93 / 81 / 72) | 0 | 2 |
| B | 450,898, 25 min (~150k a unit) | 172 (60 / 55 / 57) | 0 | 4 |

State: all six units frozen in es-es and es-latam (B1 8/76 per course). check-content 0 errors in every unit and course; accepted suspects in `accept.txt` (consolidation replays; `dirigir` used as *dirijo*). Unmet words 0 in both courses. Walk 36/36 lessons per course, challenges on screen and passing (b1-03-01 es-latam rewalked after its last edit). 36 challenges per course.

## Reviewer changes

- Unit 7: a Spanish gloss with *después de que* (B2) reworded; the story's last line *con quien lo alaba* (relative before b1-05-04) → *si alguien lo alaba*.
- Unit 11: *a raíz de* glossed "as a result of", not "because of".
- Unit 13: "Rousseau también pide paciencia" (unsupported attribution) → "El educador necesita paciencia."
- Unit 15: *Cuando todo esté preparado, compraremos los billetes mañana* lost its *mañana* (screen and listening item).
- Challenges: the Odiseo target put in one tense; the Little Women scenario reworded.
- es-latam: `fix_variant_vocab.py` for the batch's units (*boleto, computadora, enojado*), *coger* → *tomar* by hand in Unit 15, two words met only in the es-es *vosotros* unit replaced (*apetece*, *atención*).

## Incident

`fix_variant_vocab.py es-latam b1 --write` was first run level-wide and turned *hospitales móviles* into *hospitales celulares* in the unread unit `b1-revolucionmexicana-03`. Every change outside this batch's six units was reverted before committing (71 files). The script now has `--only <stem prefixes>` and the word table keeps *móviles* after *hospitales, clínicas, bibliotecas, teléfonos*.

## For the user

1. **Imperfect subjunctive forms are taught nowhere in B1.** `hypothetical-structures` (b1-04-02) and `si-clauses` (b1-08-04) use *fuera, tuviera, perdiéramos*; the forms screen is B2 (`imperfect-subjunctive-forms`, b2-15-01), and b1-38-01 teaches only the sequence of tenses. For now b1-04-02 presents *Si yo fuera tú* as a ready-made phrase, and b1-08-04 says the pattern is known from Unit 7. Options: (a) move the forms screen into B1 before b1-04-02 or b1-08-04 (a skill-level change, needs sign-off and a frozen-list entry); (b) keep B1 to set phrases and move the hypothetical items of b1-08-04 (ex07, 08, 10, 11, 14, 17, b1-08-05.ex19, consolidation ex12, ex15) to real conditions; (c) leave as is.
2. **Passive *se* is screened twice in es-es:** the cultura lesson `b1-constitucion-01` (Unit 2) and core b1-06-03 (Unit 11), which is the registered `taught_in`. Decide when the cultura track is read.
3. **Lessons with no new grammar:** b1-07-02 (*se*, *hay que*: both known) and b1-08-03 (A1 movement prepositions) are vocabulary lessons with a recap; b1-07-04 has only two items on `superlatives`, none on the absolute superlative its screen now shows; b1-07-05 has no item on *me parece que*. Thin-skill work for the level checklist.
4. **About 20 structured-writing prompts per unit do not pin their single stored answer** ("Describe your current professional role."). Not rewritten; a level-wide decision (looser grading or tighter prompts).
5. **Orphan exercises** (in a file, in no lesson): b1-05-03.ex17, b1-05-04.ex17, b1-07-05.ex18, ex19. Delete or wire in.
6. **No skill covers reciprocal *se/nos*** (b1-05-01 items use `reflexives`). The list is frozen; reported only.
7. ***si* + present + future** is used in Units 5 and 7 before its screen (b1-08-04). Left, since A2 learners meet basic *si*; say if it should be treated as not yet known.
8. Story metadata still says "Adapted from …" for the free Little Women scene and credits Samaniego for a retelling that uses neither author's wording.
