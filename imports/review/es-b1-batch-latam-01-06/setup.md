# es B1 batch: es-b1-batch-latam-01-06

Started 2026-11-26T00:03:56Z from origin/master ce9117d4. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B1 Latin America Unit 1 pre-columbian-america (b1-precolombina-01 b1-precolombina-02 b1-precolombina-03 b1-precolombina-04 b1-precolombina-05 b1-precolombina-consolidation; stories ['b1-precolombina-01-continente', 'b1-precolombina-02-civilizaciones', 'b1-precolombina-03-sociedad', 'b1-precolombina-04-vidacotidiana', 'b1-precolombina-05-evidencia']); B1 Latin America Unit 2 indigenous-civilizations (b1-civilizaciones-01 b1-civilizaciones-02 b1-civilizaciones-03 b1-civilizaciones-04 b1-civilizaciones-05 b1-civilizaciones-consolidation; stories ['b1-civilizaciones-01-mayas', 'b1-civilizaciones-02-mexicas', 'b1-civilizaciones-03-incas', 'b1-civilizaciones-04-religion', 'b1-civilizaciones-05-legado']); B1 Latin America Unit 3 arrival-of-europeans (b1-llegadaeuropeos-01 b1-llegadaeuropeos-02 b1-llegadaeuropeos-03 b1-llegadaeuropeos-04 b1-llegadaeuropeos-05 b1-llegadaeuropeos-consolidation; stories ['b1-llegadaeuropeos-01-viaje', 'b1-llegadaeuropeos-02-encuentro', 'b1-llegadaeuropeos-03-resistencia', 'b1-llegadaeuropeos-04-nuevosmundos', 'b1-llegadaeuropeos-05-transformacion'])
- Reader B: B1 Latin America Unit 4 conquest (b1-conquista-01 b1-conquista-02 b1-conquista-03 b1-conquista-04 b1-conquista-05 b1-conquista-consolidation; stories ['b1-conquista-01-mexico', 'b1-conquista-02-peru', 'b1-conquista-03-alianzas', 'b1-conquista-04-violencia', 'b1-conquista-05-catastrofe']); B1 Latin America Unit 5 colonial-society (b1-sociedadcolonial-01 b1-sociedadcolonial-02 b1-sociedadcolonial-03 b1-sociedadcolonial-04 b1-sociedadcolonial-05 b1-sociedadcolonial-consolidation; stories ['b1-sociedadcolonial-01-imperio', 'b1-sociedadcolonial-02-jerarquia', 'b1-sociedadcolonial-03-iglesia', 'b1-sociedadcolonial-04-vidacotidiana', 'b1-sociedadcolonial-05-vivir']); B1 Latin America Unit 6 colonial-economy (b1-economiacolonial-01 b1-economiacolonial-02 b1-economiacolonial-03 b1-economiacolonial-04 b1-economiacolonial-05 b1-economiacolonial-consolidation; stories ['b1-economiacolonial-01-plataoro', 'b1-economiacolonial-02-trabajo', 'b1-economiacolonial-03-plantaciones', 'b1-economiacolonial-04-comercio', 'b1-economiacolonial-05-precio'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B1 Latin America Unit 1 pre-columbian-america | latam | 29 / 2 |
| B1 Latin America Unit 2 indigenous-civilizations | latam | 21 / 4 |
| B1 Latin America Unit 3 arrival-of-europeans | latam | 28 / 2 |
| B1 Latin America Unit 4 conquest | latam | 24 / 3 |
| B1 Latin America Unit 5 colonial-society | latam | 23 / 1 |
| B1 Latin America Unit 6 colonial-economy | latam | 25 / 0 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b1 --jobs 4 --only b1-precolombina-01 b1-precolombina-02 b1-precolombina-03 b1-precolombina-04 b1-precolombina-05 b1-precolombina-consolidation b1-civilizaciones-01 b1-civilizaciones-02 b1-civilizaciones-03 b1-civilizaciones-04 b1-civilizaciones-05 b1-civilizaciones-consolidation b1-llegadaeuropeos-01 b1-llegadaeuropeos-02 b1-llegadaeuropeos-03 b1-llegadaeuropeos-04 b1-llegadaeuropeos-05 b1-llegadaeuropeos-consolidation b1-conquista-01 b1-conquista-02 b1-conquista-03 b1-conquista-04 b1-conquista-05 b1-conquista-consolidation b1-sociedadcolonial-01 b1-sociedadcolonial-02 b1-sociedadcolonial-03 b1-sociedadcolonial-04 b1-sociedadcolonial-05 b1-sociedadcolonial-consolidation b1-economiacolonial-01 b1-economiacolonial-02 b1-economiacolonial-03 b1-economiacolonial-04 b1-economiacolonial-05 b1-economiacolonial-consolidation

## Method (2026-11-26)

First B1 latam batch, three units per agent (the B2 latam rate at three was ~103–125k a unit).
Brief = `header.txt` + `units-<a|b>.txt` + `scripts/templates/edit-spanish-latam-b1-track.txt`.
Differences from B2 latam: every lesson text rewritten (garbled, many shifted to another lesson's
topic), B1 unmet-word rule (no cognate allowance), named speakers replaced, one known skill per lesson
chosen to vary across units (the generator gave every unit the same five). Structural notes by
`scripts/latam_unit_notes.py` (`structure-01.md`, `structure-02-06.md`). The 120 orphan screens of the
track were deleted at setup (ce9117d4).

## Agents (edit-in-place, Sonnet), started ~00:20 UTC 2026-11-26 on c46d5fe2

- A (Latin America Units 1–3; /home/user/parlour-read-a): agent a4800f887adf217ba
- B (Latin America Units 4–6; /home/user/parlour-read-b): agent abc22fdd7333f4ab2

Resume a stopped agent with SendMessage to its id; never start a new one.
