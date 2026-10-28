# es B1 batch: hu-b1-batch-cit-08-14

Started 2026-10-28T06:32:39Z from origin/master 5ad6d755. 2 Sonnet reader(s).

- Reader A: Unit 8 saint-stephen (b1-istvankiraly-01 b1-istvankiraly-02 b1-istvankiraly-03 b1-istvankiraly-04 b1-istvankiraly-05 b1-istvankiraly-consolidation; stories ['b1-istvankiraly-01-gezafejedelem', 'b1-istvankiraly-02-koronazas', 'b1-istvankiraly-03-keresztenykiralysag', 'b1-istvankiraly-04-szentistvanoroksege', 'b1-istvankiraly-05-szentkorona']); Unit 10 arpad-dynasty (b1-arpadhaz-01 b1-arpadhaz-02 b1-arpadhaz-03 b1-arpadhaz-04 b1-arpadhaz-05 b1-arpadhaz-consolidation; stories ['b1-arpadhaz-01-arpadhazikiralyok', 'b1-arpadhaz-02-aranybulla', 'b1-arpadhaz-03-orszagszervezes', 'b1-arpadhaz-04-egyhazesallam', 'b1-arpadhaz-05-arpadhazvege'])
- Reader B: Unit 12 mongol-invasion (b1-tatarjaras-01 b1-tatarjaras-02 b1-tatarjaras-03 b1-tatarjaras-04 b1-tatarjaras-05 b1-tatarjaras-consolidation; stories ['b1-tatarjaras-01-tatarokerkezese', 'b1-tatarjaras-02-muhicsata', 'b1-tatarjaras-03-pusztulas', 'b1-tatarjaras-04-belaujjapitese', 'b1-tatarjaras-05-kovarak']); Unit 14 angevin-kings (b1-anjouk-01 b1-anjouk-02 b1-anjouk-03 b1-anjouk-04 b1-anjouk-05 b1-anjouk-consolidation; stories ['b1-anjouk-01-karolyrobert', 'b1-anjouk-02-visegrad', 'b1-anjouk-03-nagylajos', 'b1-anjouk-04-zsigmond', 'b1-anjouk-05-nandorfehervar'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 8 saint-stephen | citizenship | 22 / 6 |
| 10 arpad-dynasty | citizenship | 17 / 7 |
| 12 mongol-invasion | citizenship | 18 / 5 |
| 14 angevin-kings | citizenship | 27 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b1 --jobs 4 --only b1-istvankiraly-01 b1-istvankiraly-02 b1-istvankiraly-03 b1-istvankiraly-04 b1-istvankiraly-05 b1-istvankiraly-consolidation b1-arpadhaz-01 b1-arpadhaz-02 b1-arpadhaz-03 b1-arpadhaz-04 b1-arpadhaz-05 b1-arpadhaz-consolidation b1-tatarjaras-01 b1-tatarjaras-02 b1-tatarjaras-03 b1-tatarjaras-04 b1-tatarjaras-05 b1-tatarjaras-consolidation b1-anjouk-01 b1-anjouk-02 b1-anjouk-03 b1-anjouk-04 b1-anjouk-05 b1-anjouk-consolidation
