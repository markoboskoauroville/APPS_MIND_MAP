# TP - Terminal Properties

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local Flask editor for shell shortcuts: search every command, give it a short name, apply; refuses to shadow a real command.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TERMINAL_SHORTCUT_MACOS](https://github.com/markoboskoauroville/TERMINAL_SHORTCUT_MACOS) |
| Also called | tp, Terminal Shortcut |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-08-24 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Scan PATH and zsh builtins and search them
- Read manual-page summaries on demand
- Create aliases or functions (when the command uses $1 or $@)
- Warn on recursive-delete commands and refuse real command names
- Toggle shortcuts off without deleting, and restore the original shell file

## Ask for it when

- make a short alias for a terminal command
- type c to clear the terminal

## How to control it

- Level: **http**
- Type: http, cli
- Port: 5077

Actions:

- `GET /api/search`
- `GET /api/check`
- `POST /api/toggle`
- `POST /api/delete`
- `POST /api/apply`
- `/api/describe`
- `tp`

**Before you call:** TP (Terminal Properties) server on 5077.

Example:

```
curl 'http://127.0.0.1:5077/api/search?q=clear'
```

More calls:

- check a shortcut: `curl -s '127.0.0.1:5077/api/check'`

Evidence: static/app.js lines 64-173; HANDOFF.md

## Inputs / Outputs

Inputs:

- commands on PATH

Outputs:

- ~/.tp/shortcuts.json and tp.zsh

## Code worth reusing

- `shell.py`: generate the guarded zsh include and marker block
- `naming.py`: shortname rules and conflict classification
- `localguard.py`: guard so only local browser requests pass

## Notes

Only three marked lines are added to .zshrc; a dated backup is made before any edit. Has a gate script and tests.

## Docs in the repo

- `README.md`
