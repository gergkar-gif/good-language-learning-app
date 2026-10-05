# Project instructions

## Work in your own worktree, not the Google Drive folder

Antigravity edits files in the main checkout (the Google Drive folder)
while Claude sessions run, and has wiped Claude's uncommitted work there
before. Claude edits and commits in its own worktree, `C:/dev/parlour-claude`.
Use absolute paths there even when the session opened in the Drive folder.
A second Claude session running at the same time makes its own:
`git worktree add --detach C:/dev/parlour-<task> origin/master`. Commit there,
then `git pull --rebase origin master` and `git push origin HEAD:master`.
commit-gate blocks git writes in the main checkout.

## Exercise metadata is required on all generated content

Every exercise you write or edit must carry the metadata the learner model
runs on. The full rules are in [AGENTS.md](AGENTS.md) § "Exercise metadata";
read them before generating content. In short:

- `category`: one of `vocabulary | grammar | reading | dialogue | writing |
  listening`. Hungarian lesson stages (`practice`, `controlled`, …) go in
  `stage`, never in `category`.
- `teaches`: exactly one slug, required unless `category` is `reading`,
  chosen by what a wrong answer shows: a tested form gets its grammar skill,
  a tested word gets the unit's vocabulary skill (`<level>-<unit id>-vocab`).
- **The skill list is frozen** (ROADMAP 125, docs/skill-tagging-spec.md).
  The source of truth is `skills/<lang>.json`; the course registries,
  `grammar-titles.json` and `skill-prereqs.json` are generated from it by
  `python scripts/build_skill_registry.py`, so never edit those by hand.
  Never add, merge, split or rename a skill without the user's sign-off and
  an entry in `skills/frozen-<lang>.json`; the validator fails otherwise.
- Grammar choice items get `distractor_skills` where a wrong option is a
  real form of another skill. A read and reviewed unit is locked with
  `scripts/lock_tags.py`; its tags then can't change silently.

`python scripts/validate-content.py --changed` checks all of this. Run it
before committing a unit, not only at push time, so a missing tag is caught
before a whole unit has been written without it. Rules the existing content
can't meet until the read-through (one tag, level, retired slugs, coverage)
are warnings; `--warnings` lists them.

**Starting a new language** (Polish, Czech, Slovak, French, German, …):
follow AGENTS.md § "Adding a new course" *before* writing content: unit ids
and `skills/<lang>.json` (families, levels, `taught_in`, `requires`, frozen
list) come first. The new course is held to exactly the same rules, and the
validator fails a course folder that has content but no schemas or tag
registry.

## Keep ROADMAP.md current

[ROADMAP.md](ROADMAP.md) is the durable record of what's shipped and what's
planned — not an automated log. No hook or CI job updates it; it only stays
accurate if whoever does the work edits it by hand.

After completing a plan item, a roadmap task, or any change worth a future
session knowing about, update ROADMAP.md before ending the session:

- Mark a "Current priority queue" item done (`~~item~~` with the date) if it
  was on that list.
- Add a dated entry to the relevant topic section (Content & curriculum,
  Workshop, Decks, etc.) describing what shipped, if it's a real feature or
  fix worth remembering later — not every small tweak needs one.
- If you find or fix something that reveals a gap worth tracking (a
  limitation, a deferred idea, a follow-up), add a new numbered entry to the
  "Current priority queue" section rather than leaving it only in a commit
  message or chat transcript.

Do this as part of finishing the work, not as an afterthought — a commit
message is not a substitute for the roadmap staying readable on its own.

## Archive finished queue items to ACHIEVED.md

[ACHIEVED.md](ACHIEVED.md) holds completed work moved out of ROADMAP.md's
"Current priority queue", so the active document doesn't grow forever
(split 2026-09-16, at 2,161 lines). When you strike through a queue item
as done, move its full entry to ACHIEVED.md in the same edit — don't leave
it sitting in the active queue. Keep its original item number (don't
renumber the items that stay behind; gaps in the numbering are expected
and fine, since the numbers are stable references other entries may cite).
This only applies to "Current priority queue" — the dated topic sections
(Content & curriculum, Workshop, Decks, etc.) stay as-is; they're living
documentation of how a feature evolved, not a queue to drain.

If moving an item leaves a dangling "see item N above"/"step N below"
reference elsewhere in ROADMAP.md, fix it to point at ACHIEVED.md instead
of leaving it broken.
