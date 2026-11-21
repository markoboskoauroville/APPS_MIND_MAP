# LAN Scanner (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app listing every device on the current network: name, IP, MAC, maker, kind, last seen. Also gives JSON through a lanscan command.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/LAN_SCANNER](https://github.com/markoboskoauroville/LAN_SCANNER) |
| Also called | LAN Scanner (Mantra), lanscan, Network scanner |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | cli (command line or script only) |

## What it can do

- Scan the local network with ICMP sweep and NetBIOS node-status
- Discover devices through SSDP/UPnP
- Show maker from the IEEE OUI table
- Copy a device IP on row click
- Scan another network interface on request
- Print the device list as JSON with --json

## Ask for it when

- which devices are on my network
- scan the LAN
- find the IP of a device on the Wi-Fi
- list network devices with maker names

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--json`
- `--iface <name>`
- `--selftest`

**Before you call:** The lanscan wrapper (in ~/.local/bin) runs the LAN Scanner (Mantra) app binary; install the app from the GitHub release first.

Example:

```
lanscan --json # every device on the LAN as JSON
```

More calls:

- scan one network interface: `lanscan --iface en0 --json`
- self test, no network: `lanscan --selftest`

Evidence: TAKEOVER.md section 'From clone to installed' step 4

## Inputs / Outputs

Inputs:

- the Mac's current network

Outputs:

- device table
- JSON device list

## Hardware

- Mac network interfaces

## Works with

- Talks to: [Star (Mantra), Swift menu](STAR_SWIFT.md)

## Code worth reusing

- `app/Discover.swift`: ICMP sweep, NetBIOS and SSDP device discovery
- `app/Oui.swift`: MAC address to maker lookup from the IEEE table
- `tools/make_oui.py`: build the OUI maker table

## Notes

Public repo with no README by rule. The lanscan wrapper script lives outside the repo (~/.local/bin). Built only by GitHub Actions; releases vN with app.zip.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/LAN_SCANNER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/LAN_SCANNER/blob/HEAD/LESSONS.md)
