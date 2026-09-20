# Google Sign-In Setup

Parlour supports 1-tap Google Sign-In alongside the email magic link.
It provides instant, passwordless access across devices without waiting for
email delivery or spam filter delays.

Under the hood:
1. The browser requests an OpenID Connect credential using Google Identity
   Services (loaded lazily on demand).
2. The credential (ID token) is sent to Parlour's Cloudflare Worker (`/auth/google`).
3. The Worker verifies the token against Google's tokeninfo endpoint,
   validating the audience, issuer, expiration, and verified email status.
4. The verified email is mapped to the existing D1 `users` table and signed with
   the same HMAC-SHA256 JWT session used by email magic links. Accounts created
   or accessed via Google Sign-In and magic link with the same email share the
   exact same cloud backup state.

---

## One-Time Setup (~10 minutes)

### 1. Create a Google Cloud Project & OAuth Client ID

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (e.g. `parlour-app`) or select an existing one.
3. Navigate to **APIs & Services** -> **OAuth consent screen**:
   - User Type: **External**.
   - App name: `Parlour`.
   - User support email: your email.
   - Developer contact email: your email.
   - Click **Save and Continue** (no additional scopes are needed; standard `openid`, `email`, `profile` are default).
   - Under **Test users** (if app status is Testing), add your Google email address, or publish the app to Production when ready.
4. Navigate to **APIs & Services** -> **Credentials**:
   - Click **Create Credentials** -> **OAuth client ID**.
   - Application type: **Web application**.
   - Name: `Parlour Web Client`.
   - Under **Authorized JavaScript origins**, add:
     - `https://parlour.me.uk`
     - `https://gergkar-gif.github.io`
     - `http://localhost:8131` (for local development)
     - `http://localhost:3000` (optional, if using another local port)
   - Click **Create**.
   - Copy the generated **Client ID** (format: `xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com`).

---

### 2. Configure Cloudflare Worker

1. Open the [Cloudflare Dashboard](https://dash.cloudflare.com/) -> **Workers & Pages** -> your sync worker (e.g. `parlour-sync`).
2. Go to **Settings** -> **Variables and Secrets**.
3. Under **Environment Variables**, click **Add**:
   - Variable name: `GOOGLE_CLIENT_ID`
   - Value: paste your Google Client ID copied in step 1.
   - (Optional: mark as Encrypted or Plain Text; client IDs are public, but encrypting is good practice).
   - Click **Save and Deploy**.
4. If you have updated the worker code on your machine:
   - Copy the contents of [`cloudflare-worker/sync-worker.js`](cloudflare-worker/sync-worker.js).
   - In your Worker page, click **Edit code**, paste the updated worker script, and click **Deploy**.

---

### 3. Configure the Web Client

1. Open [`engine/sync.js`](engine/sync.js) in your codebase.
2. Near line 40, locate `GOOGLE_CLIENT_ID`:
   ```javascript
   const GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID_HERE';
   ```
   Paste your Google Client ID into the quotes.
3. Commit and push your changes to GitHub.

---

## Verifying the Setup

1. Open Parlour in your browser (`https://parlour.me.uk` or `http://localhost:8131`).
2. Navigate to **Journey**, then scroll to the **Account** card.
3. You will see the **Sign in with Google** button rendered above the email magic link form.
4. Click **Sign in with Google** and select your Google account.
5. Upon successful sign-in:
   - Your email is displayed under Account.
   - Cloud backup and restore buttons become active.
   - Any previous cloud backup associated with that email is preserved.
   - If signing in on a new device with no local progress, the cloud backup is automatically restored.
