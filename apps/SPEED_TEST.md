# Mantra Speed Test

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Flask page and one-word command that measures a drive's real speed past its cache, reads its health and compares it with 28 popular SSDs.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SPEED_TEST](https://github.com/markoboskoauroville/SPEED_TEST) |
| Also called | speedtest |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-10-19 |
| Build / release | GitHub workflow: no; latest release: v3 |
| Control level | door (standard door) |

## What it can do

- Run big-file, large past-cache, small-files and random 4K tests with uncached writes
- Draw a live gauge and per-second curve
- Read model, bridge chip, link speed and SMART health on internal NVMe
- Compare against a table of 28 drives with sources
- Keep history, cancel a run and eject a drive

## Ask for it when

- test the real speed of an SSD
- check drive health
- compare my drive with others

## How to control it

- Level: **door**
- Type: http, cli
- Port: speedtest (8960+)

Actions:

- `GET /health`
- `GET /api/drives`
- `GET /api/reference`
- `GET /api/history`
- `POST /api/test`
- `GET /api/status`
- `POST /api/cancel`
- `POST /api/eject`

**Before you call:** Mac app; port from MANTRA_PORTS id speedtest (8960 and up).

Example:

```
curl -s -XPOST 127.0.0.1:8960/api/test -H 'Content-Type: application/json' -d '{"drive":"<name from /api/drives>"}' # body field names are not in the docs
```

More calls:

- which drives: `curl -s 127.0.0.1:8960/api/drives`
- progress: `curl -s 127.0.0.1:8960/api/status`
- eject: `curl -s -XPOST 127.0.0.1:8960/api/eject`

Evidence: server.py lines 69-152

## Inputs / Outputs

Inputs:

- a mounted drive

Outputs:

- speed numbers
- history
- web page

## Hardware

- external or internal SSD

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)

## Code worth reusing

- `engine.py`: uncached benchmark engine with F_NOCACHE, fsync and random data
- `reference.json`: 28 drives with rated and measured numbers and review links

## Notes

SMART over USB is impossible on macOS and the page says so. smartctl (smartmontools) needed for internal health. Order of tests matters: random writes last.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
