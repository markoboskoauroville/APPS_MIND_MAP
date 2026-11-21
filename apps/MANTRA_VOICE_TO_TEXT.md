# Vox to Txt (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac and Windows dictation app: press F1, talk, press F1, and the words are typed at the cursor. Many engines, Whisper offline, corrections, file transcription,**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_VOICE_TO_TEXT](https://github.com/markoboskoauroville/MANTRA_VOICE_TO_TEXT) |
| Also called | Vox to Txt, Voice to Text (Mantra), Mantra Voice to Text, Transcribe Voice to Text RT, MARKO_TRANSCRIBE, F1 dictation, mantra-voice-to-text |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Windows |
| Language | Swift (Mac), C# .NET (Windows) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Dictate with F1 into any app, typing the text at the cursor
- Run Whisper Turbo locally (whisper.cpp with Metal) offline; pick other cloud engines from one menu
- Retry network errors every 3 s and rotate to the next key of the same provider (never auto-switch engine)
- Transcribe audio files with progress and segments
- Apply Croatian and English corrections and names from the shared TTT database
- Optional Anthropic auto-correct and STYLE button
- Duck the speakers to 6 % while recording
- Show a live spectrum ellipse and a menu-bar recording timer
- Serve a loopback API for other apps (Talk Mode uses /hear)

## Ask for it when

- dictate into any Mac app with a hotkey
- transcribe an audio file
- speech to text in Croatian and English
- get text from a WAV through a local call
- dictate text anywhere on the Mac
- clean up dictated text

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8865

Actions:

- `GET /status`
- `GET /engines`
- `POST /transcribe {path, engine?, language?}`
- `GET /job/<id>`
- `POST /hear?lang=en|hr|auto (WAV body)`
- `CLI: --transcribe-file <path> [engine id] [en|hr|auto]`

**Before you call:** Vox to Txt (Mantra) must be running (menu-bar app; its door answers only for host 127.0.0.1). Dictation itself is the F1 key: press F1, talk, press F1, the words are typed at the cursor.

Example:

```
curl -s -XPOST '127.0.0.1:8865/hear?lang=en' --data-binary @take.wav
```

More calls:

- transcribe a file and poll the job: `curl -s -XPOST 127.0.0.1:8865/transcribe -H 'Content-Type: application/json' -d '{"path":"~/take.wav","language":"hr"}' # then: curl -s 127.0.0.1:8865/job/<id>`
- list the engines: `curl -s 127.0.0.1:8865/engines`
- Croatian audio file straight to text: `curl -s -XPOST '127.0.0.1:8865/hear?lang=hr' --data-binary @take.wav`
- status: `curl -s 127.0.0.1:8865/status`

Evidence: TAKEOVER.md line 78 (FileAPI, 127.0.0.1:8865 only), line 79 (CLI)

## Inputs / Outputs

Inputs:

- microphone
- audio files

Outputs:

- typed text at cursor
- transcripts and segments
- history

## Hardware

- microphone

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Talks to: [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md), [Talk Mode (Mantra)](TALK_MODE.md)
- Used by or talked to by: [Mantra Corrections](MANTRA_CORRECTIONS.md), [Startup (Mantra)](Startup-Mantra.md)

## Code worth reusing

- `mac/Sources/Corrections.swift`: TTT dictate/NLP corrections in Swift (Croatian fixes, names)
- `mac/Sources/Engines.swift`: transcription engine abstraction over several providers
- `mac/Sources/Chain.swift`: key ring and retry logic
- `mac/Resources/dict/`: EN and HR dictionaries, bigrams, trigrams

## Notes

Renamed from Voice to Text (Mantra) at v39; bundle id, data folder, port and repo unchanged. Public downloads on release repo mantra-voice-to-text-downloads and site mantravoicetotext.pages.dev. Host must be 127.0.0.1 or request refused. Latest in docs is v62 (tag list truncated). Language values: en, hr or auto. The command-line form --transcribe-file `<path>` [engine id] [en|hr|auto] exists but the binary path inside the app bundle is not in the harvested docs.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_VOICE_TO_TEXT/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_VOICE_TO_TEXT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_VOICE_TO_TEXT/blob/HEAD/LESSONS.md)
