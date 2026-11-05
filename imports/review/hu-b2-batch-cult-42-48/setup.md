# hu B2 batch: hu-b2-batch-cult-42-48

Started 2026-11-05T11:38:15Z from origin/master 6be5eb34. 2 Sonnet reader(s).

- Reader A: Unit 42 goulash-to-single-market (b2-gazdasagiatmenet-01 b2-gazdasagiatmenet-02 b2-gazdasagiatmenet-03 b2-gazdasagiatmenet-04 b2-gazdasagiatmenet-05 b2-gazdasagiatmenet-consolidation; stories ['b2-gazdasagiatmenet-01-hiperinflacio1946', 'b2-gazdasagiatmenet-02-ujgazdasagimechanizmus', 'b2-gazdasagiatmenet-03-privatizaciosokk', 'b2-gazdasagiatmenet-04-ipariiparagak', 'b2-gazdasagiatmenet-05-innovaciostorekvesek']); Unit 44 family-policy (b2-demografia-01 b2-demografia-02 b2-demografia-03 b2-demografia-04 b2-demografia-05 b2-demografia-consolidation; stories ['b2-demografia-01-ratkokorszak', 'b2-demografia-02-gyestortenet', 'b2-demografia-03-csaladpolitika', 'b2-demografia-04-gondoskodasidosekrol', 'b2-demografia-05-fiatalokjovoje'])
- Reader B: Unit 46 housing-estates-renewal (b2-lakhatas-01 b2-lakhatas-02 b2-lakhatas-03 b2-lakhatas-04 b2-lakhatas-05 b2-lakhatas-consolidation; stories ['b2-lakhatas-01-gangosberhaz', 'b2-lakhatas-02-wekerletelep', 'b2-lakhatas-03-lakotelepek', 'b2-lakhatas-04-romkocsmak', 'b2-lakhatas-05-varoseletjovoje']); Unit 48 danube-dams (b2-kornyezetpolitika-01 b2-kornyezetpolitika-02 b2-kornyezetpolitika-03 b2-kornyezetpolitika-04 b2-kornyezetpolitika-05 b2-kornyezetpolitika-consolidation; stories ['b2-kornyezetpolitika-01-folyoszabalyozas', 'b2-kornyezetpolitika-02-bosnagymarosvita', 'b2-kornyezetpolitika-03-dunakor1988', 'b2-kornyezetpolitika-04-balatontiszavedelme', 'b2-kornyezetpolitika-05-alfoldivizgazdalkodas'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 42 goulash-to-single-market | culture | 5 / 0 |
| 44 family-policy | culture | 10 / 0 |
| 46 housing-estates-renewal | culture | 15 / 0 |
| 48 danube-dams | culture | 16 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-gazdasagiatmenet-01 b2-gazdasagiatmenet-02 b2-gazdasagiatmenet-03 b2-gazdasagiatmenet-04 b2-gazdasagiatmenet-05 b2-gazdasagiatmenet-consolidation b2-demografia-01 b2-demografia-02 b2-demografia-03 b2-demografia-04 b2-demografia-05 b2-demografia-consolidation b2-lakhatas-01 b2-lakhatas-02 b2-lakhatas-03 b2-lakhatas-04 b2-lakhatas-05 b2-lakhatas-consolidation b2-kornyezetpolitika-01 b2-kornyezetpolitika-02 b2-kornyezetpolitika-03 b2-kornyezetpolitika-04 b2-kornyezetpolitika-05 b2-kornyezetpolitika-consolidation
