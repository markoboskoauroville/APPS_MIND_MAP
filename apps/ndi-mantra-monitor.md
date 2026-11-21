# NDI Mantra Monitor

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**NDI receiver for the Mac: one window, one picture, right-click to choose a source.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ndi-mantra-monitor](https://github.com/markoboskoauroville/ndi-mantra-monitor) |
| Also called | ndi monitor, NDI receiver |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS |
| Language | Swift (with C NDI shim) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Receive an NDI video source and show it in one window
- Choose the NDI source by right-click
- Build as a signed Mac app from a script

## Ask for it when

- watch an NDI stream on the Mac
- monitor the phone's NDI camera on the desktop
- view an NDI source in a window

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- NDI sources on the network

Outputs:

- video window

## Code worth reusing

- `Sources/NDI.swift`: Swift wrapper around the NDI C library for finding and receiving sources
- `CNDI/`: module map and shim header exposing the NDI C API to Swift

## Notes

No README; described from the repository description and file names. No control API found.
