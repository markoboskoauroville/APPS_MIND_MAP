# Spar Locator / DM Finder

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android map of every SPAR and INTERSPAR in Croatia (and a DM drugstore flavour), green when open now, red when shut, with today's hours and a route button.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/spar_locator](https://github.com/markoboskoauroville/spar_locator) |
| Also called | Spar Locator, DM Finder, SPAR open now map |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android |
| Language | Kotlin (Jetpack Compose) |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: spar-gh-v3 (also dm-v1) |
| Control level | none (no control api found) |

## What it can do

- Show SPAR/INTERSPAR stores on an OpenStreetMap map (VTM renderer) coloured open or shut by Croatian time
- Handle public holidays, open Sundays and renovation closures from the store list
- Show address, phone, weekly hours and open the route in a maps app
- Centre on the user's location with a pin key (no Google Play services)
- Build a second flavour 'DM Finder' from the dm store data service
- Work offline with a built-in store list copy

## Ask for it when

- which SPAR is open now
- find an open supermarket in Croatia on a map
- DM store opening hours Croatia

## How to control it

No control API found.

Evidence: api.txt only shows map library imports; no control API

## Inputs / Outputs

Inputs:

- spar.hr store list
- dm store data service
- GPS

Outputs:

- map with open/shut circles

## Hardware

- Android phone GPS

## Code worth reusing

- `app/src/main/java/com/mantra/spar/Stores.kt`: Parses store lists and computes open-now with holidays and extra days
- `app/src/main/java/com/mantra/spar/SparMap.kt`: VTM map with store markers and a location dot
- `app/src/main/java/com/mantra/spar/TileHttp.kt`: Tile HTTP loading for the map

## Notes

Two product flavours from one code base (spar and dm). Release tags spar-gh-vN and dm-vN. No README; docs in TAKEOVER.md/HANDOVER.md. Version 3 location pin was 'not yet compiled' at 2.11.2026 handover. Related to the Shop & Pool Finder (mapool) per the manifest.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/spar_locator/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/spar_locator/blob/HEAD/HANDOVER.md)
