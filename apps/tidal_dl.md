# Tidal DL

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Terminal tool (Mac Apple Silicon and Termux) that downloads TIDAL albums, tracks, playlists and artists with streamrip and checks FLAC with ffprobe.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/tidal_dl](https://github.com/markoboskoauroville/tidal_dl) |
| Also called | tidaldl, Tidal downloader, TIDAL DL |
| Visibility | public |
| Kind | cli-tool |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Termux |
| Language | Python (shell installers) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Download a TIDAL link (album, track, playlist, artist) through streamrip
- Stage requested FLAC and verify with ffprobe, saving nothing if TIDAL served AAC
- Log in once from the menu (key a) and update in-app (key u)
- Install by one line for macOS or Termux from generated installers
- Run 30 checks and gates (tests/run_all.py, gates/run_gates.py)

## Ask for it when

- download a TIDAL playlist as FLAC
- save my TIDAL album offline on the Mac
- TIDAL downloader on the phone

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `tidaldl (menu)`
- `tidaldl <tidal-url>`

**Before you call:** Log in to TIDAL once (the menu: run tidaldl with no argument). Real login and download still had to be tested by the owner at v22.

Example:

```
tidaldl https://tidal.com/playlist/<playlist-id> # downloads a playlist; album and track URLs work the same way
```

More calls:

- an album: `tidaldl https://tidal.com/album/12345`
- open the menu (login, quality, folders): `tidaldl`

Evidence: TAKEOVER.md (former README), tidaldl.py

## Inputs / Outputs

Inputs:

- TIDAL links
- TIDAL login

Outputs:

- audio files (FLAC) in the music folder

## Code worth reusing

- `tools/build_installers.py`: Generates macOS and Termux installers from one source plus .sh.in templates
- `gates/run_gates.py`: Release gates that must pass before shipping

## Notes

State 8.10.2026: v22 built and tested, real TIDAL login and download still to be tested by Marko. Uses streamrip, which djmantra_app's rule 'no reverse-engineered service APIs' applies against for the DJ app, not for this tool. api.txt shows nothing; CLI only.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/tidal_dl/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/tidal_dl/blob/HEAD/LESSONS.md)
