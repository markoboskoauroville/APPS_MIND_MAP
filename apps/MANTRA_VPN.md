# VPN (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac and Android app with one switch, FRANKFURT or DIRECT, that sends all traffic through the owner's cloud VM by driving Tailscale's exit-node setting.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_VPN](https://github.com/markoboskoauroville/MANTRA_VPN) |
| Also called | VPN (Mantra), Mantra VPN, FRANKFURT switch, Connection Keeper (simplified) |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Android |
| Language | Swift (Mac) and Kotlin (Android) |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | none (no control api found) |

## What it can do

- Switch Tailscale exit node on (the Frankfurt VM) or off (direct) on the Mac
- Drive the Android Tailscale app to use or drop the exit node
- Show public IP and country at start, after each switch and every ten minutes
- Keep the LAN reachable while on the exit node
- Update itself at start

## Ask for it when

- route my traffic through Frankfurt
- turn VPN on or off
- change my public IP to Germany
- simple Tailscale exit-node switch

## How to control it

No control API found.

Evidence: No app API; it itself calls com.tailscale.ipn.USE_EXIT_NODE broadcast (TAKEOVER.md)

## Inputs / Outputs

Inputs:

- tailscale status --json

Outputs:

- exit node set or cleared
- public IP/country display

## Works with

- Uses: [Chromium Virtual Machine (Mantra)](vm-chromium.md)

## Code worth reusing

- `mac/Sources/Tailscale.swift`: find exit node and set/clear it via the Tailscale CLI
- `android/app/src/main/java/com/mantraproductions/vpn/TailscaleCtl.kt`: drive Tailscale for Android with CONNECT_VPN and USE_EXIT_NODE intents

## Notes

No key or address in the repo by design (exit node found at run time in the tailnet). Mac and Android build into one release with the same version number. Public unpromoted repo.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_VPN/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_VPN/blob/HEAD/LESSONS.md)
