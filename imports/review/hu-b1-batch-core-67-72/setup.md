# es B1 batch: hu-b1-batch-core-67-72

Started 2026-10-28T04:47:06Z from origin/master d934fb90. 2 Sonnet reader(s).

- Reader A: Unit 67 complex-opinions (b1-34-01 b1-34-02 b1-34-03 b1-34-04 b1-34-05 b1-34-consolidation; stories ['b1-34-babits']); Unit 70 hypotheticals-possibilities (b1-35-01 b1-35-02 b1-35-03 b1-35-04 b1-35-05 b1-35-consolidation; stories ['b1-35-szerb'])
- Reader B: Unit 72 independent-hungarian (b1-36-01 b1-36-02 b1-36-03 b1-36-04 b1-36-05 b1-36-consolidation; stories ['b1-36-gardonyi'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 67 complex-opinions | core | 8 / 4 |
| 70 hypotheticals-possibilities | core | 7 / 4 |
| 72 independent-hungarian | core | 11 / 5 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-34-01 b1-34-02 b1-34-03 b1-34-04 b1-34-05 b1-34-consolidation b1-35-01 b1-35-02 b1-35-03 b1-35-04 b1-35-05 b1-35-consolidation b1-36-01 b1-36-02 b1-36-03 b1-36-04 b1-36-05 b1-36-consolidation
