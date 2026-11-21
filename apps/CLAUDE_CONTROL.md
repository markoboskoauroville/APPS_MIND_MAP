# Claude Control (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Menu-bar play/pause for everything Claude Code runs on the Mac: stops Claude process trees and tools, resumes them, shows RUNNING or PAUSED.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLAUDE_CONTROL](https://github.com/markoboskoauroville/CLAUDE_CONTROL) |
| Also called | Claude Control, claudectl, pause all |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v4 |
| Control level | cli (command line or script only) |

## What it can do

- Pause all Claude Code sessions with their child processes (SIGSTOP, deepest first)
- Resume all (SIGCONT, parents first)
- Call each registered tool's own pause API first (Macro Recorder, Queen)
- Show session and tool states in a menu
- Warn after 10 minutes paused
- Start from a SessionStart hook and quit 60 s after the last session ends

## Ask for it when

- pause everything Claude is doing
- stop all Claude agents now
- resume Claude sessions
- freeze Claude Code to save money or CPU

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `claudectl pause`
- `claudectl resume`
- `claudectl status`

**Before you call:** Tools register in ~/.config/claude-control/tools.json (pause, resume, status routes); it never stops itself, the process on :8837, Macro Recorder, Talk Mode, Voice to Text, Firefox, Tailscale or Connection Keeper.

Example:

```
claudectl pause # pauses every registered tool with background work or API calls
```

More calls:

- continue all work: `claudectl resume`
- what is paused: `claudectl status`

Evidence: TAKEOVER.md (CLI section)

## Inputs / Outputs

Inputs:

- ps process list
- ~/.config/claude-control/tools.json

Outputs:

- paused.json state
- menu-bar band

## Works with

- Talks to: [Macro Recorder (Mantra)](MANTRA_MACRO.md)

## Code worth reusing

- `app/Core.swift`: find Claude Code process roots and trees from ps, SIGSTOP/SIGCONT them safely, protect named processes
- `app/StatusBand.swift`: green/amber/grey menu-bar band

## Notes

Never stops itself, claudectl, the process on :8837, Macro Recorder, Talk Mode, Voice to Text, Firefox, Tailscale, Connection Keeper, Hammerspoon or chatd.py. Starts only from a hook, not at login. Public but unpromoted (no README).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/CLAUDE_CONTROL/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/CLAUDE_CONTROL/blob/HEAD/LESSONS.md)
