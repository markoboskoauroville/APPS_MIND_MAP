# Agent Manager (CEO) (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac window and phone door showing every running Claude Code session, agent, worker and blocker across the Mac, chromium-vm and phones.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/AGENT_MANAGER](https://github.com/markoboskoauroville/AGENT_MANAGER) |
| Also called | Agent Manager, CEO view, AGE MGR, agentmgr, Mantra Master |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Swift (+ Python helpers) |
| Status | active |
| Last push | 2026-11-17 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- List running Claude Code sessions per machine, with busy or idle state
- Show background agents and tasks, usage header (5 h session and week)
- Show a WHAT STOPPED ME column of blockers with SOLVE and DONE
- Open a fresh Master session with a hand-over (mantra-master open)
- Serve a phone door so the Android app can read overview and send commands
- Print the same overview as JSON for other sessions (--json)

## Ask for it when

- see what all my Claude sessions are doing
- who is blocked and why
- open the master Claude session
- check Claude usage this week
- pause or message an agent from the phone

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8847 (phone door, Tailscale address only, bearer token)

**Warning:** port 8847 is also quoted for [Find a File Spotlight (Mantra) (retired)](spotlight.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /ping`
- `GET /overview`
- `GET /plans`
- `GET /live`
- `GET /workers`
- `GET /blockers`
- `POST /command {slug,agent,task,action,text}`
- `POST /blocker/solve`
- `POST /blocker/done`
- `AgentManager --json`
- `AgentManager --shot out.png`
- `AgentManager --shot-live out.png`
- `mantra-master open [--dry]`

**Before you call:** Phone-door style, not the /health + /api contract: the door is bound to the Mac's Tailscale address only (not 127.0.0.1), with a bearer token read from a file on the Mac. Read first; actions are written as command files for the master session to carry out.

Example:

```
curl -s -H 'Authorization: Bearer $(cat ~/Downloads/API/agent-manager-token.txt)' http://<mac-tailscale-address>:8847/overview
```

More calls:

- live sessions and workers: `curl -s -H "Authorization: Bearer $TOKEN" http://<mac-tailscale-address>:8847/live ; ... /workers`
- what is blocked: `curl -s -H "Authorization: Bearer $TOKEN" http://<mac-tailscale-address>:8847/blockers`
- tell a session something (fields slug, agent, task, action, text): `curl -s -XPOST -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' http://<mac-tailscale-address>:8847/command -d '{"slug":"MANTRA_ROOM","text":"Run the tests"}'`
- open the Mac window as JSON or a picture: `AgentManager --json ; AgentManager --shot out.png`

Evidence: helper/server.py (path == lines 162-188), LESSONS.md items 15-16, TAKEOVER.md

## Inputs / Outputs

Inputs:

- ~/.mantra-os plans and commands
- ps and task output files of Claude Code
- adb devices
- tailscale status

Outputs:

- overview JSON
- command files in `~/.mantra-os/commands/<slug>/`

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md), [Star (Mantra), Swift menu](STAR_SWIFT.md)
- Talks to: [Agent Manager (CEO) (Mantra) for Android](AGENT_MANAGER_ANDROID.md), [Claude Code hub](claude-code.md), [Chromium Virtual Machine (Mantra)](vm-chromium.md)
- Used by or talked to by: [Agent Manager (CEO) (Mantra) for Android](AGENT_MANAGER_ANDROID.md)

## Code worth reusing

- `helper/collect.py`: collects Claude Code sessions, tasks, VM services and phones with timeouts; prints text or JSON
- `helper/server.py`: stdlib HTTP door bound to Tailscale address with bearer token re-read on every request
- `helper/mantra_master.py`: command that writes the hand-over STATE.md and opens a Master session

## Notes

Door is bound only to the Mac's Tailscale address, never 0.0.0.0; token is a file on the Mac. This is the older phone-door style, not the generic /health,/api remote-door contract. Read-only first; actions are written as command files for the master session to execute. Allowed values of action in POST /command are not described in the harvested docs. Port 8847 was also used by the retired spotlight (Find a File Spotlight); only AGENT_MANAGER is current.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/AGENT_MANAGER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/AGENT_MANAGER/blob/HEAD/LESSONS.md)
