# Voice Engine Universal (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Shared pause, continue and word-timing rules for the subtitle that follows the voice, in Swift and Kotlin, used as a submodule by the voice apps.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_ENGINE_UNIVERSAL](https://github.com/markoboskoauroville/VOICE_ENGINE_UNIVERSAL) |
| Also called | Voice Engine Universal |
| Visibility | public |
| Kind | library-module |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android |
| Language | Swift and Kotlin |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Define the PAUSE/CONTINUE mechanism in Swift and Kotlin
- Provide Reading.kt for words, pieces and the clock
- Specify the calls between the voice server and the subtitle (SPEC.md)

## Ask for it when

- shared subtitle pause logic
- word-exact pause for a speaking server
- spec for subtitle following the voice

## How to control it

No control API found.

## Works with

- Talks to: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Voice Engine (Mantra)](VOICE_ENGINE.md), [Voice Engine Android (retired)](VOICE_ENGINE_ANDROID.md)

## Code worth reusing

- `swift/PauseSync.swift`: pause/continue state machine for a subtitle synced to a voice server
- `kotlin/PauseSync.kt`: same pause/continue logic for Android
- `kotlin/Reading.kt`: words, pieces and clock for a reading
- `SPEC.md`: the call contract between voice server and subtitle

## Notes

Not an app: consumed as submodule universal/ by VOICE_ENGINE (v39+) and VOICE_ENGINE_ANDROID. Public, no secrets.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/VOICE_ENGINE_UNIVERSAL/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/VOICE_ENGINE_UNIVERSAL/blob/HEAD/LESSONS.md)
