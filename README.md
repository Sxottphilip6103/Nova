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


## Updating the app later

The service worker caches the app shell so it keeps working offline. When you push changes:

1. Bump `CACHE_VERSION` in `sw.js` (e.g. `nova-v1` → `nova-v2`). This is what makes the old cache get cleared and the new files picked up — without it, returning visitors may keep seeing the previous version until they clear site data.
2. Commit and push. Visitors will get the new version on their next load (the service worker updates in the background, then takes over on the following page load).

## Notes

- API keys for Gemini / Groq / OpenRouter are entered by the user in Settings and stored only in their browser's `localStorage`.
- The install button in the drawer only appears once the browser fires its `beforeinstallprompt` event (Chromium-based browsers). Safari/iOS doesn't support that event — installation there is manual via Share → Add to Home Screen.
