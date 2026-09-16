# Project instructions

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
