# Suno Songs prompt database

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Tagged database of reusable Suno style and lyrics prompts with a menu script and a Chromium extension that drives suno.com from a local CLI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SUNO_SONGS](https://github.com/markoboskoauroville/SUNO_SONGS) |
| Also called | Suno prompts, sunoctl |
| Visibility | private (code not readable without access) |
| Kind | content-book-guide |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Chrome |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: archive/ccr-dc3c1da5-aadsaj |
| Control level | http (own http routes) |

## What it can do

- Keep one file per reusable style with tags and measured numbers
- Print a menu of styles filtered by tag
- Measure a source track (tempo, key) in one command
- Check the repo against the song-making rules
- Drive suno.com in the background through a local extension bridge
- Read clip data through Suno's own web API and follow a remix procedure

## Ask for it when

- make a song in a given style
- pick a Suno style by tag
- generate a Suno song from the command line
- measure the tempo and key of a reference

## How to control it

- Level: **http**
- Type: cli, http
- Port: 47615-47630

Actions:

- `scripts/sunoctl.py serve`
- `scripts/sunoctl.py api`
- `scripts/menu.py`
- `scripts/measure.py`
- `scripts/check.py`

**Before you call:** sunoctl serve runs the helper door on 47615 (up to 47630).

Example:

```
python3 scripts/sunoctl.py api '{"url":"/api/clip/ID"}'
```

More calls:

- start the helper: `python3 scripts/sunoctl.py serve`
- menu: `python3 scripts/menu.py`

Evidence: scripts/sunoctl.py and extensions/suno_controller/background.js (long-polls a local bridge)

## Inputs / Outputs

Inputs:

- reference audio
- style prompts

Outputs:

- style files
- INDEX.md menu
- Suno generations

## Works with

- Talks to: [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md)
- Used by or talked to by: [Song Simple Mixer](Song_simple_mixer.md)

## Code worth reusing

- `extensions/suno_controller`: local Chromium extension plus bridge to drive suno.com
- `scripts/measure.py`: measure tempo, key and bar sections of a track
- `scripts/menu.py`: tag-filtered style menu

## Notes

Large repo (many remix parts and audio). Suno may ask for a captcha after about ten generations; a Create counts only when a new clip id returns. Method rules live in the manifest module suno-song. Verb list of sunoctl.py was only partly visible (serve, api confirmed).

## Docs in the repo

- `README.md`
