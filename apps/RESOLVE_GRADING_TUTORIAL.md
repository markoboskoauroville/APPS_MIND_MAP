# DaVinci Grading Tutorial (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Offline spoken tutorial app on grading a Sony A7 V music video in DaVinci Resolve, with diagrams and a reading highlight.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/RESOLVE_GRADING_TUTORIAL](https://github.com/markoboskoauroville/RESOLVE_GRADING_TUTORIAL) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Teach eight lessons by voice with the sentence and word highlighted
- Draw diagrams that light up per step
- Play pre-made Speechify audio with word marks
- Tag which steps the Resolve Actions button does not yet automate

## Ask for it when

- learn colour grading workflow in Resolve
- listen to the grading tutorial

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "grading tutorial" "top"
```

More calls:

- list the controls of the window: `star read "grading tutorial"`
- start the app in the background: `star open "grading tutorial"`
- quit it: `star quit "grading tutorial"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Works with

- Uses: [MA Reader Speechify module](MA_READER_SPEECHIFY.md)
- Used by or talked to by: [Indian Mantras (Mantra)](INDIAN_MANTRAS.md)

## Code worth reusing

- `tools/build_audio.py`: make per-sentence Speechify audio with word marks and key rotation
- `app/DiagramView.swift`: data-driven diagram drawing with lit parts

## Notes

Built from the CQ MixPad Tutorial player. Never touches Resolve itself. Not yet listened end to end at last note. Contains generated audio and pictures.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
