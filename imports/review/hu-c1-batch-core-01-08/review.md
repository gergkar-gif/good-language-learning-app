# HU C1 core batch 1–8 (first C1 batch, 2026-11-14)

Units (app numbering, core track): 1 argument-cohesion, 2 syntactic-compression, 3 hedging-evidentials, 4 polemics-refutation (reader A); 5 irony-understatement, 6 metaphor-idiom, 7 legal-language, 8 passive-avoidance (reader B). No pilot: HU B2 core method, four short units per reader (Units 2–8 have 52 items each, Unit 1 has 92).

## Cost

| Reader | Tokens | Minutes | Fixes written |
|---|---|---|---|
| A (Units 1–4) | 363,583 (350,404 first run + follow-up) | 15.5 + 1.3 | 423 (389 after folding duplicates) + 28 extra |
| B (Units 5–8) | 353,181 (328,742 first run + two follow-ups; stopped once by the 5-hour limit) | 13.8 + ~1.5 | 314 + 37 extra + 7 (official register) |

About 90k reader tokens a unit (HU B2 core: ~117–148k at three per reader).

## Results

- check-content: 50 errors / 100 suspects (baseline, setup.md) → 0 errors; 40 suspects accepted (`accept.txt`: 38 `vocab-unused` stems, 2 `article-blank` false positives, *abból az következne*).
- 737 fixes applied: merged-1 (638), merged-2 extras (65), merged-3 official register (7), carry (19), reviewer lists (rev-*.json, 8); 73 words listed (two vocab lists).
- Unmet words after applying: 79 → 18, all lookup misses (comparatives, participles, split verbs).
- 48 challenges added; 41 dictionary glosses.
- 28 retired `c1-*` tags retagged (C1 retired: 528 → 500).
- Tags locked, frozen 8/8 with the accept list, walk 48/48 with challenges.

## Registry decisions (user, 2026-11-14)

- The C1 culture track is hidden, so five C1 skills were taught only on hidden screens. `metaphor` is now taught in c1-06-01 and `satire-parody` in c1-05-04. `optative-subjunctive`, `conclusive-markers` and `framing-markers` are unmet in core: rewritten away.
- `epistemic-hedging` is now taught in c1-03-02. Its old screen, c1-01-04, teaches inferential connectors, and its items are retagged to `additive-connectors` / `concessive-postpositions`.
- `rhetorical-questions` is now taught in c1-04-04, not Unit 16; 6 items retagged.
- `official-register` stays in c1-08-03, which now presents *szíveskedjék* + infinitive and *… hivatkozással* (2 items).

## Facts corrected (reviewer-facts.md)

- Örkény was not in a Budapest cellar in 1944: he was a forced labourer from 1942 and a Soviet POW 1943–46. Story, screen and items rewritten; the unconfirmed title *Gondolatok a pincében* removed.
- Szerb has no volume *A varázsló eltűnik*: title removed.
- Babits/Benda: 1927 and 1928 confirmed. The meta paragraph about the learner removed.
- Mikszáth: the county-machine claim softened, and the unconfirmed "back from America" removed.
- All eight texts are generator essays *about* an author; `source` now says so where the readers changed it.

## Reviewer changes to the readers' lists

- 4 "(check)" notes left in learner-facing screens and the story removed.
- 2 sentences in the Mikszáth and Babits stories rewritten: "a szöveg szerint" inside a story, and a "(check)" note.
- *úgy hírlik* dropped as an answer for an adverb slot.
- 4 challenge targets rewritten so each uses its lesson's form and met words; 2 more for unmet words.
- *üres érdekek*, the tautology *a felülvizsgálat … a jogok védelme*, an invented 15-day deadline, *armour*.
- One recap unit corrected (*tekintetében*: "from earlier units").

## What went wrong once, and was scripted

Reader B's extra lists carried only the fields they changed. Applied after the base lists minus the replaced ids, they dropped 19 reviewed questions, tags and categories, and the items reverted to the generator's text; 5 retired tags came back. Found by `lock_tags.py`. `scripts/stage_extras.py` now builds both stages and folds the base fields under each extra.

## Not verified

- Speaking steps, spoken challenge answers, wrong-answer paths and real audio.
- A native speaker's eye.
- Pilinszky's *Szög és olaj* date and the Weil link, and the year of Kosztolányi's *Nyelv és lélek*: removed or kept unspecific, not checked online.

## For the user

- **Vocabulary lists:** C1 lesson lists carry words no item uses (899 `vocab-unused` suspects in C1, 38 stems accepted here). Keep them as SRS-only words, or prune them? Accepted for now.
- **Unit 2 (syntactic-compression) teaches no skill of its own:** every lesson recaps B1/B2 forms with a C1 register point. Reader A asks whether it should get a new point per lesson.
- **Author labels:** each unit text's `author` field names the author it is about. Change it to "about <author>" across C1?
- **Next batches (decisions to ask ahead):** `epistemic-modality` is used in core Units 9 and 15 (taught in Unit 22), `evaluative-stance` in Units 12 and 23 (taught in Unit 26).
