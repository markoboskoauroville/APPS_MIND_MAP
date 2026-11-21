# Pianoverse Demo Songs by Mantra

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Scripts that build an Ableton Live set of 108 classical piano pieces, one minute each, from MIDI performances.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/PIANOVERSE_DEMO_SONGS](https://github.com/markoboskoauroville/PIANOVERSE_DEMO_SONGS) |
| Visibility | private (code not readable without access) |
| Kind | experiment |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-10-22 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Pick 108 pieces from a MIDI performance dataset by a wish list
- Take each first minute and fold sustain pedal into note lengths
- Write clips into the running Live over AbletonOSC and colour them
- Build a second track that plays through Pianoverse inside Live

## Ask for it when

- build a long Ableton arrangement from MIDI files
- stitch piano demos one after another

## How to control it

- Level: **cli**
- Type: python-module

Actions:

- `choose.py`
- `build.py`
- `build.py inside`

**Before you call:** Run in the repo folder.

Example:

```
python3 choose.py && python3 build.py # picks the songs, then builds the demo pages
```

More calls:

- build the inside page: `python3 build.py inside`

Evidence: README.md Rebuild line

## Inputs / Outputs

Inputs:

- MAESTRO MIDI dataset

Outputs:

- Ableton Live set with 108 clips

## Hardware

- IK Multimedia Pianoverse
- IAC Driver

## Code worth reusing

- `build.py`: write MIDI clips and colours into a running Live set over AbletonOSC in batches of 100 notes

## Notes

Done on 22.10.2026. Needs the AbletonOSC remote script with Mantra handlers (from ABLETON_LIVE_ACTIONS). UDP holds about 9 KB so notes go 100 at a time.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
