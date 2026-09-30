# Bug Report Feature

The flag button (bottom-right, every screen) opens a small popup with the
context it can see automatically filled in — lesson, step, language, tab,
URL, timestamp. Tap "Report issue" for a one-tap flag with no typing, or
"Write in…" to add a note first. It submits silently in the background and
files a GitHub issue labeled `bug-report` — no GitHub login, no leaving the
app.

## Why a Cloudflare Worker

Filing a GitHub issue needs a GitHub token, and this is a static site with
no backend of its own — anything shipped to the browser is world-readable.
Two earlier approaches ran into that:

- **Embedding the token directly** in `engine/bugreport.js` — GitHub's own
  push protection rejected the commit outright, and would very likely have
  revoked the token anyway once its secret scanner found the same string
  served in plaintext by the live GitHub Pages site. Making the repo
  private doesn't fix this either: Pages serves its files publicly
  regardless of the repo's visibility (a private repo whose Pages site also
  stays private is a GitHub Enterprise–only feature).
- **No token at all**, opening GitHub's prefilled "new issue" link instead
  — safe, but it meant leaving the app, being signed into GitHub, and
  tapping "Submit new issue" yourself. Real friction on a phone.

A [Cloudflare Worker](https://developers.cloudflare.com/workers/) solves
both: it's a small serverless function that holds the token server-side, as
an encrypted secret the Worker's code never displays and the browser never
receives. The client just POSTs `{title, body}` to the Worker's URL, and
the Worker attaches the token and calls the GitHub API itself. Cloudflare's
free tier (no card required) is enough for two people occasionally flagging
bugs.

The Worker's source lives at
[`cloudflare-worker/bug-report-proxy.js`](cloudflare-worker/bug-report-proxy.js)
in this repo — it's not auto-deployed from here, though; you paste it into
Cloudflare's dashboard by hand (below). It also restricts requests by
`Origin` to the app's own domains, so the endpoint isn't a free-for-all
issue-filer for anyone else who finds the URL.

## One-time setup (~10 minutes)

1. Create a free account at [dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
   (no card needed).
2. In the dashboard sidebar, go to **Workers & Pages** → **Create** →
   **Create Worker**. Give it any name (e.g. `parlour-bug-report`) and
   click **Deploy** to scaffold it — you'll edit the code next.
3. Click **Edit code** to open the built-in editor. Delete the placeholder
   contents and paste in the full contents of
   [`cloudflare-worker/bug-report-proxy.js`](cloudflare-worker/bug-report-proxy.js)
   from this repo. Click **Deploy** (or **Save and Deploy**).
4. Create the GitHub token the Worker will use, if you don't already have
   one: [github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new) →
   fine-grained token, repository access limited to
   `gergkar-gif/good-language-learning-app`, permission **Issues: Read and
   write**. Copy the token — you won't be able to see it again.
5. Back in the Worker, go to **Settings** → **Variables and Secrets** →
   **Add** → name it `GITHUB_TOKEN`, paste the token, and mark it
   **Encrypt**. Save.
6. The Worker's overview page shows its public URL —
   `https://<worker-name>.<your-subdomain>.workers.dev`. Copy it.
7. In [`engine/bugreport.js`](engine/bugreport.js), replace the
   `WORKER_URL` placeholder near the top of the file with that URL, then
   commit and push.

That's it — the flag button will POST to the Worker from then on. If the
Worker is ever unreachable (not yet deployed, wrong URL, Cloudflare
outage), the popup falls back to a plain link that opens GitHub's prefilled
issue page instead, so a report is never a dead end.

## How reports get handled

Ask Claude to check for open issues labeled `bug-report` (e.g. "check for
new bug reports") and it will investigate and fix each one, or ask a
follow-up in the issue itself if the report doesn't reproduce or isn't
clear enough to act on.

There's also a scheduled cloud routine that does this automatically —
see `https://claude.ai/code/routines` for its current cadence and run
history, or ask Claude to check/adjust it.
