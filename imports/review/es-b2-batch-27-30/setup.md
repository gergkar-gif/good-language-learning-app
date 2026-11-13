# es B2 batch: es-b2-batch-27-30

Started 2026-11-13T21:04:04Z from origin/master e8496461. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 28 discourse-markers-structuring-sequencing (b2-28-01 b2-28-02 b2-28-03 b2-28-04 b2-28-05 b2-28-consolidation; stories ['b2-28']); B2 Unit 29 discourse-markers-reformulation-precision (b2-29-01 b2-29-02 b2-29-03 b2-29-04 b2-29-05 b2-29-consolidation; stories ['b2-29'])
- Reader B: B2 Unit 27 prepositional-regimes-locutions (b2-27-01 b2-27-02 b2-27-03 b2-27-04 b2-27-05 b2-27-consolidation; stories ['b2-27']); B2 Unit 30 discourse-markers-contrast-restriction (b2-30-01 b2-30-02 b2-30-03 b2-30-04 b2-30-05 b2-30-consolidation; stories ['b2-30'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 28 discourse-markers-structuring-sequencing | core | 6 / 18 |
| B2 Unit 29 discourse-markers-reformulation-precision | core | 8 / 21 |
| B2 Unit 27 prepositional-regimes-locutions | core | 1 / 19 |
| B2 Unit 30 discourse-markers-contrast-restriction | core | 8 / 17 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-28-01 b2-28-02 b2-28-03 b2-28-04 b2-28-05 b2-28-consolidation b2-29-01 b2-29-02 b2-29-03 b2-29-04 b2-29-05 b2-29-consolidation b2-27-01 b2-27-02 b2-27-03 b2-27-04 b2-27-05 b2-27-consolidation b2-30-01 b2-30-02 b2-30-03 b2-30-04 b2-30-05 b2-30-consolidation

## Agents (edit-in-place, Sonnet), started 21:04 UTC

- A (Units 28, 29; /home/user/parlour-read-a): agent a037cf9f9d26cf9ce
- B (Units 27, 30; /home/user/parlour-read-b): agent a881fe225e1b87fe4

Resume a stopped agent with SendMessage to its id; never start a new one.
