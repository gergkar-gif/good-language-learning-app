# es B1 batch: es-b1-batch-latam-13-18

Started 2026-11-26T03:56:30Z from origin/master b117ca31. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader B: B1 Latin America Unit 16 mexican-revolution (b1-revolucionmexicana-01 b1-revolucionmexicana-02 b1-revolucionmexicana-03 b1-revolucionmexicana-04 b1-revolucionmexicana-05 b1-revolucionmexicana-consolidation; stories ['b1-revolucionmexicana-01-porfiriato', 'b1-revolucionmexicana-02-madero', 'b1-revolucionmexicana-03-zapatayvilla', 'b1-revolucionmexicana-04-constitucion', 'b1-revolucionmexicana-05-legado']); B1 Latin America Unit 17 nationalism-state (b1-nacionalismo-01 b1-nacionalismo-02 b1-nacionalismo-03 b1-nacionalismo-04 b1-nacionalismo-05 b1-nacionalismo-consolidation; stories ['b1-nacionalismo-01-estadosmasfuertes', 'b1-nacionalismo-02-cultural', 'b1-nacionalismo-03-educacion', 'b1-nacionalismo-04-poblaciones', 'b1-nacionalismo-05-estadomoderno']); B1 Latin America Unit 18 great-depression (b1-grandepresion-01 b1-grandepresion-02 b1-grandepresion-03 b1-grandepresion-04 b1-grandepresion-05 b1-grandepresion-consolidation; stories ['b1-grandepresion-01-crisis1929', 'b1-grandepresion-02-americalatina', 'b1-grandepresion-03-menoscomercio', 'b1-grandepresion-04-cambiarmodelo', 'b1-grandepresion-05-transformoregion'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 16 mexican-revolution | latam | 27 / 0 |
| B1 Latin America Unit 17 nationalism-state | latam | 21 / 2 |
| B1 Latin America Unit 18 great-depression | latam | 18 / 2 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-revolucionmexicana-01 b1-revolucionmexicana-02 b1-revolucionmexicana-03 b1-revolucionmexicana-04 b1-revolucionmexicana-05 b1-revolucionmexicana-consolidation b1-nacionalismo-01 b1-nacionalismo-02 b1-nacionalismo-03 b1-nacionalismo-04 b1-nacionalismo-05 b1-nacionalismo-consolidation b1-grandepresion-01 b1-grandepresion-02 b1-grandepresion-03 b1-grandepresion-04 b1-grandepresion-05 b1-grandepresion-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- B (Latin America Units 16–18; /home/user/parlour-read-b)
