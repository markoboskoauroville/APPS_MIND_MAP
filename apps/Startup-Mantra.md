# Startup (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Small Mac login-item utility that chooses at startup between two voice apps: Voice to Text (Mantra) or Speechify, quitting the other.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Startup-Mantra](https://github.com/markoboskoauroville/Startup-Mantra) |
| Also called | Startup, Startup (Mantra) |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-19 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | none (no control api found) |

## What it can do

- Register itself as a login item
- Launch the chosen voice app and quit the other one
- Leave the chosen app alone when already running
- Warn when the chosen app is not installed

## Ask for it when

- choose which dictation app starts at login
- switch between Voice to Text and Speechify at boot

## How to control it

No control API found.

## Works with

- Uses: [Voice Engine (Mantra)](VOICE_ENGINE.md)
- Talks to: [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md)

## Notes

Apps handled: com.mantra.voicetotext and com.cliffweitzman.speechifymacagent. Window shows a toggle; closing it quits.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/Startup-Mantra/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/Startup-Mantra/blob/HEAD/LESSONS.md)
