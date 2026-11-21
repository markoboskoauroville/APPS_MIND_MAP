# Connection Keeper

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac menu-bar app that keeps the internet up: watches Wi-Fi/cable/phone lines, fails over, aggregates and bonds several lines through a relay, tests speed.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/connection-keeper](https://github.com/markoboskoauroville/connection-keeper) |
| Also called | ConnectionKeeper, ck-aggregate, Connection Keeper (Mantra), connection keeper stripe |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Cloud |
| Language | Swift (plus Go bonding relay, Python tools) |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v88 |
| Control level | http (own http routes) |

## What it can do

- Show the state of every internet line in a stripe and menu-bar dot, switch lines and fail over
- Aggregate connections over several uplinks through a local SOCKS proxy (ck-aggregate)
- Bond multiple lines through a relay server in Frankfurt for one faster stream (ckbond)
- Use a USB-tethered phone as the only line (NOTHING ONLY mode) and diagnose cable/adb problems
- Run speed tests and read SIM data balance
- Check bonding health with ck-bondcheck
- Self-update from GitHub releases

## Ask for it when

- my internet keeps dropping, keep the connection alive
- combine phone hotspot and cable for more speed
- switch the Mac to the phone's connection
- test my internet speed on each line
- check that bonding works

## How to control it

- Level: **http**
- Type: cli, http, python-module
- Port: 8857 (ck-aggregate SOCKS/aggregation server on 127.0.0.1, with /status)

Actions:

- `ck-aggregate serve|uplinks|test|on|off|session open|close|handover|bond-init|bond-selftest`
- `ck-net test speed`
- `ck-bondcheck --speed --json --clean`
- `GET /status on the aggregate server`
- `distributed notification ConnectionKeeperNothingOnly (object on/off)`

Example:

```
ck-bondcheck --json # health of the bonded connection; the aggregate server on 127.0.0.1:8857 answers GET /status
```

More calls:

- uplinks and speed: `ck-aggregate uplinks ; ck-net test speed`
- aggregation on / off: `ck-aggregate on ; ck-aggregate off`
- status over HTTP: `curl -s 127.0.0.1:8857/status`

Evidence: TAKEOVER.md (aggregation section, v81-v88 notes), Sources/Aggregate/main.swift, Sources/Aggregate/Ports.swift, Tools/ck-bondcheck

## Inputs / Outputs

Inputs:

- Wi-Fi/Ethernet/USB-tethered phones (adb)
- router and SIM data balance

Outputs:

- status stripe
- SOCKS proxy on loopback
- speed test results
- logs

## Hardware

- USB-tethered Android phone over adb
- Ethernet adapter
- phone hotspots

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Router SMS](router-sms.md)
- Used by or talked to by: [Router SMS](router-sms.md)

## Code worth reusing

- `Sources/Aggregate/Ports.swift`: Swift port claiming/registry (MANTRA_PORTS) incl. fixed-port owner and UDP
- `Sources/Bond/server`: Go relay that bonds several TCP/UDP legs with reordering and resend
- `Sources/Shared/Phones.swift`: Lists USB-attached Android phones over adb and pushes a helper binary
- `Sources/Daemon/TailscaleGuard.swift`: Keeps Tailscale up as a guard daemon

## Notes

Does not follow the /health + /api remote-door contract as far as the harvested files show; control is via CLI tools and the aggregate server's /status. Port 8857 is quoted in LESSONS.md (an aggregation server on 127.0.0.1) and may differ from the MANTRA_PORTS table. Very large (3 GB, 121 files). One unmerged claude/ branch. Contains hard-coded network details in docs, not copied here.

Unmerged branches with commits ahead of main: 1.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/connection-keeper/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/connection-keeper/blob/HEAD/LESSONS.md)
