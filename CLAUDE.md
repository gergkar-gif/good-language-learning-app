# Project instructions

## Exercise metadata is required on all generated content

Every exercise you write or edit must carry the metadata the learner model
runs on. The full rules are in [AGENTS.md](AGENTS.md) § "Exercise metadata";
read them before generating content. In short:

- `category`: one of `vocabulary | grammar | reading | dialogue | writing |
  listening`. Hungarian lesson stages (`practice`, `controlled`, …) go in
  `stage`, never in `category`.
- `teaches`: required unless `category` is `reading`. Use existing canonical
  slugs from `content/<course>/indexes/skill-registry.json`; vocabulary
  exercises get the unit's vocabulary-theme slug, not a grammar skill. Add
  a new slug only for a genuinely new reusable skill, never a unit- or
  topic-specific one (`past-tense-unit24`), and give a new grammar skill a
  title in `grammar-titles.json` in the house style.

`python scripts/validate-content.py --changed` checks all of this. Run it
before committing a unit, not only at push time, so a missing tag is caught
before a whole unit has been written without it.

**Starting a new language** (Polish, Czech, Slovak, French, German, …):
follow AGENTS.md § "Adding a new course" *before* writing content. The new
course copies the reference schemas, gets its own `skill-registry.json`,
and is held to exactly the same metadata rules. The validator fails a
course folder that has content but no schemas or tag registry.

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
