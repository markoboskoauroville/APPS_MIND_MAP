# Mantra Download Counter

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Cloudflare Worker that counts and shows the number of downloads beside the Download buttons on the product pages.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_DOWNLOAD_COUNTER](https://github.com/markoboskoauroville/MANTRA_DOWNLOAD_COUNTER) |
| Also called | Download Counter, mantra-downloads |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | JavaScript (Cloudflare Worker) |
| Status | active |
| Last push | 2026-11-10 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Count a button press once per visitor per app per day
- Return the count for one app or all apps
- Serve a script that adds a downloads label after each button marked data-dl-app
- Keep no visitor data beyond a daily salted hash

## Ask for it when

- add a download counter to a page
- see how many times an app was downloaded

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted (a Cloudflare worker; address not published here)

Actions:

- `GET /count?app=NAME`
- `POST /hit?app=NAME`
- `GET /counts`
- `GET /counter.js`

**Before you call:** Hosted worker; `<worker-url>` is the owner's.

Example:

```
curl -s '<worker-url>/count?app=shruti'
```

More calls:

- count a download: `curl -s -XPOST '<worker-url>/hit?app=shruti'`
- all counts: `curl -s <worker-url>/counts`

Evidence: README.md Worker table; src/worker.js

## Inputs / Outputs

Outputs:

- download counts

## Code worth reusing

- `src/worker.js`: Durable Object counter with once-per-day visitor dedupe

## Notes

Counts started 23.10.2026. No reset and no admin view beyond /counts.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
