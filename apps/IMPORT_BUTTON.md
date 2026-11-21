# Import Button (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac helper that turns the mouse thumb button into Command-I (Import Media) while DaVinci Resolve is in front.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/IMPORT_BUTTON](https://github.com/markoboskoauroville/IMPORT_BUTTON) |
| Also called | Import Button |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Learn a chosen mouse button
- Swallow that button when Resolve is in front and send a key combination
- Import media now from a button in its window
- Store settings in a JSON config

## Ask for it when

- import media in Resolve with a mouse button
- map a mouse thumb button to a shortcut

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `permissions`
- `close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "import button" "top"
```

More calls:

- list the controls of the window: `star read "import button"`
- start the app in the background: `star open "import button"`
- quit it: `star quit "import button"`

Evidence: TAKEOVER.md accessibility ids

## Hardware

- mouse with extra buttons

## Notes

Needs Accessibility permission. Born from a Hammerspoon Lua script.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
