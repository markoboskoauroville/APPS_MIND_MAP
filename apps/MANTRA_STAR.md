# Star (Mantra), Lua (Hammerspoon, legacy)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Legacy Lua version of the star menu in Hammerspoon; the current star is STAR_SWIFT (Star (Mantra), Swift menu).**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_STAR](https://github.com/markoboskoauroville/MANTRA_STAR) |
| Also called | Star Menu, David star, the star, Hammerspoon star |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Hammerspoon |
| Language | Lua |
| Status | dormant |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Show every Mantra app with an on/off tick and run it on demand
- Group apps in folders and remember which were ticked
- Open an app's web page from a WEB button
- Provide a search box with about/detail text per app
- Host Ableton assistant, keyboard and MIDI Lua apps
- Expose its app list and toggles to other programs

## Ask for it when

- start or stop one of my Mac apps from the menu bar
- see all my apps in one menu
- turn all apps off
- restart Hammerspoon with the same apps ticked

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `STAR.list()`
- `STAR.toggleKey(key)`
- `STAR.allOff()`
- `STAR.quitAll()`
- `STAR.openPageKey(key)`

**Before you call:** Legacy Lua star in Hammerspoon (the Swift menu is STAR_SWIFT); Hammerspoon with its hs command-line tool must be installed and running.

Example:

```
hs -c 'print(hs.json.encode(STAR.list()))' # Hammerspoon command line; lists the star rows
```

More calls:

- switch an app of the star on or off by its key: `hs -c 'STAR.toggleKey("timer")'`
- everything off: `hs -c 'STAR.allOff()'`

Evidence: TAKEOVER.md item 9 (What the outside may call)

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Mantra Voice (speech server)](MANTRA_VOICE.md), [Launcher (Mantra)](STAR_LAUNCHER.md)
- Talks to: [Star API (Mantra)](STAR_API.md)
- Used by or talked to by: [Ableton Command Guide](ABLETON_COMMAND_GUIDE.md), [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md), [Teacher Lessons and Scripts (Ableton, DaVinci)](ABLETON_TEACHER.md), [App Store (Mantra)](APP_STORE.md), [Brain Brake Keyboard (Hammerspoon) (retired)](BRAIN_BRAKE_KEYBOARD.md), [Brain Brake review wall](BRAIN_BRAKE_REVIEW.md), [Claude Code Monitor (Mantra) (retired)](CLAUDE_CODE_MONITOR.md), [DaVinci Resolve Assistant (retired)](DAVINCI_RESOLVE_ASSISTANT.md), [djay Sync (Mantra), Mac window](DJING_SYNC.md), [Find a File (Mantra)](FIND_FILE.md), [Free Mac](FREE_MAC.md), [Indian Mantras (Mantra)](INDIAN_MANTRAS.md), [Installation Logger (Mantra)](INSTALLATION_LOGGER.md), [Dock Switcher (Mantra)](MACOS_TASK_SWITCHER.md), [Macro Recorder (Mantra)](MANTRA_MACRO.md), [Automated Mouse Actions (Mantra)](MANTRA_MOUSE.md), [MIDI to Key Stroke](MIDI_TO_KEYSTROKE.md), [Launcher (Mantra)](STAR_LAUNCHER.md), [Star (Mantra), Swift menu](STAR_SWIFT.md), [Talk with Claude Code](TALK_WITH_CLAUDE.md), [Mantra Mackie Control Translator](mantra-mackie-control-translator.md), [Find a File Spotlight (Mantra) (retired)](spotlight.md)

## Code worth reusing

- `spawn.lua`: start servers from Hammerspoon without hs.execute
- `a1_osc.lua`: pure Lua OSC encode/decode for AbletonOSC
- `a1_ears.py`: OSC wire helper for Live questions

## Notes

Legacy Lua star; Swift STAR_SWIFT with rows.json is the newer menu (not in this list). Restart with ./restart.sh before testing. App files each declare name, key, running, start, stop, optional about/detail/url. HTTP door for apps is STAR_API, not this repo.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
- `CLAUDE.md`
