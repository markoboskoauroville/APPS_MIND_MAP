# ARKOD Layer (web)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Web app (PWA) showing Croatian cadastral parcels on a map for iPhone and any browser, with parcel info, saved parcels, offline caches and an address book.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/arkod_web](https://github.com/markoboskoauroville/arkod_web) |
| Also called | ARKOD Layer, arkod-layer, ARKOD web |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Web, Cloud, iOS |
| Language | JavaScript |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Show state cadastre parcel lines over OpenStreetMap or Google
- Tap a parcel for its info and land registry sheets
- Keep parcels in groups (Moje cestice) and cache parcels for no signal
- Find a parcel by number anywhere on the map
- Fetch data later when a service is unavailable (Worker and /api/later)
- Install on an iPhone home screen

## Ask for it when

- Croatian cadastre on a map
- look up a parcel number
- ARKOD parcels on iPhone
- land registry sheet for a parcel

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted on Cloudflare Pages (arkod-layer.pages.dev)

Actions:

- `GET /api/wms`
- `GET /api/wfs`
- `GET /api/oss/*`
- `/api/later/want`
- `/api/later/answer`
- `/api/later/status`
- `/api/later/wanted`

**Before you call:** Parameters of the proxy routes are not in the harvested docs; open the page and copy the request it makes.

Example:

```
curl -s 'https://arkod-layer.pages.dev/api/wfs?<same query string the page sends>' # proxies the state cadastral WFS as GeoJSON
```

More calls:

- the WMS proxy: `curl -s 'https://arkod-layer.pages.dev/api/wms?<query as the page sends it>'`

Evidence: functions/api/*.js headers; README.md; momentaryupdates.md lines 39-41

## Inputs / Outputs

Inputs:

- state cadastre WMS/WFS/OSS
- OpenStreetMap or Google tiles

Outputs:

- parcel map and sheets
- IndexedDB caches

## Works with

- Uses: [Mantra ARKOD](mantra_arkod.md)
- Used by or talked to by: [Mantra ARKOD](mantra_arkod.md)

## Code worth reusing

- `public/js/core/`: parcel, style, cache, mark file, owner book and outline logic ported from Kotlin
- `functions/api/oss/[[path]].js`: Cloudflare Pages proxy that strips Origin so the state service answers
- `fetcher/worker.js`: scheduled Worker that fetches when a service becomes available
- `public/js/scan.js`: fly-through scanning of the map for parcels

## Notes

The /api paths are CORS proxies for the web app, not a general control API. Settings in English, cadastre in Croatian. One secret was still awaited for the later-fetch feature at last note. Tests: npm test, verify, e2e.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/arkod_web/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/arkod_web/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/arkod_web/blob/HEAD/LESSONS.md)
