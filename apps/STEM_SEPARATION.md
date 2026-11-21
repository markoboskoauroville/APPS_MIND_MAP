# Stem Separation (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that has Ableton Live 12 split a song into vocal, bass, drums and other stems, collects the files and analyses each stem.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STEM_SEPARATION](https://github.com/markoboskoauroville/STEM_SEPARATION) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Load a song into Live through AbletonOSC
- Trigger Live's Separate Stems command via Accessibility
- Collect the four stem files into a per-song folder
- Analyse each stem into waveform and level per second

## Ask for it when

- separate a song into stems
- make stems for a DJ site player

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- song file

Outputs:

- vocals bass drums others wav
- stems.json

## Works with

- Uses: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md)

## Code worth reusing

- `app/Separator.swift`: step sequence for stem separation inside Live

## Notes

Needs Live 12.3+ Suite. Not yet run as the app at last note (Accessibility permission pending); steps proven by hand. Added two handlers to the AbletonOSC remote script, not upstreamed.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
