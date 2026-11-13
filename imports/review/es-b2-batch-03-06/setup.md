# es B2 batch: es-b2-batch-03-06

Started 2026-11-13T04:25:33Z from origin/master 0696d9d2. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: Unit 5 hypothesizing-probability (b2-03-01 b2-03-02 b2-03-03 b2-03-04 b2-03-05 b2-03-consolidation; stories ['b2-03']); Unit 9 doubt-denial-epistemic-stance (b2-05-01 b2-05-02 b2-05-03 b2-05-04 b2-05-05 b2-05-consolidation; stories ['b2-05'])
- Reader B: Unit 7 influence-will-value-judgments (b2-04-01 b2-04-02 b2-04-03 b2-04-04 b2-04-05 b2-04-consolidation; stories ['b2-04']); Unit 11 emotional-reactions-affective-stance (b2-06-01 b2-06-02 b2-06-03 b2-06-04 b2-06-05 b2-06-consolidation; stories ['b2-06'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 5 hypothesizing-probability | core | 6 / 18 |
| 9 doubt-denial-epistemic-stance | core | 10 / 18 |
| 7 influence-will-value-judgments | core | 3 / 11 |
| 11 emotional-reactions-affective-stance | core | 8 / 17 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-03-01 b2-03-02 b2-03-03 b2-03-04 b2-03-05 b2-03-consolidation b2-05-01 b2-05-02 b2-05-03 b2-05-04 b2-05-05 b2-05-consolidation b2-04-01 b2-04-02 b2-04-03 b2-04-04 b2-04-05 b2-04-consolidation b2-06-01 b2-06-02 b2-06-03 b2-06-04 b2-06-05 b2-06-consolidation

Unit numbers above are table positions (batch_setup.py before its fix): app Units 3, 5 (A) and 4, 6 (B).

## Agents (edit-in-place, Sonnet), started 04:26 UTC

- A (Units 3 hypothesizing-probability, 5 doubt-denial-epistemic-stance; /home/user/parlour-read-a): agent ae5d07a3c0235125b
- B (Units 4 influence-will-value-judgments, 6 emotional-reactions-affective-stance; /home/user/parlour-read-b): agent a3095dd2de18ee507

Resume a stopped agent with SendMessage to its id; never start a new one.
