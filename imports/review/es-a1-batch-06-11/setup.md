# es A1 batch: units 6-11 (route A, Spanish template, three units per reader)

Started 2026-10-16T03:41:51Z from origin/master 19791490. Two Sonnet readers, **three units each** (user, 2026-10-16), worktrees /home/user/parlour-read-a and -b; es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 6 daily-routine (a1-06-01…05, a1-06-consolidation; story a1-06), Unit 7 daily-routine-reflexive-verbs (a1-reflexive-01…05, consolidation; story a1-reflexive), Unit 8 home (a1-07-01…05, consolidation; story a1-07)
- Reader B: Unit 9 supermarket (a1-08-01…05, consolidation; story a1-08), Unit 10 demonstratives (a1-demonstrative-01…05, consolidation; story a1-demonstrative), Unit 11 ordering-cafe (a1-cafe-01…05, consolidation; story a1-02)

Stems and stories checked against content/es-es/curriculum/units/a1.json and content/es-es/stories/manifest.json (Unit 11's story file is a1-02, id story.a1.cafe, on lesson a1-cafe-05).

## Baseline check-content (before the read), errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 6 daily-routine | 2 / 33 | 2 / 34 |
| 7 daily-routine-reflexive-verbs | 7 / 91 | 7 / 96 |
| 8 home | 1 / 3 | 1 / 3 |
| 9 supermarket | 2 / 24 | 2 / 22 |
| 10 demonstratives | 8 / 75 | 8 / 82 |
| 11 ordering-cafe | 7 / 9 | 7 / 9 |

## Files differing es-es vs es-latam (cmp)

| Unit | exercise files | lesson files | screens (grammar) | vocabulary | story |
|---|---|---|---|---|---|
| 6 daily-routine | 2 of 6 | 0 of 6 | 3 of 7 | 0 of 5 | 0 of 1 |
| 7 daily-routine-reflexive-verbs | 1 of 6 | 0 of 6 | 4 of 5 | 1 of 5 | 1 of 1 |
| 8 home | 0 of 6 | 0 of 6 | 1 of 5 | 0 of 5 | 1 of 1 |
| 9 supermarket | 0 of 6 | 0 of 6 | 2 of 5 | 0 of 5 | 1 of 1 |
| 10 demonstratives | 0 of 6 | 0 of 6 | 0 of 5 | 0 of 5 | 1 of 1 |
| 11 ordering-cafe | 2 of 6 | 0 of 6 | 3 of 5 | 1 of 5 | 1 of 1 |

Differing files: a1-06-02-ex.json, a1-06-03-ex.json, a1-06-02-ar-verbs-gr.json, a1-06-03-er-ir-verbs-gr.json, a1-06-04-reflexive-verbs-gr.json, a1-reflexive-01-ex.json, a1-reflexive-01-pronombres-gr.json, a1-reflexive-02-cambio-radical-gr.json, a1-reflexive-03-vestirse-ponerse-gr.json, a1-reflexive-04-contraste-gr.json, a1-reflexive-04-voc.json, a1-reflexive.json, a1-07-03-estar-location-gr.json, a1-07.json, a1-08-03-querer-gr.json, a1-08-04-necesitar-gr.json, a1-08.json, a1-demonstrative.json, a1-cafe-01-ex.json, a1-cafe-consolidation-ex.json, a1-cafe-01-tomar-gr.json, a1-cafe-02-comer-gr.json, a1-cafe-03-querer-gr.json, a1-cafe-01-voc.json, a1-02.json
- Readers launched 03:44:11Z (Sonnet, background); prompts in prompt-a.txt / prompt-b.txt.
- Reader A: 312,954 tokens, 53 tool uses, 15.3 min (03:42-03:58), 32 + 57 + 26 = 115 fixes proposed (~104k a unit); report file write allowed
- Reader B: stopped 03:5x on a Sonnet session limit (429, reset 04:30 UTC) after writing all three fixes files (40 + 89 + 34) and challenges files; its report file covered Units 9-10 only. Resumed 04:39 for the Unit 11 report.
- Reader B (resumed 04:39-04:40, 2 tool uses, 44 s): completion notice reports 305,712 tokens (the first run's failure notice carried no usage, so this is the only figure; read time 03:42-03:57, ~15 min); fixes 40 + 89 + 34 = 163; report file write allowed (Unit 11 appended on resume)
