# TOML key merger

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Termux + Flask tool, loopback only, that merges an exported key file into a TOML secrets file on the phone so keys are never pasted into a chat.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TOML](https://github.com/markoboskoauroville/TOML) |
| Also called | toml-termux, TOML merger |
| Visibility | public |
| Kind | app |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | Android, Termux |
| Language | Python |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Pick a secrets file and an exported key file on the phone
- Parse and merge the keys into TOML (for Streamlit secrets)
- Reveal and copy the result
- Stay on loopback with a guard against background requests from other tabs

## Ask for it when

- merge API keys into a secrets.toml on the phone
- format keys as TOML without pasting them
- Streamlit secrets from an exported key file

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8099

Actions:

- `GET /api/ls`
- `POST /api/merge`
- `POST /api/reveal`
- `POST /api/quit`
- `toml-termux.sh`

Example:

```
curl -s http://127.0.0.1:8099/api/ls # started on the phone by toml-termux.sh; the page opens in the phone browser
```

More calls:

- merge: `curl -s -XPOST http://127.0.0.1:8099/api/merge`

Evidence: server.py lines 147, 197, 236, 243; README.md

## Inputs / Outputs

Inputs:

- exported key file
- existing secrets file

Outputs:

- merged TOML text

## Code worth reusing

- `parsers.py`: parses several exported key-file formats
- `merge.py`: merges keys into a TOML secrets file
- `guard.py`: loopback guard against cross-tab requests to a local server
- `portpick.py`: free port picker

## Notes

Handles secrets, so the tool never prints values to chat. See WHAT_IS_NOT_TESTED.md. Version 4 per README.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/TOML/blob/HEAD/README.md)
