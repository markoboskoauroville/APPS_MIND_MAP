# Spectral Analyzer (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac audio analyzer: live spectrum, EBU R128 loudness, stereo scopes, click/plosive/sibilance finder, piano keyboard for pitch, and a JSON command line.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SPECTRAL_ANALYZER](https://github.com/markoboskoauroville/SPECTRAL_ANALYZER) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v23 |
| Control level | cli (command line or script only) |

## What it can do

- Pass system sound through meters via BlackHole
- Draw spectrum, spectrogram, balance curve against 60 masters
- Measure EBU R128 loudness and true peak
- Find clicks, overs, plosives and hot S in files
- Show the sung note on a piano and play a pure tone per key
- Print findings as JSON for scripts

## Ask for it when

- check a master for clicks and loudness
- see the spectrum of what the Mac plays
- tune a voice to a piano note

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `--analyze <files>`
- `off`
- `top`
- `permissions`
- `close`

Example:

```
SpectralAnalyzer --analyze song.wav take2.wav
```

More calls:

- analyze two files: `SpectralAnalyzer --analyze song.wav take2.wav`
- press a button of the window: `star press "spectral analyzer" "top"`

Evidence: README.md From the command line; TAKEOVER.md v25 AX ids

## Inputs / Outputs

Inputs:

- audio device or BlackHole
- audio files

Outputs:

- JSON findings
- on-screen meters

## Hardware

- BlackHole 2ch
- audio interface or speakers

## Works with

- Talks to: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Code worth reusing

- `app/Detect.swift`: click and step finder: 1 ms high-passed energy against a 40 ms median
- `app/Pitch.swift`: pitch to note and piano mapping
- `app/Spek.swift`: spectrogram rendering

## Notes

Uses IOProcs not AVAudioEngine. Needs microphone permission to read input. Version 25 at last note.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
