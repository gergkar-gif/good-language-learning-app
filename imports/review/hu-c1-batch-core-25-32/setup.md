# hu C1 batch: hu-c1-batch-core-25-32

Started 2026-11-14T18:10:06Z from origin/master 9e45d1bc. 2 Sonnet reader(s).

- Reader A: C1 Unit 25 separation-of-powers (c1-25-01 c1-25-02 c1-25-03 c1-25-04 c1-25-05 c1-25-consolidation; stories ['eotvos-uralkodo-eszmek']); C1 Unit 26 press-freedom (c1-26-01 c1-26-02 c1-26-03 c1-26-04 c1-26-05 c1-26-consolidation; stories ['marai-naplo-sajtoszabadsag']); C1 Unit 27 epidemiology (c1-27-01 c1-27-02 c1-27-03 c1-27-04 c1-27-05 c1-27-consolidation; stories ['semmelweis-gyermekagyi-laz']); C1 Unit 28 railway-modernization (c1-28-01 c1-28-02 c1-28-03 c1-28-04 c1-28-05 c1-28-consolidation; stories ['baross-zonatarifa-vasut'])
- Reader B: C1 Unit 29 museums-monuments (c1-29-01 c1-29-02 c1-29-03 c1-29-04 c1-29-05 c1-29-consolidation; stories ['pulszky-nemzeti-muzeum']); C1 Unit 30 east-west-geopolitics (c1-30-01 c1-30-02 c1-30-03 c1-30-04 c1-30-05 c1-30-consolidation; stories ['ady-komp-orszag']); C1 Unit 31 historical-trauma (c1-31-01 c1-31-02 c1-31-03 c1-31-04 c1-31-05 c1-31-consolidation; stories ['bibo-kisallamok-nyomorusage']); C1 Unit 32 fundamental-rights (c1-32-01 c1-32-02 c1-32-03 c1-32-04 c1-32-05 c1-32-consolidation; stories ['solyom-lathatatlan-alkotmany'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Unit 25 separation-of-powers | core | 6 / 11 |
| C1 Unit 26 press-freedom | core | 8 / 14 |
| C1 Unit 27 epidemiology | core | 4 / 14 |
| C1 Unit 28 railway-modernization | core | 6 / 12 |
| C1 Unit 29 museums-monuments | core | 8 / 15 |
| C1 Unit 30 east-west-geopolitics | core | 6 / 14 |
| C1 Unit 31 historical-trauma | core | 8 / 13 |
| C1 Unit 32 fundamental-rights | core | 11 / 7 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-25-01 c1-25-02 c1-25-03 c1-25-04 c1-25-05 c1-25-consolidation c1-26-01 c1-26-02 c1-26-03 c1-26-04 c1-26-05 c1-26-consolidation c1-27-01 c1-27-02 c1-27-03 c1-27-04 c1-27-05 c1-27-consolidation c1-28-01 c1-28-02 c1-28-03 c1-28-04 c1-28-05 c1-28-consolidation c1-29-01 c1-29-02 c1-29-03 c1-29-04 c1-29-05 c1-29-consolidation c1-30-01 c1-30-02 c1-30-03 c1-30-04 c1-30-05 c1-30-consolidation c1-31-01 c1-31-02 c1-31-03 c1-31-04 c1-31-05 c1-31-consolidation c1-32-01 c1-32-02 c1-32-03 c1-32-04 c1-32-05 c1-32-consolidation
