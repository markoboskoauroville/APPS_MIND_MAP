# Mantra Router

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Claude Code mod: a small model judges each prompt and suggests Haiku, Sonnet or Opus; you confirm and it learns from corrections.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_ROUTER](https://github.com/markoboskoauroville/MANTRA_ROUTER) |
| Also called | model router, gatekeeper router |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Android, Termux, Linux |
| Language | TypeScript |
| Status | dormant |
| Last push | 2026-11-17 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Ask a small model which Claude model fits a prompt before it is sent
- Switch the whole turn to the chosen model
- Run in gate, auto or off modes
- Learn from your picks and from suspect turns, storing lessons per device
- Write a routing log and daily review reports to the repo

## Ask for it when

- choose the right Claude model for a prompt
- route prompts between Haiku Sonnet and Opus
- bypass the router

## How to control it

No control API found. The catalog notes some code-level hooks only.

Actions:

- `/router on`
- `/router gate`
- `/router auto`
- `/router off`
- `/router wrong <model> [why]`

Example:

```
/router auto
```

Evidence: README.md (slash commands in a Claude Code session)

## Inputs / Outputs

Inputs:

- user prompts in Claude Code

Outputs:

- model choice
- `learned/<device>.jsonl`
- `data/<device>/events-*.jsonl`
- reviews/*.md

## Code worth reusing

- `mod/hooks/judge.ts`: prompt to model judgement
- `mod/hooks/register.tsx`: Claude Code mod registration with the band UI

## Notes

OFF since 14.11.2026: the main Opus session now picks each worker model. Controlled only by slash commands inside Claude Code, no HTTP API.

## Docs in the repo

- `README.md`
