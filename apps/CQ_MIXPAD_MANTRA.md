# CQ MixPad (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android remote for the Allen & Heath CQ-12T built on its decoded private protocol: faders, PEQ, comp, RTA, record, reference matching, three layouts.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CQ_MIXPAD_MANTRA](https://github.com/markoboskoauroville/CQ_MIXPAD_MANTRA) |
| Also called | CQ MixPad, CQ MixPad Mantra, CQ12T app, concert-mix, MixPad Mantra |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | none (no control api found) |

## What it can do

- Control CQ-12T faders, mutes, EQ, compressor, gate, scenes and routing from a Pixel
- Show a rainbow RTA and match the Main PEQ to a loaded reference track (MATCH, UNDO)
- Record the CQ's USB or SD multitrack and mirror tracks
- Switch Stream Mode (Stereo or Multitrack)
- Switch between CQ, MA and S1 (Studio One look) layouts with one button
- Man-in-the-middle capture tool to decode more of the protocol

## Ask for it when

- control the CQ12T from my phone
- mix the concert from the Pixel
- match the mixer EQ to a reference song
- record multitrack from the CQ

## How to control it

No control API found.

Evidence: TAKEOVER.md mentions a file test channel files/ref_command.txt to files/ref_answer.txt (ReferenceDesk.command); no network API found

## Inputs / Outputs

Inputs:

- CQ-12T over Wi-Fi (TCP 51326, UDP 51324)
- reference audio files (MP3, FLAC)

Outputs:

- desk commands
- recordings in Music/CQ MixPad
- RTA match PEQ changes

## Hardware

- Allen & Heath CQ-12T
- Pixel 7

## Works with

- Uses: [Mantra Sandbox](MANTRA_SANDBOX.md), [CQ MixPad Protocol](cq_mixpad_protocol.md)
- Talks to: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md)
- Used by or talked to by: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md), [CQ Ethernet Bridge](CQ_ETHERNET_BRIDGE.md), [Mantra Sandbox](MANTRA_SANDBOX.md), [CQ MixPad Protocol](cq_mixpad_protocol.md), [CQ MixPad Tutorial (Mantra)](cq_mixpad_tutorial.md)

## Code worth reusing

- `android/app/src/main/java/com/mantra/cqmixpad/Cq.kt`: CQ-12T wire protocol client (handshake, get, set, dump)
- `android/app/src/main/java/com/mantra/cqmixpad/reference/Analyzer.kt`: LUFS, LRA and 31-band analysis of a reference track and matching to EQ
- `tools/cq_mitm.py`: man-in-the-middle proxy to capture the desk protocol
- `PROTOCOL.md`: decoded CQ-12T protocol (moved to public repo cq_mixpad_protocol on 8.11.2026)

## Notes

Protocol facts and scales are now in the public repo cq_mixpad_protocol. USB capture on the Pixel read zeros at v46 (open issue). Rule: same function, same place in all three layouts. Only the desk's RTA is a reliable live source until USB capture works.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/CQ_MIXPAD_MANTRA/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/CQ_MIXPAD_MANTRA/blob/HEAD/LESSONS.md)
