# MA Reader Termux / macOS (Edge / Speechify)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Single-file installer for a browser reader on Termux or macOS that speaks text aloud and lights each word, with Edge and Speechify voices and a key ring.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MA_READER_TERMUX_MACOS](https://github.com/markoboskoauroville/MA_READER_TERMUX_MACOS) |
| Also called | MA Reader, mareadweb, maread-update, MA Reader Termux |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android, Termux |
| Language | Shell (embedded Python/Flask) |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Read pasted text aloud with word and sentence highlighting
- Use Edge TTS or Speechify voices in English and Croatian
- Pause between words and sentences
- Keep a Speechify key ring and import keys
- Keep a library and offline audio, and export
- Auto-update at start with maread-update

## Ask for it when

- read text aloud on the phone or Mac with the word lit
- text to speech reader with word highlighting
- read aloud with highlighting on Android (in Termux, in Chrome)
- install the MA Reader

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8081

**Warning:** port 8081 is also quoted for [MA Reader Speechify module](MA_READER_SPEECHIFY.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /api/engines`
- `POST /api/say {text, lang}`
- `POST /api/prepare`
- `GET /api/audio/<tid>/<vkey>/<idx>.mp3`
- `GET /api/bounds/<tid>/<vkey>/<idx>`
- `GET /api/langs`
- `GET /api/voices`
- `GET /api/state`
- `GET /api/library`
- `GET /api/preview/<vkey>`
- `POST /api/mediakey`
- `GET /api/mediastatus`
- `POST /api/appswitch`
- `GET /api/speechify/status`
- `GET /api/gemini/status`
- `CLI: mareadweb`
- `CLI: maread-update [--online|--remove]`

**Before you call:** Install with the single-file installer (Termux or macOS); start with mareadweb, which serves the page on 8081 (updates with maread-update). Keys for Speechify come from KEYRING_TERMUX; Edge voices need no key.

Example:

```
curl -s -X POST http://127.0.0.1:8081/api/say -H 'Content-Type: application/json' -d '{"text":"hello","lang":"en"}' -o out.mp3
```

More calls:

- list voices: `curl -s 127.0.0.1:8081/api/voices`
- list engines (Edge, Speechify): `curl -s 127.0.0.1:8081/api/engines`
- update to the newest version: `maread-update`
- state of the reader: `curl -s 127.0.0.1:8081/api/state`

Evidence: api.txt routes; handover section (curl 127.0.0.1:8081, /api/say)

## Inputs / Outputs

Inputs:

- text
- Speechify keys

Outputs:

- mp3 audio
- word bounds

## Works with

- Uses: [Keyring](KEYRING_TERMUX.md)
- Used by or talked to by: [Voice Engine Android (retired)](VOICE_ENGINE_ANDROID.md)

## Code worth reusing

- `2py_word_timing_lab.py`: word timing experiments
- `2py_gate_audit.py`: delivery gate audit script
- `update.sh`: self-update installer pattern

## Notes

Port 8081 taken from the handover's check command. Docs are numbered markdown files (handover, four tests, working rules, Speechify engine handoff). Source Flask code lives in the installer scripts.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MA_READER_TERMUX_MACOS/blob/HEAD/README.md)
