# MKV Converter (MPA)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Repacks browser-recorded lesson MKV/WebM files into Resolve-ready MOV with time code, via a Mac app and a Resolve script.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MKV_CONVERTER](https://github.com/markoboskoauroville/MKV_CONVERTER) |
| Also called | MPA Import |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Find lesson recordings in a folder
- Repack H.264 untouched into MOV with 48 kHz 24-bit PCM audio
- Encode WebM from Firefox to H.264
- Write the time code taken from the file name
- Import each lesson into its own Resolve bin lined up by time code

## Ask for it when

- make a browser MKV importable in DaVinci Resolve
- convert classroom recordings for editing

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- MKV/WebM recordings

Outputs:

- MOV files
- Resolve bins

## Code worth reusing

- `resolve/MPA Import.py`: Resolve utility script that repacks and imports into a bin by time code

## Notes

Needs ffmpeg from Homebrew. Resolve script runs under Workspace, Scripts, Utility. Long recordings not yet tested at last note.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
