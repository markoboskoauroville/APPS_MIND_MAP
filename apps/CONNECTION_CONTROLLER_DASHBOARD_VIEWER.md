# Connection Controller Dashboard Viewer (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Native Mac dashboard of every network interface with true per-interface internet checks and an IGNORE switch that turns the service off.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CONNECTION_CONTROLLER_DASHBOARD_VIEWER](https://github.com/markoboskoauroville/CONNECTION_CONTROLLER_DASHBOARD_VIEWER) |
| Also called | Connection Controller, connection dashboard |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-20 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- List every network interface with the active one first
- Probe each interface by a bound ping with HTTP fallback
- Colour interfaces green, yellow or red by real reachability
- Turn a macOS network service off or on via IGNORE
- Print probe results as JSON

## Ask for it when

- check which network connection has internet
- turn off a network interface I do not want
- see all Mac network interfaces

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--probe-json`

Example:

```
"/Applications/Connection Controller Dashboard Viewer (Mantra).app/Contents/MacOS/ConnectionController" --probe-json
```

Evidence: README.md Build section

## Inputs / Outputs

Outputs:

- probe JSON

## Code worth reusing

- `app/Network.swift`: per-interface internet probing with bound ping and curl fallback

## Notes

Related to the connection-keeper repo.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
