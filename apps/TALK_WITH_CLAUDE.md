# Talk with Claude Code

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local web page where you press TALK, speak, and Claude answers in text and in the cloned voice with sentence and word highlighted.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TALK_WITH_CLAUDE](https://github.com/markoboskoauroville/TALK_WITH_CLAUDE) |
| Also called | Talk with Claude, talkd |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Record the microphone with a live level bar and a silence gate
- Transcribe with the local ears and drop each message into an inbox folder for Claude Code
- Show Claude replies as cards and speak them with word highlighting
- Toggle the mic from a global shortcut

## Ask for it when

- talk to Claude Code by voice
- speak with the computer and hear the answer

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8835

Actions:

- `GET /health`
- `POST /quit`
- `/reply`
- `talk.py up`
- `talk.py open`
- `talk.py reply`
- `talk.py mic`
- `talk.py inbox`
- `talk.py down`

**Before you call:** Talk with Claude Code (talkd.py) on 8835.

Example:

```
python3 ~/Developer/TALK_WITH_CLAUDE/talk.py reply "..."
```

More calls:

- start the talk window: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py up`
- read the inbox: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py inbox`
- close: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py down`
- health: `curl -s 127.0.0.1:8835/health`

Evidence: talk.py header and talkd.py line 25

## Inputs / Outputs

Inputs:

- microphone

Outputs:

- `inbox/<ms>.json` messages
- spoken replies

## Hardware

- microphone
- speakers

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Notes

Switch lives in MANTRA_STAR apps/talk.lua; state in ~/.talk. Early September design; later voice work moved to MANTRA_VOICE and Voice Engine.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
