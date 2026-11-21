# Clean Start (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Lists everything non-Apple that starts by itself on the Mac and switches it all off for the next boot (CLEAN START) or back (NORMAL START).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLEAN_START](https://github.com/markoboskoauroville/CLEAN_START) |
| Also called | Clean Start, clean boot |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v5 |
| Control level | none (no control api found) |

## What it can do

- List login items, launch agents and daemons grouped by kind with vendor and command
- CLEAN START: disable every non-Apple auto-start for the next login and boot
- NORMAL START: restore exactly the earlier state except what Marko switched himself
- Remember each personal choice and keep it in both modes
- Never touch or list Apple items as switchable (shows only the count)

## Ask for it when

- boot the Mac without any extra programs
- what starts by itself on my Mac
- turn off all startup items
- restore my startup items

## How to control it

No control API found.

Evidence: none found; Queen skill file skills/clean-start/SKILL.md exists but its chat route returned 502

## Inputs / Outputs

Inputs:

- LaunchAgents, LaunchDaemons, login items

Outputs:

- changed start settings for next boot

## Code worth reusing

- `app/Engine.swift`: enumerate and toggle launchd and login items with memory of user choices
- `tools/ax.py`: accessibility helper for window tests

## Notes

Status CLOSED 21.11.2026 at v5. Nothing running is stopped; changes apply to the next start. SIP is off on this Mac. Open questions listed in TAKEOVER.md: a root daemon pointing at a missing path and whether some helpers stay on in a Clean.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/CLEAN_START/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/CLEAN_START/blob/HEAD/LESSONS.md)
