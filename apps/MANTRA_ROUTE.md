# Mantra Route

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android notification that lists every audio output as tappable rows, with mono or stereo and a balance dial, using Shizuku.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_ROUTE](https://github.com/markoboskoauroville/MANTRA_ROUTE) |
| Also called | Mantra Route |
| Visibility | public |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: v37 |
| Control level | none (no control api found) |

## What it can do

- List every audio output the phone knows in one ongoing notification
- Route sound to the tapped output using the best available method (policy, MediaRouter2, communication routing)
- Switch stereo/mono and set a balance dial for all audio
- Probe which privileged capabilities exist on this phone and print the result
- Provide quick-settings volume tile

## Ask for it when

- switch audio output on Android with one tap
- send phone sound to the speaker or Bluetooth quickly
- mono or balance for all phone audio

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- Android audio outputs and sessions

Outputs:

- audio routing changes

## Hardware

- Nothing Phone (2a) on Android 16
- Bluetooth / USB / hearing-aid outputs

## Code worth reusing

- `app/src/main/java/com/mantra/route/Router.kt`: routing ladder with probes: policy, MediaRouter2, communication device
- `app/src/main/java/com/mantra/route/VolumeTileService.kt`: quick-settings volume tile

## Notes

MODIFY_AUDIO_ROUTING cannot be granted to normal apps; what works depends on the phone, hence the Probe screen. No external API.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_ROUTE/blob/HEAD/README.md)
