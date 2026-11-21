# Maha Transcribe (Termux/terminal)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Runs the Maha Transcribe HTML page from a small Flask server on Termux, macOS or Linux, as one shell command 'transcribe', with port fallback.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_TERMUX_TERMINAL](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_TERMUX_TERMINAL) |
| Also called | transcribe, Maha Transcribe terminal |
| Visibility | public |
| Kind | cli-tool |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android, Termux, Linux |
| Language | Python (Flask) + HTML |
| Status | active |
| Last push | 2026-10-05 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Serve maha_transcribe.html over 127.0.0.1 so the browser allows the microphone
- Start on the default port or a chosen one (transcribe 9000)
- Optimise audio with ffmpeg through /api/optimize-audio
- Show a live terminal dashboard with keypress commands
- Self-update (transcribe-update)

## Ask for it when

- use Maha Transcribe from the terminal
- start the dictation page locally
- microphone page on Termux
- optimise audio before upload
- transcribe voice on the phone in Termux
- run a local transcription server on Android

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8420 default, auto fallback

Actions:

- `GET /api/ffmpeg`
- `POST /api/optimize-audio`
- `GET /api/version`
- `GET /api/update/check`
- `POST /api/update`
- `CLI: transcribe [port]`
- `CLI: transcribe-update`

**Before you call:** Install once (one shell command per the README) in Termux, macOS or Linux; the command prints and opens the port it got.

Example:

```
transcribe 9000 # starts the page on port 9000 (default 8420, next free port if taken) and opens it in Chrome
```

More calls:

- update the installed page: `transcribe-update`
- is ffmpeg available: `curl -s 127.0.0.1:8420/api/ffmpeg`
- version, and check for an update: `curl -s 127.0.0.1:8420/api/version ; curl -s 127.0.0.1:8420/api/update/check`

Evidence: app.py lines 80-139; README.md Usage

## Inputs / Outputs

Inputs:

- browser microphone audio

Outputs:

- transcripts in the page
- optimised audio

## Hardware

- microphone

## Works with

- Used by or talked to by: [Keyring](KEYRING_TERMUX.md)

## Code worth reusing

- `portpick.py`: never-fail port picker
- `localguard.py`: local-only request guard for /api POSTs
- `selfupdate.py`: git-pull self-update
- `console.py`: terminal dashboard
- `audioprep.py`: ffmpeg audio optimisation

## Notes

Pattern source copied into KEYRING_TERMUX. Same house pattern as GDRIVE_DOWNLOADER_FLASK_MACOS.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_TERMUX_TERMINAL/blob/HEAD/README.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_TERMUX_TERMINAL/blob/HEAD/LESSONS.md)
