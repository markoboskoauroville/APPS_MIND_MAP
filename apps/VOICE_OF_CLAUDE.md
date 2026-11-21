# Voice of Claude (Mantra) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Voice Engine (Mantra)](VOICE_ENGINE.md). Replaced by VOICE_ENGINE.

**Mac window with one switch to start or stop the whole voice engine (door, ears, cloned voice) and remember the choice.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_OF_CLAUDE](https://github.com/markoboskoauroville/VOICE_OF_CLAUDE) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-11-01 |
| Build / release | GitHub workflow: no; latest release: v4 |
| Control level | cli (command line or script only) |

## What it can do

- Start the voice server through its LaunchAgent and stop all three parts
- Show each part running or stopped
- Disable or enable the LaunchAgent so the state survives login

## Ask for it when

- turn the computer voice off
- switch the voice engine on

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `--on`
- `--off`
- `--status`
- `engine-on`
- `engine-off`
- `top`
- `close`

**Before you call:** Retired; flags --on, --off, --status existed.

Example:

```
# archived: merged into Voice Engine (Mantra); use: voiceengine on
```

Evidence: TAKEOVER.md and README.md (flags and AX ids)

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Notes

Merged on 1.11.2026 into Voice Engine (Mantra) in the repo VOICE_ENGINE; no longer built or installed. RETIRED/SUPERSEDED: use VOICE_ENGINE instead.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
