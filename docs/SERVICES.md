# Services: Cloudflare Workers and third-party setup

Parlour is a static site with no backend of its own, so anything shipped to the
browser is world-readable. Everything that needs a secret, a database or an AI
model runs in a small [Cloudflare Worker](https://developers.cloudflare.com/workers/)
whose source lives in [`cloudflare-worker/`](../cloudflare-worker/). The Workers
are **not auto-deployed** from this repo: you paste the source into Cloudflare's
dashboard by hand, then put the Worker's URL into the client file named below.

| Service | Worker source | Client | What it does |
|---|---|---|---|
| [Bug reports](#bug-reports) | `bug-report-proxy.js` | `engine/bugreport.js` | Files a GitHub issue labelled `bug-report` from the flag button |
| [Cloud sync](#cloud-sync-and-sign-in) | `sync-worker.js`, `sync-schema.sql` | `engine/sync.js` | Email magic-link login plus backup and restore of progress (D1 database, Resend email) |
| [Google Sign-In](#google-sign-in) | `sync-worker.js` (`/auth/google`) | `engine/sync.js` | 1-tap login that shares the same accounts as the magic link |
| [Grader](#grader) | `grader-worker.js` | Writing Studio, Open Production drills | CEFR-aligned feedback on writing and speaking (Workers AI) |
| [Word gloss](#word-gloss-ai-fallback) | `gloss-worker.js` | `engine/gloss-ai.js` | A machine-suggested gloss when a tapped word has no dictionary entry (Workers AI + a KV cache) |
| [Speech-to-text](#speech-to-text) | `stt-worker.js` | Speaking drills and lessons | Whisper transcription of the learner's recording on mobile |

All five run on Cloudflare's free tier with no card. The two Workers AI services
(grader, STT) also fall back gracefully when the Worker is unreachable or over
quota: the grader degrades to the built-in local grader, and the bug-report popup
falls back to a plain link to GitHub's prefilled issue page.

## Creating a Worker (shared steps)

Every service below starts the same way:

1. Sign in at [dash.cloudflare.com](https://dash.cloudflare.com) (free account).
2. **Workers & Pages** then **Create** then **Create Worker**. Give it the name
   suggested in its section and click **Deploy** to scaffold it.
3. **Edit code**, delete the placeholder, paste the full contents of the Worker
   source file from `cloudflare-worker/`, then **Deploy**.
4. Do the service-specific bindings and secrets (**Settings** then **Bindings**
   or **Variables and Secrets**; mark secrets **Encrypt**).
5. Copy the Worker's public URL, `https://<worker-name>.<your-subdomain>.workers.dev`,
   from its overview page, put it in the client file, then commit and push.

The same pattern applies to the **Workers AI binding** used by the grader and STT:
**Settings** then **Bindings** then **Add** then **Workers AI**, with the variable
name set to exactly `AI`.

---

## Bug reports

The flag button (bottom-right, every screen) opens a small popup with the
context it can see automatically filled in: lesson, step, language, tab, URL,
timestamp. "Report issue" is a one-tap flag; "Write in..." adds a note first. It
submits silently and files a GitHub issue labelled `bug-report`, with no GitHub
login and no leaving the app.

**Why a Worker.** Filing an issue needs a GitHub token. Embedding it in
`engine/bugreport.js` was rejected by GitHub's push protection (and the token
would have been revoked once served in plaintext by GitHub Pages; a private repo
does not help, since Pages serves its files publicly regardless). Opening
GitHub's prefilled "new issue" link instead is safe, but means leaving the app
and submitting by hand. The Worker holds the token as an encrypted secret; the
client just POSTs `{title, body}` and the Worker calls the GitHub API. It
restricts requests by `Origin` to the app's own domains.

**Setup (~10 minutes).** Worker name `parlour-bug-report`, source
`bug-report-proxy.js`. Then:

1. Create a fine-grained GitHub token at
   [github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new),
   repository access limited to `gergkar-gif/good-language-learning-app`,
   permission **Issues: Read and write**. Copy it; it is shown once.
2. In the Worker: **Settings** then **Variables and Secrets**, add `GITHUB_TOKEN`
   with the token, **Encrypt**.
3. Put the Worker URL in `WORKER_URL` near the top of `engine/bugreport.js`.

**Handling reports.** Ask Claude to check for open `bug-report` issues; it
investigates and fixes each one, or asks a follow-up in the issue. A scheduled
cloud routine also does this automatically (see
`https://claude.ai/code/routines` for cadence and run history).

---

## Cloud sync and sign-in

My Journey's Account card lets a learner email themselves a login link, then back
up progress to the cloud or restore it on another device: an email field and two
buttons (**Back up now** / **Restore from cloud**), no password. It is opt-in and
last-write-wins: nothing syncs in the background, and restoring overwrites local
data with the last backup (see the header comment in `engine/sync.js` for why a
per-device merge is not built).

**Why a separate Worker, and why Resend.** It needs its own database
([D1](https://developers.cloudflare.com/d1/)) for login tokens and backups, and
it must send email. Cloudflare's outbound email is paid-plan only, so magic links
go through a free [Resend](https://resend.com) account (3,000 emails/month).
Resend's sandbox sender only delivers to the account owner, so the domain
`parlour.me.uk` was registered and verified in Resend (DNS records added in
Cloudflare's DNS panel; any CNAME must be **DNS only**, grey cloud).

**Setup (~20 minutes).** Worker name `parlour-sync`, source `sync-worker.js`.

1. **D1 database.** **Workers & Pages** then **D1 SQL Database** then **Create
   Database** (e.g. `parlour-sync`). In its **Console**, run the contents of
   `cloudflare-worker/sync-schema.sql` (creates `magic_links` and `users`).
2. **Resend.** Create an API key; add and verify the sending domain.
3. **Create the Worker** (shared steps above).
4. **Bind D1.** Worker **Settings** then **Bindings** then **Add** then **D1
   Database**, pick the database, variable name exactly `DB` (the code reads
   `env.DB`).
5. **Secrets**, both encrypted: `JWT_SECRET` (any long random string, used to sign
   session tokens) and `RESEND_API_KEY`.
6. Make sure the Worker's `RESEND_FROM` is an address on the verified domain (e.g.
   `noreply@parlour.me.uk`) and re-deploy, so it works for any real email address.
7. Put the Worker URL in `WORKER_URL` near the top of `engine/sync.js`.
8. **Optional bot check (Turnstile).** In the Cloudflare dashboard create a
   **Turnstile** widget, put its public site key in `TURNSTILE_SITE_KEY` in
   `engine/sync.js`, and add the widget's secret as the encrypted Worker secret
   `TURNSTILE_SECRET_KEY`. The Worker skips verification entirely when that secret
   is unset (and the client skips the widget when the site key is empty), so
   sign-in keeps working unprotected until both exist.

**Trying it out.** My Journey, then **Account**: enter an email, **Send me a login
link**, open the link from your inbox (check spam). You land back signed in.
**Back up now**, then optionally clear the site's local storage and **Restore from
cloud** to prove the round trip.

### Google Sign-In

1-tap Google Sign-In sits alongside the magic link. The browser gets an OpenID
Connect credential from Google Identity Services (loaded lazily) and sends the ID
token to the Worker's `/auth/google`. The Worker verifies it against Google's
tokeninfo endpoint (audience, issuer, expiry, verified email), maps the email to
the same D1 `users` table and issues the same HMAC-SHA256 JWT as the magic link,
so the same email shares one cloud backup either way.

**Setup (~10 minutes).**

1. **Google Cloud Console.** Create or select a project (e.g. `parlour-app`).
   - **APIs & Services** then **OAuth consent screen**: user type **External**,
     app name `Parlour`, your email for support and developer contact. No extra
     scopes are needed. While the app is in Testing, add your Google address under
     **Test users**, or publish to Production when ready.
   - **Credentials** then **Create Credentials** then **OAuth client ID**, type
     **Web application**, name `Parlour Web Client`. Under **Authorized
     JavaScript origins** add `https://parlour.me.uk`,
     `https://gergkar-gif.github.io`, `http://localhost:8131` and, optionally,
     `http://localhost:3000`. Copy the **Client ID** (ends in
     `.apps.googleusercontent.com`).
2. **Worker.** In the `parlour-sync` Worker, **Settings** then **Variables and
   Secrets**, add `GOOGLE_CLIENT_ID` with the Client ID. If `sync-worker.js`
   changed locally, paste it into **Edit code** and **Deploy** again.
3. **Client.** Put the Client ID in `GOOGLE_CLIENT_ID` near line 40 of
   `engine/sync.js`, then commit and push.

**Verifying.** Open Parlour (`https://parlour.me.uk` or `http://localhost:8131`),
go to **Journey** then **Account**. The **Sign in with Google** button appears
above the magic-link form. After signing in, your email shows under Account, the
backup and restore buttons are active, any earlier backup for that email is kept,
and on a new device with no local progress the cloud backup is restored
automatically.

---

## Grader

The **Writing Studio** (Workshop) and **Open Production Drills** evaluate writing
and speaking with CEFR-aligned formative feedback, without AI keys in the browser:

- The browser builds the prompt and POSTs to
  `https://parlour-grader.gergkar.workers.dev/grade`.
- The Worker binds to Cloudflare Workers AI (`env.AI`), calls
  `@cf/meta/llama-3.3-70b-instruct` (or the configured model) and returns the
  CEFR assessment JSON.
- If the Worker is offline, unreachable or over its daily quota, Parlour degrades
  to the built-in deterministic local grader (word count, sentence complexity,
  punctuation, structural targets), so exercises never crash.

**Setup (~3 minutes).** Worker name `parlour-grader` (so the URL is
`https://parlour-grader.<your-subdomain>.workers.dev`), source
`grader-worker.js`, plus the `AI` binding.

**Verifying.**

```bash
curl.exe -X POST https://parlour-grader.gergkar.workers.dev/grade -H "Content-Type: application/json" -d "{\"prompt\":\"Ping\"}"
```

A deployed Worker returns a JSON response from Workers AI rather than error code
`1042`. In the app, open **Workshop**, launch **Writing Studio** and submit a
short sentence: it shows CEFR scoring, vocabulary commendations and grammar
guidance.

---

## Word gloss (AI fallback)

When a learner taps a word that has no dictionary entry, no morphological reading and
is not a name, the Reader asks this Worker for the base form and a short English gloss,
and shows it labelled "machine suggestion". It is never saved to a deck. If the Worker
is unreachable, over its daily cap or unsure, the popup keeps saying "Not in the
dictionary yet", so the feature can only add help, never remove it.

- The client sends only the tapped word, its sentence and the language.
- Answers are cached in a KV namespace, so each word is generated once for every learner
  (an "unsure" answer is retried after a week). The browser also remembers answers
  (`glossAi:*` in localStorage), so a second tap is instant.
- A daily cap (default 600 uncached model calls) protects the free Workers AI allowance.
  Requests from origins other than the app's own domains and localhost are refused.
- Switch it off on one device with `localStorage.setItem('parlour_gloss_endpoint', 'none')`.

**Setup (~10 minutes).** Worker name `parlour-gloss` (the client's default address is
`https://parlour-gloss.gergkar.workers.dev/gloss`), source `gloss-worker.js`.

1. **Create the Worker** (shared steps above).
2. **Workers AI.** Add the `AI` binding as described above.
3. **KV cache.** **Workers & Pages** then **KV** then **Create a namespace**
   (`parlour-gloss-cache`). In the Worker, **Settings** then **Bindings** then **Add**
   then **KV namespace**, variable name exactly `GLOSS_CACHE`.
4. **Optional.** A plain variable `GLOSS_DAILY_CAP` to change the daily cap, and an
   encrypted secret `EXPORT_TOKEN` (any long random string) to enable `/export`.
5. If your Worker URL differs from the default, change `DEFAULT_ENDPOINT` in
   `engine/gloss-ai.js`.

**Verifying.**

```bash
curl.exe https://parlour-gloss.gergkar.workers.dev/health
curl.exe -X POST https://parlour-gloss.gergkar.workers.dev/gloss -H "Origin: https://parlour.me.uk" -H "Content-Type: application/json" -d "{\"word\":\"elnyomta\",\"lang\":\"hu\",\"sentence\":\"A hatalom elnyomta a nepet.\"}"
```

The first answers `{"status":"ok","service":"parlour-gloss",...}` with both bindings
reported true; the second returns `{"found":true,"lemma":"elnyom",...}` and, called again,
`"cached":true`.

**Turning taps into dictionary entries.** With `EXPORT_TOKEN` set, the words learners
actually tapped can be reviewed and promoted:

```bash
set GLOSS_EXPORT_TOKEN=<the secret>
python scripts/fill-dictionary-gaps.py pull-ai hu
```

That writes `imports/dictionary/gap-batches/hu-ai-cache.reply.txt`. Skim it, delete any
line you don't trust, then `python scripts/fill-dictionary-gaps.py import <that file> hu`.
The long tail of rare words fills itself, a little at a time, in the order people meet it.

---

## Speech-to-text

Speaking drills and lessons give automated pronunciation evaluation and a "Listen
to your recording" comparison (your voice next to the model voice).

**Why a Worker.** On desktop the Web Speech API can run alongside `MediaRecorder`.
On iOS and Android the microphone is single-client: opening `getUserMedia` to
record starves `webkitSpeechRecognition` (silence, then a timeout), and giving
speech recognition the mic prevents capturing audio to replay. So on mobile:

1. The client records clean audio with `MediaRecorder` only.
2. An audio blob URL is created straight away, arming the **Your Voice** button.
3. The blob goes to `parlour-stt`, which runs `@cf/openai/whisper-large-v3-turbo`
   on the Workers AI free tier (10,000 free neurons a day, about 200-500 speaking
   evaluations).
4. The returned transcript is scored word by word against the target prompt.

**Setup (~3 minutes).** Worker name `parlour-stt` (endpoint
`https://parlour-stt.<your-subdomain>.workers.dev/transcribe`), source
`stt-worker.js`, plus the `AI` binding.

**Verifying.**

```bash
curl.exe https://parlour-stt.gergkar.workers.dev/health
```

Expected:

```json
{"status":"ok","service":"parlour-stt","model":"@cf/openai/whisper-large-v3-turbo","workersAiAvailable":true}
```

After that, any speaking drill or oral challenge records cleanly on mobile and
desktop, scores pronunciation with Whisper, and lets you tap **Your Voice** to
listen back.
