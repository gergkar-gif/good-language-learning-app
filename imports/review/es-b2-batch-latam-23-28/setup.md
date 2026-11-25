# es B2 batch: es-b2-batch-latam-23-28

Started 2026-11-25T12:27:26Z from origin/master 842d5dbe. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 23 chile-atacama-patagonia (b2-chileextremos-01 b2-chileextremos-02 b2-chileextremos-03 b2-chileextremos-04 b2-chileextremos-05 b2-chileextremos-consolidation; stories ['b2-chileextremos-01', 'b2-chileextremos-02', 'b2-chileextremos-03', 'b2-chileextremos-04', 'b2-chileextremos-05', 'b2-chileextremos-consolidation']); B2 Latin America Unit 24 argentina-buenos-aires (b2-argentinaba-01 b2-argentinaba-02 b2-argentinaba-03 b2-argentinaba-04 b2-argentinaba-05 b2-argentinaba-consolidation; stories ['b2-argentinaba-01', 'b2-argentinaba-02', 'b2-argentinaba-03', 'b2-argentinaba-04', 'b2-argentinaba-05', 'b2-argentinaba-consolidation']); B2 Latin America Unit 25 argentina-pampas-patagonia (b2-argentinaregiones-01 b2-argentinaregiones-02 b2-argentinaregiones-03 b2-argentinaregiones-04 b2-argentinaregiones-05 b2-argentinaregiones-consolidation; stories ['b2-argentinaregiones-01', 'b2-argentinaregiones-02', 'b2-argentinaregiones-03', 'b2-argentinaregiones-04', 'b2-argentinaregiones-05', 'b2-argentinaregiones-consolidation'])
- Reader B: B2 Latin America Unit 26 argentina-politics (b2-argentinasociedad-01 b2-argentinasociedad-02 b2-argentinasociedad-03 b2-argentinasociedad-04 b2-argentinasociedad-05 b2-argentinasociedad-consolidation; stories ['b2-argentinasociedad-01', 'b2-argentinasociedad-02', 'b2-argentinasociedad-03', 'b2-argentinasociedad-04', 'b2-argentinasociedad-05', 'b2-argentinasociedad-consolidation']); B2 Latin America Unit 27 uruguay (b2-uruguay-01 b2-uruguay-02 b2-uruguay-03 b2-uruguay-04 b2-uruguay-05 b2-uruguay-consolidation; stories ['b2-uruguay-01', 'b2-uruguay-02', 'b2-uruguay-03', 'b2-uruguay-04', 'b2-uruguay-05', 'b2-uruguay-consolidation']); B2 Latin America Unit 28 paraguay (b2-paraguay-01 b2-paraguay-02 b2-paraguay-03 b2-paraguay-04 b2-paraguay-05 b2-paraguay-consolidation; stories ['b2-paraguay-01', 'b2-paraguay-02', 'b2-paraguay-03', 'b2-paraguay-04', 'b2-paraguay-05'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 23 chile-atacama-patagonia | latam | 1 / 20 |
| B2 Latin America Unit 24 argentina-buenos-aires | latam | 17 / 20 |
| B2 Latin America Unit 25 argentina-pampas-patagonia | latam | 14 / 23 |
| B2 Latin America Unit 26 argentina-politics | latam | 16 / 36 |
| B2 Latin America Unit 27 uruguay | latam | 2 / 28 |
| B2 Latin America Unit 28 paraguay | latam | 6 / 21 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-chileextremos-01 b2-chileextremos-02 b2-chileextremos-03 b2-chileextremos-04 b2-chileextremos-05 b2-chileextremos-consolidation b2-argentinaba-01 b2-argentinaba-02 b2-argentinaba-03 b2-argentinaba-04 b2-argentinaba-05 b2-argentinaba-consolidation b2-argentinaregiones-01 b2-argentinaregiones-02 b2-argentinaregiones-03 b2-argentinaregiones-04 b2-argentinaregiones-05 b2-argentinaregiones-consolidation b2-argentinasociedad-01 b2-argentinasociedad-02 b2-argentinasociedad-03 b2-argentinasociedad-04 b2-argentinasociedad-05 b2-argentinasociedad-consolidation b2-uruguay-01 b2-uruguay-02 b2-uruguay-03 b2-uruguay-04 b2-uruguay-05 b2-uruguay-consolidation b2-paraguay-01 b2-paraguay-02 b2-paraguay-03 b2-paraguay-04 b2-paraguay-05 b2-paraguay-consolidation

## Method (2026-11-25)

As batch 17–22. Mixed units: Units 24–27 drill known skills with a few later ones (re-pointed in
the notes) and two near-duplicate units (25: five concessions; 27: one skill twice), Units 23 and
28 partly topic-only.

## Agents (edit-in-place, Sonnet), started 12:28 UTC on 842d5dbe
