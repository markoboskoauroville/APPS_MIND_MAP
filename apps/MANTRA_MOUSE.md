# Automated Mouse Actions (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac pointer helper: moves the mouse to the default button of any pop-up dialog, and maps a mouse button chord to Mission Control.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_MOUSE](https://github.com/markoboskoauroville/MANTRA_MOUSE) |
| Also called | Automated Mouse Actions, mouse helper |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Web, Hammerspoon |
| Language | Lua, Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v7 |
| Control level | http (own http routes) |

## What it can do

- Detect new dialogs and sheets and put the pointer on the default button
- Choose the bottom-right button when no default is declared
- Turn two mouse buttons pressed together into Mission Control
- Show a settings page and a window with ON/OFF

## Ask for it when

- move the mouse to the OK button automatically
- make a mouse chord open Mission Control

## How to control it

- Level: **http**
- Type: http
- Port: 8831

Actions:

- `GET /health`

**Before you call:** Automated Mouse Actions (Mantra) must be running.

Example:

```
curl -s 127.0.0.1:8831/health # the only documented route; the actions are inside the app
```

Evidence: page.lua line 174

## Hardware

- mouse with extra buttons

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `default_button.lua`: picks the default button of a dialog from the accessibility tree, with tests

## Notes

Original was Hammerspoon Lua with a web page; a Swift window app was added later.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
