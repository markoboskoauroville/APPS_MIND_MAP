# djay Sync, command line (djay-sync)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Command djay-sync copies djay Pro playlists from the Mac to the Pixel for DJ Mantra over adb, one way, differences only; its Mac window is DJING_SYNC.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/djay-playlists](https://github.com/markoboskoauroville/djay-playlists) |
| Also called | djay-sync, djay playlists |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Android |
| Language | Python, Swift |
| Status | active |
| Last push | 2026-10-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Read djay Pro playlists read-only from a copy of its library database
- Push missing or changed songs to the phone and write .m3u8 playlists
- Show a dry-run plan and per-playlist status
- Output plans and progress as JSON for a Swift front-end window
- Pull phone-only playlists back to the Mac as .m3u8
- Export playlists.json and PLAYLISTS.md
- Resolve moved files through macOS bookmarks

## Ask for it when

- sync djay playlists to my phone
- put my DJ playlists on the Pixel for DJ Mantra
- see which playlists differ between djay and the phone

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--dry-run`
- `--status`
- `--json`
- `--sync`
- `--pull`
- `--export DIR`
- `--serial S`

**Before you call:** djay Pro and the phone must be reachable for sync (see --serial).

Example:

```
djay-sync --status
```

More calls:

- what would change, without doing it: `djay-sync --dry-run`
- sync: `djay-sync --sync`
- pull from a device: `djay-sync --pull --serial S`

Evidence: README.md, djay_sync.py

## Inputs / Outputs

Inputs:

- djay Pro library database
- music files

Outputs:

- phone playlist folders and .m3u8
- progress.json

## Hardware

- Android phone over adb (Wi-Fi or USB)

## Works with

- Uses: [djay Sync (Mantra), Mac window](DJING_SYNC.md)
- Talks to: [DJ Transfer Monitor (Mantra)](DJ_TRANSFER_MONITOR.md), [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md)
- Used by or talked to by: [djay Sync (Mantra), Mac window](DJING_SYNC.md), [DJ Transfer Monitor (Mantra)](DJ_TRANSFER_MONITOR.md)

## Code worth reusing

- `djay_sync.py`: parser for djay's YapDatabase playlist storage (TSAF) and adb file push with resume
- `tools/resolve_bookmarks.swift`: resolves macOS URL bookmarks to find moved files

## Notes

One way Mac to phone. Streaming items are listed but not copied. Auto-run on phone connect was not built.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
