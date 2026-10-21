# es A2 batch: es-a2-batch-13-18

Started 2026-10-21T10:54:39Z from origin/master bfa0a254. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 13 describing-events-time (a2-13-01 a2-13-02 a2-13-03 a2-13-04 a2-13-05 a2-13-consolidation; stories ['a2-13']); Unit 14 asking-what-happened (a2-14-01 a2-14-02 a2-14-03 a2-14-04 a2-14-05 a2-14-consolidation; stories ['a2-14']); Unit 15 explaining-what-happened (a2-15-01 a2-15-02 a2-15-03 a2-15-04 a2-15-05 a2-15-consolidation; stories ['a2-15'])
- Reader B: Unit 16 plans (a2-16-01 a2-16-02 a2-16-03 a2-16-04 a2-16-05 a2-16-consolidation; stories ['a2-16']); Unit 17 review-experiences (a2-17-01 a2-17-02 a2-17-03 a2-17-04 a2-17-05 a2-17-consolidation; stories ['a2-17']); Unit 18 travel-goodbyes (a2-18-01 a2-18-02 a2-18-03 a2-18-04 a2-18-05 a2-18-consolidation; stories ['a2-18'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 13 describing-events-time | 3 / 19 | 3 / 19 |
| 14 asking-what-happened | 20 / 22 | 20 / 22 |
| 15 explaining-what-happened | 3 / 24 | 3 / 24 |
| 16 plans | 9 / 18 | 9 / 18 |
| 17 review-experiences | 10 / 20 | 10 / 20 |
| 18 travel-goodbyes | 16 / 21 | 16 / 21 |

## Files differing es-es vs es-latam

- describing-events-time: a2-13.json
- asking-what-happened: none
- explaining-what-happened: a2-15-05-ex.json, a2-15.json
- plans: a2-16-05-ex.json, a2-16.json
- review-experiences: a2-17-05-ex.json, a2-17.json
- travel-goodbyes: a2-18-01-gr.json, a2-18-01-ex.json, a2-18-02-voc.json, a2-18-02-ex.json, a2-18-05-ex.json

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> a2 --jobs 4 --only a2-13-01 a2-13-02 a2-13-03 a2-13-04 a2-13-05 a2-13-consolidation a2-14-01 a2-14-02 a2-14-03 a2-14-04 a2-14-05 a2-14-consolidation a2-15-01 a2-15-02 a2-15-03 a2-15-04 a2-15-05 a2-15-consolidation a2-16-01 a2-16-02 a2-16-03 a2-16-04 a2-16-05 a2-16-consolidation a2-17-01 a2-17-02 a2-17-03 a2-17-04 a2-17-05 a2-17-consolidation a2-18-01 a2-18-02 a2-18-03 a2-18-04 a2-18-05 a2-18-consolidation
- Readers launched 10:55:57Z.
- Reader B finished 11:17Z: 365,875 tokens, 70 tool uses, 21.3 min (~122k a unit); fixes 50 + 35 + 48 = 133; report file allowed
- Reader A finished 11:17Z: 341,525 tokens, 65 tool uses, 21.5 min (~114k a unit); fixes 43 + 56 + 45 = 144; report file allowed
