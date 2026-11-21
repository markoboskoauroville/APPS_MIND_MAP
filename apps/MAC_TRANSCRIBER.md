# Mac Transcriber (scribe)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Command scribe: transcribe a YouTube URL or audio file with Groq, AssemblyAI or Deepgram, chunked at silences, with key rotation and timestamps.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAC_TRANSCRIBER](https://github.com/markoboskoauroville/MAC_TRANSCRIBER) |
| Also called | scribe, Mac Transcriber |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Download audio only from a URL and register it on the Download Monitor
- Cut the audio at silences into 10-minute chunks
- Transcribe with Groq Whisper, AssemblyAI or Deepgram and rotate keys on quota or auth errors
- Resume per chunk
- Write Markdown with timestamps
- List and test the available keys (scribe keys)

## Ask for it when

- transcribe a YouTube video to text
- transcribe a long audio file with timestamps
- check which transcription keys work

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `scribe <url|file> [--name N] [--out DIR] [--engine groq|assemblyai|deepgram] [--chunk SEC] [--lang] [--prompt] [--boost]`
- `scribe keys`

**Before you call:** Needs the key of the chosen engine in the key ring (scribe keys shows them).

Example:

```
scribe <youtube-url> --engine groq --out ~/transcripts
```

More calls:

- a local file with Croatian, assemblyai: `scribe ~/Movies/talk.mov --engine assemblyai --lang hr --out ~/transcripts`
- which keys work: `scribe keys`

Evidence: README.md; scribe.py argparse

## Inputs / Outputs

Inputs:

- YouTube URL or media file

Outputs:

- timestamped Markdown transcript

## Works with

- Uses: [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md)

## Code worth reusing

- `scribe.py`: chunked transcription with engine order, key rotation and per-chunk resume

## Notes

Named scribe because transcribe is taken by another tool.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
