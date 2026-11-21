# Mantra NDI Screen Share (Android)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that sends the phone screen onto the network as an NDI source (compressed HX or full NDI), turning with the phone.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra-ndi-screen-share-android](https://github.com/markoboskoauroville/mantra-ndi-screen-share-android) |
| Also called | NDI screen share Android, Mantra NDI Screen Share, phone screen as NDI |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | Android |
| Language | Kotlin (C++ NDI bridge) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | none (no control api found) |

## What it can do

- Share the phone screen as an NDI source seen by vMix, OBS and NDI Studio Monitor
- Send compressed NDI HX (H.264/H.265, hardware encoder) or full NDI (SpeedHQ)
- Rebuild the stream when the phone rotates
- Show estimated bitrate cost before starting
- Start from a quick-settings tile
- Reopen the share at 25 minutes to survive the Advanced SDK 30-minute cap

## Ask for it when

- mirror my Android screen to OBS over NDI
- show the phone screen in vMix
- stream Android screen as NDI

## How to control it

No control API found.

Evidence: api.txt empty; NdiTileService and TileStartActivity only (quick tile)

## Inputs / Outputs

Inputs:

- Android screen capture

Outputs:

- NDI video source

## Works with

- Uses: [Mantra Manual Camera](mantra-manual-camera.md), [Mantra NDI SDK (private vendor files)](mantra-ndi-sdk.md)

## Code worth reusing

- `app/src/main/cpp/ndi_bridge.cpp`: NDI sender bridge for Android (compressed and full paths)
- `app/src/main/java/com/mantraproductions/ndiscreen/Mechanism.kt`: Pure functions for sizing, orientation, bitrate and NDI cost estimates, with unit tests

## Notes

v1 written 21.9.2026 and never run on a phone at that point (HANDOVER); later tags v2, v3 exist. No README in the repo; the former README is inside TAKEOVER.md. Part of the Mantra NDI family with mantra-manual-camera.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/mantra-ndi-screen-share-android/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/mantra-ndi-screen-share-android/blob/HEAD/LESSONS.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/mantra-ndi-screen-share-android/blob/HEAD/HANDOVER.md)
