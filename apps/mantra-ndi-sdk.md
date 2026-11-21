# Mantra NDI SDK (private vendor files)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Private store of the licensed NDI Advanced SDK for Android (arm64) that the mantra-ndi build fetches in CI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra-ndi-sdk](https://github.com/markoboskoauroville/mantra-ndi-sdk) |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | Android, Cloud |
| Language | C |
| Status | active |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Hold NDI headers and the arm64 runtime library for the Android NDI app build
- Keep the licensed SDK out of the public app repo

## Ask for it when

- build the Android NDI app
- where are the NDI SDK headers for Android

## How to control it

No control API found.

## Inputs / Outputs

Outputs:

- headers and libndi_advanced.so for the APK build

## Works with

- Talks to: [Mantra Manual Camera](mantra-manual-camera.md)
- Used by or talked to by: [Mantra Manual Camera](mantra-manual-camera.md), [Mantra NDI Screen Share (Android)](mantra-ndi-screen-share-android.md)

## Notes

Licensed material, must stay private and never be redistributed. Not for the public map beyond this record.

## Docs in the repo

- `README.md`
