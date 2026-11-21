# Claude Code for Termux

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One-command installer for Claude Code on an Android phone through Termux: patched native binary or proot-Ubuntu.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLAUDE_CODE_TERMUX](https://github.com/markoboskoauroville/CLAUDE_CODE_TERMUX) |
| Also called | cct, Claude Code Termux |
| Visibility | public |
| Kind | cli-tool |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Shell |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Install Claude Code on aarch64 Android via --proot (proven) or --native (experimental)
- Print a dependency table and numbered steps with progress bars
- Uninstall cleanly
- Run four-test and delivery-gate suites for the installer

## Ask for it when

- install Claude Code on my phone
- run Claude Code in Termux
- set up Claude on Android

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `bash cct.sh`
- `bash cct.sh --native`
- `bash cct.sh --proot`
- `bash cct.sh --yes`
- `uninstall.sh`

**Before you call:** Run inside Termux; --proot installs Claude Code in a Linux proot, --native without it.

Example:

```
curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/CLAUDE_CODE_TERMUX/main/install.sh -o cct.sh && bash cct.sh --proot
```

More calls:

- native install without questions: `bash cct.sh --native --yes`
- remove it: `bash uninstall.sh`

Evidence: README.md, install.sh

## Inputs / Outputs

Inputs:

- Termux on 64-bit ARM Android
- paid Claude plan or API key

Outputs:

- claude command in Termux

## Code worth reusing

- `tests/lib.sh`: shell four-test harness (mechanism, real, ugly, upgrade) for installers

## Notes

Termux must come from F-Droid or GitHub, not Google Play. --native installed but segfaulted on a Nothing Phone 2a with Claude Code 2.1.301; --proot works (about 2.5 GB). Hundreds of phantom processes hurt Termux: see COCKPIT_TERMUX for lifting the limit.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/CLAUDE_CODE_TERMUX/blob/HEAD/README.md)
