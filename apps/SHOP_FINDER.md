# Store & Pool Finder

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One web page that finds the nearest Spar, dm, bio&bio, Mlinar, malls and banks and shows Zagreb city pool hours, with a small Python server and Termux command.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SHOP_FINDER](https://github.com/markoboskoauroville/SHOP_FINDER) |
| Also called | Shop & Pool Finder, shopfinder, mapool |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Termux, Linux, Web, Cloud |
| Language | Python |
| Status | active |
| Last push | 2026-10-20 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Find nearest shops with today's opening hours from the user's position
- Show the eight Zagreb city pools with public-swim hours read from the official pages
- Offer a free OSM map or a Google map through the server
- Show a walking route (OSRM)
- Run on Cloudflare Pages plus a server, or on the phone in Termux with the mapool command
- Keep API keys on the server only

## Ask for it when

- nearest shop open now
- Zagreb pool opening hours
- find a Spar or dm near me
- store and pool finder

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8900 on the server (8080 for local serve.py)

Actions:

- `GET /pools.json`
- `POST /update`
- `GET /config.js`
- `GET /places`
- `GET /gtile/...`
- `GET /health`
- `GET /settings/state`
- `GET /settings/test`
- `POST /settings/import`
- `mapool`
- `mapool update`
- `mapool boot`
- `mapool install`
- `mapool where`

**Before you call:** Server on 8900 behind Caddy; local serve.py on 8080; on the phone: mapool.

Example:

```
curl -s http://127.0.0.1:8900/shopfinder/health # only health is documented as a call; the finder is a map page
```

More calls:

- places JSON: `curl -s http://127.0.0.1:8900/shopfinder/places`
- update the place list: `mapool update`

Evidence: serve.py lines 312-346; HANDOVER.md; mapool script header

## Inputs / Outputs

Inputs:

- user position
- Overpass, Places and official pool pages

Outputs:

- web page
- pools.json

## Works with

- Used by or talked to by: [Keyring](KEYRING_TERMUX.md), [Oracle machine notes](oracle_machine.md)

## Code worth reusing

- `serve.py`: stdlib server for a static page with proxying of paid map APIs so keys stay server-side
- `portpick.py`: free port picker
- `selfupdate.py`: GitHub self-updater
- `mapool`: Termux global command with boot/update/install subcommands
- `tests/run_all.py`: four-test runner (mechanism, UI, ugly, upgrade)

## Notes

Keys live only on the server machine. Pool list is kept in two places (public/index.html and update_pools.py). Tied to Zagreb.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/SHOP_FINDER/blob/HEAD/README.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/SHOP_FINDER/blob/HEAD/HANDOVER.md)
