# hu C1 batch: hu-c1-batch-cult-18-32

Started 2026-11-18T01:57:38Z from origin/master 73c06cb7. 2 Sonnet reader(s).

- Reader A: C1 Culture Unit 9 patient-rights (c1-bioetika-01 c1-bioetika-02 c1-bioetika-03 c1-bioetika-04 c1-bioetika-05 c1-bioetika-consolidation; stories ['c1-bioetika-01-genszerkesztes', 'c1-bioetika-02-transzplantacio', 'c1-bioetika-03-embriokutatas', 'c1-bioetika-04-karsaidaniel', 'c1-bioetika-05-mestersegesintelligencia']); C1 Culture Unit 10 corporate-law (c1-szerzodesek-01 c1-szerzodesek-02 c1-szerzodesek-03 c1-szerzodesek-04 c1-szerzodesek-05 c1-szerzodesek-consolidation; stories ['c1-szerzodesek-01-cegfelvasarlas', 'c1-szerzodesek-02-kockazatitoke', 'c1-szerzodesek-03-versenyjog', 'c1-szerzodesek-04-kozbeszerzes', 'c1-szerzodesek-05-nemzetkozimaganjog']); C1 Culture Unit 11 minority-protections (c1-emberijogok-01 c1-emberijogok-02 c1-emberijogok-03 c1-emberijogok-04 c1-emberijogok-05 c1-emberijogok-consolidation; stories ['c1-emberijogok-01-strasbourg', 'c1-emberijogok-02-nyelvikarta', 'c1-emberijogok-03-szegregacio', 'c1-emberijogok-04-fogyatekossagjogok', 'c1-emberijogok-05-parisprinciples']); C1 Culture Unit 12 civil-disobedience (c1-polgariengedetlenseg-01 c1-polgariengedetlenseg-02 c1-polgariengedetlenseg-03 c1-polgariengedetlenseg-04 c1-polgariengedetlenseg-05 c1-polgariengedetlenseg-consolidation; stories ['c1-polgariengedetlenseg-01-deak', 'c1-polgariengedetlenseg-02-szamizdat', 'c1-polgariengedetlenseg-03-taxisblokad', 'c1-polgariengedetlenseg-04-tanarok', 'c1-polgariengedetlenseg-05-dworkin'])
- Reader B: C1 Culture Unit 13 forint-eurozone (c1-monetaris-01 c1-monetaris-02 c1-monetaris-03 c1-monetaris-04 c1-monetaris-05 c1-monetaris-consolidation; stories ['c1-monetaris-01-pengo', 'c1-monetaris-02-bokros', 'c1-monetaris-03-savszel', 'c1-monetaris-04-devizahitel', 'c1-monetaris-05-eurodilemma']); C1 Culture Unit 14 paks-nuclear (c1-energetika-01 c1-energetika-02 c1-energetika-03 c1-energetika-04 c1-energetika-05 c1-energetika-consolidation; stories ['c1-energetika-01-paks1', 'c1-energetika-02-paks2', 'c1-energetika-03-bosnagymaros', 'c1-energetika-04-geotermia', 'c1-energetika-05-napenergia']); C1 Culture Unit 15 ai-ethics (c1-mestersegesintelligencia-01 c1-mestersegesintelligencia-02 c1-mestersegesintelligencia-03 c1-mestersegesintelligencia-04 c1-mestersegesintelligencia-05 c1-mestersegesintelligencia-consolidation; stories ['c1-mestersegesintelligencia-01-alapmodellek', 'c1-mestersegesintelligencia-02-etika', 'c1-mestersegesintelligencia-03-automatizacio', 'c1-mestersegesintelligencia-04-orvoslas', 'c1-mestersegesintelligencia-05-jovo']); C1 Culture Unit 16 media-pluralism (c1-mediakritika-01 c1-mediakritika-02 c1-mediakritika-03 c1-mediakritika-04 c1-mediakritika-05 c1-mediakritika-consolidation; stories ['c1-mediakritika-01-pluralizmus', 'c1-mediakritika-02-buborekok', 'c1-mediakritika-03-dezinformacio', 'c1-mediakritika-04-oknyomozas', 'c1-mediakritika-05-jovo'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Culture Unit 9 patient-rights | culture | 8 / 15 |
| C1 Culture Unit 10 corporate-law | culture | 6 / 12 |
| C1 Culture Unit 11 minority-protections | culture | 8 / 10 |
| C1 Culture Unit 12 civil-disobedience | culture | 3 / 11 |
| C1 Culture Unit 13 forint-eurozone | culture | 5 / 9 |
| C1 Culture Unit 14 paks-nuclear | culture | 13 / 9 |
| C1 Culture Unit 15 ai-ethics | culture | 8 / 15 |
| C1 Culture Unit 16 media-pluralism | culture | 8 / 14 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-bioetika-01 c1-bioetika-02 c1-bioetika-03 c1-bioetika-04 c1-bioetika-05 c1-bioetika-consolidation c1-szerzodesek-01 c1-szerzodesek-02 c1-szerzodesek-03 c1-szerzodesek-04 c1-szerzodesek-05 c1-szerzodesek-consolidation c1-emberijogok-01 c1-emberijogok-02 c1-emberijogok-03 c1-emberijogok-04 c1-emberijogok-05 c1-emberijogok-consolidation c1-polgariengedetlenseg-01 c1-polgariengedetlenseg-02 c1-polgariengedetlenseg-03 c1-polgariengedetlenseg-04 c1-polgariengedetlenseg-05 c1-polgariengedetlenseg-consolidation c1-monetaris-01 c1-monetaris-02 c1-monetaris-03 c1-monetaris-04 c1-monetaris-05 c1-monetaris-consolidation c1-energetika-01 c1-energetika-02 c1-energetika-03 c1-energetika-04 c1-energetika-05 c1-energetika-consolidation c1-mestersegesintelligencia-01 c1-mestersegesintelligencia-02 c1-mestersegesintelligencia-03 c1-mestersegesintelligencia-04 c1-mestersegesintelligencia-05 c1-mestersegesintelligencia-consolidation c1-mediakritika-01 c1-mediakritika-02 c1-mediakritika-03 c1-mediakritika-04 c1-mediakritika-05 c1-mediakritika-consolidation
- Reader A: 366,063 tokens, 43 tool uses, 17 min
- Reader B: 477,856 tokens, 68 tool uses, 24 min
