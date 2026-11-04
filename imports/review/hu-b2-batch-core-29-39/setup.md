# hu B2 batch: hu-b2-batch-core-29-39

Started 2026-11-04T04:57:46Z from origin/master bb0c8912. 2 Sonnet reader(s).

- Reader A: Unit 29 censorship-ambiguity-indirect-expression (b2-15-01 b2-15-02 b2-15-03 b2-15-04 b2-15-05 b2-15-consolidation; stories ['b2-15-niki']); Unit 31 ideological-debates-public-polemics (b2-16-01 b2-16-02 b2-16-03 b2-16-04 b2-16-05 b2-16-consolidation; stories ['b2-16-adypublicisztika']); Unit 33 information-overload-rumor-verification (b2-17-01 b2-17-02 b2-17-03 b2-17-04 b2-17-05 b2-17-consolidation; stories ['b2-17-nero'])
- Reader B: Unit 35 rhetoric-framing-mass-persuasion (b2-18-01 b2-18-02 b2-18-03 b2-18-04 b2-18-05 b2-18-consolidation; stories ['b2-18-urimuri']); Unit 37 landscape-belonging-regional-character (b2-19-01 b2-19-02 b2-19-03 b2-19-04 b2-19-05 b2-19-consolidation; stories ['b2-19-pusztaknepe']); Unit 39 social-mobility-class-opportunity (b2-20-01 b2-20-02 b2-20-03 b2-20-04 b2-20-05 b2-20-consolidation; stories ['b2-20-szamadas'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 29 censorship-ambiguity-indirect-expression | core | 21 / 2 |
| 31 ideological-debates-public-polemics | core | 36 / 1 |
| 33 information-overload-rumor-verification | core | 25 / 0 |
| 35 rhetoric-framing-mass-persuasion | core | 12 / 1 |
| 37 landscape-belonging-regional-character | core | 12 / 0 |
| 39 social-mobility-class-opportunity | core | 55 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-15-01 b2-15-02 b2-15-03 b2-15-04 b2-15-05 b2-15-consolidation b2-16-01 b2-16-02 b2-16-03 b2-16-04 b2-16-05 b2-16-consolidation b2-17-01 b2-17-02 b2-17-03 b2-17-04 b2-17-05 b2-17-consolidation b2-18-01 b2-18-02 b2-18-03 b2-18-04 b2-18-05 b2-18-consolidation b2-19-01 b2-19-02 b2-19-03 b2-19-04 b2-19-05 b2-19-consolidation b2-20-01 b2-20-02 b2-20-03 b2-20-04 b2-20-05 b2-20-consolidation
