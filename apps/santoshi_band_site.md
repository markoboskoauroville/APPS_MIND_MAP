# Santoshi Kirtan Band sites

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Published Santoshi Kirtan Band websites on Cloudflare Pages: protected admin, picture library, live streaming, live chat and viewer count.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/santoshi_band_site](https://github.com/markoboskoauroville/santoshi_band_site) |
| Also called | Santoshi band website, santoshi-band.pages.dev, mantrasantoshiconcerts |
| Visibility | public |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | HTML/JS (Cloudflare Pages Functions) |
| Status | active |
| Last push | 2026-11-17 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Serve the band site and the concerts site (HLS audio, SEO pages made at deploy)
- Offer an /admin area with Google sign-in limited to allowed addresses
- Go live: create a VDO.Ninja stream, show a live banner and viewer on every page, record the camera to Drive in 5-second pieces
- Run live chat and a watching count through a Durable Object over WebSockets (/api/room)
- Serve private reference pictures from KV behind login (/api/pics)
- Pair a phone camera by QR/mantracam link (/api/cam) and expose public /api/live status
- Deploy both sites by GitHub Actions on push

## Ask for it when

- go live on the band website
- update the Santoshi band site
- pair the phone camera with the band site
- show how many are watching the concert stream
- band concerts web page

## How to control it

- Level: **http**
- Type: http, websocket
- Port: HTTPS 443, hosted on Cloudflare Pages

Actions:

- `GET /api/live (public status)`
- `POST /api/live go|stop|status (Bearer token or admin cookie)`
- `WS /api/room (chat and viewer count)`
- `/api/pics (login)`
- `/api/cam pair`
- `/api/google (login)`
- `/api/relay`
- `/api/stats`

**Before you call:** Go-live and stop need a bearer token or an admin cookie (not published).

Example:

```
curl -s https://santoshi-band.pages.dev/api/live # public: is the band live now
```

More calls:

- chat and viewer count: `WebSocket /api/room`

Evidence: TAKEOVER.md (13-14.11.2026 sections), LESSONS.md; Mantra Manual Camera docs for /api/live go|stop|status

## Inputs / Outputs

Inputs:

- published files copied from the private a private repo workshop
- phone camera stream via VDO.Ninja

Outputs:

- two Cloudflare Pages sites
- Drive recordings of live streams

## Works with

- Uses: [Mantra Manual Camera](mantra-manual-camera.md)
- Used by or talked to by: [Cloud Mixer](CLOUD_MIXER.md), [Mantra Manual Camera](mantra-manual-camera.md)

## Code worth reusing

- `admin/live.js`: Admin LIVE tab: start/stop a VDO.Ninja stream with Drive recording
- `room/worker.js (per TAKEOVER)`: Durable Object WebSocket room for chat and viewer count with rate limits

## Notes

Edit in the private a private repo repo, not here (publish_site.sh copies files here). 166 MB mostly audio segments. Admin addresses are secrets, none in repo. Endpoint list is from docs; functions/ source not in the harvested file list so exact request formats are unverified.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/santoshi_band_site/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/santoshi_band_site/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/santoshi_band_site/blob/HEAD/LESSONS.md)
