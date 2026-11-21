# Brain Brake Keyboard (Hammerspoon) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** GitHub marks it archived.

**Marko's Hammerspoon keyboard: clipboard buckets for imgtoimg and Suno, F-key actions, voice key, and a hand that drives imgtoimg.ai.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAIN_BRAKE_KEYBOARD](https://github.com/markoboskoauroville/BRAIN_BRAKE_KEYBOARD) |
| Also called | Buckets, the hand, keyboard app, Brain Break keyboard |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Hammerspoon |
| Language | Lua (+ Python) |
| Status | retired |
| Last push | 2026-09-06 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Paste next bucket (reference image, prompt, file name; lyrics, style, exclude for Suno) with F2
- Press buttons in the imgtoimg page: Use Image URL (F4), Save (F6), left click (F3)
- Fire a key from one spoken word (voice.lua, F7)
- Run an extended hand job from the terminal (hand.sh, hand_job.py)
- Serve the same shortcut menu as a page on port 8823 with a deck of SCREENSHOT, TEST, PLAY, STOP
- Open Path Finder from the trackball button

## Ask for it when

- drive imgtoimg.ai from the keyboard
- clipboard buckets for prompts
- voice word triggers a key
- Hammerspoon keyboard for the film

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `hand.sh`
- `hand_job.py`
- `hand_deliver.py`
- `confirm_screen.py`
- `push_original.py`
- `measure_colour.py`

**Before you call:** Retired in practice: the Hammerspoon keyboard of the Brain Brake film; the map of the actions is scripts only (hand.sh, hand_job.py, hand_deliver.py). Not enough evidence for an HTTP call.

Example:

```
bash hand.sh # the hand-over script; there is no HTTP call documented except the menu page on 8823
```

Evidence: README.md, HOW_TO_STOP_KEYBOARD.md line 231 (page on 8823); hand.sh is a terminal front end. No documented action API.

## Inputs / Outputs

Inputs:

- keys and trackball
- microphone (voice key)
- imgtoimg.ai page

Outputs:

- key presses and clicks
- saved originals pushed with push_original.py

## Hardware

- Kensington trackball

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Talks to: [Brain Brake originals](BRAIN_BRAKE_ORIGINALS.md)

## Code worth reusing

- `paste_queue.lua`: clipboard bucket queue with a menu
- `voice_match.py`: match a spoken word to a key command
- `tests/run_tests.sh`: the four-tests runner pattern for Hammerspoon modules

## Notes

GitHub marks it archived. Paths are hard-coded to ~/Developer/brain_break/tools/keyboard. Booted by the star menu, not init.lua. Handover file BRAIN_BREAK_HANDOVER.md also documents the older speak/chat server; that lives on as CCMC. RETIRED/SUPERSEDED: no replacement is named in the docs.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_KEYBOARD/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_KEYBOARD/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_KEYBOARD/blob/HEAD/LESSONS.md)
