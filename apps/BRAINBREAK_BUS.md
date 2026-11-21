# Brain Brake night bus

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Append-only JSONL message bus between a Claude chat session and Claude Code on the Mac, plus chatlink.py to read and send in the claude.ai tab.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAINBREAK_BUS](https://github.com/markoboskoauroville/BRAINBREAK_BUS) |
| Also called | night bus, chatlink |
| Visibility | public |
| Kind | experiment |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Pass requests, acks, objections and done lines between two sessions through chat.jsonl and code.jsonl
- chatlink.py read: last reply in the claude.ai tab as JSON
- chatlink.py send: type a [MAC] message into the composer and send
- chatlink.py watch: deliver a finished reply to ~/.tspeak/inbox

## Ask for it when

- let the chat Claude and Claude Code talk overnight
- read the claude.ai tab from the Mac
- send a message to the chat session

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `chatlink.py read`
- `chatlink.py send "text"`
- `chatlink.py watch [seconds]`

Example:

```
python3 tools/chatlink.py send "Scene 3 render is done"
```

More calls:

- read the latest messages: `python3 tools/chatlink.py read`
- watch for new messages for 60 seconds: `python3 tools/chatlink.py watch 60`

Evidence: tools/chatlink.py docstring

## Inputs / Outputs

Inputs:

- chat.jsonl
- code.jsonl
- Chrome claude.ai tab

Outputs:

- appended JSON lines
- inbox files for the session monitor

## Works with

- Uses: [CCMC (MANTRA CHAT, the sister of Claude Code)](CCMC.md)
- Used by or talked to by: [CCMC (MANTRA CHAT, the sister of Claude Code)](CCMC.md)

## Code worth reusing

- `tools/chatlink.py`: find the claude.ai tab in Chrome, read the finished reply, send text without moving the mouse

## Notes

Protocol: one writer per file, lines never edited, kinds request/ack/done/object/correct/question/note, a request without done or object is resumed after restart. Written for the Brain Brake night shifts; likely superseded by newer session tooling.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/BRAINBREAK_BUS/blob/HEAD/TAKEOVER.md)
