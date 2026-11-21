# 111 Transcribe

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit web app: upload audio or video, get a transcript with speakers, timecodes, subtitles and translation through AssemblyAI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/111-transcribe](https://github.com/markoboskoauroville/111-transcribe) |
| Also called | 111 TRANSCRIBE, one eleven transcribe, Mantra Productions transcribe |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Transcribe uploaded audio or video files up to 2000 MB
- Label speakers and add timecodes
- Export subtitles
- Translate the transcript
- Record in the browser and transcribe on stop
- Accept a link (Dropbox, Drive, WeTransfer, any URL) instead of an upload
- Rotate through several AssemblyAI keys when one is refused or out of credit

## Ask for it when

- transcribe a long interview with speakers
- make subtitles from a video
- upload a file and get text
- translate a transcript

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- audio or video file
- URL to a file
- browser microphone

Outputs:

- transcript text with speakers and timecodes
- subtitle files
- translation

## Works with

- Used by or talked to by: [222 Transcribe](222-transcribe.md)

## Code worth reusing

- `transcribe_engine.py`: AssemblyAI transcription engine with multi-key fallback and ffmpeg handling, usable outside Streamlit

## Notes

Runs on Streamlit Cloud, not on a local port. Gate is a single secret USERNAME in Streamlit secrets; AssemblyAI credit is spent on every upload. Look is borrowed from Maha Transcribe (MAHA_TRANSCRIBE_STREAMLIT). No control API.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/111-transcribe/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/111-transcribe/blob/HEAD/LESSONS.md)
