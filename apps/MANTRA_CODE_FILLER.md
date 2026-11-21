# Code Filler (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that watches an Android phone over adb for new verification codes and types the code into the focused text box on the Mac, or copies it with a bubble.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_CODE_FILLER](https://github.com/markoboskoauroville/MANTRA_CODE_FILLER) |
| Also called | Code Filler, security code filler |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Android |
| Language | Swift |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Poll an Android phone over adb for new messages and notifications
- Detect a verification code and fill it into the focused field through Accessibility
- Fall back to the clipboard with a notice and restore the clipboard after two minutes
- Fill the newest recent code again from a global hotkey
- Never press Submit; keep codes in memory only

## Ask for it when

- fill the SMS verification code on the Mac
- copy the login code from the phone automatically

## How to control it

No control API found.

Evidence: none found; global hotkey only

## Hardware

- Android phone over adb

## Notes

Privacy: codes stay in memory and are never logged.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
