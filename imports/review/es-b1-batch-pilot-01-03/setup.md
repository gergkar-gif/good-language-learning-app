# es B1 batch: es-b1-batch-pilot-01-03

Started 2026-11-11T03:23:11Z from origin/master fd4a1728. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 1 telling-stories (b1-01-01 b1-01-02 b1-01-03 b1-01-04 b1-01-05 b1-01-consolidation; stories ['b1-01'])
- Reader B: Unit 3 experiences-memories (b1-02-01 b1-02-02 b1-02-03 b1-02-04 b1-02-05 b1-02-consolidation; stories ['b1-02'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 1 telling-stories | 17 / 4 | 21 / 4 |
| 3 experiences-memories | 13 / 2 | 16 / 2 |

## Files differing es-es vs es-latam

- telling-stories: none
- experiences-memories: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-01-01 b1-01-02 b1-01-03 b1-01-04 b1-01-05 b1-01-consolidation b1-02-01 b1-02-02 b1-02-03 b1-02-04 b1-02-05 b1-02-consolidation
