# hu B2 batch: hu-b2-batch-cult-18-24

Started 2026-11-04T23:49:54Z from origin/master 660a3b8d. 2 Sonnet reader(s).

- Reader A: Unit 18 mathematics-chess (b2-matematikasakk-01 b2-matematikasakk-02 b2-matematikasakk-03 b2-matematikasakk-04 b2-matematikasakk-05 b2-matematikasakk-consolidation; stories ['b2-matematikasakk-01-bolyaijanos', 'b2-matematikasakk-02-komalhagyomany', 'b2-matematikasakk-03-erdospal', 'b2-matematikasakk-04-polgarjudit', 'b2-matematikasakk-05-elvonttudomanyok']); Unit 20 elite-education (b2-gimnaziumok-01 b2-gimnaziumok-02 b2-gimnaziumok-03 b2-gimnaziumok-04 b2-gimnaziumok-05 b2-gimnaziumok-consolidation; stories ['b2-gimnaziumok-01-fasorigimnazium', 'b2-gimnaziumok-02-mintagimnazium', 'b2-gimnaziumok-03-eotvoscollegium', 'b2-gimnaziumok-04-iskolatipusok', 'b2-gimnaziumok-05-eselyegyenloseg'])
- Reader B: Unit 22 psychoanalysis (b2-pszichoanalizis-01 b2-pszichoanalizis-02 b2-pszichoanalizis-03 b2-pszichoanalizis-04 b2-pszichoanalizis-05 b2-pszichoanalizis-consolidation; stories ['b2-pszichoanalizis-01-ferenczisandor', 'b2-pszichoanalizis-02-koltokesanalitikusok', 'b2-pszichoanalizis-03-balintmihaly', 'b2-pszichoanalizis-04-ujjaszuletes1989', 'b2-pszichoanalizis-05-flowelmeny']); Unit 24 kempelen-to-rubik (b2-talalmanyok-01 b2-talalmanyok-02 b2-talalmanyok-03 b2-talalmanyok-04 b2-talalmanyok-05 b2-talalmanyok-consolidation; stories ['b2-talalmanyok-01-kempelenfarkas', 'b2-talalmanyok-02-jedlikganz', 'b2-talalmanyok-03-birolaszlo', 'b2-talalmanyok-04-gabordenes', 'b2-talalmanyok-05-rubikerno'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 18 mathematics-chess | culture | 12 / 4 |
| 20 elite-education | culture | 10 / 3 |
| 22 psychoanalysis | culture | 15 / 0 |
| 24 kempelen-to-rubik | culture | 7 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-matematikasakk-01 b2-matematikasakk-02 b2-matematikasakk-03 b2-matematikasakk-04 b2-matematikasakk-05 b2-matematikasakk-consolidation b2-gimnaziumok-01 b2-gimnaziumok-02 b2-gimnaziumok-03 b2-gimnaziumok-04 b2-gimnaziumok-05 b2-gimnaziumok-consolidation b2-pszichoanalizis-01 b2-pszichoanalizis-02 b2-pszichoanalizis-03 b2-pszichoanalizis-04 b2-pszichoanalizis-05 b2-pszichoanalizis-consolidation b2-talalmanyok-01 b2-talalmanyok-02 b2-talalmanyok-03 b2-talalmanyok-04 b2-talalmanyok-05 b2-talalmanyok-consolidation
