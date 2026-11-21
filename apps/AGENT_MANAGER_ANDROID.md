# Agent Manager (CEO) (Mantra) for Android

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Phone view of the Agent Manager: usage, running agents, blockers with SOLVE/DONE, plan cards, and PAUSE/STOP/MESSAGE per task, over Tailscale.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/AGENT_MANAGER_ANDROID](https://github.com/markoboskoauroville/AGENT_MANAGER_ANDROID) |
| Also called | Agent Manager Android, AGE MGR phone, CEO status on phone |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | Android |
| Language | Kotlin (Compose) |
| Status | active |
| Last push | 2026-11-10 |
| Build / release | GitHub workflow: yes; latest release: v7 |
| Control level | none (no control api found) |

## What it can do

- Show usage header (session and week), running sessions and agents
- Show blockers and press SOLVE or DONE
- Show Session Manager plan cards with progress and a reply box
- Send PAUSE, STOP or MESSAGE to a task
- List sessions per device
- Refresh every 5 s while open

## Ask for it when

- check my Claude agents from the phone
- answer a blocked agent from the phone
- stop a running task from the phone

## How to control it

No control API found.

Evidence: app is only a client of the AGENT_MANAGER door (Api.kt, port 8847); it serves nothing

## Inputs / Outputs

Inputs:

- Mac door GET /overview, /plans, /blockers

Outputs:

- POST /command, /blocker/solve, /blocker/done to the Mac

## Works with

- Uses: [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md)
- Used by or talked to by: [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md)

## Notes

Needs Tailscale on the phone and the Mac address and token typed in Settings or passed by adb (am start ... --es address ... --es token ...). Version label upper right opens the latest release. Parity rule: every Mac feature is mirrored here.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/AGENT_MANAGER_ANDROID/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/AGENT_MANAGER_ANDROID/blob/HEAD/LESSONS.md)
