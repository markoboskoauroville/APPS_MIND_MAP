# Claude Talkie

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Flask web skin over Claude with microphone input, streamed answers read aloud with word highlighting, a daily quota and one shared login.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Claude_Toki](https://github.com/markoboskoauroville/Claude_Toki) |
| Also called | Claude Toki, Claude Talkie |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | Linux, Web, Cloud |
| Language | Python (Flask), JavaScript |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Chat with Claude with streamed answers
- Dictate by microphone button
- Read answers aloud one sentence at a time with word highlighting
- Choose voice by detected language (Croatian vs other)
- Enforce a daily message quota and keep conversations in a bin
- Serve under a path prefix behind a shared login portal

## Ask for it when

- talk to Claude with a microphone and hear the answer
- read Claude answers aloud with highlighted words

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted (Cloudflare worker path /claude)

Actions:

- `GET /claude/health`
- `POST /claude/api/speech`
- `SSE chat stream (start, delta, done, error)`

**Before you call:** Hosted web service ('Claude Talkie'); the base address is not published in this map.

Example:

```
curl -s <site>/claude/health # also POST /claude/api/speech; the chat stream is server-sent events
```

Evidence: README.md addresses section; HANDOVER.md

## Inputs / Outputs

Inputs:

- microphone audio
- typed messages

Outputs:

- streamed text
- speech clips

## Works with

- Uses: [TTT Portal](TTT_PORTAL.md)
- Used by or talked to by: [Oracle machine notes](oracle_machine.md)

## Code worth reusing

- `static/reader.js`: TokiReader player that lights the current sentence and word from the media clock
- `core.py`: sentence splitting, language detection per sentence, quota arithmetic

## Notes

Part of the second architecture (one login for all apps). Settings read from the portal database.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
