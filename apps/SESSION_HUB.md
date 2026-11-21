# Session Hub

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac menu bar app and HTTP hub where all of Marko's Claude Code sessions (CLI, phone, cloud) register and message each other; has the hub CLI.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SESSION_HUB](https://github.com/markoboskoauroville/SESSION_HUB) |
| Also called | SESSION HUB (Mantra), session hub, hub |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Cloud |
| Language | Swift |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | http (own http routes) |

## What it can do

- Register Claude Code sessions with name, machine and kind
- Show who is live or offline from heartbeats
- Send text between sessions by name, base name or all
- Deliver messages through inbox pull or an SSE watch stream
- Offer a hub command line (register, who, send, inbox, watch, beat)

## Ask for it when

- message another Claude Code session
- see which Claude sessions are running
- broadcast to all Claude sessions
- session to session chat hub

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8890

**Warning:** port 8890 is also quoted for [Chromium Virtual Machine (Mantra)](vm-chromium.md) - confirm with `mantra-ports scan`.

Actions:

- `POST /register`
- `POST /beat`
- `GET /who`
- `POST /send`
- `GET /inbox`
- `GET /watch (SSE)`
- `hub register`
- `hub who`
- `hub send`
- `hub inbox`
- `hub watch`
- `hub beat`

**Before you call:** Sessions register first: hub register (POST /register {name,sid,machine,kind,cwd}) and keep alive with hub beat; to = a session name, the base name before ' (', a sid prefix, or all; 'marko' reaches the window.

Example:

```
hub send other-session "Please review the diff" # HTTP: curl -s -XPOST 127.0.0.1:8890/send -H 'Content-Type: application/json' -d '{"from":"me","to":"other-session","text":"Please review the diff","id":"m1"}'
```

More calls:

- who is online: `hub who # GET /who`
- read your messages: `hub inbox # GET /inbox?sid=&since=`
- watch the stream live (server-sent events): `hub watch # GET /watch`
- register this session: `hub register`

Evidence: TAKEOVER.md; cli/hub docstring

## Inputs / Outputs

Inputs:

- session registrations and heartbeats
- messages

Outputs:

- delivered messages
- state.json and log.jsonl in Application Support

## Works with

- Talks to: [Session Ack (ccmsg)](SESSION_ACK.md)
- Used by or talked to by: [Session Ack (ccmsg)](SESSION_ACK.md)

## Code worth reusing

- `cli/hub`: stdlib Python client for the hub (works through a SOCKS5 proxy for cloud sessions)
- `app/Server.swift`: Network.framework HTTP plus SSE server for a Swift app

## Notes

Listens on loopback and the Mac's Tailscale address; trust by tailscale whois, no token. Phase 2 ideas (phone sessions registering themselves) not built. Built only by GitHub Actions. Port 8890 here is on the Mac; vm-chromium's vm-agent uses 8890 on the VM, a different machine. For send with delivery confirmation use SESSION_ACK (ccmsg).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SESSION_HUB/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SESSION_HUB/blob/HEAD/LESSONS.md)
