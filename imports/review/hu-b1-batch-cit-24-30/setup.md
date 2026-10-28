# es B1 batch: hu-b1-batch-cit-24-30

Started 2026-10-28T12:04:27Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 24 driving-out-ottomans (b1-torokkiuzese-01 b1-torokkiuzese-02 b1-torokkiuzese-03 b1-torokkiuzese-04 b1-torokkiuzese-05 b1-torokkiuzese-consolidation; stories ['b1-torokkiuzese-01-ostrom', 'b1-torokkiuzese-02-karloca', 'b1-torokkiuzese-03-ara', 'b1-torokkiuzese-04-serelmek', 'b1-torokkiuzese-05-szabadsagharc']); Unit 26 rakoczi-war (b1-rakoczi-01 b1-rakoczi-02 b1-rakoczi-03 b1-rakoczi-04 b1-rakoczi-05 b1-rakoczi-consolidation; stories ['b1-rakoczi-01-vezerlo', 'b1-rakoczi-02-kurucok', 'b1-rakoczi-03-onod', 'b1-rakoczi-04-szatmar', 'b1-rakoczi-05-emlekezet', 'b1-rakoczi'])
- Reader B: Unit 28 18th-century-rebuilding (b1-mariaterezia-01 b1-mariaterezia-02 b1-mariaterezia-03 b1-mariaterezia-04 b1-mariaterezia-05 b1-mariaterezia-consolidation; stories ['b1-mariaterezia-01-telepesek', 'b1-mariaterezia-02-uralkodono', 'b1-mariaterezia-03-reformok', 'b1-mariaterezia-04-kalaposkiraly', 'b1-mariaterezia-05-ebredes', 'b1-mariaterezia']); Unit 30 reform-age (b1-reformkor-01 b1-reformkor-02 b1-reformkor-03 b1-reformkor-04 b1-reformkor-05 b1-reformkor-consolidation; stories ['b1-reformkor-01-szechenyi', 'b1-reformkor-02-lanchid', 'b1-reformkor-03-kossuth', 'b1-reformkor-04-nyelv', 'b1-reformkor-05-forradalom', 'b1-reformkor'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 24 driving-out-ottomans | citizenship | 25 / 1 |
| 26 rakoczi-war | citizenship | 13 / 0 |
| 28 18th-century-rebuilding | citizenship | 11 / 0 |
| 30 reform-age | citizenship | 10 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-torokkiuzese-01 b1-torokkiuzese-02 b1-torokkiuzese-03 b1-torokkiuzese-04 b1-torokkiuzese-05 b1-torokkiuzese-consolidation b1-rakoczi-01 b1-rakoczi-02 b1-rakoczi-03 b1-rakoczi-04 b1-rakoczi-05 b1-rakoczi-consolidation b1-mariaterezia-01 b1-mariaterezia-02 b1-mariaterezia-03 b1-mariaterezia-04 b1-mariaterezia-05 b1-mariaterezia-consolidation b1-reformkor-01 b1-reformkor-02 b1-reformkor-03 b1-reformkor-04 b1-reformkor-05 b1-reformkor-consolidation
