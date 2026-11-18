# ES C1 core pilot: Units 1-2 (2026-11-18)

Units `academic-argument` (1) and `written-norm` (2), written from scratch in
es-latam by two Sonnet writers in parallel (`scripts/templates/new-spanish-c1.txt`),
read by one Sonnet reader (`read-spanish-latam.txt` with a C1 focus), planted in
es-es with `scripts/plant_es_es_c1.py`. Frozen in both courses; C1 core stays hidden.

## Cost

| Step | Tokens | Time |
|---|---|---|
| Writer, Unit 1 | 356k | 19 min |
| Writer, Unit 2 (incl. one fix round) | 322k | 17 min |
| Reader, both units | 293k | 12 min |
| **Per unit** | **~485k** | |

Above the plan's 250-350k guess; reviewer time (verification, applying, planting) on top.

## Defects

- Reviewer, before the read (sent back to the Unit 2 writer): the lesson 05 rule
  "only the short participle as an adjective" is false for *imprimir* and *proveer*
  (RAE DPD, from rae.es search excerpts: *proveído/provisto* both valid as adjectives,
  *impreso* preferred, only *frito* required); 6+ items had acceptable wrong options;
  5 two-option items (now 3 options); 2 sequence-of-tenses items with an arguable
  wrong option (now in finished past frames). Unit 1: *se queja por* -> *se queja de*.
- Reader: 25 fixes (Unit 1: 12, Unit 2: 13), mostly pinning prompts and wording; two
  amended by the reviewer (no invented scene with Meg's sister in c1-02-05.ex09; a
  challenge target glued from two sentences replaced by one gerund sentence).
- es-es plant: the word converter turned tile *sala* into *salón* next to tile *la*
  (*la salón*). Fixed in the script (tiles copied and listed, not converted); es-es
  c1-02-consolidation.ex11 uses *la oficina* (es-es lists *salón*, not *sala*).

## Results

| Check | es-latam | es-es |
|---|---|---|
| check-content | 0 / 0 | 0 / 0 |
| unmet words (`--with-hidden`) | none | none |
| check_es_c1_forms (core) | 0 | 0 |
| validate --changed | pass | pass |
| walk with challenges | 12/12 | 12/12 |
| frozen | 2/2 | 2/2 |

Files identical in both courses apart from c1-02-consolidation.ex11.

Not checked: a native reader's eye (writers' "unsure" lines: *tener su terreno*,
*Te concedo que…*, a few stiff examples), speaking steps, real audio.

## For the next batches

- Writers in parallel cannot see each other's words: no duplicates this time (75
  entries), but the reviewer checks it per batch.
- The writer's first draft had the factual rule error the reader would probably not
  have caught (it trusted the screen): the reviewer verifies every norm claim of a
  screen against a source before the read.
- Ask for 3+ options in the template (added).
