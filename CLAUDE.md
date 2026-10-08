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

## Roles and subagents

Roles are in [AGENTS.md](AGENTS.md) § "Who does what": the user decides,
Claude manages, Antigravity does bulk work from briefs. **Never run more than
2 subagents at once**; count the running ones before launching. Small
mistakes in a worker's output can be fixed directly or by a Haiku subagent;
bigger ones go back through the brief.

## Project records: follow AGENTS.md

The rules for ROADMAP.md, ACHIEVED.md and the docs are in
[AGENTS.md](AGENTS.md) § "Project records", shared with Antigravity so both
agents keep the records the same way. In short: finished work always moves
to ACHIEVED.md in the same commit (whole items and finished parts; nothing
struck through stays in the roadmap); update every other entry that lists
the same work; write any new content rule or lesson-type fix into the
authoring docs so future content is generated right; queue findings with
their actual list; check the files before calling anything open or done.
