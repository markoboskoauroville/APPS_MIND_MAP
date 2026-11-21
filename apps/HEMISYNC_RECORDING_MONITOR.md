# Hemi-Sync Recording Monitor (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Dashboard window for the long Hemi-Sync recording job: phase, clip and album bars, current track, time left and a silent-recorder warning.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/HEMISYNC_RECORDING_MONITOR](https://github.com/markoboskoauroville/HEMISYNC_RECORDING_MONITOR) |
| Also called | Hemi-Sync Recording Monitor, hemisync monitor |
| Visibility | public |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | none (no control api found) |

## What it can do

- Read ~/Music/HemiSync/progress.json every 2 s
- Show phase, state, clips and albums progress, current album and track, time left, finish time and elapsed
- Warn amber with Recorder silent? after 2 minutes without an update
- Open the folder in Finder

## Ask for it when

- how far is the Hemi-Sync recording
- monitor the long recording job
- when will the recording finish

## How to control it

No control API found.

Evidence: none found; reads a progress file

## Inputs / Outputs

Inputs:

- ~/Music/HemiSync/progress.json (HEMISYNC_PROGRESS env overrides for tests)

Outputs:

- window view only

## Code worth reusing

- `app/Updater.swift`: mac-updater kit that asks at start for a newer GitHub release
- `check_one_title.sh`: guard that the window has one title only

## Notes

Status v1, 21.11.2026. Monitor only: it does not record. The worker that records the albums is not in this repo. Coded by MAI Code 2 on a first draft by Claude Code. The Hemi-Sync name is the title of the audio programmes being recorded.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/HEMISYNC_RECORDING_MONITOR/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/HEMISYNC_RECORDING_MONITOR/blob/HEAD/LESSONS.md)
