# Claude Code Session Names

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Claude Code SessionStart hook/plugin that names each session by place, day counter and date, e.g. mac1_14-11, pixel1_15-11, cloud7k_14-11.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/claude-code-session-names](https://github.com/markoboskoauroville/claude-code-session-names) |
| Also called | session names plugin, session-names |
| Visibility | public |
| Kind | cli-tool |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Termux, Linux, Cloud |
| Language | Python |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Names every Claude Code session place+number+date via a SessionStart hook answering sessionTitle
- Keeps one locked counter per place and day so parallel tabs never collide
- Keeps the name on resume or compact, takes the next number on /clear
- Installs as a Claude Code plugin or as a plain hook in settings.json via install.sh

## Ask for it when

- name my Claude Code sessions automatically
- tell Mac and phone Claude sessions apart
- install the session name hook

## How to control it

No control API found.

Example:

```
curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/claude-code-session-names/main/install.sh | bash -s -- mac
```

Evidence: TAKEOVER.md (install section), install.sh, hooks/hooks.json

## Inputs / Outputs

Outputs:

- session title JSON for the hook
- counters in ~/.claude/session-names/

## Code worth reusing

- `session_name.py`: Stdlib-only locked per-day counter and Claude Code hook that returns sessionTitle

## Notes

Install tool, not an app to call at runtime. No README; docs are in TAKEOVER.md (former README).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/claude-code-session-names/blob/HEAD/TAKEOVER.md)
