# es B1 batch: es-b1-batch-65-76

Started 2026-11-12T10:24:35Z from origin/master c8ec3cce. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 65 reported-speech (b1-33-01 b1-33-02 b1-33-03 b1-33-04 b1-33-05 b1-33-consolidation; stories ['b1-33-elrumor']); Unit 67 complex-opinions (b1-34-01 b1-34-02 b1-34-03 b1-34-04 b1-34-05 b1-34-consolidation; stories ['b1-34-dudasrazonables']); Unit 69 hypotheticals-possibilities (b1-35-01 b1-35-02 b1-35-03 b1-35-04 b1-35-05 b1-35-consolidation; stories ['b1-35-ojosverdes']); Unit 71 independent-spanish (b1-36-01 b1-36-02 b1-36-03 b1-36-04 b1-36-05 b1-36-consolidation; stories ['b1-36'])
- Reader B: Unit 73 present-perfect-subjunctive (b1-37-01 b1-37-02 b1-37-03 b1-37-04 b1-37-05 b1-37-consolidation; stories []); Unit 74 sequence-of-tenses (b1-38-01 b1-38-02 b1-38-03 b1-38-04 b1-38-05 b1-38-consolidation; stories []); Unit 75 verbs-of-becoming (b1-39-01 b1-39-02 b1-39-03 b1-39-04 b1-39-05 b1-39-consolidation; stories []); Unit 76 connectors-prepositional-regimes (b1-40-01 b1-40-02 b1-40-03 b1-40-04 b1-40-05 b1-40-consolidation; stories [])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 65 reported-speech | 9 / 1 | 9 / 1 |
| 67 complex-opinions | 13 / 4 | 13 / 3 |
| 69 hypotheticals-possibilities | 11 / 1 | 11 / 1 |
| 71 independent-spanish | 18 / 1 | 18 / 1 |
| 73 present-perfect-subjunctive | 8 / 19 | 11 / 20 |
| 74 sequence-of-tenses | 10 / 15 | 10 / 18 |
| 75 verbs-of-becoming | 14 / 15 | 14 / 18 |
| 76 connectors-prepositional-regimes | 14 / 19 | 14 / 20 |

## Files differing es-es vs es-latam

- reported-speech: none
- complex-opinions: none
- hypotheticals-possibilities: none
- independent-spanish: none
- present-perfect-subjunctive: none
- sequence-of-tenses: none
- verbs-of-becoming: none
- connectors-prepositional-regimes: b1-40-01-ex.json

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-33-01 b1-33-02 b1-33-03 b1-33-04 b1-33-05 b1-33-consolidation b1-34-01 b1-34-02 b1-34-03 b1-34-04 b1-34-05 b1-34-consolidation b1-35-01 b1-35-02 b1-35-03 b1-35-04 b1-35-05 b1-35-consolidation b1-36-01 b1-36-02 b1-36-03 b1-36-04 b1-36-05 b1-36-consolidation b1-37-01 b1-37-02 b1-37-03 b1-37-04 b1-37-05 b1-37-consolidation b1-38-01 b1-38-02 b1-38-03 b1-38-04 b1-38-05 b1-38-consolidation b1-39-01 b1-39-02 b1-39-03 b1-39-04 b1-39-05 b1-39-consolidation b1-40-01 b1-40-02 b1-40-03 b1-40-04 b1-40-05 b1-40-consolidation
