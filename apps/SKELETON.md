# Skeleton (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that follows a person with a body-pose skeleton from any chosen camera, scores matches to target poses, and takes Pixel phones with Manual Camera.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SKELETON](https://github.com/markoboskoauroville/SKELETON) |
| Also called | SKELETON (Mantra), pose tracker |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS, Android |
| Language | Swift |
| Status | active |
| Last push | 2026-11-16 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | cli (command line or script only) |

## What it can do

- Track body pose with Apple Vision from any camera (built-in, USB, Continuity, virtual)
- Compare to a target pose by limb angle with green/yellow/red bones and score
- Run a session of starter yoga poses (voice cues) and save poses
- Use phones running Mantra Manual Camera as sources over USB or Wi-Fi, auto-starting them via adb
- Calibrate multiple cameras (board, bundle adjustment, triangulation)

## Ask for it when

- follow me with a skeleton on camera
- check my yoga pose against a target
- multi-camera body tracking
- use the Pixel as a pose camera

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--camera <name> launch argument`

Example:

```
open -a "Skeleton (Mantra)" --args --camera ILCE-7M5 # the skeleton of the picture from the named camera
```

Evidence: TAKEOVER.md (Command line); app/Voice.swift, app/PhoneSource.swift

## Inputs / Outputs

Inputs:

- camera images
- phone Manual Camera streams (HEVC)

Outputs:

- skeleton overlay
- pose score
- saved poses (json+jpg)

## Hardware

- Sony ILCE-7M5 over USB
- Pixel/Nothing phones with Manual Camera
- Mac cameras

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md), [Mantra Manual Camera](mantra-manual-camera.md)

## Code worth reusing

- `app/Calib/`: camera calibration: board detection, bundle adjustment, triangulation, linear algebra
- `app/PhoneSource.swift`: discovers and starts adb phones as cameras, clock sync with NTP-style exchange
- `app/Camera.swift`: capture plus Vision body pose
- `blender/yoga_poses.py`: renders yoga pose mannequins

## Notes

Only a launch-time camera argument is controllable from outside; no control server. Public, unpromoted. Built only by GitHub Actions.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SKELETON/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SKELETON/blob/HEAD/LESSONS.md)
