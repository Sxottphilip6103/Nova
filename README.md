# Nova

Nova is a client-side, installable AI chat PWA. Everything runs in the browser — chats and API keys are stored in `localStorage` on the user's device; nothing is sent to a backend of ours (requests go straight from the browser to whichever AI provider is selected).

## What's in here

```
index.html                    the whole app (UI, styles, logic)
manifest.json                 PWA manifest (name, icons, theme, display mode)
sw.js                         service worker (offline app-shell caching)
icon-192.png
icon-512.png
icon-maskable-192.png
icon-maskable-512.png
apple-touch-icon.png
gen_icons_from_logo.py        script used to generate the icons (optional, not needed at runtime)
```

All files sit flat in one folder on purpose (no subfolders) so the whole project can be uploaded from a phone in one go via GitHub's web "Upload files" page, which doesn't preserve folder structure from a mobile file picker.

## Deploying from a phone (no computer needed)

1. Unzip the project on your phone (tap the `.zip` in Files/Downloads — iOS and Android both extract it in place).
2. In your phone's browser, go to **github.com**, sign in (or create a free account).
3. Tap **+ → New repository**. Give it a name, set it to **Public**, and create it (skip adding a README).
4. On the new repo's page, tap **Add file → Upload files**.
5. Tap to browse, select **all the files** from the unzipped folder (all of them at once, no subfolders), and upload. Commit directly to `main`.
6. Go to **Settings → Pages** in the repo. Under **Build and deployment → Source**, choose **Deploy from a branch**, pick `main` / `/ (root)`, and save.
7. Wait about a minute, then open the URL GitHub gives you (`https://<username>.github.io/<repo>/`).
8. On that page: Android/Chrome will offer to install it (or use the **Install app** button in Nova's drawer); on iPhone/Safari, tap **Share → Add to Home Screen**.



## Updating the app later

The service worker caches the app shell so it keeps working offline. When you push changes:

1. Bump `CACHE_VERSION` in `sw.js` (e.g. `nova-v1` → `nova-v2`). This is what makes the old cache get cleared and the new files picked up — without it, returning visitors may keep seeing the previous version until they clear site data.
2. Commit and push. Visitors will get the new version on their next load (the service worker updates in the background, then takes over on the following page load).

## Notes

- API keys for Gemini / Groq / OpenRouter are entered by the user in Settings and stored only in their browser's `localStorage`.
- The install button in the drawer only appears once the browser fires its `beforeinstallprompt` event (Chromium-based browsers). Safari/iOS doesn't support that event — installation there is manual via Share → Add to Home Screen.
