# Star API (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**The common remote door for every Mac star app: list, open, quit, read and press controls by name, plus per-app functions, over CLI and token-guarded HTTP.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STAR_API](https://github.com/markoboskoauroville/STAR_API) |
| Also called | star, one common API, star CLI |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS |
| Language | Python (plus Swift wrapper app) |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- List all Mantra Mac apps and whether they run
- Open or quit an app in the background
- Read an app's controls through Accessibility
- Press a control by name (exact, prefix, part)
- List and call per-app functions such as the recorder's record.suno
- Fill password dialogs through Macro Recorder

## Ask for it when

- press a button in one of my Mac apps remotely
- start an app from my phone
- call a function of an app by name
- list all my apps

## How to control it

- Level: **http**
- Type: http, cli, remote-door-http
- Port: 8863

Actions:

- `GET /apps`
- `GET /apps/<name>`
- `POST /apps/<name>/open`
- `POST /apps/<name>/quit`
- `POST /apps/<name>/press`
- `GET /fn`
- `GET /apps/<name>/fn`
- `POST /apps/<name>/fn/<function>`
- `POST /login-dialog`
- `star apps`
- `star open`
- `star read`
- `star press`
- `star quit`
- `star serve`
- `star fn`
- `star login-dialog`

**Before you call:** From another machine (phone, cloud session) add header X-Mantra-Token with the token in ~/.config/mantra-door.token; on 127.0.0.1 no token is needed. The server is started with: star serve (runs in the background once Star API (Mantra) is on).

Example:

```
curl -s -XPOST 127.0.0.1:8863/apps/timer/press -H "Content-Type: application/json" -d '{"label":"stopwatch"}' # same as: star press "timer" "stopwatch"
```

More calls:

- list every Star app and whether it runs: `curl -s 127.0.0.1:8863/apps # CLI: star apps`
- read the controls (role, label, window) of an app: `curl -s 127.0.0.1:8863/apps/timer # CLI: star read "timer"`
- start or quit an app: `curl -s -XPOST 127.0.0.1:8863/apps/timer/open # /quit to close; CLI: star open "timer" / star quit "timer"`
- call a function an app registered (Sound Recorder example): `star fn "sound recorder" record.suno '{"out":"~/x.wav","url":"https://suno.com/song/..."}'`

Evidence: README.md and starapi.py

## Inputs / Outputs

Inputs:

- app names and control labels

Outputs:

- JSON app lists and results

## Works with

- Uses: [Macro Recorder (Mantra)](MANTRA_MACRO.md)
- Talks to: [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md)
- Used by or talked to by: [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `starapi.py`: library, CLI and HTTP server for app control by Accessibility labels

## Notes

Binds loopback and the Mac's tailnet address only; token header required off loopback. Runs always (autostart). Press goes through Macro Recorder v10+, which holds the Accessibility permission. Mac Swift star apps expose buttons with ids like off, top, close. Names match by part (timer = Timer Stopwatch Clock). The press goes through Macro Recorder's ax-press; to press a button in an app that is NOT one of the Star apps use MANTRA_MACRO: macro ax-press `"<app>"` `"<label>"`. Whether `/apps/<name>/press` resolves a non-Star app name was not verified.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
