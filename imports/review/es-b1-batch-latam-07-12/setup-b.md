# es B1 batch: es-b1-batch-latam-07-12

Started 2026-11-26T00:34:26Z from origin/master 1bafd85a. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader B: B1 Latin America Unit 10 caudillismo (b1-caudillismo-01 b1-caudillismo-02 b1-caudillismo-03 b1-caudillismo-04 b1-caudillismo-05 b1-caudillismo-consolidation; stories ['b1-caudillismo-01-caudillo', 'b1-caudillismo-02-poderpersonal', 'b1-caudillismo-03-ejercitopolitica', 'b1-caudillismo-04-ordeninestabilidad', 'b1-caudillismo-05-legado']); B1 Latin America Unit 11 nation-nationalism (b1-nacionnacionalismo-01 b1-nacionnacionalismo-02 b1-nacionnacionalismo-03 b1-nacionnacionalismo-04 b1-nacionnacionalismo-05 b1-nacionnacionalismo-consolidation; stories ['b1-nacionnacionalismo-01-nacion', 'b1-nacionnacionalismo-02-simbolos', 'b1-nacionnacionalismo-03-identidad', 'b1-nacionnacionalismo-04-pueblosfronteras', 'b1-nacionnacionalismo-05-imaginarnacion']); B1 Latin America Unit 12 liberalism-modernization (b1-liberalismomodernizacion-01 b1-liberalismomodernizacion-02 b1-liberalismomodernizacion-03 b1-liberalismomodernizacion-04 b1-liberalismomodernizacion-05 b1-liberalismomodernizacion-consolidation; stories ['b1-liberalismomodernizacion-01-ideas', 'b1-liberalismomodernizacion-02-reformar', 'b1-liberalismomodernizacion-03-iglesiayestado', 'b1-liberalismomodernizacion-04-modernizar', 'b1-liberalismomodernizacion-05-nuevomodelo'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 10 caudillismo | latam | 35 / 3 |
| B1 Latin America Unit 11 nation-nationalism | latam | 36 / 0 |
| B1 Latin America Unit 12 liberalism-modernization | latam | 23 / 1 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-caudillismo-01 b1-caudillismo-02 b1-caudillismo-03 b1-caudillismo-04 b1-caudillismo-05 b1-caudillismo-consolidation b1-nacionnacionalismo-01 b1-nacionnacionalismo-02 b1-nacionnacionalismo-03 b1-nacionnacionalismo-04 b1-nacionnacionalismo-05 b1-nacionnacionalismo-consolidation b1-liberalismomodernizacion-01 b1-liberalismomodernizacion-02 b1-liberalismomodernizacion-03 b1-liberalismomodernizacion-04 b1-liberalismomodernizacion-05 b1-liberalismomodernizacion-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 on 1bafd85a

- B (Latin America Units 10–12; /home/user/parlour-read-b): agent a41ef6faa09aa64c9 (rolling start).
