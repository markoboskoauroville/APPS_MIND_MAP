# Voice Engine (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that draws the subtitle band while Claude's voice speaks, with pause, stop and replay, and holds the global voice on/off switch (voiceengine).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_ENGINE](https://github.com/markoboskoauroville/VOICE_ENGINE) |
| Also called | Voice Engine, Voice Engine (Mantra), voiceengine, voicectl |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift (app) and Python (tools/voiceengine) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v64 |
| Control level | http (own http routes) |

## What it can do

- Show a word-lit subtitle card that follows the spoken voice on a chosen screen
- Pause, continue and stop the current reading; replay the last message from the menu bar
- Switch all speaking on or off at once (voiceengine on|off|toggle|status)
- Show the state of the speaking server, ears and cloned-voice processes
- Ask the voice server to close or stop a reading

## Ask for it when

- mute all Claude voices
- global voice on and off switch
- subtitle while Claude speaks
- replay what Claude just said
- pause the voice reading
- turn the computer voice off
- switch the voice engine on

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8837 (MANTRA_VOICE speaking server it talks to)

**Warning:** port 8837 is also quoted for [Mantra Voice (speech server)](MANTRA_VOICE.md) - confirm with `mantra-ports scan`.

Actions:

- `voiceengine on`
- `voiceengine off`
- `voiceengine toggle`
- `voiceengine status [--json]`
- `GET :8837/speaking`
- `POST :8837/speak/pause`
- `POST :8837/speak/stop`
- `POST :8837/speak/close`
- `GET :8837/health`

**Before you call:** Voice Engine (Mantra) is the window and the switch; the speech itself is done by MANTRA_VOICE on port 8837, which must be running. The off state does not touch speech to text.

Example:

```
voiceengine off (writes ~/.mantra/voice_engine_state and stops the current reading)
```

More calls:

- turn reading on, or flip it: `voiceengine on ; voiceengine toggle`
- state for a program: `voiceengine status --json`
- stop the current reading now: `curl -s -XPOST 127.0.0.1:8837/speak/stop`
- pause the current reading: `curl -s -XPOST 127.0.0.1:8837/speak/pause`

Evidence: TAKEOVER.md v64; tools/voiceengine docstring; universal/SPEC.md section 4

## Inputs / Outputs

Inputs:

- ~/.mantra/voice_engine_state
- MANTRA_VOICE /speaking

Outputs:

- subtitle window
- menu bar replay player
- state file

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md), [Voice Engine Universal (Mantra)](VOICE_ENGINE_UNIVERSAL.md)
- Used by or talked to by: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md), [Startup (Mantra)](Startup-Mantra.md), [Talk Mode (Mantra)](TALK_MODE.md), [Termux Tools](termux-tools.md)

## Code worth reusing

- `tools/voiceengine`: CLI for the one global voice ON/OFF state file
- `app/Subtitle.swift`: resizable subtitle card that follows the spoken word
- `app/Replay.swift`: menu bar replay player for the last spoken message
- `reply/main.swift`: reply helper binary

## Notes

The speech server itself is MANTRA_VOICE; this repo is the window and switch. The off state does not touch speech to text (/hear). Callers sending user:true (app reading on Marko's own click) still speak. Android sibling VOICE_ENGINE_ANDROID is retired.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/VOICE_ENGINE/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/VOICE_ENGINE/blob/HEAD/LESSONS.md)
