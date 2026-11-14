# hu C1 batch: hu-c1-batch-core-01-08

Started 2026-11-14T03:17:36Z from origin/master 6c9878bd. 2 Sonnet reader(s).

- Reader A: C1 Unit 1 argument-cohesion (c1-01-01 c1-01-02 c1-01-03 c1-01-04 c1-01-05 c1-01-consolidation; stories ['c1-01-babits']); C1 Unit 2 syntactic-compression (c1-02-01 c1-02-02 c1-02-03 c1-02-04 c1-02-05 c1-02-consolidation; stories ['c1-02-kosztolanyi']); C1 Unit 3 hedging-evidentials (c1-03-01 c1-03-02 c1-03-03 c1-03-04 c1-03-05 c1-03-consolidation; stories ['c1-03-szerb']); C1 Unit 4 polemics-refutation (c1-04-01 c1-04-02 c1-04-03 c1-04-04 c1-04-05 c1-04-consolidation; stories ['c1-04-ady'])
- Reader B: C1 Unit 5 irony-understatement (c1-05-01 c1-05-02 c1-05-03 c1-05-04 c1-05-05 c1-05-consolidation; stories ['c1-05-orkeny']); C1 Unit 6 metaphor-idiom (c1-06-01 c1-06-02 c1-06-03 c1-06-04 c1-06-05 c1-06-consolidation; stories ['c1-06-pilinszky']); C1 Unit 7 legal-language (c1-07-01 c1-07-02 c1-07-03 c1-07-04 c1-07-05 c1-07-consolidation; stories ['c1-07-eotvos']); C1 Unit 8 passive-avoidance (c1-08-01 c1-08-02 c1-08-03 c1-08-04 c1-08-05 c1-08-consolidation; stories ['c1-08-mikszath'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Unit 1 argument-cohesion | core | 19 / 13 |
| C1 Unit 2 syntactic-compression | core | 9 / 13 |
| C1 Unit 3 hedging-evidentials | core | 5 / 11 |
| C1 Unit 4 polemics-refutation | core | 4 / 13 |
| C1 Unit 5 irony-understatement | core | 3 / 17 |
| C1 Unit 6 metaphor-idiom | core | 6 / 14 |
| C1 Unit 7 legal-language | core | 2 / 6 |
| C1 Unit 8 passive-avoidance | core | 2 / 13 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-01-01 c1-01-02 c1-01-03 c1-01-04 c1-01-05 c1-01-consolidation c1-02-01 c1-02-02 c1-02-03 c1-02-04 c1-02-05 c1-02-consolidation c1-03-01 c1-03-02 c1-03-03 c1-03-04 c1-03-05 c1-03-consolidation c1-04-01 c1-04-02 c1-04-03 c1-04-04 c1-04-05 c1-04-consolidation c1-05-01 c1-05-02 c1-05-03 c1-05-04 c1-05-05 c1-05-consolidation c1-06-01 c1-06-02 c1-06-03 c1-06-04 c1-06-05 c1-06-consolidation c1-07-01 c1-07-02 c1-07-03 c1-07-04 c1-07-05 c1-07-consolidation c1-08-01 c1-08-02 c1-08-03 c1-08-04 c1-08-05 c1-08-consolidation
