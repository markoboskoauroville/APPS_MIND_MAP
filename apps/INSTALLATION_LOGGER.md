# Installation Logger (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Records every file an installer writes on the Mac, saves a log and can uninstall or put back the ticked rows.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/INSTALLATION_LOGGER](https://github.com/markoboskoauroville/INSTALLATION_LOGGER) |
| Also called | Installation Logger, installer logger |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Web |
| Language | Swift (original Python/Flask) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | http (own http routes) |

## What it can do

- Watch file events under system and home folders while an installer runs
- Fold the log into created, modified, temporary and deleted rows
- Save the log as JSON
- Move ticked files out to uninstall and put them back to reinstall
- Delete removed files permanently on request

## Ask for it when

- see what an installer put on my Mac
- uninstall an app completely using a log
- record an installation

## How to control it

- Level: **http**
- Type: http
- Port: 8841

**Warning:** port 8841 is also quoted for [Cloud Mixer](CLOUD_MIXER.md), [Mantra Remote Viewing (Mantra Remote)](MANTRA_REMOTE_VIEWING.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `POST /quit`

**Before you call:** Port 8841 here is the Mac's logger; other apps also use 8841 on other machines.

Example:

```
curl -s 127.0.0.1:8841/health # only /health and /quit exist; the logger is used in its window
```

More calls:

- close it: `curl -s -XPOST 127.0.0.1:8841/quit`

Evidence: TAKEOVER.md; logger.py line 34

## Inputs / Outputs

Outputs:

- ~/.installation_logger/logs/*.json

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Notes

Port 8841 is also quoted for another app in the manifest port table; the Python page is the older engine replaced by a Swift window.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
