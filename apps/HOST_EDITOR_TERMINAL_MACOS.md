# Host Editor Terminal

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Curses terminal tool to view, filter and prune /etc/hosts on macOS with Blocked and Allowed tabs and atomic writes.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/HOST_EDITOR_TERMINAL_MACOS](https://github.com/markoboskoauroville/HOST_EDITOR_TERMINAL_MACOS) |
| Also called | Host Editor, hosts editor |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Python (curses, standard library) |
| Status | active |
| Last push | 2026-08-22 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Split hosts entries into BLOCKED and ALLOWED tabs as an exact partition
- Filter entries as you type
- Delete any line with atomic writes
- Run on a copy via the HOSTS_FILE variable for safe tests

## Ask for it when

- edit the hosts file
- see which domains are blocked in hosts
- remove a blocked entry from hosts

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `sudo python3 host.py`
- `HOSTS_FILE=<path> python3 host.py`

**Before you call:** Needs sudo to edit /etc/hosts; `HOSTS_FILE=<path>` tests on a copy.

Example:

```
sudo python3 host.py
```

More calls:

- on a copy of the hosts file: `HOSTS_FILE=/tmp/hosts python3 host.py`

Evidence: README.md

## Inputs / Outputs

Inputs:

- /etc/hosts

Outputs:

- edited hosts file

## Notes

Interactive TUI, not scriptable beyond the HOSTS_FILE variable. Needs sudo for the real file.

## Docs in the repo

- `README.md`
