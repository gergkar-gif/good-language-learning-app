# es B1 batch: es-b1-batch-latam-31-36

Started 2026-11-26T10:03:18Z from origin/master 2f01f1c7. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 31 indigenous-movements (b1-movimientosindigenas-01 b1-movimientosindigenas-02 b1-movimientosindigenas-03 b1-movimientosindigenas-04 b1-movimientosindigenas-05 b1-movimientosindigenas-consolidation; stories ['b1-movimientosindigenas-01-pueblosindigenas', 'b1-movimientosindigenas-02-tierraderechos', 'b1-movimientosindigenas-03-identidadyreconocimiento', 'b1-movimientosindigenas-04-movilizacionpolitica', 'b1-movimientosindigenas-05-nuevasvoces']); B1 Latin America Unit 32 regional-integration (b1-integracionregional-01 b1-integracionregional-02 b1-integracionregional-03 b1-integracionregional-04 b1-integracionregional-05 b1-integracionregional-consolidation; stories ['b1-integracionregional-01-porqueintegrarse', 'b1-integracionregional-02-mercosur', 'b1-integracionregional-03-comunidadandina', 'b1-integracionregional-04-comercioycooperacion', 'b1-integracionregional-05-unaregionunida']); B1 Latin America Unit 33 end-cold-war (b1-finalguerrafria-01 b1-finalguerrafria-02 b1-finalguerrafria-03 b1-finalguerrafria-04 b1-finalguerrafria-05 b1-finalguerrafria-consolidation; stories ['b1-finalguerrafria-01-1989', 'b1-finalguerrafria-02-unnuevomundo', 'b1-finalguerrafria-03-nuevasprioridades', 'b1-finalguerrafria-04-americalatinadespuesdelaguerrafria', 'b1-finalguerrafria-05-haciaanosnoventa'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 31 indigenous-movements | latam | 31 / 0 |
| B1 Latin America Unit 32 regional-integration | latam | 20 / 0 |
| B1 Latin America Unit 33 end-cold-war | latam | 13 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-movimientosindigenas-01 b1-movimientosindigenas-02 b1-movimientosindigenas-03 b1-movimientosindigenas-04 b1-movimientosindigenas-05 b1-movimientosindigenas-consolidation b1-integracionregional-01 b1-integracionregional-02 b1-integracionregional-03 b1-integracionregional-04 b1-integracionregional-05 b1-integracionregional-consolidation b1-finalguerrafria-01 b1-finalguerrafria-02 b1-finalguerrafria-03 b1-finalguerrafria-04 b1-finalguerrafria-05 b1-finalguerrafria-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- A (Latin America Units 31–33; /home/user/parlour-read-a)
