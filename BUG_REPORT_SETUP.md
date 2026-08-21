# Bug Report Feature — Setup

The flag button (bottom-right, every screen) files a GitHub issue directly
from the live site, tagged `bug-report`, with whatever context the app can
capture (lesson, step, language, tab) plus an optional note. It needs one
piece of setup before it will actually send anything: a GitHub access token
pasted into `engine/bugreport.js`.

**This embeds a real credential in a public, client-side file.** That's a
deliberate, discussed tradeoff — acceptable only because the audience today
is you and your girlfriend, both trusted. Read "Before this has any real
audience" at the bottom before sharing the site link more widely.

## 1. Create the token

1. Go to **github.com → Settings → Developer settings → Personal access
   tokens → Fine-grained tokens → Generate new token**
   (`https://github.com/settings/personal-access-tokens/new`).
2. **Name**: something like `parlour-bug-report`.
3. **Expiration**: pick something you're comfortable rotating — 90 days is
   reasonable. Note the date; when it expires the button will silently stop
   working until you generate a replacement.
4. **Repository access**: "Only select repositories" → choose
   `good-language-learning-app`. Not "All repositories."
5. **Permissions**: expand "Repository permissions" → set **Issues** to
   **Read and write**. Leave every other permission at "No access" —
   specifically, do *not* grant Contents, Administration, or anything else.
6. Generate the token and copy it (`github_pat_...`). GitHub only shows it
   once.

## 2. Paste it into the code

Open `engine/bugreport.js` and replace this line:

```js
const GITHUB_TOKEN = 'PASTE_YOUR_FINE_GRAINED_TOKEN_HERE';
```

with your actual token, then commit and push as normal (`git add`,
`git commit`, `git push`) so it reaches the live GitHub Pages site.

## 3. Verify

1. Open the live site, click the flag button, then "Report issue" (the
   quick path, no note needed).
2. Check `https://github.com/gergkar-gif/good-language-learning-app/issues`
   for a new issue titled `[Bug report] ...`, labeled `bug-report`.
3. If it doesn't show up: open the browser console on the click and look
   for the failed `fetch` — a 401 means the token is wrong or expired, a
   404 usually means the repository access scope wasn't set correctly.

## How reports get handled

Ask Claude to check for open issues labeled `bug-report` (e.g. "check for
new bug reports") and it will investigate and fix each one, or ask a
follow-up in the issue itself if the report doesn't reproduce or isn't
clear enough to act on. There's no fully automatic background watcher yet —
this is a manual "ask when you want a sweep" step for now, not a schedule.

## Before this has any real audience

Once anyone besides the two of you might use the site, the embedded token
becomes a real problem — anyone who opens the browser's dev tools can read
it and use it to create or edit issues on this repo (nothing more, given
the scoping above, but still unwanted). Before that happens, move
submission behind something that doesn't ship the token to the browser —
options include a small serverless function (e.g. a Cloudflare Worker or
Vercel function) that holds the token server-side and proxies the request,
or GitHub's own "New issue" prefilled-URL scheme (no token needed at all,
but requires the reporter to be logged into GitHub and click submit
themselves).
