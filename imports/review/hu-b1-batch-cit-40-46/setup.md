# es B1 batch: hu-b1-batch-cit-40-46

Started 2026-10-28T23:35:17Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 40 world-war-1 (b1-vilaghaboru-01 b1-vilaghaboru-02 b1-vilaghaboru-03 b1-vilaghaboru-04 b1-vilaghaboru-05 b1-vilaghaboru-consolidation; stories ['b1-vilaghaboru-01-hadbaindulas', 'b1-vilaghaboru-02-hatorszag', 'b1-vilaghaboru-03-doberdo', 'b1-vilaghaboru-04-oszirozsa', 'b1-vilaghaboru-05-osszeomlas', 'b1-vilaghaboru']); Unit 42 trianon-1920 (b1-trianon-01 b1-trianon-02 b1-trianon-03 b1-trianon-04 b1-trianon-05 b1-trianon-consolidation; stories ['b1-trianon-01-apponyi', 'b1-trianon-02-alairas', 'b1-trianon-03-kisebbseg', 'b1-trianon-04-trauma', 'b1-trianon-05-osszetartozas', 'b1-trianon'])
- Reader B: Unit 44 interwar-years (b1-horthykorszak-01 b1-horthykorszak-02 b1-horthykorszak-03 b1-horthykorszak-04 b1-horthykorszak-05 b1-horthykorszak-consolidation; stories ['b1-horthykorszak-01-kormanyzo', 'b1-horthykorszak-02-bethlen', 'b1-horthykorszak-03-klebelsberg', 'b1-horthykorszak-04-tarsadalom', 'b1-horthykorszak-05-revizio', 'b1-horthykorszak']); Unit 46 world-war-2 (b1-masodikvh-01 b1-masodikvh-02 b1-masodikvh-03 b1-masodikvh-04 b1-masodikvh-05 b1-masodikvh-consolidation; stories ['b1-masodikvh-01-hadbalepes', 'b1-masodikvh-02-doni', 'b1-masodikvh-03-megszallas', 'b1-masodikvh-04-nyilas', 'b1-masodikvh-05-ostrom', 'b1-masodikvh'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 40 world-war-1 | citizenship | 7 / 10 |
| 42 trianon-1920 | citizenship | 8 / 4 |
| 44 interwar-years | citizenship | 11 / 7 |
| 46 world-war-2 | citizenship | 13 / 6 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-vilaghaboru-01 b1-vilaghaboru-02 b1-vilaghaboru-03 b1-vilaghaboru-04 b1-vilaghaboru-05 b1-vilaghaboru-consolidation b1-trianon-01 b1-trianon-02 b1-trianon-03 b1-trianon-04 b1-trianon-05 b1-trianon-consolidation b1-horthykorszak-01 b1-horthykorszak-02 b1-horthykorszak-03 b1-horthykorszak-04 b1-horthykorszak-05 b1-horthykorszak-consolidation b1-masodikvh-01 b1-masodikvh-02 b1-masodikvh-03 b1-masodikvh-04 b1-masodikvh-05 b1-masodikvh-consolidation
