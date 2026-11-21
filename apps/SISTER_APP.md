# Sister App (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Small Mac window with ON/OFF for the MANTRA CHAT local server and a link to its page.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SISTER_APP](https://github.com/markoboskoauroville/SISTER_APP) |
| Also called | MANTRA CHAT switch |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Start and stop the chat server process
- Open the chat page in Chrome
- Show a light from the server health check every 2 s

## Ask for it when

- turn the chat server on or off
- open the Mantra chat page

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `close`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "sister" "top"
```

More calls:

- list the controls of the window: `star read "sister"`
- start the app in the background: `star open "sister"`
- quit it: `star quit "sister"`

Evidence: TAKEOVER.md: controls are Accessibility buttons with ids off, top, close; reachable through STAR_API press

## Notes

Nothing starts by itself; opening the app never starts the server. Built from the old Hammerspoon sister row.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
