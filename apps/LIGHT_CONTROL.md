# Light Control (Mantra) (planned)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Connections](../CONNECTIONS.md)

> **PLANNED - not built yet.** There is no repository and no API. The kickoff prompt is [prompts/LIGHT_CONTROL.md](../prompts/LIGHT_CONTROL.md).

**Planned Mac app that drives a Neewer Bluetooth LED light with smooth colour transitions and a local API, linked to Meditation Room and, through Webcam Recorder, to a Sony camera.**

| Fact | Value |
|---|---|
| Status | planned |
| App id | light-control |
| Also called | Mantra Neewer, Light Control (Mantra), Neewer light control |
| Category | [Lights, keyboard and visuals](../capabilities/lights-keyboard-visuals.md) |
| Platforms | macOS |

## What it is meant to do

- Find the light over Bluetooth LE and expose every function it has
- Change colour and colour temperature with smooth transitions
- Calibrate the light from the picture of a Sony Alpha 7 V, reached only through Webcam Recorder
- Breathe the light slowly at brainwave pace (alpha, theta) to set a mood in the room
- Follow the colours of the Meditation Room visualization, and be driven by it

## Ask for it when

- control a Bluetooth LED light
- set the room light colour or colour temperature
- make the room light follow the meditation visuals
- pulse the light slowly in alpha or theta rhythm

Until it is built, no app does this: see the planned links below for what exists today.

## Hardware

- Neewer Bluetooth LED light
- Sony Alpha 7 V (through Webcam Recorder)

## Planned links

Arrow: `->` this app calls the other, `<-` the other calls this app, `<->` both.

- <-> [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](MANTRA_ROOM.md) [door 8965]: room drives the light; the light follows the visualization colours
- -> [Webcam Recorder (Mantra) (web-cam-viewer)](web-cam-viewer.md) [http 8867]: the only road to the Sony camera
- -> [Mantra Ports (MANTRA_PORTS)](MANTRA_PORTS.md): claims the port id light-control
- <- Mantra Door and mantra_remote.py (not a repo on this map): calls the light's actions
- <- [Queen (Groq AI Studio), server and tools (groq_ai_studio)](groq_ai_studio.md): Queen can drive it through the API
- <- [Macro Recorder (Mantra) (MANTRA_MACRO)](MANTRA_MACRO.md): presses its accessibility buttons
- -> [G815 Lights (G815_LIGHTS)](G815_LIGHTS.md) [http 8877]: optional, through the G815 Lights API only, never direct

Keywords: bluetooth, ble, led, light, neewer, brainwave, alpha, theta
