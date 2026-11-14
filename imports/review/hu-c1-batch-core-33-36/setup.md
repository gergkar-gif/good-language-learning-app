# hu C1 batch: hu-c1-batch-core-33-36

Started 2026-11-14T18:30:38Z from origin/master 6686976f. 1 Sonnet reader(s).

- Reader A: C1 Unit 33 literary-modernism (c1-33-01 c1-33-02 c1-33-03 c1-33-04 c1-33-05 c1-33-consolidation; stories ['babits-europai-irodalom-tortenete']); C1 Unit 34 philosophy-of-science (c1-34-01 c1-34-02 c1-34-03 c1-34-04 c1-34-05 c1-34-consolidation; stories ['polanyi-tudomany-koztarsasaga']); C1 Unit 35 digital-ethics (c1-35-01 c1-35-02 c1-35-03 c1-35-04 c1-35-05 c1-35-consolidation; stories ['neumann-szamologep-es-az-agy']); C1 Unit 36 democratic-tradition (c1-36-01 c1-36-02 c1-36-03 c1-36-04 c1-36-05 c1-36-consolidation; stories ['deak-bibo-a-szabadsag-hagyomanya'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Unit 33 literary-modernism | core | 8 / 12 |
| C1 Unit 34 philosophy-of-science | core | 13 / 12 |
| C1 Unit 35 digital-ethics | core | 9 / 12 |
| C1 Unit 36 democratic-tradition | core | 10 / 13 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-33-01 c1-33-02 c1-33-03 c1-33-04 c1-33-05 c1-33-consolidation c1-34-01 c1-34-02 c1-34-03 c1-34-04 c1-34-05 c1-34-consolidation c1-35-01 c1-35-02 c1-35-03 c1-35-04 c1-35-05 c1-35-consolidation c1-36-01 c1-36-02 c1-36-03 c1-36-04 c1-36-05 c1-36-consolidation
