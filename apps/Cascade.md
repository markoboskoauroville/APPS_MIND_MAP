# Cascade

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Menu-bar app: one click cascades every window on the screen under the pointer so each keeps a title-bar strip showing; click again to restore.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Cascade](https://github.com/markoboskoauroville/Cascade) |
| Also called | CA menu bar, window cascade, AutoRaise partner |
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

- Cascade all windows of the pointer's screen in two halves with 30 pt steps
- Restore every window's position, size and stacking order on the second click
- Option-click to re-cascade without restoring
- Remember the arrangement per display
- Fill the screen when only one window, split left/right for two

## Ask for it when

- tidy all my windows
- cascade windows so I can reach each with the mouse
- restore my window layout

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- window list through Accessibility

Outputs:

- moved windows

## Code worth reusing

- `Sources/Cascade/AXBridge.swift`: Accessibility bridge to read and move other apps' windows
- `Sources/Cascade/Snapshots.swift`: record and restore window geometry and order
- `Sources/Cascade/CascadeLayout.swift`: cascade layout maths per display

## Notes

Needs Accessibility permission; after an update toggle it off and on if nothing happens. Install: brew install --cask markoboskoauroville/pasty/cascade. Only the display under the pointer is touched.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/Cascade/blob/HEAD/README.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/Cascade/blob/HEAD/HANDOFF.md)
