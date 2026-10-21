# es A2 batch: es-a2-batch-07-12

Started 2026-10-21T07:48:14Z from origin/master c8493d38. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 7 how-long (a2-07-01 a2-07-02 a2-07-03 a2-07-04 a2-07-05 a2-07-consolidation; stories ['a2-07']); Unit 8 making-responding-invitations (a2-08-01 a2-08-02 a2-08-03 a2-08-04 a2-08-05 a2-08-consolidation; stories ['a2-08']); Unit 9 experiences (a2-09-01 a2-09-02 a2-09-03 a2-09-04 a2-09-05 a2-09-consolidation; stories ['a2-09'])
- Reader B: Unit 10 keeping-touch (a2-10-01 a2-10-02 a2-10-03 a2-10-04 a2-10-05 a2-10-consolidation; stories ['a2-10']); Unit 11 what-happened (a2-11-01 a2-11-02 a2-11-03 a2-11-04 a2-11-05 a2-11-consolidation; stories ['a2-11']); Unit 12 giving-receiving-things (a2-12-01 a2-12-02 a2-12-03 a2-12-04 a2-12-05 a2-12-consolidation; stories ['a2-12'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 7 how-long | 3 / 10 | 3 / 10 |
| 8 making-responding-invitations | 18 / 18 | 18 / 21 |
| 9 experiences | 16 / 15 | 16 / 16 |
| 10 keeping-touch | 8 / 12 | 8 / 13 |
| 11 what-happened | 3 / 40 | 3 / 42 |
| 12 giving-receiving-things | 2 / 11 | 2 / 11 |

## Files differing es-es vs es-latam

- how-long: a2-07.json
- making-responding-invitations: a2-08.json
- experiences: a2-09.json
- keeping-touch: a2-10-05-ex.json, a2-10.json
- what-happened: a2-11-03-gr.json, a2-11.json
- giving-receiving-things: a2-12-05-ex.json, a2-12.json

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> a2 --jobs 4 --only a2-07-01 a2-07-02 a2-07-03 a2-07-04 a2-07-05 a2-07-consolidation a2-08-01 a2-08-02 a2-08-03 a2-08-04 a2-08-05 a2-08-consolidation a2-09-01 a2-09-02 a2-09-03 a2-09-04 a2-09-05 a2-09-consolidation a2-10-01 a2-10-02 a2-10-03 a2-10-04 a2-10-05 a2-10-consolidation a2-11-01 a2-11-02 a2-11-03 a2-11-04 a2-11-05 a2-11-consolidation a2-12-01 a2-12-02 a2-12-03 a2-12-04 a2-12-05 a2-12-consolidation
- Readers launched 07:49:37Z.
- Reader A finished 08:13Z: fixes 45 + 75 + 39 = 159; report file write allowed; 351,365 tokens, 68 tool uses, 23.4 min (~117k a unit)
- Reader B stopped by a Sonnet session limit (resets 10:30Z) after Units 10-11's files; resumed 10:31Z for Unit 12
