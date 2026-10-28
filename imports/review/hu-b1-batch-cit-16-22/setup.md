# es B1 batch: hu-b1-batch-cit-16-22

Started 2026-10-28T11:19:59Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 16 matthias-corvinus (b1-matyas-01 b1-matyas-02 b1-matyas-03 b1-matyas-04 b1-matyas-05 b1-matyas-consolidation; stories ['b1-matyas-01-megvalasztas', 'b1-matyas-02-feketesereg', 'b1-matyas-03-reneszanszudvar', 'b1-matyas-04-igazsagossag', 'b1-matyas-05-orokseg']); Unit 18 mohacs-1526 (b1-mohacs-01 b1-mohacs-02 b1-mohacs-03 b1-mohacs-04 b1-mohacs-05 b1-mohacs-consolidation; stories ['b1-mohacs-01-meggyengult', 'b1-mohacs-02-elorenyomulas', 'b1-mohacs-03-csata', 'b1-mohacs-04-kiralyhalala', 'b1-mohacs-05-fontossag'])
- Reader B: Unit 20 three-part-hungary (b1-haromresz-01 b1-haromresz-02 b1-haromresz-03 b1-haromresz-04 b1-haromresz-05 b1-haromresz-consolidation; stories ['b1-haromresz-01-kiralyi', 'b1-haromresz-02-hodoltsag', 'b1-haromresz-03-erdely', 'b1-haromresz-04-veghazak', 'b1-haromresz-05-megosztottsag']); Unit 22 transylvania-golden-age (b1-erdelyaranykora-01 b1-erdelyaranykora-02 b1-erdelyaranykora-03 b1-erdelyaranykora-04 b1-erdelyaranykora-05 b1-erdelyaranykora-consolidation; stories ['b1-erdelyaranykora-01-onallo', 'b1-erdelyaranykora-02-vallasbeke', 'b1-erdelyaranykora-03-bethlen', 'b1-erdelyaranykora-04-europa', 'b1-erdelyaranykora-05-hagyatek'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 16 matthias-corvinus | citizenship | 26 / 0 |
| 18 mohacs-1526 | citizenship | 23 / 0 |
| 20 three-part-hungary | citizenship | 12 / 0 |
| 22 transylvania-golden-age | citizenship | 19 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-matyas-01 b1-matyas-02 b1-matyas-03 b1-matyas-04 b1-matyas-05 b1-matyas-consolidation b1-mohacs-01 b1-mohacs-02 b1-mohacs-03 b1-mohacs-04 b1-mohacs-05 b1-mohacs-consolidation b1-haromresz-01 b1-haromresz-02 b1-haromresz-03 b1-haromresz-04 b1-haromresz-05 b1-haromresz-consolidation b1-erdelyaranykora-01 b1-erdelyaranykora-02 b1-erdelyaranykora-03 b1-erdelyaranykora-04 b1-erdelyaranykora-05 b1-erdelyaranykora-consolidation
