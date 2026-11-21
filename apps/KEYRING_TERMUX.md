# Keyring

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Key vault on the phone: finds API keys by shape in notes, tests them for real, exports one format, serves them to apps via 'keyring get'.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/KEYRING_TERMUX](https://github.com/markoboskoauroville/KEYRING_TERMUX) |
| Also called | KEYRING, key repository, key vault, Keyring Termux |
| Visibility | public |
| Kind | service-daemon |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | Android, Termux |
| Language | Python (Flask) |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Import API keys by shape from notes, files or folders
- Test each key with the smallest real work call and label it works/valid/etc
- Store keys in a local vault with masked listing
- Print one key value for scripts with 'keyring get `<provider>'`
- Export keys in the 'keyring v1' format
- Serve a local web page and JSON API on loopback
- Self-update from GitHub

## Ask for it when

- get an API key for a provider in a script
- check which of my API keys still work and have credit
- collect all API keys from my notes into one place
- export my keys in one standard file

## How to control it

- Level: **door**
- Type: http, cli
- Port: 8842 (8842-8857, then any free)

Actions:

- `GET /health`
- `GET /api/keys`
- `POST /api/keys/<id>`
- `DELETE /api/keys/<id>`
- `POST /api/keys/<id>/reveal`
- `POST /api/keys/<id>/test`
- `POST /api/import`
- `POST /api/import-folder`
- `POST /api/export`
- `GET /api/log`
- `CLI: keyring get <provider>`
- `CLI: keyring secret <provider>`
- `CLI: keyring list [provider]`
- `CLI: keyring import <file|dir>`
- `CLI: keyring export out.txt [provider]`
- `CLI: keyring test <provider|all>`
- `CLI: keyring update`

**Before you call:** Run on the phone in Termux (loopback only; vault in ~/.keyring, mode 0600); HTTP page on 8842, up to 8857. Only `/api/keys/<id>/reveal` returns a value.

Example:

```
keyring get groq # prints one working key value for the provider on stdout; use as $(keyring get groq)
```

More calls:

- list providers and key counts: `keyring list`
- test every key: `keyring test all`
- import a notes file of keys: `keyring import ~/Downloads/keys.txt`
- health: `curl -s 127.0.0.1:8842/health`

Evidence: app.py routes (lines 82-249); README.md command table

## Inputs / Outputs

Inputs:

- notes and text files containing keys
- keyring v1 files

Outputs:

- key values on stdout
- keyring v1 export file
- state log (fingerprints only)

## Works with

- Uses: [Maha Transcribe (Termux/terminal)](MAHA_TRANSCRIBE_TERMUX_TERMINAL.md)
- Talks to: [Store & Pool Finder](SHOP_FINDER.md)
- Used by or talked to by: [Cockpit Termux](COCKPIT_TERMUX.md), [Maha Commute](MAHA_COMMUTE.md), [MA Reader Termux / macOS (Edge / Speechify)](MA_READER_TERMUX_MACOS.md), [Oxi Controller (E16 Remote)](oxi-controller.md), [ZET Strike](zet_strike.md)

## Code worth reusing

- `localguard.py`: loopback-only guard with three checks on every /api call
- `portpick.py`: pick a free port in a range
- `selfupdate.py`: pull newest version from GitHub and restart
- `probes.py`: real provider key tests (smallest work call per provider)
- `console.py`: terminal console helper

## Notes

Loopback only; the vault lives in ~/.keyring (0600). Only `/api/keys/<id>/reveal` returns a value. Gates in gates/run_gates.py.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/KEYRING_TERMUX/blob/HEAD/README.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/KEYRING_TERMUX/blob/HEAD/HANDOVER.md)
