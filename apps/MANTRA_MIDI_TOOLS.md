# MIDI Tools (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac menu-bar app with two MIDI tools: MIDI to MK Control (knobs and keys to Ableton Mackie commands) and MIDI to Key Stroke (notes and CC to key strokes).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_MIDI_TOOLS](https://github.com/markoboskoauroville/MANTRA_MIDI_TOOLS) |
| Also called | MIDI Tools, MIDI to MK Control, MIDI to Key Stroke, MIDI to MKEY, MIDI to Keyboard, miditools |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift (with a Python helper) |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | none (no control api found) |

## What it can do

- Map any MIDI controller knob or key to 121 Mackie Control commands in Ableton Live
- Map a knob CC or note to a key stroke in the front app or to Mac volume
- Colour controller pads (E16 helper)
- Sign and package a DMG and publish a download site with a stable download URL

## Ask for it when

- use a MIDI knob as a keyboard shortcut
- control Ableton Live from a MIDI controller via Mackie Control
- map MIDI to keystrokes on the Mac

## How to control it

No control API found.

Evidence: No page server any more (README/app comments); Ports.swift can claim a port but no endpoints were seen in what was harvested

## Inputs / Outputs

Inputs:

- MIDI controller input via IAC Driver or device

Outputs:

- Mackie Control messages to Ableton
- key strokes
- Mac volume

## Hardware

- Any MIDI controller (E16 colour helper)
- Ableton Live with MackieControl surface and optional AbletonOSC

## Works with

- Uses: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md)
- Used by or talked to by: [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](MANTRA_CONTROLS.md)

## Code worth reusing

- `app/MackieEngine.swift`: Mackie Control engine: MIDI in to MCU commands for Live
- `app/MidiKeysEngine.swift`: MIDI to key stroke engine with rules
- `app/Ports.swift`: MANTRA_PORTS claim helper
- `app/Permissions.swift`: Accessibility and Input Monitoring permission handling

## Notes

Replaces MANTRA_CONTROLS windows and the Lua engines. Live Actions still carries the same modules: run one or the other on a controller, never both. Website mantramiditools.pages.dev; DMG under 25 MB.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_MIDI_TOOLS/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_MIDI_TOOLS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_MIDI_TOOLS/blob/HEAD/LESSONS.md)
