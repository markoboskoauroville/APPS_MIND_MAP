# Google TTS and STT (gtt)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One local app for Gemini text-to-speech and speech-to-text on one shared free-tier key ring: thirty voices, two speakers, transcription, key tests.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GOOGLE_TTS_STT](https://github.com/markoboskoauroville/GOOGLE_TTS_STT) |
| Also called | gtt, gtts, MA Reader, Maha Transcribe (Gemini side), Google TTS and STT |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android, Termux, Web |
| Language | Shell installer, Python (Flask), HTML |
| Status | dormant |
| Last push | 2026-09-19 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Speak: text in, audio out with thirty Gemini voices and plain-English direction, two speakers in one pass
- Listen: audio in, text out (Maha Transcribe side)
- Test every key, measure limits and show remaining budget
- Import keys from any file format (txt, env, JSON, CSV, markdown)
- Chunk long jobs and resume them
- Optimise audio with ffmpeg

## Ask for it when

- read text aloud with Gemini voices
- transcribe audio with Gemini
- manage my Gemini free keys
- text to speech on the phone

## How to control it

- Level: **door**
- Type: http, cli
- Port: 7311 (MANTRA_PORTS id gtt, then +16)

Actions:

- `POST /api/speak`
- `GET /api/preview`
- `GET /api/cache`
- `GET /api/voice/<name>`
- `GET /api/voices`
- `GET /api/emotions`
- `POST /api/listen`
- `POST /api/import`
- `POST /api/rewrite`
- `GET /api/ffmpeg`
- `POST /api/optimize-audio`
- `POST /api/chunk/start`
- `GET /api/chunk`
- `GET /api/chunk/<jid>`
- `POST /api/chunk/<jid>/resume`
- `GET /api/health`
- `GET /api/keys`
- `GET /api/ring`
- `POST /api/key/<label>/test`
- `GET /api/key/<label>/models`
- `POST /api/delete`
- `GET /api/removed`
- `POST /api/restore`
- `GET /api/budget`
- `gtt`
- `gtt import <file>`
- `gtt test`
- `gtt-update`

**Before you call:** Start with the command gtt (menu and the app on localhost:7311, port 7311 or next free up to 7327). Tests make real calls and a TTS account allows about ten requests a day: run gtt test only on request.

Example:

```
curl -s -XPOST 127.0.0.1:7311/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs
```

More calls:

- list voices: `curl -s 127.0.0.1:7311/api/voices`
- health: `curl -s 127.0.0.1:7311/api/health`
- key ring state and budget: `curl -s 127.0.0.1:7311/api/ring ; curl -s 127.0.0.1:7311/api/budget`
- add keys from a file: `gtt import ~/Downloads/more-keys.txt`

Evidence: 30-google-tts-stt-v30.sh lines 2414-2569

## Inputs / Outputs

Inputs:

- text
- audio
- key files

Outputs:

- audio
- transcripts
- key ledger

## Works with

- Talks to: [GVoices (Google Voices)](GoogleVoices.md)

## Code worth reusing

- `src/10_app.py`: Flask app with Gemini TTS/STT, key ring, ledger and fallback
- `src/41_reader.py`: reader module (MA Reader)
- `src/42_voicesex.py`: voice descriptions and emotion direction
- `get.sh`: versionless installer that reads LATEST and verifies the download

## Notes

Installing spends nothing; tests make real calls and a TTS account has about ten requests a day, so run them only on request (gtt test). Single installer file 30-google-tts-stt-v30.sh embeds the source. Overlaps with GoogleVoices (gvoice), which is TTS only.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/GOOGLE_TTS_STT/blob/HEAD/README.md)
- [DEVELOPMENT.md](https://github.com/markoboskoauroville/GOOGLE_TTS_STT/blob/HEAD/DEVELOPMENT.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/GOOGLE_TTS_STT/blob/HEAD/HANDOFF.md)
