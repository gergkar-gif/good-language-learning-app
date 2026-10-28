# es B1 batch: hu-b1-batch-cit-32-38

Started 2026-10-28T22:58:28Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 32 revolution-1848 (b1-forradalom-01 b1-forradalom-02 b1-forradalom-03 b1-forradalom-04 b1-forradalom-05 b1-forradalom-consolidation; stories ['b1-forradalom-01-marcius15', 'b1-forradalom-02-tizenketpont', 'b1-forradalom-03-fuggetlenseg', 'b1-forradalom-04-szabadsagharc', 'b1-forradalom-05-vilagos', 'b1-forradalom']); Unit 34 kossuth-petofi-national-cause (b1-nemzetiugy-01 b1-nemzetiugy-02 b1-nemzetiugy-03 b1-nemzetiugy-04 b1-nemzetiugy-05 b1-nemzetiugy-consolidation; stories ['b1-nemzetiugy-01-kossuthemigracio', 'b1-nemzetiugy-02-petofikolto', 'b1-nemzetiugy-03-nemzetidal', 'b1-nemzetiugy-04-kokarda', 'b1-nemzetiugy-05-marciusunnep', 'b1-nemzetiugy'])
- Reader B: Unit 36 compromise-1867 (b1-kiegyezes-01 b1-kiegyezes-02 b1-kiegyezes-03 b1-kiegyezes-04 b1-kiegyezes-05 b1-kiegyezes-consolidation; stories ['b1-kiegyezes-01-passzivellenallas', 'b1-kiegyezes-02-deakferenc', 'b1-kiegyezes-03-koronazas', 'b1-kiegyezes-04-dualizmus', 'b1-kiegyezes-05-fejlodes', 'b1-kiegyezes']); Unit 38 austria-hungary (b1-monarchia-01 b1-monarchia-02 b1-monarchia-03 b1-monarchia-04 b1-monarchia-05 b1-monarchia-consolidation; stories ['b1-monarchia-01-ketsas', 'b1-monarchia-02-millennium', 'b1-monarchia-03-vilagvaros', 'b1-monarchia-04-ipar', 'b1-monarchia-05-bekeidok', 'b1-monarchia'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 32 revolution-1848 | citizenship | 6 / 6 |
| 34 kossuth-petofi-national-cause | citizenship | 11 / 4 |
| 36 compromise-1867 | citizenship | 11 / 6 |
| 38 austria-hungary | citizenship | 12 / 4 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-forradalom-01 b1-forradalom-02 b1-forradalom-03 b1-forradalom-04 b1-forradalom-05 b1-forradalom-consolidation b1-nemzetiugy-01 b1-nemzetiugy-02 b1-nemzetiugy-03 b1-nemzetiugy-04 b1-nemzetiugy-05 b1-nemzetiugy-consolidation b1-kiegyezes-01 b1-kiegyezes-02 b1-kiegyezes-03 b1-kiegyezes-04 b1-kiegyezes-05 b1-kiegyezes-consolidation b1-monarchia-01 b1-monarchia-02 b1-monarchia-03 b1-monarchia-04 b1-monarchia-05 b1-monarchia-consolidation
