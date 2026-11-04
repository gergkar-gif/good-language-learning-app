# hu B2 batch: hu-b2-batch-cult-02-08

Started 2026-11-04T15:41:03Z from origin/master 4c9f1f94. 2 Sonnet reader(s).

- Reader A: Unit 2 nyugat-coffeehouses (b2-kavehazikultura-01 b2-kavehazikultura-02 b2-kavehazikultura-03 b2-kavehazikultura-04 b2-kavehazikultura-05 b2-kavehazikultura-consolidation; stories ['b2-kavehazikultura-01-otszazkavehaz', 'b2-kavehazikultura-02-nyugatszuletese', 'b2-kavehazikultura-03-osvaterno', 'b2-kavehazikultura-04-modernistakvita', 'b2-kavehazikultura-05-kavehaziorokseg']); Unit 4 fin-de-siecle-budapest (b2-szecesszio-01 b2-szecesszio-02 b2-szecesszio-03 b2-szecesszio-04 b2-szecesszio-05 b2-szecesszio-consolidation; stories ['b2-szecesszio-01-egyesites', 'b2-szecesszio-02-lechnerodon', 'b2-szecesszio-03-zsolnaymaza', 'b2-szecesszio-04-korutakberhazak', 'b2-szecesszio-05-homlokzatok'])
- Reader B: Unit 6 language-reform (b2-nyelvujitas-01 b2-nyelvujitas-02 b2-nyelvujitas-03 b2-nyelvujitas-04 b2-nyelvujitas-05 b2-nyelvujitas-consolidation; stories ['b2-nyelvujitas-01-latinorszaggyules', 'b2-nyelvujitas-02-kazinczy', 'b2-nyelvujitas-03-ortologusneologus', 'b2-nyelvujitas-04-tizezerujszo', 'b2-nyelvujitas-05-allamnyelv1844']); Unit 8 national-theatre (b2-szinhazmuveszet-01 b2-szinhazmuveszet-02 b2-szinhazmuveszet-03 b2-szinhazmuveszet-04 b2-szinhazmuveszet-05 b2-szinhazmuveszet-consolidation; stories ['b2-szinhazmuveszet-01-nemzetiszinhaz', 'b2-szinhazmuveszet-02-bankbanszinhaz', 'b2-szinhazmuveszet-03-vigszinhaz', 'b2-szinhazmuveszet-04-operettvilag', 'b2-szinhazmuveszet-05-rendezoescenzor'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 2 nyugat-coffeehouses | culture | 7 / 7 |
| 4 fin-de-siecle-budapest | culture | 7 / 2 |
| 6 language-reform | culture | 6 / 3 |
| 8 national-theatre | culture | 6 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-kavehazikultura-01 b2-kavehazikultura-02 b2-kavehazikultura-03 b2-kavehazikultura-04 b2-kavehazikultura-05 b2-kavehazikultura-consolidation b2-szecesszio-01 b2-szecesszio-02 b2-szecesszio-03 b2-szecesszio-04 b2-szecesszio-05 b2-szecesszio-consolidation b2-nyelvujitas-01 b2-nyelvujitas-02 b2-nyelvujitas-03 b2-nyelvujitas-04 b2-nyelvujitas-05 b2-nyelvujitas-consolidation b2-szinhazmuveszet-01 b2-szinhazmuveszet-02 b2-szinhazmuveszet-03 b2-szinhazmuveszet-04 b2-szinhazmuveszet-05 b2-szinhazmuveszet-consolidation
