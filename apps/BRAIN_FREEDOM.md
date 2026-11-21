# Brain Freedom

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Split-screen studio for making a film by voice: left brain speaks and shows frames, right brain is a real terminal running the coding agent.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAIN_FREEDOM](https://github.com/markoboskoauroville/BRAIN_FREEDOM) |
| Also called | BRAIN FREEDOM, 10sh_brain_freedom |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Web |
| Language | Shell installer, Python (Flask), HTML |
| Status | dormant |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Record voice in the browser, transcribe through AssemblyAI with key fallback, drop text in the composer
- Type the words into the agent character by character (the invisible hand)
- Read any text aloud with word highlighting
- Drop a render: name, optimise, commit, push and put the raw link on the clipboard
- Estimate agent usage from local session logs
- Harvest and sort API keys from any messy file in a key manager

## Ask for it when

- work on the film by voice with the coding agent
- dictate to the coding agent in a terminal
- drop a render and get its raw link

## How to control it

- Level: **http**
- Type: http
- Port: 8770 base, then next free (written to ~/brain_freedom/port)

Actions:

- `GET /api/state`
- `POST /api/config`
- `POST /api/say`
- `POST /api/key`
- `POST /api/restart`
- `POST /api/transcribe`
- `POST /api/image`
- `GET /api/gallery`
- `POST /api/repo`
- `POST /api/push`
- `GET /api/usage`
- `GET /api/errors`
- `POST /api/tts`
- `GET /api/keys`
- `POST /api/keys/import`
- `POST /api/keys/act`
- `GET /api/browsers`
- `GET /api/online`

**Before you call:** The port is 8770 or the next free one, written to ~/brain_freedom/port.

Example:

```
curl -s -XPOST 127.0.0.1:8770/api/say -H 'Content-Type: application/json' -d '{"text":"Good morning"}' # body field names are not in the docs
```

More calls:

- state of the app: `curl -s 127.0.0.1:8770/api/state`
- generated images: `curl -s 127.0.0.1:8770/api/gallery`
- spend so far: `curl -s 127.0.0.1:8770/api/usage`

Evidence: src/bf_server.py (routes at lines 101-673); also embedded in 10sh_brain_freedom_v10_macos.sh

## Inputs / Outputs

Inputs:

- microphone
- dropped image renders
- key files

Outputs:

- transcripts
- committed frames with raw links
- TTS audio

## Code worth reusing

- `src/bf_server.py`: Flask server with pty terminal over websocket, voice transcription with key fallback, image-drop-to-git pipeline, key harvester

## Notes

Base port 8770 clashes with ahkedit's 8770 in the MANTRA_PORTS table; it picks the next free one. Not part of the /health,/api remote-door contract and no token guard was documented. Keys live in ~/.brain_freedom (mode 600). Installed by one script with single-key menu. Built for a dyslexic voice-first director.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/BRAIN_FREEDOM/blob/HEAD/README.md)
