# es B2 batch: es-b2-batch-latam-11-16

Started 2026-11-25T07:17:10Z from origin/master 9dd0bd98. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 11 dominican-republic (b2-dominicana-01 b2-dominicana-02 b2-dominicana-03 b2-dominicana-04 b2-dominicana-05 b2-dominicana-consolidation; stories ['b2-dominicana-01', 'b2-dominicana-02', 'b2-dominicana-03', 'b2-dominicana-04', 'b2-dominicana-05', 'b2-dominicana']); B2 Latin America Unit 12 puerto-rico (b2-puertorico-01 b2-puertorico-02 b2-puertorico-03 b2-puertorico-04 b2-puertorico-05 b2-puertorico-consolidation; stories ['b2-puertorico-01', 'b2-puertorico-02', 'b2-puertorico-03', 'b2-puertorico-04', 'b2-puertorico-05', 'b2-puertorico']); B2 Latin America Unit 13 colombia-andes (b2-colombiaandina-01 b2-colombiaandina-02 b2-colombiaandina-03 b2-colombiaandina-04 b2-colombiaandina-05 b2-colombiaandina-consolidation; stories ['b2-colombiaandina-01', 'b2-colombiaandina-02', 'b2-colombiaandina-03', 'b2-colombiaandina-04', 'b2-colombiaandina-05', 'b2-colombiaandina-consolidation'])
- Reader B: B2 Latin America Unit 14 colombia-caribbean-pacific (b2-colombiaperiferias-01 b2-colombiaperiferias-02 b2-colombiaperiferias-03 b2-colombiaperiferias-04 b2-colombiaperiferias-05 b2-colombiaperiferias-consolidation; stories ['b2-colombiaperiferias-01', 'b2-colombiaperiferias-02', 'b2-colombiaperiferias-03', 'b2-colombiaperiferias-04', 'b2-colombiaperiferias-05', 'b2-colombiaperiferias-consolidation']); B2 Latin America Unit 15 venezuela-oil-caracas (b2-venezuelapetroleo-01 b2-venezuelapetroleo-02 b2-venezuelapetroleo-03 b2-venezuelapetroleo-04 b2-venezuelapetroleo-05 b2-venezuelapetroleo-consolidation; stories ['b2-venezuelapetroleo-01', 'b2-venezuelapetroleo-02', 'b2-venezuelapetroleo-03', 'b2-venezuelapetroleo-04', 'b2-venezuelapetroleo-05', 'b2-venezuelapetroleo-consolidation']); B2 Latin America Unit 16 venezuela-llanos-diaspora (b2-venezuelasabana-01 b2-venezuelasabana-02 b2-venezuelasabana-03 b2-venezuelasabana-04 b2-venezuelasabana-05 b2-venezuelasabana-consolidation; stories ['b2-venezuelasabana-01', 'b2-venezuelasabana-02', 'b2-venezuelasabana-03', 'b2-venezuelasabana-04', 'b2-venezuelasabana-05', 'b2-venezuelasabana-consolidation'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 11 dominican-republic | latam | 13 / 15 |
| B2 Latin America Unit 12 puerto-rico | latam | 10 / 14 |
| B2 Latin America Unit 13 colombia-andes | latam | 15 / 15 |
| B2 Latin America Unit 14 colombia-caribbean-pacific | latam | 12 / 12 |
| B2 Latin America Unit 15 venezuela-oil-caracas | latam | 14 / 5 |
| B2 Latin America Unit 16 venezuela-llanos-diaspora | latam | 15 / 4 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-dominicana-01 b2-dominicana-02 b2-dominicana-03 b2-dominicana-04 b2-dominicana-05 b2-dominicana-consolidation b2-puertorico-01 b2-puertorico-02 b2-puertorico-03 b2-puertorico-04 b2-puertorico-05 b2-puertorico-consolidation b2-colombiaandina-01 b2-colombiaandina-02 b2-colombiaandina-03 b2-colombiaandina-04 b2-colombiaandina-05 b2-colombiaandina-consolidation b2-colombiaperiferias-01 b2-colombiaperiferias-02 b2-colombiaperiferias-03 b2-colombiaperiferias-04 b2-colombiaperiferias-05 b2-colombiaperiferias-consolidation b2-venezuelapetroleo-01 b2-venezuelapetroleo-02 b2-venezuelapetroleo-03 b2-venezuelapetroleo-04 b2-venezuelapetroleo-05 b2-venezuelapetroleo-consolidation b2-venezuelasabana-01 b2-venezuelasabana-02 b2-venezuelasabana-03 b2-venezuelasabana-04 b2-venezuelasabana-05 b2-venezuelasabana-consolidation

## Method (2026-11-25)

As batch 5–10: three units per agent, all six units topic-only (one known skill per lesson, from
`notes.md`). Present-day facts searched before launch and written into the unit notes
(Venezuela after 3 January 2026, Colombia's 2026 election, R4V figures). Briefs = `unit-<x>.txt`
+ `scripts/templates/edit-spanish-latam-b2-track.txt`.

## Agents (edit-in-place, Sonnet), started 07:17 UTC on 9dd0bd98

- A (Latin America Units 11, 12, 13; /home/user/parlour-read-a): agent a1848106ba02db261
- B (Latin America Units 14, 15, 16; /home/user/parlour-read-b): agent a214e82b2823f9307

Resume a stopped agent with SendMessage to its id; never start a new one.
