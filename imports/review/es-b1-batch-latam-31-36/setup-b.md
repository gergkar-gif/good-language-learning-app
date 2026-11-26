# es B1 batch: es-b1-batch-latam-31-36

Started 2026-11-26T10:17:51Z from origin/master 8b2f7c4f. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader B: B1 Latin America Unit 34 latin-america-1990s (b1-latamnoventa-01 b1-latamnoventa-02 b1-latamnoventa-03 b1-latamnoventa-04 b1-latamnoventa-05 b1-latamnoventa-consolidation; stories ['b1-latamnoventa-01-losanosdemenem', 'b1-latamnoventa-02-fujimoriyperu', 'b1-latamnoventa-03-mexicoyeltlcan', 'b1-latamnoventa-04-democraciaymercado', 'b1-latamnoventa-05-unadecadadecontrastes']); B1 Latin America Unit 35 legacy-20th-century (b1-legadosigloveinte-01 b1-legadosigloveinte-02 b1-legadosigloveinte-03 b1-legadosigloveinte-04 b1-legadosigloveinte-05 b1-legadosigloveinte-consolidation; stories ['b1-legadosigloveinte-01-revolucionyreforma', 'b1-legadosigloveinte-02-dictaduraydemocracia', 'b1-legadosigloveinte-03-desigualdadydesarrollo', 'b1-legadosigloveinte-04-identidadymemoria', 'b1-legadosigloveinte-05-quedejoelsigloxx']); B1 Latin America Unit 36 latin-america-toward-2000 (b1-americalatinadosmil-01 b1-americalatinadosmil-02 b1-americalatinadosmil-03 b1-americalatinadosmil-04 b1-americalatinadosmil-05 b1-americalatinadosmil-consolidation; stories ['b1-americalatinadosmil-01-unaregiontransformada', 'b1-americalatinadosmil-02-politica', 'b1-americalatinadosmil-03-economiayglobalizacion', 'b1-americalatinadosmil-04-sociedadeidentidad', 'b1-americalatinadosmil-05-americalatinaalentrarenelnuevosiglo'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 34 latin-america-1990s | latam | 19 / 0 |
| B1 Latin America Unit 35 legacy-20th-century | latam | 22 / 0 |
| B1 Latin America Unit 36 latin-america-toward-2000 | latam | 17 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-latamnoventa-01 b1-latamnoventa-02 b1-latamnoventa-03 b1-latamnoventa-04 b1-latamnoventa-05 b1-latamnoventa-consolidation b1-legadosigloveinte-01 b1-legadosigloveinte-02 b1-legadosigloveinte-03 b1-legadosigloveinte-04 b1-legadosigloveinte-05 b1-legadosigloveinte-consolidation b1-americalatinadosmil-01 b1-americalatinadosmil-02 b1-americalatinadosmil-03 b1-americalatinadosmil-04 b1-americalatinadosmil-05 b1-americalatinadosmil-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 (rolling start)

- B (Latin America Units 34–36; /home/user/parlour-read-b)
