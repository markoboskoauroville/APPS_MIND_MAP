# Maha Transcribe Flask

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Flask app in an Avid-style look: record or upload audio, transcribe live, read text aloud with word highlighting, keep notes with quotas; one shared login.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_FLASK](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_FLASK) |
| Also called | Maha Transcribe Flask, Maha Transcribe |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Linux, Web, Cloud |
| Language | Python (Flask), JavaScript |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Record in the browser with live VU meters and transcribe in pieces while recording
- Transcribe uploaded files in Croatian, English or auto
- Read pasted text aloud with the voice following each sentence language
- Keep notes with search, edit and undo delete
- Store audio as small mono AAC with storage quotas
- Save a reading as one audio file

## Ask for it when

- dictate and get text in Croatian
- read my text aloud with highlighted words
- keep transcripts as notes

## How to control it

- Level: **http**
- Type: http
- Port: 8700 (behind /flask/)

Actions:

- `POST /api/recordings`
- `POST /api/recordings/<id>/transcribe`
- `POST /api/recordings/assemble`
- `POST /api/live`
- `POST /api/speak`
- `POST /api/read/plan`
- `POST /api/read/save`

**Before you call:** Runs behind a login on a server (port 8700 behind the path /flask/); the shared login of the one-login-for-all-apps setup is needed, base is the hosted address (not published here).

Example:

```
curl -s -XPOST <base>/flask/api/recordings/<id>/transcribe -H 'Content-Type: application/json' -d '{"language":"hr"}'
```

More calls:

- read text aloud with word highlighting: get the plan: `curl -s -XPOST <base>/flask/api/read/plan -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}'`
- speak a text: `curl -s -XPOST <base>/flask/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}'`

Evidence: HANDOVER.md

## Inputs / Outputs

Inputs:

- microphone
- audio files

Outputs:

- notes
- m4a recordings
- speech audio

## Works with

- Uses: [TTT Portal](TTT_PORTAL.md)

## Code worth reusing

- `static/reader.js`: sentence and word highlighting player
- `ttt_auth.py`: shared-login cookie check copied from the portal

## Notes

Successor of the Streamlit version; part of the one-login-for-all-apps architecture. Request bodies of /api/read/plan and /api/speak are not in the harvested docs; only the route names.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
