# es B1 batch: hu-b1-batch-core-07-17

Started 2026-10-22T15:02:17Z from origin/master cef72806. 2 Sonnet reader(s).

- Reader A: Unit 7 giving-advice (b1-04-01 b1-04-02 b1-04-03 b1-04-04 b1-04-05 b1-04-consolidation; stories ['b1-04-bedeanna']); Unit 9 relationships (b1-05-01 b1-05-02 b1-05-03 b1-05-04 b1-05-05 b1-05-consolidation; stories ['b1-05-legyjomindhalalig']); Unit 11 work-professional-life (b1-06-01 b1-06-02 b1-06-03 b1-06-04 b1-06-05 b1-06-consolidation; stories ['b1-06-rokonok'])
- Reader B: Unit 13 education-learning (b1-07-01 b1-07-02 b1-07-03 b1-07-04 b1-07-05 b1-07-consolidation; stories ['b1-07-tanarurkerem']); Unit 15 travel-mobility (b1-08-01 b1-08-02 b1-08-03 b1-08-04 b1-08-05 b1-08-consolidation; stories ['b1-08-szentpeter']); Unit 17 health-wellbeing (b1-09-01 b1-09-02 b1-09-03 b1-09-04 b1-09-05 b1-09-consolidation; stories ['b1-09-estikornel'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 7 giving-advice | core | 14 / 6 |
| 9 relationships | core | 17 / 1 |
| 11 work-professional-life | core | 3 / 0 |
| 13 education-learning | core | 21 / 0 |
| 15 travel-mobility | core | 16 / 0 |
| 17 health-wellbeing | core | 26 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-04-01 b1-04-02 b1-04-03 b1-04-04 b1-04-05 b1-04-consolidation b1-05-01 b1-05-02 b1-05-03 b1-05-04 b1-05-05 b1-05-consolidation b1-06-01 b1-06-02 b1-06-03 b1-06-04 b1-06-05 b1-06-consolidation b1-07-01 b1-07-02 b1-07-03 b1-07-04 b1-07-05 b1-07-consolidation b1-08-01 b1-08-02 b1-08-03 b1-08-04 b1-08-05 b1-08-consolidation b1-09-01 b1-09-02 b1-09-03 b1-09-04 b1-09-05 b1-09-consolidation
