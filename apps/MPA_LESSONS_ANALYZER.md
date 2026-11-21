# MPA Lessons Analyzer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac SwiftUI helper for the MPA Academy frame-drum lessons: splits voice/drums, transcribes, analyzes and assists shooting lessons; has a local HTTP API.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MPA_LESSONS_ANALYZER](https://github.com/markoboskoauroville/MPA_LESSONS_ANALYZER) |
| Also called | MPA Lessons Analyzer (Mantra), lessons analyzer, drumsplit |
| Visibility | public |
| Kind | app |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v8 |
| Control level | http (own http routes) |

## What it can do

- Open a lesson video, split voice and drums (drumsplit CLI)
- Send the voice track to Voice to Text for a transcript
- Show a Time/Transcription/Remarks table from analysis.json
- Play, watch and manage clips and takes full screen
- Run the Second Take shooting protocol on the LAN for a phone controller
- Finish a shoot: trim, H.265 vertical export, verify, write LESSON_DRAFT.md

## Ask for it when

- analyze a drum lesson video
- transcribe a lesson and mark sections
- split voice from drums in a recording
- shoot a lesson with the phone as remote
- trim and export lesson takes

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8965 (LAN Second Take protocol 8966)

**Warning:** port 8965 is also quoted for [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [Second Take Remote](SECOND_TAKE_REMOTE.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /status`
- `POST /open`
- `POST /transcribe`
- `GET /transcript`
- `GET /transcript/full`
- `GET /analysis`
- `POST /reload`
- `GET /strokes`
- `GET /clips`
- `GET /shots`
- `GET /takes`
- `GET /finish`
- `POST /split`
- `POST /play`
- `POST /stop`
- `POST /watch`
- `POST /shoot/start`
- `POST /shoot/action`
- `POST /mute`
- `POST /takes/add`
- `POST /finish/run`
- `GET /finish/result`

**Before you call:** MPA Lessons Analyzer (Mantra) must be running. Port 8965 may shift to the next free port; the actual port is in ~/.mantra/ports/mpa-lessons-analyzer. 8965 is ALSO the number of MANTRA_ROOM (Meditation Room): check which app answers (GET /status). LAN listener for Second Take on 8966.

Example:

```
curl -s -XPOST 127.0.0.1:8965/open -H 'Content-Type: application/json' -d '{"path":"~/Movies/lesson1.mov"}'
```

More calls:

- transcribe the opened video, then read it: `curl -s -XPOST 127.0.0.1:8965/transcribe ; curl -s 127.0.0.1:8965/transcript`
- play a part: `curl -s -XPOST 127.0.0.1:8965/play -H 'Content-Type: application/json' -d '{"start":10,"end":25}'`
- stop: `curl -s -XPOST 127.0.0.1:8965/stop`
- open the shooting window without the voice: `curl -s -XPOST 127.0.0.1:8965/shoot/start -H 'Content-Type: application/json' -d '{"quiet":true}'`

Evidence: TAKEOVER.md (Local API, API sections); app/Http.swift

## Inputs / Outputs

Inputs:

- lesson video/audio
- `<video>.analysis.json` written by Claude Code

Outputs:

- `<name>.voice.wav`
- `<name>.transcript.json` and .transcript.full.json
- trimmed H.265 clips
- LESSON_DRAFT.md

## Hardware

- Sony camera via Webcam Recorder / Sony remote

## Works with

- Uses: [Second Take Remote](SECOND_TAKE_REMOTE.md), [Voice Engine (Mantra)](VOICE_ENGINE.md)
- Talks to: [Mantra Voice (speech server)](MANTRA_VOICE.md), [Transcribe Voice to Text RT (Mantra) (retired)](MARKO_TRANSCRIBE.md), [Webcam Recorder (Mantra)](web-cam-viewer.md)
- Used by or talked to by: [MPA Academy, Android app](MPA_ACADEMY_ANDROID.md), [Second Take Remote](SECOND_TAKE_REMOTE.md), [Webcam Recorder (Mantra)](web-cam-viewer.md)

## Code worth reusing

- `drumsplit/main.swift`: CLI that splits a drum lesson into voice and drum tracks (ffmpeg + parameter presets)
- `app/Slicer.swift`: slicing of strokes/clips from audio
- `app/Http.swift`: small local HTTP server pattern for a SwiftUI app

## Notes

Port 8965 may shift to the next free port; actual number in ~/.mantra/ports/mpa-lessons-analyzer. SHOOT/TALK parts were never run per TAKEOVER. Built only by GitHub Actions (app.zip).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MPA_LESSONS_ANALYZER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MPA_LESSONS_ANALYZER/blob/HEAD/LESSONS.md)
