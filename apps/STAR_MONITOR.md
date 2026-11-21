# Star Monitor (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac window that manages every app of the star menu: start, stop, order, run-time tracking and which apps come back after a restart.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STAR_MONITOR](https://github.com/markoboskoauroville/STAR_MONITOR) |
| Also called | Star Monitor |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v5 |
| Control level | door (standard door) |

## What it can do

- Start and stop each star app
- Reorder apps and arrange the OPEN NOW order
- Track time run today, 7 days and all time
- Remember which apps stay open between sessions
- Turn all apps off

## Ask for it when

- see which Mantra apps are running
- start or stop all my apps
- how long has each app run
- manage what comes back after restart

## How to control it

- Level: **door**
- Type: accessibility, http
- Port: 8851 (former Flask version)

**Warning:** port 8851 is also quoted for [YT Transcriber](YT_TRANSCRIBER.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /api/state`
- `POST /api/<key>/start`
- `POST /api/<key>/stop`
- `POST /api/order`
- `POST /api/open-order`
- `POST /api/alloff`
- `GET /health`
- `POST /quit`

**Before you call:** Verify first: the HTTP API on 8851 belongs to the old Flask page and may not exist in the Swift window version (v5). The window buttons answer Accessibility as off, top, close (STAR_API press).

Example:

```
curl -s 127.0.0.1:8851/api/state
```

More calls:

- switch all off: `curl -s -XPOST 127.0.0.1:8851/api/alloff`

Evidence: TAKEOVER.md lines 97-102 (describes the former Python Flask monitor.py); app/App.swift header says the Swift window replaces monitor.py

## Inputs / Outputs

Inputs:

- star state files (star-running.json, star-time.json, star-order.json)

Outputs:

- state written to those files

## Works with

- Uses: [Star (Mantra), Swift menu](STAR_SWIFT.md)
- Used by or talked to by: [Star (Mantra), Swift menu](STAR_SWIFT.md)

## Notes

Repo is now the Swift window (v5, writes order files itself); the HTTP API on 8851 belongs to the older Flask page and may not exist in the Swift version. Window buttons answer Accessibility as off, top, close. Verify before calling.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/STAR_MONITOR/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/STAR_MONITOR/blob/HEAD/LESSONS.md)

_Low confidence: little was documented in this repository. Check the code before relying on this card._
