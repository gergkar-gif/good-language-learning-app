# hu B2 batch: hu-b2-batch-cult-58-64

Started 2026-11-10T13:38:23Z from origin/master f14bf87f. 2 Sonnet reader(s).

- Reader A: Unit 58 visegrad-geopolitics (b2-kulpolitika-01 b2-kulpolitika-02 b2-kulpolitika-03 b2-kulpolitika-04 b2-kulpolitika-05 b2-kulpolitika-consolidation; stories ['b2-kulpolitika-01-visegradi1335', 'b2-kulpolitika-02-vnegyek1991', 'b2-kulpolitika-03-kereskedelmiutak', 'b2-kulpolitika-04-uniosvitak', 'b2-kulpolitika-05-diplomaciaistrategia']); Unit 60 ombudsman-civic-rights (b2-jogvedelem-01 b2-jogvedelem-02 b2-jogvedelem-03 b2-jogvedelem-04 b2-jogvedelem-05 b2-jogvedelem-consolidation; stories ['b2-jogvedelem-01-ombudsman', 'b2-jogvedelem-02-fellebbezes', 'b2-jogvedelem-03-kozerdekuadat', 'b2-jogvedelem-04-egyszazalekcivil', 'b2-jogvedelem-05-hivatalosbeadvany'])
- Reader B: Unit 62 paprika-tokaj (b2-borkultura-01 b2-borkultura-02 b2-borkultura-03 b2-borkultura-04 b2-borkultura-05 b2-borkultura-consolidation; stories ['b2-borkultura-01-reneszanszizek', 'b2-borkultura-02-tokajhegyalja', 'b2-borkultura-03-gundelkor', 'b2-borkultura-04-szocialistareceptek', 'b2-borkultura-05-gasztroforradalom']); Unit 64 sport-national-identity (b2-sporttortenet-01 b2-sporttortenet-02 b2-sporttortenet-03 b2-sporttortenet-04 b2-sporttortenet-05 b2-sporttortenet-consolidation; stories ['b2-sporttortenet-01-hajosalfred', 'b2-sporttortenet-02-vizilabdaesvivas', 'b2-sporttortenet-03-aranycsapat1953', 'b2-sporttortenet-04-melbourne1956', 'b2-sporttortenet-05-sportnemzetielet'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| 58 visegrad-geopolitics | culture | 13 / 0 |
| 60 ombudsman-civic-rights | culture | 15 / 0 |
| 62 paprika-tokaj | culture | 7 / 0 |
| 64 sport-national-identity | culture | 9 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js hu b2 --jobs 4 --only b2-kulpolitika-01 b2-kulpolitika-02 b2-kulpolitika-03 b2-kulpolitika-04 b2-kulpolitika-05 b2-kulpolitika-consolidation b2-jogvedelem-01 b2-jogvedelem-02 b2-jogvedelem-03 b2-jogvedelem-04 b2-jogvedelem-05 b2-jogvedelem-consolidation b2-borkultura-01 b2-borkultura-02 b2-borkultura-03 b2-borkultura-04 b2-borkultura-05 b2-borkultura-consolidation b2-sporttortenet-01 b2-sporttortenet-02 b2-sporttortenet-03 b2-sporttortenet-04 b2-sporttortenet-05 b2-sporttortenet-consolidation
