# es B1 batch: es-b1-batch-latam-25-30

Started 2026-11-26T09:48:54Z from origin/master c8149f92. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader B: B1 Latin America Unit 28 debt-crisis (b1-crisisdeuda-01 b1-crisisdeuda-02 b1-crisisdeuda-03 b1-crisisdeuda-04 b1-crisisdeuda-05 b1-crisisdeuda-consolidation; stories ['b1-crisisdeuda-01-ladeudacrece', 'b1-crisisdeuda-02-lacrisisde1982', 'b1-crisisdeuda-03-austeridad', 'b1-crisisdeuda-04-elcostesocial', 'b1-crisisdeuda-05-unadecadaperdida']); B1 Latin America Unit 29 neoliberalism (b1-neoliberalismo-01 b1-neoliberalismo-02 b1-neoliberalismo-03 b1-neoliberalismo-04 b1-neoliberalismo-05 b1-neoliberalismo-consolidation; stories ['b1-neoliberalismo-01-lasideasneoliberales', 'b1-neoliberalismo-02-privatizacion', 'b1-neoliberalismo-03-elmercadoyelestado', 'b1-neoliberalismo-04-desigualdadypobreza', 'b1-neoliberalismo-05-ellegadoneoliberal']); B1 Latin America Unit 30 democratization (b1-democratizacion-01 b1-democratizacion-02 b1-democratizacion-03 b1-democratizacion-04 b1-democratizacion-05 b1-democratizacion-consolidation; stories ['b1-democratizacion-01-volveravotar', 'b1-democratizacion-02-nuevasinstituciones', 'b1-democratizacion-03-democraciayjusticia', 'b1-democratizacion-04-lasdificultadesdelatransicion', 'b1-democratizacion-05-democraciasimperfectas'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 28 debt-crisis | latam | 11 / 1 |
| B1 Latin America Unit 29 neoliberalism | latam | 27 / 0 |
| B1 Latin America Unit 30 democratization | latam | 25 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-crisisdeuda-01 b1-crisisdeuda-02 b1-crisisdeuda-03 b1-crisisdeuda-04 b1-crisisdeuda-05 b1-crisisdeuda-consolidation b1-neoliberalismo-01 b1-neoliberalismo-02 b1-neoliberalismo-03 b1-neoliberalismo-04 b1-neoliberalismo-05 b1-neoliberalismo-consolidation b1-democratizacion-01 b1-democratizacion-02 b1-democratizacion-03 b1-democratizacion-04 b1-democratizacion-05 b1-democratizacion-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- B (Latin America Units 28–30; /home/user/parlour-read-b)
