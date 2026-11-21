# Macro Recorder (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac macro recorder and AutoHotkey-like script engine: records and plays macros, finds buttons by picture or OCR, presses buttons in any app, guards input.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_MACRO](https://github.com/markoboskoauroville/MANTRA_MACRO) |
| Also called | Macro Recorder, Macro Recorder (Mantra), macro, AutoHotkey on the Mac, MARCO_MACRO_RECORDER, guard |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Linux |
| Language | Swift (Mac), Python/GTK (Linux), legacy Lua |
| Status | active |
| Last push | 2026-11-19 |
| Build / release | GitHub workflow: yes; latest release: v31 |
| Control level | http (own http routes) |

## What it can do

- Record and play macros, ten slots on digit keys, saved as readable .ahk-style scripts
- Edit scripts in a built-in editor that suggests the next command
- Find a button on screen from a picture (ScreenCaptureKit template match)
- Capture screen, rectangle, window or page; OCR text and click, wait for or find text
- Read and press UI elements through accessibility (ax-read, ax-press, ax-focus-end)
- Move, snap and list windows and displays (Rectangle actions)
- Lock the user's input while Claude acts (lock/unlock/request) and pause/resume all work
- Run on Linux through GTK + xdotool with the same verbs where possible

## Ask for it when

- automate the Mac mouse and keyboard
- record a macro and replay it
- click a button I can describe or screenshot
- read text off the screen
- press a button in another app through accessibility
- lock keyboard while Claude types
- guard my keyboard while Claude uses the mouse
- stop typing going into the wrong window during automation

## How to control it

- Level: **http**
- Type: cli, http
- Port: 8829

Actions:

- `macro run`
- `macro do`
- `macro record`
- `macro capture-screen`
- `macro capture-rect`
- `macro capture-window`
- `macro capture-page`
- `macro ocr`
- `macro find-text`
- `macro click-text`
- `macro wait-text`
- `macro win-list`
- `macro win-move`
- `macro win-snap`
- `macro ax-read`
- `macro ax-press`
- `macro ax-focus-end`
- `macro lock`
- `macro unlock`
- `macro lock-status`
- `macro request`
- `macro pause [who]`
- `macro resume [who]`
- `macro pause-status`
- `macro recalibrate`
- `macro view`
- `macro trigger`
- `macro login-dialog`
- `macro file-rename`
- `macro has`
- `macro skills`
- `POST :8829/pause`
- `POST :8829/resume`
- `GET :8829/pause`
- `guard (command on PATH)`

**Before you call:** Macro Recorder (Mantra) must be running on the Mac; it holds the Accessibility and Screen Recording permissions, so every other app asks it to press and capture. macro run plays a macro stored under ~/.mantra_macro/macros by its exact name.

Example:

```
macro run "Resolve - Voice Convert Render"
```

More calls:

- press a button in ANY running Mac app by its label (exact, then prefix, then part; case and spaces ignored): `macro ax-press "Safari" "Reload" # the inbox form is ax-press: <app> | <label>; list the labels first with: macro ax-read "Safari"`
- run a one-off script (AutoHotkey-v2 syntax) in one request: `macro do 'WinActivate "DaVinci Resolve" Send "{Space}"'`
- picture of one window, even behind others: `macro capture-window "Resolve" ~/shot.png`
- pause all its work, and read the state: `curl -s -XPOST 127.0.0.1:8829/pause -d '{"by":"claude"}' # resume: POST /resume, state: GET /pause`

Evidence: README.md, TAKEOVER.md (v24 lock, v29 pause, Linux verbs), app/App.swift header

## Inputs / Outputs

Inputs:

- screen pixels
- accessibility tree
- scripts in ~/.mantra_macro

Outputs:

- synthetic input events
- screenshots, OCR text
- script files

## Hardware

- Mac display and input devices

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Talks to: [MAI Worker (maiwork)](MAI_WORKER.md), [Mantra Chrome Extensions](MANTRA_CHROME_EXTENSIONS.md)
- Used by or talked to by: [Claude Control (Mantra)](CLAUDE_CONTROL.md), [Macro Skills](MACRO_SKILLS.md), [MAI Worker (maiwork)](MAI_WORKER.md), [Mantra Chrome Extensions](MANTRA_CHROME_EXTENSIONS.md), [Keyboard and Mouse Router (Mantra), retired (retired)](MANTRA_KEYBOARD_MOUSE_ROUTER.md), [Mantra Remote Viewing (Mantra Remote)](MANTRA_REMOTE_VIEWING.md), [Star API (Mantra)](STAR_API.md), [Talk Mode (Mantra)](TALK_MODE.md), [Queen auto-update (Groq Auto Update)](groq-auto-update.md), [Queen (Groq AI Studio), server and tools](groq_ai_studio.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) will be driven by this app (presses its accessibility buttons)

## Code worth reusing

- `app/AX.swift`: accessibility tree read/press
- `app/Ocr.swift`: screen OCR
- `app/Eye.swift`: template-match finder with ScreenCaptureKit and Accelerate
- `app/Lock.swift`: input lock with event tap
- `app/Guard.swift`: input guard with owner queue and focus restore
- `app/Pause.swift`: PauseGate for pause/resume of all work
- `app/Layouts.swift`: window layouts (from Rectangle, see THIRD_PARTY)
- `linux/mantra_macro/verbs.py`: Linux versions of the macro verbs

## Notes

This is the app-driving tool other repos rely on. The Mac README says the web page on :8829 is gone, while TAKEOVER (v24+) and app header say HTTP :8829 answers lock/pause on loopback; treat HTTP as loopback only. Linux build lacks accessibility, capture-page, layout, real input lock. Includes third-party Rectangle license. MARCO_MACRO_RECORDER is a separate stub. Pressing works on any running app (AX.swift: ax-press matches the app by name among running apps, then the control by title, description or value). Does not work on the Linux build. The exact CLI split of arguments for ax-press (macro ax-press `"<app>"` `"<label>"`) follows the pattern of ax-read in the README; the inbox form in the source is certain.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_MACRO/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_MACRO/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_MACRO/blob/HEAD/LESSONS.md)
