# Grader Worker Feature & Setup

The **Writing Studio** (in Workshop) and **Open Production Drills** evaluate student writing and speaking responses with CEFR-aligned formative feedback.

## Architecture & Zero-Secret Security

To keep AI API keys and model credentials off the browser client, all AI evaluations run through a serverless proxy:

- **Browser / Client**: Builds the prompt and sends a POST request to `https://parlour-grader.gergkar.workers.dev/grade`.
- **Cloudflare Worker**: Runs in Cloudflare's serverless edge, securely binds to Cloudflare Workers AI (`env.AI`), calls `@cf/meta/llama-3.3-70b-instruct` (or configured model), and formats the CEFR assessment JSON.
- **Graceful Local Fallback**: If the Worker is offline, unreachable, or daily AI quota is exhausted, Parlour **automatically degrades** to the built-in deterministic local grader (scoring word counts, sentence complexity, punctuation, and structural target compliance) so exercises never crash.

The Worker source code is located at:
[`cloudflare-worker/grader-worker.js`](cloudflare-worker/grader-worker.js)

---

## One-Time Setup (~3 minutes)

This reuses your existing Cloudflare account (the same one used for `parlour-sync` and `parlour-bug-report`). No credit card is required.

### 1. Create the Worker
1. Log in to [dash.cloudflare.com](https://dash.cloudflare.com).
2. In the sidebar, go to **Workers & Pages** → **Create** → **Create Worker**.
3. Name it **`parlour-grader`** (this ensures the URL is `https://parlour-grader.<your-subdomain>.workers.dev`).
4. Click **Deploy** to scaffold it.

### 2. Paste the Worker Code
1. Click **Edit code** to open Cloudflare's online code editor.
2. Delete the placeholder code.
3. Paste the entire contents of [`cloudflare-worker/grader-worker.js`](cloudflare-worker/grader-worker.js).
4. Click **Deploy** (top right).

### 3. Bind Workers AI
1. Go back to the Worker's main page and click the **Settings** tab (or **Variables and Bindings** in newer dashboard layouts).
2. Under **Bindings**, click **Add** → select **Workers AI**.
3. Set the **Variable name** to exactly:
   ```text
   AI
   ```
4. Click **Save and Deploy**.

---

## Verification

You can verify the deployment by running:
```bash
curl.exe -X POST https://parlour-grader.gergkar.workers.dev/grade -H "Content-Type: application/json" -d "{\"prompt\":\"Ping\"}"
```
Once deployed, the endpoint will respond with a valid JSON response from Workers AI rather than error code `1042`.

Within Parlour, open the **Workshop** tab, launch **Writing Studio**, and submit any short sentence. The studio will display detailed formative feedback with CEFR scoring, vocabulary commendations, and grammar guidance.
