# Brain Brake review wall

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local full-screen page that shows each new frame from the chat session and sends KEEP or REDO verdicts back with no typing.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAIN_BRAKE_REVIEW](https://github.com/markoboskoauroville/BRAIN_BRAKE_REVIEW) |
| Also called | review wall, STEP 92 |
| Visibility | public |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS, Web |
| Language | Python (Flask) |
| Status | dormant |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | door (standard door) |

## What it can do

- Poll review/latest.json in BRAIN_BRAKE_ORIGINALS every 3 s over raw URL
- Download new frames and show the newest full screen with a strip of previous ones
- Record KEEP or REDO (with a reason for REDO) and push verdicts.json via gh api
- Push page updates over server-sent events

## Ask for it when

- review the new film frames and say keep or redo
- show generated frames on the screen as they arrive
- send verdicts to the chat session

## How to control it

- Level: **door**
- Type: http
- Port: 8777

Actions:

- `GET /health`
- `GET /api/state`
- `POST /api/verdict`
- `GET /api/events`

**Before you call:** Needs gh logged in as the repo owner; REVIEW_RAW points it at a local mock for tests.

Example:

```
curl -s -XPOST 127.0.0.1:8777/api/verdict -H 'Content-Type: application/json' -d '{"verdict":"keep"}' # body field names are not documented; the page keys are k (keep) and r (redo)
```

More calls:

- what is on screen now: `curl -s 127.0.0.1:8777/api/state`
- event stream: `curl -sN 127.0.0.1:8777/api/events`

Evidence: review_wall.py lines 473-508

## Inputs / Outputs

Inputs:

- review/latest.json and frames in BRAIN_BRAKE_ORIGINALS

Outputs:

- review/verdicts.json

## Works with

- Uses: [Brain Brake originals](BRAIN_BRAKE_ORIGINALS.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Brain Brake originals](BRAIN_BRAKE_ORIGINALS.md)

## Code worth reusing

- `review_wall.py`: doorbell pattern: poll one tiny JSON over raw URL, one writer per file, SSE page refresh

## Notes

Needs gh logged in as the repo owner. REVIEW_RAW env var points it at a local mock for testing. Keys k and r keep or redo.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_REVIEW/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_REVIEW/blob/HEAD/LESSONS.md)
