# Queen, Mac app (Groq AI Studio (Mantra))

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Queen's Mac app (Groq AI Studio (Mantra)): chat, status line, and axread, a reader of other apps' accessibility trees; the server is in groq_ai_studio.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GROQ_AI_STUDIO_MAC](https://github.com/markoboskoauroville/GROQ_AI_STUDIO_MAC) |
| Also called | Queen, Groq AI Studio, Grok AI Studio, groq studio mac |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Chat with Queen with streamed answers and saved chats
- Start the Python Queen server if it is down
- Show server status, model, keys and spend
- Read the macOS Accessibility tree of any app as JSON with axread
- Let Queen read WhatsApp Web in Firefox through accessibility
- Ask to update at start

## Ask for it when

- chat with Queen on the Mac
- read the text of a window without screenshots
- check my last WhatsApp messages through accessibility

## How to control it

- Level: **door**
- Type: http, cli, accessibility
- Port: 8765 (Queen server)

**Warning:** port 8765 is also quoted for [Queen auto-update (Groq Auto Update)](groq-auto-update.md), [Queen (Groq AI Studio), server and tools](groq_ai_studio.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `GET /api/app/status`
- `GET /api/chats`
- `POST /api/chats/save`
- `POST /api/chat`
- `POST /api/ax/read`
- `POST /api/whatsapp/ax/latest`
- `axread`

**Before you call:** This repo is the Mac app and the axread command; the Python server on 8765 is in groq_ai_studio and must be running. Fields of /api/ax/read (from the public repo): app, window?, query?, depth?, roles?, max?, timeout?, frames?, focused?.

Example:

```
curl -s -XPOST 127.0.0.1:8765/api/ax/read -H 'X-Queen-Token: <token from the local token file>' -H 'Content-Type: application/json' -d '{"app":"Firefox","query":"WhatsApp"}'
```

More calls:

- the last WhatsApp messages in Firefox: `curl -s -XPOST 127.0.0.1:8765/api/whatsapp/ax/latest -H 'X-Queen-Token: <token>'`
- saved chats: `curl -s 127.0.0.1:8765/api/chats`
- same read from the shell: `axread Firefox`

Evidence: TAKEOVER.md; app/Queen.swift

## Inputs / Outputs

Outputs:

- JSON accessibility tree
- chat answers

## Works with

- Uses: [Queen (Groq AI Studio), server and tools](groq_ai_studio.md)

## Code worth reusing

- `axread/main.swift`: command-line reader of the macOS Accessibility tree that outputs JSON

## Notes

The Python server lives in the separate groq_ai_studio repo; this repo is only the Mac app and axread. Built only by GitHub Actions.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
