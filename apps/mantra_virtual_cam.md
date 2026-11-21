# Virtual Cam (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that makes the phone's Mantra Manual Camera the Mac's webcam over USB or Wi-Fi, with its interface shown in a window and clickable.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mantra_virtual_cam](https://github.com/markoboskoauroville/mantra_virtual_cam) |
| Also called | Mantra Virtual Cam, mantravirtualcam |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS, Android |
| Language | Swift |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | other (other protocols) |

## What it can do

- Link to the phone camera over adb forward or Wi-Fi and receive its hardware H.265/H.264 stream
- Decode with VideoToolbox and feed the OBS Virtual Camera sink as 1920x1080
- Show the phone camera's own interface in a window controlled by mouse and keyboard
- List several phones and pick one as the webcam
- Be controlled from outside through a URL scheme

## Ask for it when

- use my phone camera as a webcam on the Mac
- control the Mantra Manual Camera from the Mac
- use several phone cameras in OBS

## How to control it

- Level: **other**
- Type: url-scheme

Actions:

- `connect`
- `disconnect`
- `webcam/<name>`
- `find`

**Before you call:** Needs Mantra Manual Camera v161+ on the phone; the camera app must be in front for direct Wi-Fi.

Example:

```
open -g mantravirtualcam://webcam/<name> # the phone camera becomes the Mac webcam (shown as OBS Virtual Camera)
```

More calls:

- find phones: `open -g mantravirtualcam://find`
- connect / disconnect: `open -g mantravirtualcam://connect ; open -g mantravirtualcam://disconnect`

Evidence: TAKEOVER.md (v4 control from outside)

## Inputs / Outputs

Inputs:

- camera stream from Mantra Manual Camera over Mantra Link (port 48100)

Outputs:

- OBS Virtual Camera frames

## Hardware

- Android phone camera
- USB cable

## Works with

- Uses: [Mantra Manual Camera](mantra-manual-camera.md)

## Code worth reusing

- `Sources/Decoder.swift`: VideoToolbox H.264/H.265 decoder finding parameter sets by NAL type
- `Sources/VirtualCamera.swift`: feeds frames into OBS Virtual Camera's sink without OBS running
- `Sources/Link.swift`: Mantra Link client with adb forward per phone

## Notes

Needs camera app v161 or later on the phone. The webcam name stays OBS Virtual Camera by decision (no paid Apple account). The camera app must be in front on the phone for direct Wi-Fi. A firewall prompt may need to be allowed.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
