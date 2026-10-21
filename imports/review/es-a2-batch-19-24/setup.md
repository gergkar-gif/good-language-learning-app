# es A2 batch: es-a2-batch-19-24

Started 2026-10-21T11:43:18Z from origin/master e81d17f6. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 19 the-future (a2-19-01 a2-19-02 a2-19-03 a2-19-04 a2-19-05 a2-19-consolidation; stories ['a2-19']); Unit 20 looking-back-moving-forward (a2-20-01 a2-20-02 a2-20-03 a2-20-04 a2-20-05 a2-20-consolidation; stories ['a2-20']); Unit 21 imperfect-tense (a2-imperfectobasico-01 a2-imperfectobasico-02 a2-imperfectobasico-03 a2-imperfectobasico-04 a2-imperfectobasico-05 a2-imperfectobasico-consolidation; stories [])
- Reader B: Unit 22 imperfect-vs-preterite (a2-imperfectocontraste-01 a2-imperfectocontraste-02 a2-imperfectocontraste-03 a2-imperfectocontraste-04 a2-imperfectocontraste-05 a2-imperfectocontraste-consolidation; stories []); Unit 23 giving-instructions-directions (a2-imperativoafirmativo-01 a2-imperativoafirmativo-02 a2-imperativoafirmativo-03 a2-imperativoafirmativo-04 a2-imperativoafirmativo-05 a2-imperativoafirmativo-consolidation; stories ['a2-imperativoafirmativo']); Unit 24 setting-rules-warnings (a2-imperativonegativo-01 a2-imperativonegativo-02 a2-imperativonegativo-03 a2-imperativonegativo-04 a2-imperativonegativo-05 a2-imperativonegativo-consolidation; stories ['a2-imperativonegativo'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 19 the-future | 24 / 17 | 24 / 20 |
| 20 looking-back-moving-forward | 15 / 26 | 15 / 26 |
| 21 imperfect-tense | 10 / 34 | 10 / 35 |
| 22 imperfect-vs-preterite | 4 / 87 | 4 / 87 |
| 23 giving-instructions-directions | 0 / 52 | 0 / 51 |
| 24 setting-rules-warnings | 0 / 82 | 0 / 80 |

## Files differing es-es vs es-latam

- the-future: a2-19-05-ex.json, a2-19.json
- looking-back-moving-forward: none
- imperfect-tense: a2-imperfectobasico-01-gr.json, a2-imperfectobasico-02-gr.json, a2-imperfectobasico-03-gr.json, a2-imperfectobasico-04-ex.json, a2-imperfectobasico-05-gr.json, a2-imperfectobasico-consolidation-gr.json
- imperfect-vs-preterite: none
- giving-instructions-directions: a2-imperativoafirmativo-05-gr.json, a2-imperativoafirmativo-05-ex.json, a2-imperativoafirmativo.json
- setting-rules-warnings: a2-imperativonegativo-01-ex.json, a2-imperativonegativo-02-ex.json, a2-imperativonegativo-03-voc.json, a2-imperativonegativo-03-ex.json, a2-imperativonegativo-05-gr.json, a2-imperativonegativo.json

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> a2 --jobs 4 --only a2-19-01 a2-19-02 a2-19-03 a2-19-04 a2-19-05 a2-19-consolidation a2-20-01 a2-20-02 a2-20-03 a2-20-04 a2-20-05 a2-20-consolidation a2-imperfectobasico-01 a2-imperfectobasico-02 a2-imperfectobasico-03 a2-imperfectobasico-04 a2-imperfectobasico-05 a2-imperfectobasico-consolidation a2-imperfectocontraste-01 a2-imperfectocontraste-02 a2-imperfectocontraste-03 a2-imperfectocontraste-04 a2-imperfectocontraste-05 a2-imperfectocontraste-consolidation a2-imperativoafirmativo-01 a2-imperativoafirmativo-02 a2-imperativoafirmativo-03 a2-imperativoafirmativo-04 a2-imperativoafirmativo-05 a2-imperativoafirmativo-consolidation a2-imperativonegativo-01 a2-imperativonegativo-02 a2-imperativonegativo-03 a2-imperativonegativo-04 a2-imperativonegativo-05 a2-imperativonegativo-consolidation
- Readers launched 11:44:42Z.
