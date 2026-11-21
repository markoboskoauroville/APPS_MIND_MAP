# DJ Mantra (Android DJ app)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android DJ app built on the Mixxx 2.5.6 engine for the Hercules DJControl Mix Ultra: two decks, USB-stick library, beat lights, test builds.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/djmantra_app](https://github.com/markoboskoauroville/djmantra_app) |
| Also called | DJ Mantra app, DJMantra, Mixxx Android, djmantra app |
| Visibility | public |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | Android, Linux |
| Language | C++ (Mixxx engine, Qt Quick, Kotlin/Java glue) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: android-latest |
| Control level | none (no control api found) |

## What it can do

- Mix on two decks with sync, key lock, loops, hot cues, EQ and effects (Mixxx engine)
- Play to speaker, USB audio or Bluetooth through Oboe/AAudio
- Map the Hercules DJControl Mix Ultra over USB-C or Bluetooth LE MIDI incl. all pad modes, jog wheels and LEDs
- Light beat 1-8 of the phrase on the pads to line up songs
- Read music from USB sticks/SD cards, copy before play, keep folders as playlists while the drive is unplugged
- Rate, sort and export library lists with store links; play video files as tracks
- Build APKs and a launch test on an emulator in CI

## Ask for it when

- DJ from my Android phone
- use the Hercules Mix Ultra with the phone
- play music from a USB stick on the phone
- line up two songs by phrase with beat lights
- download the DJ Mantra test APK

## How to control it

No control API found.

Evidence: api.txt shows only a TIDAL OAuth localhost:8765 callback listener inside the app and adb/test docs; no control API found

## Inputs / Outputs

Inputs:

- music files on phone or USB drives
- Hercules DJControl Mix Ultra MIDI
- TIDAL login (planned)

Outputs:

- audio to the phone output
- controller LED feedback
- APK test builds (release android-latest)

## Hardware

- Hercules DJControl Mix Ultra
- Pixel 7 test phone
- USB sticks/SD cards

## Works with

- Uses: [DJ Mantra Ecstatic Dance page](djmantra-ecstatic-dance.md), [Termux Tools](termux-tools.md)
- Used by or talked to by: [DJ Mantra Ecstatic Dance page](djmantra-ecstatic-dance.md), [Generated Playlists](generated_playlists.md), [Controller Mapper (Mantra)](mix-ultra-mapper.md)

## Code worth reusing

- `lib/`: Mixxx engine tree (268 top-level entries) with Android Oboe audio output
- `.claude/commands/`: Claude commands: test-on-phone, test-tidal, capture-mix-ultra (device test workflows)
- `docs/research/djay-beatgrid-slicer.md`: Research on beat grid and slicer behaviour of djay for reuse

## Notes

Test builds, versions V1, V2... in CMakeLists. Status shown on djmantra.pages.dev. Large Mixxx fork; has one unmerged claude/ branch (many commits ahead). Touch UI, two outputs, TIDAL, genres and sections are 'coming next' per README. Rule: no reverse-engineered service APIs.

Unmerged branches with commits ahead of main: 1.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/djmantra_app/blob/HEAD/README.md)
- [CLAUDE.md](https://github.com/markoboskoauroville/djmantra_app/blob/HEAD/CLAUDE.md)
