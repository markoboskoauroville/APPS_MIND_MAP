# GVoices (Google Voices)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local page for Google's thirty prebuilt Gemini voices: a sentence in, a WAV out, archive of everything said, and a key ring manager. Command gvoice.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GoogleVoices](https://github.com/markoboskoauroville/GoogleVoices) |
| Also called | GVoices, gvoice, Google Voices |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android, Termux, Linux, Web |
| Language | Python (Flask) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Say a sentence with any of thirty Gemini voices and download the WAV
- Keep an archive of everything said
- Manage a ring of Google keys with import, test, delete, restore, move to bottom
- Show progress while a sentence is generated
- Update itself from GitHub (u key)

## Ask for it when

- text to speech with a Google voice
- make a WAV of a sentence with Gemini
- gvoice command
- pick a Gemini voice

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8300 (MANTRA_PORTS id gvoice, 8300-8315, live port in ~/.mantra/ports/gvoice)

Actions:

- `GET /api/state`
- `POST /api/settings`
- `POST /api/say`
- `GET /api/progress`
- `GET /audio/<file>`
- `DELETE /api/archive/<id>`
- `GET /api/keys`
- `POST /api/keys/import`
- `POST /api/keys/test`
- `POST /api/keys/delete`
- `POST /api/keys/restore`
- `POST /api/keys/bottom`
- `gvoice`
- `gvoice update`

**Before you call:** Start with the command gvoice (port 8300, up to 8315; the live port is in ~/.mantra/ports/gvoice). TTS only; overlaps with GOOGLE_TTS_STT.

Example:

```
curl -s -XPOST 127.0.0.1:8300/api/say -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs
```

More calls:

- state: `curl -s 127.0.0.1:8300/api/state`
- progress of a long job: `curl -s 127.0.0.1:8300/api/progress`
- update: `gvoice update`

Evidence: app.py lines 96-319; localguard.py guards POSTs

## Inputs / Outputs

Inputs:

- text
- key file

Outputs:

- WAV audio
- archive

## Works with

- Used by or talked to by: [Google TTS and STT (gtt)](GOOGLE_TTS_STT.md)

## Code worth reusing

- `ring.py`: key ring with fallback
- `localguard.py`: guard so only the local page can POST
- `portpick.py`: preferred port then next fifteen then any
- `selfupdate.py`: self-update

## Notes

35 checks green on 15.9.2026 (tests/run_all.py). Overlaps with GOOGLE_TTS_STT, which adds transcription. Keys stay in GoogleVoices/keys on the running machine.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/GoogleVoices/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/GoogleVoices/blob/HEAD/LESSONS.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/GoogleVoices/blob/HEAD/HANDOVER.md)
- [DEVELOPMENT.md](https://github.com/markoboskoauroville/GoogleVoices/blob/HEAD/DEVELOPMENT.md)
- [MEMORY.md](https://github.com/markoboskoauroville/GoogleVoices/blob/HEAD/MEMORY.md)
