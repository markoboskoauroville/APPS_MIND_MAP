# Resolve Pages (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Command-Tab style switcher for DaVinci Resolve pages: hold Option and tap backtick to cycle the page ring.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/RESOLVE_PAGES](https://github.com/markoboskoauroville/RESOLVE_PAGES) |
| Also called | Command-Tab for Resolve |
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

- Show a row of Resolve pages and step through them with the hotkey
- Jump back to the last page with a quick tap
- Show the current page as three letters in the menu bar
- Show a hover card with state in the menu bar

## Ask for it when

- switch Resolve pages from the keyboard
- see which Resolve page is open

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
star press "resolve pages" "top"
```

More calls:

- list the controls of the window: `star read "resolve pages"`
- start the app in the background: `star open "resolve pages"`
- quit it: `star quit "resolve pages"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Code worth reusing

- `helper/pages_helper.py`: Resolve scripting helper with a line protocol: open, pages, quit
- `app/HoverCard.swift`: shared menu-bar hover card kit file

## Notes

Needs Resolve External scripting set to Local; no permission otherwise (Carbon hot keys). State in ~/.config/pages.json. Born from MANTRA_STAR apps/pages.lua.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
