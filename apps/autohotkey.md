# TinyTask to AutoHotkey

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit page that converts TinyTask .rec macro recordings into AutoHotkey v2 scripts.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/autohotkey](https://github.com/markoboskoauroville/autohotkey) |
| Also called | tinytask converter |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | Windows, Web |
| Language | Python (Streamlit) |
| Status | active |
| Last push | 2026-05-19 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Decode TinyTask binary .rec files (mouse and key events)
- Write an AutoHotkey v2 script with the original timing
- Compress runs of mouse moves
- Scale playback speed and set a minimum sleep

## Ask for it when

- convert a TinyTask recording to AutoHotkey
- turn a macro recording into an editable script

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- .rec TinyTask recordings

Outputs:

- .ahk AutoHotkey v2 scripts

## Code worth reusing

- `app.py`: parser for the 20-byte TinyTask .rec record format and AHK v2 generator

## Notes

Coordinates are absolute, so scripts only fit the same screen resolution as when recorded. Streamlit UI only, no API.

## Docs in the repo

- `README.md`
