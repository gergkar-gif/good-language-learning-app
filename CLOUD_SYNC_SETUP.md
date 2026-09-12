# Cloud Sync Feature

My Journey's "Account" card lets a learner email themselves a login link,
then back up their progress to the cloud or restore it on another device.
No password, no account screen elsewhere in the app — just an email field
and two buttons (**Back up now** / **Restore from cloud**).

It's opt-in and last-write-wins: nothing syncs automatically in the
background, and restoring overwrites local data with whatever was last
backed up (see `engine/sync.js`'s own header comment for why a smarter
per-device merge isn't built yet).

## Why a second Worker, and why Resend

This reuses the same [Cloudflare Worker](https://developers.cloudflare.com/workers/)
pattern as the bug-report feature (see `BUG_REPORT_SETUP.md`) — a small
serverless function holding secrets server-side that the browser never
sees — but it's a **separate Worker** (`cloudflare-worker/sync-worker.js`),
since it does something genuinely different: it needs its own database
([D1](https://developers.cloudflare.com/d1/), Cloudflare's serverless SQL)
to store login tokens and each learner's backed-up data, and it needs to
**send an email**.

That last part is why this also needs a free [Resend](https://resend.com)
account: Cloudflare's own outbound email sending is gated to their paid
Workers plan, so a magic-link email has to go through a separate
transactional-email API. Resend's free tier (3,000 emails/month) covers
this comfortably. Resend's own sandbox sender (`onboarding@resend.dev`)
only delivers to the Resend account's own email, which is enough to
smoke-test the flow but not for anyone else to sign in — sending to
arbitrary emails needs a verified domain, which is why the domain
`parlour.me.uk` was registered and verified in Resend (a handful of DNS
records, added in Cloudflare's own DNS panel since that's also where the
domain was bought).

## One-time setup (~20 minutes)

You already have a Cloudflare account and a deployed Worker from the
bug-report setup — this reuses that account, just adds a new Worker and
database inside it.

1. **Create the D1 database.** Dashboard sidebar → **Workers & Pages** →
   **D1 SQL Database** → **Create Database**. Name it anything (e.g.
   `parlour-sync`).
2. **Run the schema.** Open the new database → **Console** tab → paste in
   the full contents of
   [`cloudflare-worker/sync-schema.sql`](cloudflare-worker/sync-schema.sql)
   and run it. This creates the two tables (`magic_links`, `users`).
3. **Create a Resend account** at [resend.com](https://resend.com) (no
   card needed for the free tier). Dashboard → **API Keys** → **Create API
   Key** → copy it. Also add and verify a domain (**Domains** → **Add
   Domain**) — the DNS records it asks for go in Cloudflare's DNS panel
   for that domain; make sure any CNAME it gives you is set to **DNS
   only** (grey cloud), not proxied.
4. **Create the Worker.** Dashboard → **Workers & Pages** → **Create** →
   **Create Worker**. Name it `parlour-sync` (or anything), **Deploy** to
   scaffold it.
5. **Bind the D1 database to the Worker.** On the Worker's page → **Settings**
   → **Bindings** → **Add** → **D1 Database** → pick the database from
   step 1, and set the **Variable name** to exactly `DB` (the Worker code
   reads `env.DB`).
6. **Paste the Worker code.** **Edit code** → delete the placeholder →
   paste in the full contents of
   [`cloudflare-worker/sync-worker.js`](cloudflare-worker/sync-worker.js)
   from this repo → **Deploy**.
7. **Set the two secrets.** Worker → **Settings** → **Variables and
   Secrets** → **Add**, twice, both marked **Encrypt**:
   - `JWT_SECRET` — any long random string (a password generator's output
     is fine; this is never shown to anyone, just used to sign session
     tokens).
   - `RESEND_API_KEY` — the key from step 3.
8. **Copy the Worker's URL** from its overview page —
   `https://<worker-name>.<your-subdomain>.workers.dev`.
9. In [`engine/sync.js`](engine/sync.js), replace the `WORKER_URL`
   placeholder near the top of the file with that URL, then commit and
   push.

That's it — My Journey's Account card will start working from then on.

## Trying it out

1. Open the app, go to **My Journey**, scroll to **Account**, enter any
   email address, **Send me a login link**.
2. Check that inbox (and spam folder) for an email from "Parlour," click
   the link.
3. You should land back in the app signed in. **Back up now**, then
   (optionally, to prove it round-trips) clear the site's local storage
   and **Restore from cloud**.

Since `parlour.me.uk` is verified in Resend, this now works for any real
email address, not just the Resend account's own — as long as the
Worker's `RESEND_FROM` has been updated to an address on that domain
(e.g. `noreply@parlour.me.uk`) and re-deployed.
