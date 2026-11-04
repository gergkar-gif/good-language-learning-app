# HU B2 core batch: Units 17, 19, 21 (reader A) and 23, 25, 27 (reader B), 2026-11-04

No usage limit hit. Reader A 352,680 tokens (54 tool uses, 17 min), reader B 348,797
(60, 17 min): **~117k a unit**, the cheapest B2 batch so far.

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 17 `logic-paradox-abstract-reasoning` | 15 / 3 | 72 | 56 | 2 (tells; rewritten) | 3 second right answers (*Bárki jön is*, two all-conditional options), a *senki* tell, *önmagának* → *saját magának*, 9 items retagged `b2-cataphoric-clauses`, 5 words listed | 0 / 0 |
| 19 `mentorship-discipline-intellectual-growth` | 38 / 2 | 77 | 67 | 1 (goal line found twice; done by script) | `causative-verbal-derivations` moved (below), 2 words listed | 0 / 0 |
| 21 `unconscious-dreams-inner-conflict` | 9 / 0 | 96 | 82 | 2 (suffixes in an English option; goal line found twice) | *hiszen* before Unit 25 → *mert*, a hint, *sohasem*, 3 words listed | 0 / 0 |
| 23 `ingenuity-design` | 5 / 1 | 79 | 79 | 0 | a second right answer, a tag/category mismatch the validator caught, 2 words listed | 0 / 0 (1 accepted) |
| 25 `irony-satire` | 23 / 2 | 90 | 79 | 3 (tells; rewritten) | a grammatical wrong option, a length give-away, *ugyan* and *bezzeg* listed, 4 words listed | 0 / 0 (1 accepted) |
| 27 `visual-storytelling-perspective-time` | 18 / 2 | 89 | 83 | 0 | 2 second right answers (*…, eközben*; literary *a szabadságnak allegóriája*), 2 words listed | 0 / 0 |

501 fixes applied, 36 challenges (2 corrected: a `canDo`, *önmagának*), 20 words listed on
the first lesson using them (common words on no earlier list: *természetes*, *tűnik*,
*előző*, *félelem*, *jelenet* …), 164 dictionary entries (138 lemmas, 26 surface forms).
Accepted at freeze: *gyártás* (b2-12-05, used in the consolidation, which has no
vocabulary list), *bezzeg* (b2-13-02, taught on the screen). Walk 36/36 with
challenges. B2 14/72 frozen.

## Decided by the user (2026-11-04)

- `causative-verbal-derivations` `taught_in` b2-10-04 → **b2-10-01-a-gr** (same unit;
  lessons 01–03 teach and drill the causative): 32 `taught-later` errors gone.
- `b2-cataphoric-clauses` `taught_in` b2-18-01 (Unit 35) → **b2-09-04-a-gr** (Unit 17,
  *függetlenül attól, hogy*, *tekintet nélkül arra, hogy*): Unit 35's screen recaps it.
  Units 13 and 21 had their cataphoric uses rewritten before this move; they stay so.

## Judged by Claude

- Units 23 and 27 teach no new registry skill (they recap B1 *-andó/-endő*, *révén*,
  *céljából*, *miközben*, *amint*): not a defect (the B1 decision on skill-less units).
- *mintha* in Unit 25 lesson 04 is the B1 skill `mixed-conditionals` ("mixed conditionals
  and *mintha* clauses", B1 Unit 70), not the B2 `mintha` (Unit 61): kept.
- `discourse-particles` names *hiszen, ugyan, bezzeg*; its screen taught *hiszen,
  ugyebár, mégiscsak*: reader B's sentence on *ugyan … de* and *bezzeg* kept, both
  listed, so the screen teaches what the skill says.
- Classics: b2-09 (Örkény) and b2-10 (Babits) relabelled "Adaptation inspired by";
  *Magasiskola*'s year (1967) not verified (`reviewer-facts.md`).
