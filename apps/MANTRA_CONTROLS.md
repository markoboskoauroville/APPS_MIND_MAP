# Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Two small Mac windows that control the MIDI to Key Stroke and MIDI to MK Control engines over their local HTTP state/do servers.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_CONTROLS](https://github.com/markoboskoauroville/MANTRA_CONTROLS) |
| Also called | MIDI to Key Stroke app, MIDI to MK Control app, star control pages |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v8 |
| Control level | none (no control api found) |

## What it can do

- Draw the MIDI-to-keystroke mapping table from the engine's /state
- Switch DETECT and the engine on or off from the window
- Show NOT RUNNING and start the engine with START
- Control the Mackie control engine in the same way

## Ask for it when

- control the MIDI to keystroke mapper from a Mac window
- switch MIDI detect on and off
- edit MIDI mapping rows

## How to control it

No control API found.

Evidence: TAKEOVER.md table; this repo is a client of those servers (GET /state, POST /do), not a server

## Inputs / Outputs

Inputs:

- engine /state JSON

Outputs:

- POST /do verbs

## Hardware

- MIDI controllers (via the engines)

## Works with

- Uses: [MIDI Tools (Mantra)](MANTRA_MIDI_TOOLS.md), [MIDI to Key Stroke](MIDI_TO_KEYSTROKE.md), [Mantra Mackie Control Translator](mantra-mackie-control-translator.md)
- Talks to: [Launcher (Mantra)](STAR_LAUNCHER.md)

## Code worth reusing

- `Sources/Common/Server.swift`: HTTP client helpers for a state/do JSON engine
- `Sources/Common/Parts.swift`: shared Swift UI parts for control windows

## Notes

Old faces of the Lua engines; MIDI Tools (Mantra) replaces them (v8 starts MIDI Tools instead of Hammerspoon). Likely superseded.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_CONTROLS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_CONTROLS/blob/HEAD/LESSONS.md)
