# hu B2 batch: hu-b2-batch-cult-50-56

Started 2026-11-10T13:08:08Z from origin/master ca3291c2. 2 Sonnet reader(s).

- Reader A: Unit 50 constitutional-history (b2-alkotmanytortenet-01 b2-alkotmanytortenet-02 b2-alkotmanytortenet-03 b2-alkotmanytortenet-04 b2-alkotmanytortenet-05 b2-alkotmanytortenet-consolidation; stories ['b2-alkotmanytortenet-01-tortenetialkotmany', 'b2-alkotmanytortenet-02-aprilisitorvenyek', 'b2-alkotmanytortenet-03-alkotmanyosforradalom', 'b2-alkotmanytortenet-04-alkotmanybirosag', 'b2-alkotmanytortenet-05-alaptorveny2011']); Unit 52 nationalities (b2-nemzetisegek-01 b2-nemzetisegek-02 b2-nemzetisegek-03 b2-nemzetisegek-04 b2-nemzetisegek-05 b2-nemzetisegek-consolidation; stories ['b2-nemzetisegek-01-nepmozaik', 'b2-nemzetisegek-02-zsidonegyed', 'b2-nemzetisegek-03-romakultura', 'b2-nemzetisegek-04-svabokesszlovakok', 'b2-nemzetisegek-05-nemzetisegionkormanyzat'])
- Reader B: Unit 54 hungarians-carpathian-basin (b2-hatarontul-01 b2-hatarontul-02 b2-hatarontul-03 b2-hatarontul-04 b2-hatarontul-05 b2-hatarontul-consolidation; stories ['b2-hatarontul-01-erdelyszekelyfold', 'b2-hatarontul-02-felvidekvajdasag', 'b2-hatarontul-03-anyanyelviintezmenyek', 'b2-hatarontul-04-kettosallampolgarsag', 'b2-hatarontul-05-hataronatnyuloegyuttmukodes']); Unit 56 emigre-waves (b2-diaszpora-01 b2-diaszpora-02 b2-diaszpora-03 b2-diaszpora-04 b2-diaszpora-05 b2-diaszpora-consolidation; stories ['b2-diaszpora-01-amerikasok', 'b2-diaszpora-02-otvenhatosemigracio', 'b2-diaszpora-03-diaszporaintezmenyek', 'b2-diaszpora-04-uniosmobilitas', 'b2-diaszpora-05-hazaterok'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 50 constitutional-history | culture | 4 / 0 |
| 52 nationalities | culture | 6 / 0 |
| 54 hungarians-carpathian-basin | culture | 2 / 1 |
| 56 emigre-waves | culture | 10 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-alkotmanytortenet-01 b2-alkotmanytortenet-02 b2-alkotmanytortenet-03 b2-alkotmanytortenet-04 b2-alkotmanytortenet-05 b2-alkotmanytortenet-consolidation b2-nemzetisegek-01 b2-nemzetisegek-02 b2-nemzetisegek-03 b2-nemzetisegek-04 b2-nemzetisegek-05 b2-nemzetisegek-consolidation b2-hatarontul-01 b2-hatarontul-02 b2-hatarontul-03 b2-hatarontul-04 b2-hatarontul-05 b2-hatarontul-consolidation b2-diaszpora-01 b2-diaszpora-02 b2-diaszpora-03 b2-diaszpora-04 b2-diaszpora-05 b2-diaszpora-consolidation
