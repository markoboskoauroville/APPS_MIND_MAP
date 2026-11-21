# Cockpit Termux

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Phone health page in Termux: CPU, RAM, battery, wifi, every process with force-stop, kill-all, ADB bridge, phantom-process limit lift, wake lock.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/COCKPIT_TERMUX](https://github.com/markoboskoauroville/COCKPIT_TERMUX) |
| Also called | cockpit command, phone cockpit page |
| Visibility | public |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Python (Flask) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Show CPU number, per-core bars, GHz, RAM, swap, battery, thermal, storage, wifi
- List every process with memory (dumpsys meminfo) and force-stop one
- Kill every background process (am kill-all)
- Pair and connect Wireless debugging as a bridge
- Lift the Android phantom-process limit
- Hold a wake lock and log every action

## Ask for it when

- kill memory-hungry apps on my phone
- phone health page
- lift the phantom process limit
- see what my Android is doing

## How to control it

- Level: **door**
- Type: http, cli
- Port: 8860 (MANTRA_PORTS id cockpit, 8860-8875 then any)

Actions:

- `GET /health`
- `GET /api/status`
- `POST /api/refresh`
- `POST /api/stop`
- `POST /api/kill-all`
- `POST /api/bridge/pair`
- `POST /api/bridge/connect`
- `POST /api/bridge/disconnect`
- `POST /api/phantom/lift`
- `POST /api/wake`
- `GET /api/log`
- `cockpit`
- `cockpit update`

**Before you call:** Cockpit runs on the phone in Termux (start with the command cockpit); port 8860 or the next free one up to 8875.

Example:

```
curl -s -XPOST 127.0.0.1:8860/api/refresh
```

More calls:

- status: `curl -s 127.0.0.1:8860/api/status`
- wake the phone: `curl -s -XPOST 127.0.0.1:8860/api/wake`
- stop everything it started: `curl -s -XPOST 127.0.0.1:8860/api/kill-all`
- update itself: `cockpit update`

Evidence: app.py lines 218-316

## Inputs / Outputs

Inputs:

- /proc/meminfo, cpuidle counters
- Termux:API
- adb shell

Outputs:

- web page
- ~/.cockpit/log.jsonl

## Works with

- Uses: [Keyring](KEYRING_TERMUX.md)
- Talks to: [Cockpit Android](COCKPIT_ANDROID.md)
- Used by or talked to by: [Cockpit Android](COCKPIT_ANDROID.md)

## Code worth reusing

- `portpick.py`: preferred port, next fifteen, then OS port; writes `~/.mantra/ports/<command>`
- `localguard.py`: three checks on every /api call so only the local page can POST
- `bridge.py`: Termux to ADB wireless-debugging bridge for force-stop and kill-all
- `selfupdate.py`: pull newest version and restart

## Notes

Loopback only. Without the ADB bridge only Termux's own processes can be handled. Install line is a curl pipe to install-termux.sh.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/COCKPIT_TERMUX/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/COCKPIT_TERMUX/blob/HEAD/HANDOVER.md)
