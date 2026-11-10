# hu B2 batch: hu-b2-batch-cult-66-72

Started 2026-11-10T22:03:48Z from origin/master b1355083. 2 Sonnet reader(s).

- Reader A: Unit 66 political-thought (b2-eszmetortenet-01 b2-eszmetortenet-02 b2-eszmetortenet-03 b2-eszmetortenet-04 b2-eszmetortenet-05 b2-eszmetortenet-consolidation; stories ['b2-eszmetortenet-01-szechenyi', 'b2-eszmetortenet-02-eotvosjozsef', 'b2-eszmetortenet-03-polanyitestverek', 'b2-eszmetortenet-04-biboistvan', 'b2-eszmetortenet-05-klasszikusokma']); Unit 68 youth-culture (b2-ifjusagikultura-01 b2-ifjusagikultura-02 b2-ifjusagikultura-03 b2-ifjusagikultura-04 b2-ifjusagikultura-05 b2-ifjusagikultura-consolidation; stories ['b2-ifjusagikultura-01-beatkorszak', 'b2-ifjusagikultura-02-tanchazmozgalom', 'b2-ifjusagikultura-03-nyolcvanasevekunderground', 'b2-ifjusagikultura-04-szigetfesztival', 'b2-ifjusagikultura-05-digitalisszleng'])
- Reader B: Unit 70 knowledge-economy (b2-tudomanyjovo-01 b2-tudomanyjovo-02 b2-tudomanyjovo-03 b2-tudomanyjovo-04 b2-tudomanyjovo-05 b2-tudomanyjovo-consolidation; stories ['b2-tudomanyjovo-01-krauszferenc', 'b2-tudomanyjovo-02-elialpsszeged', 'b2-tudomanyjovo-03-magyarmestintelligencia', 'b2-tudomanyjovo-04-zoldenergia', 'b2-tudomanyjovo-05-kozepesnyelvekjovoje']); Unit 72 speaking-hungarian-today (b2-magyaridentitas-01 b2-magyaridentitas-02 b2-magyaridentitas-03 b2-magyaridentitas-04 b2-magyaridentitas-05 b2-magyaridentitas-consolidation; stories ['b2-magyaridentitas-01-finnugorgyokerek', 'b2-magyaridentitas-02-koltokhivatasa', 'b2-magyaridentitas-03-humoresmelankolia', 'b2-magyaridentitas-04-belsopisztaszemmel', 'b2-magyaridentitas-05-utac1fele'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 66 political-thought | culture | 11 / 0 |
| 68 youth-culture | culture | 8 / 0 |
| 70 knowledge-economy | culture | 5 / 2 |
| 72 speaking-hungarian-today | culture | 12 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-eszmetortenet-01 b2-eszmetortenet-02 b2-eszmetortenet-03 b2-eszmetortenet-04 b2-eszmetortenet-05 b2-eszmetortenet-consolidation b2-ifjusagikultura-01 b2-ifjusagikultura-02 b2-ifjusagikultura-03 b2-ifjusagikultura-04 b2-ifjusagikultura-05 b2-ifjusagikultura-consolidation b2-tudomanyjovo-01 b2-tudomanyjovo-02 b2-tudomanyjovo-03 b2-tudomanyjovo-04 b2-tudomanyjovo-05 b2-tudomanyjovo-consolidation b2-magyaridentitas-01 b2-magyaridentitas-02 b2-magyaridentitas-03 b2-magyaridentitas-04 b2-magyaridentitas-05 b2-magyaridentitas-consolidation
