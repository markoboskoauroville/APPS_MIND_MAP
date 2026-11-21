# aooserver-arm64

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**GitHub Actions build of the SonoBus connection server (essej/aooserver) for Linux arm64 so the cloud VM can run its own SonoBus server on its Tailscale address.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/aooserver-arm64](https://github.com/markoboskoauroville/aooserver-arm64) |
| Also called | aooserver, SonoBus server |
| Visibility | public |
| Kind | service-daemon |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | Linux, Cloud |
| Language | C++ (upstream), built by workflow |
| Status | active |
| Last push | 2026-11-12 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | cli (command line or script only) |

## What it can do

- Build aooserver for Linux arm64 and publish release vN
- Let SonoBus peers exchange tailnet addresses through a server on the VM
- Run as aooserver -p `<port>` [-l logdir] [-b blocklist]

## Ask for it when

- SonoBus server on the cloud machine
- audio link between the VM and my Mac with SonoBus
- arm64 aooserver binary

## How to control it

- Level: **cli**
- Type: cli
- Port: 10998

Actions:

- `aooserver -p <port> -l <logdir> -b <blocklist>`

**Before you call:** Listens on UDP/TCP port 10998 by default; -l sets the log folder and -b a blocklist file.

Example:

```
aooserver -p 10998
```

More calls:

- with log folder and blocklist: `aooserver -p 10998 -l ~/aoo-logs -b ~/aoo-blocklist.txt`

Evidence: TAKEOVER.md (Usage of the binary)

## Inputs / Outputs

Outputs:

- aooserver-linux-arm64 release asset

## Hardware

- Oracle arm64 VM chromium-vm

## Notes

Only a build recipe plus TAKEOVER.md; no source. Reason: SonoBus direct link failed through the firewall and router, so a server on the tailnet is used. Public, unpromoted.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/aooserver-arm64/blob/HEAD/TAKEOVER.md)
