# es B1 batch: es-b1-batch-latam-13-18

Started 2026-11-26T03:52:44Z from origin/master 64020a18. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 13 export-economies (b1-economiasexportacion-01 b1-economiasexportacion-02 b1-economiasexportacion-03 b1-economiasexportacion-04 b1-economiasexportacion-05 b1-economiasexportacion-consolidation; stories ['b1-economiasexportacion-01-modelo', 'b1-economiasexportacion-02-productos', 'b1-economiasexportacion-03-ferrocarriles', 'b1-economiasexportacion-04-trabajo', 'b1-economiasexportacion-05-dependencia']); B1 Latin America Unit 14 social-change (b1-cambiosocial-01 b1-cambiosocial-02 b1-cambiosocial-03 b1-cambiosocial-04 b1-cambiosocial-05 b1-cambiosocial-consolidation; stories ['b1-cambiosocial-01-ciudades', 'b1-cambiosocial-02-clases', 'b1-cambiosocial-03-inmigracion', 'b1-cambiosocial-04-conflicto', 'b1-cambiosocial-05-transformacion']); B1 Latin America Unit 15 revolution (b1-revolucion-01 b1-revolucion-02 b1-revolucion-03 b1-revolucion-04 b1-revolucion-05 b1-revolucion-consolidation; stories ['b1-revolucion-01-quees', 'b1-revolucion-02-tierraypoder', 'b1-revolucion-03-trabajadores', 'b1-revolucion-04-estado', 'b1-revolucion-05-cuandocambia'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 13 export-economies | latam | 28 / 0 |
| B1 Latin America Unit 14 social-change | latam | 29 / 2 |
| B1 Latin America Unit 15 revolution | latam | 29 / 3 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-economiasexportacion-01 b1-economiasexportacion-02 b1-economiasexportacion-03 b1-economiasexportacion-04 b1-economiasexportacion-05 b1-economiasexportacion-consolidation b1-cambiosocial-01 b1-cambiosocial-02 b1-cambiosocial-03 b1-cambiosocial-04 b1-cambiosocial-05 b1-cambiosocial-consolidation b1-revolucion-01 b1-revolucion-02 b1-revolucion-03 b1-revolucion-04 b1-revolucion-05 b1-revolucion-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- A (Latin America Units 13–15; /home/user/parlour-read-a)
