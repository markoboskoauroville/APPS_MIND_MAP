# CQ MixPad Tutorial (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Offline Swift tutorial app that teaches the Allen & Heath CQ-12T by voice, diagrams and an on-screen hand that clicks CQ MixPad and Live.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/cq_mixpad_tutorial](https://github.com/markoboskoauroville/cq_mixpad_tutorial) |
| Also called | CQ MixPad Tutorial, CQ tutorial, mixer tutorial |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Play 27 lessons on the CQ-12T with pre-made narration and word-by-word highlighting
- Draw diagrams from data and light up the parts each step explains
- Move and click the real mouse in CQ MixPad and Ableton Live (the hand) via Accessibility
- Control Ableton Live over OSC and restore Live's playhead and solos after a lesson
- Be started, paused, resumed and played from a given step from outside via distributed notifications
- Pre-render narration with a TTS service into per-sentence mp3 with word marks

## Ask for it when

- teach me the CQ-12T mixer
- learn mixing and gain staging with a guided course
- walk me through routing and USB recording on the mixer
- start lesson N of the mixer tutorial

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `start <lesson>[.<step>]`
- `pause`
- `resume`

**Before you call:** Installed as a Mac app (Audio Mixing folder of the star menu); CQ MixPad must be open for the hand to click it. Hand click points depend on Live's full-screen layout.

Example:

```
build/start 6.2
```

More calls:

- start a lesson from its first step: `build/start 6`
- pause and continue the lesson: `# actions pause and resume are listed; their exact form is not in the harvested docs`

Evidence: TAKEOVER.md (build/start via distributed notifications)

## Inputs / Outputs

Inputs:

- content/lessons.json
- pre-made audio
- CQ MixPad window
- Ableton Live over OSC

Outputs:

- spoken lessons
- mouse clicks in CQ MixPad and Live

## Hardware

- Allen & Heath CQ-12T
- external monitor

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Talks to: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md)
- Used by or talked to by: [CQ MixPad Protocol](cq_mixpad_protocol.md)

## Code worth reusing

- `app/Hand.swift`: glides the real mouse to a control of another app, clicks it, with a ring and caption
- `app/LiveTurn.swift`: shared use of Ableton's OSC reply port with a lock so two sessions do not collide
- `tools/build_audio.py`: builds per-sentence narration with word marks via TTS, only for edited sentences

## Notes

Installed as a Mac app in the star menu folder Audio Mixing. Clicks only change pages and banks. Hand click points depend on Live's full-screen layout. Course tested end to end on 25.10.2026.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
