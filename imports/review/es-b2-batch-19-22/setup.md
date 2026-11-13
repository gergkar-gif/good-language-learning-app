# es B2 batch: es-b2-batch-19-22

Started 2026-11-13T14:15:42Z from origin/master a726b50e. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 19 passive-se (b2-19-01 b2-19-02 b2-19-03 b2-19-04 b2-19-05 b2-19-consolidation; stories ['b2-19']); B2 Unit 21 impersonality-strategic-distance (b2-21-01 b2-21-02 b2-21-03 b2-21-04 b2-21-05 b2-21-consolidation; stories ['b2-21'])
- Reader B: B2 Unit 20 analytical-resultative-passives (b2-20-01 b2-20-02 b2-20-03 b2-20-04 b2-20-05 b2-20-consolidation; stories ['b2-20']); B2 Unit 22 verbs-becoming-transformation (b2-22-01 b2-22-02 b2-22-03 b2-22-04 b2-22-05 b2-22-consolidation; stories ['b2-22'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 19 passive-se | core | 7 / 7 |
| B2 Unit 21 impersonality-strategic-distance | core | 4 / 17 |
| B2 Unit 20 analytical-resultative-passives | core | 10 / 7 |
| B2 Unit 22 verbs-becoming-transformation | core | 1 / 20 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-19-01 b2-19-02 b2-19-03 b2-19-04 b2-19-05 b2-19-consolidation b2-21-01 b2-21-02 b2-21-03 b2-21-04 b2-21-05 b2-21-consolidation b2-20-01 b2-20-02 b2-20-03 b2-20-04 b2-20-05 b2-20-consolidation b2-22-01 b2-22-02 b2-22-03 b2-22-04 b2-22-05 b2-22-consolidation

## Agents (edit-in-place, Sonnet), started 14:15 UTC

- A (Units 19, 21; /home/user/parlour-read-a): agent aea92c99cce0ad488
- B (Units 20, 22; /home/user/parlour-read-b): agent a2b700b4552340639

Resume a stopped agent with SendMessage to its id; never start a new one.
