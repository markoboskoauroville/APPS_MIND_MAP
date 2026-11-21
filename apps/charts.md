# Charts

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Turns a BeatStats chart PDF into a Spotify playlist, reading the pages with Gemini and searching Spotify.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/charts](https://github.com/markoboskoauroville/charts) |
| Also called | beatstats charts, charts to Spotify |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-10-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Read each page of a BeatStats chart PDF (rank, artist, title, genre) with Gemini Flash
- Search Spotify for each row and fall back to Gemini with Google Search
- Create a Spotify playlist with a report of added and skipped tracks

## Ask for it when

- make a Spotify playlist from a chart PDF
- import BeatStats chart into Spotify
- turn a top-100 PDF into a playlist

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `charts (interactive, key 'o' starts)`

**Before you call:** Installed command; no arguments needed.

Example:

```
charts # interactive chart viewer; press o to start
```

Evidence: README.md; single file 'charts'

## Inputs / Outputs

Inputs:

- BeatStats chart PDF

Outputs:

- Spotify playlist
- report

## Code worth reusing

- `charts`: PDF page OCR via Gemini plus Spotify track matching with Google-Search fallback

## Notes

Single Python file installed to /usr/local/bin/charts. API keys are kept next to the PDFs, not in the repo. The DJ Mantra Android app is getting a BeatStats view built on the same idea.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
