# ES B2 read-through: decisions before the pilot (user, 2026-11-13)

Spanish B2 exists only in es-latam (es-es has no B2 unit table or lessons), so
the B2 pass reads es-latam alone and mirrors nothing. The `latam` track is
hidden (HIDDEN_TRACKS); the pass starts with the 36 core units.

Found at setup and decided by the user:

1. **Screens and question stems in English.** All 180 core screens and 363 of
   385 choice-question stems explain grammar in academic Spanish the learner has
   not met. They are rewritten in English (as in A1–B1 and HU B2): explanation
   and stems in English, Spanish terms and examples in italics.
2. **Stories by authors in copyright.** 27 of the 36 unit stories retell
   in-copyright works (Borges, Rulfo, García Márquez, Fuentes, Paz, Galeano,
   Carpentier, Allende, Vargas Llosa, Benedetti, Sabato, Icaza, Alegría,
   Céspedes, Coloane, Roa Bastos, Lispector, Cortázar, Scorza, J. M. Arguedas…);
   the Borges one follows the original's sentences closely, and CREDITS.md says
   every adapted work is public domain. Each of the 27 is replaced with an
   original Parlour text *about* the author and the work (who, when, what it is
   about, why it matters): no retold scenes, no near-quotes, facts checked on the
   web. The public-domain ones stay retellings checked against their sources.
   (Copyright terms to check per author by the reviewer; "in copyright" here is
   the reviewer's reading, not legal advice.)
3. **Cognate allowance for unmet words.** B2 core exercises use 3,069 distinct
   words no visible lesson lists. From B2, a transparent English cognate counts
   as met: `scripts/build_cognates.py` builds `imports/dictionary/cognates-es.json`
   (each lemma's dictionary gloss must be predicted by its spelling), the
   reviewer strikes false friends into its `never` list, and
   `scripts/unmet-words.js` skips the rest. Every other unmet word follows the B1
   rule (list it in the first lesson that uses it, or replace it).
4. **Skills taught only on the hidden track get core homes, batch by batch.**
   12 B2 grammar skills have their only screen in a `latam` unit
   (`stance-adverbs`, `contrast-markers`, `reporting-verbs`,
   `gerund-periphrases`, `concesivas-por-mas-que`, `concesivas-si-bien`,
   `concesivas-aun-cuando`, `antes-despues-de-que`, `consecutivas-de-tal-manera`,
   `participios-absolutos-narrativos`, `perifrasis-modales-probabilidad-epistemica`,
   and the es-latam-only `voseo-rioplatense-reconocimiento`). Each gets its
   `taught_in` moved to the core lesson that teaches or drills it (a screen
   written where none exists), brought to the user for sign-off with its batch
   (`skills/frozen-es.json` entry). Pilot: `stance-adverbs` → b2-01-02.

## Answers to the reviewer's report (user, 2026-11-13)

5. **Unit numbers: one rule for all languages, logical and consistent within the
   app.** The app numbers units per track (build-manifest.py), so every "Unit N"
   in content is the number the app shows. Existing recaps written by table
   position (all HU, part of ES B1) are renumbered by script.
6. **Copyright: make the texts safe** (confirms decision 2 for all 27).
7. **New units may be added** where a skill has no core home (*de tal manera
   que*, absolute participles) and a section in an existing unit doesn't fit.
