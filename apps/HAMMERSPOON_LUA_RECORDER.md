# Hammerspoon Lua Recorder

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Keyboard and mouse macro recorder for macOS in Lua for Hammerspoon: records itself to disk with fixed waits, undo, redo and a line that teaches the Lua.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/HAMMERSPOON_LUA_RECORDER](https://github.com/markoboskoauroville/HAMMERSPOON_LUA_RECORDER) |
| Also called | Marco recorder Mac, marco_recorder, Hammerspoon recorder |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Hammerspoon |
| Language | Lua |
| Status | dormant |
| Last push | 2026-08-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Record keys and mouse clicks as hs.eventtap Lua, with a fixed wait(333) between steps
- Write every step to disk at once so the file is the only source of truth
- Undo and redo recorded steps
- Show what was pressed and the exact Lua written in a status strip
- Let you edit CapturedMacro.lua by hand while recording continues between marker comments

## Ask for it when

- record a macro on the Mac
- keyboard and mouse recorder in Lua
- teach me Hammerspoon Lua by recording

## How to control it

No control API found.

Evidence: none found; hotkeys only

## Inputs / Outputs

Inputs:

- keyboard and mouse events

Outputs:

- CapturedMacro.lua

## Works with

- Uses: [Marco Macro Recorder (Windows)](MARCO_MACRO_RECORDER.md)
- Used by or talked to by: [Marco Macro Recorder (Windows)](MARCO_MACRO_RECORDER.md)

## Code worth reusing

- `marco_recorder.lua`: macro recorder core with marker-bounded file writing

## Notes

MIT licence. Needs Accessibility and Input Monitoring for Hammerspoon. Installed by install_marco_recorder_v1.sh with backup. The Swift Macro Recorder (MANTRA_MACRO) is the newer Mantra app for the same job.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/HAMMERSPOON_LUA_RECORDER/blob/HEAD/README.md)
