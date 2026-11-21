# Launcher (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Spotlight-style app launcher opened by Pause (F15) or Option-Space, with history icons, ranked search and remembered search chips.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STAR_LAUNCHER](https://github.com/markoboskoauroville/STAR_LAUNCHER) |
| Also called | Star Menu, Star Launcher, Star Menu app |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-05 |
| Build / release | GitHub workflow: no; latest release: v5 |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Open a search box in the middle of the screen the mouse is on
- Rank every Mac app by name, word start, initials and frequency
- Show last-opened apps first as icons
- Record a custom shortcut and take over the system one it clashes with
- Start at login without showing the box

## Ask for it when

- launch an app by typing a few letters
- open the launcher from the G815 Pause key

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `on`
- `off`
- `close`
- `gear`
- `search-N`
- `app-N`
- `record`
- `pause`
- `altspace-on`
- `altspace-off`
- `clear-apps`
- `clear-searches`
- `settings-close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "launcher" "record"
```

More calls:

- record / pause / search buttons (ids record, pause, search-N, app-N, gear): `star press "launcher" "pause"`
- list the controls: `star read "launcher"`
- quit it (pressing off quits): `star press "launcher" "off"`
- start it in the background: `star open "launcher"`

Evidence: TAKEOVER.md testing section: AX identifiers; pressing off quits it

## Hardware

- Logitech G815 (Pause key)

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](MANTRA_CONTROLS.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `Sources/Hotkey.swift`: Carbon hot key registration with no permission

## Notes

Repo is STAR_LAUNCHER; v1-v3 were called Star Menu. Bundle id com.mantra.starlauncher unchanged. Test helpers post distributed notifications (com.mantra.starlauncher.show/.query/.settings/.hide). Never post F13.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
