# hu B2 batch: hu-b2-batch-cult-34-40

Started 2026-11-05T11:10:59Z from origin/master b92d0904. 2 Sonnet reader(s).

- Reader A: Unit 34 public-sphere-history (b2-mediatortenet-01 b2-mediatortenet-02 b2-mediatortenet-03 b2-mediatortenet-04 b2-mediatortenet-05 b2-mediatortenet-consolidation; stories ['b2-mediatortenet-01-pestihirlap', 'b2-mediatortenet-02-telefonhirmondo', 'b2-mediatortenet-03-radiotelevizio', 'b2-mediatortenet-04-mediapiac1989', 'b2-mediatortenet-05-digitalisnyilvanossag']); Unit 36 monuments-political-memory (b2-politikairetorika-01 b2-politikairetorika-02 b2-politikairetorika-03 b2-politikairetorika-04 b2-politikairetorika-05 b2-politikairetorika-consolidation; stories ['b2-politikairetorika-01-hosoktere', 'b2-politikairetorika-02-utcanevek', 'b2-politikairetorika-03-szoborpark', 'b2-politikairetorika-04-szonoklattortenet', 'b2-politikairetorika-05-emlekezetpolitika'])
- Reader B: Unit 38 regional-identities (b2-tajegysegek-01 b2-tajegysegek-02 b2-tajegysegek-03 b2-tajegysegek-04 b2-tajegysegek-05 b2-tajegysegek-consolidation; stories ['b2-tajegysegek-01-dunantulalfold', 'b2-tajegysegek-02-debrecencivis', 'b2-tajegysegek-03-pannoniaoroksege', 'b2-tajegysegek-04-vizfejvita', 'b2-tajegysegek-05-tajegyszellem']); Unit 40 village-change (b2-falutortenet-01 b2-falutortenet-02 b2-falutortenet-03 b2-falutortenet-04 b2-falutortenet-05 b2-falutortenet-consolidation; stories ['b2-falutortenet-01-tanyavilag', 'b2-falutortenet-02-foldosztaskollektivizalas', 'b2-falutortenet-03-haztajigazdasag', 'b2-falutortenet-04-falvakatalakulasa', 'b2-falutortenet-05-ujvidekielet'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 34 public-sphere-history | culture | 5 / 0 |
| 36 monuments-political-memory | culture | 5 / 0 |
| 38 regional-identities | culture | 5 / 0 |
| 40 village-change | culture | 11 / 2 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-mediatortenet-01 b2-mediatortenet-02 b2-mediatortenet-03 b2-mediatortenet-04 b2-mediatortenet-05 b2-mediatortenet-consolidation b2-politikairetorika-01 b2-politikairetorika-02 b2-politikairetorika-03 b2-politikairetorika-04 b2-politikairetorika-05 b2-politikairetorika-consolidation b2-tajegysegek-01 b2-tajegysegek-02 b2-tajegysegek-03 b2-tajegysegek-04 b2-tajegysegek-05 b2-tajegysegek-consolidation b2-falutortenet-01 b2-falutortenet-02 b2-falutortenet-03 b2-falutortenet-04 b2-falutortenet-05 b2-falutortenet-consolidation
