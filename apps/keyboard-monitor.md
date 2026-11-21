# Keyboard Monitor (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac menu-less app showing one big blob with the key just pressed, including modifiers, function and media keys.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/keyboard-monitor](https://github.com/markoboskoauroville/keyboard-monitor) |
| Also called | keyboard monitor, key blob |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Lights, keyboard and visuals](../capabilities/lights-keyboard-visuals.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Show the last pressed key in a 300x300 floating glass blob
- Show left/right modifiers, Caps Lock, Fn, arrows, F1-F20, keypad and media keys
- Quit from the blob's close button
- Take an off-screen screenshot of a given key for checking (--shot)

## Ask for it when

- show which key I am pressing on screen
- display keystrokes for a screen recording or lesson

## How to control it

- Level: **cli**
- Type: cli, accessibility

Actions:

- `--shot <png> [glyph] [name]`
- `--shot <png> --missing`
- `AX off`
- `AX permissions`

Example:

```
KeyboardMonitor --shot /tmp/k.png # picture of the keyboard monitor
```

More calls:

- the keys that are missing: `KeyboardMonitor --shot /tmp/k.png --missing`

Evidence: README.md, TAKEOVER.md

## Inputs / Outputs

Inputs:

- global key events (needs Accessibility permission)

Outputs:

- on-screen key blob

## Code worth reusing

- `app/Keys.swift`: listen-only CGEventTap decoding keys, modifiers left/right and media keys
- `app/Blob.swift`: borderless non-activating HUD-glass floating panel

## Notes

Accessory app (no Dock icon, no window), listed in the star menu under Keyboard and mouse. Keeps no history.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
