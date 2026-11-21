# MAI Worker (maiwork)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**maiwork: hands a task from any Claude Code session or script to the Copilot agent (MAI Code 2) running in VS Code and prints the answer on stdout.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MAI_WORKER](https://github.com/markoboskoauroville/MAI_WORKER) |
| Also called | maiwork, MAI Code 2 worker, MAI Code worker |
| Visibility | public |
| Kind | cli-tool |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Send a task to the VS Code agent host over its Unix-socket WebSocket (AHP, JSON-RPC)
- Choose model mai-code-2 or mai-code-2-flash
- Set working folder, timeout and approval mode (all/assisted/manual)
- Print final answer, or JSON with model, session, seconds and tools used
- Report agent status (maiwork status)

## Ask for it when

- delegate a task to the Copilot agent in VS Code
- let MAI Code 2 write a macro
- run a worker agent from a script
- ask VS Code's agent and get the answer on stdout

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `maiwork "<task>"`
- `maiwork status`
- `--cwd`
- `--model`
- `--timeout`
- `--approve all|assisted|manual`
- `--json`
- `--debug`
- `maiwork - (task from stdin)`

**Before you call:** Run inside a checkout; --approve all|assisted|manual sets how much it may do alone.

Example:

```
maiwork "<task>" --cwd ~/Developer/SOMETHING --model mai-code-2
```

More calls:

- task from standard input as JSON: `echo "fix the failing test" | maiwork - --cwd ~/Developer/SOMETHING --json`
- status: `maiwork status`

Evidence: TAKEOVER.md Use section; maiwork.py argparse line 244

## Inputs / Outputs

Inputs:

- task text

Outputs:

- agent answer on stdout
- VS Code session

## Works with

- Talks to: [Macro Recorder (Mantra)](MANTRA_MACRO.md)
- Used by or talked to by: [Macro Recorder (Mantra)](MANTRA_MACRO.md)

## Code worth reusing

- `maiwork.py`: AHP client: JSON-RPC over a Unix-socket WebSocket to VS Code's agent host

## Notes

Needs VS Code running (exit 3 otherwise) and the websockets package. Default approval is Allow all: the agent edits files and runs shell commands without asking. Connection token is read from VS Code's local endpoint file, never printed.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MAI_WORKER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MAI_WORKER/blob/HEAD/LESSONS.md)
