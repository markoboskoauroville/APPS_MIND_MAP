# MA Reader Speechify module

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Termux read-aloud web app (MA Reader v34) with Edge and Speechify voices, plus a reusable Speechify key ring, key parser and API guide.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MA_READER_SPEECHIFY](https://github.com/markoboskoauroville/MA_READER_SPEECHIFY) |
| Also called | MA Reader Web, Speechify key ring |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android, Termux, Web |
| Language | Shell / Python |
| Status | dormant |
| Last push | 2026-08-10 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Read texts aloud on the phone with the sentence and word highlighted
- Switch between a built-in Edge voice engine and Speechify
- Find many API keys inside a notes file, rotate them and set rejected ones aside
- Show per-key spend from Speechify counts
- Dump the voice catalogue of an account
- Show a standard server screen for terminal Flask servers

## Ask for it when

- use many Speechify keys with rotation
- read text aloud in Croatian or English on the phone
- wire Speechify into another app

## How to control it

- Level: **http**
- Type: http
- Port: 8081

**Warning:** port 8081 is also quoted for [MA Reader Termux / macOS (Edge / Speechify)](MA_READER_TERMUX_MACOS.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /api/voices`
- `GET /api/langs`
- `GET/POST /api/state`
- `POST /api/prepare`
- `GET /api/library`
- `GET /api/library/<tid>`
- `POST /api/library/<tid>/delete`
- `POST /api/library/delete_bulk`
- `POST /api/library/delete_all`
- `GET /api/audio/<tid>/<vkey>/<idx>.mp3`
- `GET /api/bounds/<tid>/<vkey>/<idx>`

**Before you call:** Termux read-aloud web app (v34) with Edge and Speechify voices; routes were read from the v26 installer script and v34 has not yet run on the phone.

Example:

```
curl http://localhost:8081/api/voices
```

More calls:

- list languages: `curl -s 127.0.0.1:8081/api/langs`
- the saved texts: `curl -s 127.0.0.1:8081/api/library`
- prepare a text for reading (body fields not in the docs): `curl -s -XPOST 127.0.0.1:8081/api/prepare -H 'Content-Type: application/json' -d '{"text":"Dobar dan","lang":"hr"}'`

Evidence: 26sh_i_ma_reader_v26_termux.sh lines 2095-2181 (routes), line 231 (port 8081)

## Inputs / Outputs

Inputs:

- text
- Speechify keys

Outputs:

- mp3 audio
- word timings

## Works with

- Used by or talked to by: [CCMC (MANTRA CHAT, the sister of Claude Code)](CCMC.md), [DaVinci Grading Tutorial (Mantra)](RESOLVE_GRADING_TUTORIAL.md), [Sample Player, Android](SAMPLE_PLAYER.md)

## Code worth reusing

- `speechify_keyring.py`: key ring, parser, rotation and tester
- `speechify_routes.py`: reference Flask routes for Speechify
- `server_screen.py`: standard terminal screen for Flask servers
- `SPEECHIFY_API_GUIDE.md`: endpoints, paging, models, speech marks, errors

## Notes

Routes were read from the v26 installer script; v34 is the current version and has not yet run on the phone. Key files are never in git.

## Docs in the repo

- `README.md`
