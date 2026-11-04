# hu B2 batch: hu-b2-batch-cult-10-16

Started 2026-11-04T22:45:14Z from origin/master 0ce99963. 2 Sonnet reader(s).

- Reader A: Unit 10 bartok-kodaly (b2-bartokkodaly-01 b2-bartokkodaly-02 b2-bartokkodaly-03 b2-bartokkodaly-04 b2-bartokkodaly-05 b2-bartokkodaly-consolidation; stories ['b2-bartokkodaly-01-fonografhenger', 'b2-bartokkodaly-02-pentatonnepdal', 'b2-bartokkodaly-03-bartokmodernizmus', 'b2-bartokkodaly-04-kodalymodszer', 'b2-bartokkodaly-05-tanchazmozgalom']); Unit 12 visual-arts-modernism (b2-festeszet-01 b2-festeszet-02 b2-festeszet-03 b2-festeszet-04 b2-festeszet-05 b2-festeszet-consolidation; stories ['b2-festeszet-01-munkacsy', 'b2-festeszet-02-nagybanya', 'b2-festeszet-03-csontvary', 'b2-festeszet-04-moholynagy', 'b2-festeszet-05-szepmuveszeti'])
- Reader B: Unit 14 the-martians (b2-marslakok-01 b2-marslakok-02 b2-marslakok-03 b2-marslakok-04 b2-marslakok-05 b2-marslakok-consolidation; stories ['b2-marslakok-01-kikvoltakamarslakok', 'b2-marslakok-02-neumannjanos', 'b2-marslakok-03-szilardleo', 'b2-marslakok-04-wignerkarman', 'b2-marslakok-05-budapestititok']); Unit 16 medical-pioneers (b2-semmelweis-01 b2-semmelweis-02 b2-semmelweis-03 b2-semmelweis-04 b2-semmelweis-05 b2-semmelweis-consolidation; stories ['b2-semmelweis-01-gyermekagyilaz', 'b2-semmelweis-02-szakmaiellenallas', 'b2-semmelweis-03-szentgyorgyiszeged', 'b2-semmelweis-04-karikokatalin', 'b2-semmelweis-05-orvosietika'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 10 bartok-kodaly | culture | 7 / 0 |
| 12 visual-arts-modernism | culture | 7 / 0 |
| 14 the-martians | culture | 14 / 4 |
| 16 medical-pioneers | culture | 7 / 4 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-bartokkodaly-01 b2-bartokkodaly-02 b2-bartokkodaly-03 b2-bartokkodaly-04 b2-bartokkodaly-05 b2-bartokkodaly-consolidation b2-festeszet-01 b2-festeszet-02 b2-festeszet-03 b2-festeszet-04 b2-festeszet-05 b2-festeszet-consolidation b2-marslakok-01 b2-marslakok-02 b2-marslakok-03 b2-marslakok-04 b2-marslakok-05 b2-marslakok-consolidation b2-semmelweis-01 b2-semmelweis-02 b2-semmelweis-03 b2-semmelweis-04 b2-semmelweis-05 b2-semmelweis-consolidation
