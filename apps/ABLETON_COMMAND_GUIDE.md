# Ableton Command Guide

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local voice chat page that answers shortcut questions about Ableton Live and performs spoken orders in Live over AbletonOSC.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ABLETON_COMMAND_GUIDE](https://github.com/markoboskoauroville/ABLETON_COMMAND_GUIDE) |
| Also called | Ableton Guide, Ableton command guide, guide app |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Web, Hammerspoon |
| Language | Python |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Answer how-do-I questions about Ableton Live as cards
- Listen by voice (local Whisper) and read answers aloud with word highlighting
- Do spoken orders in Live (tempo, play, mute) by sending AbletonOSC messages
- Rotate through several Gemini free keys with Haiku as fallback and probe keys at start
- Tile Live beside the page
- Open as a bubble from a global hotkey via the star menu

## Ask for it when

- ask Ableton how to do something by voice
- tell Ableton to start playing
- set the tempo in Live by voice
- mute a track in Live by speaking

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8843

Actions:

- `GET /health`
- `guide.py ask`
- `guide.py keys`
- `guide.py test`
- `guide.py state`

**Before you call:** Run in the repo folder; the page server guided.py serves the card page on 127.0.0.1:8843 and Live needs AbletonOSC for spoken orders (UDP 11001 is held by one process only).

Example:

```
python3 guide.py ask "how do I split a clip" # answer from the key ring (Gemini, then Haiku); a spoken order is performed in Live
```

More calls:

- one engine for this question: `python3 guide.py ask --engine haiku "how do I loop a clip"`
- probe the whole key ring, one line per key: `python3 guide.py keys`
- ears, mouth and one answer: `python3 guide.py test`
- is the page alive: `curl -s http://127.0.0.1:8843/health`

Evidence: README.md "From the terminal" section

## Inputs / Outputs

Inputs:

- voice via local Whisper
- typed questions

Outputs:

- answer cards
- spoken answers
- OSC messages to Live

## Hardware

- microphone

## Works with

- Uses: [Teacher Lessons and Scripts (Ableton, DaVinci)](ABLETON_TEACHER.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Code worth reusing

- `guide.py`: API key ring with probing, verdicts, dead-key fingerprints and engine fallback
- `act.py`: turns a spoken order into AbletonOSC messages restricted to /live/ addresses

## Notes

Only health plus CLI, no declared /api action list. Port 11001 can be held by only one process (the teacher).

## Docs in the repo

- `README.md`
- `CLAUDE.md`
