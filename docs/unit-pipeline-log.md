# Unit pipeline: prompts, measurements, process reviews

How the reviewer (Claude) runs units through Sonnet agents, what each step
costs, and what changed at each review. **Every 2 finished units, the
reviewer reviews the process** (decided by the user 2026-10-13, under
time and usage pressure): add the units' numbers to the table, compare
with the previous rows, pick one or two changes that cut tokens or
reviewer work without losing defects, record them below, and apply them
to the next units. Repeated defects go into `docs/unit-agent-rules.md`
§ 6 at once; a defect a script could catch becomes a `check-content.py`
check.

## Pipeline (current)

1. **Stub unit** (repeated screens, shared checklists, generic content):
   Sonnet regenerates it. **Real content:** skip to 2.
2. Sonnet blind read (report only) on a read-only worktree.
3. Reviewer filters the report against the files, writes
   `imports/review/sonnet-reads/hu-a1-<unit id>.md` (Applied / Not taken),
   applies the fixes (small lists directly; long lists to a fixer agent),
   re-locks, freezes, commits through commit-gate.
At most 2 agents at once. A `challenges.json` conflict when taking a unit's
commit: `python scripts/merge_challenges.py hu <commit>`, then
`git cherry-pick --continue`; a `word-lesson-index.json` conflict: rerun
`python scripts/build_word_lesson_index.py hu` (revert the es-* indexes it
also rewrites). Worktrees: `git worktree add --detach
/home/user/parlour-<job> HEAD`, removed after.

## Prompt templates

Fill `<…>`. Each agent reads `docs/unit-agent-rules.md` and nothing else
by default. Reads end with "fix as an exact old → new replacement; quote
the option text whenever you name an option" and "Run ALL its § 5
commands"; regenerations get the unit's taught/not-yet-taught list
(verbs, cases, *is*, -ik, accusative) spelled out.

**Read.** "You are reviewing one unit of a Hungarian course (Parlour app)
for a learner who knows only English, to find everything wrong with it.
REPORT ONLY: edit, create or commit nothing; change no git or tool
config. Work only in `<folder>`. Unit `hu a1 <unit id>`: lessons
`<stems>`, story `<story stem>`; earlier units `<range>`. Read
`docs/unit-agent-rules.md` first; it is your rulebook (open other docs
only to settle a point it doesn't cover). Run its § 5 commands. Read
every exercise, screen, challenge, goal, checklist, speaking step and the
story, checking § 1–4 and every item of § 6. Skip what check-content
reports. Focus: `<unit-specific grammar to watch>`. Report grouped: 1.
Found by reading; 2. Metadata; 3. Challenges / goals / checklists; 4.
Doubtful. One line each: id, problem quoting the text, fix; mark
uncertain items (unsure). Don't pad."

**Regenerate.** "Regenerate hu a1 unit `<n>` `<unit id>` (`<stems>`) in
`<folder>`. Rulebook: `docs/unit-agent-rules.md`; shape:
`docs/course-generation-brief.md` § 2.2/2.3 (read only those). Rewrite
both screens per lesson, story, exercises, goals/checklists, challenges;
keep ids and stems. `<unit-specific points>`. Run § 5 checks, fix
everything, lock tags, don't freeze. Commit normally with start/finish
times; report the commit, per-lesson points, and Hungarian you are unsure
of."

**Fix.** "Apply the fix list `<file>` to hu a1 `<unit id>` in `<folder>`.
Rulebook: `docs/unit-agent-rules.md`. Apply every Applied item, nothing
under Not taken; re-lock; run § 5 checks; don't freeze; commit normally
listing each item."

## Measurements

| Date | Unit | Route | Regen / fix (tok, min) | Read (tok, min) | Real defects in read | Notes |
|---|---|---|---|---|---|---|
| 10-10 | 8 plurals-quantities | Sonnet regen (pilot A) | 251k, 16 | 153k, 4.5 | ~21 | |
| 10-10 | 9 possession | read → fixer (pilot B) | 298k, 23 | 159k, 7.5 | ~14 | |
| 10-13 | 8 + 9 | pilot fix lists, one Sonnet fixer | 142k, 4.5 | | | both units in one agent |
| 10-13 | 11 where-things-are | Sonnet regen | 267k, 14 | 155k, 5.5 | 9 applied | frozen; agent bypassed hooks (now forbidden) |
| 10-13 | 10 foundations-review | Sonnet regen | 245k, 9 | 187k, 5 | ~15 to filter | |
| 10-13 | 8 (second read) | | | 161k, 5 | 8 applied | found a wrong pilot fix-list item |
| 10-13 | 9 (second read) | | | **123k, 3.5** (rules sheet) | 10 applied, 1 false | first read on the rules sheet |
| 10-13 | 8 + 10 fixes | **Haiku** applies filtered lists | 118k Haiku, 2.5 | | all 17 items right | the one slip was in Claude's list |
| 10-13 | 9 fixes | Claude directly | | | | short list |
| 10-13 | 12 going-places | Sonnet regen (rules sheet) | 171k, 9 | 125k, 4.5 | 9 applied | |
| 10-13 | 13 everyday-actions | Sonnet regen (rules sheet) | 204k, 11 | 106k, 2 | 8 applied | read skipped 2 commands |
| 10-13 | 12 + 13 fixes | Haiku | 115k Haiku, 3 | | 16/17; 1 skipped, 1 wrong | both caused by Claude's list |
| 10-13 | 14 questions-negation | regen + § 6 self-check | 171k, 9 | 113k, 2.5 | 9 applied | |
| 10-13 | 15 daily-routine | regen + § 6 self-check | 214k, 12 | 135k, 4 | 11 applied | |
| 10-13 | 14 fixes | Haiku, exact old → new list | 74k Haiku, 1 | | 9/9 | |
| 10-13 | 15 fixes | Haiku, exact old → new list | 83k Haiku, 3 | | 11/11 | |
| 10-13 | 16 time-dates | read first (real content) | | 132k, 4 | 40+ | → regenerate |
| 10-13 | 16 time-dates | Sonnet regen | 177k, 10 | 112k, 3 | 6 applied | Claude applied directly |
| 10-13 | 17 frequency-word-order | verdict-first read → regen | 181k, 9 | 90k + 121k | 9 applied | read caught a reversed answer key |
| 10-13 | A1 story questions ×12 | Haiku translation | 77k Haiku, 1 | | 36 questions | for the English toggle |

Reads before unit 9's second read used the full docs (brief, AGENTS, spec, registry).

## Process reviews

### 2026-10-13 (after units 10, 11)

- Cost per finished unit ≈ 450k Sonnet tokens on either route; reads
  (150–190k) mostly re-read the same four docs. **Change:** this rules
  sheet replaces them for every agent; templates above replace hand-written
  prompts. Measure on unit 9's second read against the 155–187k reads.
- Reviewer's own cost: filtering by checking each claim in the files is
  where errors were caught (wrong pilot item, "Harminc éves" two-answer
  item), so it stays.
- Done: `check-content.py` `vocab-duplicate` (error); it also found
  *foto* twice in es-es/es-latam `a1-03-01-voc` (left for the Spanish A1 pass).
- Next candidates: a check for `distractor_skills` on non-word options (the Reader
  lexicon can tell a non-word); Haiku for applying an already-filtered
  fix list.

### 2026-10-13 (after units 8, 9, 10 frozen)

- **Rules sheet:** unit 9's read cost 123k / 3.5 min against 155–187k /
  5 min, with as many real findings (and one new class: challenge scenarios
  not naming the target's object). Keep it; every agent uses it.
- **Haiku for applying a filtered list:** 17/17 items right, 118k Haiku
  tokens, 2.5 min, no improvisation. Use Haiku for every fix list from now
  on; Sonnet only for regeneration and reads.
- **Reviewer slips found by the next step:** twice the reviewer's own list
  put `distractor_skills` on the wrong option (pilot a1-44 items; a1-38-check-2,
  where the option order differed). **Change:** a list item naming an option
  index must quote the option text, and the fixer checks the text matches
  before editing. Added to the rules sheet § 3.
- Reads still produce ~1 false claim each (*táskája* does not lengthen):
  filtering against the files stays.

### 2026-10-13 (after units 12, 13 frozen)

- **Cost per unit is down ~30%:** regeneration 171–204k (was 245–267k),
  read 106–125k (was 155–187k), Haiku fix ~58k Haiku. About 300k Sonnet +
  60k Haiku per stub unit, ~25 min wall time with two units in parallel.
  Projection for the 20 HU A1 units left: ~6–7M Sonnet tokens (was ~9M).
- **Remaining errors are the reviewer's fix lists:** a conditional item
  ("only if that is the exact text") made Haiku add *i, í* to a vowel list
  the screen's own tip contradicts; an item asked for `answers` next to
  `answer`, which the schema rejects (`answers` replaces `answer`).
  **Change:** fix-list items are exact old → new replacements, no
  conditionals; field shapes are checked against an existing item first.
- **Regenerators still write words whose meaning needs a form not yet
  taught** (*hallgat* alone = "is silent"). Added to rules § 6.
- **New checks (user: script every repeat defect):** `ds-on-answer`,
  `ds-own-skill` (0 hits course-wide: guards), `glued-blank` (HU suspect: a
  blank glued to a stem in *-a/-e* with a lengthening suffix as the answer;
  3 real hits in B1: b1-18-03.ex03, b1-26-05.ex02, b1-30-03.ex05; one false
  positive, a verb, b1-33-04.ex02).
- `unmet-word` now also scans challenge targets. (It briefly scanned
  stories too; the user ruled 2026-10-13 that stories may use unmet words.)
- **Next to try (units 14, 15):** have each regenerator run a self-check
  against rules § 6 and list what it checked, to see if the read finds
  fewer defects; keep two units in parallel.

### 2026-10-13 (after units 14, 15 frozen)

- **§ 6 self-check in regeneration: dropped.** Reads still found 9–11
  real defects per unit (same as without it) and regeneration cost the
  same or more (171k, 214k).
- **Reads propose exact old → new fixes: kept.** The fix list is then a
  near-copy, Haiku's pass fell to 74–83k / 1–3 min, all items right.
- **Real-content units: read first, then decide.** Unit 16's read found
  40+ defects (no challenges, generic checklists, forms taught later, an
  incoherent story): regenerate when a read finds more than ~30 or the
  challenges/checklists are missing or generic; else fix.
- **New checks this round:** `ds-on-answer`, `ds-own-skill`,
  `glued-blank`, and `unmet-word` over stories and challenge targets;
  `scripts/merge_challenges.py` for parallel-unit conflicts.
- Running cost per stub unit now ≈ 190k regen + 120k read Sonnet + 80k
  Haiku; ~4 units/hour with two agents.

### 2026-10-13 (after units 16, 17 frozen)

- **Verdict-first reads** on old units cost 90k (vs 130k) and decide
  regenerate/fix before anyone pays for a full defect list. Keep for every
  unit not yet read.
- **Regenerated units so far all needed regenerating** (8–17 except 9):
  units 18–33 are probably the same; verdict-first read stays as the gate.
- **Short fix lists (≤ ~8 text edits): the reviewer applies them directly**
  (unit 16, 17); Haiku only for longer lists — the agent's own setup
  (~50k) outweighs a few edits.
- **A read caught a reversed answer key** (a1-84-check-2) that every check
  passed. No script can tell which option is right; reads stay.
- **English toggle (user, 2026-10-13):** A1 comprehension questions in
  Hungarian with `questionEnglish`/`optionsEnglish`; done for units 1–7, 9,
  11–15, 17. The rest (units 8, 10, 16 need Hungarian questions; 18+ need
  English) is done by Sonnet once all units are finished (user).
