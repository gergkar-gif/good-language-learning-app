# es B1 batch: es-b1-batch-29-39

Started 2026-11-11T19:20:30Z from origin/master e01d06ad. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 29 culture-entertainment (b1-15-01 b1-15-02 b1-15-03 b1-15-04 b1-15-05 b1-15-consolidation; stories ['b1-15-clarinteatro']); Unit 31 environment (b1-16-01 b1-16-02 b1-16-03 b1-16-04 b1-16-05 b1-16-consolidation; stories ['b1-16-cuentosdelaselva']); Unit 33 society-inequality (b1-17-01 b1-17-02 b1-17-03 b1-17-04 b1-17-05 b1-17-consolidation; stories ['b1-17-fortunatayjacinta'])
- Reader B: Unit 35 politics-public-life (b1-18-01 b1-18-02 b1-18-03 b1-18-04 b1-18-05 b1-18-consolidation; stories ['b1-18-facundo']); Unit 37 money-economy (b1-19-01 b1-19-02 b1-19-03 b1-19-04 b1-19-05 b1-19-consolidation; stories ['b1-19-tradicionesperuanas']); Unit 39 problems-solutions (b1-20-01 b1-20-02 b1-20-03 b1-20-04 b1-20-05 b1-20-consolidation; stories ['b1-20-laislavirgen'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 29 culture-entertainment | 12 / 1 | 12 / 2 |
| 31 environment | 20 / 3 | 20 / 3 |
| 33 society-inequality | 16 / 0 | 16 / 0 |
| 35 politics-public-life | 17 / 0 | 17 / 0 |
| 37 money-economy | 13 / 2 | 13 / 3 |
| 39 problems-solutions | 21 / 2 | 21 / 2 |

## Files differing es-es vs es-latam

- culture-entertainment: none
- environment: b1-16-consolidation-ex.json
- society-inequality: none
- politics-public-life: none
- money-economy: none
- problems-solutions: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-15-01 b1-15-02 b1-15-03 b1-15-04 b1-15-05 b1-15-consolidation b1-16-01 b1-16-02 b1-16-03 b1-16-04 b1-16-05 b1-16-consolidation b1-17-01 b1-17-02 b1-17-03 b1-17-04 b1-17-05 b1-17-consolidation b1-18-01 b1-18-02 b1-18-03 b1-18-04 b1-18-05 b1-18-consolidation b1-19-01 b1-19-02 b1-19-03 b1-19-04 b1-19-05 b1-19-consolidation b1-20-01 b1-20-02 b1-20-03 b1-20-04 b1-20-05 b1-20-consolidation
