# es B2 batch: es-b2-batch-31-36

Started 2026-11-13T23:43:10Z from origin/master 3031f4d6. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 31 discourse-markers-consequence-causality (b2-31-01 b2-31-02 b2-31-03 b2-31-04 b2-31-05 b2-31-consolidation; stories ['b2-31']); B2 Unit 32 advanced-concessives (b2-32-01 b2-32-02 b2-32-03 b2-32-04 b2-32-05 b2-32-consolidation; stories ['b2-32']); B2 Unit 33 complex-conditionals (b2-33-01 b2-33-02 b2-33-03 b2-33-04 b2-33-05 b2-33-consolidation; stories ['b2-33'])
- Reader B: B2 Unit 34 dialect-variation-register (b2-34-01 b2-34-02 b2-34-03 b2-34-04 b2-34-05 b2-34-consolidation; stories ['b2-34']); B2 Unit 35 formal-registers (b2-35-01 b2-35-02 b2-35-03 b2-35-04 b2-35-05 b2-35-consolidation; stories ['b2-35']); B2 Unit 36 own-voice-synthesis (b2-36-01 b2-36-02 b2-36-03 b2-36-04 b2-36-05 b2-36-consolidation; stories ['b2-36'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 31 discourse-markers-consequence-causality | core | 8 / 24 |
| B2 Unit 32 advanced-concessives | core | 8 / 29 |
| B2 Unit 33 complex-conditionals | core | 9 / 34 |
| B2 Unit 34 dialect-variation-register | core | 13 / 24 |
| B2 Unit 35 formal-registers | core | 7 / 23 |
| B2 Unit 36 own-voice-synthesis | core | 12 / 38 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-31-01 b2-31-02 b2-31-03 b2-31-04 b2-31-05 b2-31-consolidation b2-32-01 b2-32-02 b2-32-03 b2-32-04 b2-32-05 b2-32-consolidation b2-33-01 b2-33-02 b2-33-03 b2-33-04 b2-33-05 b2-33-consolidation b2-34-01 b2-34-02 b2-34-03 b2-34-04 b2-34-05 b2-34-consolidation b2-35-01 b2-35-02 b2-35-03 b2-35-04 b2-35-05 b2-35-consolidation b2-36-01 b2-36-02 b2-36-03 b2-36-04 b2-36-05 b2-36-consolidation

## Agents (edit-in-place, Sonnet), started 23:46 UTC

- A (Units 31, 32, 33; /home/user/parlour-read-a): agent a60c9e86591805c6d
- B (Units 34, 35, 36; /home/user/parlour-read-b): agent a3dfc0af1bcab4294

Resume a stopped agent with SendMessage to its id; never start a new one.
