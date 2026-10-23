# es B1 batch: hu-b1-batch-core-31-41

Started 2026-10-23T05:13:47Z from origin/master 7fe56776. 2 Sonnet reader(s).

- Reader A: Unit 31 environment (b1-16-01 b1-16-02 b1-16-03 b1-16-04 b1-16-05 b1-16-consolidation; stories ['b1-16-gardonyi']); Unit 33 society-inequality (b1-17-01 b1-17-02 b1-17-03 b1-17-04 b1-17-05 b1-17-consolidation; stories ['b1-17-moricz']); Unit 35 politics-public-life (b1-18-01 b1-18-02 b1-18-03 b1-18-04 b1-18-05 b1-18-consolidation; stories ['b1-18-mikszath'])
- Reader B: Unit 37 money-economy (b1-19-01 b1-19-02 b1-19-03 b1-19-04 b1-19-05 b1-19-consolidation; stories ['b1-19-mikszath']); Unit 39 problems-solutions (b1-20-01 b1-20-02 b1-20-03 b1-20-04 b1-20-05 b1-20-consolidation; stories ['b1-20-karinthy']); Unit 41 opinions-arguments (b1-21-01 b1-21-02 b1-21-03 b1-21-04 b1-21-05 b1-21-consolidation; stories ['b1-21-karinthy'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 31 environment | core | 20 / 0 |
| 33 society-inequality | core | 22 / 0 |
| 35 politics-public-life | core | 26 / 1 |
| 37 money-economy | core | 26 / 0 |
| 39 problems-solutions | core | 26 / 5 |
| 41 opinions-arguments | core | 23 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-16-01 b1-16-02 b1-16-03 b1-16-04 b1-16-05 b1-16-consolidation b1-17-01 b1-17-02 b1-17-03 b1-17-04 b1-17-05 b1-17-consolidation b1-18-01 b1-18-02 b1-18-03 b1-18-04 b1-18-05 b1-18-consolidation b1-19-01 b1-19-02 b1-19-03 b1-19-04 b1-19-05 b1-19-consolidation b1-20-01 b1-20-02 b1-20-03 b1-20-04 b1-20-05 b1-20-consolidation b1-21-01 b1-21-02 b1-21-03 b1-21-04 b1-21-05 b1-21-consolidation
