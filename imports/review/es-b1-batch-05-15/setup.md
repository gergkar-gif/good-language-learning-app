# es B1 batch: es-b1-batch-05-15

Started 2026-11-11T07:43:47Z from origin/master 95d7ab55. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 5 plans-ambitions (b1-03-01 b1-03-02 b1-03-03 b1-03-04 b1-03-05 b1-03-consolidation; stories ['b1-03']); Unit 7 giving-advice (b1-04-01 b1-04-02 b1-04-03 b1-04-04 b1-04-05 b1-04-consolidation; stories ['b1-04']); Unit 9 relationships (b1-05-01 b1-05-02 b1-05-03 b1-05-04 b1-05-05 b1-05-consolidation; stories ['b1-05'])
- Reader B: Unit 11 work-professional-life (b1-06-01 b1-06-02 b1-06-03 b1-06-04 b1-06-05 b1-06-consolidation; stories ['b1-06']); Unit 13 education-learning (b1-07-01 b1-07-02 b1-07-03 b1-07-04 b1-07-05 b1-07-consolidation; stories ['b1-07']); Unit 15 travel-mobility (b1-08-01 b1-08-02 b1-08-03 b1-08-04 b1-08-05 b1-08-consolidation; stories ['b1-08'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 5 plans-ambitions | 7 / 0 | 7 / 7 |
| 7 giving-advice | 7 / 2 | 7 / 4 |
| 9 relationships | 9 / 4 | 9 / 3 |
| 11 work-professional-life | 8 / 3 | 8 / 3 |
| 13 education-learning | 9 / 1 | 9 / 1 |
| 15 travel-mobility | 6 / 5 | 6 / 22 |

## Files differing es-es vs es-latam

- plans-ambitions: none
- giving-advice: none
- relationships: b1-05-consolidation-ex.json
- work-professional-life: none
- education-learning: none
- travel-mobility: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-03-01 b1-03-02 b1-03-03 b1-03-04 b1-03-05 b1-03-consolidation b1-04-01 b1-04-02 b1-04-03 b1-04-04 b1-04-05 b1-04-consolidation b1-05-01 b1-05-02 b1-05-03 b1-05-04 b1-05-05 b1-05-consolidation b1-06-01 b1-06-02 b1-06-03 b1-06-04 b1-06-05 b1-06-consolidation b1-07-01 b1-07-02 b1-07-03 b1-07-04 b1-07-05 b1-07-consolidation b1-08-01 b1-08-02 b1-08-03 b1-08-04 b1-08-05 b1-08-consolidation
