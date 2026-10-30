# Project instructions

## Work in your own worktree, not the main checkout

The main checkout is `C:/dev/parlour` (moved off Google Drive 2026-10-08;
the old Drive folder is retired, don't use it). Antigravity edits files there
while Claude sessions run, and has wiped Claude's uncommitted work there
before. Claude edits and commits in its own worktree, `C:/dev/parlour-claude`.
Use absolute paths there even when the session opened in the main checkout.
A second Claude session running at the same time makes its own:
`git -C C:/dev/parlour worktree add --detach C:/dev/parlour-<task> origin/master`.
Commit there, then `git pull --rebase origin master` and
`git push origin HEAD:master`. commit-gate blocks git writes in the main checkout.

**Cloud sessions (Linux, claude.ai/code)** have no `C:/dev` folders and no
Antigravity: work in the session's own checkout (`git checkout --detach
origin/master` first) and put reader worktrees at `/home/user/parlour-read-a`
and `-b` (`git worktree add --detach <path> origin/master`; remove them
after). `.claude/hooks/session-start.sh` turns on the pre-push gate there.
The container can restart mid-task: anything not committed or written to a
file (an agent's reply, for one) can be lost.

**Everything goes on `master`, no other branches (user, 2026-10-30).** Commit
and push to `master` (`git push origin HEAD:master`), also when the session
was started on a feature branch: if a harness-named branch has commits, fast-
forward `master` to it and work on `master` from then on. The cloud git proxy
refuses branch deletes and tag pushes, so don't create branches you can't
remove; tell the user which branches are left for them to delete on GitHub.

## Session practices (learned on HU B1, 2026-10-30)

- **Commit as you go**, in small commits: every reader file the moment it
  arrives, every fact-check file, every applied batch. A restart loses the rest.
- **Use the wait.** While subagents run, do the reviewer's own read and fact
  check (pipeline doc § "Best practices"), not idle polling.
- **A subagent stopped by the usage limit is resumed, not replaced:**
  SendMessage to the same agent after the reset time its failure notice names.
- **Facts about today age.** Check present-day claims (offices, laws,
  procedures, figures) for changes since the content was written, not only
  for whether they were once true. The counties are *megye* again since
  1 October 2026.
- **Never quote a law, a speech or a poem from memory.** Quote it only from a
  source you could read; otherwise paraphrase it and say so to the user.
- **Shell safety:** `rm` with a shell variable in the path is blocked; use
  literal paths. Write reader scratch files to the scratchpad, not `/tmp`.

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

## Finishing units (release gate 1, ROADMAP 153)

Units are finished and frozen one at a time. The current method, prompt
templates, costs and the "before calling a level done" checklist are in
[docs/unit-pipeline-log.md](docs/unit-pipeline-log.md) § "Pipeline";
agents get [docs/unit-agent-rules.md](docs/unit-agent-rules.md) as their
only rulebook. Read both before running a unit. Never tell the user a level
is done from memory: run the checklist and say what it doesn't cover.
An issue that recurs gets a Python script (a `check-content.py` check, a
fixer that refuses rather than guesses, or a chore script) in the same
session, not another prompt: see the pipeline doc § "Script recurring
problems".

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
