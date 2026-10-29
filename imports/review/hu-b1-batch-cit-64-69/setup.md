# es B1 batch: hu-b1-batch-cit-64-69

Started 2026-10-29T13:14:16Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 64 government-institutions-today (b1-allamszervezet-01 b1-allamszervezet-02 b1-allamszervezet-03 b1-allamszervezet-04 b1-allamszervezet-05 b1-allamszervezet-consolidation; stories ['b1-allamszervezet-01-orszaggyules', 'b1-allamszervezet-02-elnok', 'b1-allamszervezet-03-kormany', 'b1-allamszervezet-04-birosagok', 'b1-allamszervezet-05-torvenyhozas', 'b1-allamszervezet']); Unit 66 local-governments-public-administration (b1-onkormanyzat-01 b1-onkormanyzat-02 b1-onkormanyzat-03 b1-onkormanyzat-04 b1-onkormanyzat-05 b1-onkormanyzat-consolidation; stories ['b1-onkormanyzat-01-onkormanyzatok', 'b1-onkormanyzat-02-polgarmester', 'b1-onkormanyzat-03-varmegyek', 'b1-onkormanyzat-04-kormanyablak', 'b1-onkormanyzat-05-kozszolgaltatas', 'b1-onkormanyzat'])
- Reader B: Unit 68 hungarian-culture-science-heritage (b1-nemzetiertekek-01 b1-nemzetiertekek-02 b1-nemzetiertekek-03 b1-nemzetiertekek-04 b1-nemzetiertekek-05 b1-nemzetiertekek-consolidation; stories ['b1-nemzetiertekek-01-tudomany', 'b1-nemzetiertekek-02-talalmanyok', 'b1-nemzetiertekek-03-zene', 'b1-nemzetiertekek-04-irodalom', 'b1-nemzetiertekek-05-hungarikumok', 'b1-nemzetiertekek']); Unit 69 literary-musical-canon (b1-europaiorokseg-01 b1-europaiorokseg-02 b1-europaiorokseg-03 b1-europaiorokseg-04 b1-europaiorokseg-05 b1-europaiorokseg-consolidation; stories ['b1-europaiorokseg-01-antik', 'b1-europaiorokseg-02-regeny', 'b1-europaiorokseg-03-zene', 'b1-europaiorokseg-04-klasszikus', 'b1-europaiorokseg-05-modern', 'b1-europaiorokseg'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 64 government-institutions-today | citizenship | 6 / 9 |
| 66 local-governments-public-administration | citizenship | 9 / 4 |
| 68 hungarian-culture-science-heritage | citizenship | 4 / 4 |
| 69 literary-musical-canon | citizenship | 2 / 10 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-allamszervezet-01 b1-allamszervezet-02 b1-allamszervezet-03 b1-allamszervezet-04 b1-allamszervezet-05 b1-allamszervezet-consolidation b1-onkormanyzat-01 b1-onkormanyzat-02 b1-onkormanyzat-03 b1-onkormanyzat-04 b1-onkormanyzat-05 b1-onkormanyzat-consolidation b1-nemzetiertekek-01 b1-nemzetiertekek-02 b1-nemzetiertekek-03 b1-nemzetiertekek-04 b1-nemzetiertekek-05 b1-nemzetiertekek-consolidation b1-europaiorokseg-01 b1-europaiorokseg-02 b1-europaiorokseg-03 b1-europaiorokseg-04 b1-europaiorokseg-05 b1-europaiorokseg-consolidation
