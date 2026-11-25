# es B2 batch: es-b2-batch-latam-17-22

Started 2026-11-25T12:03:37Z from origin/master 031a4653. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 17 ecuador (b2-ecuador-01 b2-ecuador-02 b2-ecuador-03 b2-ecuador-04 b2-ecuador-05 b2-ecuador-consolidation; stories ['b2-ecuador-01', 'b2-ecuador-02', 'b2-ecuador-03', 'b2-ecuador-04', 'b2-ecuador-05', 'b2-ecuador-consolidation']); B2 Latin America Unit 18 peru-cusco-andes (b2-peruandino-01 b2-peruandino-02 b2-peruandino-03 b2-peruandino-04 b2-peruandino-05 b2-peruandino-consolidation; stories ['b2-peruandino-01', 'b2-peruandino-02', 'b2-peruandino-03', 'b2-peruandino-04', 'b2-peruandino-05', 'b2-peruandino-consolidation']); B2 Latin America Unit 19 peru-coast-lima (b2-perucosta-01 b2-perucosta-02 b2-perucosta-03 b2-perucosta-04 b2-perucosta-05 b2-perucosta-consolidation; stories ['b2-perucosta-01', 'b2-perucosta-02', 'b2-perucosta-03', 'b2-perucosta-04', 'b2-perucosta-05', 'b2-perucosta-consolidation'])
- Reader B: B2 Latin America Unit 20 bolivia-altiplano (b2-boliviaaltiplano-01 b2-boliviaaltiplano-02 b2-boliviaaltiplano-03 b2-boliviaaltiplano-04 b2-boliviaaltiplano-05 b2-boliviaaltiplano-consolidation; stories ['b2-boliviaaltiplano-01', 'b2-boliviaaltiplano-02', 'b2-boliviaaltiplano-03', 'b2-boliviaaltiplano-04', 'b2-boliviaaltiplano-05', 'b2-boliviaaltiplano-consolidation']); B2 Latin America Unit 21 bolivia-lowlands (b2-boliviaoriente-01 b2-boliviaoriente-02 b2-boliviaoriente-03 b2-boliviaoriente-04 b2-boliviaoriente-05 b2-boliviaoriente-consolidation; stories ['b2-boliviaoriente-01', 'b2-boliviaoriente-02', 'b2-boliviaoriente-03', 'b2-boliviaoriente-04', 'b2-boliviaoriente-05', 'b2-boliviaoriente-consolidation']); B2 Latin America Unit 22 chile-central (b2-chilecentro-01 b2-chilecentro-02 b2-chilecentro-03 b2-chilecentro-04 b2-chilecentro-05 b2-chilecentro-consolidation; stories ['b2-chilecentro-01', 'b2-chilecentro-02', 'b2-chilecentro-03', 'b2-chilecentro-04', 'b2-chilecentro-05', 'b2-chilecentro-consolidation'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 17 ecuador | latam | 11 / 8 |
| B2 Latin America Unit 18 peru-cusco-andes | latam | 15 / 10 |
| B2 Latin America Unit 19 peru-coast-lima | latam | 9 / 6 |
| B2 Latin America Unit 20 bolivia-altiplano | latam | 8 / 7 |
| B2 Latin America Unit 21 bolivia-lowlands | latam | 2 / 21 |
| B2 Latin America Unit 22 chile-central | latam | 3 / 26 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-ecuador-01 b2-ecuador-02 b2-ecuador-03 b2-ecuador-04 b2-ecuador-05 b2-ecuador-consolidation b2-peruandino-01 b2-peruandino-02 b2-peruandino-03 b2-peruandino-04 b2-peruandino-05 b2-peruandino-consolidation b2-perucosta-01 b2-perucosta-02 b2-perucosta-03 b2-perucosta-04 b2-perucosta-05 b2-perucosta-consolidation b2-boliviaaltiplano-01 b2-boliviaaltiplano-02 b2-boliviaaltiplano-03 b2-boliviaaltiplano-04 b2-boliviaaltiplano-05 b2-boliviaaltiplano-consolidation b2-boliviaoriente-01 b2-boliviaoriente-02 b2-boliviaoriente-03 b2-boliviaoriente-04 b2-boliviaoriente-05 b2-boliviaoriente-consolidation b2-chilecentro-01 b2-chilecentro-02 b2-chilecentro-03 b2-chilecentro-04 b2-chilecentro-05 b2-chilecentro-consolidation

## Method (2026-11-25)

As batch 11–16 (three units per agent, all topic-only, facts searched before launch). Brief adds the
no-invented-people rule up front; consolidation story files are the reviewer's
(`latam_consolidation_story.py`).

## Agents (edit-in-place, Sonnet), started 12:04 UTC on 031a4653
