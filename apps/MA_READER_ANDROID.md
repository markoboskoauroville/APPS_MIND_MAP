# MA Reader for Android

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android port of the MA Reader screen (paste text, sentence split, library, voice list) that does not speak yet; the voice client is not built.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MA_READER_ANDROID](https://github.com/markoboskoauroville/MA_READER_ANDROID) |
| Also called | MA Reader Android, MA Reader v26 |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin + HTML |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: build-2 |
| Control level | http (own http routes) |

## What it can do

- Take pasted text and split it into sentences as the Mac reader does
- Show it in the OpenDyslexic-friendly web UI
- Save and manage a library of texts
- List English and Croatian voices
- Serve the Mac reader's /api/* endpoints from a local NanoHTTPD server (audio, bounds, export, offline and gemini are stubs)

## Ask for it when

- MA Reader on the phone (native app, text only for now)
- paste text and keep a reading library on Android

## How to control it

- Level: **http**
- Type: http
- Port: loopback port of the on-device server, not stated in the docs

Actions:

- `GET /api/voices`
- `GET /api/langs`
- `GET /api/state`
- `POST /api/prepare`
- `/api/library/* (save, list, open, delete, bulk delete, delete all)`
- `/api/audio (stub)`
- `/api/bounds (stub)`
- `/api/export (stub)`
- `/api/offline/* (stub)`
- `/api/gemini/* (stub)`

**Before you call:** Only reachable from inside the phone. Text is pasted, split into sentences, rendered and archived; the voice client is the next step (README: 'It does not speak yet'). To read aloud with highlighting on the phone today use MA_READER_TERMUX_MACOS or MA_READER_SPEECHIFY (Termux).

Example:

```
curl -s http://127.0.0.1:<port>/api/voices # lists English and Croatian voices; the app does NOT speak yet
```

Evidence: HANDOFF.md lines 32-38; MaServer.kt

## Inputs / Outputs

Inputs:

- pasted text

Outputs:

- rendered sentences
- library entries

## Works with

- Uses: [MA Reader Engine](MA_READER_ENGINE.md)
- Used by or talked to by: [MA Reader Engine](MA_READER_ENGINE.md)

## Code worth reusing

- `app/src/main/kotlin/dev/mantraproductions/reader/text/MaText.kt`: clean_text and split_units ported from Python, tested against it

## Notes

Per README it does not speak yet. The speech engine is in MA_READER_ENGINE (clone with submodules). Internal UI backend API only. Reading aloud with word highlighting on Android is done by MA_READER_TERMUX_MACOS / MA_READER_SPEECHIFY (browser reader in Termux) and by the LLL reader inside TTT (DictateKeyboard), which uses MA_READER_ENGINE.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MA_READER_ANDROID/blob/HEAD/README.md)
