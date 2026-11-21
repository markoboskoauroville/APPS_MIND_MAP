# Session Ack (ccmsg)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Receipt protocol and mailbox service for messages between Claude Code sessions: sent, delivered, read, done, with the ccmsg CLI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SESSION_ACK](https://github.com/markoboskoauroville/SESSION_ACK) |
| Also called | session-ack, ccmsg, session ack |
| Visibility | public |
| Kind | service-daemon |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Linux, Cloud |
| Language | Python |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Give each message between Claude sessions an id and track its state forward (sent, delivered, read, done/refused/lost)
- Send, resend, wait for and check a message with the ccmsg CLI
- Keep a mailbox (sqlite) so a receiver can pull messages when push fails
- Spool receipts when the mailbox is down and send them later
- Fall back to git-based receipt logs for cloud sessions

## Ask for it when

- confirm that a message between Claude sessions was received
- track message receipts between sessions
- mailbox for Claude Code sessions
- did the other session read my message

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8899 (SESSION_ACK_PORT)

Actions:

- `GET /health`
- `POST /msg`
- `POST /ack`
- `GET /status/<id>`
- `GET /wait/<id>`
- `GET /inbox/<to>`
- `GET /sent/<from>`
- `ccmsg send`
- `ccmsg wait`
- `ccmsg resend`
- `ccmsg status`
- `ccmsg ack`
- `ccmsg inbox`
- `ccmsg flush`
- `ccmsg hook`
- `ccmsg id`

**Before you call:** Listens on loopback and the Mac's Tailscale address; trust by tailscale whois (no token). Address configurable by CCMSG_URL.

Example:

```
ccmsg send <to> "text" then ccmsg wait <id>
```

More calls:

- read your messages: `ccmsg inbox`
- acknowledge: `ccmsg ack <id>`
- status of what you sent: `ccmsg status <id>`
- one sentence over HTTP: `curl -s -XPOST 127.0.0.1:8899/msg -H 'Content-Type: application/json' -d '{"from":"a","to":"b","text":"hi"}'`

Evidence: server/session_ack_server.py docstring; ccmsg.py; TAKEOVER.md

## Inputs / Outputs

Inputs:

- messages between Claude Code sessions
- hook events (PostToolUse, UserPromptSubmit, Stop)

Outputs:

- receipt states per message id
- `ACKS/<id>.log` in the hub repo for cloud sessions

## Hardware

- always-on VM (chromium-vm) reachable over Tailscale

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md), [Session Hub](SESSION_HUB.md)
- Used by or talked to by: [Session Hub](SESSION_HUB.md), [Chromium Virtual Machine (Mantra)](vm-chromium.md)

## Code worth reusing

- `ccmsg.py`: CLI and hook handlers for message ids, receipts, spool and git fallback
- `server/session_ack_server.py`: stdlib HTTP mailbox with sqlite and long-poll wait
- `server/systemd/session-ack.service`: systemd unit for the mailbox

## Notes

Listens on the Tailscale address and loopback only; no token, owner check by tailscale whois. Address configurable by CCMSG_URL. Sister of SESSION_HUB.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SESSION_ACK/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SESSION_ACK/blob/HEAD/LESSONS.md)
