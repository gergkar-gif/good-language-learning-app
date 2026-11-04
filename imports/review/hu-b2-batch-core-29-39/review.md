# HU B2 core batch: Units 29, 31, 33 (reader A) and 35, 37, 39 (reader B), 2026-11-04

No usage limit hit. Reader B 345,347 tokens (53 tool uses, 15 min; ~115k a unit).
Reader A finished just before a container restart, so its completion notice (and its
usage) was lost; its nine files survived in the worktree.

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 29 `censorship-ambiguity-indirect-expression` | 21 / 2 | 68 | 55 | 4 (2 length, a tell, a hint = answer; rewritten) | 2 length give-aways; *minden bizonnyal*, *hazudik*, *szorul* listed | 0 / 0 |
| 31 `ideological-debates-public-polemics` | 36 / 1 | 95 | 74 | 3 (2 length, a hint = answer; rewritten) | a risky wrong option (*… a feladat is*); *szakértő*, *hamis* listed | 0 / 0 |
| 33 `information-overload-rumor-verification` | 25 / 0 | 84 | 71 | 4 (3 length, a hint = answer; rewritten) | "he" for "the speaker" → "they"; *újságíró*, *hiteles*, *sérült* listed | 0 / 0 |
| 35 `rhetoric-framing-mass-persuasion` | 12 / 1 | 70 | 62 | 1 (a tell; rewritten) | a hint naming a case; *duplájára* | 0 / 0 (1 accepted) |
| 37 `landscape-belonging-regional-character` | 12 / 0 | 86 | 81 | 1 (a tell; rewritten) | a length give-away; *látható*, *táj* listed | 0 / 0 |
| 39 `social-mobility-class-opportunity` | 55 / 0 | 91 | 85 | 0 | 26 items retagged `b2-relational-compounds` (below); *felzárkózik* listed | 0 / 0 |

494 fixes applied, 36 challenges (1 `canDo` corrected), 11 words listed, 182 dictionary
entries (166 lemmas, 16 surface forms). Accepted at freeze: *üzenet* (b2-18-04). Walk
36/36 with challenges. B2 20/72 frozen.

## Decided by the user (2026-11-04)

- `b2-relational-compounds` `taught_in` b2-20-05 → **b2-20-01-a-gr** (same unit; lessons
  01–04 teach *rovására, javára, szempontjából, függvényében, híján*): the reader's 40
  vocabulary stopgap tags reverted, 26 items on the skill, 2 meaning questions stay
  vocabulary.

## Recurring, scripted

- **Dialogue prompts as text:** reader A wrote all 32 of its dialogue `prompt` fixes in the
  rendered form ("Speaker: text / Speaker: ____"), which crashed check-content.
  `check_fixes.py` now converts them to turns before sorting (refusing any turn without a
  "Speaker: " head).

## Judged by Claude

- Unit 29's *-ásra kerül* lesson is the B2 `agentless-constructions` skill, not the C1
  official register: kept.
- *cívis* replaces the unattested *cíviselem* (reader B; vocabulary, items, Unit 39 intro).
- Recaps checked by hand: *azzal a feltétellel, hogy* (b2-marslakok-03, B2 Unit 14), *attól,
  hogy* (B2 Unit 17) are right; the script reads only italicised single words.
- Classics: b2-16 (Ady), b2-19 (Illyés), b2-20 (Veres) relabelled "Adaptation inspired by";
  *Nero* 1921 is the Nyugat serial (`reviewer-facts.md`).
