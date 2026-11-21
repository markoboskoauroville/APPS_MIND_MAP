# Mantra Room (Meditation Room / Chakra and Elements Toning)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Meditation app (Android, Mac, Linux): chakra toning with MilkDrop visuals, element stripes, breath circle and timer; the Mac version loops tracks to any output.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_ROOM](https://github.com/markoboskoauroville/MANTRA_ROOM) |
| Also called | Meditation Room, Meditation Room (Mantra), Mantra Room, Chakra and Elements Toning, Chakra Toning (Mantra), meditation-room |
| Visibility | public |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | macOS, Android, Linux, Web |
| Language | Kotlin + JavaScript (Android), Swift (Mac), Python (Linux) |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | door (standard door) |

## What it can do

- Play the guided chakra toning mix with MilkDrop (butterchurn) visuals and 100 presets
- Show five element stripes to sing along (A, U, I, O, A-U-I-O) and a breath circle (4-6, box, 4-7-8)
- Run a session timer with fade and soft bell, background play, practice log
- On Mac: play thirteen tracks in a loop to any chosen output without changing the default output
- On Mac: send the picture to a Logitech G815 keyboard as a small display via G815 Lights
- On Mac and Linux: publish the visuals as an NDI/HLS stream, with melting text captions and pre-show

## Ask for it when

- play meditation toning with visuals
- loop meditation audio to a chosen output until a time
- put visuals on the keyboard lights
- stream the meditation visuals
- breathing circle and session timer

## How to control it

- Level: **door**
- Type: remote-door-http, http
- Port: 8965 (id meditation-room, Mac, 127.0.0.1 only)

**Warning:** port 8965 is also quoted for [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md), [Second Take Remote](SECOND_TAKE_REMOTE.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `GET /api`
- `GET /api/state`
- `POST /api/play-loop {output, until, lights, gain_db, from}`
- `POST /api/next`
- `POST /api/stop`
- `POST /api/lights {on}`
- `POST /api/output {name}`
- `POST /api/outputs`
- `POST /api/gain {db}`
- `POST /api/style {to}`
- `POST /api/status`
- `POST /api/text`
- `/fn/<action> for STAR_API`

**Before you call:** The app must be running (open -g -a "Meditation Room (Mantra)"); it answers on 127.0.0.1 only, and the port is claimed through MANTRA_PORTS under the id meditation-room.

Example:

```
curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'
```

More calls:

- stop the sound: `curl -s -XPOST 127.0.0.1:8965/api/stop`
- keyboard lights on or off: `curl -s -XPOST 127.0.0.1:8965/api/lights -d '{"on":false}'`
- list audio outputs, then pick one: `curl -s -XPOST 127.0.0.1:8965/api/outputs`
- what is playing now: `curl -s 127.0.0.1:8965/api/state`

Evidence: mac/app/Door.swift lines 2-5, 41, 88-91; TAKEOVER.md lines 241-244

## Inputs / Outputs

Inputs:

- guide.mp3 toning mix and element songs
- MilkDrop/butterchurn presets

Outputs:

- audio to chosen output
- visuals window
- NDI stream named Meditation Room
- G815 keyboard frames

## Hardware

- Logitech G815 keyboard
- any audio output (e.g. BlackHole 2ch)
- NDI network

## Works with

- Uses: [G815 Lights](G815_LIGHTS.md), [Mantra Ports](MANTRA_PORTS.md), [DJ Mantra Ecstatic Dance page](djmantra-ecstatic-dance.md)
- Talks to: [Star API (Mantra)](STAR_API.md)
- Used by or talked to by: [G815 Lights](G815_LIGHTS.md), [Marko Bosko Therapies](MARKOBOSKO_THERAPIES.md), [Streaming Dashboard (Mantra)](STREAMING_DASHBOARD.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) and this app will drive each other (room drives the light; the light follows the visualization colours) [door 8965]

## Code worth reusing

- `mac/app/Door.swift`: standard remote-door HTTP server (/health, /api, `/api/<action>`) in Swift
- `mac/app/Lights.swift`: turn the visual into G815 key colours with bilinear sampling
- `mac/app/Ndi.swift`: NDI output of the visuals
- `mac/app/Player.swift`: loop playback to a chosen output device
- `linux/mrvisuals.py`: headless MilkDrop visual render for streaming
- `android/app/src/main/assets/web/vendor/butterchurn.min.js`: MilkDrop visualizer in the browser (vendored)

## Notes

Android app has no INTERNET permission. Mac releases are tagged mac-vN (not Latest); Android vN owns releases/latest. Only one painter on the G815 at a time (do not run lightshow.py with it). Linux part has services, HLS :8989 and API :9994 for a visual test, and an NDI-like stream version. Start from the shell instead of HTTP: open -g -a "Meditation Room (Mantra)" --args --play-loop --output "BlackHole 2ch" --lights --until 11:55 --gain-db -5 (from TAKEOVER). Port 8965 is also quoted for MPA_LESSONS_ANALYZER and SECOND_TAKE_REMOTE: confirm with GET /health (this app answers app: meditation-room) before calling.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_ROOM/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_ROOM/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_ROOM/blob/HEAD/LESSONS.md)
