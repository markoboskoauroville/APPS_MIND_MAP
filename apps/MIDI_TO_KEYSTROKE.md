# MIDI to Key Stroke

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Turns a MIDI controller knob into a key press or the Mac volume through a CC/value/key table with detect and learn.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MIDI_TO_KEYSTROKE](https://github.com/markoboskoauroville/MIDI_TO_KEYSTROKE) |
| Also called | midikeys, MIDI to keystroke |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS, Hammerspoon |
| Language | Lua |
| Status | dormant |
| Last push | 2026-10-02 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Lock onto a USB MIDI device by turning a knob
- Map CC and value to a key press in the front app
- Map a knob to the Mac system volume with the native volume blob
- Learn a row by turning the knob and pressing a key
- Show an incoming MIDI monitor and activity LED

## Ask for it when

- map a MIDI knob to a keyboard shortcut
- control Mac volume with a MIDI knob
- trigger Ableton shortcuts from a controller

## How to control it

- Level: **http**
- Type: http
- Port: 8853

Actions:

- `GET /health`

**Before you call:** MIDI to Key Stroke must be running.

Example:

```
curl -s 127.0.0.1:8853/health # the only documented route; the mappings are set in the app window
```

Evidence: midikeys.lua line 561 (/health returns ok); the page is a web UI

## Inputs / Outputs

Inputs:

- MIDI Control Change messages

Outputs:

- key events
- system volume changes

## Hardware

- any USB MIDI controller
- IAC Driver for tests

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](MANTRA_CONTROLS.md)

## Code worth reusing

- `midiwatch.lua`: shared MIDI device watcher and incoming-message monitor
- `volume.lua`: press the Mac volume keys so the native blob appears
- `tablekeep.lua`: persist an editable rule table
- `e16led.lua`: LED colour output for the E16 controller

## Notes

Settings in ~/.config/midi-to-keystroke.json. Port claimed as midikeys (usually 8853). midiwatch.lua, volume.lua and tablekeep.lua are shared with other apps.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
