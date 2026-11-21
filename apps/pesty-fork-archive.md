# Pesty fork (archive) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Pasty](Pasty.md). Replaced by Pasty.

**Archived public fork of the open-source Pesty clipboard manager (Swift/SwiftUI); superseded by Marko's private Pasty repo. Safe to delete.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/pesty-fork-archive](https://github.com/markoboskoauroville/pesty-fork-archive) |
| Also called | pesty, Pesty clipboard manager fork, Pasty (old public fork) |
| Visibility | public |
| Kind | fork |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-07-06 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Keep a history of copied text, rich text, links, images, files and colours
- Slide up a colour-coded strip by global hotkey and paste the chosen clip into the front app
- Save clips into pinboards, search history, optional iCloud sync

## Ask for it when

- clipboard history manager for Mac
- paste from clipboard history with a hotkey

## How to control it

No control API found.

Evidence: README.md; no control API in the fork (api.txt only an App Store badge link)

## Inputs / Outputs

Inputs:

- system clipboard

Outputs:

- pasted clips

## Code worth reusing

- `Sources/Pesty/Monitor/ClipboardMonitor.swift`: Polls the macOS pasteboard and stores clips by type
- `Sources/Pesty/Hotkey/HotKeyCenter.swift`: Global hotkey registration and recorder

## Notes

Description says ARCHIVE, superseded by the private Pasty repo, safe to delete. Upstream is momenbasel/pesty (MIT). Current Pasty install is via homebrew-pasty. RETIRED/SUPERSEDED: use Pasty instead.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/pesty-fork-archive/blob/HEAD/README.md)
