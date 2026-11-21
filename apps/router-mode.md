# Router Mode (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac menu-bar watcher for the home TP-Link 4G router: shows whether phone-tethering or the SIM carries the internet, warns, and can switch mode.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/router-mode](https://github.com/markoboskoauroville/router-mode) |
| Also called | routermode, Router Mode |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Cloud |
| Language | Swift (menu-bar app) and Python (client) |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | cli (command line or script only) |

## What it can do

- Read router status (mode, LTE backup, WAN link state, daily data, signal) through its encrypted web API
- Show PHONE or SIM and data used in the menu bar, orange when the SIM carries while the phone is home
- Warn by macOS notification when Ethernet tethering is probably off
- Switch to phone internet or SIM only (confirm, router reboots 1-2 minutes)
- Detect the phone's Ethernet tether state over adb
- Self-update from GitHub releases

## Ask for it when

- is my internet coming from the phone or the SIM
- switch the router to SIM only
- warn me when the router fell back to the SIM

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `routermode status`
- `routermode tether`
- `routermode state`
- `routermode daemon`
- `routermode set`

**Before you call:** Mantra Router mode helper (router and phone tethering).

Example:

```
routermode status
```

More calls:

- tethering state: `routermode tether`
- current state as data: `routermode state`

Evidence: TAKEOVER.md (The pieces table); routermode.py; bin/routermode

## Inputs / Outputs

Inputs:

- router web API
- adb phone state
- password file (never printed)

Outputs:

- state.json
- menu-bar title
- log file
- notifications

## Hardware

- TP-Link TL-MR110 4G outdoor router
- Android phone with Ethernet dongle (tethering)

## Works with

- Uses: [Router SMS](router-sms.md)

## Code worth reusing

- `routermode.py`: TP-Link MR router client: RSA/AES login, read WAN/LTE status, switch mode
- `app/Updater.swift`: Updater kit for GitHub Latest releases in a menu-bar app
- `app/HoverCard.swift`: Hover card UI for a menu-bar item

## Notes

No README (public, not promoted). The router allows one session: a login throws out other admin tabs and router-sms. The watcher never switches by itself. Hand back from SIM to cable not yet proven (15.11.2026). Queen has a local skill 'router status / use phone / use SIM'.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/router-mode/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/router-mode/blob/HEAD/LESSONS.md)
