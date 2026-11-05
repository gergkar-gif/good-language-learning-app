# HU B2 culture batch: Units 26, 28 (reader A) and 30, 32 (reader B), 2026-11-05

No usage limit hit. Reader A 388,908 tokens (60 tool uses, 23 min), reader B 430,492 (52,
24 min): ~205k a unit. Text first, facts file per unit. The session's worker restarted once
during the review; nothing was lost (everything was committed).

## Counts

| Unit | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|
| 26 `pesti-humor` | 85 | 63 | 0 | **Bonbonnière on Teréz körút** (story, consolidation.ex02); 15 words listed | 0 / 5 accepted |
| 28 `hungarian-cinema` | 116 | 69 | 0 | **Szegénylegények set in 1869**; *mihelyt* items tagged `miutan-mielott` like *amint* (as core Unit 27 does), not the unit vocabulary; 12 words listed | 0 / 4 accepted |
| 30 `three-ts-censorship` | 107 | 85 | 0 | *sokszorosodik* for *sokszorosítódik* everywhere; 2 question stems (one printed the answer word); Beszélő "1981 őszén"; 7 words listed | 0 / 1 accepted |
| 32 `urbanists-populists` | 135 | 107 | 0 | Monor facts confirmed; 6 words listed | 0 / 3 accepted |

443 reader fixes applied plus 2 reviewer text fixes; 4 unit readings restitched; 24
challenges; 40 more words listed; 109 dictionary entries. Accepted at freeze: `vocab-unused`
per lesson (culture words). Walk 24/24 with challenges. validate --changed passes. B2 52/72
frozen.

## Found by the readers (applied)

- **All four units re-teach a core unit's grammar as new** and teach no skill of their own:
  Unit 26 the discourse particles (B2 Unit 25), Unit 28 the time clauses (B2 Unit 27), Unit 30
  agentless constructions and nominalisation (B2 Unit 29), Unit 32 the contrastive connectors
  (B2 Unit 31). Recaps added, screens titled "Recap". Each culture unit after a core unit
  replays it: a generator pattern (see the pipeline log).
- Politics: "szovjet megszállás" made "a szovjet csapatok jelenléte" in Units 30 and 32;
  regime intentions, "totalitárius", "zsarolás", "legvidámabb barakk" attributed; the
  Kétfarkú Kutya Párt judgement and the present-day sovereignty/federalism framing removed.
- Quotations from memory paraphrased: Karinthy's aphorism, Höfgen's line, "Kádárnak mennie
  kell" (the Társadalmi szerződés is widely quoted with it; kept as a paraphrase).
- "bizalmi szelep" → *biztonsági szelep*; *nem … -e*; *elutasításra lelt*; *megénekeltetője*;
  plural verbs with plural subjects; twin answers (*miközben/mialatt*, *amint/mihelyt*,
  *tartották/tekintették*, the *bár* family).

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
Whether a culture unit should keep five lessons that replay the preceding core unit is a
design question for the user (below).
