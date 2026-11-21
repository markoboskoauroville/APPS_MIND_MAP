# Ableton Teacher and DaVinci Teacher apps (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Public Swift code of the two Teacher apps (Ableton Teacher, DaVinci Teacher): a window proposes one lesson step, speaks and takes replies (ports 8970, 8971).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_TEACHERS](https://github.com/markoboskoauroville/MANTRA_TEACHERS) |
| Also called | Ableton Teacher, DaVinci Teacher, Universal Teacher |
| Visibility | public |
| Kind | app |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | http (own http routes) |

## What it can do

- Show a lesson step window and move up/down through steps
- Speak a hint or reply with voice
- Take a snapshot of its own window as PNG
- Accept a proposed step as JSON (never presses NEXT itself: only a human click approves)
- Build two app bundles from one Swift source

## Ask for it when

- teach me Ableton step by step
- DaVinci Resolve lesson helper
- guided lesson window on the Mac

## How to control it

- Level: **http**
- Type: http
- Port: 8970 ableton-teacher, 8971 davinci-teacher, 8972 universal-teacher

Actions:

- `GET /health`
- `GET /state`
- `POST /up`
- `POST /down`
- `POST /quit`
- `POST /propose`
- `POST /reply {text}`
- `POST /hint {text}`
- `POST /speak {text, where}`
- `POST /snap {path}`

**Before you call:** The Teacher app (Ableton Teacher (Mantra) or DaVinci Teacher (Mantra)) must be running; ports are claimed in ~/.config/mantra-ports.json.

Example:

```
curl -s 127.0.0.1:8970/state # Ableton Teacher; DaVinci Teacher is 8971, universal 8972
```

More calls:

- show a proposed step in the window: `curl -s -XPOST 127.0.0.1:8970/propose`
- answer a message from the learner and speak it: `curl -s -XPOST 127.0.0.1:8970/reply -H 'Content-Type: application/json' -d '{"text":"Press cmd+T for a new track"}'`
- speak a sentence: `curl -s -XPOST 127.0.0.1:8970/speak -H 'Content-Type: application/json' -d '{"text":"Watch the track list","where":"mac"}'`
- screenshot the app to a file: `curl -s -XPOST 127.0.0.1:8970/snap -H 'Content-Type: application/json' -d '{"path":"/tmp/teacher.png"}'`

Evidence: app/Door.swift header lines 1-9 and cases lines 130-163; TAKEOVER.md ports

## Inputs / Outputs

Inputs:

- step JSON (step.json)
- lessons from ABLETON_TEACHER

Outputs:

- lesson window
- spoken hints
- PNG snapshots

## Works with

- Uses: [Teacher Lessons and Scripts (Ableton, DaVinci)](ABLETON_TEACHER.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Teacher Lessons and Scripts (Ableton, DaVinci)](ABLETON_TEACHER.md)

## Code worth reusing

- `app/Door.swift`: small loopback HTTP door with MANTRA_PORTS claim
- `app/Teacher.swift`: teacher engine shared by both apps

## Notes

Code only; lessons, voice files and Oracle scripts are in private ABLETON_TEACHER. Port 8965 belongs to MPA Lessons Analyzer, not here. Little documentation (TAKEOVER is two lines). Argument shapes of /propose and the value of where in /speak are not described in the harvested docs (only the list of routes). The command-line side (teacher.py, live.py, resolve.py) is in private ABLETON_TEACHER.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_TEACHERS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_TEACHERS/blob/HEAD/LESSONS.md)
