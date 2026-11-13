# es B2 batch: es-b2-batch-15-18

Started 2026-11-13T09:32:56Z from origin/master 94679340. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Unit 15 imperfect-subjunctive-forms-nuances (b2-15-01 b2-15-02 b2-15-03 b2-15-04 b2-15-05 b2-15-consolidation; stories ['b2-15']); B2 Unit 16 pluperfect-subjunctive (b2-16-01 b2-16-02 b2-16-03 b2-16-04 b2-16-05 b2-16-consolidation; stories ['b2-16'])
- Reader B: B2 Unit 17 reported-speech-past-frames (b2-17-01 b2-17-02 b2-17-03 b2-17-04 b2-17-05 b2-17-consolidation; stories ['b2-17']); B2 Unit 18 rhetorical-reporting-verbs (b2-18-01 b2-18-02 b2-18-03 b2-18-04 b2-18-05 b2-18-consolidation; stories ['b2-18'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Unit 15 imperfect-subjunctive-forms-nuances | core | 14 / 7 |
| B2 Unit 16 pluperfect-subjunctive | core | 14 / 11 |
| B2 Unit 17 reported-speech-past-frames | core | 8 / 9 |
| B2 Unit 18 rhetorical-reporting-verbs | core | 11 / 7 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-15-01 b2-15-02 b2-15-03 b2-15-04 b2-15-05 b2-15-consolidation b2-16-01 b2-16-02 b2-16-03 b2-16-04 b2-16-05 b2-16-consolidation b2-17-01 b2-17-02 b2-17-03 b2-17-04 b2-17-05 b2-17-consolidation b2-18-01 b2-18-02 b2-18-03 b2-18-04 b2-18-05 b2-18-consolidation

## Agents (edit-in-place, Sonnet), started 09:33 UTC

- A (Units 15, 16; /home/user/parlour-read-a): agent a57ceb64c0586c1df
- B (Units 17, 18; /home/user/parlour-read-b): agent ade4e5df004c44804

Resume a stopped agent with SendMessage to its id; never start a new one.
