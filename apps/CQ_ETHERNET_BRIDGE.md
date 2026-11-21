# CQ Ethernet Bridge

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Recipe, not code: control an Allen & Heath CQ-12T from CQ MixPad on a Pixel phone over a USB-LAN cable using Android Ethernet tethering.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CQ_ETHERNET_BRIDGE](https://github.com/markoboskoauroville/CQ_ETHERNET_BRIDGE) |
| Also called | CQ cable control, CQ MixPad over cable |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | Android |
| Language | Markdown |
| Status | active |
| Last push | 2026-11-07 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | adb (android adb / intents) |

## What it can do

- Document how to wire phone, USB-LAN dongle and the CQ mixer
- Explain that Ethernet tethering makes the phone the DHCP server for the mixer
- Keep phone internet, Tailscale and adb working at the same time
- List the checks to run when MixPad finds nothing

## Ask for it when

- control the CQ mixer by cable from the phone
- CQ MixPad cannot find the mixer
- keep internet on the phone while connected to the mixer

## How to control it

- Level: **adb**
- Type: adb-intent

Actions:

- `adb shell am start -a android.settings.TETHER_SETTINGS`

**Before you call:** Pixel phone with the USB-LAN cable to the CQ-12T, CQ MixPad installed on the phone. Tethering may switch off after unplug or reboot.

Example:

```
adb shell am start -a android.settings.TETHER_SETTINGS # opens the phone's tethering page; switch on Ethernet tethering with the USB-LAN cable plugged in
```

Evidence: README.md "The fix"

## Hardware

- Allen & Heath CQ-12T
- Pixel 7
- USB-to-LAN dongle

## Works with

- Talks to: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md)

## Notes

No code; working state confirmed 7.11.2026. Tethering may switch off after unplug or reboot.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
