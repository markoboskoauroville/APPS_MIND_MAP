# Mantra Sony Remote (TC Jam), Android

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that jams time code into Sony Alpha cameras over USB, starts REC on all Sonys over Bluetooth, outputs LTC; Mac counterpart: SONY_REMOTE_MAC.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/sony_remote_controller](https://github.com/markoboskoauroville/sony_remote_controller) |
| Also called | Sony Remote Controller, TC Jam, Mantra Sony Remote, Sony Alpha remote Android |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v29 |
| Control level | adb (android adb / intents) |

## What it can do

- Jam free-run time code into a Sony Alpha over USB PTP (settings 0xD0D3, 0xD0D6, 0xD0D7)
- Start and stop REC on every Sony over a Bluetooth LE remote (service 8000FF00) and read recording reports
- Read time code from a camera's screen with the phone camera and on-device OCR
- Generate SMPTE LTC at 25 fps as audio out
- Play a clap (tones, torch flash, white slate) for sync
- Serve a download page (mantrasonyremote.pages.dev) with the latest APK
- Planned: Wi-Fi live view and exposure/focus control of the A7 V

## Ask for it when

- sync time code on my Sony cameras
- start recording on all Sony cameras at once
- jam timecode from the phone to a Sony A7
- clap sync for multi-camera shoot
- Sony Alpha Android remote

## How to control it

- Level: **adb**
- Type: adb-intent

Actions:

- `am start --es tc HH:MM:SS:FF (jam)`
- `am start --ez read true (open reader)`
- `USB key attach (jam on plug-in, disabled auto-open in v29)`

**Before you call:** Phone on adb; the camera body on USB for TC Jam. Android app with Bluetooth REC remote and time code jam.

Example:

```
adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --es tc 12:00:00:00
```

More calls:

- open the reader: `adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --ez read true`

Evidence: TAKEOVER.md 'TC JAM' section (test doors --es tc, --ez read true); activity class name inferred from file list TcJamActivity.kt

## Inputs / Outputs

Inputs:

- Sony camera over USB
- Sony Bluetooth remote service
- camera screen via phone camera

Outputs:

- time code on cameras
- REC start/stop
- LTC audio
- status displays

## Hardware

- Sony Alpha 7 V / a6600 and other Alphas
- Accsoon CineView Nano (planned mode)
- USB-C

## Works with

- Uses: [Sony Remote (Mantra), Mac](SONY_REMOTE_MAC.md)
- Talks to: [Mantra Manual Camera](mantra-manual-camera.md)
- Used by or talked to by: [Mantra Manual Camera](mantra-manual-camera.md)

## Code worth reusing

- `app/src/main/java/com/mantraproductions/sonyremote/BleRemote.kt`: Sony Bluetooth LE remote commander: REC on all and recording reports
- `app/src/main/java/com/mantraproductions/sonyremote/Ltc.kt`: SMPTE LTC generator at 25 fps
- `app/src/main/java/com/mantraproductions/sonyremote/ScreenReader.kt`: Camera2 plus ML Kit OCR that reads a time code off a camera screen
- `tools/a7v_probe.py`: Probe of Sony A7 V PTP/IP live view and properties from the Mac

## Notes

README is stale (says 'planning'); TAKEOVER.md describes the working TC Jam (v29). The same TC Jam is also built into Mantra Manual Camera v187+. Public repo; Sony's official reference docs are kept local only. a6600 has no time code over USB. Not verified: LTC with a decoder, clap timing. The adb-intent how_to_call is derived from TAKEOVER wording; check the manifest for the exact component. Time code jam works over USB PTP only on bodies that accept it (A7 V yes, a6600 no per the manifest).

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/sony_remote_controller/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/sony_remote_controller/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/sony_remote_controller/blob/HEAD/LESSONS.md)
