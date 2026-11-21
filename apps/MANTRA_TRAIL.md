# Mantra Trail

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android offline outdoor map app for Croatian mountains: offline OpenAndroMaps and TK25 layers, GPX track recorded point by point, compass and spirit level.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_TRAIL](https://github.com/markoboskoauroville/MANTRA_TRAIL) |
| Also called | Mantra Trail, trail app |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android |
| Language | Java and Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v94 |
| Control level | none (no control api found) |

## What it can do

- Show offline maps from an OpenAndroMaps .map file, TK25 Hrvatska WMS, OpenTopoMap and an online Google layer
- Record a GPX 1.1 track point by point, flushed every fix, refusing bad fixes (accuracy ›50 m, ›12 m/s, clock back)
- Show the count of refused fixes on screen
- Route offline with the embedded BRouter engine (trekking, hiking-mountain, shortest profiles)
- Show a compass and a spirit level
- Show cadastral parcels (WMS/WFS)

## Ask for it when

- offline hiking map on Android
- record a hike as GPX
- navigate in the mountains without signal
- route on foot offline

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- mapsforge .map files
- GPS fixes
- WMS tiles

Outputs:

- GPX tracks
- map display

## Hardware

- phone GPS, compass, accelerometer

## Works with

- Uses: [Mantra Maps](MANTRA_MAPS.md), [Mantra Map Server](MANTRA_MAP_SERVER.md)
- Used by or talked to by: [Mantra Maps](MANTRA_MAPS.md), [Mantra Map Server](MANTRA_MAP_SERVER.md), [Mantra ARKOD](mantra_arkod.md)

## Code worth reusing

- `app/src/main/java/btools/`: embedded BRouter routing engine (see LICENSE-BROUTER)
- `app/src/main/java/com/mantra/trail/Geo.kt`: Web Mercator and geo helpers
- `app/src/main/java/com/mantra/trail/TileHttp.kt`: tile fetching over HTTP

## Notes

Google layer is online only because Google's terms forbid caching tiles. Release tags v93, v94 seen; keeps only the two newest builds. Built only by GitHub Actions.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_TRAIL/blob/HEAD/TAKEOVER.md)
