# djay Sync (Mantra), Mac window

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Swift Mac window (djay Sync (Mantra)) that syncs djay Pro playlists to the DJ phone app and pulls phone ones back as .m3u8; logic is in djay-playlists.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DJING_SYNC](https://github.com/markoboskoauroville/DJING_SYNC) |
| Also called | djay Sync, DJ sync |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Android |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | none (no control api found) |

## What it can do

- Compare djay Pro playlists on the Mac with the phone (same, new, changed)
- Copy only missing songs to the phone with progress, speed and ETA
- Pull phone playlists to the Mac as .m3u8 for import into djay
- Auto-sync when the phone appears on adb (optional)
- Never write djay's database; removed playlists move to a _removed folder

## Ask for it when

- sync my DJ playlists to the phone
- copy djay playlists to Android
- pull playlists from the phone into djay

## How to control it

No control API found.

Evidence: none found; app runs djay-sync CLI from DJAY_PLAYLISTS

## Inputs / Outputs

Inputs:

- djay Pro playlists
- phone over adb

Outputs:

- files on phone
- .m3u8 playlists
- progress.json

## Hardware

- Android phone over adb

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [djay Sync, command line (djay-sync)](djay-playlists.md)
- Talks to: [DJ Transfer Monitor (Mantra)](DJ_TRANSFER_MONITOR.md)
- Used by or talked to by: [DJ Transfer Monitor (Mantra)](DJ_TRANSFER_MONITOR.md), [djay Sync, command line (djay-sync)](djay-playlists.md)

## Notes

Start only from the star. The actual sync logic lives in the DJAY_PLAYLISTS repo.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
