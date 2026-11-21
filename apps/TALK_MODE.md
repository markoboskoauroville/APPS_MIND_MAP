# Talk Mode (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app for talking with Claude Code sessions by voice: listens, transcribes, types into a chosen iTerm2 or VM session and reads the reply aloud.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TALK_MODE](https://github.com/markoboskoauroville/TALK_MODE) |
| Also called | Talk Mode, Space bar mode |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v8 |
| Control level | cli (command line or script only) |

## What it can do

- Listen with voice activity detection and send the words to a chosen Claude session
- Type into iTerm2 tabs by AppleScript or into tmux sessions on a VM
- Speak Claude's replies through the Mantra voice and replay the unheard ones
- Space bar mode: push-to-talk with a red screen edge and input lock
- Write its state to state.json with a plain-sentence summary
- Filter noise and sound tags such as laughs or music

## Ask for it when

- talk to Claude with my voice
- dictate to a terminal session and hear the reply
- hands-free conversation with Claude Code
- which session am I talking to

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `--preview <state> --shot f.png --size WxH`
- `--test-wav`
- `--edge-shot f.png`

**Before you call:** Talk Mode (Mantra) is a client of other apps' APIs (Voice to Text, Mantra Voice); no listening server found. Queen answers 'talk mode status'. Switch keys F5-F8 since v17.

Example:

```
# no call: read state.json of the app (folder not given in the docs); Queen answers 'talk mode status'
```

Evidence: TAKEOVER.md: debug flags and state.json; no listening server of its own found

## Inputs / Outputs

Inputs:

- microphone
- iTerm2 sessions and Claude session files
- Voice to Text engine selection

Outputs:

- typed text in terminal sessions
- spoken replies
- state.json
- archived AAC takes

## Hardware

- microphone

## Works with

- Uses: [Macro Recorder (Mantra)](MANTRA_MACRO.md), [Mantra Voice (speech server)](MANTRA_VOICE.md), [Voice Engine (Mantra)](VOICE_ENGINE.md)
- Used by or talked to by: [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md)

## Code worth reusing

- `app/ITerm.swift`: iTerm2 AppleScript: list sessions, write text without newline then Return
- `app/Audio.swift`: voice activity detection with noise-floor threshold
- `app/RedEdge.swift`: click-through red border overlay on all screens
- `app/Voice.swift`: client for the Mantra voice /hear and /speak API and phrase noise filters

## Notes

Client of other apps' APIs, no control door of its own found; its state is readable in state.json (Queen answers 'talk mode status'). Switch keys F5-F8 since v17. Built only by GitHub Actions. The exact folder of state.json is not given in the harvested docs.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/TALK_MODE/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/TALK_MODE/blob/HEAD/LESSONS.md)
