# Song Simple Mixer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app: one vocal, one backing track, two faders, nudge and 'vocal space' ducking, exports the mix as a WAV.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Song_simple_mixer](https://github.com/markoboskoauroville/Song_simple_mixer) |
| Also called | Song simple mixer, Mantra song mixer |
| Visibility | public |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: archive/ccr-37854fff-xt3izt |
| Control level | none (no control api found) |

## What it can do

- Load a vocal and a backing track in any common format and resample to 48 kHz
- Set levels (-30 to +12 dB) and mute each
- Nudge the vocal earlier or later in 1, 10 and 50 ms steps
- Duck the backing band by band where the vocal sings (vocal space)
- Play, seek and export a 48 kHz 16-bit WAV with a -1 dBFS limiter

## Ask for it when

- mix a vocal over a backing track on the phone
- remix a Suno song parts
- export a simple two-track mix

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- vocal file and backing file (mp3, wav, flac, m4a, ogg/opus)

Outputs:

- 48 kHz 16-bit WAV mix

## Works with

- Uses: [Suno Songs prompt database](SUNO_SONGS.md)
- Talks to: [Mantra Manifest](MANTRA_MANIFEST.md)

## Code worth reusing

- `app/src/main/java/community/auroville/mantra/mixer/Space.kt`: band-wise vocal-aware ducking of a backing track
- `app/src/main/java/community/auroville/mantra/mixer/Mix.kt`: mix, limiter and dithered export
- `app/src/main/java/community/auroville/mantra/mixer/Decoder.kt`: decode and resample to 48 kHz stereo

## Notes

Has unit tests (MixTest, SpaceTest). Built by GitHub Actions APK workflow.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/Song_simple_mixer/blob/HEAD/TAKEOVER.md)
