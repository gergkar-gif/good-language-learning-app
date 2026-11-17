# hu C1 batch: hu-c1-batch-cult-02-16

Started 2026-11-17T13:28:56Z from origin/master af9a5c5f. 2 Sonnet reader(s).

- Reader A: C1 Culture Unit 1 language-worldview (c1-nyelvfilozofia-01 c1-nyelvfilozofia-02 c1-nyelvfilozofia-03 c1-nyelvfilozofia-04 c1-nyelvfilozofia-05 c1-nyelvfilozofia-consolidation; stories ['c1-nyelvfilozofia-01-belsoforma', 'c1-nyelvfilozofia-02-tizlegszebb', 'c1-nyelvfilozofia-03-relativizmus', 'c1-nyelvfilozofia-04-termetaforak', 'c1-nyelvfilozofia-05-digitalishorizont']); C1 Culture Unit 2 hungarian-essay (c1-esszemuveszet-01 c1-esszemuveszet-02 c1-esszemuveszet-03 c1-esszemuveszet-04 c1-esszemuveszet-05 c1-esszemuveszet-consolidation; stories ['c1-esszemuveszet-01-pazmany', 'c1-esszemuveszet-02-nyugat', 'c1-esszemuveszet-03-szerb', 'c1-esszemuveszet-04-csszabo', 'c1-esszemuveszet-05-nemeth']); C1 Culture Unit 3 paradigm-shifts (c1-tudomanyelmelet-01 c1-tudomanyelmelet-02 c1-tudomanyelmelet-03 c1-tudomanyelmelet-04 c1-tudomanyelmelet-05 c1-tudomanyelmelet-consolidation; stories ['c1-tudomanyelmelet-01-polanyi', 'c1-tudomanyelmelet-02-lakatos', 'c1-tudomanyelmelet-03-neumann', 'c1-tudomanyelmelet-04-objektivitas', 'c1-tudomanyelmelet-05-etika']); C1 Culture Unit 4 public-debate (c1-vitakultura-01 c1-vitakultura-02 c1-vitakultura-03 c1-vitakultura-04 c1-vitakultura-05 c1-vitakultura-consolidation; stories ['c1-vitakultura-01-reformkor', 'c1-vitakultura-02-deak', 'c1-vitakultura-03-dualizmus', 'c1-vitakultura-04-sajtovita', 'c1-vitakultura-05-media'])
- Reader B: C1 Culture Unit 5 urban-satire (c1-pestiironia-01 c1-pestiironia-02 c1-pestiironia-03 c1-pestiironia-04 c1-pestiironia-05 c1-pestiironia-consolidation; stories ['c1-pestiironia-01-kavicsok', 'c1-pestiironia-02-karinthy', 'c1-pestiironia-03-kabare', 'c1-pestiironia-04-szamizdat', 'c1-pestiironia-05-memek']); C1 Culture Unit 6 hungarian-metaphors (c1-metaforak-01 c1-metaforak-02 c1-metaforak-03 c1-metaforak-04 c1-metaforak-05 c1-metaforak-consolidation; stories ['c1-metaforak-01-ter', 'c1-metaforak-03-termeszet', 'c1-metaforak-04-tortenelem', 'c1-metaforak-05-jovo']); C1 Culture Unit 7 rule-of-law (c1-jogallamisag-01 c1-jogallamisag-02 c1-jogallamisag-03 c1-jogallamisag-04 c1-jogallamisag-05 c1-jogallamisag-consolidation; stories ['c1-jogallamisag-01-aranybulla', 'c1-jogallamisag-02-szentkorona', 'c1-jogallamisag-03-aprilitorvenyek', 'c1-jogallamisag-04-alkotmanybirosag', 'c1-jogallamisag-05-eu-jogallamisag']); C1 Culture Unit 8 transparency-redress (c1-kozszolgalat-01 c1-kozszolgalat-02 c1-kozszolgalat-03 c1-kozszolgalat-04 c1-kozszolgalat-05 c1-kozszolgalat-consolidation; stories ['c1-kozszolgalat-01-adatigenyles', 'c1-kozszolgalat-02-ombudsman', 'c1-kozszolgalat-03-bejelentovedelem', 'c1-kozszolgalat-04-digitaliskozigazgatas', 'c1-kozszolgalat-05-civilszervezetek'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| C1 Culture Unit 1 language-worldview | culture | 19 / 20 |
| C1 Culture Unit 2 hungarian-essay | culture | 3 / 9 |
| C1 Culture Unit 3 paradigm-shifts | culture | 9 / 10 |
| C1 Culture Unit 4 public-debate | culture | 11 / 12 |
| C1 Culture Unit 5 urban-satire | culture | 9 / 10 |
| C1 Culture Unit 6 hungarian-metaphors | culture | 6 / 11 |
| C1 Culture Unit 7 rule-of-law | culture | 6 / 12 |
| C1 Culture Unit 8 transparency-redress | culture | 7 / 13 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu c1 --jobs 4 --only c1-nyelvfilozofia-01 c1-nyelvfilozofia-02 c1-nyelvfilozofia-03 c1-nyelvfilozofia-04 c1-nyelvfilozofia-05 c1-nyelvfilozofia-consolidation c1-esszemuveszet-01 c1-esszemuveszet-02 c1-esszemuveszet-03 c1-esszemuveszet-04 c1-esszemuveszet-05 c1-esszemuveszet-consolidation c1-tudomanyelmelet-01 c1-tudomanyelmelet-02 c1-tudomanyelmelet-03 c1-tudomanyelmelet-04 c1-tudomanyelmelet-05 c1-tudomanyelmelet-consolidation c1-vitakultura-01 c1-vitakultura-02 c1-vitakultura-03 c1-vitakultura-04 c1-vitakultura-05 c1-vitakultura-consolidation c1-pestiironia-01 c1-pestiironia-02 c1-pestiironia-03 c1-pestiironia-04 c1-pestiironia-05 c1-pestiironia-consolidation c1-metaforak-01 c1-metaforak-02 c1-metaforak-03 c1-metaforak-04 c1-metaforak-05 c1-metaforak-consolidation c1-jogallamisag-01 c1-jogallamisag-02 c1-jogallamisag-03 c1-jogallamisag-04 c1-jogallamisag-05 c1-jogallamisag-consolidation c1-kozszolgalat-01 c1-kozszolgalat-02 c1-kozszolgalat-03 c1-kozszolgalat-04 c1-kozszolgalat-05 c1-kozszolgalat-consolidation
