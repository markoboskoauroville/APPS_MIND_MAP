# ZET Strike

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Termux app that follows Zagreb public transport during the ZET strike: live map, next tram or bus near you, lines, strike news with Gemini summary.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/zet_strike](https://github.com/markoboskoauroville/zet_strike) |
| Also called | zet, zet strike, ZET Zagreb strike app |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android, Termux |
| Language | Python (Flask) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Show live vehicles, lines and stops on a map with several views (OSM dark, Esri, Google map/satellite/terrain)
- Tell where and when to catch the next tram or bus near the user (zet near)
- List lines and stops, show what runs now in the terminal
- Fetch strike headlines with a Gemini summary and timeline
- Manage Gemini keys with fallback and test them; store a Google Maps key
- Update itself from GitHub (zet update)

## Ask for it when

- what trams are running in Zagreb now
- next bus near me in Zagreb
- Zagreb public transport strike news
- ZET map

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8100

Actions:

- `zet`
- `zet now`
- `zet near`
- `zet lines`
- `zet line N`
- `zet news`
- `zet log`
- `zet keys`
- `zet watch`
- `zet data`
- `zet update [check]`
- `zet map`
- `GET /health`
- `GET /api/live`
- `GET /api/near`
- `GET /api/place`
- `GET /api/lines`
- `GET /api/line/<name>`
- `GET /api/news`
- `POST /api/news/refresh`
- `GET /api/log`
- `GET|POST /api/settings`
- `POST /api/keys|import|title|test|delete`
- `GET /api/traffic`
- `GET /api/google`
- `POST /api/google/save|test|select|delete`
- `GET /stream`

**Before you call:** Flask server on 8100 (zet map); every /api call needs the X-ZET header (local guard).

Example:

```
zet near # the next ZET trams and buses at the nearest stop
```

More calls:

- live vehicles: `curl -s 127.0.0.1:8100/api/live -H 'X-ZET: 1'`
- lines: `zet lines ; zet line 6`
- news: `zet news`
- health: `curl -s 127.0.0.1:8100/health`

Evidence: README block in TAKEOVER.md (commands); app/app.py route decorators; HANDOVER.md (port 8100 then next fifteen)

## Inputs / Outputs

Inputs:

- ZET real-time feed
- strike news sources
- GPS via Termux:API

Outputs:

- web UI in Chrome
- terminal boards

## Hardware

- Android phone GPS

## Works with

- Uses: [Keyring](KEYRING_TERMUX.md), [Mantra Ports](MANTRA_PORTS.md)

## Code worth reusing

- `app/localguard.py`: Host, Origin/Referer and X-ZET header guard for a localhost Flask server (copied from KEYRING_TERMUX)
- `app/portpick.py`: Preferred port then next fifteen then OS port picker
- `app/keyparse.py`: Key file parser for API keys
- `app/tiles.py`: Map tile proxy for OSM, Esri and Google sessions

## Notes

Version V12 at 30.9.2026 handover; later pushes up to 21.11.2026 not read. Listens on 127.0.0.1 only. Not a remote-door contract (/health exists, /api is a set of data routes). Strike began 28.9.2026 so the app is event-specific. Keys kept in ~/.zet-strike/secrets, not in git. The value of the X-ZET header is not in the harvested docs; 1 is only a placeholder.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/zet_strike/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/zet_strike/blob/HEAD/HANDOVER.md)
