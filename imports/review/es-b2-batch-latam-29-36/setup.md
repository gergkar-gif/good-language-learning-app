# es B2 batch: es-b2-batch-latam-29-36

Started 2026-11-25T12:50:07Z from origin/master 29a041dd. 2 Sonnet reader(s); es-latam only (the level has no es-es course), nothing mirrored.

- Reader A: B2 Latin America Unit 29 brazil-rio-sao-paulo (b2-brasilsudeste-01 b2-brasilsudeste-02 b2-brasilsudeste-03 b2-brasilsudeste-04 b2-brasilsudeste-05 b2-brasilsudeste-consolidation; stories ['b2-brasilsudeste-01', 'b2-brasilsudeste-02', 'b2-brasilsudeste-03', 'b2-brasilsudeste-04', 'b2-brasilsudeste-05']); B2 Latin America Unit 30 brazil-northeast (b2-brasilnordeste-01 b2-brasilnordeste-02 b2-brasilnordeste-03 b2-brasilnordeste-04 b2-brasilnordeste-05 b2-brasilnordeste-consolidation; stories ['b2-brasilnordeste-01', 'b2-brasilnordeste-02', 'b2-brasilnordeste-03', 'b2-brasilnordeste-04', 'b2-brasilnordeste-05']); B2 Latin America Unit 31 brazil-amazonia-brasilia (b2-brasilinterior-01 b2-brasilinterior-02 b2-brasilinterior-03 b2-brasilinterior-04 b2-brasilinterior-05 b2-brasilinterior-consolidation; stories ['b2-brasilinterior-01', 'b2-brasilinterior-02', 'b2-brasilinterior-03', 'b2-brasilinterior-04', 'b2-brasilinterior-05', 'b2-brasilinterior-consolidation']); B2 Latin America Unit 32 amazon-basin (b2-amazoniapan-01 b2-amazoniapan-02 b2-amazoniapan-03 b2-amazoniapan-04 b2-amazoniapan-05 b2-amazoniapan-consolidation; stories ['b2-amazoniapan-01', 'b2-amazoniapan-02', 'b2-amazoniapan-03', 'b2-amazoniapan-04', 'b2-amazoniapan-05', 'b2-amazoniapan-consolidation'])
- Reader B: B2 Latin America Unit 33 regional-integration-corridors (b2-integracion-01 b2-integracion-02 b2-integracion-03 b2-integracion-04 b2-integracion-05 b2-integracion-consolidation; stories ['b2-integracion-01', 'b2-integracion-02', 'b2-integracion-03', 'b2-integracion-04', 'b2-integracion-05', 'b2-integracion-consolidation']); B2 Latin America Unit 34 south-american-migration (b2-migracion-01 b2-migracion-02 b2-migracion-03 b2-migracion-04 b2-migracion-05 b2-migracion-consolidation; stories ['b2-migracion-01', 'b2-migracion-02', 'b2-migracion-03', 'b2-migracion-04', 'b2-migracion-05', 'b2-migracion-consolidation']); B2 Latin America Unit 35 legal-pluralism (b2-pluralismo-01 b2-pluralismo-02 b2-pluralismo-03 b2-pluralismo-04 b2-pluralismo-05 b2-pluralismo-consolidation; stories ['b2-pluralismo-01', 'b2-pluralismo-02', 'b2-pluralismo-03', 'b2-pluralismo-04', 'b2-pluralismo-05', 'b2-pluralismo-consolidation']); B2 Latin America Unit 36 latin-america-global (b2-futuro-01 b2-futuro-02 b2-futuro-03 b2-futuro-04 b2-futuro-05 b2-futuro-consolidation; stories ['b2-futuro-01', 'b2-futuro-02', 'b2-futuro-03', 'b2-futuro-04', 'b2-futuro-05', 'b2-futuro-consolidation'])

## Baseline check-content, errors / suspects

| Unit | track | errors / suspects |
|---|---|---|
| B2 Latin America Unit 29 brazil-rio-sao-paulo | latam | 15 / 25 |
| B2 Latin America Unit 30 brazil-northeast | latam | 15 / 16 |
| B2 Latin America Unit 31 brazil-amazonia-brasilia | latam | 6 / 27 |
| B2 Latin America Unit 32 amazon-basin | latam | 7 / 26 |
| B2 Latin America Unit 33 regional-integration-corridors | latam | 7 / 27 |
| B2 Latin America Unit 34 south-american-migration | latam | 11 / 30 |
| B2 Latin America Unit 35 legal-pluralism | latam | 10 / 27 |
| B2 Latin America Unit 36 latin-america-global | latam | 9 / 28 |

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js es-latam b2 --jobs 4 --only b2-brasilsudeste-01 b2-brasilsudeste-02 b2-brasilsudeste-03 b2-brasilsudeste-04 b2-brasilsudeste-05 b2-brasilsudeste-consolidation b2-brasilnordeste-01 b2-brasilnordeste-02 b2-brasilnordeste-03 b2-brasilnordeste-04 b2-brasilnordeste-05 b2-brasilnordeste-consolidation b2-brasilinterior-01 b2-brasilinterior-02 b2-brasilinterior-03 b2-brasilinterior-04 b2-brasilinterior-05 b2-brasilinterior-consolidation b2-amazoniapan-01 b2-amazoniapan-02 b2-amazoniapan-03 b2-amazoniapan-04 b2-amazoniapan-05 b2-amazoniapan-consolidation b2-integracion-01 b2-integracion-02 b2-integracion-03 b2-integracion-04 b2-integracion-05 b2-integracion-consolidation b2-migracion-01 b2-migracion-02 b2-migracion-03 b2-migracion-04 b2-migracion-05 b2-migracion-consolidation b2-pluralismo-01 b2-pluralismo-02 b2-pluralismo-03 b2-pluralismo-04 b2-pluralismo-05 b2-pluralismo-consolidation b2-futuro-01 b2-futuro-02 b2-futuro-03 b2-futuro-04 b2-futuro-05 b2-futuro-consolidation

## Method (2026-11-25)

Last batch: four units per agent (Units 31–36 are half size). Two lessons re-pointed (29-01, 30-01),
one retired slug (36-05); the rest recap known skills.

## Agents (edit-in-place, Sonnet), started 12:50 UTC on 29a041dd

- A (Latin America Units 29–32; /home/user/parlour-read-a): agent a83562193ef052253
- B (Latin America Units 33–36; /home/user/parlour-read-b): agent a5d0db00c84424c35

Resume a stopped agent with SendMessage to its id; never start a new one.

## Found during the wait (2026-11-25)

- **Reader leak:** four combined readings of frozen units (Guatemala, Nicaragua, El Salvador/
  Honduras, Paraguay) were referenced by no lesson, so the manifest listed them with no unit and no
  `hidden` flag: open in the Reader while the track is hidden. Their consolidation lessons now show
  the combined reading (as Cuba, Costa Rica do); units refrozen, consolidations walked 4/4.
  **Scripted:** `scripts/reader_orphans.py <course> [level]`; B2 now lists 0. (es-latam A1–B1 list
  55 free-standing Reader stories, es-es 56, hu 11: read at their levels' checklists, ES B1's 29 in
  its close-out; not part of this pass.)
- `check_es_c1_forms.py es-latam --track latam`: 0 hits in the 28 frozen B2 latam units; 27 in the
  old texts of Units 29–36 (agents told) and in the unread B1 track.
