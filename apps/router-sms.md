# Router SMS

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Reads and sends SMS and checks the SIM data balance through the 4G router's web page, using its own headless Firefox.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/router-sms](https://github.com/markoboskoauroville/router-sms) |
| Also called | ROUTER_SMS, SIM data balance |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Check the SIM data left by sending the operator's balance SMS and parsing the reply
- Send an SMS and read the newest inbox messages
- Switch the router's 2.4 GHz Wi-Fi on or off and read it back
- Run a warm local server that keeps the headless Firefox logged in
- Show the same steps in a visible Firefox window on request

## Ask for it when

- how much mobile data is left on the router SIM
- send an SMS through the router
- read SMS received by the router
- switch the router Wi-Fi off

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8880 (localhost; next free port if taken, written to ~/.mantra/ports/router-sms)

Actions:

- `balance`
- `last`
- `send`
- `inbox`
- `serve`
- `status`
- `wifi`
- `GET /balance`
- `GET /last`
- `GET /sms/inbox?n=`
- `POST /sms`
- `GET /health`

**Before you call:** Holds the router login; runs on 8880 (next free port if taken, written to ~/.mantra/ports/router-sms).

Example:

```
router-sms send <number> "text" # sends an SMS through the router SIM
```

More calls:

- SIM credit: `router-sms balance --json`
- last received SMS: `router-sms last`
- inbox: `curl -s '127.0.0.1:8880/sms/inbox?n=5'`
- health: `curl -s 127.0.0.1:8880/health`

Evidence: README.md, TAKEOVER.md

## Inputs / Outputs

Inputs:

- router web interface

Outputs:

- balance.json
- SMS text

## Hardware

- TP-Link 4G router with SIM

## Works with

- Uses: [Firefox Control](firefox-control.md)
- Talks to: [Connection Keeper](connection-keeper.md)
- Used by or talked to by: [Connection Keeper](connection-keeper.md), [Router Credits (Android)](router-credits.md), [Router Mode (Mantra)](router-mode.md)

## Code worth reusing

- `router-sms`: headless Firefox BiDi driver that logs into a router page and operates its SMS and Wi-Fi menus

## Notes

The router login is read from a local key file and never logged. A balance check takes about 12 to 14 seconds. Only one router action at a time. Runs as a LaunchAgent. The argument order of 'router-sms send' is by analogy with the verb list; not shown in the docs.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
