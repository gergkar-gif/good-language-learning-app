# es B1 batch: es-b1-batch-latam-07-12

Started 2026-11-26T00:30:30Z from origin/master 57527666. 1 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 7 race-class-power (b1-razaclasepoder-01 b1-razaclasepoder-02 b1-razaclasepoder-03 b1-razaclasepoder-04 b1-razaclasepoder-05 b1-razaclasepoder-consolidation; stories ['b1-razaclasepoder-01-castas', 'b1-razaclasepoder-02-elites', 'b1-razaclasepoder-03-posicion', 'b1-razaclasepoder-04-mestizaje', 'b1-razaclasepoder-05-herencias']); B1 Latin America Unit 8 independence (b1-independencia-01 b1-independencia-02 b1-independencia-03 b1-independencia-04 b1-independencia-05 b1-independencia-consolidation; stories ['b1-independencia-01-mundocambia', 'b1-independencia-02-guerras', 'b1-independencia-03-lideres', 'b1-independencia-04-republicas', 'b1-independencia-05-paraquien']); B1 Latin America Unit 9 new-republics (b1-nuevasrepublicas-01 b1-nuevasrepublicas-02 b1-nuevasrepublicas-03 b1-nuevasrepublicas-04 b1-nuevasrepublicas-05 b1-nuevasrepublicas-consolidation; stories ['b1-nuevasrepublicas-01-estado', 'b1-nuevasrepublicas-02-fronteras', 'b1-nuevasrepublicas-03-liberales', 'b1-nuevasrepublicas-04-inestabilidad', 'b1-nuevasrepublicas-05-desafios'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 7 race-class-power | latam | 36 / 0 |
| B1 Latin America Unit 8 independence | latam | 33 / 2 |
| B1 Latin America Unit 9 new-republics | latam | 31 / 3 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-razaclasepoder-01 b1-razaclasepoder-02 b1-razaclasepoder-03 b1-razaclasepoder-04 b1-razaclasepoder-05 b1-razaclasepoder-consolidation b1-independencia-01 b1-independencia-02 b1-independencia-03 b1-independencia-04 b1-independencia-05 b1-independencia-consolidation b1-nuevasrepublicas-01 b1-nuevasrepublicas-02 b1-nuevasrepublicas-03 b1-nuevasrepublicas-04 b1-nuevasrepublicas-05 b1-nuevasrepublicas-consolidation

## Agent (edit-in-place, Sonnet), started 2026-11-26 on 57527666

- A (Latin America Units 7–9; /home/user/parlour-read-a): agent afed7cf66af450231. Started as soon as
  Units 1–3 were frozen, while Reader B of batch 1–6 was still running (rolling start).
