# Mantra ARKOD

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android map app showing every cadastral parcel in Croatia; tap one to open its possession and owner sheets; offline map and parcel cache.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra_arkod](https://github.com/markoboskoauroville/mantra_arkod) |
| Also called | ARKOD, Mantra Arkod, Croatian cadastre app, Mantra Trail derivative |
| Visibility | public |
| Kind | app |
| Category | [Maps, travel and location](../capabilities/maps-travel-location.md) |
| Platforms | Android, Cloud |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v28 |
| Control level | none (no control api found) |

## What it can do

- Show Croatian cadastral parcels (ARKOD) over offline mapsforge, Google or OSM maps
- Open the possession sheet (posjedovni list) and owner sheet (vlasnički list) for a tapped parcel
- Keep the user's own parcels in a chosen colour
- Cache every cadastre tile seen and prefetch around the map and the user
- Queue requests the state did not answer ('fetch when available') for a Cloudflare worker to retry every 10 minutes
- Offer Croatian and English help

## Ask for it when

- look up a land parcel in Croatia
- who owns this cadastral parcel
- offline cadastre map for walking
- find my parcels on a map

## How to control it

No control API found.

Evidence: No app control API found; it calls arkod-layer.pages.dev/api/later and parcel-info endpoints (client side) per FEATURES.md and LOCAL_TASKS.md

## Inputs / Outputs

Inputs:

- GPS location
- cadastre WMS tiles
- offline Croatia map download (176 MB)

Outputs:

- parcel sheets
- cached tiles

## Hardware

- Android phone GPS

## Works with

- Uses: [Mantra Trail](MANTRA_TRAIL.md), [ARKOD Layer (web)](arkod_web.md)
- Used by or talked to by: [ARKOD Layer (web)](arkod_web.md)

## Code worth reusing

- `app/src/main/java/com/mantra/arkod/CacheTiles.kt`: Tile cache for cadastre and map layers
- `scripts/remote-cache/sweep.py`: Script that sweeps requests into the remote cache repository

## Notes

Built only by GitHub Actions (no local APK build). Google tiles are not stored (Google forbids). Several tokens and secrets are mentioned in docs as pending; none copied. Derived from Mantra Trail on 29.9.2026.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/mantra_arkod/blob/HEAD/README.md)
