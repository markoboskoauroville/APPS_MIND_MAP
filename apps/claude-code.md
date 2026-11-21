# Claude Code hub

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Hub repo: journal of every Claude Code session, handover of every project, code index, and every program as a git submodule.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/claude-code](https://github.com/markoboskoauroville/claude-code) |
| Also called | the hub, handover hub, everything built with Claude Code |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python, Markdown |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Print or speak a handover report of where work stopped (handover.py brief / say), run by a SessionStart hook
- Keep the INDEX of every program: what it is, where it runs, how it starts
- Keep a dated journal of each session in SESSIONS/
- Point to every program repo as a submodule at the commit current when the journal was written
- Hold session-start and session-name hooks and settings for Claude Code
- Hold research notes, domain lists and an inbox of cloud-session reports

## Ask for it when

- where did I stop
- what is pending on my projects
- list my projects
- continue project X
- close the session and store the state
- find which repo holds a program

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `handover.py brief`
- `handover.py say`

**Before you call:** Run from a checkout in ~/Developer/claude-code.

Example:

```
python3 ~/Developer/claude-code/handover.py brief
```

More calls:

- speak the handover: `python3 ~/Developer/claude-code/handover.py say`

Evidence: CLAUDE.md, README.md

## Inputs / Outputs

Inputs:

- session reports
- project repos as submodules

Outputs:

- HANDOVER.md
- INDEX.md
- SESSIONS journal
- spoken handover

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Talks to: [Claude Persist](claude-persist.md)
- Used by or talked to by: [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md), [CCMC (MANTRA CHAT, the sister of Claude Code)](CCMC.md), [Claude Code Monitor (Mantra) (retired)](CLAUDE_CODE_MONITOR.md), [Claude Persist](claude-persist.md), [Queen auto-update (Groq Auto Update)](groq-auto-update.md), [Queen (Groq AI Studio), server and tools](groq_ai_studio.md), [Termux Tools](termux-tools.md)

## Code worth reusing

- `handover.py`: prints or speaks the project handover at session start
- `.claude/hooks/cloud_session_name.py`: hook that names a Claude Code cloud session

## Notes

Central documentation hub, not a runnable app. Contains some private case notes and screenshots that must not be published. The speak call goes to the voice service on its known port.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
- `LESSONS.md`
- `CLAUDE.md`
