# Suno Controller (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Chrome extension plus sunoctl CLI that lets Claude drive suno.com in the signed-in Chrome and record each song with Sound Recorder.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CHROME_SUNO_CONTROLLER](https://github.com/markoboskoauroville/CHROME_SUNO_CONTROLLER) |
| Also called | Chrome Suno Controller, sunoctl, Suno controller |
| Visibility | private (code not readable without access) |
| Kind | browser-extension |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Chrome |
| Language | JavaScript (extension), shell CLI |
| Status | active |
| Last push | 2026-11-10 |
| Build / release | GitHub workflow: no; latest release: v8 |
| Control level | http (own http routes) |

## What it can do

- List recent songs from the Suno feed
- Open and play or pause a song
- Record a whole song from Chrome only to a WAV through Sound Recorder
- Fill the Create form (styles, lyrics, title) and submit with --submit, then wait for completion
- Pause Suno after each take so it does not roll on
- Report captchas instead of bypassing them

## Ask for it when

- create a song on Suno from lyrics
- record a Suno song to a WAV file
- list my latest Suno songs
- download Suno songs by recording Chrome audio

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8869 (Sound Recorder door, which the extension polls)

**Warning:** port 8869 is also quoted for [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md) - confirm with `mantra-ports scan`.

Actions:

- `ping`
- `state`
- `list`
- `open`
- `play`
- `pause`
- `stop`
- `record`
- `create`

**Before you call:** Sound Recorder (Mantra) must be running (its door 8869 is polled by the Chrome extension); Suno open in Firefox/Chrome.

Example:

```
sunoctl record https://suno.com/song/<id> ~/Music/Suno/air.wav
```

More calls:

- what is playing: `sunoctl state`
- play or pause the open song: `sunoctl play ; sunoctl pause`
- liked songs list: `sunoctl list`

Evidence: README.md; TAKEOVER.md commands section; tools/sunoctl

## Inputs / Outputs

Inputs:

- song URL or id
- style and lyrics text

Outputs:

- WAV recordings
- song feed list

## Works with

- Uses: [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md)

## Code worth reusing

- `extension/background.js`: Chrome MV3 service worker that polls a local door for commands and runs them in a dedicated tab

## Notes

Replaced Firefox control because Cloudflare blocked it. Extension loaded unpacked in Chrome.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
