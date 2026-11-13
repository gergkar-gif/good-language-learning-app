# es B2 batch: es-b2-batch-23-26

Started 2026-11-13T14:38:14Z from origin/master ff925927. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 23 inceptive-iterative-periphrases (b2-23-01 b2-23-02 b2-23-03 b2-23-04 b2-23-05 b2-23-consolidation; stories ['b2-23']); B2 Unit 25 terminative-resultative-periphrases (b2-25-01 b2-25-02 b2-25-03 b2-25-04 b2-25-05 b2-25-consolidation; stories ['b2-25'])
- Reader B: B2 Unit 24 durative-progressive-periphrases (b2-24-01 b2-24-02 b2-24-03 b2-24-04 b2-24-05 b2-24-consolidation; stories ['b2-24']); B2 Unit 26 modal-periphrases-conjecture-duty (b2-26-01 b2-26-02 b2-26-03 b2-26-04 b2-26-05 b2-26-consolidation; stories ['b2-26'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 23 inceptive-iterative-periphrases | core | 0 / 24 |
| B2 Unit 25 terminative-resultative-periphrases | core | 10 / 23 |
| B2 Unit 24 durative-progressive-periphrases | core | 0 / 15 |
| B2 Unit 26 modal-periphrases-conjecture-duty | core | 6 / 25 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-23-01 b2-23-02 b2-23-03 b2-23-04 b2-23-05 b2-23-consolidation b2-25-01 b2-25-02 b2-25-03 b2-25-04 b2-25-05 b2-25-consolidation b2-24-01 b2-24-02 b2-24-03 b2-24-04 b2-24-05 b2-24-consolidation b2-26-01 b2-26-02 b2-26-03 b2-26-04 b2-26-05 b2-26-consolidation
