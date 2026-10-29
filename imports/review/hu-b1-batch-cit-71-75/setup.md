# es B1 batch: hu-b1-batch-cit-71-75

Started 2026-10-29T13:47:55Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 71 hungarians-abroad (b1-magyarsag-01 b1-magyarsag-02 b1-magyarsag-03 b1-magyarsag-04 b1-magyarsag-05 b1-magyarsag-consolidation; stories ['b1-magyarsag-01-hatarontul', 'b1-magyarsag-02-regiok', 'b1-magyarsag-03-diaszpora', 'b1-magyarsag-04-eu', 'b1-magyarsag-05-honositas', 'b1-magyarsag']); Unit 73 being-hungarian-citizen (b1-allampolgarsag-01 b1-allampolgarsag-02 b1-allampolgarsag-03 b1-allampolgarsag-04 b1-allampolgarsag-05 b1-allampolgarsag-consolidation; stories ['b1-allampolgarsag-01-megszerzese', 'b1-allampolgarsag-02-jogok', 'b1-allampolgarsag-03-kotelessegek', 'b1-allampolgarsag-04-esku', 'b1-allampolgarsag-05-vizsga', 'b1-allampolgarsag'])
- Reader B: Unit 74 kormanyablak (b1-kormanyablak-01 b1-kormanyablak-02 b1-kormanyablak-03 b1-kormanyablak-04 b1-kormanyablak-05 b1-kormanyablak-consolidation; stories ['b1-kormanyablak']); Unit 75 tenancy-contracts (b1-alberlet-01 b1-alberlet-02 b1-alberlet-03 b1-alberlet-04 b1-alberlet-05 b1-alberlet-consolidation; stories ['b1-alberlet'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 71 hungarians-abroad | citizenship | 8 / 5 |
| 73 being-hungarian-citizen | citizenship | 10 / 8 |
| 74 kormanyablak | citizenship | 6 / 8 |
| 75 tenancy-contracts | citizenship | 9 / 5 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-magyarsag-01 b1-magyarsag-02 b1-magyarsag-03 b1-magyarsag-04 b1-magyarsag-05 b1-magyarsag-consolidation b1-allampolgarsag-01 b1-allampolgarsag-02 b1-allampolgarsag-03 b1-allampolgarsag-04 b1-allampolgarsag-05 b1-allampolgarsag-consolidation b1-kormanyablak-01 b1-kormanyablak-02 b1-kormanyablak-03 b1-kormanyablak-04 b1-kormanyablak-05 b1-kormanyablak-consolidation b1-alberlet-01 b1-alberlet-02 b1-alberlet-03 b1-alberlet-04 b1-alberlet-05 b1-alberlet-consolidation
