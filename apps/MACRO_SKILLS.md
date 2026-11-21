# Macro Skills

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Catalogue of Mac actions the Macro Recorder already knows; any app or session asks it first with macroskill has before clicking or typing.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MACRO_SKILLS](https://github.com/markoboskoauroville/MACRO_SKILLS) |
| Also called | Macro Skills, macroskill |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python (Markdown action cards, AutoHotkey-syntax macros) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Search stored macro actions by words and return how to run them
- Run a stored macro by id with arguments
- List, show and check actions and sync macro copies into the repository
- Add a new action card after a macro is built
- Return JSON for programs
- Store rules for Chrome, Gemini, NDI monitor and pause/resume actions

## Ask for it when

- is there already a macro for this
- snap a window left
- switch the Gemini account
- pause all macros
- pick an NDI monitor source

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `macroskill has`
- `macroskill has --json`
- `macroskill run <id>`
- `macroskill list`
- `macroskill show <id>`
- `macroskill check`
- `macroskill sync`
- `macroskill add`
- `macro has`
- `tools/sonycam connect|start|stop|status|front|away`

**Before you call:** macroskill has searches the stored macros by words (id, title, app, tags); only if it finds nothing, build the macro in Macro Recorder (MANTRA_MACRO) and then macroskill add it. Installed as ~/.local/bin/macroskill.

Example:

```
macroskill has --json "snap a window left"
```

More calls:

- play a found macro: `macroskill run <id> # same as macro run "<macro name>"`
- register a new macro after building it: `macroskill add "<macro name>" --title "Snap window left" --app Finder --tags "window, snap" --needs "Accessibility"`
- press a button in any Mac app (Macro Recorder command, not a stored macro): `macro ax-press "<app>" "<label>"`
- Sony camera REC through Imaging Edge Remote (Accessibility), Mac over USB: `tools/sonycam start # also: connect, stop, status, front, away`

Evidence: README.md; TAKEOVER.md

## Works with

- Uses: [Macro Recorder (Mantra)](MANTRA_MACRO.md)

## Code worth reusing

- `macro_skills.py`: the has/run/add/sync command over action cards
- `actions/`: one markdown card per stored action with id, app, kind, needs and state

## Notes

Ask here first before building any new UI automation; if not found, build the macro, then add it. The Accessibility steps themselves (ax-press, ax-read, win-snap, capture-window, ocr) are Macro Recorder commands, see MANTRA_MACRO; macroskill is only the index of stored macros. tools/sonycam (connect|start|stop|status|front|away) drives Sony Imaging Edge Remote by Accessibility to start REC on the camera card; named in the manifest module sony-remote-wifi, not checked in this repo's docs.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
