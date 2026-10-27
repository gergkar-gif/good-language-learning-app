# es B1 batch: hu-b1-batch-core-55-65

Started 2026-10-27T23:28:43Z from origin/master 85fa4fb6. 2 Sonnet reader(s).

- Reader A: Unit 55 rules-rights-responsibilities (b1-28-01 b1-28-02 b1-28-03 b1-28-04 b1-28-05 b1-28-consolidation; stories ['b1-28-mikszath']); Unit 57 migration-identity (b1-29-01 b1-29-02 b1-29-03 b1-29-04 b1-29-05 b1-29-consolidation; stories ['b1-29-marai']); Unit 59 culture-language-society (b1-30-01 b1-30-02 b1-30-03 b1-30-04 b1-30-05 b1-30-consolidation; stories ['b1-30-szabo'])
- Reader B: Unit 61 future-society (b1-31-01 b1-31-02 b1-31-03 b1-31-04 b1-31-05 b1-31-consolidation; stories ['b1-31-madach']); Unit 63 connecting-ideas (b1-32-01 b1-32-02 b1-32-03 b1-32-04 b1-32-05 b1-32-consolidation; stories ['b1-32-jokai']); Unit 65 reported-speech (b1-33-01 b1-33-02 b1-33-03 b1-33-04 b1-33-05 b1-33-consolidation; stories ['b1-33-mikszath'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 55 rules-rights-responsibilities | core | 10 / 2 |
| 57 migration-identity | core | 14 / 4 |
| 59 culture-language-society | core | 10 / 2 |
| 61 future-society | core | 10 / 2 |
| 63 connecting-ideas | core | 12 / 1 |
| 65 reported-speech | core | 6 / 5 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-28-01 b1-28-02 b1-28-03 b1-28-04 b1-28-05 b1-28-consolidation b1-29-01 b1-29-02 b1-29-03 b1-29-04 b1-29-05 b1-29-consolidation b1-30-01 b1-30-02 b1-30-03 b1-30-04 b1-30-05 b1-30-consolidation b1-31-01 b1-31-02 b1-31-03 b1-31-04 b1-31-05 b1-31-consolidation b1-32-01 b1-32-02 b1-32-03 b1-32-04 b1-32-05 b1-32-consolidation b1-33-01 b1-33-02 b1-33-03 b1-33-04 b1-33-05 b1-33-consolidation
