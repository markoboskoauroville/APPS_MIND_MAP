# vm-android (Pixel 7 in Oracle Cloud)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android 15 run in a redroid container on the Oracle ARM VM, dressed as a Pixel 7, with an HTTP test door (pixel7d), a job mailbox and Mac helper commands.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/vm-android](https://github.com/markoboskoauroville/vm-android) |
| Also called | pixel7d, Pixel 7 container, redroid Pixel 7, mantra-sonobus |
| Visibility | public |
| Kind | service-daemon |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Linux, Cloud |
| Language | Python (plus C++ Mantra SonoBus) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: scrcpy-v5.0.1 |
| Control level | http (own http routes) |

## What it can do

- Run a Pixel 7-identity Android (redroid) beside Ubuntu on the cloud VM
- Serve pixel7d, a token-protected test door: health, install, test an APK, screenshot, logcat, tap, swipe, key, text, launch, stop, clear, shell, reset
- Accept test jobs through a GitHub mailbox (pixel7-jobs)
- Target other adb phones with ?device= or X-Device and list them
- Show the phone live on the Mac with scrcpy (built for arm64 by workflow)
- Include Mantra SonoBus: multichannel audio between own machines over Tailscale with a VU-meter strip

## Ask for it when

- test an Android APK in the cloud
- take a screenshot of the Android VM
- tap and type on the cloud Pixel 7
- run an Android test without a phone
- send multichannel audio between machines

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8897

Actions:

- `GET /api`
- `GET /health`
- `GET /devices`
- `GET /screenshot`
- `GET /logcat`
- `POST /install`
- `POST /test`
- `POST /uninstall`
- `POST /launch`
- `POST /stop`
- `POST /clear`
- `POST /tap`
- `POST /swipe`
- `POST /key`
- `POST /text`
- `POST /instrument`
- `POST /shell`
- `POST /reset`
- `pixel7 health|test <apk>|shot|tap|log|shell|reset|screen|--on <phone> (Mac command)`
- `phones enable|list|connect (Mac command)`

**Before you call:** Run on the Mac, where the pixel7 command is installed (mac/pixel7 into ~/.local/bin). The door pixel7d answers only on the VM's Tailscale address with header X-Mantra-Token (not on 127.0.0.1 of the Mac), so a session needs Tailscale to reach it.

Example:

```
pixel7 test app.apk # Mac command: installs, launches, screenshots the APK on the cloud Pixel 7
```

More calls:

- screenshot of the cloud phone: `pixel7 shot`
- tap at real pixels (screen 1080x2400): `pixel7 tap 540 1200`
- run an adb shell command on it: `pixel7 shell 'dumpsys activity top | head -40'`
- health, logcat, wipe back to a clean image: `pixel7 health ; pixel7 log ; pixel7 reset`

Evidence: api/pixel7d.py (routes ~lines 297-348), TAKEOVER.md table of doors

## Inputs / Outputs

Inputs:

- APK files
- job messages in the mailbox

Outputs:

- screenshots
- logcat
- test results

## Hardware

- Oracle Cloud Ampere A1 VM (no KVM)

## Works with

- Uses: [Chromium Virtual Machine (Mantra)](vm-chromium.md)
- Used by or talked to by: [VM Android jobs mailbox](vm-android-jobs.md), [Chromium Virtual Machine (Mantra)](vm-chromium.md)

## Code worth reusing

- `api/pixel7d.py`: Token-protected HTTP door over adb: install, test, tap, swipe, screenshot, logcat, shell
- `api/jobrunner.py`: Mailbox job runner using flock to share one phone between processes
- `mantra-sonobus/`: SonoBus-based multichannel audio sender/receiver with VU strip for Mac, Linux, Android

## Notes

pixel7d listens on the Tailscale address only and needs X-Mantra-Token (port 8897 also appears in the manifest for the pixel7d door). Android 16 image does not boot on this kernel (no ashmem). A 'machine' note: the VM has no /dev/kvm. Marko's real phone adb pairing waits for his 'Always allow'. Release tag scrcpy-v5.0.1 is scrcpy, not the app. For no-Tailscale, no-terminal use, the git mailbox vm-android-jobs drives the same phone. A real phone of the owner can be targeted with pixel7 --on `<phone>` after 'phones enable'.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/vm-android/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/vm-android/blob/HEAD/LESSONS.md)
