# 222 Transcribe

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit web app: upload or record audio/video, get a transcript with speakers, timecodes, subtitles and translation via AssemblyAI. Copy of 111 Transcribe.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/222-transcribe](https://github.com/markoboskoauroville/222-transcribe) |
| Also called | 222 TRANSCRIBE, two two two transcribe |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Transcribe uploaded audio or video files up to 2000 MB
- Record in the browser and transcribe on stop
- Detect speakers and give timecodes
- Export subtitles
- Translate transcripts and read them aloud (TTS)
- Fetch a file from a link (Dropbox, Drive, WeTransfer, any URL)
- Rotate through several AssemblyAI keys when one runs out

## Ask for it when

- transcribe this interview with speakers
- get subtitles for a video file
- transcribe a recording from my phone
- make a transcript from a shared link

## How to control it

No control API found.

Evidence: none found (Streamlit UI only; api.txt only shows an outbound translation call in app.py)

## Inputs / Outputs

Inputs:

- audio/video files
- links to files
- browser microphone

Outputs:

- transcript text
- subtitles
- translation

## Works with

- Uses: [111 Transcribe](111-transcribe.md)

## Code worth reusing

- `transcribe_engine.py`: AssemblyAI transcription engine with key ring failover

## Notes

Copy of 111-transcribe made for a second user; fixes in one are not in the other until copied. Gated by a username secret only.

## Docs in the repo

- `README.md`
- `LESSONS.md`
