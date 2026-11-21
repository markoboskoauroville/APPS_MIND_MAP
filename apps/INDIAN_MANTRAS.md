# Indian Mantras (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Offline Mac app that teaches the Gayatri and Asato Ma mantras word by word with a choice of voices, speed control and word highlighting.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/INDIAN_MANTRAS](https://github.com/markoboskoauroville/INDIAN_MANTRAS) |
| Also called | Indian Mantras |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | macOS |
| Language | Swift (Python tools) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | none (no control api found) |

## What it can do

- Teach six lessons word by word with pauses to repeat
- Show Devanagari, transliteration and meaning on a card
- Switch among pre-rendered voices from several engines
- Change speed with pitch kept and toggle sentence/word highlight
- Play a real performance clip at the end of each lesson with a gentle fade
- Render voices ahead with a tool script

## Ask for it when

- learn the Gayatri mantra word by word
- practise Asato Ma pronunciation
- listen to a mantra lesson offline

## How to control it

No control API found.

Evidence: none found (hot keys only)

## Inputs / Outputs

Inputs:

- content/lessons.json

Outputs:

- audio lessons

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [DaVinci Grading Tutorial (Mantra)](RESOLVE_GRADING_TUTORIAL.md)

## Code worth reusing

- `tools/render_voices.py`: renders every sentence in every voice once, keyed by hash

## Notes

Contains copyrighted performance clips inside the private app; keep private.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
