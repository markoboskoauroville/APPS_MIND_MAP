# Screenshot to TIDAL (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Reads a chart or tracklist screenshot with on-device OCR and builds a TIDAL playlist; also copies djay Pro playlists to TIDAL.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SCREENSHOT_TO_TIDAL](https://github.com/markoboskoauroville/SCREENSHOT_TO_TIDAL) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v3 |
| Control level | cli (command line or script only) |

## What it can do

- OCR screenshots with Apple Vision and parse ranks, titles and artists
- Search TIDAL by ISRC or artist and title with confidence scoring
- Create unlisted playlists or add only missing songs
- Convert every djay Pro playlist to a TIDAL playlist of the same name
- List own TIDAL playlists

## Ask for it when

- turn a chart screenshot into a TIDAL playlist
- copy my djay playlists to TIDAL

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `--test`
- `--tidal-login`
- `--sync-playlists`
- `--list-playlists`
- `--shot`
- `off`
- `top`
- `close`

**Before you call:** Needs a TIDAL developer app key file chosen by the user; log in once with --tidal-login. Binary name inside the bundle is not in the harvested docs.

Example:

```
"Screenshot to TIDAL (Mantra).app/Contents/MacOS/<binary>" --list-playlists
```

More calls:

- sync playlists: `... --sync-playlists`
- test: `... --test`

Evidence: TAKEOVER.md (code table: app/App.swift) and v5 note on AX ids

## Inputs / Outputs

Inputs:

- screenshots
- djay playlists.json or m3u8

Outputs:

- TIDAL playlists
- match cache

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)
- Used by or talked to by: [Generated Playlists](generated_playlists.md)

## Code worth reusing

- `app/OCR.swift`: Vision OCR for ranked lists with noise filters
- `app/Tidal.swift`: TIDAL PKCE login, search, scoring, playlists
- `app/PlaylistSync.swift`: read djay playlists and tags, match and sync

## Notes

Needs a TIDAL developer app key file chosen by the user; token in the login keychain. Some GUI buttons not yet proven by hand at last note.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
