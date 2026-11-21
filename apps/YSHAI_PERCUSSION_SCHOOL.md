# Percussion School (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that compares the lessons on a course portal with a local folder, lists what is missing and downloads only that.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/YSHAI_PERCUSSION_SCHOOL](https://github.com/markoboskoauroville/YSHAI_PERCUSSION_SCHOOL) |
| Also called | Percussion School lesson downloader |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v8 |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Control Firefox through WebDriver BiDi and read the portal catalogue
- Match videos by stream duration and PDFs by name or size so nothing is downloaded twice
- Show complete, partial and missing lessons with per-lesson download
- Download missing videos, exercises and PDFs oldest first with speed and time left

## Ask for it when

- download missing percussion lessons
- check which lessons I do not have yet

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
star press "percussion school" "top"
```

More calls:

- list the controls of the window: `star read "percussion school"`
- start the app in the background: `star open "percussion school"`
- quit it: `star quit "percussion school"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Code worth reusing

- `app/Bidi.swift`: WebDriver BiDi client over WebSocket to Firefox
- `app/Pipeline.swift`: catalogue compare and download pipeline

## Notes

Never types a password; user stays logged in in Firefox. Course and teacher details left out. Local folder layout follows a manifest module on lessons.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
