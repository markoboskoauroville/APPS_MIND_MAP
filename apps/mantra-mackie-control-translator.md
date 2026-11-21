# Mantra Mackie Control Translator

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Hammerspoon module that translates OXI E16 MIDI knobs and notes into Mackie Control so Ableton Live's arrangement timeline can sit under a knob.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra-mackie-control-translator](https://github.com/markoboskoauroville/mantra-mackie-control-translator) |
| Also called | MANTRA_MACKIE, mackie translator, OXI E16 to Mackie |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS, Hammerspoon |
| Language | Lua |
| Status | active |
| Last push | 2026-10-02 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Translate a knob press or pad into one PLAY/STOP button where the insert point is master
- Turn a relative knob into the Mackie jog wheel (invertible) to move the arrangement
- Map relative knobs to V-Pots and absolute knobs to 14-bit faders
- Map notes or momentary CCs to Mackie buttons
- Show a rules page with what Live receives and why a rule cannot fire
- Read whether Live is playing from Live's own log

## Ask for it when

- control Ableton's timeline with a MIDI knob
- make an OXI E16 knob scroll the arrangement
- map MIDI CC to Mackie Control for Live

## How to control it

No control API found.

Evidence: HANDOFF.md, star/mackie.lua (settings page at the rules port; no declared actions)

## Inputs / Outputs

Inputs:

- MIDI from OXI E16

Outputs:

- Mackie Control messages on an IAC bus to Ableton Live

## Hardware

- OXI Instruments E16
- IAC MIDI driver

## Works with

- Uses: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](MANTRA_CONTROLS.md)

## Code worth reusing

- `mcu.lua`: Mackie Control message encoder (buttons, 14-bit faders, V-Pot, jog)
- `rules.lua`: rule engine translating MIDI input kinds to Mackie output kinds
- `tests/sendmk.c`: tool to send raw Mackie messages for testing

## Notes

Switched on and off from the star menu. Tests run with plain lua5.4. Needs the Live control surface set to MackieControl and the scene sent to the E16.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
