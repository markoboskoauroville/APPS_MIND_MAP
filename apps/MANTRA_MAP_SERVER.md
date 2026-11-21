# Mantra Map Server

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that serves mapsforge offline maps as ordinary z/x/y PNG tiles over HTTP from the phone, so any map app on the wifi can use them.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_MAP_SERVER](https://github.com/markoboskoauroville/MANTRA_MAP_SERVER) |
| Also called | Map Server |
| Visibility | public |
| Kind | service-daemon |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | http (own http routes) |

## What it can do

- Render mapsforge .map files into 256 px PNG tiles and cache each tile
- Download a map region from mapsforge's server, resumably
- Import a .map file with the file picker
- Count tiles served per caller address and show the table
- Serve /, /maps and /status to a browser on another machine

## Ask for it when

- serve offline maps as tiles
- give my laptop or tablet the phone's offline map
- map tile server on Android

## How to control it

- Level: **http**
- Type: http
- Port: 8088

Actions:

- `GET /tiles/<region>/{z}/{x}/{y}.png`
- `GET /`
- `GET /maps`
- `GET /status`

**Before you call:** Serves offline map tiles from local files; /maps lists the regions available.

Example:

```
curl -s http://127.0.0.1:8088/tiles/croatia/10/553/366.png -o tile.png
```

More calls:

- which maps are installed: `curl -s 127.0.0.1:8088/maps`
- status: `curl -s 127.0.0.1:8088/status`

Evidence: TAKEOVER.md (from former README); HANDOFF.md line 26

## Inputs / Outputs

Inputs:

- mapsforge .map files

Outputs:

- PNG tiles over HTTP

## Works with

- Uses: [Mantra Maps](MANTRA_MAPS.md)
- Talks to: [Mantra Trail](MANTRA_TRAIL.md)
- Used by or talked to by: [Mantra Maps](MANTRA_MAPS.md), [Mantra Trail](MANTRA_TRAIL.md)

## Code worth reusing

- `app/src/main/java/com/mantra/mapserver/Renderer.kt`: mapsforge to PNG tile rendering
- `app/src/main/java/com/mantra/mapserver/Download.kt`: resumable region download
- `app/src/main/java/com/mantra/mapserver/Usage.kt`: per-caller tile counters

## Notes

No authentication and no HTTPS by design; anything on the same network can fetch tiles. Never serves Google or Thunderforest tiles (terms forbid storing them). Tile URL may take ?key= for LAN use per tests.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_MAP_SERVER/blob/HEAD/TAKEOVER.md)
