# Sound Design

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Sound department workspace for a short film: a cue sheet derived from the film data, sound tools and method notes.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SOUND_DESIGN](https://github.com/markoboskoauroville/SOUND_DESIGN) |
| Visibility | private (code not readable without access) |
| Kind | experiment |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-08-19 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Derive a frame-by-frame spotting cue sheet from the film data
- Keep sound decisions across rebuilds and orphan retired frames
- Propose a soundscape per frame
- Hold notes on tools, sources and method

## Ask for it when

- rebuild the spotting sheet after the picture changes
- plan sound for a short film

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `tools/spotting.py`
- `tools/soundscape.py`

Example:

```
python3 tools/spotting.py # marks where sound is needed in a film
```

More calls:

- build a soundscape: `python3 tools/soundscape.py`

Evidence: README.md; argparse in both tools

## Inputs / Outputs

Inputs:

- film frame data json

Outputs:

- spotting.csv and spotting.md
- suggestions

## Works with

- Uses: [The Brain Brake (film repository)](BRAIN_BRAKE.md)

## Code worth reusing

- `tools/spotting.py`: build and merge a cue sheet from frame JSON, preserving manual columns

## Notes

Never edits the picture repo. Running time must never grow. Has four plus four tests.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
