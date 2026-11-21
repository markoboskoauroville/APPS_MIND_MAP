# TTT Portal

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Login door on Cloudflare Pages plus a Flask portal on a cloud machine: users, admin panel, API keys and an HTTP API for transcription and speech.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TTT_PORTAL](https://github.com/markoboskoauroville/TTT_PORTAL) |
| Also called | TTT-LLL portal, door |
| Visibility | private (code not readable without access) |
| Kind | website |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | Linux, Web, Cloud |
| Language | Python / JavaScript |
| Status | dormant |
| Last push | 2026-10-29 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Verify session cookies at the edge and route to a portal or the transcribe app
- Manage users and logins with hashed passwords in an admin panel
- Issue and revoke API keys, counting calls
- Offer transcription, speech and voices endpoints on offline engines

## Ask for it when

- give other apps an API for transcription and speech
- add or remove a portal user
- put a login in front of an app

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted (portal URL is not published in this map)

Actions:

- `POST /api/v1/transcribe`
- `POST /api/v1/speech`
- `GET /api/v1/voices`

**Before you call:** An account and API key from the portal admin (the key is issued per user, never stored in git); the portal-url is a hosted address kept out of this map.

Example:

```
curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe
```

More calls:

- text to speech with the Piper engine: `curl -s -H "Authorization: Bearer <api-key>" -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' <portal-url>/api/v1/speech -o out.wav # body fields not in the docs`
- list voices: `curl -s -H "Authorization: Bearer <api-key>" <portal-url>/api/v1/voices`

Evidence: README.md The API, for other apps; portal.py

## Inputs / Outputs

Inputs:

- audio files
- text

Outputs:

- transcripts
- wav speech

## Works with

- Uses: [Maha Transcribe / TTT-LLL (Streamlit)](MAHA_TRANSCRIBE_STREAMLIT.md)
- Used by or talked to by: [Claude Talkie](Claude_Toki.md), [Maha Transcribe Flask](MAHA_TRANSCRIBE_FLASK.md), [Oracle machine notes](oracle_machine.md)

## Code worth reusing

- `portal.py`: accounts with salted scrypt, signed session tokens, admin panel and API keys
- `pages/functions/_middleware.js`: edge session check with HMAC and routing

## Notes

Secrets live as Pages secrets and on the machine, never in git. Whisper small and Piper are the engines on the cloud machine; cloned voices were a planned next step. Hostnames and keys left out.

## Docs in the repo

- `README.md`
