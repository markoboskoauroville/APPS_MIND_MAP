# Termux Emulator Image

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Ready-made 5 GB Android emulator disk (Termux, Ubuntu in proot, Claude Code installed) in split parts for Claude Code cloud sessions; restore, never rebuild.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/termux-emulator-image](https://github.com/markoboskoauroville/termux-emulator-image) |
| Also called | Termux AVD image, cloud Android emulator image |
| Visibility | public |
| Kind | data |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux, Linux, Cloud |
| Language | none (binary parts) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Provide the 'termux' Android 11 x86_64 AVD as 54 split zstd parts with SHA256SUMS
- Restore into a cloud session through MANTRA_MANIFEST tools/cloud-android/termux-emulator.sh (restore, start, tx, type, save)

## Ask for it when

- test Termux apps in a cloud session
- get an Android emulator with Termux and Claude Code in the cloud
- restore the Termux emulator

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `termux-emulator.sh restore|start|tx|type|save (tool lives in MANTRA_MANIFEST, not here)`

**Before you call:** From a MANTRA_MANIFEST checkout.

Example:

```
bash tools/cloud-android/termux-emulator.sh restore (in a MANTRA_MANIFEST checkout)
```

More calls:

- start the saved emulator: `bash tools/cloud-android/termux-emulator.sh start`
- type into it: `bash tools/cloud-android/termux-emulator.sh type "ls"`

Evidence: TAKEOVER.md (former README)

## Inputs / Outputs

Inputs:

- attach this repo to the session

Outputs:

- restored AVD ~/.android/avd/termux.avd

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md)

## Notes

Do not git clone (5 GB pack is cut off by the session proxy); the tool downloads parts via the GitHub contents API (about 95 s). x86_64 only: proves Termux packages, proot and Claude Code x64, nothing about ARM. Claude Code inside is not logged in. Built 16.10.2026. api.txt was skipped (large).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/termux-emulator-image/blob/HEAD/TAKEOVER.md)
