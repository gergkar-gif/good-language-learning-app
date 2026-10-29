# es B1 batch: hu-b1-batch-cit-48-54

Started 2026-10-29T03:57:48Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 48 rakosi-era (b1-rakosikorszak-01 b1-rakosikorszak-02 b1-rakosikorszak-03 b1-rakosikorszak-04 b1-rakosikorszak-05 b1-rakosikorszak-consolidation; stories ['b1-rakosikorszak-01-szalami', 'b1-rakosikorszak-02-szemelyikultusz', 'b1-rakosikorszak-03-avh', 'b1-rakosikorszak-04-koncepcio', 'b1-rakosikorszak-05-kulak', 'b1-rakosikorszak']); Unit 50 revolution-1956 (b1-otvenhat-01 b1-otvenhat-02 b1-otvenhat-03 b1-otvenhat-04 b1-otvenhat-05 b1-otvenhat-consolidation; stories ['b1-otvenhat-01-kitores', 'b1-otvenhat-02-pestisracok', 'b1-otvenhat-03-gyozelem', 'b1-otvenhat-04-invazio', 'b1-otvenhat-05-megtorlas', 'b1-otvenhat'])
- Reader B: Unit 52 kadar-era (b1-kadarkorszak-01 b1-kadarkorszak-02 b1-kadarkorszak-03 b1-kadarkorszak-04 b1-kadarkorszak-05 b1-kadarkorszak-consolidation; stories ['b1-kadarkorszak-01-megtorlas', 'b1-kadarkorszak-02-mechanizmus', 'b1-kadarkorszak-03-gulyas', 'b1-kadarkorszak-04-haromt', 'b1-kadarkorszak-05-eladosodas', 'b1-kadarkorszak']); Unit 54 regime-change (b1-rendszervaltas-01 b1-rendszervaltas-02 b1-rendszervaltas-03 b1-rendszervaltas-04 b1-rendszervaltas-05 b1-rendszervaltas-consolidation; stories ['b1-rendszervaltas-01-kerekasztal', 'b1-rendszervaltas-02-hatarnyitas', 'b1-rendszervaltas-03-ujratemetes', 'b1-rendszervaltas-04-kikialtas', 'b1-rendszervaltas-05-valasztasok', 'b1-rendszervaltas'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 48 rakosi-era | citizenship | 14 / 3 |
| 50 revolution-1956 | citizenship | 12 / 7 |
| 52 kadar-era | citizenship | 12 / 6 |
| 54 regime-change | citizenship | 12 / 6 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-rakosikorszak-01 b1-rakosikorszak-02 b1-rakosikorszak-03 b1-rakosikorszak-04 b1-rakosikorszak-05 b1-rakosikorszak-consolidation b1-otvenhat-01 b1-otvenhat-02 b1-otvenhat-03 b1-otvenhat-04 b1-otvenhat-05 b1-otvenhat-consolidation b1-kadarkorszak-01 b1-kadarkorszak-02 b1-kadarkorszak-03 b1-kadarkorszak-04 b1-kadarkorszak-05 b1-kadarkorszak-consolidation b1-rendszervaltas-01 b1-rendszervaltas-02 b1-rendszervaltas-03 b1-rendszervaltas-04 b1-rendszervaltas-05 b1-rendszervaltas-consolidation
