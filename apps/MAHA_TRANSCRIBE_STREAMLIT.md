# Maha Transcribe / TTT-LLL (Streamlit)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit web app: record in the browser, ffmpeg downsample, Whisper on Groq to text (EN/HR), plus Talk tab that reads text aloud sentence by sentence.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_STREAMLIT](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_STREAMLIT) |
| Also called | TTT-LLL, Talk To Type, TTT LLL, Maha Transcribe Streamlit, ttt-lll.streamlit.app |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: claude-code-7-9-2026 |
| Control level | http (own http routes) |

## What it can do

- Record in the browser and transcribe with Groq whisper-large-v3-turbo
- Re-run the same audio with whisper-large-v3 (Correct)
- Read text aloud sentence by sentence (Talk, LLL: Look Listen Learn)
- Rotate between several Groq keys on rate limit
- Save per-user settings in session, browser localStorage and profile
- Serve /healthz for monitoring

## Ask for it when

- transcribe my voice in the browser
- dictate in Croatian or English
- read text aloud and show it
- speech to text with Groq Whisper

## How to control it

- Level: **http**
- Type: http
- Port: 8810 (local run; hosted on Streamlit Cloud with no port)

**Warning:** port 8810 is also quoted for [Maha Transcribe VM (TTT-LLL)](MAHA_TRANSCRIBE_VM.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /healthz`

**Before you call:** No control API: GET /healthz only says the process is up (the handover says it does not prove the app works).

Example:

```
Open the Streamlit page, record in the browser, choose language en or hr, press transcribe # no HTTP call: only GET /healthz exists
```

More calls:

- is it up: `curl -s 127.0.0.1:8810/healthz`

Evidence: HANDOVER.md lines 2329-2331; no app-control API

## Inputs / Outputs

Inputs:

- browser microphone audio

Outputs:

- transcript text
- spoken audio

## Hardware

- microphone

## Works with

- Used by or talked to by: [Sample Player, Android](SAMPLE_PLAYER.md), [TTT Portal](TTT_PORTAL.md)

## Code worth reusing

- `app.py`: record, ffmpeg 16 kHz mono FLAC prep, Groq Whisper call with key rotation
- `cassette_frontend/index.html`: cassette-style frontend component
- `ls_bridge.py`: Streamlit localStorage bridge via declare_component

## Notes

Only has /healthz (which the handover says does not prove the app is alive). Huge HANDOVER.md with standing rules, including a 'wrong chat' rule. Live on Streamlit Cloud. Many delivery records in handoff/.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_STREAMLIT/blob/HEAD/README.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_STREAMLIT/blob/HEAD/HANDOVER.md)
