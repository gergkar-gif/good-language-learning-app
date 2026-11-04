# hu B2 batch: hu-b2-batch-core-41-51

Started 2026-11-04T06:05:36Z from origin/master ad74365e. 2 Sonnet reader(s).

- Reader A: Unit 41 economic-cycles-crisis-adaptation (b2-21-01 b2-21-02 b2-21-03 b2-21-04 b2-21-05 b2-21-consolidation; stories ['b2-21-agyertyakcsonkigegnek']); Unit 43 demographics-generations-life-course (b2-22-01 b2-22-02 b2-22-03 b2-22-04 b2-22-05 b2-22-consolidation; stories ['b2-22-azajto']); Unit 45 urban-space-architecture-coexistence (b2-23-01 b2-23-02 b2-23-03 b2-23-04 b2-23-05 b2-23-consolidation; stories ['b2-23-buda'])
- Reader B: Unit 47 ecology-infrastructure-stewardship (b2-24-01 b2-24-02 b2-24-03 b2-24-04 b2-24-05 b2-24-consolidation; stories ['b2-24-tuskevar']); Unit 49 law-justice-constitutional-principles (b2-25-01 b2-25-02 b2-25-03 b2-25-04 b2-25-05 b2-25-consolidation; stories ['b2-25-afalujegyzoje']); Unit 51 pluralism-heritage-minority-perspectives (b2-26-01 b2-26-02 b2-26-03 b2-26-04 b2-26-05 b2-26-consolidation; stories ['b2-26-sorstalansag'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 41 economic-cycles-crisis-adaptation | core | 15 / 1 |
| 43 demographics-generations-life-course | core | 7 / 0 |
| 45 urban-space-architecture-coexistence | core | 23 / 0 |
| 47 ecology-infrastructure-stewardship | core | 21 / 1 |
| 49 law-justice-constitutional-principles | core | 14 / 1 |
| 51 pluralism-heritage-minority-perspectives | core | 12 / 1 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-21-01 b2-21-02 b2-21-03 b2-21-04 b2-21-05 b2-21-consolidation b2-22-01 b2-22-02 b2-22-03 b2-22-04 b2-22-05 b2-22-consolidation b2-23-01 b2-23-02 b2-23-03 b2-23-04 b2-23-05 b2-23-consolidation b2-24-01 b2-24-02 b2-24-03 b2-24-04 b2-24-05 b2-24-consolidation b2-25-01 b2-25-02 b2-25-03 b2-25-04 b2-25-05 b2-25-consolidation b2-26-01 b2-26-02 b2-26-03 b2-26-04 b2-26-05 b2-26-consolidation
