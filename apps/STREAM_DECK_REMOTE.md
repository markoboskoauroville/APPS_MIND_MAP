# Stream Deck Remote

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android phone mirror of the Elgato 15-key Stream Deck with a Mac helper: app switcher, OBS scenes and a classroom profile for the MPA online lessons.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STREAM_DECK_REMOTE](https://github.com/markoboskoauroville/STREAM_DECK_REMOTE) |
| Also called | Stream Deck Remote (Mantra), StreamDeck remote, streamdeck-remote |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Android |
| Language | Swift (Mac) and Kotlin (Android) |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v6 |
| Control level | http (own http routes) |

## What it can do

- Show a 5x3 deck on the phone mirrored with the real deck
- APPS profile: switch applications
- OBS profile: one key per scene via obs-websocket
- CLASSROOM profile: layouts, mic, echo/noise, camera and swap for the teacher in the MPA room
- Find the Mac by Bonjour or adb reverse over USB

## Ask for it when

- use my phone as a Stream Deck
- switch OBS scenes from the phone
- remote for the MPA classroom
- press deck keys from Android
- use a Stream Deck as an application switcher
- drive a Stream Deck without the Elgato app

## How to control it

- Level: **http**
- Type: http, websocket
- Port: 8963 (MANTRA_PORTS streamdeck-remote)

Actions:

- `GET /hello`
- `GET /state?profile=apps|obs&v=N`
- `GET /press?profile=...&key=0..14`
- `GET /icon?id=<bundle id>`

**Before you call:** Mac app (port 8963, MANTRA_PORTS id streamdeck-remote); the phone shows Stream Deck pages.

Example:

```
curl 'http://127.0.0.1:8963/press?profile=obs&key=0'
```

More calls:

- state of a profile: `curl -s 'http://127.0.0.1:8963/state?profile=apps'`
- hello: `curl -s http://127.0.0.1:8963/hello`

Evidence: TAKEOVER.md 'The wire' section

## Inputs / Outputs

Inputs:

- phone taps
- real Stream Deck keys

Outputs:

- app switches
- OBS scene changes
- classroom room commands

## Hardware

- Elgato Stream Deck 15-key

## Works with

- Talks to: [MPA Academy, website and hub](mpa-academy.md)
- Used by or talked to by: [Stream Deck Control (Mantra), retired (retired)](stream-deck-control.md)

## Code worth reusing

- `mac/app/OBS.swift`: obs-websocket v5 client reading port and password from OBS config
- `mac/app/Classroom.swift`: joins the MPA classroom websocket as a hidden teacher remote
- `mac/app/Deck.swift`: 15-key deck model and key rendering

## Notes

Two builds: Mac release `mac-v<N>`, APK release `v<N>`. Phone APK v6 was installed but never opened at last note. Keys were not pressed during a live lesson.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/STREAM_DECK_REMOTE/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/STREAM_DECK_REMOTE/blob/HEAD/LESSONS.md)
