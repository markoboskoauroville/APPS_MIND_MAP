# Marko Transcribe (Streamlit)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit web transcriber that sends audio to AssemblyAI with a rotating ring of keys, ffmpeg handling and results logged to Google Sheets (v3.16).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/marko-transcribe](https://github.com/markoboskoauroville/marko-transcribe) |
| Also called | Maha Transcribe Streamlit, AssemblyAI transcriber |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | dormant |
| Last push | 2026-09-17 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Transcribe uploaded audio with AssemblyAI, retrying across a ring of keys with verdict handling
- Use ffmpeg for audio preparation
- Log or fetch data through Google Sheets (gspread)
- Show the app version badge top corner

## Ask for it when

- transcribe a long audio file online
- web transcription app with AssemblyAI

## How to control it

No control API found.

Evidence: app.py, transcribe_engine.py; only Streamlit UI found

## Inputs / Outputs

Inputs:

- audio files

Outputs:

- transcripts

## Code worth reusing

- `transcribe_engine.py`: AssemblyAI upload/poll engine with key ring, retry and verdict logic

## Notes

No README; described from source headers only (APP_VERSION v3.16, Sept 2026). Keys come from Streamlit secrets and are not in the repo.

_Low confidence: little was documented in this repository. Check the code before relying on this card._
