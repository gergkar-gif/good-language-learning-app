# Second read: hu a1 introducing-yourself (Sonnet, 2026-10-09)

Blind report-only read of the unit as Antigravity first froze it
(`c4bdb9030`), checked and filtered by Claude. The redo (`c51c54944`)
already fixed the a1-11 challenge, the a1-15-controlled options, the *az a*
options and a1-15-practice-3; skip anything already fixed. Fix every item
below. "Met" follows `docs/unit-finish-brief.md` step 4.

## Words and forms used before they are taught

- *hol* is taught in a1-13 (`spatial-questions-hol-hova`, `a1-13-a-gr`); before that it appears only in a1-07's own grammar example. Remove it from `a1-12-intro-1`, `a1-12-intro-2`, `a1-12-controlled-1` (option *hol*), `a1-12-controlled-4` (*Hol ő?*, also unnatural: *Hol van ő?*), `a1-12-check-1`, `a1-12-check-2`, and `a1-11-dialogue-2` (*Hol laksz?*, also a question offered as a reply). Replace with met near misses and **remove the matching `distractor_skills` entries** (they point at a skill taught a lesson later).
- *itt*, *lakom* before a1-13: `a1-11-dialogue-1` (*Én itt lakom.*), `a1-12-practice-3` (*Itt.*), `a1-12-dialogue-1` (*Itt Károly.*, also ungrammatical). Use met wrong replies (not *Ez Károly.* for *Ki ő?*: that is a fair answer).
- `a1-13-dialogue-2`: *Budapest vagyok.* (*Budapest* not taught before a1-15, and absurd). Use *Én Károly vagyok.* and drop its `van-zero-copula` entry.
- `a1-14-intro-2`: option *lakik* (3rd person, not taught in a1-14). Use a met word.
- `a1-14-check-1`: option *néni* (not taught). Use *ember* or *család*.

## Misleading content

- `a1-11-practice-4`, `a1-15-practice-4` (matching): the pair *van* = "he/she is" contradicts the unit's own rule (*Ő Anna*, no verb; `a1-15-check-1` marks *Ő Anna van.* wrong). Replace with *ő* = "he / she" (or *te* = "you").
- `a1-14-review-2`: the wrong option *Ő egy család.* is absurd. Use a met near miss.
- Trailing space inside the question of `a1-11-intro-1`, `a1-11-intro-2`, `a1-15-consolidation-1`, `a1-15-consolidation-6`.
- `a1-13-practice-2` (fill-blank, *lakom*): a new person-marked verb with no hint; add the hint *I live*.

## Metadata

- `a1-14-writing-2` (*Ki vagy?*): tagged the unit vocabulary skill; the same item elsewhere is `ki-and-mi`. Make it `ki-and-mi`.
- `a1-14-intro-1`, `a1-14-practice-3`, `a1-15-controlled-4`: `distractor_skills` `ki-and-mi` on *Ki laksz?* / *Mi laksz?*, which are not well-formed forms of another skill. Remove them (an ungrammatical option gets none).
- Wrong replies that answer *Ki?* (*Én Meg vagyok.*, *Ő Anna.*) under a *Hol?* question: record `ki-and-mi` consistently (`a1-13-dialogue-1` has none).
- `a1-15-dialogue-1`: the wrong option *Te hol laksz?* is a well-formed form of `spatial-questions-hol-hova`; record it.
- `a1-11-review-1`, `-2` review reading-hungarian words: tag them `a1-reading-hungarian-vocab`.
- Re-lock after the changes.

## Goals, checklists, challenges

- `a1-14` challenge: the prompt says "a good friend", the target has no *jó*; make them match. Check its `canDo` is the lesson's first checklist line.
- `a1-15`, `a1-15-consolidation`: the second checklist line (*…where they live*) is shared; give each lesson its own lines.

## Not taken (no action)

- Writing exercises "requiring" the full pronoun: structured-writing is not graded (the model answer is shown for comparison).
- Builder word orders: ROADMAP 148(b), parked.
- Story consistency (Károly asking Meg *Ki vagy?*; *Igen.* after *Én itt lakom.*): uncertain; report a proposal if you agree.
