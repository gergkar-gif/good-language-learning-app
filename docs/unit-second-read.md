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

1. Antigravity finishes the unit (brief steps 1–5), commits it **unfrozen**
   and pushes. Check it reached `origin/master`; if it is only in the main
   checkout, push it from `C:/dev/parlour-claude` (`git checkout --detach
   <commit>`, then `git push origin HEAD:master`).
2. The reviewer runs the second read (below): a Sonnet subagent, report only.
3. The reviewer checks and filters the report into a fix list,
   `imports/review/sonnet-reads/<course>-<level>-<unit id>.md`, commits it,
   and adds a short review note to the brief.
4. Antigravity fixes every item, re-locks tags where they changed, freezes,
   commits, pushes.
5. The reviewer spot-checks the fixes (the new options especially; that is
   where slips happen), fixes small things directly (unfreeze → fix →
   `lock_tags.py --update` → re-freeze with the same `--accept`s), and
   records it in the brief's review notes.

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
> app) for a learner who knows only English. The unit has been finished by
> another agent; your job is an independent second read to find anything it
> missed. REPORT ONLY: do not edit, create or commit any file. Work only
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
