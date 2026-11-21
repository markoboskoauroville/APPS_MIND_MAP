# DJ Transfer Monitor (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Small read-only Mac window that shows the live progress of a djay playlist transfer to the phone: file, bars, speed, ETA, skipped files and last error.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DJ_TRANSFER_MONITOR](https://github.com/markoboskoauroville/DJ_TRANSFER_MONITOR) |
| Also called | DJ Transfer Monitor |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Read the sync progress file once a second
- Show playlist, file, from and to paths, file and total progress
- Show speed, ETA, files done and skipped, and the last error
- Float on top via a TOP switch

## Ask for it when

- watch the DJ transfer to the phone
- see how long the playlist copy will take

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "dj transfer" "top"
```

More calls:

- list the controls of the window: `star read "dj transfer"`
- start the app in the background: `star open "dj transfer"`
- quit it: `star quit "dj transfer"`

Evidence: TAKEOVER.md: accessibility buttons off, top, close

## Inputs / Outputs

Inputs:

- djay-sync progress.json

## Works with

- Uses: [djay Sync (Mantra), Mac window](DJING_SYNC.md), [djay Sync, command line (djay-sync)](djay-playlists.md)
- Used by or talked to by: [djay Sync (Mantra), Mac window](DJING_SYNC.md), [djay Sync, command line (djay-sync)](djay-playlists.md)

## Notes

Read-only: it only watches, the transfer belongs to djay-sync.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
