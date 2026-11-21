# Sound Recorder (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac recorder with input/output VU meters in dB, take waveforms, WAV save, and recording of one app's sound (Chrome, Suno) through a process tap.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_SOUND_RECORDER](https://github.com/markoboskoauroville/MANTRA_SOUND_RECORDER) |
| Also called | Mantra Sound Recorder, sound recorder |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-10 |
| Build / release | GitHub workflow: no; latest release: v15 |
| Control level | http (own http routes) |

## What it can do

- Record from a chosen input device with dB volume sliders and auto gain to -12 dB peak
- Play back takes with waveforms and save them as 24-bit WAV
- Record one app's audio (for example Chrome or Firefox) without a virtual cable
- Record a Suno song start to end with automatic stop and trim
- Expose record functions over a local HTTP door

## Ask for it when

- record the sound of one app
- record a song playing in Suno
- record the microphone to a WAV
- measure input level in dB

## How to control it

- Level: **http**
- Type: http
- Port: 8869

**Warning:** port 8869 is also quoted for [Suno Controller (Mantra)](CHROME_SUNO_CONTROLLER.md) - confirm with `mantra-ports scan`.

Actions:

- `record.app`
- `record.suno`
- `record.status`
- `record.stop`
- `permissions`

**Before you call:** Sound Recorder (Mantra) v12+ running; its function door is port 8869, called through Star API (port 8863); Suno open in Firefox.

Example:

```
star fn "sound recorder" record.suno '{"out":"~/x.wav","url":"https://suno.com/song/<id>"}' # the song in Suno, start to end, auto stop, trimmed, as WAV
```

More calls:

- record one app's sound (ScreenCaptureKit): `star fn "sound recorder" record.app '{"bundle":"com.apple.Safari","out":"~/x.wav","seconds":30}'`
- status: `star fn "sound recorder" record.status`
- stop: `star fn "sound recorder" record.stop`

Evidence: TAKEOVER.md line 136, app/Door.swift

## Inputs / Outputs

Inputs:

- audio input devices
- app audio via CoreAudio process tap

Outputs:

- 24-bit WAV takes

## Hardware

- any CoreAudio input and output device

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md), [Star API (Mantra)](STAR_API.md)
- Used by or talked to by: [Suno Controller (Mantra)](CHROME_SUNO_CONTROLLER.md), [Mantra Voice (speech server)](MANTRA_VOICE.md), [Star API (Mantra)](STAR_API.md), [Suno Songs prompt database](SUNO_SONGS.md)

## Code worth reusing

- `app/ProcTap.swift`: capture one app's audio through a CoreAudio process tap
- `app/Audio.swift`: IOProc based input and output with dB metering
- `app/Door.swift`: tiny JSON-over-HTTP function door registered for STAR_API

## Notes

Takes live in memory only and are lost when the app quits unless saved. Needs microphone permission. Bundle: Sound Recorder (Mantra).app, version 15 at last note. Door is on loopback and registered in ~/.config/star-fns/sound-recorder.json.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
