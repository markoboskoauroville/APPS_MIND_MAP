# Stream Deck Control (Mantra) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Stream Deck Remote](STREAM_DECK_REMOTE.md). Replaced by STREAM_DECK_REMOTE.

**Obsolete Mac app that drove the original Elgato Stream Deck over USB as an app switcher and F1/F2 keys; replaced by Stream Deck Remote.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/stream-deck-control](https://github.com/markoboskoauroville/stream-deck-control) |
| Also called | stream deck control |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Lights, keyboard and visuals](../capabilities/lights-keyboard-visuals.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-11-06 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | accessibility (accessibility button ids only) |

## What it can do

- Drive the 15-key Stream Deck directly over USB HID without Elgato's software
- Put every open app on a key with its icon and bring it to front on press
- Send F1 and F2 to the front app from keys
- Expose its controls as Accessibility buttons (off, top, close, key1 to key15)

## Ask for it when

- use the Stream Deck as an application switcher
- drive a Stream Deck without the Elgato app

## How to control it

- Level: **accessibility**
- Type: accessibility

Actions:

- `off`
- `top`
- `close`
- `key1..key15`
- `appSwitcher`
- `functionKeys`

**Before you call:** No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

Example:

```
star press "stream deck control" "key1"
```

More calls:

- list the controls of the window: `star read "stream deck control"`
- start the app in the background: `star open "stream deck control"`
- quit it: `star quit "stream deck control"`

Evidence: README.md (every control is an Accessibility button)

## Hardware

- Elgato Stream Deck original 15-key (0x0fd9:0x0060)

## Works with

- Uses: [Stream Deck Remote](STREAM_DECK_REMOTE.md)

## Code worth reusing

- `app/Deck.swift`: IOKit HID driver for the original Stream Deck: key images, presses, brightness

## Notes

Obsolete since 6.11.2026; replaced by Stream Deck Remote (Mantra). Only the original 0x0060 model is matched. Elgato's app must be closed while it runs. RETIRED/SUPERSEDED: use STREAM_DECK_REMOTE instead.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
