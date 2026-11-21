# Audio Prefer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Background helper that makes the Mac's audio output follow a fixed order: the CQ12T mixer, then ADAM monitors, then the built-in speakers.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/audio-prefer](https://github.com/markoboskoauroville/audio-prefer) |
| Also called | audio prefer |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-10-26 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Switch the default output to the first available device in the preferred order
- Act at login and whenever an output is plugged in or removed
- Respect an output chosen by hand until the next plug-in
- Never take over BlackHole during a recording or test
- List outputs and apply the order once from the command line

## Ask for it when

- make the Mac use the mixer as sound output automatically
- fix audio output after plugging the CQ12T
- stop the Mac switching away from my speakers

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--list`
- `--once`

Example:

```
audio-prefer --once # sets the Mac's audio output to the first available device in the fixed order (CQ12T, ADAM monitors, ...)
```

More calls:

- show the order and what is present: `audio-prefer --list`

Evidence: README.md

## Inputs / Outputs

Outputs:

- Mac default audio output

## Hardware

- Allen & Heath CQ-12T
- ADAM Audio D3V
- MacBook Pro speakers

## Notes

Installed as a LaunchAgent via install.sh; one file main.swift with the order at the top.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
