# Star (Mantra), Swift menu

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**The star: Swift menu-bar app that lists and launches all of Marko's Mantra apps, groups running ones, orders menu bar items; replaces the Lua star MANTRA_STAR.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STAR_SWIFT](https://github.com/markoboskoauroville/STAR_SWIFT) |
| Also called | Star, the star, MANTRA_STAR, Star (Mantra) |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Linux |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v17 |
| Control level | cli (command line or script only) |

## What it can do

- Show every Mantra app as a menu row and start or stop it
- List running apps under Swift Matrix, last picked first
- Fix the order of third-party menu bar icons
- Print its menu as text (--print-menu)
- Give the whole Mantra icon set via icons6
- Run a Linux variant (linux/star.py)

## Ask for it when

- launch one of my Mantra apps
- menu with all my apps
- order my menu bar icons
- what apps are on the star menu

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--print-menu`
- `--picked`

**Before you call:** The six-pointed star menu launcher; rows are in ~/.config/star-rows.json.

Example:

```
open -a "Star (Mantra)" --args --print-menu # prints the menu rows; the exact binary path is in TAKEOVER.md
```

More calls:

- the menu rows as text: `open -a "Star (Mantra)" --args --print-menu`

Evidence: TAKEOVER.md v8/v9 states (--print-menu, --picked)

## Inputs / Outputs

Inputs:

- rows.json app list
- Hammerspoon states cache

Outputs:

- menu bar menu
- star-running and order files

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Star Monitor (Mantra)](STAR_MONITOR.md)
- Talks to: [Swift Matrix (Mantra)](SWIFT_MATRIX.md)
- Used by or talked to by: [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md), [Screen Brightness Automatic (Mantra)](DARKEN_THE_SCREENS.md), [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md), [LAN Scanner (Mantra)](LAN_SCANNER.md), [Star Monitor (Mantra)](STAR_MONITOR.md), [Swift Matrix (Mantra)](SWIFT_MATRIX.md)

## Code worth reusing

- `app/MenuBar.swift`: orders third-party menu bar items into fixed places
- `icons6/install_icons.py`: installs the six-icon set onto apps
- `launchd/com.mantra.star.plist`: launchd login item

## Notes

HAMMERSPOON_TO_SWIFT.md plans moving the five remaining Lua rows (MIDI to Key Stroke, MIDI to MK Control, Macro Recorder, Buckets, Hammerspoon) to Swift, only on Marko's word. Control surface is command-line flags only.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/STAR_SWIFT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/STAR_SWIFT/blob/HEAD/LESSONS.md)
