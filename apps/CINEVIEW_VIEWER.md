# CineView Viewer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Swift Mac viewer that shows the picture of an Accsoon CineView Nano over its own Wi-Fi. Protocol implemented but not working against the Nano yet.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CINEVIEW_VIEWER](https://github.com/markoboskoauroville/CINEVIEW_VIEWER) |
| Also called | Axon Nano Viewer, CineView Nano viewer, Accsoon viewer |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-01 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Connect to the transmitter over TCP and UDP and reassemble H.264/HEVC video fragments
- Decode with VideoToolbox and show frames in a window
- Test the protocol parsing with unit tests

## Ask for it when

- view the Accsoon CineView Nano picture on the Mac
- watch the wireless video monitor without the vendor app

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- Accsoon CineView Nano video over its Wi-Fi

Outputs:

- live picture window

## Hardware

- Accsoon CineView Nano

## Works with

- Used by or talked to by: [MacBook Pro as external display](MacBook_Pro_as_external_display.md)

## Code worth reusing

- `Sources/CineViewCore/Reassembler.swift`: reassembles fragmented video messages into frames
- `Sources/CineViewCore/NAL.swift`: Annex-B H.264/HEVC NAL parsing for VideoToolbox

## Notes

Protocol taken from third-party decoders (Master 4K captures); the real Nano firmware did not answer on the expected port, vendor SDK for iOS only. Waiting on vendor SDK.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
