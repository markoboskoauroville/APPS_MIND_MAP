# Voice Engine Android (retired) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Termux Voice (voiced)](TERMUX_VOICE.md). Replaced by TERMUX_VOICE.

**RETIRED Android app that drew a subtitle pop-up over every app while the phone spoke, with reply recording; replaced by TERMUX_VOICE.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_ENGINE_ANDROID](https://github.com/markoboskoauroville/VOICE_ENGINE_ANDROID) |
| Also called | Voice Engine Android, community.auroville.voiceengine |
| Visibility | public |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Kotlin |
| Status | retired |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v27 |
| Control level | http (own http routes) |

## What it can do

- Draw a word-lit subtitle over any app (historical)
- Pause, stop and hide the subtitle from a notification
- Record a spoken reply and send it back to the Mac
- Play audio clips posted to it with its own MediaPlayer

## Ask for it when

- subtitle over apps on the phone while it speaks (retired)
- phone voice with reply button (retired)

## How to control it

- Level: **http**
- Type: http
- Port: 8720 (app side, 8720-8735 range)

Actions:

- `POST /start`
- `POST /pos`
- `POST /end`
- `POST /play`
- `POST /say`

**Before you call:** RETIRED, replaced by TERMUX_VOICE; the app side served POST /say on 8720.

Example:

```
# retired: use TERMUX_VOICE: phonesay pixel "text"
```

Evidence: TAKEOVER.md lines 65-114; universal/SPEC.md (phone calls). RETIRED 15.11.2026, so do not rely on it

## Inputs / Outputs

Inputs:

- talker feed from Termux

Outputs:

- subtitle overlay
- reply recordings

## Hardware

- Android phones (Nothing A142)

## Works with

- Uses: [MA Reader Termux / macOS (Edge / Speechify)](MA_READER_TERMUX_MACOS.md), [Voice Engine Universal (Mantra)](VOICE_ENGINE_UNIVERSAL.md)
- Talks to: [Termux Voice (voiced)](TERMUX_VOICE.md)

## Code worth reusing

- `android/app/src/main/java/community/auroville/voiceengine/GroqKeys.kt`: encrypted key ring read from a key file with forward-only cursor
- `android/app/src/main/java/community/auroville/voiceengine/Overlay.kt`: subtitle overlay drawn over other apps

## Notes

RETIRED 15.11.2026 by Marko: only TERMUX_VOICE (voiced :8840) is the voice engine on the phones. Use TERMUX_VOICE instead. Repo pushed recently only for housekeeping. RETIRED/SUPERSEDED: use TERMUX_VOICE instead.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/VOICE_ENGINE_ANDROID/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/VOICE_ENGINE_ANDROID/blob/HEAD/LESSONS.md)
