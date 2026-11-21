# Maha Transcribe Android v3 (web view, superseded) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Maha Transcribe Android (native)](MAHA_TRANSCRIBE_ANDROID_2.md). Replaced by MAHA_TRANSCRIBE_ANDROID_2.

**Maha Transcribe v3 for Android with the web UI in a WebView on an on-device server; superseded by the native MAHA_TRANSCRIBE_ANDROID_2.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_ANDROID](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_ANDROID) |
| Also called | Maha Transcribe v3, TTT Android |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin + HTML |
| Status | retired |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: build-4 |
| Control level | http (own http routes) |

## What it can do

- Record speech and store audio first, transcribe later
- Transcribe with AssemblyAI
- Run text features with Anthropic, Gemini and Groq
- Persist settings and recordings on the device
- Import keys from a file picker (masked only)

## Ask for it when

- dictate on Android and keep the audio safe
- transcribe speech to text on the phone
- speech-to-text app with AssemblyAI

## How to control it

- Level: **http**
- Type: http
- Port: loopback port of the on-device server, not stated in the docs

Actions:

- `GET /api/state`
- `GET /api/online`
- `GET/POST /api/settings`
- `POST /api/settings/reset`
- `GET/POST /api/recordings`
- `POST /api/keys/import`
- `POST /api/ai`

**Before you call:** Only reachable from inside the phone (the app's WebView server on 127.0.0.1); the app is superseded by MAHA_TRANSCRIBE_ANDROID_2 (native, T screen only in v1). Transcription uses AssemblyAI, text features Anthropic, Gemini or Groq, with keys from the user.

Example:

```
curl -s http://127.0.0.1:<port>/api/recordings # lists recordings; the web UI's own backend inside the app
```

Evidence: app/src/main/kotlin/com/mantraproductions/mahatranscribe/MahaServer.kt lines 56-73

## Inputs / Outputs

Inputs:

- microphone audio
- key file via picker

Outputs:

- transcripts
- stored recordings

## Hardware

- Android microphone

## Works with

- Uses: [TTT&LLL (Talk to Type, Look Listen Learn)](DictateKeyboard.md)

## Code worth reusing

- `app/src/main/kotlin/com/mantraproductions/mahatranscribe/MahaServer.kt`: in-app loopback HTTP server feeding a WebView UI

## Notes

Internal UI backend API (loopback), not the standard Mantra /health+/api door. Some routes (key import) return 'not yet'. Later superseded by the native MAHA_TRANSCRIBE_ANDROID_2. Needs git clone --recurse-submodules. RETIRED/SUPERSEDED: use MAHA_TRANSCRIBE_ANDROID_2 instead. The native replacement shows only the T (talk to type) screen in v1.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_ANDROID/blob/HEAD/README.md)
