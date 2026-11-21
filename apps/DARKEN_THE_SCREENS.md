# Screen Brightness Automatic (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Toggle that sets every Mac display to 0 percent brightness and back to 100, through BetterDisplay, keeping VNC screenshots intact.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DARKEN_THE_SCREENS](https://github.com/markoboskoauroville/DARKEN_THE_SCREENS) |
| Also called | Darken the Screens, Screen Brightness Automatic, SCR BRI, sunmoon |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | none (no control api found) |

## What it can do

- Darken all displays together to hardware and software brightness 0
- Light all displays back to 1.0
- Toggle from a notification or a key (control-option-command-F1)
- List displays with BetterDisplay get -identifiers

## Ask for it when

- turn off my screens without sleeping the Mac
- darken both monitors
- set brightness to zero on all displays

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- BetterDisplay CLI

Outputs:

- display brightness changes

## Hardware

- built-in display
- BenQ monitor

## Works with

- Uses: [Star (Mantra), Swift menu](STAR_SWIFT.md)

## Notes

Bundle id and the toggle notification keep the old name com.mantra.darkenthescreens so permissions and the star switch survive. Earlier approaches (gamma to zero, brightness key presses) failed or blacked out VNC. Confirmed working by Marko 2.11.2026. Toggle is via a notification, no HTTP API.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/DARKEN_THE_SCREENS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/DARKEN_THE_SCREENS/blob/HEAD/LESSONS.md)
