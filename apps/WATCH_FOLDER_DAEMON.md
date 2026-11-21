# Watch Folder Daemon

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**launchd daemon plus a global watch command: anything dropped in a folder is pushed to a git repo, with progress and verification.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/WATCH_FOLDER_DAEMON](https://github.com/markoboskoauroville/WATCH_FOLDER_DAEMON) |
| Also called | watch, watch-update |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Python / Shell |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Watch a folder and push new files to a chosen git repo and branch
- Wait until a file stops growing before pushing
- Wake on file events through fswatch with a polling safety net
- Show a menu with progress, last transfers and one-key actions
- Update itself and uninstall cleanly

## Ask for it when

- auto-push files dropped in a folder to GitHub
- upload big renders to a repo automatically

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `watch`
- `watch-update`
- `watch menu keys: P push, T interval, S stop, F folder, L log, U update, Q quit`

Example:

```
watch # menu keys: P push, T interval, S stop, F folder, L log, U update, Q quit
```

More calls:

- update the tool: `watch-update`

Evidence: README.md The menu

## Inputs / Outputs

Inputs:

- a watched folder

Outputs:

- git commits and pushes
- daemon.log

## Code worth reusing

- `bin/worker.py`: settle-then-push worker with remote verification

## Notes

Built for a film repo but generic. Optional fswatch via Homebrew. Touches only ~/.watchfolder, LaunchAgents and /usr/local/bin/watch.

## Docs in the repo

- `README.md`
