# es B1 batch: hu-b1-pilot

Started 2026-10-22T08:39:02Z from origin/master 22c14a28. 2 Sonnet reader(s).

- Reader A: Unit 1 longer-stories (b1-01-01 b1-01-02 b1-01-03 b1-01-04 b1-01-05 b1-01-consolidation; stories ['b1-01-janosvitez'])
- Reader B: Unit 2 hungary-today-land-symbols (b1-orszagma-01 b1-orszagma-02 b1-orszagma-03 b1-orszagma-04 b1-orszagma-05 b1-orszagma-consolidation; stories ['b1-orszagma-01-elhelyezkedes', 'b1-orszagma-02-megyekesvarosok', 'b1-orszagma-03-zaszlocimer', 'b1-orszagma-04-szomszedosorszagok', 'b1-orszagma-05-attekintes'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 1 longer-stories | core | 0 / 5 |
| 2 hungary-today-land-symbols | citizenship | 1 / 4 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-01-01 b1-01-02 b1-01-03 b1-01-04 b1-01-05 b1-01-consolidation b1-orszagma-01 b1-orszagma-02 b1-orszagma-03 b1-orszagma-04 b1-orszagma-05 b1-orszagma-consolidation
