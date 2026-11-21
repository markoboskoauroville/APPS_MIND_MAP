# Claude Code Monitor (Mantra) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Archived on GitHub.

**Swift Mac window listing every open Claude Code session with its state and buttons to go to, topic, summarize or close it.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLAUDE_CODE_MONITOR](https://github.com/markoboskoauroville/CLAUDE_CODE_MONITOR) |
| Also called | Claude Code Monitor, claudemon |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-11-07 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | none (no control api found) |

## What it can do

- List every Claude Code session with name, topic, current state, folder and last prompt
- Bring a session's iTerm tab to the front
- Set a session topic
- Type summarize or close-the-session into a session
- Turn the naming hook in Claude settings on or off

## Ask for it when

- see all my Claude Code sessions
- switch to a particular Claude session
- close all finished Claude sessions

## How to control it

No control API found.

Evidence: none found; app reads data from the hub script other_sessions.py

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Claude Code hub](claude-code.md)

## Notes

Archived on GitHub. Built only by GitHub Actions. Needs the hub repo cloned on the Mac. RETIRED/SUPERSEDED: no replacement is named in the docs. A current tool that shows live sessions is AGENT_MANAGER (not stated as its replacement).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
