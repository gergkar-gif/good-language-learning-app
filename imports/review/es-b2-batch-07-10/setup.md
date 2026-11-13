# es B2 batch: es-b2-batch-07-10

Started 2026-11-13T04:50:37Z from origin/master 4c125864. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 7 temporal-clauses-future (b2-07-01 b2-07-02 b2-07-03 b2-07-04 b2-07-05 b2-07-consolidation; stories ['b2-07']); B2 Unit 8 concession-counter-argument (b2-08-01 b2-08-02 b2-08-03 b2-08-04 b2-08-05 b2-08-consolidation; stories ['b2-08'])
- Reader B: B2 Unit 9 conditionals-potential-scenarios (b2-09-01 b2-09-02 b2-09-03 b2-09-04 b2-09-05 b2-09-consolidation; stories ['b2-09']); B2 Unit 10 conditionals-counterfactuals-regrets (b2-10-01 b2-10-02 b2-10-03 b2-10-04 b2-10-05 b2-10-consolidation; stories ['b2-10'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 7 temporal-clauses-future | core | 9 / 17 |
| B2 Unit 8 concession-counter-argument | core | 19 / 22 |
| B2 Unit 9 conditionals-potential-scenarios | core | 10 / 20 |
| B2 Unit 10 conditionals-counterfactuals-regrets | core | 8 / 17 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-07-01 b2-07-02 b2-07-03 b2-07-04 b2-07-05 b2-07-consolidation b2-08-01 b2-08-02 b2-08-03 b2-08-04 b2-08-05 b2-08-consolidation b2-09-01 b2-09-02 b2-09-03 b2-09-04 b2-09-05 b2-09-consolidation b2-10-01 b2-10-02 b2-10-03 b2-10-04 b2-10-05 b2-10-consolidation
