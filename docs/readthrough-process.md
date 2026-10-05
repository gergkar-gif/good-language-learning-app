# Skill-tag read-through: how to run it

How a level of the skill-tag read-through (ROADMAP 125 step 3) is run, so every
course and level is done the same way. Distilled from HU A1 (33 units) and HU A2
(44 units, 4,154 exercises), both finished 2026-10-05. The tagging rules
themselves are in [skill-tagging-spec.md](skill-tagging-spec.md) § "Read-through
conventions"; this file is about the workflow around them.

Applies to any course and level (HU B1–C1, ES A1 onward, a new language), and
to similar per-unit review passes that use subagents.

## Roles

- **Subagent (Sonnet), one per pair of units**, at most two running at a time
  (the user's two-subagent limit). It reads the units, writes a decisions file,
  fixes content defects in its own units' files, runs the check until clean,
  and reports. It never runs `apply_tags.py`, `lock_tags.py` or git writes.
  Haiku is too weak for the judgment calls; don't use it here.
- **Main session** reviews each unit with the filtered view, corrects
  decisions, applies, locks, validates, logs and commits.

Work in `C:/dev/parlour-claude` (see CLAUDE.md), never the Drive checkout.

## Before starting a level (do once, before the first unit)

1. **Fix the registry first.** For every skill at or below the level, find the
   first grammar screen in this level that teaches it and compare it with
   `taught_in`. List the mismatches for the user's sign-off (like ROADMAP 135
   and 138), apply them, rebuild with `python scripts/build_skill_registry.py`.
   In HU A2, 17 late `taught_in` screens produced ~150 "taught later" warnings
   that every subagent had to explain and the reviewer had to read past.
2. **Update the rule sheet** [readthrough-brief.md](readthrough-brief.md): fold
   any new conventions from the last level into it. It is the only rules
   document subagents read (not the spec, not ACHIEVED.md), so it must be
   complete and short. One page, one worked example per rule.
3. **Check `readthrough_check.py` covers the known patterns** (list below). A
   correction the reviewer makes more than twice should become a check.

## Per batch

1. Launch two subagents, each with two consecutive units, pointing at
   `docs/readthrough-brief.md` and a scratch folder for decisions files.
2. When one reports: run
   `python scripts/readthrough_review.py <course> <level> <unit> <decisions>`
   for each of its units. It hides unchanged vocabulary items and marks
   checker-flagged (`!`) and changed (`~`) lines. Read those, plus the
   subagent's "judgment calls" list. Use `--all` only if something looks off.
3. Correct decisions in the JSON, re-run `readthrough_check.py`, then
   `apply_tags.py` and `lock_tags.py`, and launch the next pair right away so
   the two slots stay busy.
4. Every ~4 units: add one ACHIEVED.md log entry per unit (tag counts, rules
   applied, content fixes, what was left), run
   `python scripts/validate-content.py --changed`, and commit **only those
   units' files** plus `tags.lock.json` and ACHIEVED.md (never `git add -A`: a
   running subagent's half-done edits would be swept in). Then
   `git pull --rebase --autostash origin master` and push.
5. Update ROADMAP 125's progress note at the halfway point and at the end.

## At the end of a level

- ACHIEVED.md "<course> <level> read-through complete" entry.
- New conventions → spec § "Read-through conventions" and the rule sheet.
- Thin skills (< 6 exercises), late `taught_in` screens and skill gaps → one
  new ROADMAP queue item for the user's sign-off.
- Tell the user it's a good point to start a new chat.

## Checks `readthrough_check.py` should run

Errors/warnings the subagent must clear before reporting. The ones marked
*(to add)* were reviewer corrections in HU A2; implement them before the next
level:

- unknown/retired slug, skill above level, every exercise decided (exists)
- category follows the tag on choice/fill-blank/builder/matching, including
  items whose category is `dialogue`/`writing` (exists)
- matching pairs tagged anything but vocabulary *(to add)*
- `ds` naming the item's own `teaches`, or a vocabulary skill *(to add)*
- `ds` on an item whose options are suffix names or patterns rather than word
  forms *(to add)*
- a wrong option beginning *Nem,* while the right one begins *Igen,* (or the
  reverse) not tagged `yes-no-questions` *(to add, warning)*
- `ik-verbs-dolgozom-not-dolgozok` on an answer that isn't a 1st-person
  singular *-m* form *(to add, warning)*
- the answer printed in the prompt or sentence *(to add)*
- a fill-blank whose answer carries a possessive or person ending but whose
  hint names no person *(to add, warning)*

## Cost reference (HU A2)

About 110k subagent tokens and ~2.5 min per unit when each subagent did one
unit and re-read the spec and log; ~10–15k main-session tokens per unit to
review every line. The setup above (one rule sheet, two units per subagent,
filtered review, registry fixed first, more checks) targets roughly 35–40%
fewer subagent tokens, half the review cost and ~40% less wall time at the
same or better quality.
