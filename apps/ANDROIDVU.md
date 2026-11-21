# AndroidVU

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android probe for per-stream audio levels (call, media, ring, notification, alarm); meant to become five hairline VU meters as an overlay. v1 draws no meters.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ANDROIDVU](https://github.com/markoboskoauroville/ANDROIDVU) |
| Also called | Android VU, AndroidVU probe, MA channels probe |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | none (no control api found) |

## What it can do

- Probe what level each Android audio stream can actually be read at
- Report the probe result (MaProbeReport)
- Plan: draw five one-pixel VU meters as a system overlay with a Quick Settings tile

## Ask for it when

- show audio levels on my Android phone
- find out if Android lets me read stream volume
- VU meter overlay on the phone

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- Android audio streams STREAM_VOICE_CALL, MUSIC, RING, NOTIFICATION, ALARM

Outputs:

- probe report

## Notes

v1 is only a measuring probe: no overlay and no SYSTEM_ALERT_WINDOW permission yet. Android has no per-stream output level API, so the finished meters may be impossible or approximate. HANDOFF.md and NEXT_DEFAULTS.md explain the decisions.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/ANDROIDVU/blob/HEAD/TAKEOVER.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/ANDROIDVU/blob/HEAD/HANDOFF.md)
