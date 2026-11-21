# Oracle machine notes

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Working notes for the free Oracle cloud machine that hosts transcription, speech and tool web services behind a Cloudflare door.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/oracle_machine](https://github.com/markoboskoauroville/oracle_machine) |
| Also called | teacher-vm, oracle machine, free Oracle VM |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | Linux, Cloud |
| Language | Markdown |
| Status | active |
| Last push | 2026-11-02 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Document how a session reaches the machine through the Mac's Remote Control session
- Describe the services on it: portal with API, transcription pages, Claude web terminal view, shop finder
- List the transcription and speech API endpoints
- Record lessons and standing rules (work on main, times in Croatian time, no secrets in the repo)

## Ask for it when

- where does the cloud transcription service run
- how do I reach the Oracle machine
- what ports and routes does the cloud machine serve

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted behind a Cloudflare door

Actions:

- `/api/v1/transcribe`
- `/api/v1/transcribe/chunk`
- `/api/v1/speech`
- `/api/v1/speech/stream`
- `/api/v1/voices`
- `/portal/api/health`
- `/portal/api/docs`

**Before you call:** This repo is documentation of the machine; the service code is elsewhere (see TTT_PORTAL). `<portal-url>` and keys are the owner's.

Example:

```
curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe # same API as TTT_PORTAL
```

More calls:

- health: `curl -s <portal-url>/portal/api/health`
- voices: `curl -s -H "Authorization: Bearer <api-key>" <portal-url>/api/v1/voices`

Evidence: manifest/lessonsarehere.md (described there; the service itself is not in this repo)

## Works with

- Uses: [Claude Talkie](Claude_Toki.md), [Store & Pool Finder](SHOP_FINDER.md), [TTT Portal](TTT_PORTAL.md)

## Notes

Documentation repo only; the service code lives elsewhere. Only parts of the main notes file were harvested. Secrets are never stored here, only file paths.

## Docs in the repo

- `CLAUDE.md`
