# hu B2 batch: hu-b2-batch-core-65-71

Started 2026-11-04T15:07:59Z from origin/master e49969cd. 2 Sonnet reader(s).

- Reader A: Unit 65 political-philosophy (b2-33-01 b2-33-02 b2-33-03 b2-33-04 b2-33-05 b2-33-consolidation; stories ['b2-33-kisallamoknyomorusage']); Unit 67 slang-register (b2-34-01 b2-34-02 b2-34-03 b2-34-04 b2-34-05 b2-34-consolidation; stories ['b2-34-piszkosfred'])
- Reader B: Unit 69 technology-futurism-human-agency (b2-35-01 b2-35-02 b2-35-03 b2-35-04 b2-35-05 b2-35-consolidation; stories ['b2-35-utazasfaremidoba']); Unit 71 mastery-voice (b2-36-01 b2-36-02 b2-36-03 b2-36-04 b2-36-05 b2-36-consolidation; stories ['b2-36-estikornel'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 65 political-philosophy | core | 9 / 0 |
| 67 slang-register | core | 13 / 1 |
| 69 technology-futurism-human-agency | core | 17 / 2 |
| 71 mastery-voice | core | 14 / 1 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-33-01 b2-33-02 b2-33-03 b2-33-04 b2-33-05 b2-33-consolidation b2-34-01 b2-34-02 b2-34-03 b2-34-04 b2-34-05 b2-34-consolidation b2-35-01 b2-35-02 b2-35-03 b2-35-04 b2-35-05 b2-35-consolidation b2-36-01 b2-36-02 b2-36-03 b2-36-04 b2-36-05 b2-36-consolidation
