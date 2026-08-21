# Bug Report Feature

The flag button (bottom-right, every screen) opens a prefilled GitHub "new
issue" page — title, context (lesson, step, language, tab, URL, timestamp),
and an optional note, all filled in for you. Labeled `bug-report`
automatically. Click "Report issue" for a one-tap flag with no typing, or
"Write in…" to add detail first.

**No setup needed, and no secret involved.** An earlier version tried to
POST straight to the GitHub API with an embedded access token, but GitHub's
own push protection rejected that commit outright, and would very likely
have revoked the token anyway once its secret scanner found the same string
served in plaintext by the live GitHub Pages site — making the repo private
doesn't change that either, since Pages serves its files publicly regardless
of the repo's visibility (private-repo Pages that stays private is an
Enterprise-only feature). There is no way to hide a secret from GitHub's own
scanners in something a browser has to download and run, so this uses
GitHub's own prefilled-issue link instead. Nothing is embedded in the code
for anyone to find.

The one tradeoff: you need to be signed into GitHub, and the button opens a
new tab where you still have to click "Submit new issue" yourself — it's
not a silent one-click submission. That's the cost of not shipping a
credential to the public internet.

## How reports get handled

Ask Claude to check for open issues labeled `bug-report` (e.g. "check for
new bug reports") and it will investigate and fix each one, or ask a
follow-up in the issue itself if the report doesn't reproduce or isn't
clear enough to act on.

There's also a scheduled cloud routine that does this automatically —
see `https://claude.ai/code/routines` for its current cadence and run
history, or ask Claude to check/adjust it.
