# Minimalist Stopwatch

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android stopwatch, timer and clock: black screen, huge white digits, three transport buttons, orientation lock and full-screen mode.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MINIMALIST_STOPWATCH](https://github.com/markoboskoauroville/MINIMALIST_STOPWATCH) |
| Also called | Minimalist Stopwatch |
| Visibility | public |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: yes; latest release: v49 |
| Control level | none (no control api found) |

## What it can do

- Run a stopwatch (S), a countdown timer (T) and a 24 h clock (R)
- Start/stop on tap, reset on double-tap or long press
- Pinch out to show only the digits, pinch in to restore
- Lock portrait or landscape
- Check for updates from GitHub releases
- Include voice, listening and birdsong helpers in code

## Ask for it when

- big stopwatch on the phone
- countdown timer readable across the room
- simple clock app

## How to control it

No control API found.

## Works with

- Used by or talked to by: [Sample Player, Android](SAMPLE_PLAYER.md), [Timer Stopwatch Clock (Mantra)](TIMER_STOPWATCH_CLOCK.md)

## Code worth reusing

- `app/src/main/java/com/mantra/stopwatch/Stopwatch.kt`: stopwatch and timer state logic
- `app/src/main/java/com/mantra/stopwatch/UpdateCheck.kt`: check GitHub releases for a newer APK

## Notes

The Kotlin sources include Voice, VoiceEngine, ListeningService, Birdsong and MaMeter files whose purpose is not described in the README parts read.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MINIMALIST_STOPWATCH/blob/HEAD/README.md)
