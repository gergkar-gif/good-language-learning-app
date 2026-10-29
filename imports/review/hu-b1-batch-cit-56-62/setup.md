# es B1 batch: hu-b1-batch-cit-56-62

Started 2026-10-29T04:28:46Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 56 modern-democratic-hungary (b1-demokracia-01 b1-demokracia-02 b1-demokracia-03 b1-demokracia-04 b1-demokracia-05 b1-demokracia-consolidation; stories ['b1-demokracia-01-alkotmany', 'b1-demokracia-02-allamszervezet', 'b1-demokracia-03-nato', 'b1-demokracia-04-eu', 'b1-demokracia-05-nemzetpolitika', 'b1-demokracia']); Unit 58 national-symbols (b1-nemzetijelkepek-01 b1-nemzetijelkepek-02 b1-nemzetijelkepek-03 b1-nemzetijelkepek-04 b1-nemzetijelkepek-05 b1-nemzetijelkepek-consolidation; stories ['b1-nemzetijelkepek-01-zaszlo', 'b1-nemzetijelkepek-02-szentkorona', 'b1-nemzetijelkepek-03-cimer', 'b1-nemzetijelkepek-04-himnusz', 'b1-nemzetijelkepek-05-szozat', 'b1-nemzetijelkepek'])
- Reader B: Unit 60 national-holidays-remembrance-days (b1-nemzetiunnepek-01 b1-nemzetiunnepek-02 b1-nemzetiunnepek-03 b1-nemzetiunnepek-04 b1-nemzetiunnepek-05 b1-nemzetiunnepek-consolidation; stories ['b1-nemzetiunnepek-01-marcius15', 'b1-nemzetiunnepek-02-augusztus20', 'b1-nemzetiunnepek-03-oktober23', 'b1-nemzetiunnepek-04-emleknapok', 'b1-nemzetiunnepek-05-aldozatok', 'b1-nemzetiunnepek']); Unit 62 fundamental-law (b1-alaptorveny-01 b1-alaptorveny-02 b1-alaptorveny-03 b1-alaptorveny-04 b1-alaptorveny-05 b1-alaptorveny-consolidation; stories ['b1-alaptorveny-01-szuletese', 'b1-alaptorveny-02-hitvallas', 'b1-alaptorveny-03-jogok', 'b1-alaptorveny-04-allam', 'b1-alaptorveny-05-garanciak', 'b1-alaptorveny'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 56 modern-democratic-hungary | citizenship | 8 / 1 |
| 58 national-symbols | citizenship | 9 / 5 |
| 60 national-holidays-remembrance-days | citizenship | 10 / 15 |
| 62 fundamental-law | citizenship | 8 / 7 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-demokracia-01 b1-demokracia-02 b1-demokracia-03 b1-demokracia-04 b1-demokracia-05 b1-demokracia-consolidation b1-nemzetijelkepek-01 b1-nemzetijelkepek-02 b1-nemzetijelkepek-03 b1-nemzetijelkepek-04 b1-nemzetijelkepek-05 b1-nemzetijelkepek-consolidation b1-nemzetiunnepek-01 b1-nemzetiunnepek-02 b1-nemzetiunnepek-03 b1-nemzetiunnepek-04 b1-nemzetiunnepek-05 b1-nemzetiunnepek-consolidation b1-alaptorveny-01 b1-alaptorveny-02 b1-alaptorveny-03 b1-alaptorveny-04 b1-alaptorveny-05 b1-alaptorveny-consolidation
