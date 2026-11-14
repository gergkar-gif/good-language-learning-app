# hu C1 batch: hu-c1-batch-core-17-24

Started 2026-11-14T08:16:16Z from origin/master db565bc2. 2 Sonnet reader(s).

- Reader A: C1 Unit 17 regional-geopolitics (c1-17-01 c1-17-02 c1-17-03 c1-17-04 c1-17-05 c1-17-consolidation; stories ['c1-17-szucs']); C1 Unit 18 digital-sovereignty (c1-18-01 c1-18-02 c1-18-03 c1-18-04 c1-18-05 c1-18-consolidation; stories ['c1-18-kalmar']); C1 Unit 19 social-stratification (c1-19-01 c1-19-02 c1-19-03 c1-19-04 c1-19-05 c1-19-consolidation; stories ['c1-19-erdei']); C1 Unit 20 drying-alfold (c1-20-01 c1-20-02 c1-20-03 c1-20-04 c1-20-05 c1-20-consolidation; stories ['c1-20-kaan'])
- Reader B: C1 Unit 21 labour-economics (c1-21-01 c1-21-02 c1-21-03 c1-21-04 c1-21-05 c1-21-consolidation; stories ['c1-21-nagylajos']); C1 Unit 22 computational-linguistics (c1-22-01 c1-22-02 c1-22-03 c1-22-04 c1-22-05 c1-22-consolidation; stories ['c1-22-karinthy']); C1 Unit 23 urban-preservation (c1-23-01 c1-23-02 c1-23-03 c1-23-04 c1-23-05 c1-23-consolidation; stories ['c1-23-szerbantal']); C1 Unit 24 academic-autonomy (c1-24-01 c1-24-02 c1-24-03 c1-24-04 c1-24-05 c1-24-consolidation; stories ['c1-24-szentgyorgyi'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Unit 17 regional-geopolitics | core | 10 / 10 |
| C1 Unit 18 digital-sovereignty | core | 6 / 8 |
| C1 Unit 19 social-stratification | core | 3 / 10 |
| C1 Unit 20 drying-alfold | core | 9 / 18 |
| C1 Unit 21 labour-economics | core | 13 / 18 |
| C1 Unit 22 computational-linguistics | core | 11 / 17 |
| C1 Unit 23 urban-preservation | core | 5 / 17 |
| C1 Unit 24 academic-autonomy | core | 8 / 17 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-17-01 c1-17-02 c1-17-03 c1-17-04 c1-17-05 c1-17-consolidation c1-18-01 c1-18-02 c1-18-03 c1-18-04 c1-18-05 c1-18-consolidation c1-19-01 c1-19-02 c1-19-03 c1-19-04 c1-19-05 c1-19-consolidation c1-20-01 c1-20-02 c1-20-03 c1-20-04 c1-20-05 c1-20-consolidation c1-21-01 c1-21-02 c1-21-03 c1-21-04 c1-21-05 c1-21-consolidation c1-22-01 c1-22-02 c1-22-03 c1-22-04 c1-22-05 c1-22-consolidation c1-23-01 c1-23-02 c1-23-03 c1-23-04 c1-23-05 c1-23-consolidation c1-24-01 c1-24-02 c1-24-03 c1-24-04 c1-24-05 c1-24-consolidation
