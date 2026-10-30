# HU B2 pilot: Units 1 and 3 (2026-10-30)

Two Sonnet readers, one core unit each (`batch_setup.py b2 … A=1 B=3 --course hu`).
Both stopped at the 5-hour limit within three minutes, before writing a file,
and were resumed after the reset (04:50 UTC). Reports, fix lists and challenge
drafts are in this folder; `reviewer-facts.md` has the classics checked.

## Cost

| Reader | Unit | tokens (resumed run) | tool uses | minutes |
|---|---|---|---|---|
| A | 1 `nuance-focus-emphasis-narrative` | 201,538 | 8 | 4.3 |
| B | 3 `memory-nostalgia-sensory-description` | 190,621 | 6 | 3.8 |

The first runs' usage was lost with the limit (both ran ~3 minutes, reading
the rulebook and sheet). **~200k a unit at one unit per reader**, against the
HU B1 pilot's 257k (language) and B1 core's ~109–194k at three per reader.

## Counts

| Unit | baseline errors / suspects | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 1 | 17 / 1 | 70 | 49 | 2 (answer in prompt; length) | 3 dialogue items (*hanem te*, two person-fault options, one reply that didn't answer), 2 rejected rewritten, 3 challenges, *csak* recap, *vendéglő* → *étterem* ×2 | 0 / 0 |
| 3 | 69 / 2 | 87 | 55 | 0 | *felbukkanó* → *gördülő*, *hegedűs* → *zenész* | 0 / 0 |

55 dictionary entries (50 lemma glosses, 5 surface forms); 12 challenges;
no checklists missing; no glued blanks; walk 12/12 with challenges.
Unit 1 frozen; **Unit 3 applied and locked but not frozen**: its tags depend
on the user's decision below.

## What the B2 generator gets wrong (both units)

- **A core unit teaches the next culture unit's skill.** Unit 3 is built
  on expanded pre-nominal participial phrases (*a sötétben nesztelenül
  tovatűnő postakocsi*), the skill `participial-clauses`, whose screen is
  b2-szecesszio-02 (Unit 4): 66 `taught-later` errors, every item. Unit 1
  lesson 3 teaches contrastive topic (*Ami … illeti*, *viszont*), the skill
  `b2-contrastive-topic` of Unit 2. Unit 1 lesson 1 used preverb inversion
  before lesson 2's screen.
- **Known material presented as new:** the focus slot (A1
  `basic-hungarian-word-order`), *-ó/-ő* and *-t/-tt* participles (B1 Units
  11 and 3), *viszont* / *ezzel szemben* (B1 Unit 21), prefix separation
  (A2 Unit 10). Readers added recaps; one named the wrong unit (*csak* "from
  A2 Unit 5", which teaches *nem csak … hanem*).
- **~60 unmet words a unit** in items and options (core units rewrite them).
- Second right answers among wrong options (natural replies, free word
  order), wrong options failing on person rather than the tested form,
  meta questions with absurd options, a "B2-C1" label, a wrong grammar
  claim (an active 3pl verb called passive), invented facts in challenge
  drafts (a "new dress", Pacsirta "doesn't like music").
- Fix counts (70, 87) are in the B1 core range (~64–74); the per-unit
  checker baselines vary from 17 to 69 errors.

## Retags

Unit 1 lesson 1's focus items → `basic-hungarian-word-order` (its title is
"focus position before the verb"); *viszont* items → `adversative-contrast`;
*Ami … illeti* → unit vocabulary. Unit 3's 66 `participial-clauses` items →
`present-participle` / `past-participle-adjective` (B1) where a wrong answer
is a wrong participle, the unit vocabulary skill where it is the phrase's order.

## For the user

**`participial-clauses` (and `b2-contrastive-topic`): where are they taught?**
Unit 3 (core) teaches expanded participial phrases on every screen before
Unit 4 (culture), the skill's `taught_in`, does; the readers' retags make the
checker pass but leave the B2 pattern in Unit 3's screens before its screen.
Options: (a) move `participial-clauses` `taught_in` to b2-02-01-a-gr (Unit 3;
Unit 4 then recaps it; a registry change, your sign-off); (b) keep the
registry and leave Unit 3 as applied (participle forms tagged with the B1
skills, the expanded order as vocabulary); (c) rewrite Unit 3 to plain
participles and relative clauses (a second pass, ~200k). Claude recommends
(a): Unit 3 comes first in the app and teaches the pattern fully. The same
question, smaller, for `b2-contrastive-topic` (Unit 1 lesson 3 vs Unit 2).
