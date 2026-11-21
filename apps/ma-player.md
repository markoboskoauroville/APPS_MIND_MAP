# MA Player

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Terminal music player for Termux with a browser front end and a downloader for TIDAL and YouTube, driving mpv.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ma-player](https://github.com/markoboskoauroville/ma-player) |
| Also called | maplay, maplayer, maplayerweb, matidal, MA Player WEB |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | Android, Termux |
| Language | Python (scripts) |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Play playlist CSVs and audio in a terminal player
- Serve the same library as a dark web UI on the LAN
- Drive mpv over an IPC socket so either front end controls the same playback
- Take one-word commands from outside (toggle, next, prev, quit)
- Download from TIDAL (streamrip) and YouTube (yt-dlp)

## Ask for it when

- play music on the phone from the terminal
- control music playback from a browser on the Wi-Fi
- download a track from YouTube or TIDAL on the phone

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8084

Actions:

- `maplay`
- `maplayerweb`
- `matidal`
- `maplay-cmd toggle|next|prev|quit`

**Before you call:** Starts with maplay (page player), maplayerweb or matidal on 8084; maplay-cmd sends it commands.

Example:

```
maplay-cmd next
```

More calls:

- play or pause: `maplay-cmd toggle`
- previous: `maplay-cmd prev`

Evidence: README.md; bin/maplay-cmd

## Inputs / Outputs

Inputs:

- playlist CSVs
- audio files

Outputs:

- audio playback
- downloaded tracks

## Hardware

- Android phone

## Code worth reusing

- `bin/maweb-engine`: serves a folder of music as a web player controlling mpv over IPC
- `bin/maplay-cmd`: drops one-word commands to a running player

## Notes

No build or source folder: the bin files are the program, installed to $PREFIX/bin. Streaming is free preview quality only. Web edition listens on all interfaces.

## Docs in the repo

- `README.md`
