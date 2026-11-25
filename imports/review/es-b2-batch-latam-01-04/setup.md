# es B2 batch: es-b2-batch-latam-01-04

Started 2026-11-25T01:28:58Z from origin/master b5a00f42. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 1 mexico-central (b2-mexicocentro-01 b2-mexicocentro-02 b2-mexicocentro-03 b2-mexicocentro-04 b2-mexicocentro-05 b2-mexicocentro-consolidation; stories ['b2-mexicocentro-01', 'b2-mexicocentro-02', 'b2-mexicocentro-03', 'b2-mexicocentro-04', 'b2-mexicocentro-05']); B2 Latin America Unit 2 mexico-north (b2-mexiconorte-01 b2-mexiconorte-02 b2-mexiconorte-03 b2-mexiconorte-04 b2-mexiconorte-05 b2-mexiconorte-consolidation; stories ['b2-mexiconorte-01', 'b2-mexiconorte-02', 'b2-mexiconorte-03', 'b2-mexiconorte-04', 'b2-mexiconorte-05', 'b2-mexiconorte'])
- Reader B: B2 Latin America Unit 3 mexico-south (b2-mexicosur-01 b2-mexicosur-02 b2-mexicosur-03 b2-mexicosur-04 b2-mexicosur-05 b2-mexicosur-consolidation; stories ['b2-mexicosur-01', 'b2-mexicosur-02', 'b2-mexicosur-03', 'b2-mexicosur-04', 'b2-mexicosur-05', 'b2-mexicosur']); B2 Latin America Unit 4 guatemala (b2-guatemala-01 b2-guatemala-02 b2-guatemala-03 b2-guatemala-04 b2-guatemala-05 b2-guatemala-consolidation; stories ['b2-guatemala-01', 'b2-guatemala-02', 'b2-guatemala-03', 'b2-guatemala-04', 'b2-guatemala-05'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 1 mexico-central | latam | 32 / 20 |
| B2 Latin America Unit 2 mexico-north | latam | 23 / 11 |
| B2 Latin America Unit 3 mexico-south | latam | 28 / 13 |
| B2 Latin America Unit 4 guatemala | latam | 30 / 13 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-mexicocentro-01 b2-mexicocentro-02 b2-mexicocentro-03 b2-mexicocentro-04 b2-mexicocentro-05 b2-mexicocentro-consolidation b2-mexiconorte-01 b2-mexiconorte-02 b2-mexiconorte-03 b2-mexiconorte-04 b2-mexiconorte-05 b2-mexiconorte-consolidation b2-mexicosur-01 b2-mexicosur-02 b2-mexicosur-03 b2-mexicosur-04 b2-mexicosur-05 b2-mexicosur-consolidation b2-guatemala-01 b2-guatemala-02 b2-guatemala-03 b2-guatemala-04 b2-guatemala-05 b2-guatemala-consolidation

## Method (2026-11-25)

Edit-in-place agents (Sonnet), two units each, as the ES B2 core batches: the track needs rewriting
(Spanish screens, question stems, goals and intro; truncated reading options; 13 lessons drilling
core skills taught later). Briefs: `brief-a.txt`, `brief-b.txt` = `unit-<x>.txt` +
`scripts/templates/edit-spanish-latam-b2-track.txt` (new, from `edit-spanish-latam-b2.txt`). The
`prompt-*.txt` read prompts batch_setup.py writes were not used and are removed.

Fixed at setup: `prior_knowledge.py` and `unmet-words.js --with-hidden` counted the hidden, unread
B1 latam track as met for a B2 latam unit (Mexico I: 109 unmet words with it, 140 without). Both
now open only the reviewed unit's own level and track. Knowledge sheets regenerated after the fix.
