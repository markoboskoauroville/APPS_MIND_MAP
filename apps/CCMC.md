# CCMC (MANTRA CHAT, the sister of Claude Code)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local chat page that mirrors every Claude Code session as cards, reads answers aloud with Speechify, takes voice and typed input back into the session.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CCMC](https://github.com/markoboskoauroville/CCMC) |
| Also called | MANTRA CHAT, Sister, chatd, tspeak |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Web |
| Language | Python (Flask) |
| Status | dormant |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Mirror each prompt and answer of a Claude Code session as cards on a local page
- READ an answer aloud sentence by sentence in a floating window with the spoken word lit
- Send what is typed or dictated on the page into the session through an inbox
- Transcribe voice recorded in the browser (/api/hear)
- Open claude.ai in a side pane at the golden section
- Install hooks (SessionStart, UserPromptSubmit, Stop) into ~/.claude/settings.json

## Ask for it when

- read Claude's answer aloud
- mirror my Claude Code session on a web page
- talk to Claude Code through a page
- speak the last answer with Beatrice

## How to control it

- Level: **door**
- Type: http
- Port: 8825

Actions:

- `GET /health`
- `POST /api/send`
- `POST /api/hear`
- `POST /api/voice`
- `POST /api/read/<id>`
- `GET /api/read/<id>/plan`
- `GET /api/read/<id>/sent/<n>`
- `POST /api/read/draft/plan`
- `GET /api/messages`
- `POST /api/message`
- `GET /api/events`
- `POST /api/session`
- `POST /api/mirror`
- `POST /api/open`
- `POST /api/pane`
- `POST /api/clear`
- `POST /api/reconnect`

**Before you call:** MANTRA CHAT (chatd.py, Flask) runs when 'Sister' is ticked in the star menu, not by the hook; it binds upward from 8825 and writes the winning port to ~/.tspeak/port.txt. It mirrors the Claude Code session of the open project and opens only in Chrome.

Example:

```
curl -s -XPOST 127.0.0.1:8825/api/send -H 'Content-Type: application/json' -d '{"text":"Yes, go ahead"}' # the answer lands in ~/.tspeak/inbox where the Claude Code session watches
```

More calls:

- add a message to the mirrored chat (role claude|marko|system): `curl -s -XPOST 127.0.0.1:8825/api/message -H 'Content-Type: application/json' -d '{"role":"system","text":"Build finished","project":"MANTRA_ROOM"}'`
- read all messages since an id: `curl -s '127.0.0.1:8825/api/messages?since=0'`
- speak a message and get audio clips plus sentences: `curl -s -XPOST 127.0.0.1:8825/api/read/<message-id> -H 'Content-Type: application/json' -d '{"speed":1.0}'`
- recording from the browser to text and sent to the session as typed: `curl -s -XPOST '127.0.0.1:8825/api/hear?send=1' --data-binary @take.webm`

Evidence: api.txt, TAKEOVER.md lines 61-235, CLAUDE.md

## Inputs / Outputs

Inputs:

- Claude Code hooks and transcripts
- microphone (browser)

Outputs:

- cards
- spoken audio
- ~/.tspeak/inbox messages

## Works with

- Uses: [MA Reader Speechify module](MA_READER_SPEECHIFY.md)
- Talks to: [Brain Brake night bus](BRAINBREAK_BUS.md), [Claude Code hub](claude-code.md)
- Used by or talked to by: [Brain Brake night bus](BRAINBREAK_BUS.md)

## Code worth reusing

- `ring.py`: key ring with fingerprints only and fallback between keys
- `speechify.py`: Speechify client with one-sentence cache
- `chat_hook.py`: Claude Code SessionStart/UserPromptSubmit/Stop hook that feeds the chat page
- `voice.py`: browser recording to ffmpeg to Whisper path

## Notes

CLAUDE.md is addressed to Claude Code: she is started by ticking Sister in the star menu, never by the hook. Paths in docs are hard-coded to Marko's home. Opens only in Chrome. Needs a Speechify key file with label lines. Master branch exists but is not ahead. Routes and fields checked in chatd.py of the public repo.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/CCMC/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/CCMC/blob/HEAD/LESSONS.md)
- [CLAUDE.md](https://github.com/markoboskoauroville/CCMC/blob/HEAD/CLAUDE.md)
