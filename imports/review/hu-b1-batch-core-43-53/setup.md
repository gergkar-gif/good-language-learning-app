# es B1 batch: hu-b1-batch-core-43-53

Started 2026-10-27T22:58:23Z from origin/master 35d6d2cc. 2 Sonnet reader(s).

- Reader A: Unit 43 possibilities-predictions (b1-22-01 b1-22-02 b1-22-03 b1-22-04 b1-22-05 b1-22-consolidation; stories ['b1-22-jokai']); Unit 45 making-decisions (b1-23-01 b1-23-02 b1-23-03 b1-23-04 b1-23-05 b1-23-consolidation; stories ['b1-23-mikszath']); Unit 47 how-things-work (b1-24-01 b1-24-02 b1-24-03 b1-24-04 b1-24-05 b1-24-consolidation; stories ['b1-24-ottlik'])
- Reader B: Unit 49 change-development (b1-25-01 b1-25-02 b1-25-03 b1-25-04 b1-25-05 b1-25-consolidation; stories ['b1-25-moricz']); Unit 51 work-ambition-balance (b1-26-01 b1-26-02 b1-26-03 b1-26-04 b1-26-05 b1-26-consolidation; stories ['b1-26-kosztolanyi']); Unit 53 social-life-communication (b1-27-01 b1-27-02 b1-27-03 b1-27-04 b1-27-05 b1-27-consolidation; stories ['b1-27-molnar'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 43 possibilities-predictions | core | 10 / 2 |
| 45 making-decisions | core | 6 / 2 |
| 47 how-things-work | core | 10 / 0 |
| 49 change-development | core | 12 / 3 |
| 51 work-ambition-balance | core | 12 / 4 |
| 53 social-life-communication | core | 10 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-22-01 b1-22-02 b1-22-03 b1-22-04 b1-22-05 b1-22-consolidation b1-23-01 b1-23-02 b1-23-03 b1-23-04 b1-23-05 b1-23-consolidation b1-24-01 b1-24-02 b1-24-03 b1-24-04 b1-24-05 b1-24-consolidation b1-25-01 b1-25-02 b1-25-03 b1-25-04 b1-25-05 b1-25-consolidation b1-26-01 b1-26-02 b1-26-03 b1-26-04 b1-26-05 b1-26-consolidation b1-27-01 b1-27-02 b1-27-03 b1-27-04 b1-27-05 b1-27-consolidation
