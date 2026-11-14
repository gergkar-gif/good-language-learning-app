# hu C1 batch: hu-c1-batch-core-09-16

Started 2026-11-14T07:33:30Z from origin/master 700153c9. 2 Sonnet reader(s).

- Reader A: C1 Unit 9 bioethics (c1-09-01 c1-09-02 c1-09-03 c1-09-04 c1-09-05 c1-09-consolidation; stories ['c1-09-nemeth']); C1 Unit 10 contracts-negotiation (c1-10-01 c1-10-02 c1-10-03 c1-10-04 c1-10-05 c1-10-consolidation; stories ['c1-10-marai']); C1 Unit 11 human-rights-law (c1-11-01 c1-11-02 c1-11-03 c1-11-04 c1-11-05 c1-11-consolidation; stories ['c1-11-bibo']); C1 Unit 12 civic-resistance (c1-12-01 c1-12-02 c1-12-03 c1-12-04 c1-12-05 c1-12-consolidation; stories ['c1-12-konrad'])
- Reader B: C1 Unit 13 macroeconomics (c1-13-01 c1-13-02 c1-13-03 c1-13-04 c1-13-05 c1-13-consolidation; stories ['c1-13-kornai']); C1 Unit 14 energy-transition (c1-14-01 c1-14-02 c1-14-03 c1-14-04 c1-14-05 c1-14-consolidation; stories ['c1-14-fekete']); C1 Unit 15 artificial-intelligence (c1-15-01 c1-15-02 c1-15-03 c1-15-04 c1-15-05 c1-15-consolidation; stories ['c1-15-neumann']); C1 Unit 16 public-sphere (c1-16-01 c1-16-02 c1-16-03 c1-16-04 c1-16-05 c1-16-consolidation; stories ['c1-16-bibo'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Unit 9 bioethics | core | 13 / 13 |
| C1 Unit 10 contracts-negotiation | core | 7 / 8 |
| C1 Unit 11 human-rights-law | core | 9 / 11 |
| C1 Unit 12 civic-resistance | core | 7 / 9 |
| C1 Unit 13 macroeconomics | core | 7 / 7 |
| C1 Unit 14 energy-transition | core | 8 / 7 |
| C1 Unit 15 artificial-intelligence | core | 9 / 11 |
| C1 Unit 16 public-sphere | core | 6 / 14 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-09-01 c1-09-02 c1-09-03 c1-09-04 c1-09-05 c1-09-consolidation c1-10-01 c1-10-02 c1-10-03 c1-10-04 c1-10-05 c1-10-consolidation c1-11-01 c1-11-02 c1-11-03 c1-11-04 c1-11-05 c1-11-consolidation c1-12-01 c1-12-02 c1-12-03 c1-12-04 c1-12-05 c1-12-consolidation c1-13-01 c1-13-02 c1-13-03 c1-13-04 c1-13-05 c1-13-consolidation c1-14-01 c1-14-02 c1-14-03 c1-14-04 c1-14-05 c1-14-consolidation c1-15-01 c1-15-02 c1-15-03 c1-15-04 c1-15-05 c1-15-consolidation c1-16-01 c1-16-02 c1-16-03 c1-16-04 c1-16-05 c1-16-consolidation
