# Mantra Bridge

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac server that wraps a persistent Claude Code process per project and streams its events over HTTP (SSE) for a phone chat front end. Only gate 1 of 8 built.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_BRIDGE](https://github.com/markoboskoauroville/MANTRA_BRIDGE) |
| Also called | Claude bridge, phone Claude chat |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Android |
| Language | Python (standard library) |
| Status | dormant |
| Last push | 2026-08-29 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Hold a live Claude Code session per project directory
- Speak NDJSON to Claude Code and expose the parsed event stream over HTTP using SSE with replay by Last-Event-ID
- Authenticate with a bearer token shown once as a QR code
- Reach the Mac only over loopback or Tailscale

## Ask for it when

- drive Claude Code on the Mac from the phone
- stream a Claude Code session over HTTP

## How to control it

- Level: **http**
- Type: http
- Port: not stated in the docs (set by --project run in mac/)

Actions:

- `GET /health`
- `SSE event stream`
- `POST messages (see mac/bridge/server.py)`

**Before you call:** Run in mac/ of the repo; the message routes are in mac/bridge/server.py (not harvested).

Example:

```
python3 -m bridge.server --project ~/Developer/SOME_REPO # run in mac/; then GET /health and the SSE stream
```

Evidence: README.md; mac/bridge/server.py line 96

## Code worth reusing

- `mac/bridge/httpd.py`: standard-library HTTP server with SSE and Last-Event-ID replay
- `mac/bridge/session.py`: persistent Claude Code subprocess wrapper reading NDJSON events

## Notes

No Android app yet; only the Mac server (gate 1). Only /health route is evidenced in the harvested grep; other routes are in server.py.

## Docs in the repo

- `README.md`
