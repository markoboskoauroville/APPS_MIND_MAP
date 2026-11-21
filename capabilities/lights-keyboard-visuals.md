[Back to the index](../CAPABILITIES.md)

# Lights, keyboard and visuals

- show a picture on my keyboard lights -> [G815 Lights](../apps/G815_LIGHTS.md) (macOS; API: http 8877) - call: `curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"color":"ff0000"}'`
- light the G815 keys -> [G815 Lights](../apps/G815_LIGHTS.md) (macOS; API: http 8877)
- keyboard light show -> [G815 Lights](../apps/G815_LIGHTS.md) (macOS; API: http 8877)
- make my keyboard display what the app shows -> [G815 Lights](../apps/G815_LIGHTS.md) (macOS; API: http 8877)
- flash the keyboard when something happens -> [G815 Lights](../apps/G815_LIGHTS.md) (macOS; API: http 8877)
- show which key I am pressing on screen -> [Keyboard Monitor (Mantra)](../apps/keyboard-monitor.md) (macOS; API: cli) - call: `KeyboardMonitor --shot /tmp/k.png # picture of the keyboard monitor`
- display keystrokes for a screen recording or lesson -> [Keyboard Monitor (Mantra)](../apps/keyboard-monitor.md) (macOS; API: cli)
- control a Bluetooth LED light -> [Light Control (Mantra) (planned)](../apps/LIGHT_CONTROL.md) (PLANNED, not built; no API yet) - [kickoff prompt](../prompts/LIGHT_CONTROL.md)

## Retired - do not use

- [Stream Deck Control (Mantra), retired (retired)](../apps/stream-deck-control.md) - replaced by [Stream Deck Remote](../apps/STREAM_DECK_REMOTE.md)
