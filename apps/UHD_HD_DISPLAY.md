# UHD HD Display (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Shows DaVinci Resolve's HD or UHD project mode as a word in the menu bar; a click or hotkey toggles it via a Resolve script.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/UHD_HD_DISPLAY](https://github.com/markoboskoauroville/UHD_HD_DISPLAY) |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Show HD or UHD in the menu bar while Resolve runs
- Switch the project resolution by a click or a hotkey
- Follow a shared state file every second
- Show a hover card with state

## Ask for it when

- switch Resolve between HD and UHD
- see current Resolve resolution

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
star press "uhd hd" "top"
```

More calls:

- list the controls of the window: `star read "uhd hd"`
- start the app in the background: `star open "uhd hd"`
- quit it: `star quit "uhd hd"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Code worth reusing

- `app/HoverCard.swift`: shared menu-bar hover card kit file

## Notes

Needs Resolve External scripting set to Local. State and hotkey in ~/.config/hdbadge.json. Carbon hot key, no permission.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
