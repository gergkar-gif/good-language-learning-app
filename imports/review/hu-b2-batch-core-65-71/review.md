# HU B2 core batch: Units 65, 67 (reader A) and 69, 71 (reader B), 2026-11-04: last core batch

No usage limit hit. Reader A 385,337 tokens (53 tool uses, 20 min), reader B 441,755 (68,
24 min): ~207k a unit, two units per reader. **The core track is complete: 36/36 frozen.**

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 65 `political-philosophy` | 9 / 0 | 94 | 70 | 1 (length; rewritten) | *ami / amely* second answer; story relabelled; 26 items retagged to `b2-cataphoric-clauses` by the reader | 0 / 0 |
| 67 `slang-register` | 13 / 1 | 101 | 68 | 1 (length; rewritten) | 6 second right answers (*Ugyan*, *Dehogy*, *elvállalni*, *hiszen* ×2, *stílusra*); story relabelled; 7 words listed | 0 / 2 accepted |
| 69 `technology-futurism-human-agency` | 17 / 2 | 125 | 123 | 2 (a *volna* in the prompt, an *örökre* tell; rewritten) | a grammatical wrong option (*a természetben*) replaced, and my own replacement duplicated an option (caught by check-content); 1 word listed | 0 / 0 |
| 71 `mastery-voice` | 14 / 1 | 103 | 101 | 2 (*mindig*, *senki* tells; rewritten) | 2 recaps named Unit 32 (a culture unit) for *mindazonáltal*: B2 Unit 31; Esti Kornél source corrected and relabelled; a capitalised challenge target; 19 words listed | 0 / 1 accepted |

423 fixes applied (417 from the readers' lists, 6 rewrites), 24 challenges, 27 words listed,
115 dictionary entries. Accepted at freeze: `vocab-unused` b2-34-01 *szabadul*, b2-34-03
*szleng*, b2-36-05 *nyelvvizsga* (consolidation only). Walk 24/24 with challenges. No new B2
validator warning. B2 36/72 frozen (all `core`).

## Found for the culture track

- **C1 *feltéve, hogy* is taught in culture units:** `b2-marslakok-01/03/05/consolidation`
  (B2 Unit 14, "Stipulative Conditionals: feltéve, hogy …"), `b2-tudomanyjovo-01` ("Speculative
  Conditions: Feltéve, ha…"), `b2-magyaridentitas-04` (reader B). The user's rule is to rewrite
  C1 forms; these units' batches do it (Unit 69 now recaps only *azzal a feltétellel, hogy*
  from Unit 14).
- Reader A: Unit 67 lesson 04 is a register-shift lesson (slang to formal). The C1
  `official-register` forms in it (*szíveskedjék*, *nem áll módomban*) are rewritten; the lesson
  stays (register contrast at B2 level).

## Judged by Claude

- Classics (`reviewer-facts.md`): Bibó (an essay, so a dialogue is not the work), Rejtő (2000s
  slang in a 1940 voice) and Kosztolányi ("Esti Kornél kalandjai (1933)" mixes the 1933 book and
  the later *Tengerszem* cycle) relabelled "Adaptation inspired by"; Karinthy kept, with reader B's
  fixes (the crash/shipwreck contradiction, Karinthy's motive stated as fact).
- The doubled-subject *X az nem más, mint Y* (Unit 65's skill) is colloquial but correct; kept.
- `check_unit_refs.py` flags a recap only when the named unit is earlier than the word's first
  appearance, so *mindazonáltal* "from B2 Unit 32" (taught in Unit 31) passed it; found by
  reading. A stricter rule would flag every incidental early use, so it stays a reading check.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
