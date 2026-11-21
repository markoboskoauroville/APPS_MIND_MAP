# Dock Switcher (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app: ctrl-backtick opens a square of your Dock icons on every screen to switch or launch apps, with clock, weather and next event; also feeds the phone.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MACOS_TASK_SWITCHER](https://github.com/markoboskoauroville/MACOS_TASK_SWITCHER) |
| Also called | Dock Switcher, Dock Switcher (Mantra), macOS Task Switcher, dock-switcher, Dock replacement |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Hammerspoon |
| Language | Swift (and Lua) |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v7 |
| Control level | http (own http routes) |

## What it can do

- Open a square of Dock icons on every screen with Ctrl+` or double-tap Ctrl
- Switch to or launch the lit app, quit (Q) or hide (H)
- Learn app order from use
- Show clock, date, weather and next calendar event
- Serve the phone's dock over HTTP: app list, icons, open app, front app's menu
- Keep an older Lua version for Hammerspoon

## Ask for it when

- switch apps like Command-Tab but launch closed apps
- show my Dock as a grid
- open a Mac app from the phone
- show the front app's menu on the phone

## How to control it

- Level: **http**
- Type: http, remote-door-http
- Port: 8861

Actions:

- `/apps`
- `/icon?id=`
- `/open?id=`
- `/menu`
- `/menuclose`
- `/keys?after=N`

**Before you call:** Dock Switcher (Mantra) must be running; no token. The door contract of the manifest (/health, /api) is still being added.

Example:

```
curl -s http://127.0.0.1:8861/apps # the open apps; from the phone use the Mac's address on the home network or Tailscale
```

More calls:

- open an app by its id: `curl -s 'http://127.0.0.1:8861/open?id=<id-from-/apps>'`
- the menu page: `curl -s http://127.0.0.1:8861/menu`

Evidence: TAKEOVER.md Remote.swift section; app/Remote.swift

## Inputs / Outputs

Inputs:

- Dock persistent apps
- dock.json settings

Outputs:

- app switching
- list of apps for the phone

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Talks to: [Mantra Ports](MANTRA_PORTS.md), [Mantra Remote Viewing (Mantra Remote)](MANTRA_REMOTE_VIEWING.md)

## Code worth reusing

- `app/Ports.swift`: claim a port from the MANTRA_PORTS registry with health path
- `app/Dock.swift`: read Dock persistent apps and icons
- `app/Keys.swift`: Carbon hot key and double-Ctrl event tap
- `app/Remote.swift`: small HTTP listener for phone control; AXPress of front app menu

## Notes

Not yet the standard /health + /api door; custom endpoints. Lua and Swift versions coexist. Does not use the Mantra Door token itself.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MACOS_TASK_SWITCHER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MACOS_TASK_SWITCHER/blob/HEAD/LESSONS.md)
