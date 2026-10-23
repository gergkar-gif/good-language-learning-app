# es B1 batch: hu-b1-batch-core-19-29

Started 2026-10-23T04:23:57Z from origin/master 0869e9c9. 2 Sonnet reader(s).

- Reader A: Unit 19 home-housing (b1-10-01 b1-10-02 b1-10-03 b1-10-04 b1-10-05 b1-10-consolidation; stories ['b1-10-edesanna']); Unit 21 cities-communities (b1-11-01 b1-11-02 b1-11-03 b1-11-04 b1-11-05 b1-11-consolidation; stories ['b1-11-legyjomindhalalig']); Unit 23 food-lifestyle (b1-12-01 b1-12-02 b1-12-03 b1-12-04 b1-12-05 b1-12-consolidation; stories ['b1-12-szindbad'])
- Reader B: Unit 25 media-information (b1-13-01 b1-13-02 b1-13-03 b1-13-04 b1-13-05 b1-13-consolidation; stories ['b1-13-palutcaifiuk']); Unit 27 technology-communication (b1-14-01 b1-14-02 b1-14-03 b1-14-04 b1-14-05 b1-14-consolidation; stories ['b1-14-karinthy']); Unit 29 culture-entertainment (b1-15-01 b1-15-02 b1-15-03 b1-15-04 b1-15-05 b1-15-consolidation; stories ['b1-15-koszivuemberfiai'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 19 home-housing | core | 21 / 0 |
| 21 cities-communities | core | 16 / 0 |
| 23 food-lifestyle | core | 14 / 1 |
| 25 media-information | core | 8 / 0 |
| 27 technology-communication | core | 10 / 0 |
| 29 culture-entertainment | core | 4 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-10-01 b1-10-02 b1-10-03 b1-10-04 b1-10-05 b1-10-consolidation b1-11-01 b1-11-02 b1-11-03 b1-11-04 b1-11-05 b1-11-consolidation b1-12-01 b1-12-02 b1-12-03 b1-12-04 b1-12-05 b1-12-consolidation b1-13-01 b1-13-02 b1-13-03 b1-13-04 b1-13-05 b1-13-consolidation b1-14-01 b1-14-02 b1-14-03 b1-14-04 b1-14-05 b1-14-consolidation b1-15-01 b1-15-02 b1-15-03 b1-15-04 b1-15-05 b1-15-consolidation
