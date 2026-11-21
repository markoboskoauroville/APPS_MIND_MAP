# Cockpit Android

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that puts a 0-100 CPU number in the status bar and a health notification: RAM, battery, temperature, network speed, watts, recent apps with stop.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/COCKPIT_ANDROID](https://github.com/markoboskoauroville/COCKPIT_ANDROID) |
| Also called | Cockpit, phone cockpit |
| Visibility | public |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | none (no control api found) |

## What it can do

- Show CPU percent as the notification icon in the status bar (from cpuidle counters)
- Show RAM, swap, battery, thermal, uptime, storage and per-core load in a notification
- Show download and upload speed and battery watts when units are unambiguous
- Let the user pick which four numbers sit at the top
- Show recent apps with a stop button (via Shizuku if installed)
- Open the Termux cockpit page from a notification button

## Ask for it when

- show CPU usage in the Android status bar
- which apps use memory on my phone
- phone health notification
- kill a background app on Android

## How to control it

No control API found.

Evidence: none found; it only links to the Termux page at 127.0.0.1:8860

## Inputs / Outputs

Inputs:

- /sys cpuidle counters
- Usage access
- system battery and net totals

Outputs:

- status-bar number
- notification

## Works with

- Uses: [Cockpit Termux](COCKPIT_TERMUX.md)
- Used by or talked to by: [Cockpit Termux](COCKPIT_TERMUX.md)

## Code worth reusing

- `app/src/main/java/com/mantra/cockpit/Sampler.kt`: CPU percent from idle counters when /proc/stat is denied (Android 16)
- `app/src/main/java/com/mantra/cockpit/NumberIcon.kt`: draw a number as a status-bar notification icon

## Notes

Android 14+ forbids killing other apps and reading /proc/stat, so stopping apps needs the ADB bridge in COCKPIT_TERMUX or Shizuku. HANDOFF.md and DEVELOPMENT.md hold state and reasons.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/COCKPIT_ANDROID/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/COCKPIT_ANDROID/blob/HEAD/HANDOVER.md)
- [DEVELOPMENT.md](https://github.com/markoboskoauroville/COCKPIT_ANDROID/blob/HEAD/DEVELOPMENT.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/COCKPIT_ANDROID/blob/HEAD/HANDOFF.md)
