# DaVinci Resolve Assistant (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [DaVinci Resolve Actions (Mantra)](DAVINCI_RESOLVE_ACTIONS.md). Replaced by DAVINCI_RESOLVE_ACTIONS.

**Older set of Resolve menu scripts (Toggle HD UHD, Previous Page, Create Timeline) with a self-check and the star menu's UHD/HD badge and page turner.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DAVINCI_RESOLVE_ASSISTANT](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ASSISTANT) |
| Also called | DaVinci Resolve Assistant, resolve-scripts, enterprise-grade code |
| Visibility | public |
| Kind | cli-tool |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Lua + Python |
| Status | retired |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Toggle project and timeline between 1920x1080 and 3840x2160
- Go back to the previous Resolve page
- Create a timeline from selected Media Pool clips named after the first clip
- Self-check: Resolve up, API answers, project, resolution, page, scripts current (exit 0 when all well)
- Install the three scripts into Resolve's Scripts/Utility folder

## Ask for it when

- toggle HD and UHD in Resolve
- previous page in DaVinci Resolve
- make a timeline from selected clips

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `python3 check.py`
- `python3 'Toggle HD UHD.py' --read`
- `./install.sh`

**Before you call:** Superseded by DAVINCI_RESOLVE_ACTIONS (router on 8940), which absorbed these scripts.

Example:

```
python3 check.py
```

More calls:

- read the HD/UHD state: `python3 'Toggle HD UHD.py' --read`

Evidence: README.md (check.py, --read), CLAUDE.md

## Inputs / Outputs

Inputs:

- DaVinci Resolve scripting API

Outputs:

- ~/.config/hdbadge.json
- log ~/.config/resolve-assistant.log

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)

## Code worth reusing

- `Create Timeline.py`: timeline from selected Media Pool clips
- `star/pages_helper.py`: page ring and back-one-page logic shared with the star

## Notes

Default branch is master. Superseded in practice by DAVINCI_RESOLVE_ACTIONS (same scripts plus the router and an app). Prefer that repo for any new Resolve work. Every failure is logged with time; no network API. RETIRED/SUPERSEDED: use DAVINCI_RESOLVE_ACTIONS instead.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ASSISTANT/blob/HEAD/README.md)
- [CLAUDE.md](https://github.com/markoboskoauroville/DAVINCI_RESOLVE_ASSISTANT/blob/HEAD/CLAUDE.md)
