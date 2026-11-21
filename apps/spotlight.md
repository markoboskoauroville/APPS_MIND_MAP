# Find a File Spotlight (Mantra) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Find a File (Mantra)](FIND_FILE.md). Replaced by FIND_FILE.

**Retired: local page and server that index one folder with Spotlight and search it; merged into Find a File (repo FIND_FILE).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/spotlight](https://github.com/markoboskoauroville/spotlight) |
| Also called | Spotlight Folder (Mantra), spotlightd |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Python, Swift |
| Status | retired |
| Last push | 2026-11-01 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Index a chosen folder with mdimport and report how many items Spotlight knows
- Search inside one folder by name or content with mdfind
- Show hits in compact, list, grid and large thumbnail views
- Reveal, open, copy path or open the folder of a hit

## Ask for it when

- search files inside one folder on the Mac
- make Spotlight index a single folder

## How to control it

- Level: **door**
- Type: http
- Port: 8847

**Warning:** port 8847 is also quoted for [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `POST /api/choose`
- `POST /api/index`
- `GET /api/status`
- `POST /api/search`
- `POST /api/reveal`
- `POST /api/open`
- `POST /api/folder`
- `POST /api/copy`
- `POST /api/quit`
- `GET /thumb`

**Before you call:** RETIRED 1.11.2026: use FIND_FILE (Find a File (Mantra)).

Example:

```
curl -X POST http://127.0.0.1:8847/api/search -H 'Content-Type: application/json' -d '{"folder":"~/Desktop","query":"poster"}'
```

More calls:

- search one folder (retired, use FIND_FILE): `curl -s -XPOST 127.0.0.1:8847/api/search -H 'Content-Type: application/json' -d '{"folder":"~/Desktop","query":"poster"}'`

Evidence: spotlightd.py header and routes

## Inputs / Outputs

Inputs:

- folder path
- search words

Outputs:

- search hits
- thumbnails

## Works with

- Uses: [Find a File (Mantra)](FIND_FILE.md)
- Talks to: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `spotlightd.py`: Flask server wrapping mdimport, mdfind and Quick Look thumbnails

## Notes

Retired 1.11.2026: use Find a File (Mantra), whose ENGINE SPOTLIGHT replaced this. RETIRED/SUPERSEDED: use FIND_FILE instead.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
