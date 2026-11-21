# Shazam Local

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Offline song and recording recognition in one Python file: landmark matching for same-recording offsets and chroma matching for songs across concerts.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SHAZAM_LOCAL](https://github.com/markoboskoauroville/SHAZAM_LOCAL) |
| Also called | shazam-local, local Shazam |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Linux |
| Language | Python |
| Status | active |
| Last push | 2026-11-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Enrol a song with landmark hashes and chroma
- Tell whether a clip is the same recording and at what offset (16 ms)
- Recognise a song at another concert with key and tempo shift
- Scan a long file for a timeline of matches
- Align two recordings of the same event

## Ask for it when

- find which song this is
- sync a camera audio track to a desk recording
- locate a clip inside a long recording

## How to control it

- Level: **cli**
- Type: cli, python-module

Actions:

- `add`
- `match`
- `song`
- `scan`
- `songscan`
- `align`
- `list`
- `remove`

**Before you call:** Run in the repo environment; 'add' builds the local fingerprint library from audio first.

Example:

```
shazam-local --json song clip.wav --dur 45
```

More calls:

- add a song to the library: `shazam-local add song.wav`
- find which song a clip is: `shazam-local match clip.wav`
- list the library: `shazam-local list`

Evidence: README.md Commands; shazam_local.py argparse

## Inputs / Outputs

Inputs:

- wav mp3 mp4 mov or HLS m3u8

Outputs:

- JSON match results
- SQLite database

## Code worth reusing

- `shazam_local.py`: whole library and CLI: landmarks, chroma, align; needs numpy scipy ffmpeg

## Notes

No network, models or keys. Database files are gitignored and rebuilt by test scripts. Landmarks never recognise a new performance of a song; chroma does but needs enrolment. Test scripts refer to specific concerts.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
