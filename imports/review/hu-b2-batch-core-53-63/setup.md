# hu B2 batch: hu-b2-batch-core-53-63

Started 2026-11-04T10:40:21Z from origin/master 202b0d22. 2 Sonnet reader(s).

- Reader A: Unit 53 borders-kinship-transborder-identity (b2-27-01 b2-27-02 b2-27-03 b2-27-04 b2-27-05 b2-27-consolidation; stories ['b2-27-anyamkonnyualmotiger']); Unit 55 exile-emigration-global-networks (b2-28-01 b2-28-02 b2-28-03 b2-28-04 b2-28-05 b2-28-consolidation; stories ['b2-28-marainaplo']); Unit 57 diplomacy-alliances-sovereignty (b2-29-01 b2-29-02 b2-29-03 b2-29-04 b2-29-05 b2-29-consolidation; stories ['b2-29-banffymiklos'])
- Reader B: Unit 59 civic-participation-advocacy-public (b2-30-01 b2-30-02 b2-30-03 b2-30-04 b2-30-05 b2-30-consolidation; stories ['b2-30-kulonoshazassag']); Unit 61 gastronomy-conviviality-cultural-rituals (b2-31-01 b2-31-02 b2-31-03 b2-31-04 b2-31-05 b2-31-consolidation; stories ['b2-31-szindbad']); Unit 63 competition-mastery-peak-performance (b2-32-01 b2-32-02 b2-32-03 b2-32-04 b2-32-05 b2-32-consolidation; stories ['b2-32-utazasatizenhatos'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 53 borders-kinship-transborder-identity | core | 14 / 0 |
| 55 exile-emigration-global-networks | core | 9 / 0 |
| 57 diplomacy-alliances-sovereignty | core | 8 / 0 |
| 59 civic-participation-advocacy-public | core | 8 / 1 |
| 61 gastronomy-conviviality-cultural-rituals | core | 19 / 1 |
| 63 competition-mastery-peak-performance | core | 9 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-27-01 b2-27-02 b2-27-03 b2-27-04 b2-27-05 b2-27-consolidation b2-28-01 b2-28-02 b2-28-03 b2-28-04 b2-28-05 b2-28-consolidation b2-29-01 b2-29-02 b2-29-03 b2-29-04 b2-29-05 b2-29-consolidation b2-30-01 b2-30-02 b2-30-03 b2-30-04 b2-30-05 b2-30-consolidation b2-31-01 b2-31-02 b2-31-03 b2-31-04 b2-31-05 b2-31-consolidation b2-32-01 b2-32-02 b2-32-03 b2-32-04 b2-32-05 b2-32-consolidation
