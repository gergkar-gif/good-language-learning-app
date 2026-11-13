# es B2 batch: es-b2-batch-11-14

Started 2026-11-13T09:08:29Z from origin/master b4421967. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 11 mixed-restrictive-conditionals (b2-11-01 b2-11-02 b2-11-03 b2-11-04 b2-11-05 b2-11-consolidation; stories ['b2-11']); B2 Unit 12 purpose-clauses (b2-12-01 b2-12-02 b2-12-03 b2-12-04 b2-12-05 b2-12-consolidation; stories ['b2-12'])
- Reader B: B2 Unit 13 relatives-unknown-antecedents (b2-13-01 b2-13-02 b2-13-03 b2-13-04 b2-13-05 b2-13-consolidation; stories ['b2-13']); B2 Unit 14 universal-indefinite-relatives (b2-14-01 b2-14-02 b2-14-03 b2-14-04 b2-14-05 b2-14-consolidation; stories ['b2-14'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 11 mixed-restrictive-conditionals | core | 9 / 16 |
| B2 Unit 12 purpose-clauses | core | 9 / 23 |
| B2 Unit 13 relatives-unknown-antecedents | core | 8 / 16 |
| B2 Unit 14 universal-indefinite-relatives | core | 10 / 20 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-11-01 b2-11-02 b2-11-03 b2-11-04 b2-11-05 b2-11-consolidation b2-12-01 b2-12-02 b2-12-03 b2-12-04 b2-12-05 b2-12-consolidation b2-13-01 b2-13-02 b2-13-03 b2-13-04 b2-13-05 b2-13-consolidation b2-14-01 b2-14-02 b2-14-03 b2-14-04 b2-14-05 b2-14-consolidation

## Agents (edit-in-place, Sonnet), started 09:08 UTC

- A (Units 11, 12; /home/user/parlour-read-a): agent af0e9e53d15939475
- B (Units 13, 14; /home/user/parlour-read-b): agent a1a6b4c0c9b1f1c53

Resume a stopped agent with SendMessage to its id; never start a new one.
