# ES B1 core Units 41–51 (2026-11-12)

Units (es-es numbers): 41 `opinions-arguments`, 43 `possibilities-predictions`, 45 `making-decisions` (reader A); 47 `how-things-work`, 49 `change-development`, 51 `work-ambition-balance` (reader B). Two Sonnet readers, three units each; both stopped by the 5-hour limit and resumed.

| Reader | Tokens (resumed notices) | Fixes proposed (per unit) | Rejected by check_fixes | Changed or added by the reviewer |
|---|---|---|---|---|
| A | 370,764 | 239 (94 / 71 / 74) | 0 | ~14 word fixes in Unit 41 (its own unmet check undercounted), *comunitario* restored |
| B | 384,297 | 200 (75 / 68 / 57) | 1 (rewritten and applied) | 1 challenge |

State: all six frozen in es-es and es-latam (B1 26/76 per course). check-content 0 errors; accepted: *comunitario* unused in b1-21-05 (a conversation scenario requires it). Unmet words: only inflected forms of listed verbs (*pulso, consiste, adaptábamos, dedicaría*). Walk 36/36 lessons per course. 36 challenges per course.

## What the read found

- **Two lessons did not teach their registered skill:** b1-24-04 `prepositional-phrases` (now around *mediante*) and b1-25-01 `verbs-of-change` (the screen listed *convertirse en*, not *ponerse, volverse, hacerse, quedarse*; rewritten, items retagged). Third case after b1-20-01.
- **The new `conditional-conjunctions` section in b1-21-05** got five items (*siempre que, con tal de que, a menos que*).
- **Stories corrected against sources:** Darío's "El pájaro azul" (no doctor; Niní's death, the father's letter, the ending told in one sentence), Palma's "La camisa de Margarita" (the uncle's no-dowry condition, the shirt worth a fortune), Trafalgar and Marianela to their outlines (Marianela now tells its ending). *Pepita Jiménez* to the outline only (no source).
- **Reading items in five of six lesson-05s asked about texts that do not exist** (Gulliver, a scientist, Ulises, a philosopher, "un hombre"): rewritten for the story shown.

## Incidents

1. **The rulebook was truncated by the reviewer** (commit d0e3dabd, 566 → 216 lines, § 6c gone) and both readers worked from it. Restored in 07e4196d. The readers' lists still met the Spanish rules (checked on application).
2. **A reader removed a vocabulary entry a conversation scenario needs** (*comunitario*); the pre-push scenario test caught it. Rule added to the rulebook and template.
3. **Reader A's Unit 41 unmet count was wrong** (it reported 6 left; the reviewer found 27): Spanish glosses in English stems. Scripted: `drop_spanish_stem_glosses.py`.

## For the user

- `por lo tanto`, `ya que` and `en cambio` appear in core screens with no skill of their own (the readers kept *ya que* and *en cambio* as phrases, replaced *por lo tanto*). Fine unless you want them in the skill list.
- Unchanged from earlier batches: hidden exercises in lesson-05 files, orphan story files, word-list growth.
