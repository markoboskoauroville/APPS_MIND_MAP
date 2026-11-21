# Shruti Box and Voice Trainer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android shruti box emulator: thirteen vector valves with synthesised reeds, 41 drone, raga and chord presets, a sequencer, a voice trainer and MIDI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SHRUTI_BOX_AND_VOICE_TRAINER](https://github.com/markoboskoauroville/SHRUTI_BOX_AND_VOICE_TRAINER) |
| Also called | Mantra Shruti Box, MANTRA_SHRUTI_BOX, shruti box |
| Visibility | public |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v27 |
| Control level | none (no control api found) |

## What it can do

- Sound a shruti box by tapping valves, in any key C to B
- Open 41 presets (drones, ragas, chords) and save custom ones
- Sequence presets with BPM and crossfade
- Train the voice with AUTO walking a range of the 88 keys at set tolerances
- Play it from a USB MIDI keyboard with velocity and held keys

## Ask for it when

- shruti box on the phone
- drone for singing practice
- voice trainer pitch exercises
- raga drone

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- touch
- USB MIDI keyboard

Outputs:

- synthesised audio (AudioTrack 48 kHz)
- APK

## Hardware

- USB MIDI keyboard (Launchkey Mini MK4)

## Code worth reusing

- `app/src/main/java/com/mantra/shrutibox/Reeds.kt`: reed tuning, wavetable and mixer, no Android dependency
- `app/src/main/java/com/mantra/shrutibox/Engine.kt`: AudioTrack float synth engine on its own thread

## Notes

Renamed from MANTRA_SHRUTI_BOX on 22.10.2026. TAKEOVER calls the repo private but the catalog list marks it public; trust repos_full.tsv. Only the two newest releases are kept.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/SHRUTI_BOX_AND_VOICE_TRAINER/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/SHRUTI_BOX_AND_VOICE_TRAINER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SHRUTI_BOX_AND_VOICE_TRAINER/blob/HEAD/LESSONS.md)
