# Plugin Assistant

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac rack of Audio Unit effects for the microphone (output to BlackHole) plus a Chrome extension that swaps the browser mic for it; local HTTP API.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/PLUGIN_ASSISTANT](https://github.com/markoboskoauroville/PLUGIN_ASSISTANT) |
| Also called | Plugin Assistant (Mantra), PatchWork-like rack |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS, Chrome |
| Language | Swift |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | http (own http routes) |

## What it can do

- Host a chain of Audio Unit effects on a chosen microphone
- Add, remove, move and bypass plug-ins, save and load presets
- Output to BlackHole 2ch so apps hear the processed mic
- Chrome extension swaps getUserMedia audio for BlackHole on the academy site
- Show input and output level meters

## Ask for it when

- put plug-ins on my microphone
- process the mic in the browser with AU effects
- vocal effects chain for lessons
- PatchWork-like mic rack

## How to control it

- Level: **http**
- Type: http
- Port: 8873

Actions:

- `GET /status`
- `GET /plugins`
- `GET /devices`
- `GET /presets`
- `POST /on`
- `POST /off`
- `POST /device`
- `POST /chain`
- `POST /preset/save`
- `POST /preset/load`
- `POST /ui/open`

**Before you call:** Plugin Assistant (Mantra) running on 8873.

Example:

```
curl -X POST http://127.0.0.1:8873/on
```

More calls:

- which plugins and devices: `curl -s 127.0.0.1:8873/plugins ; curl -s 127.0.0.1:8873/devices`
- load a preset: `curl -s -XPOST 127.0.0.1:8873/preset/load`
- switch off: `curl -s -XPOST 127.0.0.1:8873/off`

Evidence: TAKEOVER.md; extension/background.js (HOST 127.0.0.1:8873)

## Inputs / Outputs

Inputs:

- microphone

Outputs:

- processed audio to BlackHole 2ch

## Hardware

- microphone
- BlackHole 2ch virtual device

## Works with

- Talks to: [MPA Academy, website and hub](mpa-academy.md)

## Code worth reusing

- `app/Rack.swift`: AVAudioEngine Audio Unit rack with bypass, reorder and meters
- `extension/inject.js`: wraps getUserMedia to swap the mic for a named device

## Notes

/chain takes an action object (add/remove/move/bypass). Written without compiling on the Mac; first real run was left to Marko. Port moves to next free if busy. Body of /preset/load is not in the harvested docs.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/PLUGIN_ASSISTANT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/PLUGIN_ASSISTANT/blob/HEAD/LESSONS.md)
