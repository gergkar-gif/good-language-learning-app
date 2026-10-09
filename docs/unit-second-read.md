# Second read of a finished unit: how to run it

How the reviewer (the main Claude session) runs the independent second read
that every unit gets before it is frozen (ROADMAP 153). Antigravity's side of
the work is [unit-finish-brief.md](unit-finish-brief.md); this file is the
reviewer's side. Set up 2026-10-09 after a test on two HU A1 units: a blind
Sonnet read found 5½ of the reviewer's 6 findings plus about 20 defects per
unit that Antigravity's pass and the reviewer had both missed. About a
quarter of its claims were wrong or judgement calls, so its report is always
filtered before anyone acts on it.

## The flow, per unit

Changed 2026-10-09 (from Run 4): the read comes **before** Antigravity's
pass, not after it. In runs 1–3 Antigravity finished a unit, the reader found
20–30 more defects, and Antigravity went through the unit a second time; its
own reading pass found little the reader didn't. Now there is one pass.

1. The reviewer runs the second read (below) on the unit **as it stands**:
   a Sonnet subagent, report only. Run `check-content.py` first and give the
   reader nothing from it; the reader reads blind.
2. The reviewer checks and filters the report into a fix list,
   `imports/review/sonnet-reads/<course>-<level>-<unit id>.md`, and commits
   it. Leave out what `check-content.py` already reports (length
   give-aways, `unmet-word`): Antigravity gets those from the checker.
3. Antigravity does the unit (brief steps 1–7) with the fix list in the same
   pass, freezes it, commits, pushes.
4. The reviewer spot-checks the unit (the changed options especially; that
   is where slips happen), fixes small things directly (unfreeze → fix →
   `lock_tags.py --update` → re-freeze with the same `--accept`s), and
   records it in the brief's review notes. A unit with bigger problems is
   unfrozen and sent back.

Units committed under the old order (finished, then read) keep it: their fix
lists are applied and then they are frozen.

## Running the read

- **Model: Sonnet** (`model: sonnet`, `subagent_type: general-purpose`).
  Haiku is too weak for the judgement calls. About 140–160k tokens a unit.
- **At most two at a time** (the user's limit). Run them in the background.
- **A read-only copy for each reader:** `git -C C:/dev/parlour-claude
  worktree add --detach C:/dev/parlour-sonnet-<n> origin/master`. Remove it
  afterwards (`git worktree remove --force …`). The reader works only there
  and never edits.
- **Spanish:** one reader per unit covers es-es and es-latam together
  (point it at both courses' files and tell it es-latam has no *vosotros*).

### The prompt

Fill in `<course>`, `<unit id>`, `<stems>`, the earlier units and the folder.

> You are reviewing one unit of a `<language>` language course (the Parlour
> app) for a learner who knows only English. Another agent will finish the
> unit using your findings; your job is an independent read to find
> everything that is wrong with it. REPORT ONLY: do not edit, create or commit any file. Work only
> inside the folder `<folder>` (absolute paths; `cd <folder> && …`).
>
> The unit is `<course>` `<level>` `<unit id>`: lessons `<stems>` (lesson,
> exercise, vocabulary and grammar files under `content/<course>/`,
> challenges in `content/<course>/curriculum/challenges.json` keyed by
> stem). Earlier units: `<list>`. "Met" is defined in
> `docs/unit-finish-brief.md` step 4.
>
> First read in full: `docs/unit-finish-brief.md` steps 2–4 and its review
> notes; `AGENTS.md` § "Exercise metadata"; `docs/skill-tagging-spec.md`
> § "Read-through conventions"; `skills/<lang>.json` for `taught_in`.
>
> Tools: `python scripts/check-content.py <course> <level> <unit id>`;
> `node scripts/render_lesson.js <course> <stems>` (every screen as the app
> builds it, including the generated speaking steps and the challenge);
> `node scripts/audit-reader-coverage.js <course> --story <story stem> --top 0`.
>
> Skip what `check-content.py` already reports (length give-aways,
> `unmet-word`): the other agent gets those from the checker. A lesson whose
> challenge is still the generic fallback will get one written; don't report
> that. The render may omit `*-review-*` exercises; read those in the
> exercise JSON.
>
> Read every exercise, challenge, goal, checklist, speaking step and the
> story. For each exercise check: correct, natural target language; exactly
> one right answer; only met words and forms; wrong options that break
> exactly one thing and don't give themselves away; and the metadata
> (`teaches` = the one skill a wrong answer shows; `distractor_skills` for
> every wrong option that is a real form of another skill, each entry still
> fitting its option's text; `category` follows the tag; `hint` needed, not
> the answer, person-pinned; `english` translates the completed sentence and
> fits only the right answer). For each challenge: the target answers the
> prompt with met words; the cues don't give the words; `canDo` is the
> lesson's own first checklist line.
>
> Report, grouped: 1. Found by reading; 2. Metadata; 3. Challenges / goals /
> checklists; 4. Checked and fine but doubtable. One line each: id, the
> problem quoting the text, your proposed fix. Mark anything uncertain
> "(unsure)". Don't pad.

For a blind check of a reader (or of a new model), point it at the commit
*before* the reviewer's own review, so the brief's review notes can't give
the findings away, and score its report against the reviewer's.

## Filtering the report

Verify before you pass anything on:

- **Check a sample of claims against the files** (the words a claim says are
  untaught: grep the vocabulary and grammar files up to that lesson).
- **Apply the "met" rule** from the brief: a vocabulary list or a grammar
  screen's subject at or before the lesson; a lesson's own grammar-example
  phrases are allowed. Readers tend to flag those phrases; drop such items.
- **Check engine claims in the engine.** In the test a reader said writing
  exercises would mark a pro-drop answer wrong; `structured-writing` isn't
  graded (the model answer is shown), so the claim was dropped.
- **Drop** parked items (sentence-builder word orders, ROADMAP 148(b)),
  deliberate near misses that are the lesson's point (*jó* / *jól*), and
  "(unsure)" items you don't agree with; list them under "Not taken" with the
  reason, so Antigravity doesn't redo the judgement.
- **Engine issues** (a generated screen is wrong, not the content) are the
  reviewer's: fix them in the engine for every course, bump `sw.js`
  `CACHE_VERSION` and the `?v=` in `index.html`.

The fix list is grouped like the report, every item concrete (id, problem,
fix), with a "Not taken" section at the end. Examples:
`imports/review/sonnet-reads/hu-a1-greetings-basic-interaction.md`,
`hu-a1-introducing-yourself.md`.
