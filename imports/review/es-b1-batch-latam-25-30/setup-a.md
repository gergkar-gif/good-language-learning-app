# es B1 batch: es-b1-batch-latam-25-30

Started 2026-11-26T09:36:40Z from origin/master 94f33795. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 25 political-repression (b1-represionpolitica-01 b1-represionpolitica-02 b1-represionpolitica-03 b1-represionpolitica-04 b1-represionpolitica-05 b1-represionpolitica-consolidation; stories ['b1-represionpolitica-01-elestadorepresivo', 'b1-represionpolitica-02-censurraypersecucion', 'b1-represionpolitica-03-desaparecidos', 'b1-represionpolitica-04-resistencia', 'b1-represionpolitica-05-memoriayjusticia']); B1 Latin America Unit 26 central-america-revolution-conflict (b1-centroamerica-01 b1-centroamerica-02 b1-centroamerica-03 b1-centroamerica-04 b1-centroamerica-05 b1-centroamerica-consolidation; stories ['b1-centroamerica-01-nicaragua', 'b1-centroamerica-02-elsalvador', 'b1-centroamerica-03-guatemala', 'b1-centroamerica-04-intervencionyguerrafria', 'b1-centroamerica-05-losacuerdosdepaz']); B1 Latin America Unit 27 southern-cone-dictatorships (b1-conosur-01 b1-conosur-02 b1-conosur-03 b1-conosur-04 b1-conosur-05 b1-conosur-consolidation; stories ['b1-conosur-01-chile', 'b1-conosur-02-argentina', 'b1-conosur-03-uruguay', 'b1-conosur-04-operacioncondor', 'b1-conosur-05-democraciaymemoria'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 25 political-repression | latam | 26 / 0 |
| B1 Latin America Unit 26 central-america-revolution-conflict | latam | 16 / 0 |
| B1 Latin America Unit 27 southern-cone-dictatorships | latam | 14 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-represionpolitica-01 b1-represionpolitica-02 b1-represionpolitica-03 b1-represionpolitica-04 b1-represionpolitica-05 b1-represionpolitica-consolidation b1-centroamerica-01 b1-centroamerica-02 b1-centroamerica-03 b1-centroamerica-04 b1-centroamerica-05 b1-centroamerica-consolidation b1-conosur-01 b1-conosur-02 b1-conosur-03 b1-conosur-04 b1-conosur-05 b1-conosur-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- A (Latin America Units 25–27; /home/user/parlour-read-a)
