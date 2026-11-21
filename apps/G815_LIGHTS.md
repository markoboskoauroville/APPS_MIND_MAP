# G815 Lights

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Runs the Logitech G815 keyboard's 115 keys as a low-resolution LED display for any app: pictures, colours, key colours, ten light shows, idle show.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/G815_LIGHTS](https://github.com/markoboskoauroville/G815_LIGHTS) |
| Also called | G815 Lights, Logitech lights, keyboard lights, G815 lights app |
| Visibility | public |
| Kind | app |
| Category | [Lights, keyboard and visuals](../capabilities/lights-keyboard-visuals.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v39 |
| Control level | http (own http routes) |

## What it can do

- Show a picture on the keyboard (area-averaged per key in linear light, gamma 1.8)
- Set a flat colour or per-key colours
- Start one of ten shows (sweep, rainbow, digits, rain, ripple, scan, checker, chase, sparkle, heartbeat) or all
- Stream live frames over TCP
- Stop the show at once when a real key is pressed and resume 300 s after the last key, restoring Marko's profile
- Light the Resolve page buttons with macros and switch pages through the router
- Update itself from main when VERSION is higher

## Ask for it when

- show a picture on my keyboard lights
- light the G815 keys
- keyboard light show
- make my keyboard display what the app shows
- flash the keyboard when something happens

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8877 HTTP and 8878 TCP stream (loopback)

Actions:

- `GET /status`
- `GET /layout`
- `GET /shows`
- `POST /frame`
- `POST /show`
- `POST /stop`
- `POST /config`
- `TCP 8878: type byte R/I/J + 4-byte length + payload`
- `build/g815 status`
- `build/g815 shows`
- `build/g815 layout`
- `build/g815 stop`
- `build/g815 show <name|all> [s]`
- `build/g815 frame <picture> [fit]`
- `build/g815 frame color <hex>`
- `build/g815 frame keys 26:ff0000 ...`

**Before you call:** The G815 Lights app must be running (if GET /status does not answer, open ~/Developer/G815_LIGHTS/build/"G815 Lights.app"). Loopback only.

Example:

```
curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"color":"ff0000"}'
```

More calls:

- show a picture on the keyboard (fit stretch|contain|cover): `build/g815 frame ~/Pictures/pic.png contain # from the repo checkout; or: curl -s -XPOST '127.0.0.1:8877/frame?fit=cover&ttl=20' -H 'Content-Type: image/png' --data-binary @pic.png`
- play a light show for 20 seconds: `curl -s -XPOST 127.0.0.1:8877/show -H 'Content-Type: application/json' -d '{"name":"rainbow","seconds":20}'`
- light single keys: `curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"keys":{"26":"ff0000"},"keep":false}'`
- hand the keyboard back: `curl -s -XPOST 127.0.0.1:8877/stop`

Evidence: TAKEOVER.md v35 entry; app/LightShow.swift; MANTRA_MANIFEST keyboard-lights.md

## Inputs / Outputs

Inputs:

- bitmaps
- hex colours
- key:colour lists
- frame stream

Outputs:

- LED colours on the keyboard

## Hardware

- Logitech G815 keyboard (HID++)

## Works with

- Uses: [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md), [Mantra Ports](MANTRA_PORTS.md)
- Talks to: [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md)
- Used by or talked to by: [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md), [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) will drive this app (optional, through the G815 Lights API only, never direct) [http 8877]

## Code worth reusing

- `src/hidpp.swift`: Logitech HID++ per-key lighting
- `app/LightShow.swift`: HTTP and TCP light API, ten shows, picture-to-keys mapping, yield-to-typing
- `src/lightclient.swift`: Swift client for the light API
- `tools/lightshow.py`: Python client for the light API
- `layout.json`: 115 key positions on a 24 x 7.5 key-unit board

## Notes

A key shows nothing below value 45 (dead zone); about 19 fps reach the keyboard. If GET /status does not answer the app is not running. 24 x 7.5 key unit board in GET /layout order. Idle show ends when a key is pressed; frames arriving while paused are accepted and dropped. Marko's rule: always provide one copy-paste command block in MANIFEST.md. POST /frame body forms (from the manifest module keyboard-lights): image/png or jpeg bytes with ?fit= and ?ttl=; or JSON {"path"}, {"image_base64"}, {"rgb":[[r,g,b] x115]}, {"keys":{"26":"ff0000"}}, {"color":"rrggbb"}. Show names: sweep rainbow digits rain ripple scan checker chase sparkle heartbeat, or all.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/G815_LIGHTS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/G815_LIGHTS/blob/HEAD/LESSONS.md)
- [CLAUDE.md](https://github.com/markoboskoauroville/G815_LIGHTS/blob/HEAD/CLAUDE.md)
