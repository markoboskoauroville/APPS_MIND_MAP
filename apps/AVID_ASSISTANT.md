# Avid Assistant

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**AutoHotkey v2 suite for a Windows edit suite around Avid Media Composer: macros, window handling, monitor setup.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/AVID_ASSISTANT](https://github.com/markoboskoauroville/AVID_ASSISTANT) |
| Also called | A1 Assistant, A1_ASSISTANT |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | Windows |
| Language | AutoHotkey v2 |
| Status | dormant |
| Last push | 2026-09-03 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Run recorded mouse macros in Avid with an interruptible stop key
- Step-run mode with red crosshair to confirm each click
- Translate recorded 2K coordinates to a 1080p desk
- Generate export names and convert archive names
- Pin windows on top and move them between monitors
- Set monitor environment (primary monitor, taskbar)

## Ask for it when

- automate Avid Media Composer clicks
- stop a running macro
- set up the edit suite monitors on Windows

## How to control it

No control API found.

Evidence: none found (hotkey-driven AutoHotkey scripts)

## Hardware

- two-monitor Windows workstation
- OpenRGB lighting (optional)

## Code worth reusing

- `scripts/A1_ASSISTANT/A1_ASSISTANT_v100_classic.ahk`: interruptible sleep (AbSleep) and coordinate mapping (MapPoint) for macros

## Notes

Superseded versions kept as history; run only one of the 2K or 1080 editions. HANDOFF.md and rules.md exist in the repo.

## Docs in the repo

- `README.md`
