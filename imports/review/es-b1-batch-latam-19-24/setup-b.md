# es B1 batch: es-b1-batch-latam-19-24

Started 2026-11-26T04:20:36Z from origin/master 9350caa3. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader B: B1 Latin America Unit 22 cold-war (b1-guerrafria-01 b1-guerrafria-02 b1-guerrafria-03 b1-guerrafria-04 b1-guerrafria-05 b1-guerrafria-consolidation; stories ['b1-guerrafria-01-dosbloques', 'b1-guerrafria-02-americalatina', 'b1-guerrafria-03-revolucionoanticomunismo', 'b1-guerrafria-04-intervencionextranjera', 'b1-guerrafria-05-continentedividido']); B1 Latin America Unit 23 united-states-latin-america (b1-eeuu-01 b1-eeuu-02 b1-eeuu-03 b1-eeuu-04 b1-eeuu-05 b1-eeuu-consolidation; stories ['b1-eeuu-01-vecinodelnorte', 'b1-eeuu-02-intervenciones', 'b1-eeuu-03-economiaydependencia', 'b1-eeuu-04-alianzaparaelprogreso', 'b1-eeuu-05-unarelacioncompleja']); B1 Latin America Unit 24 military-governments (b1-gobiernosmilitares-01 b1-gobiernosmilitares-02 b1-gobiernosmilitares-03 b1-gobiernosmilitares-04 b1-gobiernosmilitares-05 b1-gobiernosmilitares-consolidation; stories ['b1-gobiernosmilitares-01-losgolpesdeestado', 'b1-gobiernosmilitares-02-brasil', 'b1-gobiernosmilitares-03-chile', 'b1-gobiernosmilitares-04-argentina', 'b1-gobiernosmilitares-05-elpodermilitar'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 22 cold-war | latam | 20 / 2 |
| B1 Latin America Unit 23 united-states-latin-america | latam | 33 / 0 |
| B1 Latin America Unit 24 military-governments | latam | 27 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-guerrafria-01 b1-guerrafria-02 b1-guerrafria-03 b1-guerrafria-04 b1-guerrafria-05 b1-guerrafria-consolidation b1-eeuu-01 b1-eeuu-02 b1-eeuu-03 b1-eeuu-04 b1-eeuu-05 b1-eeuu-consolidation b1-gobiernosmilitares-01 b1-gobiernosmilitares-02 b1-gobiernosmilitares-03 b1-gobiernosmilitares-04 b1-gobiernosmilitares-05 b1-gobiernosmilitares-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- B (Latin America Units 22–24; /home/user/parlour-read-b)
