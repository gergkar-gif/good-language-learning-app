# es B1 batch: es-b1-batch-latam-19-24

Started 2026-11-26T04:11:55Z from origin/master ff3b8c37. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 19 populism (b1-populismo-01 b1-populismo-02 b1-populismo-03 b1-populismo-04 b1-populismo-05 b1-populismo-consolidation; stories ['b1-populismo-01-quees', 'b1-populismo-02-peron', 'b1-populismo-03-cardenas', 'b1-populismo-04-puebloylider', 'b1-populismo-05-legado']); B1 Latin America Unit 20 industrialization (b1-industrializacion-01 b1-industrializacion-02 b1-industrializacion-03 b1-industrializacion-04 b1-industrializacion-05 b1-industrializacion-consolidation; stories ['b1-industrializacion-01-producirencasa', 'b1-industrializacion-02-nuevasindustrias', 'b1-industrializacion-03-migracion', 'b1-industrializacion-04-sociedadesurbanas', 'b1-industrializacion-05-continenteindustrial']); B1 Latin America Unit 21 cuban-revolution (b1-revolucioncubana-01 b1-revolucioncubana-02 b1-revolucioncubana-03 b1-revolucioncubana-04 b1-revolucioncubana-05 b1-revolucioncubana-consolidation; stories ['b1-revolucioncubana-01-cubaantes', 'b1-revolucioncubana-02-fidelcastro', 'b1-revolucioncubana-03-socialista', 'b1-revolucioncubana-04-bahiacochinos', 'b1-revolucioncubana-05-cubayamericalatina'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 19 populism | latam | 27 / 1 |
| B1 Latin America Unit 20 industrialization | latam | 23 / 2 |
| B1 Latin America Unit 21 cuban-revolution | latam | 23 / 1 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-populismo-01 b1-populismo-02 b1-populismo-03 b1-populismo-04 b1-populismo-05 b1-populismo-consolidation b1-industrializacion-01 b1-industrializacion-02 b1-industrializacion-03 b1-industrializacion-04 b1-industrializacion-05 b1-industrializacion-consolidation b1-revolucioncubana-01 b1-revolucioncubana-02 b1-revolucioncubana-03 b1-revolucioncubana-04 b1-revolucioncubana-05 b1-revolucioncubana-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- A (Latin America Units 19–21; /home/user/parlour-read-a)
