# es B1 batch: es-b1-batch-53-63

Started 2026-11-12T05:48:45Z from origin/master 6c40eaf4. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 53 social-life-communication (b1-27-01 b1-27-02 b1-27-03 b1-27-04 b1-27-05 b1-27-consolidation; stories ['b1-27-dondimas']); Unit 55 rules-rights-responsibilities (b1-28-01 b1-28-02 b1-28-03 b1-28-04 b1-28-05 b1-28-consolidation; stories ['b1-28-nuestraamerica']); Unit 57 migration-identity (b1-29-01 b1-29-02 b1-29-03 b1-29-04 b1-29-05 b1-29-consolidation; stories ['b1-29-exilio'])
- Reader B: Unit 59 culture-language-society (b1-30-01 b1-30-02 b1-30-03 b1-30-04 b1-30-05 b1-30-consolidation; stories ['b1-30-andresbello']); Unit 61 future-society (b1-31-01 b1-31-02 b1-31-03 b1-31-04 b1-31-05 b1-31-consolidation; stories ['b1-31-eltriunfodecaliban']); Unit 63 connecting-ideas (b1-32-01 b1-32-02 b1-32-03 b1-32-04 b1-32-05 b1-32-consolidation; stories ['b1-32-porestarazon'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 53 social-life-communication | 17 / 2 | 17 / 14 |
| 55 rules-rights-responsibilities | 16 / 0 | 16 / 9 |
| 57 migration-identity | 24 / 0 | 24 / 0 |
| 59 culture-language-society | 17 / 0 | 17 / 0 |
| 61 future-society | 15 / 3 | 15 / 3 |
| 63 connecting-ideas | 15 / 8 | 15 / 10 |

## Files differing es-es vs es-latam

- social-life-communication: none
- rules-rights-responsibilities: none
- migration-identity: none
- culture-language-society: none
- future-society: none
- connecting-ideas: none

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> b1 --jobs 4 --only b1-27-01 b1-27-02 b1-27-03 b1-27-04 b1-27-05 b1-27-consolidation b1-28-01 b1-28-02 b1-28-03 b1-28-04 b1-28-05 b1-28-consolidation b1-29-01 b1-29-02 b1-29-03 b1-29-04 b1-29-05 b1-29-consolidation b1-30-01 b1-30-02 b1-30-03 b1-30-04 b1-30-05 b1-30-consolidation b1-31-01 b1-31-02 b1-31-03 b1-31-04 b1-31-05 b1-31-consolidation b1-32-01 b1-32-02 b1-32-03 b1-32-04 b1-32-05 b1-32-consolidation
