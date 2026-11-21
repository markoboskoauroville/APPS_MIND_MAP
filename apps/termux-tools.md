# Termux Tools

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Phone-side Termux toolkit: mamc app launcher, talk (spoken Claude replies), ccnotify, claudelogin, phonelink and adbup (adb without Wi-Fi).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/termux-tools](https://github.com/markoboskoauroville/termux-tools) |
| Also called | mamc, talk, ccnotify, ccpush, claudelogin, phonelink, adbup, Midnight Commander for phone apps |
| Visibility | public |
| Kind | cli-tool |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Python (plus shell) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- mamc: file-manager-style launcher that lists, runs, opens in Chrome, moves, uninstalls and updates every app on the phone
- talk: speak Claude Code's replies aloud on a code word and feed the Mac subtitle (via Voice Engine :8720-8735)
- ccnotify and ccpush: notification when Claude stops or needs input, with a button that pushes 'continue' into the session
- claudelogin: sign Claude Code in as a different account (sign out of claude.ai, open login, paste code)
- phonelink: run shell commands, screencap and installs on the phone via adb loopback or Shizuku rish, with a watcher
- adbup: connect and pin adb on the phone's own port without Wi-Fi
- Install with one line (install-termux.sh) and keep a test suite (tests/)

## Ask for it when

- install my Termux tools on a phone
- launch Termux apps from a menu
- have Claude's replies read aloud on the phone
- get a notification when Claude Code finishes on the phone
- switch Claude account in Termux
- keep adb connected on the phone without Wi-Fi

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `mamc`
- `mamc --update`
- `talk`
- `talk sub on|off|test|hide|stop|toggle|status|set k=v`
- `ccnotify`
- `ccpush TEXT`
- `claudelogin`
- `phonelink sh|exec-out|install|status|watch`
- `adbup [status]`

**Before you call:** On the phone in Termux (mamc starts the apps; phonelink from the Mac sends adb commands).

Example:

```
phonelink sh 'input tap 300 400'
```

More calls:

- update: `mamc --update`
- send a text to the Mac (notification): `ccpush "build done"`
- adb helper status: `adbup status`

Evidence: README block in TAKEOVER.md, HANDOVER.md, phonelink and adbup script headers, notify/ccpush, talker/talk

## Inputs / Outputs

Inputs:

- Termux environment (PRoot Ubuntu)
- port registry `~/.mantra/ports/<command>`

Outputs:

- spoken audio
- notifications
- adb sessions

## Hardware

- Android phone (Pixel 7, Nothing Phone)

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md), [Voice Engine (Mantra)](VOICE_ENGINE.md)
- Talks to: [Claude Code hub](claude-code.md)
- Used by or talked to by: [DJ Mantra (Android DJ app)](djmantra_app.md)

## Code worth reusing

- `phonelink`: Shell wrapper that reaches a phone's adb via loopback or Shizuku with a keep-alive watcher
- `adbup/adbup`: Pins adb to 127.0.0.1:5555 and scans for the Wi-Fi debug port in one asyncio process
- `notify/ccnotify.py`: Claude Code hook that sends phone notifications and lets a button push text back
- `talker/talker.py`: Claude hook speaker with word timing and subtitle feed
- `tests/run_all.py`: Four-stage test harness (mechanism, UI, ugly cases, upgrade)

## Notes

The repo was private when the README was written and is public now (flag in repos list); docs were written when it was private, so the install line using gh may be outdated: curl form works. Change talker.py here AND the copy in ~/.talker. Release tags are only archive refs. The artefact is the checkout; mamc's u key does git pull.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/termux-tools/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/termux-tools/blob/HEAD/HANDOVER.md)
