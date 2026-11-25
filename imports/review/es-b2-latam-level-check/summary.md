# ES B2 Latin America track: level checklist (es-latam, 2026-11-25)

The pipeline doc's "Before calling a level done" list, run over the 36 latam units after the last
batch. The track stays hidden (`HIDDEN_TRACKS`) until the B1 latam track is ready too (user,
2026-11-25).

| Step | Result |
|---|---|
| `freeze_unit.py --status` | B2 72/72 frozen (core 36, latam 36) |
| `check-content.py es-latam b2` | 0 errors; 67 suspects, all `story-attribution` on the **core** classics (b2-01 … b2-36 and copies), none on the latam track |
| `validate-content.py --warnings` (B2 lines) | 0 retired slugs on B2 (566 at the start of the pass); 9 vocabulary skills with 5 items (6 latam: Units 31–36, half-size units; 3 core) |
| `unmet-words.js --with-hidden`, per unit | 0, apart from proper names (*Itaipú*, *Samanta*, *Alejandro*, *Trinidad*, *Asunción*) |
| `check_es_c1_forms.py es-latam --track latam` | 0 hits on B2 (27 in the old texts at the start); 10 left on the unread B1 latam track |
| `check_unit_refs.py … --named` | 3 hits, all false: Mexico I quotes two example sentences from b2-01-01, which has them |
| `reader_orphans.py es-latam b2` | 0 (4 combined readings were open in the Reader while hidden; fixed) |
| `walk_lessons.js` over the 216 latam lessons | 216/216 OK, challenges included |
| `story-quote` (new) | 0 unaccepted on the track; the real quotations (Costa Rica's article 12, Colombia's article 7, Menchú's title, UNESCO's Chiribiquete name) accepted |

Not covered: speaking steps, spoken challenge answers, wrong-answer paths, a native speaker's
read, live audio. Present-day facts were checked against 2026 news per batch; facts the agents and
the reviewer stated from knowledge without a fetched source are marked so in each batch's
`reviewer-facts.md`.

## For the user

1. **Thin vocabulary skills (5 items, threshold 6):** `b2-brazil-amazonia-brasilia-vocab`,
   `b2-amazon-basin-vocab`, `b2-regional-integration-corridors-vocab`, `b2-south-american-migration-vocab`,
   `b2-legal-pluralism-vocab`, `b2-latin-america-global-vocab` (half-size units), and three core ones.
   Either `thin_ok` for these or one more word item per unit.
2. **Core `story-attribution` suspects (67):** the core classics' Library labels, outside this pass;
   from the ES B2 core close-out.
3. **The B1 latam track** comes next (decided); `story-quote`, `latam_consolidation_story.py`,
   `reader_orphans.py` and `check_es_c1_forms.py` are ready for it.

## After the user's decision (2026-11-25)

"add one word items, then i think we can mark as complete": one review matching item added to
each thin vocabulary skill's consolidation (4 unit words from different lessons; core ones mirrored
to es-es); validator: no B2 warnings left. Refreezing ran the newer `story-attribution` check on
B2 core: the 31 texts about a work got `about: true` (es-latam and es-es), Güiraldes's adaptation
accepted. es-latam B2 and es-es B2: 0 errors, 0 suspects. Track signed off as complete.
