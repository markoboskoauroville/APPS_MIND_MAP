# Mantra Remote Viewing (Mantra Remote)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app to view and drive Macs, a VM and other phones (VNC, Tailscale, adb), share its own screen as a VNC server and expose phone and macro doors.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_REMOTE_VIEWING](https://github.com/markoboskoauroville/MANTRA_REMOTE_VIEWING) |
| Also called | Mantra Remote, Mantra Remote VNC, Claude Control (phone), MANTRA_REMOTE, mremote, rvctl, remote viewing |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | Android, Cloud |
| Language | Kotlin (plus Python tools) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | door (standard door) |

## What it can do

- View and control machines over VNC with a toolbar of Mac keys
- Share this phone's screen as a built-in VNC server (port 5900, password optional)
- Run a Claude Control accessibility door that taps, swipes, types and screenshots the phone itself with a big visible pointer
- Run a macro door on port 8841: run a Macro Recorder script in one request, state and small screenshot
- Keep USB/wireless debugging switched on and restore adb on 5555
- Find the Mac and phones on the tailnet and show a floating machine bubble

## Ask for it when

- control my phone from Claude
- see the Mac screen on the phone
- tap or swipe on the Android phone remotely
- share the phone screen to a laptop
- run a macro on the phone

## How to control it

- Level: **door**
- Type: remote-door-http, http, accessibility, adb-intent
- Port: 8841 macro door; 8790 Claude Control door; 5900 VNC

**Warning:** port 8841 is also quoted for [Cloud Mixer](CLOUD_MIXER.md), [Installation Logger (Mantra)](INSTALLATION_LOGGER.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `GET /api`
- `GET /api/state`
- `POST /api/run`
- `GET /api/shot?w=`
- `Claude Control door (8790): tap, swipe, scroll, longpress, text, key, shot, tree`
- `CLI rvctl: pixel tap X Y, swipe, scroll, longpress, text, key, shot, tree, open-viewer`
- `CLI mremote (incl. keep <phone>)`

**Before you call:** Mac side through adb forward tcp:8790 tcp:8790. Since v63 rvctl refuses every action without --watched (ask the owner: are you watching?) and without --expect ‹package in front›, and it reads GET /foreground before acting. The Accessibility service 'Mantra Remote Viewing - Claude Control' must be switched on by hand once on the phone.

Example:

```
rvctl pixel tap 540 1200 --label "NDI" --watched --expect com.mantraproductions.manualcamera
```

More calls:

- a picture of the phone screen: `rvctl pixel shot`
- type text, press a key, swipe, scroll (same guards): `rvctl pixel text "hello" --watched --expect com.android.chrome ; rvctl pixel key BACK --watched --expect com.android.chrome`
- read the screen as a node tree instead of a picture: `rvctl pixel tree`
- run a Macro Recorder script on the phone in one request (phone door 8841, command mremote): `mremote run pixel 'Press "CHROMIUM-VM"' # HTTP form: POST /api/run; GET /api/shot?w=360 gives one small picture`

Evidence: TAKEOVER.md lines 44-62 (Claude Control door) and 139-142 (macro door, MacroDoor.kt); tools/rvctl.py, tools/mremote.py

## Inputs / Outputs

Inputs:

- VNC streams
- adb
- Tailscale network

Outputs:

- phone/Mac control
- screen shares
- screenshots

## Hardware

- Android phones (Pixel 7, Nothing Phone)
- Mac
- Linux VM

## Works with

- Uses: [Macro Recorder (Mantra)](MANTRA_MACRO.md)
- Used by or talked to by: [Dock Switcher (Mantra)](MACOS_TASK_SWITCHER.md)

## Code worth reusing

- `android/app/src/main/java/com/mantra/remote/VncServer.kt`: pure Kotlin RFB 3.8 VNC server with ZRLE and Raw tiles
- `android/app/src/main/java/com/mantra/remote/ClaudeControl.kt`: AccessibilityService door: gestures, screenshot, node tree, visible pointer
- `android/app/src/main/java/com/mantra/remote/MacroDoor.kt`: HTTP door with /health, /api, /api/run per the remote-door protocol
- `android/app/src/main/java/com/mantra/remote/DebugKeeper.kt`: keeps USB and wireless debugging enabled
- `android/app/src/main/java/com/mantra/remote/adb/AdbLink.kt`: adb over Wi-Fi client inside the app

## Notes

Loopback or adb forward needs no token; LAN/Tailscale calls need the X-Mantra-Token header. Accessibility service must be enabled by hand once. Built by GitHub Actions only. One unmerged cloud branch. Big FEATURE_REQUEST.md backlog. The package given to --expect is an example and the exact mremote argument form is from the manifest digest; the guard flags are from TAKEOVER v63. Emulator for tests: rvctl emu ...

Unmerged branches with commits ahead of main: 1.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_REMOTE_VIEWING/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_REMOTE_VIEWING/blob/HEAD/LESSONS.md)
