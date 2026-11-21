# Maha Transcribe Termux v1 (superseded) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Maha Transcribe (Termux/terminal)](MAHA_TRANSCRIBE_TERMUX_TERMINAL.md). Replaced by MAHA_TRANSCRIBE_TERMUX_TERMINAL.

**One-file Termux installer for a store-first voice transcription app: Flask + Waitress + SQLite, terminal dashboard, multi-provider keys.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_TERMUX](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_TERMUX) |
| Also called | Maha Transcribe Termux, transcribe (command) |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android, Termux |
| Language | Shell (embedded Python/Flask) |
| Status | retired |
| Last push | 2026-08-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Record audio, commit it to disk and SQLite before transcribing
- Retry transcription with backoff after network loss
- Manage, test and default provider keys
- Export recordings and run AI text actions
- Show a live terminal dashboard with one-key commands

## Ask for it when

- transcribe voice on the phone in Termux
- speech to text that never loses audio
- run a local transcription server on Android

## How to control it

- Level: **http**
- Type: http, cli
- Port: not stated in the docs (a Flask server on the phone)

Actions:

- `GET /api/state`
- `GET /api/online`
- `POST /api/keys/add`
- `POST /api/keys/import`
- `POST /api/keys/<kid>/test`
- `POST /api/keys/testall`
- `POST /api/keys/<kid>/default`
- `POST /api/keys/<kid>/delete`
- `GET/POST /api/models/<provider>`
- `GET/POST /api/settings`
- `GET/POST /api/recordings`
- `GET /api/recordings/<rid>`
- `GET /api/recordings/<rid>/audio`
- `POST /api/recordings/<rid>/transcribe`
- `POST /api/recordings/<rid>/text`
- `POST /api/recordings/<rid>/rename`
- `POST /api/recordings/<rid>/delete`
- `GET /api/recordings/<rid>/export`
- `POST /api/ai`

**Before you call:** Early Termux version (Aug 2026), superseded by MAHA_TRANSCRIBE_TERMUX_TERMINAL: use that one. The routes are the web UI's own backend, not an API for other programs.

Example:

```
curl -s -XPOST http://127.0.0.1:<port>/api/recordings/<rid>/transcribe # UI backend route; <port> is not stated in the docs
```

Evidence: 1-maha-transcribe-v1-termux.sh lines 993-1143 and following (Flask routes)

## Inputs / Outputs

Inputs:

- microphone audio via browser
- key files

Outputs:

- transcripts
- SQLite database

## Hardware

- phone microphone

## Code worth reusing

- `1-maha-transcribe-v1-termux.sh`: store-first recording queue with SQLite WAL and Waitress in Termux

## Notes

Early version (Aug 2026); superseded by MAHA_TRANSCRIBE_TERMUX_TERMINAL. Routes are the web UI backend, port not stated in what was read. RETIRED/SUPERSEDED: use MAHA_TRANSCRIBE_TERMUX_TERMINAL instead.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_TERMUX/blob/HEAD/README.md)
