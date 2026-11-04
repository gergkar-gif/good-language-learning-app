# HU B2 culture batch: Units 10, 12 (reader A) and 14, 16 (reader B), 2026-11-04

No usage limit hit. Reader A 319,217 tokens (49 tool uses, 16 min), reader B 435,986 (60, 26
min): ~189k a unit. Text first, with a facts file per unit.

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 10 `bartok-kodaly` | 7 / 0 | 53 | 53 | 0 | 13 words listed | 0 / 5 accepted |
| 12 `visual-arts-modernism` | 7 / 0 | 60 | 56 | 0 | **El Greco** (not in the 1871 purchase) -> Rembrandt; 2 English summaries; 11 words listed | 0 / 5 accepted |
| 14 `the-martians` | 14 / 4 | 127 | 82 | 1 (a *senki* tell; rewritten) | **lesson 04 rewritten around *minél … annál*** (user's decision, below); a second right answer (*amennyire*); a challenge target; 17 words listed | 0 / 3 accepted |
| 16 `medical-pioneers` | 7 / 4 | 102 | 73 | 1 (an answer in the prompt; rewritten) | **14 counterfactual *ha*-clauses given *volna*** (the reader's own fix had made them plain past, with a tip saying that is correct); 11 words listed | 0 / 4 accepted |

345 fixes applied, 4 unit readings restitched, 24 challenges, 52 more words listed (the readers
listed ~300), 233 dictionary entries. Accepted at freeze: `vocab-unused` per lesson (culture
words). Walk 24/24 with challenges. No new B2 validator warning. B2 44/72 frozen.

## Decided by the user (2026-11-04)

- **Unit 14 lesson 04 taught `annyira-hogy` (*annyira / olyan mértékben …, hogy*), the core Unit
  63 skill.** The user chose to rewrite the lesson rather than move the skill: its screen,
  goal line, 2 items (ex03 now a vocabulary fill on *repüléstudomány*, ex04 a *minél … annál*
  choice), the writing prompt and the challenge target now use *minél … annál* (B2 Unit 13) and
  known forms; Unit 63 stays the skill's home.

## Found by the readers (applied)

- Unit 10 and 12 re-teach core grammar (*-gat/-get* from Unit 9; *-va/-ve*, *-ván/-vén* from
  Unit 11): recaps added, tags were right.
- Unit 14 lesson 03 taught C1 *feltéve, hogy* (rewritten to *azzal a feltétellel, hogy* /
  *amennyiben*); an invented condition put on Szilárd removed; *amennyiben* had been glossed
  "insofar as".
- Unit 16 lesson 03 taught C1 epistemic modals (*érezhetett*), rewritten with *valószínűleg* and
  the plain past; the Nobel committee and the actin/myosin claim corrected.

## Judged by Claude

- Facts: `reviewer-facts.md`.
- The counterfactual error in Unit 16 is a reader-introduced grammar error that the checker
  can't see: *Ha … fogadta, … átírhatták volna* (plain past in the condition). Standard Hungarian
  puts *volna* in both clauses. Rulebook § 6b now says so.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
