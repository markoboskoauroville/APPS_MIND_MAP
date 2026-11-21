# Mantra Voice Switch

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Claude Code mod: /vox on|off silences or enables spoken replies per chat and shows VOX state in the prompt bar.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_VOICE_SWITCH](https://github.com/markoboskoauroville/MANTRA_VOICE_SWITCH) |
| Also called | vox switch, /vox |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Linux |
| Language | TypeScript |
| Status | dormant |
| Last push | 2026-11-06 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Turn spoken replies off for one chat and refuse commands that would speak
- Stop a reading already playing
- Show VOX on/off in the one-line bar beside other Mantra mods

## Ask for it when

- mute the voice for this Claude chat
- turn spoken replies back on

## How to control it

No control API found. The catalog notes some code-level hooks only.

Actions:

- `/vox on`
- `/vox off`
- `/vox status`

Example:

```
/vox off
```

Evidence: README.md

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Code worth reusing

- `mod/hooks/register.tsx`: per-session switch stored in session state, plus tool-call refusal

## Notes

State is per chat session, default on. Installed as a Claude Code plugin from its marketplace file. Slash commands only; no HTTP.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
