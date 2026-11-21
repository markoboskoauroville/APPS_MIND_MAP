# Claude Persist

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Resumes a Claude Code session that stopped on an API error every 10 seconds, and restarts it when the quota resets.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/claude-persist](https://github.com/markoboskoauroville/claude-persist) |
| Also called | claude persist, claudepersist |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-10-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Record a session in a StopFailure hook when Claude Code gives up on an error
- Resume due sessions with claude -p --resume every 10 seconds via launchd
- Read the quota reset time from the error and restart then
- Skip errors retrying cannot fix and log them for Marko
- Show waiting sessions with the status command

## Ask for it when

- keep Claude Code retrying after a dropped connection
- auto resume a session after quota reset
- see which sessions are waiting

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `fail`
- `ok`
- `tick`
- `status`

**Before you call:** Keeps a Claude Code session alive across stops (ok/fail/tick bookkeeping).

Example:

```
python3 persist.py status
```

More calls:

- mark success / failure / a heartbeat: `python3 persist.py ok ; python3 persist.py fail ; python3 persist.py tick`

Evidence: README.md, persist.py

## Inputs / Outputs

Inputs:

- Claude Code Stop and StopFailure hook JSON

Outputs:

- session state files
- PERSIST.md log

## Works with

- Talks to: [Claude Code hub](claude-code.md)
- Used by or talked to by: [Claude Code hub](claude-code.md)

## Code worth reusing

- `persist.py`: hook-driven retry and resume scheduler for Claude Code sessions

## Notes

Single file persist.py with launchd plist (10 s interval); a running resume is never started twice.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
