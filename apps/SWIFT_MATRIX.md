# Swift Matrix (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac window listing everything that starts by itself (star rows, login items, LaunchAgents, open apps) with ON/OFF auto-start switches and open/quit per row.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SWIFT_MATRIX](https://github.com/markoboskoauroville/SWIFT_MATRIX) |
| Also called | Swift Matrix |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- List 60-odd startup items and open apps in one window
- Switch auto-start on or off for login items and LaunchAgents (launchctl)
- Open or quit an app from its row
- Keep the window on top (TOP)

## Ask for it when

- what starts by itself on my Mac
- turn off auto-start of an app
- manage login items and launch agents

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
star press "swift matrix" "top"
```

More calls:

- list the controls of the window: `star read "swift matrix"`
- start the app in the background: `star open "swift matrix"`
- quit it: `star quit "swift matrix"`

Evidence: TAKEOVER.md v8: the window's first-row buttons OFF, TOP and X answer Accessibility as off, top, close

## Inputs / Outputs

Inputs:

- launchctl state
- login items

Outputs:

- launchctl enable/disable changes

## Works with

- Uses: [Star (Mantra), Swift menu](STAR_SWIFT.md)
- Used by or talked to by: [Star (Mantra), Swift menu](STAR_SWIFT.md)

## Notes

No HTTP or CLI control found. Only a button label convention for Accessibility.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SWIFT_MATRIX/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SWIFT_MATRIX/blob/HEAD/LESSONS.md)
