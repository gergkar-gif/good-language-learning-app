# HU C1 core batch 17–24 (2026-11-14)

Units (app numbering): 17 regional-geopolitics, 18 digital-sovereignty, 19 social-stratification, 20 drying-alfold (reader A); 21 labour-economics, 22 computational-linguistics, 23 urban-preservation, 24 academic-autonomy (reader B). Four units per reader. Both readers were stopped by the 5-hour limit (reset 12:10 UTC) and resumed at 17:57.

## Cost

Resumed runs only (the first runs' totals were lost with the limit stop): A 376,461 tokens; B 364,720 tokens, including one follow-up. The resumed runs alone come to ~90k a unit, so this is a floor, not a full cost.

## Results

- check-content 65 errors / 113 suspects (setup.md) → 0 errors; 40 `vocab-unused` stems accepted.
- 864 fixes applied: merged-1 826, merged-2 27, practice-11 1, reviewer lists 4, two by hand (c1-20-05-reading-4, c1-17-01-introduce-1). 68 words listed.
- Unmet words after applying: 119 → 52, all lookup misses (participles, inflections).
- 48 challenges; 37 glosses.
- c1-22-01 now teaches the epistemic past modals (*kellett, hogy*, *-hatott/-hetett*) with 3 new items (user, 2026-11-14).
- Locked, frozen 8/8, walk 48/48 with challenges.

## Facts (reviewer-facts.md)

- **Karinthy:** 'szolifák' → *szolasz*.
- **Kalmár:** the invented 1962 study and the Gödel "proof" are removed. The text now states his known work: the 1957/1959 argument against Church's thesis, and cybernetics research in Szeged. I corrected the reader's circular gloss of Church's thesis.
- **Szűcs:** 1980 → first printed 1981 (Történelmi Szemle), book 1983.
- **Kaán:** *békediktátum* → *békeszerződés*.
- **Nagy Lajos:** the unverified quotation is removed.
- **Szent-Györgyi:** the aphorism is paraphrased and "embermentő" cut.
- **Present-day judgements removed:** Visegrád/illiberal (Unit 17), battery plants (Unit 21).

## Reviewer changes

- **Unit 21:** c1-21-consolidation-6 had no main clause for its participle.
- **Unit 24:** a wrong sense of *alátámaszt*; a possibly true distractor (Academy membership) flagged to the reader.
- **Unit 17:** doubled *szerint*.
- **Unit 20:** *fokozatosan* accepted for "alarmingly".
- **Two recap units:** *szembeötlően*, *céljából*.

## Scripted

`check_fixes.py` now adds the null for the other of `answer`/`answers` when a fix sets one (seen in batches 9–16 and 17–24: 5 and 9 rejects).

## Not verified

- Speaking steps, spoken answers, wrong-answer paths, real audio, a native speaker's eye.
- Budapest building facts in Unit 23 (from memory).
- Szent-Györgyi's exact 1943 role.
