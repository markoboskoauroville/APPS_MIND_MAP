# Claude Remote (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Claude Code mod that draws one status line under the prompt: router, model, session and week usage, skill, context, remote control, voice, permission mode.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLAUDE_REMOTE](https://github.com/markoboskoauroville/CLAUDE_REMOTE) |
| Also called | Claude Remote mod, Claude Code status line |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | TypeScript, Python |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Show model, session and week usage and context in one status line
- Show the last-used skill
- Show toggles for remote control, voice and router
- Read state files written by the router and voice-switch mods

## Ask for it when

- show usage in the Claude Code status line
- install the Claude Code status bar mod

## How to control it

No control API found.

Evidence: none found; slash commands /router and /vox belong to sibling mods

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md)

## Code worth reusing

- `statusline-usage.py`: status line script that writes per-session usage JSON to a cache folder

## Notes

Not the same as MANTRA_REMOTE (VNC/Tailscale remote); name chosen to avoid the clash.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
