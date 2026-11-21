# Ableton Live Actions (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One Mac app that fits Ableton Live to Marko's hands: A1 assistant, MIDI-to-Mackie, MIDI-to-keystroke, CQ-12T channel macros, audio sync.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ABLETON_LIVE_ACTIONS](https://github.com/markoboskoauroville/ABLETON_LIVE_ACTIONS) |
| Also called | Ableton Live Actions, Ableton Assistant A1, A1, LIVE menu bar app, MIDI to MK Control, MIDI to keystroke |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift (+ Python helpers) |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v20 |
| Control level | none (no control api found) |

## What it can do

- Drive Ableton Live through AbletonOSC (UDP 11000 orders, answers on 11001 with a shared lock)
- Continue playback with Space, set markers, set the loop on transients (A1 assistant)
- Turn a MIDI controller knob into a Mackie Control command in Live
- Turn a MIDI CC or note into a keystroke or the Mac volume
- Macro: map Live tracks 1-16 to Ext. In/Out of an Allen & Heath CQ-12T and set up the CQ scene via CQ MixPad
- Copy track names between Live and the CQ-12T (both directions)
- Sync track 2 to track 1 from two recorders and export two equal-length WAVs
- Auto-run the channel macro when a Live set opens

## Ask for it when

- map Ableton tracks to the CQ12T mixer
- sync two recordings of the same concert
- use a MIDI knob as a Mackie control in Live
- set the loop to the transients in Ableton
- copy mixer channel names into Live

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- Ableton Live via AbletonOSC
- MIDI controllers
- two audio files (for sync)
- CQ MixPad window

Outputs:

- Live set changes
- synced WAV pairs
- CQ-12T scene and names

## Hardware

- Allen & Heath CQ-12T (via CQ MixPad, USB multitrack)
- MIDI controllers (e.g. OXI E16)

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Talks to: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md)
- Used by or talked to by: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md), [MIDI Tools (Mantra)](MANTRA_MIDI_TOOLS.md), [Stem Separation (Mantra)](STEM_SEPARATION.md), [Queen auto-update (Groq Auto Update)](groq-auto-update.md), [Queen (Groq AI Studio), server and tools](groq_ai_studio.md), [Mantra Mackie Control Translator](mantra-mackie-control-translator.md)

## Code worth reusing

- `app/LiveTurn.swift`: shared turn (flock) so only one program holds AbletonOSC answer port 11001 at a time; copied into other Swift apps
- `helpers/liveosc.py`: Python OSC client for AbletonOSC using the same shared-turn rule
- `helpers/audio_sync.py`: align two recordings of the same music to the sample and export equal-length WAVs; runs without Live (--a --b --out)
- `helpers/mixpad.py`: drives CQ MixPad by accessibility: connect, scenes, input source, names
- `app/Ports.swift`: MANTRA_PORTS claim helper

## Notes

No HTTP /health or /api door found in the harvested files (Ports.swift is present but only the OSC side is documented). It is a client of AbletonOSC, not a server. Older OSC router on port 11002 was removed in v17. abletonosc/mantra-application.patch carries a patch for the AbletonOSC remote script.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/ABLETON_LIVE_ACTIONS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/ABLETON_LIVE_ACTIONS/blob/HEAD/LESSONS.md)
