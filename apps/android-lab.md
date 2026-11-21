# Android Lab

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One command (droid) that builds, installs, tests and screenshots an Android app on a Pixel 7 emulated on the Mac.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/android-lab](https://github.com/markoboskoauroville/android-lab) |
| Also called | droid, android bench, Pixel 7 emulator bench |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | macOS, Android |
| Language | Bash, Python, C |
| Status | active |
| Last push | 2026-09-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Start and stop an emulated Pixel 7 (API 35, arm64) and wait until it has really booted
- Build, install and launch the Android project you are standing in
- Take screenshots off the emulator
- Run structural gates and unit tests with counts
- Keep every built APK under a stamped name plus latest-debug.apk
- Upload the newest APK to a Drive folder (droid publish)
- Tap UI elements by visible text instead of pixels

## Ask for it when

- test an Android app on the Mac
- build an APK locally
- start the Pixel 7 emulator
- take a screenshot of the emulated phone
- run Android unit tests locally
- publish a local APK build

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `doctor`
- `up`
- `run`
- `shot`
- `test`
- `kept`
- `publish`
- `down`
- `tap-text`
- `build`

**Before you call:** Run from inside an Android project folder; droid up starts the emulator, droid down stops it.

Example:

```
droid run # from inside any Android project under ~/Developer: builds, installs and starts it in the headless emulator
```

More calls:

- check the toolchain: `droid doctor`
- screenshot of the emulator: `droid shot`
- run the project's tests: `droid test`

Evidence: README.md, TAKEOVER.md (single script 'droid')

## Inputs / Outputs

Inputs:

- Android Gradle project (settings.gradle.kts)

Outputs:

- debug APKs
- screenshots
- test counts

## Hardware

- Apple Silicon Mac (emulator)

## Code worth reusing

- `droid`: bash driver: Java 17 selection, emulator boot wait, build, sign, keep APK, tap-text via view tree
- `find_node.py`: find a UI node by text in the Android view tree
- `ndi_find.c`: small NDI source finder/receiver used to check emulator NDI streams

## Notes

Local loop only; does not publish to GitHub and runs no instrumented tests. NDI over the emulator works only through a port forward, not real multicast. Local builds are signed with the project's real key kept outside the repo.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
- `NETWORK.md`
