# es B1 batch: es-b1-batch-41-51

Started 2026-11-12T01:11:24Z from origin/master 3726d8c8. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 41 opinions-arguments (b1-21-01 b1-21-02 b1-21-03 b1-21-04 b1-21-05 b1-21-consolidation; stories ['b1-21-paliques']); Unit 43 possibilities-predictions (b1-22-01 b1-22-02 b1-22-03 b1-22-04 b1-22-05 b1-22-consolidation; stories ['b1-22-elpajaroazul']); Unit 45 making-decisions (b1-23-01 b1-23-02 b1-23-03 b1-23-04 b1-23-05 b1-23-consolidation; stories ['b1-23-pepitajimenez'])
- Reader B: Unit 47 how-things-work (b1-24-01 b1-24-02 b1-24-03 b1-24-04 b1-24-05 b1-24-consolidation; stories ['b1-24-lacamisa']); Unit 49 change-development (b1-25-01 b1-25-02 b1-25-03 b1-25-04 b1-25-05 b1-25-consolidation; stories ['b1-25-trafalgar']); Unit 51 work-ambition-balance (b1-26-01 b1-26-02 b1-26-03 b1-26-04 b1-26-05 b1-26-consolidation; stories ['b1-26-marianela'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 41 opinions-arguments | 30 / 4 | 30 / 4 |
| 43 possibilities-predictions | 21 / 2 | 21 / 2 |
| 45 making-decisions | 24 / 1 | 24 / 1 |
| 47 how-things-work | 12 / 4 | 12 / 4 |
| 49 change-development | 23 / 0 | 23 / 0 |
| 51 work-ambition-balance | 14 / 1 | 14 / 1 |

## Files differing es-es vs es-latam

- opinions-arguments: none
- possibilities-predictions: none
- making-decisions: none
- how-things-work: none
- change-development: none
- work-ambition-balance: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-21-01 b1-21-02 b1-21-03 b1-21-04 b1-21-05 b1-21-consolidation b1-22-01 b1-22-02 b1-22-03 b1-22-04 b1-22-05 b1-22-consolidation b1-23-01 b1-23-02 b1-23-03 b1-23-04 b1-23-05 b1-23-consolidation b1-24-01 b1-24-02 b1-24-03 b1-24-04 b1-24-05 b1-24-consolidation b1-25-01 b1-25-02 b1-25-03 b1-25-04 b1-25-05 b1-25-consolidation b1-26-01 b1-26-02 b1-26-03 b1-26-04 b1-26-05 b1-26-consolidation
