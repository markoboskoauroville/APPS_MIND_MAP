# Oxi Controller (E16 Remote)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that turns the OXI E16 knob controller into a remote for Ableton Live (via AbletonOSC) or DaVinci Resolve audio, with a drawn screen.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/oxi-controller](https://github.com/markoboskoauroville/oxi-controller) |
| Also called | OXI E16 controller, DJ Mantra Ableton Remote for OXI E16, E16 for DaVinci Resolve, E16Remote, oxi controller |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift (Python tools) |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | other (other protocols) |

## What it can do

- Put the OXI E16 into Remote Mode over USB SysEx and draw its 128x64 screen and ring colours
- Map 16 knobs and pushes over 112 pages to Ableton Live actions through AbletonOSC and virtual MIDI
- Turn Live's arrangement zoom via an added AbletonOSC handler
- Control DaVinci Resolve track volume/pan/mute/solo through the Resolve Actions router (POST :8940/run)
- Ask Claude per knob whether a typed prompt is buildable (chat with four verdicts)
- Page-turner mode with profiles placed on pages
- Offer a UDP test door for scripted turns and pushes

## Ask for it when

- use the OXI E16 to control Ableton
- knobs for DaVinci Resolve audio mixing
- show Ableton values on the E16 screen
- map an endless encoder to a Live parameter

## How to control it

- Level: **other**
- Type: osc, midi
- Port: 11010

Actions:

- `turn N STEP`
- `push N`
- `release N`
- `shift 0|1`
- `present`
- `role N ROLE`
- `nav`
- `place NAME PAGE`

**Before you call:** One of the two apps (Ableton Remote for OXI E16 or E16 for DaVinci Resolve) must be running; UDP 11010 is a test door (no HTTP /api). Knob numbers are 1-based.

Example:

```
echo 'turn 1 5' | nc -u 127.0.0.1 11010 (UDP test door; knob numbers are 1-based)
```

More calls:

- push and release knob 3: `echo 'push 3' | nc -u -w1 127.0.0.1 11010 ; echo 'release 3' | nc -u -w1 127.0.0.1 11010`
- hold shift: `echo 'shift 1' | nc -u -w1 127.0.0.1 11010`
- redraw the colours on the E16: `echo 'present' | nc -u -w1 127.0.0.1 11010`

Evidence: TAKEOVER.md (v24 'Test door (UDP 11010)' and v27 Resolve notes)

## Inputs / Outputs

Inputs:

- OXI E16 over three CoreMIDI ports
- Live state via AbletonOSC
- Resolve state via port 8940

Outputs:

- AbletonOSC messages (UDP 11000)
- Resolve router calls
- E16 screen and ring LEDs
- Mackie/MIDI messages

## Hardware

- OXI Instruments E16

## Works with

- Uses: [Keyring](KEYRING_TERMUX.md), [Mantra Ports](MANTRA_PORTS.md)
- Used by or talked to by: [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md)

## Code worth reusing

- `Sources/E16/E16Remote.swift`: OXI E16 Remote Mode: SysEx screen/ring protocol over CoreMIDI
- `app/Resolve.swift`: Resolve mixer client through the Resolve Actions router with mute-by-gain workaround
- `tools/AbletonOSC-view.py`: AbletonOSC handler adding /live/view/zoom_arrangement
- `tools/resolve_keys.py`: Resolve hotkey helper

## Notes

Two app builds from one source: 'DJ Mantra Ableton Remote for OXI E16 (Mantra)' and 'E16 for DaVinci Resolve (Mantra)'. Always end a Remote Mode test with build/e16looks exit or the E16 stays blank. The ACK (06 53) is not recognised yet. A separate older repo oxi_e16_cq-12t bridges the E16 to the CQ mixer. UDP 11010 is a test door, not a MANTRA_PORTS-style /api. Always end a Remote Mode test with build/e16looks exit or the E16 stays blank.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/oxi-controller/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/oxi-controller/blob/HEAD/LESSONS.md)
