# YT Transcriber

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Turns a YouTube channel, playlist or video URL into one transcript file, one video at a time via Groq Whisper, with an optional knowledge summary.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/YT_TRANSCRIBER](https://github.com/markoboskoauroville/YT_TRANSCRIBER) |
| Also called | YouTube transcriber |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Linux, Cloud |
| Language | Python / Shell |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Download lowest-bitrate audio and transcribe with Groq Whisper with fallbacks
- Rotate keys on rate limits and resume from saved state
- Write per-video txt and srt and a merged transcript
- Make a per-video knowledge note and merge them by topic
- Show a status monitor page and rotate cookie accounts when blocked

## Ask for it when

- transcribe a whole YouTube channel
- get all transcripts of a playlist
- summarise a channel into topics

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8851

**Warning:** port 8851 is also quoted for [Star Monitor (Mantra)](STAR_MONITOR.md) - confirm with `mantra-ports scan`.

Actions:

- `download_channel.sh <url> [name] [--limit N --client ... --audio-dir DIR]`
- `GET /api/status`
- `python3 cookie_sync.py watch|once`

Example:

```
./download_channel.sh https://www.youtube.com/@channel mychannel --limit 20 # downloads audio of the last 20 videos of a channel
```

More calls:

- status of the local helper: `curl -s 127.0.0.1:8851/api/status`
- keep the cookies fresh: `python3 cookie_sync.py watch`

Evidence: README.md and monitor.py (route /api/status)

## Inputs / Outputs

Inputs:

- YouTube URL

Outputs:

- ALL_TRANSCRIPTS.txt
- per-video txt srt
- KNOWLEDGE.md

## Code worth reusing

- `yt_transcribe.py`: one-at-a-time download, transcribe, knowledge pass with resume
- `cookie_sync.py`: export allowed browser-profile cookies to the server on a schedule

## Notes

Runs as systemd user services on a cloud VM; monitor listens on the tailnet address only. Cookie and key files are never committed; some accounts are protected and never used.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
