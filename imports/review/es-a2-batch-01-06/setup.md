# es A2 batch: es-a2-batch-01-06

Started 2026-10-21T06:51:33Z from origin/master 0828a604. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 1 your-trip (a2-01-01 a2-01-02 a2-01-03 a2-01-04 a2-01-05 a2-01-consolidation; stories ['a2-01']); Unit 2 what-you-have-done (a2-02-01 a2-02-02 a2-02-03 a2-02-04 a2-02-05 a2-02-consolidation; stories ['a2-02']); Unit 3 day-out (a2-03-01 a2-03-02 a2-03-03 a2-03-04 a2-03-05 a2-03-consolidation; stories ['a2-03'])
- Reader B: Unit 4 following-instructions (a2-04-01 a2-04-02 a2-04-03 a2-04-04 a2-04-05 a2-04-consolidation; stories ['a2-04']); Unit 5 giving-reasons-opinions (a2-05-01 a2-05-02 a2-05-03 a2-05-04 a2-05-05 a2-05-consolidation; stories ['a2-05']); Unit 6 comparing-trips-memories (a2-06-01 a2-06-02 a2-06-03 a2-06-04 a2-06-05 a2-06-consolidation; stories ['a2-06'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 1 your-trip | 0 / 25 | 0 / 28 |
| 2 what-you-have-done | 7 / 12 | 7 / 18 |
| 3 day-out | 4 / 20 | 4 / 20 |
| 4 following-instructions | 6 / 29 | 6 / 28 |
| 5 giving-reasons-opinions | 1 / 19 | 1 / 20 |
| 6 comparing-trips-memories | 4 / 38 | 4 / 38 |

## Files differing es-es vs es-latam

- your-trip: a2-01-01-participles-gr.json, a2-01-03-questions-gr.json, a2-01-03-ex.json, a2-01.json, a2-01-consolidation-ex.json
- what-you-have-done: none
- day-out: a2-03-01-gr.json, a2-03-01-ex.json, a2-03-02-gr.json, a2-03-02-voc.json, a2-03-02-ex.json, a2-03.json
- following-instructions: none
- giving-reasons-opinions: a2-05-05-ex.json
- comparing-trips-memories: a2-06.json
- Readers launched 06:53:00Z.
- Reader B finished 07:10Z: fixes 36 + 24 + 41 = 101; report file write allowed; token count not in the hand-back
