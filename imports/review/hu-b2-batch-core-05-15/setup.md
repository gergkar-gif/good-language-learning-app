# hu B2 batch: hu-b2-batch-core-05-15

Started 2026-10-30T06:55:49Z from origin/master 6204f5aa. 2 Sonnet reader(s).

- Reader A: Unit 5 language-style-word-formation (b2-03-01 b2-03-02 b2-03-03 b2-03-04 b2-03-05 b2-03-consolidation; stories ['b2-03-igyirtokti']); Unit 7 performance-drama-persuasion (b2-04-01 b2-04-02 b2-04-03 b2-04-04 b2-04-05 b2-04-consolidation; stories ['b2-04-bankban']); Unit 9 roots-tradition-collective-memory (b2-05-01 b2-05-02 b2-05-03 b2-05-04 b2-05-05 b2-05-consolidation; stories ['b2-05-abelarengetegben'])
- Reader B: Unit 11 aesthetics-vision-creative-obsession (b2-06-01 b2-06-02 b2-06-03 b2-06-04 b2-06-05 b2-06-consolidation; stories ['b2-06-avarazslokertje']); Unit 13 scientific-discovery-hypothesis (b2-07-01 b2-07-02 b2-07-03 b2-07-04 b2-07-05 b2-07-consolidation; stories ['b2-07-utazasakoponyamkorul']); Unit 15 medicine-ethics-responsibility (b2-08-01 b2-08-02 b2-08-03 b2-08-04 b2-08-05 b2-08-consolidation; stories ['b2-08-nemethlaszlo'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 5 language-style-word-formation | core | 9 / 2 |
| 7 performance-drama-persuasion | core | 8 / 0 |
| 9 roots-tradition-collective-memory | core | 13 / 0 |
| 11 aesthetics-vision-creative-obsession | core | 18 / 0 |
| 13 scientific-discovery-hypothesis | core | 16 / 0 |
| 15 medicine-ethics-responsibility | core | 19 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-03-01 b2-03-02 b2-03-03 b2-03-04 b2-03-05 b2-03-consolidation b2-04-01 b2-04-02 b2-04-03 b2-04-04 b2-04-05 b2-04-consolidation b2-05-01 b2-05-02 b2-05-03 b2-05-04 b2-05-05 b2-05-consolidation b2-06-01 b2-06-02 b2-06-03 b2-06-04 b2-06-05 b2-06-consolidation b2-07-01 b2-07-02 b2-07-03 b2-07-04 b2-07-05 b2-07-consolidation b2-08-01 b2-08-02 b2-08-03 b2-08-04 b2-08-05 b2-08-consolidation
