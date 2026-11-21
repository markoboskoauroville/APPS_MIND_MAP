# Screen Copy (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app showing every Android phone's screen in tabs (own scrcpy-protocol client), with audio, recording, mic link and a local control API and Python client.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_SCREEN_COPY](https://github.com/markoboskoauroville/MANTRA_SCREEN_COPY) |
| Also called | Screen Copy, Screen Copy (Mantra), screencopy, scrcpy tabs |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Android |
| Language | Swift (+ Python client) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Show one tab per Android phone, found automatically over USB, Wi-Fi adb or Tailscale
- Play phone audio with a jitter buffer and per-tab volume, global mute
- Record each phone's screen/audio with start/pause/resume/stop/next/rename
- Send taps, keys and text to the active phone
- Link the Mac microphone to the phone over adb reverse (port 8879)
- Rotate between portrait and landscape from the window

## Ask for it when

- see my Android phone on the Mac
- record the phone screen to a file
- tap or type on the phone from the Mac by script
- mirror several phones at once

## How to control it

- Level: **http**
- Type: http, cli, url-scheme
- Port: 8883 (tries up to 8898; chosen port in ~/.mantra/ports/screen-copy)

Actions:

- `GET /tabs`
- `GET /status`
- `POST /record/start`
- `POST /record/pause`
- `POST /record/resume`
- `POST /record/stop`
- `POST /record/next`
- `POST /record/rename`
- `POST /record/monitor`
- `POST /tab/select`
- `POST /tap`
- `POST /key`
- `POST /text`
- `CLI: screencopy tabs|status|record start|record pause|record next|monitor off|tab select N|tap X Y|key CODE|text ".."`
- `URL: screencopy://tab/N, rotate, tap/<x>/<y>, record/start|pause|resume|stop|next|rename`

**Before you call:** Screen Copy (Mantra) must be running (port 8883, up to 8898; the chosen port is in ~/.mantra/ports/screen-copy) and the phone connected by adb (Wi-Fi adb needs the Local Network permission).

Example:

```
curl -s -XPOST 127.0.0.1:8883/record/start # records the selected phone tab; CLI: screencopy record start --serial emulator-5556 --name "01 Title"
```

More calls:

- stop the recording: `curl -s -XPOST 127.0.0.1:8883/record/stop`
- which phones are in tabs: `curl -s 127.0.0.1:8883/tabs`
- tap on a phone screen: `screencopy tap 540 1200`
- pause, then next take: `screencopy record pause ; screencopy record next`

Evidence: TAKEOVER.md section 'v31 control API'; app/ControlServer.swift; python/screencopy.py

## Inputs / Outputs

Inputs:

- adb-connected Android phones

Outputs:

- screen recordings
- live phone view
- mic audio to phone

## Hardware

- Android phones over USB/Wi-Fi/Tailscale
- Mac microphone

## Works with

- Talks to: [Mantra Sandbox](MANTRA_SANDBOX.md), [TTT Voice Type keyboard](TTT.md)
- Used by or talked to by: [TTT Voice Type keyboard](TTT.md)

## Code worth reusing

- `app/Session.swift`: scrcpy-server protocol client: video H.264 to VideoToolbox, raw audio
- `app/Audio.swift`: jitter-buffered audio output per tab
- `app/ControlServer.swift`: loopback HTTP JSON control server with port range
- `app/Recorder.swift`: per-phone recorder with pause and next-clip
- `python/screencopy.py`: urllib-only client CLI

## Notes

Loopback only. Skill file in skills/screen-copy/SKILL.md. Needs macOS Local Network permission for Wi-Fi adb. Releases v7-v9 tagged; latest version is the v32 in TAKEOVER (tag list truncated).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_SCREEN_COPY/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_SCREEN_COPY/blob/HEAD/LESSONS.md)
