# Homebrew tap for Mantra tools

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Homebrew tap that installs Mantra Mac tools: Cascade (window cascading), FKeys (function-key switch) and Pasty (clipboard manager).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/homebrew-pasty](https://github.com/markoboskoauroville/homebrew-pasty) |
| Also called | Pasty tap, Cascade, FKeys, Pasty |
| Visibility | public |
| Kind | config |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Ruby |
| Status | dormant |
| Last push | 2026-08-11 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Install Cascade cask: one-click window cascade per display
- Install FKeys cask: menu-bar toggle between function keys and media keys
- Install Pasty formula: clipboard manager with one board and inline pinning (build from HEAD)

## Ask for it when

- install Pasty clipboard manager
- cascade my windows on a Mac
- switch function keys to media keys
- brew tap markoboskoauroville/pasty

## How to control it

No control API found.

Example:

```
brew install --cask markoboskoauroville/pasty/cascade
```

Evidence: README.md; Casks/cascade.rb, Casks/fkeys.rb, Formula/pasty.rb

## Inputs / Outputs

Outputs:

- installed Mac apps

## Notes

Only formulas/casks, no app source here. Cascade needs Accessibility permission. See pesty-fork-archive for the Pasty source fork.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/homebrew-pasty/blob/HEAD/README.md)
