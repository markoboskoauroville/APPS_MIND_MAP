# Marco Macro Recorder (Windows)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Windows keyboard and mouse macro recorder in AutoHotkey v2 that records to disk with fixed Sleep(333) gaps and shows the AutoHotkey code it wrote.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MARCO_MACRO_RECORDER](https://github.com/markoboskoauroville/MARCO_MACRO_RECORDER) |
| Also called | Marco Macro Recorder, AHK macro recorder |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | Windows |
| Language | AutoHotkey v2 |
| Status | dormant |
| Last push | 2026-08-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Record keys and clicks instantly to CapturedMacro.ahk
- Write a fixed Sleep(333) between steps so playback does not depend on timing
- Show what you pressed and the exact AutoHotkey code beside it
- Undo and redo recorded steps
- Allow hand edits of the file while recording continues

## Ask for it when

- record a macro on Windows
- learn AutoHotkey by watching what it writes
- replay my keyboard and mouse actions on Windows

## How to control it

No control API found.

## Inputs / Outputs

Outputs:

- CapturedMacro.ahk

## Works with

- Talks to: [Hammerspoon Lua Recorder](HAMMERSPOON_LUA_RECORDER.md)
- Used by or talked to by: [Hammerspoon Lua Recorder](HAMMERSPOON_LUA_RECORDER.md)

## Code worth reusing

- `13-Marco_Macro_Recorder_AHK_v13.ahk`: self-writing macro recorder with teaching status line

## Notes

Windows only. The Mac equivalent is MANTRA_MACRO (Macro Recorder (Mantra)); older Mac port is HAMMERSPOON_LUA_RECORDER. MIT licence.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MARCO_MACRO_RECORDER/blob/HEAD/README.md)
