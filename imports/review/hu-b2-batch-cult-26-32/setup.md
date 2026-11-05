# hu B2 batch: hu-b2-batch-cult-26-32

Started 2026-11-05T06:03:19Z from origin/master dd087d2f. 2 Sonnet reader(s).

- Reader A: Unit 26 pesti-humor (b2-pestihumor-01 b2-pestihumor-02 b2-pestihumor-03 b2-pestihumor-04 b2-pestihumor-05 b2-pestihumor-consolidation; stories ['b2-pestihumor-01-nagyendre', 'b2-pestihumor-02-tulniatortenelmet', 'b2-pestihumor-03-hofigeza', 'b2-pestihumor-04-szatirikussajto', 'b2-pestihumor-05-onironia']); Unit 28 hungarian-cinema (b2-magyarfilm-01 b2-magyarfilm-02 b2-magyarfilm-03 b2-magyarfilm-04 b2-magyarfilm-05 b2-magyarfilm-consolidation; stories ['b2-magyarfilm-01-hollywoodialapitok', 'b2-magyarfilm-02-jancsomiklos', 'b2-magyarfilm-03-szaboistvan', 'b2-magyarfilm-04-meszarostarr', 'b2-magyarfilm-05-kortarsmagyarfilm'])
- Reader B: Unit 30 three-ts-censorship (b2-szamizdat-01 b2-szamizdat-02 b2-szamizdat-03 b2-szamizdat-04 b2-szamizdat-05 b2-szamizdat-consolidation; stories ['b2-szamizdat-01-haromt', 'b2-szamizdat-02-alkudozas', 'b2-szamizdat-03-viragnyelv', 'b2-szamizdat-04-szamizdatnyomda', 'b2-szamizdat-05-beszelofolyoirat']); Unit 32 urbanists-populists (b2-urbanusnepi-01 b2-urbanusnepi-02 b2-urbanusnepi-03 b2-urbanusnepi-04 b2-urbanusnepi-05 b2-urbanusnepi-consolidation; stories ['b2-urbanusnepi-01-falukutatok', 'b2-urbanusnepi-02-urbanusok', 'b2-urbanusnepi-03-vitapontok', 'b2-urbanusnepi-04-monoritalalkozo', 'b2-urbanusnepi-05-modernvisszhangok'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 26 pesti-humor | culture | 13 / 2 |
| 28 hungarian-cinema | culture | 9 / 6 |
| 30 three-ts-censorship | culture | 10 / 4 |
| 32 urbanists-populists | culture | 11 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-pestihumor-01 b2-pestihumor-02 b2-pestihumor-03 b2-pestihumor-04 b2-pestihumor-05 b2-pestihumor-consolidation b2-magyarfilm-01 b2-magyarfilm-02 b2-magyarfilm-03 b2-magyarfilm-04 b2-magyarfilm-05 b2-magyarfilm-consolidation b2-szamizdat-01 b2-szamizdat-02 b2-szamizdat-03 b2-szamizdat-04 b2-szamizdat-05 b2-szamizdat-consolidation b2-urbanusnepi-01 b2-urbanusnepi-02 b2-urbanusnepi-03 b2-urbanusnepi-04 b2-urbanusnepi-05 b2-urbanusnepi-consolidation
