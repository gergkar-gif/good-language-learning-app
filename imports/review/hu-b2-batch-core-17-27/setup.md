# hu B2 batch: hu-b2-batch-core-17-27

Started 2026-11-04T00:11:14Z from origin/master 9edfe89e. 2 Sonnet reader(s).

- Reader A: Unit 17 logic-paradox-abstract-reasoning (b2-09-01 b2-09-02 b2-09-03 b2-09-04 b2-09-05 b2-09-consolidation; stories ['b2-09-egypercesek']); Unit 19 mentorship-discipline-intellectual-growth (b2-10-01 b2-10-02 b2-10-03 b2-10-04 b2-10-05 b2-10-consolidation; stories ['b2-10-halalfiai']); Unit 21 unconscious-dreams-inner-conflict (b2-11-01 b2-11-02 b2-11-03 b2-11-04 b2-11-05 b2-11-consolidation; stories ['b2-11-afelesegemtortenete'])
- Reader B: Unit 23 ingenuity-design (b2-12-01 b2-12-02 b2-12-03 b2-12-04 b2-12-05 b2-12-consolidation; stories ['b2-12-feketegyemantok']); Unit 25 irony-satire (b2-13-01 b2-13-02 b2-13-03 b2-13-04 b2-13-05 b2-13-consolidation; stories ['b2-13-beszterceostroma']); Unit 27 visual-storytelling-perspective-time (b2-14-01 b2-14-02 b2-14-03 b2-14-04 b2-14-05 b2-14-consolidation; stories ['b2-14-magasiskola'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 17 logic-paradox-abstract-reasoning | core | 15 / 3 |
| 19 mentorship-discipline-intellectual-growth | core | 38 / 2 |
| 21 unconscious-dreams-inner-conflict | core | 9 / 0 |
| 23 ingenuity-design | core | 5 / 1 |
| 25 irony-satire | core | 23 / 2 |
| 27 visual-storytelling-perspective-time | core | 18 / 2 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-09-01 b2-09-02 b2-09-03 b2-09-04 b2-09-05 b2-09-consolidation b2-10-01 b2-10-02 b2-10-03 b2-10-04 b2-10-05 b2-10-consolidation b2-11-01 b2-11-02 b2-11-03 b2-11-04 b2-11-05 b2-11-consolidation b2-12-01 b2-12-02 b2-12-03 b2-12-04 b2-12-05 b2-12-consolidation b2-13-01 b2-13-02 b2-13-03 b2-13-04 b2-13-05 b2-13-consolidation b2-14-01 b2-14-02 b2-14-03 b2-14-04 b2-14-05 b2-14-consolidation
