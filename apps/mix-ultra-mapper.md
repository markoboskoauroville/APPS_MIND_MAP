# Controller Mapper (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that maps any USB MIDI controller by guiding the owner through every control, lighting its LEDs, and saves a capture JSON.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mix-ultra-mapper](https://github.com/markoboskoauroville/mix-ultra-mapper) |
| Also called | Mix Ultra mapper, controller mapper |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Draw a controller from a layout JSON and point at the next control with an amber ring
- Record what each control sends over USB MIDI and advance by itself
- Light the control's own LED when it has one
- Save a capture JSON for DJ Mantra's mapping tools
- Resume after restart and allow back, redo, skip and start over

## Ask for it when

- map a new MIDI controller
- record all controls of the Hercules DJControl Mix Ultra
- create a layout for another DJ controller

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `open -a ... --args layout.json`
- `AX off`
- `AX top`
- `AX close`

**Before you call:** Controller Mapper (Mantra) opens a layout file per controller; its buttons are Accessibility ids off, top, close (press with STAR_API).

Example:

```
open -a "Controller Mapper (Mantra)" --args /path/layout.json
```

More calls:

- press a button through Star API: `star press "controller mapper" "top"`

Evidence: README.md, TAKEOVER.md (v5 Accessibility ids)

## Inputs / Outputs

Inputs:

- controller layout JSON
- USB MIDI from the controller

Outputs:

- capture JSON (midi_capture schema)

## Hardware

- Hercules DJControl Mix Ultra
- any USB MIDI controller

## Works with

- Uses: [DJ Mantra (Android DJ app)](djmantra_app.md)

## Code worth reusing

- `layouts/hercules-djcontrol-mix-ultra.json`: controller layout format (shapes, LEDs, steps) usable as a template
- `tools/make_mix_ultra_layout.py`: generates a controller layout from measured positions

## Notes

Layout file per controller is the template. A full run by Marko was still pending at last note.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
