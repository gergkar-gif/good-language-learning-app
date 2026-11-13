# es B2 batch: es-b2-pilot

Started 2026-11-13T03:46:43Z from origin/master fc33b25f. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: Unit 1 nuance-precision-emphasis (b2-01-01 b2-01-02 b2-01-03 b2-01-04 b2-01-05 b2-01-consolidation; stories ['b2-01'])
- Reader B: Unit 3 narrative-time-aspect (b2-02-01 b2-02-02 b2-02-03 b2-02-04 b2-02-05 b2-02-consolidation; stories ['b2-02'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 1 nuance-precision-emphasis | core | 12 / 11 |
| 3 narrative-time-aspect | core | 5 / 17 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-01-01 b2-01-02 b2-01-03 b2-01-04 b2-01-05 b2-01-consolidation b2-02-01 b2-02-02 b2-02-03 b2-02-04 b2-02-05 b2-02-consolidation
