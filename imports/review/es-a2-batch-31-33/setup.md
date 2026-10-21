# es A2 batch: es-a2-batch-31-33

Started 2026-10-21T23:20:05Z from origin/master 74559b8b. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 31 indefinites-double-negation (a2-indefinidosnegacion-01 a2-indefinidosnegacion-02 a2-indefinidosnegacion-03 a2-indefinidosnegacion-04 a2-indefinidosnegacion-05 a2-indefinidosnegacion-consolidation; stories []); Unit 32 duration-recent-actions (a2-perifrasisduracion-01 a2-perifrasisduracion-02 a2-perifrasisduracion-03 a2-perifrasisduracion-04 a2-perifrasisduracion-05 a2-perifrasisduracion-consolidation; stories [])
- Reader B: Unit 33 vosotros (a2-vosotrospeninsular-01 a2-vosotrospeninsular-02 a2-vosotrospeninsular-03 a2-vosotrospeninsular-04 a2-vosotrospeninsular-05 a2-vosotrospeninsular-consolidation; stories [])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 31 indefinites-double-negation | 11 / 52 | 11 / 54 |
| 32 duration-recent-actions | 4 / 49 | 4 / 49 |
| 33 vosotros | 3 / 48 | no es-latam unit |

## Files differing es-es vs es-latam

- indefinites-double-negation: a2-indefinidosnegacion-01-gr.json, a2-indefinidosnegacion-02-ex.json, a2-indefinidosnegacion-03-gr.json, a2-indefinidosnegacion-03-ex.json
- duration-recent-actions: a2-perifrasisduracion-01-gr.json, a2-perifrasisduracion-02-ex.json
- vosotros: es-es only

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> a2 --jobs 4 --only a2-indefinidosnegacion-01 a2-indefinidosnegacion-02 a2-indefinidosnegacion-03 a2-indefinidosnegacion-04 a2-indefinidosnegacion-05 a2-indefinidosnegacion-consolidation a2-perifrasisduracion-01 a2-perifrasisduracion-02 a2-perifrasisduracion-03 a2-perifrasisduracion-04 a2-perifrasisduracion-05 a2-perifrasisduracion-consolidation a2-vosotrospeninsular-01 a2-vosotrospeninsular-02 a2-vosotrospeninsular-03 a2-vosotrospeninsular-04 a2-vosotrospeninsular-05 a2-vosotrospeninsular-consolidation
