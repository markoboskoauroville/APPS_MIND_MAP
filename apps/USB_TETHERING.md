# USB Tethering (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app with a 1x1 home widget and Quick Settings tile that switch USB tethering on and off with one tap through Shizuku.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/USB_TETHERING](https://github.com/markoboskoauroville/USB_TETHERING) |
| Also called | USB Tethering, usbtether |
| Visibility | public |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v5 |
| Control level | none (no control api found) |

## What it can do

- Show tethering state ON/OFF on a widget and a tile
- Switch USB tethering with svc usb setFunctions rndis through Shizuku
- Fall back to opening Android's tether settings when Shizuku is off
- Refresh state from the USB_STATE broadcast and a 15-minute fallback

## Ask for it when

- toggle USB tethering with one tap
- internet from the phone to the Mac over USB
- tethering widget

## How to control it

No control API found.

## Hardware

- Nothing Phone 2a
- Pixel 7
- USB cable to Mac

## Code worth reusing

- `android/app/src/main/java/community/auroville/usbtether/Tether.kt`: toggles USB tethering via shell through Shizuku
- `android/app/src/main/java/community/auroville/usbtether/UsbWatch.kt`: watches the USB_STATE broadcast

## Notes

Shizuku must be restarted after each reboot via Wireless debugging. Public, unpromoted. Built only by GitHub Actions.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/USB_TETHERING/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/USB_TETHERING/blob/HEAD/LESSONS.md)
