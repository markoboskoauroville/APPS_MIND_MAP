# DaVinci Resolve Actions (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app with ACTIONS and MODS tabs for DaVinci Resolve, plus resolve_router.py, the one door every app and session uses to reach Resolve's scripting API.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DAVINCI_RESOLVE_ACTIONS](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ACTIONS) |
| Also called | DaVinci Resolve Actions, Resolve Actions, resolve router, resolve-run |
| Visibility | public |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Swift + Lua + Python |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v24 |
| Control level | cli (command line or script only) |

## What it can do

- Run Balancing, Grading and Exporting Automatic as a stepped action (play, next step, stop, restart)
- Create a timeline from the selected clips, toggle HD and UHD, previous page
- Switch Resolve pages (about 0.1 s) and J K L keys
- Project Backup: clean up renders and generated media to the Trash
- Run any Resolve Python code through the router with timeout, queue and BUSY detection
- Hold the router for one caller while it works (hold and release)

## Ask for it when

- automatically grade and export in Resolve
- switch Resolve page from a script
- create a timeline from the selected clips
- run Python inside DaVinci Resolve safely
- back up and clean a Resolve project
- toggle HD and UHD in Resolve
- previous page in DaVinci Resolve

## How to control it

- Level: **cli**
- Type: remote-door-http, cli
- Port: 8940 preferred (MANTRA_PORTS id resolve; also quoted for OXI controller in the manifest)

Actions:

- `GET /health`
- `GET /status`
- `GET /page`
- `GET /pages`
- `POST /open?page=edit`
- `POST /run {who,code|file,args,timeout}`
- `POST /hold {who,minutes}`
- `POST /release {who}`
- `resolve-run`

**Before you call:** DaVinci Resolve Actions (Mantra) must be running; the router starts with it and ends with it, and only while Resolve runs does it answer. Never open a second Resolve connection: send everything through POST /run (HTTP codes: 200 done, 503 busy, 423 held by someone else, 504 timeout, 500 code failed).

Example:

```
curl -s -X POST 'http://127.0.0.1:8940/run' -H 'Content-Type: application/json' -d '{"who":"me","code":"result = project.GetName()","timeout":30}'
```

More calls:

- open a page (media|cut|edit|fusion|color|fairlight|deliver): `curl -s -XPOST '127.0.0.1:8940/open?page=edit'`
- what page and project is Resolve on: `curl -s 127.0.0.1:8940/status`
- run a script file through the router from a shell: `resolve-run --who me job.py # also: resolve-run status; hold / release`
- add a timeline marker (Resolve scripting API call; the repo docs show the same marker only as resolve.py marker, see ABLETON_TEACHER): `curl -s -XPOST 127.0.0.1:8940/run -H 'Content-Type: application/json' -d '{"who":"me","code":"result = project.GetCurrentTimeline().AddMarker(250, \"Red\", \"look here\", \"\", 1)","timeout":30}'`

Evidence: scripts/resolve_router.py docstring lines 15-33; app/Common.swift ROUTER_PORT

## Inputs / Outputs

Inputs:

- DaVinci Resolve (External scripting: Local)
- action scripts in scripts/

Outputs:

- Resolve timelines, renders, page changes
- JSON answers from the router

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Star (Mantra), Swift menu](STAR_SWIFT.md)
- Talks to: [G815 Lights](G815_LIGHTS.md), [Oxi Controller (E16 Remote)](oxi-controller.md)
- Used by or talked to by: [G815 Lights](G815_LIGHTS.md)

## Code worth reusing

- `scripts/resolve_router.py`: queue, timeout and BUSY detection for Resolve's scripting API; run code with resolve, project, pm in a killable worker
- `scripts/resolve-run`: command line client for the router
- `scripts/Project Backup.py`: safe cleanup of Resolve renders, caches and proxies to Trash
- `app/Pages.swift`: Resolve page switching

## Notes

HTTP codes: 200 done, 503 busy, 423 held by someone else, 504 timeout (worker replaced), 500 code failed. Router starts with the app and ends with it. Router /run is the supported way; never open a second Resolve connection. Absorbs the older DAVINCI_RESOLVE_ASSISTANT scripts. Port 8940 is also cited for OXI controller POST /run in the manifest, verify with mantra-ports scan.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ACTIONS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ACTIONS/blob/HEAD/LESSONS.md)
