# es B1 batch: hu-b1-batch-03-06

Started 2026-10-22T14:09:38Z from origin/master 097358be. 2 Sonnet reader(s).

- Reader A: Unit 3 experiences-memories (b1-02-01 b1-02-02 b1-02-03 b1-02-04 b1-02-05 b1-02-consolidation; stories ['b1-02-hetkrajcar']); Unit 4 carpathian-basin-before-magyars (b1-karpatmedence-01 b1-karpatmedence-02 b1-karpatmedence-03 b1-karpatmedence-04 b1-karpatmedence-05 b1-karpatmedence-consolidation; stories ['b1-karpatmedence-01-korainepek', 'b1-karpatmedence-02-pannonia', 'b1-karpatmedence-03-nepvandorlas', 'b1-karpatmedence-04-kikeltekitt', 'b1-karpatmedence-05-honfoglalaselott'])
- Reader B: Unit 5 plans-ambitions (b1-03-01 b1-03-02 b1-03-03 b1-03-04 b1-03-05 b1-03-consolidation; stories ['b1-03-aranyember']); Unit 6 honfoglalas (b1-honfoglalas-01 b1-honfoglalas-02 b1-honfoglalas-03 b1-honfoglalas-04 b1-honfoglalas-05 b1-honfoglalas-consolidation; stories ['b1-honfoglalas-01-nyugatranyomas', 'b1-honfoglalas-02-atkeles', 'b1-honfoglalas-03-arpadeshettorzs', 'b1-honfoglalas-04-birtokbavetel', 'b1-honfoglalas-05-nemzetiemlekezet'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 3 experiences-memories | core | 17 / 5 |
| 4 carpathian-basin-before-magyars | citizenship | 17 / 5 |
| 5 plans-ambitions | core | 16 / 3 |
| 6 honfoglalas | citizenship | 15 / 7 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-02-01 b1-02-02 b1-02-03 b1-02-04 b1-02-05 b1-02-consolidation b1-karpatmedence-01 b1-karpatmedence-02 b1-karpatmedence-03 b1-karpatmedence-04 b1-karpatmedence-05 b1-karpatmedence-consolidation b1-03-01 b1-03-02 b1-03-03 b1-03-04 b1-03-05 b1-03-consolidation b1-honfoglalas-01 b1-honfoglalas-02 b1-honfoglalas-03 b1-honfoglalas-04 b1-honfoglalas-05 b1-honfoglalas-consolidation
