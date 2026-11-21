# Voice Cloning (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac window to clone a voice from a file or the microphone, choose which voice talks and test every voice, over the MANTRA_VOICE API.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_CLONING](https://github.com/markoboskoauroville/VOICE_CLONING) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v3 |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- List voices and make one the talking voice
- Clone a voice from a file range or 15 s of microphone
- Remove a voice after asking
- Run the test of every voice with ears playback

## Ask for it when

- clone a new voice
- change which voice the computer uses

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "voice cloning" "top"
```

More calls:

- list the controls of the window: `star read "voice cloning"`
- start the app in the background: `star open "voice cloning"`
- quit it: `star quit "voice cloning"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Notes

Never starts the voice server; says so when it is down. Needs microphone permission for the mic option. AX ids include permissions.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
