# Mantra Pages

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**The one fixed local web server of the Mac on port 8800: a folder per project, plus an endpoint to order Ableton Live.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra_pages](https://github.com/markoboskoauroville/mantra_pages) |
| Also called | pages server, local web server |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-10-24 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Serve `www/<project>/` pages at a fixed bookmarkable address
- List every project at the root
- Answer a health check
- Send orders to Ableton Live through the OSC router (venue_stereo, play_from_beats, solo, unsolo, stop)
- Start at login and restart after a crash via launchd

## Ask for it when

- serve a local web page I can bookmark
- host a project page on this Mac
- open a local page from any browser

## How to control it

- Level: **door**
- Type: http
- Port: 8800 (MANTRA_PORTS id: pages)

Actions:

- `GET /`
- `GET /api/health`
- `POST /api/live {cmd: venue_stereo|play_from_beats|solo|unsolo|stop}`

**Before you call:** Ableton Live Actions must run (OSC router on UDP 11002).

Example:

```
curl -s -XPOST 127.0.0.1:8800/api/live -H 'Content-Type: application/json' -d '{"cmd":"solo"}' # orders to Ableton Live through the OSC router of Ableton Live Actions (127.0.0.1:11002)
```

More calls:

- stop: `curl -s -XPOST 127.0.0.1:8800/api/live -H 'Content-Type: application/json' -d '{"cmd":"stop"}'`
- health: `curl -s 127.0.0.1:8800/api/health`

Evidence: README.md, server.py

## Inputs / Outputs

Inputs:

- `www/<project>` folders

Outputs:

- local web pages

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)

## Code worth reusing

- `server.py`: stdlib fixed-port static server that refuses another port

## Notes

No pages were in www yet at last note. An older separate server on another port was left in place.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
