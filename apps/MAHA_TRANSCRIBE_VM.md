# Maha Transcribe VM (TTT-LLL)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit app on the VM: record voice, transcribe with Groq Whisper, read text aloud sentence by sentence; TTT-LLL moved off Streamlit Cloud.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAHA_TRANSCRIBE_VM](https://github.com/markoboskoauroville/MAHA_TRANSCRIBE_VM) |
| Also called | TTT-LLL, TTT LLL, Talk To Type, Look Listen Learn, MAHA_TRANSCRIBE_STREAMLIT |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Linux, Web, Cloud |
| Language | Python (Streamlit) |
| Status | active |
| Last push | 2026-09-03 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Record audio and auto-transcribe with whisper-large-v3-turbo, with a Correct re-run on large-v3
- Downsample to 16 kHz mono FLAC before upload
- Rotate through multiple Groq keys on rate limit
- Read text aloud live sentence by sentence with word timings
- Keep per-user settings (language, voice) in session, browser storage and a server file
- Offer a Google Apps Script back end for accounts

## Ask for it when

- dictate by voice into text in the browser
- read text aloud in a chosen voice
- transcribe Croatian speech

## How to control it

- Level: **http**
- Type: http
- Port: 8810 (same as the Streamlit version it was forked from)

**Warning:** port 8810 is also quoted for [Maha Transcribe / TTT-LLL (Streamlit)](MAHA_TRANSCRIBE_STREAMLIT.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /healthz`

**Before you call:** No control API: GET /healthz only says the process is up.

Example:

```
Open the page, record in the browser, press transcribe # no HTTP call: only GET /healthz exists
```

More calls:

- is it up: `curl -s 127.0.0.1:8810/healthz`

Evidence: HANDOVER.md lines 2329-2392 (health check only)

## Inputs / Outputs

Inputs:

- microphone audio

Outputs:

- transcripts
- speech

## Code worth reusing

- `ls_bridge.py`: Streamlit custom component bridging browser localStorage via postMessage

## Notes

Hard fork of MAHA_TRANSCRIBE_STREAMLIT; the HANDOVER.md is very long and holds the standing rules and version history.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
