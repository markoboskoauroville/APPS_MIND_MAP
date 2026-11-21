[Back to the index](../CAPABILITIES.md)

# Lights, keyboard and visuals

### [G815 Lights](../apps/G815_LIGHTS.md)

macOS; API: http 8877. Main call: `curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"color":"ff0000"}'`

Before: The G815 Lights app must be running (if GET /status does not answer, open ~/Developer/G815_LIGHTS/build/"G815 Lights.app"). Loopback only.

- show a picture on my keyboard lights (G815 Lights) - call: `build/g815 frame ~/Pictures/pic.png contain # from the repo checkout; or: curl -s -XPOST '127.0.0.1:8877/frame?fit=cover&ttl=20' -H 'Content-Type: image/png' --data-binary @pic.png`
- light the G815 keys (G815 Lights)
- keyboard light show (G815 Lights)
- make my keyboard display what the app shows (G815 Lights)
- flash the keyboard when something happens (G815 Lights)

### [Keyboard Monitor (Mantra)](../apps/keyboard-monitor.md)

macOS; API: cli. Main call: `KeyboardMonitor --shot /tmp/k.png # picture of the keyboard monitor`

- show which key I am pressing on screen (Keyboard Monitor)
- display keystrokes for a screen recording or lesson (Keyboard Monitor)

- control a Bluetooth LED light -> [Light Control (Mantra) (planned)](../apps/LIGHT_CONTROL.md) (PLANNED, not built; no API yet) - [kickoff prompt](../prompts/LIGHT_CONTROL.md)

## Retired - do not use

- [Stream Deck Control (Mantra) (retired)](../apps/stream-deck-control.md) - replaced by [Stream Deck Remote](../apps/STREAM_DECK_REMOTE.md)
