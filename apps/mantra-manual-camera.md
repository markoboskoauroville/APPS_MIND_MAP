# Mantra Manual Camera

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android manual-control cinema camera app: ISO/shutter/focus/WB faders, log curves, 10-bit HEVC, NDI and VDO.Ninja live out, Sony REC and timecode, adb-driven.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra-manual-camera](https://github.com/markoboskoauroville/mantra-manual-camera) |
| Also called | Mantra NDI, mantra-ndi, Manual Camera, Mantra Camera, Mantra Link camera, mcam, Skeleton mode |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS, Android |
| Language | Kotlin (plus C++ NDI/tracker bridges) |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v222 |
| Control level | adb (android adb / intents) |

## What it can do

- Shoot with manual or half-manual ISO, shutter, focus and colour temperature and log curves (S-Log3, V-Log, LogC3/4, BMD Film Gen5)
- Record 10-bit HLG HEVC with free-run timecode track
- Send the camera as an NDI HX/full NDI source over Wi-Fi or USB cable
- Go live to a paired band website through VDO.Ninja
- Start REC on Sony cameras over Bluetooth and feed them time code (Sony Remote inside)
- Run SKELETON mode: stream the camera at a requested size/rate over Mantra Link (TCP 48100) with lens calibration status JSON
- Be driven from the Mac over adb with the mcam script
- Show a clean full-screen feed for screen mirroring

## Ask for it when

- use my phone as a manual camera
- stream the phone camera to OBS or vMix over NDI
- set ISO, shutter, white balance on the phone by command
- record a take with log curve on Android
- start all Sony cameras recording with the phone
- go live from the phone to my website

## How to control it

- Level: **adb**
- Type: adb-intent, cli, http
- Port: 48102 (status JSON); 48100 (Mantra Link stream)

Actions:

- `mcam state`
- `mcam settings`
- `mcam set NAME VALUE`
- `mcam restart`
- `mcam update`
- `mcam lens N`
- `mcam torch on|off|toggle`
- `mcam exposure auto`
- `mcam iso 400|auto`
- `mcam shutter 1/50|auto`
- `mcam ev +1`
- `mcam wb 4500|auto`
- `mcam focus 0..1|auto`
- `mcam circle iso|wb|tap|+|-`
- `mcam key NAME`
- `mcam fix`
- `mcam snap out.png`
- `mcam open`
- `am start --es mode skeleton|off (lens, width, fps, mbps, codec, gop, lock, flicker, stab, orient, dim)`
- `GET http://<phone>:48102/status`

**Before you call:** Needs the Pixel 7 on adb (cable, or wireless debugging; MCAM_SERIAL overrides) with the camera app open or openable and Settings, MORE, ADB CONTROL on (default on from v144); run from a checkout of the repo (scripts/mcam).

Example:

```
scripts/mcam iso 400
```

More calls:

- what is set and how bright the picture is: `scripts/mcam state`
- white balance in Kelvin, shutter, focus: `scripts/mcam wb 4500 ; scripts/mcam shutter 1/50 ; scripts/mcam focus 0.5`
- press a rail key such as REC: `scripts/mcam key REC`
- start the SKELETON stream mode with an explicit lens and frame rate: `adb shell am start -n com.mantraproductions.manualcamera/com.mantraproductions.ndi.MainActivity --es mode skeleton --es lens back_main --ei fps 30`

Evidence: scripts/mcam (docstring), TAKEOVER.md (v222 SKELETON mode entry), SkeletonMode.kt; adb receiver action com.mantraproductions.manualcamera.ADB

## Inputs / Outputs

Inputs:

- phone camera sensors
- Sony cameras over USB or Bluetooth
- pairing QR from the band site

Outputs:

- video files with timecode
- NDI stream
- VDO.Ninja live stream
- Mantra Link H.264/HEVC stream
- status JSON

## Hardware

- Pixel 7 and Nothing Phone (Android)
- Sony Alpha cameras (REC over Bluetooth, timecode over USB)
- USB cable for NDI without network

## Works with

- Uses: [Mantra NDI SDK (private vendor files)](mantra-ndi-sdk.md), [Santoshi Kirtan Band sites](santoshi_band_site.md), [Mantra Sony Remote (TC Jam), Android](sony_remote_controller.md)
- Used by or talked to by: [Skeleton (Mantra)](SKELETON.md), [Sound Link (Mantra)](SOUND_LINK.md), [Mantra NDI Screen Share (Android)](mantra-ndi-screen-share-android.md), [Mantra NDI SDK (private vendor files)](mantra-ndi-sdk.md), [Virtual Cam (Mantra)](mantra_virtual_cam.md), [Santoshi Kirtan Band sites](santoshi_band_site.md), [Mantra Sony Remote (TC Jam), Android](sony_remote_controller.md)

## Code worth reusing

- `scripts/mcam`: Python adb driver for the camera: state, settings, ISO, shutter, WB, focus, lens, snap
- `app/src/main/cpp/ndi_bridge.cpp`: NDI sender bridge with hardware encoder keyframe handling for Android
- `app/src/main/java/com/mantraproductions/ndi/SkeletonMode.kt`: Headless camera streaming mode for a Mac-side consumer
- `app/src/main/cpp/third_party/ceres`: Vendored Ceres solver used by the tracker JNI

## Notes

Sold app (about 22 EUR mentioned in README). Repo renamed from mantra-ndi; app id com.mantraproductions.manualcamera, Kotlin package still com.mantraproductions.ndi. Control only works while Settings › MORE › ADB CONTROL is on; the receiver answers only the adb shell. NDI Advanced SDK trial stops after 5 min without a licence. 3 unmerged branches. Very large repo (35 MB). All mcam verbs listed in actions were checked against the docstring of scripts/mcam in the public repo. mcam works only through adb (the camera answers only the shell); port 48102 serves status JSON and 48100 the Mantra Link stream.

Unmerged branches with commits ahead of main: 3.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/mantra-manual-camera/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/mantra-manual-camera/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/mantra-manual-camera/blob/HEAD/LESSONS.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/mantra-manual-camera/blob/HEAD/HANDOVER.md)
