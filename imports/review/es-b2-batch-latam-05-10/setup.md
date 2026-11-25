# es B2 batch: es-b2-batch-latam-05-10

Started 2026-11-25T06:47:44Z from origin/master 5547a695. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 5 el-salvador-honduras (b2-salvadorhonduras-01 b2-salvadorhonduras-02 b2-salvadorhonduras-03 b2-salvadorhonduras-04 b2-salvadorhonduras-05 b2-salvadorhonduras-consolidation; stories ['b2-salvadorhonduras-01', 'b2-salvadorhonduras-02', 'b2-salvadorhonduras-03', 'b2-salvadorhonduras-04', 'b2-salvadorhonduras-05']); B2 Latin America Unit 6 nicaragua (b2-nicaragua-01 b2-nicaragua-02 b2-nicaragua-03 b2-nicaragua-04 b2-nicaragua-05 b2-nicaragua-consolidation; stories ['b2-nicaragua-01', 'b2-nicaragua-02', 'b2-nicaragua-03', 'b2-nicaragua-04', 'b2-nicaragua-05']); B2 Latin America Unit 7 costa-rica (b2-costarica-01 b2-costarica-02 b2-costarica-03 b2-costarica-04 b2-costarica-05 b2-costarica-consolidation; stories ['b2-costarica-01', 'b2-costarica-02', 'b2-costarica-03', 'b2-costarica-04', 'b2-costarica-05', 'b2-costarica'])
- Reader B: B2 Latin America Unit 8 panama (b2-panama-01 b2-panama-02 b2-panama-03 b2-panama-04 b2-panama-05 b2-panama-consolidation; stories ['b2-panama-01', 'b2-panama-02', 'b2-panama-03', 'b2-panama-04', 'b2-panama-05', 'b2-panama']); B2 Latin America Unit 9 belize-guianas (b2-guyanas-01 b2-guyanas-02 b2-guyanas-03 b2-guyanas-04 b2-guyanas-05 b2-guyanas-consolidation; stories ['b2-guyanas-01', 'b2-guyanas-02', 'b2-guyanas-03', 'b2-guyanas-04', 'b2-guyanas-05', 'b2-guyanas']); B2 Latin America Unit 10 cuba (b2-cuba-01 b2-cuba-02 b2-cuba-03 b2-cuba-04 b2-cuba-05 b2-cuba-consolidation; stories ['b2-cuba-01', 'b2-cuba-02', 'b2-cuba-03', 'b2-cuba-04', 'b2-cuba-05', 'b2-cuba'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 5 el-salvador-honduras | latam | 29 / 16 |
| B2 Latin America Unit 6 nicaragua | latam | 33 / 13 |
| B2 Latin America Unit 7 costa-rica | latam | 13 / 17 |
| B2 Latin America Unit 8 panama | latam | 15 / 14 |
| B2 Latin America Unit 9 belize-guianas | latam | 17 / 21 |
| B2 Latin America Unit 10 cuba | latam | 7 / 21 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-salvadorhonduras-01 b2-salvadorhonduras-02 b2-salvadorhonduras-03 b2-salvadorhonduras-04 b2-salvadorhonduras-05 b2-salvadorhonduras-consolidation b2-nicaragua-01 b2-nicaragua-02 b2-nicaragua-03 b2-nicaragua-04 b2-nicaragua-05 b2-nicaragua-consolidation b2-costarica-01 b2-costarica-02 b2-costarica-03 b2-costarica-04 b2-costarica-05 b2-costarica-consolidation b2-panama-01 b2-panama-02 b2-panama-03 b2-panama-04 b2-panama-05 b2-panama-consolidation b2-guyanas-01 b2-guyanas-02 b2-guyanas-03 b2-guyanas-04 b2-guyanas-05 b2-guyanas-consolidation b2-cuba-01 b2-cuba-02 b2-cuba-03 b2-cuba-04 b2-cuba-05 b2-cuba-consolidation

## Method (2026-11-25)

As batch 1–4, three units per agent (core B2 fell from ~166k to ~100k a unit at three). Briefs:
`brief-a.txt`, `brief-b.txt` = `unit-<x>.txt` + `scripts/templates/edit-spanish-latam-b2-track.txt`.
New in this batch: Units 7–10 are topic-only (every lesson tagged with a retired topic slug, no
grammar); each lesson gets one known skill, suggested in the notes.

## Agents (edit-in-place, Sonnet), started 06:48 UTC on 5547a695
