# Free Mac

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Collection of root scripts and small apps that free the Mac from Apple defaults: stay off, block and door-open Apple update servers, system freedom switches.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/FREE_MAC](https://github.com/markoboskoauroville/FREE_MAC) |
| Also called | Free Mac, Apple Door, Freedom |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Shell, Python, Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v3 |
| Control level | cli (command line or script only) |

## What it can do

- Make the laptop stay shut down by setting boot preference
- Block Apple update servers and open a timed door for apps that need them
- Install Command Line Tools from Apple packages when update servers are blocked
- Offer system-wide open-door and close-door commands
- Remove an installed suite with an uninstall script
- Apply a set of system freedom settings (freedom.sh) with a small app

## Ask for it when

- open the Apple update door for 30 minutes
- make the Mac not start when the lid opens
- install command line tools without the update server
- check which Apple servers are blocked

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `stay-off.sh --check`
- `apple-door open|close|status|diagnose|install-clt`
- `open-door`
- `close-door`
- `freedom.sh`

Example:

```
sudo -n /usr/local/sbin/apple-door open 15m # opens the Apple door (lets Apple services through) for 15 minutes
```

More calls:

- close it again: `sudo -n /usr/local/sbin/apple-door close`
- state: `sudo -n /usr/local/sbin/apple-door status`
- check that the Mac stays off the Apple services: `stay-off.sh --check`

Evidence: README.md apple-door.sh section

## Works with

- Uses: [App Store (Mantra)](APP_STORE.md), [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `apple-door.sh`: timed hosts-file door with a root copy and a sudoers rule so apps can open it without a password

## Notes

Requires System Integrity Protection off by the owner's choice. Privileged scripts; read before running.

## Docs in the repo

- `README.md`
- `CLAUDE.md`
