# Speech-to-Text (STT) Worker Setup

Parlour's speaking drills and lessons provide automated pronunciation evaluation and a **"Listen to your recording"** dual-audio comparison (playing your voice side-by-side with the model voice).

---

## Architecture: Why a Cloudflare STT Worker?

On desktop browsers, the browser's built-in Web Speech API can run concurrently with `MediaRecorder`. However, **mobile operating systems (iOS and Android) enforce a single-client hardware lock on the microphone**:
- Opening `getUserMedia` to record audio starves `webkitSpeechRecognition`, producing silence and timing out.
- Giving `webkitSpeechRecognition` exclusive mic access prevents capturing raw audio buffers to replay.

**The Solution:**
1. **Client**: Parlour captures clean audio via `MediaRecorder` exclusively on mobile. This has zero hardware contention and works on 100% of iOS and Android devices.
2. **Audio URL**: An audio blob URL is immediately created, arming the **"Your Voice"** button.
3. **STT Worker**: The audio blob is sent to `parlour-stt` running `@cf/openai/whisper` on Cloudflare Workers AI free tier.
4. **Scoring**: The returned transcript is evaluated word-by-word against the target prompt.

The Worker source code is located at:
[`cloudflare-worker/stt-worker.js`](cloudflare-worker/stt-worker.js)

---

## One-Time Setup (~3 minutes)

This uses your existing Cloudflare account (the same one used for `parlour-grader`, `parlour-sync`, and `parlour-bug-report`). It runs entirely on Cloudflare's **100% free tier** (10,000 free AI neurons/day, equivalent to 200–500 speaking evaluations daily). No credit card required.

### 1. Create the Worker
1. Log in to [dash.cloudflare.com](https://dash.cloudflare.com).
2. In the sidebar, navigate to **Workers & Pages** → **Create** → **Create Worker**.
3. Name it:
   ```text
   parlour-stt
   ```
   *(This gives the endpoint `https://parlour-stt.<your-subdomain>.workers.dev/transcribe`)*.
4. Click **Deploy**.

### 2. Paste the Worker Code
1. Click **Edit code** to open Cloudflare's browser editor.
2. Delete the placeholder code.
3. Paste the complete contents of [`cloudflare-worker/stt-worker.js`](cloudflare-worker/stt-worker.js).
4. Click **Deploy** (top right).

### 3. Bind Workers AI
1. Go back to the `parlour-stt` Worker's main page in the Cloudflare dashboard.
2. Click the **Settings** tab (or **Variables and Bindings**).
3. Under **Bindings**, click **Add** → select **Workers AI**.
4. Set the **Variable name** to exactly:
   ```text
   AI
   ```
5. Click **Save and Deploy**.

---

## Verification

You can verify the deployment with a simple GET health check:
```bash
curl.exe https://parlour-stt.gergkar.workers.dev/health
```

Expected response:
```json
{"status":"ok","service":"parlour-stt","model":"@cf/openai/whisper","workersAiAvailable":true}
```

Once deployed, any speaking drill or oral challenge in Parlour will record your voice cleanly on mobile and desktop, score pronunciation with Whisper, and let you tap **"Your Voice"** to listen to your recording.
