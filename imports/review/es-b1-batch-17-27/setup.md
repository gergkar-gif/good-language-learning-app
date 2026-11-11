# es B1 batch: es-b1-batch-17-27

Started 2026-11-11T13:05:09Z from origin/master 0cf2f40a. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 17 health-wellbeing (b1-09-01 b1-09-02 b1-09-03 b1-09-04 b1-09-05 b1-09-consolidation; stories ['b1-09']); Unit 19 home-housing (b1-10-01 b1-10-02 b1-10-03 b1-10-04 b1-10-05 b1-10-consolidation; stories ['b1-10']); Unit 21 cities-communities (b1-11-01 b1-11-02 b1-11-03 b1-11-04 b1-11-05 b1-11-consolidation; stories ['b1-11'])
- Reader B: Unit 23 food-lifestyle (b1-12-01 b1-12-02 b1-12-03 b1-12-04 b1-12-05 b1-12-consolidation; stories ['b1-12-picanteria']); Unit 25 media-information (b1-13-01 b1-13-02 b1-13-03 b1-13-04 b1-13-05 b1-13-consolidation; stories ['b1-13-cronicanuevayork']); Unit 27 technology-communication (b1-14-01 b1-14-02 b1-14-03 b1-14-04 b1-14-05 b1-14-consolidation; stories ['b1-14-cartasveruela'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 17 health-wellbeing | 3 / 1 | 3 / 1 |
| 19 home-housing | 11 / 4 | 11 / 10 |
| 21 cities-communities | 5 / 1 | 5 / 15 |
| 23 food-lifestyle | 23 / 1 | 23 / 1 |
| 25 media-information | 16 / 1 | 16 / 1 |
| 27 technology-communication | 24 / 0 | 24 / 0 |

## Files differing es-es vs es-latam

- health-wellbeing: none
- home-housing: none
- cities-communities: none
- food-lifestyle: none
- media-information: none
- technology-communication: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-09-01 b1-09-02 b1-09-03 b1-09-04 b1-09-05 b1-09-consolidation b1-10-01 b1-10-02 b1-10-03 b1-10-04 b1-10-05 b1-10-consolidation b1-11-01 b1-11-02 b1-11-03 b1-11-04 b1-11-05 b1-11-consolidation b1-12-01 b1-12-02 b1-12-03 b1-12-04 b1-12-05 b1-12-consolidation b1-13-01 b1-13-02 b1-13-03 b1-13-04 b1-13-05 b1-13-consolidation b1-14-01 b1-14-02 b1-14-03 b1-14-04 b1-14-05 b1-14-consolidation
