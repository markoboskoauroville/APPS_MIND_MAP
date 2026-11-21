# MPA Academy, Android app

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app of the Mantreshwar Percussions Academy: plays frame-drum exercises with drum and voice samples and a lit cell that follows the sound.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MPA_ACADEMY_ANDROID](https://github.com/markoboskoauroville/MPA_ACADEMY_ANDROID) |
| Also called | MPA Academy, Mantreshwar Percussions Academy app, MPA academy Android, Exercise Lab Android |
| Visibility | public |
| Kind | app |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | none (no control api found) |

## What it can do

- Play frame-drum exercises (currently PH01 Basic Phrasing) at speeds 16/1 to 16/32
- Play with voice or drum samples through AudioTrack
- Light the current cell in time with the playback
- Pin its icon to the launcher via an intent (am start --ez pin true)
- Load exercises from a generated exercises.json

## Ask for it when

- practise frame drum phrasing on the phone
- play the academy exercises on Android
- drum exercise player with a moving light
- add an exercise to the academy app

## How to control it

No control API found.

Example:

```
adb shell am start -n com.mantra.mpaacademy/.MainActivity --ez pin true
```

Evidence: TAKEOVER.md (v2 note); only the pin-shortcut intent is documented, no control API

## Inputs / Outputs

Inputs:

- android/app/src/main/assets/exercises.json
- drum samples (D, P, T, k, touch .wav)

Outputs:

- audio playback
- APK named `<N>-mpa-academy-v<N>.apk`

## Works with

- Talks to: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)

## Code worth reusing

- `android/app/src/main/java/com/mantra/mpaacademy/Engine.kt`: AudioTrack sample sequencer whose light follows playbackHeadPosition
- `tools/phrasing-rhythms.mjs`: generates phrasing rhythm data for exercises.json

## Notes

Built only by GitHub Actions (signed APK, release `v<N>`). Public, no README. Version 1 holds a single exercise. Control API: none beyond the pin intent.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MPA_ACADEMY_ANDROID/blob/HEAD/TAKEOVER.md)
