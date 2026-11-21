# Mantra Ports

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Tiny port registry for local servers: a server claims a port by name, a client asks for the name instead of a number.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_PORTS](https://github.com/markoboskoauroville/MANTRA_PORTS) |
| Also called | port registry, mantra-ports, ports.py |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS |
| Language | Python (plus Lua and Swift copies) |
| Status | dormant |
| Last push | 2026-10-27 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Claim a port for a named service (preferred number, else the next free one)
- Look up a live service by name and return its base URL, with fallback to the usual number
- List every registered service and whether it answers
- Report which program holds a fixed port (for example the Ableton OSC ports) and scan code for clashes
- Suggest the next free port for a new app

## Ask for it when

- which port is this app on
- avoid two apps using the same port
- give a new local server a free port
- find the URL of the voice server
- check for port clashes on the Mac

## How to control it

- Level: **cli**
- Type: cli, python-module

Actions:

- `list`
- `find`
- `forget`
- `next`
- `scan`
- `check`

**Before you call:** Install once with sh ~/Developer/MANTRA_PORTS/install.sh (copies ports.py, ports.lua, Ports.swift and the mantra-ports command into ~/.local/lib/mantra). The registry file is ~/.config/mantra-ports.json.

Example:

```
mantra-ports next
```

More calls:

- claim a port for a NEW app (Python server): take the number from 'mantra-ports next', then at start: `import sys, os; sys.path.insert(0, os.path.expanduser('~/.local/lib/mantra')); import ports; PORT = ports.claim('my-app', 8962) # id = app name, lower case, hyphens; returns the wanted port if free, else the next free one`
- claim a port in a Swift app (copy ~/.local/lib/mantra/Ports.swift into app/): `let port = Ports.claim("my-app", 8962) // client side: Ports.url("voice", fallback: 8837)`
- find where a running service is: `mantra-ports find voice # base URL, or nothing and exit 1; client code: ports.url('voice', 8837) never returns None`
- reserve a number for an app that is not running yet, and check for clashes: `mantra-ports book my-app 8962 ; mantra-ports check ; mantra-ports scan`

Evidence: README.md and TAKEOVER.md (ports.py is the registry and the command)

## Inputs / Outputs

Inputs:

- ~/.config/mantra-ports.json

Outputs:

- registry file entries
- base URLs

## Works with

- Used by or talked to by: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md), [Cost Agent (Mantra)](COST_AGENT.md), [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md), [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md), [G815 Lights](G815_LIGHTS.md), [Dock Switcher (Mantra)](MACOS_TASK_SWITCHER.md), [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Mantra Voice (speech server)](MANTRA_VOICE.md), [MIDI to Key Stroke](MIDI_TO_KEYSTROKE.md), [Opening and Closing (Mantra)](OPENING_AND_CLOSING.md), [Screenshot to TIDAL (Mantra)](SCREENSHOT_TO_TIDAL.md), [Mantra Speed Test](SPEED_TEST.md), [Connection Keeper](connection-keeper.md), [Mantra Pages](mantra_pages.md), [Oxi Controller (E16 Remote)](oxi-controller.md), [ZET Strike](zet_strike.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) will drive this app (claims the port id light-control)

## Code worth reusing

- `ports.py`: Python port claim/find/url, stdlib only
- `ports.lua`: Hammerspoon half of the same registry
- `Ports.swift`: Swift half, copied into each Swift app that serves HTTP

## Notes

Registry is a convenience, never a dependency: callers must fall back to the usual number. Fixed-port owners (FIXED table) are handled via check/scan. Install with install.sh into ~/.local/lib/mantra. To register a new app: run mantra-ports next, claim that number at start with ports.claim / Ports.claim / PORTS.claim (Lua ports.lua), and have every client ask by name. Rule from the manifest: never 5000, 5900 or 8080 (except the finder); fixed ports owned by another program (AbletonOSC UDP 11000/11001/11002) use Ports.own / mantra-ports check.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
