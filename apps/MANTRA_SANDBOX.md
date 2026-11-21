# Mantra Sandbox

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Runs Android apps in a headless emulator with its own screen, touch and keys through adb, so automation never fights for the owner's mouse.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_SANDBOX](https://github.com/markoboskoauroville/MANTRA_SANDBOX) |
| Also called | sandbox, Mantra Sandbox |
| Visibility | public |
| Kind | cli-tool |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Android |
| Language | Shell |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Create and boot a headless Pixel 7 / Android 15 emulator in about 25 s
- Install APKs, or pull an installed app from the real phone and install it
- Tap, swipe, type, press keys and take screenshots through adb
- Dump UI elements with uiautomator
- Run plain-text macros in one adb call (about 0.4 s for ten taps)
- Forward Mac ports into the sandbox

## Ask for it when

- run an Android app without touching my screen
- test a phone app in an emulator by script
- drive CQ MixPad in the background
- automate an Android app in parallel with my own work

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `sandbox create`
- `sandbox start`
- `sandbox stop`
- `sandbox status`
- `sandbox install`
- `sandbox install-from-pixel <pkg>`
- `sandbox launch <pkg>`
- `sandbox landscape`
- `sandbox portrait`
- `sandbox shot [file]`
- `sandbox tap X Y [ms]`
- `sandbox qtap X Y`
- `sandbox swipe X1 Y1 X2 Y2 [ms]`
- `sandbox drag`
- `sandbox type "text"`
- `sandbox key <code>`
- `sandbox ui [word]`
- `sandbox run <file.macro> [k=v]`
- `sandbox redir udp|tcp <port>`
- `sandbox adb <args>`

**Before you call:** sandbox create once, sandbox start to boot the emulator; it has its own screen, touch and keys through adb so the owner's phone is never touched.

Example:

```
sandbox run macros/cqmixpad/tab_fader.macro # plays a recorded macro inside the headless Android emulator
```

More calls:

- install an app and open it: `sandbox install app.apk ; sandbox launch com.example.app`
- tap, swipe, type: `sandbox tap 540 1200 ; sandbox swipe 540 1800 540 600 300 ; sandbox type "hello"`
- screenshot: `sandbox shot ~/shot.png`
- status: `sandbox status`

Evidence: TAKEOVER.md 'The command' section; bin/sandbox

## Inputs / Outputs

Inputs:

- APK files
- macro files

Outputs:

- screenshots
- app state in the emulator

## Hardware

- Android emulator (AVD mantra_sandbox, serial emulator-5580)

## Works with

- Talks to: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md), [CQ MixPad Protocol](cq_mixpad_protocol.md)
- Used by or talked to by: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md), [Screen Copy (Mantra)](MANTRA_SCREEN_COPY.md)

## Code worth reusing

- `bin/sandbox`: adb wrapper: headless AVD lifecycle, input, uiautomator dump, macro runner
- `macros/cqmixpad/`: ready macros for CQ MixPad tabs, layers, gain/gate/comp/PEQ panels and faders

## Notes

v2 (macOS VM for Mac apps) needs a 15 GB IPSW and only with the owner's yes. Some apps ignore a bare tap, so tap is a held press.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_SANDBOX/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_SANDBOX/blob/HEAD/LESSONS.md)
