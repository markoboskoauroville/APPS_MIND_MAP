# FKeys

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Menu-bar letter that switches F1 to F12 between function keys (F) and media controls (C) with one click or control-option-command-K.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/FKeys](https://github.com/markoboskoauroville/FKeys) |
| Also called | F keys switch, Function keys toggle |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: latest |
| Control level | none (no control api found) |

## What it can do

- Swap the top row between plain function keys and media keys with hidutil key remapping
- Read the Mac's own key table so it works on any model
- Switch from a menu-bar click or a registered global hotkey
- Need no Accessibility or Input Monitoring permission

## Ask for it when

- make F keys work as function keys
- toggle media keys and F keys
- one click fn key mode

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- keyboard HID key table

Outputs:

- hidutil remapping

## Code worth reusing

- `Sources/FKeys/Hidutil.swift`: apply and clear hidutil key remapping
- `Sources/FKeys/FnKeyMap.swift`: build the fn swap map from the Mac's key table
- `Sources/FKeys/HotKey.swift`: registered global hotkey without Input Monitoring

## Notes

Install: brew install --cask markoboskoauroville/pasty/fkeys. Three other approaches (defaults fnState, IOHIDSystem call, private event system) failed on Apple Silicon. Release tag is the rolling tag latest.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/FKeys/blob/HEAD/README.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/FKeys/blob/HEAD/HANDOFF.md)
