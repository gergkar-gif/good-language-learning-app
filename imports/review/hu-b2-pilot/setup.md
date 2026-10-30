# hu B2 batch: hu-b2-pilot

Started 2026-10-30T01:31:11Z from origin/master 08ad9fa7. 2 Sonnet reader(s).

- Reader A: Unit 1 nuance-focus-emphasis-narrative (b2-01-01 b2-01-02 b2-01-03 b2-01-04 b2-01-05 b2-01-consolidation; stories ['b2-01-pacsirta'])
- Reader B: Unit 3 memory-nostalgia-sensory-description (b2-02-01 b2-02-02 b2-02-03 b2-02-04 b2-02-05 b2-02-consolidation; stories ['b2-02-vorospostakocsi'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 1 nuance-focus-emphasis-narrative | core | 17 / 1 |
| 3 memory-nostalgia-sensory-description | core | 69 / 2 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-01-01 b2-01-02 b2-01-03 b2-01-04 b2-01-05 b2-01-consolidation b2-02-01 b2-02-02 b2-02-03 b2-02-04 b2-02-05 b2-02-consolidation
