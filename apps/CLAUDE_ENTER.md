# Claude Enter (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac helper that makes Return send and Shift+Return add a new line in a claude.ai tab in Chrome.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLAUDE_ENTER](https://github.com/markoboskoauroville/CLAUDE_ENTER) |
| Also called | Claude Enter |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Chrome |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | none (no control api found) |

## What it can do

- Swallow Return in Chrome claude.ai tabs and send Command+Return instead
- Check the front tab address through Apple Events
- Skip when a dialog or a modifier key is active
- Switch ON or OFF from its window

## Ask for it when

- press Enter to send in Claude chat
- change Enter behaviour in claude.ai

## How to control it

No control API found.

Evidence: none found; window buttons have accessibility ids off, top, close per TAKEOVER.md

## Notes

Needs Accessibility and Automation to Chrome. Born from a Hammerspoon Lua script (MANTRA_STAR apps/enter.lua).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
