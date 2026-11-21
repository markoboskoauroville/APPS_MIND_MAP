# Keyboard and Mouse Router (Mantra) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Macro Recorder (Mantra)](MANTRA_MACRO.md). Replaced by MANTRA_MACRO.

**RETIRED Mac guard app: would hold Marko's keyboard/mouse while Claude drives the Mac and show a badge. Replaced by Macro Recorder's input lock.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_KEYBOARD_MOUSE_ROUTER](https://github.com/markoboskoauroville/MANTRA_KEYBOARD_MOUSE_ROUTER) |
| Also called | Keyboard and Mouse Router, keyboard mouse guard, Mouse router |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | http (own http routes) |

## What it can do

- Offer a borrow/return token API on port 8870
- Show a badge 'Claude is borrowing your mouse and keyboard'
- Buffer the person's typing during a borrow and restore app and pointer afterwards

## Ask for it when

- guard my keyboard while Claude uses the mouse
- stop typing going into the wrong window during automation

## How to control it

- Level: **http**
- Type: http
- Port: 8870

Actions:

- `POST /borrow {reason, seconds}`
- `POST /return`
- `GET /status`
- `POST /enabled {on}`

**Before you call:** RETIRED, do not use (see notes).

Example:

```
curl -X POST http://127.0.0.1:8870/borrow -d '{"reason":"typing","seconds":20}'
```

More calls:

- give back: `curl -s -XPOST 127.0.0.1:8870/return`
- status: `curl -s 127.0.0.1:8870/status`

Evidence: TAKEOVER.md section 'The API (127.0.0.1:8870)'

## Works with

- Talks to: [Macro Recorder (Mantra)](MANTRA_MACRO.md)

## Notes

DO NOT USE: retired 14.11.2026, never installed or tested. Use Macro Recorder's guard (MANTRA_MACRO, port 8829, `guard` command). Do not take port 8870 for any guard. RETIRED/SUPERSEDED: use MANTRA_MACRO instead.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_KEYBOARD_MOUSE_ROUTER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_KEYBOARD_MOUSE_ROUTER/blob/HEAD/LESSONS.md)
