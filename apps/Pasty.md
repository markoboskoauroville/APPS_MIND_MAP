# Pasty

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Clipboard manager for macOS with one board, pins on every card, one-click paste and a global hotkey. Forked from pesty and reworked.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Pasty](https://github.com/markoboskoauroville/Pasty) |
| Also called | Pasty clipboard manager, pesty fork |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: build-4 |
| Control level | none (no control api found) |

## What it can do

- Keep clipboard history of text, images and other clips
- Pin a clip so it stays in front
- Paste a card with a click, Return or Cmd 1-9
- Search the history by typing
- Open with the global hotkey Cmd Ctrl A

## Ask for it when

- clipboard history on the Mac
- pin things I copy
- paste an earlier copied item
- clipboard manager
- clipboard history manager for Mac

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- system clipboard

Outputs:

- paste into the frontmost app

## Code worth reusing

- `Sources/Pasty/Hotkey/HotKeyCenter.swift`: global hotkey registration for a menu bar Mac app
- `Sources/Pasty/Monitor/ClipboardMonitor.swift`: clipboard change watcher
- `Sources/Pasty/Monitor/PasteService.swift`: pastes a clip into the previous app

## Notes

Fork of momenbasel/pesty (MIT). Keyboard-driven only, no external control API. Installable via Homebrew or releases.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/Pasty/blob/HEAD/TAKEOVER.md)
