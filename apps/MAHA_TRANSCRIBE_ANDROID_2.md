# Maha Transcribe Android (native)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Native Kotlin/Compose rewrite of Maha Transcribe for Android; version 1 is the T (talk to type) screen only, built for a dyslexic, low-vision user.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_ANDROID_2](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_ANDROID_2) |
| Also called | Maha Transcribe Android 2, Talk To Type Android |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Record audio in a foreground service and save it as WAV
- Transcribe through a provider with the user's own key
- Apply edits, take/verdict/level logic and key ring on device
- Show a large-target Talk screen and a Gear (settings) screen

## Ask for it when

- native Android dictation app
- speech to text on Android with big buttons
- record and transcribe on the phone
- dictate on Android (v1: the T screen only)

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- microphone audio

Outputs:

- transcript text
- WAV recordings

## Hardware

- Android microphone

## Code worth reusing

- `app/src/main/kotlin/com/mantra/mahatranscribe/audio/Recorder.kt`: recording and WAV writing for Android
- `app/src/main/kotlin/com/mantra/mahatranscribe/logic/Keys.kt`: masked API key ring handling
- `app/src/main/kotlin/com/mantra/mahatranscribe/net/Transcribe.kt`: transcription HTTP call to a provider

## Notes

Only TAKEOVER.md (with former README) was harvested. Other screens are drawn but disabled in v1. No API; no key in repo. Has ATTRIBUTION.md.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_ANDROID_2/blob/HEAD/TAKEOVER.md)

_Low confidence: little was documented in this repository. Check the code before relying on this card._
