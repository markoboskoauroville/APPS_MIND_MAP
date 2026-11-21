# Sony Remote (Mantra), Mac

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app and local door that connects to a Sony camera and starts or stops REC on its card; the Android counterpart is sony_remote_controller.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SONY_REMOTE_MAC](https://github.com/markoboskoauroville/SONY_REMOTE_MAC) |
| Also called | Sony Remote, Sony remote Mac |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | http (own http routes) |

## What it can do

- Find the camera on the network (SSDP) and connect over PTP-IP through an SSH tunnel
- Start and stop movie recording on the camera card
- Show live view, recording time, card time left and battery
- Serve a local HTTP door for other apps (Second Take, Queen)

## Ask for it when

- start and stop recording on the Sony from the Mac
- record the Sony to its card remotely
- Sony alpha remote record button
- grab a live view frame from the Sony

## How to control it

- Level: **http**
- Type: http
- Port: 8881

Actions:

- `GET /status`
- `GET /start`
- `GET /stop`
- `GET /connect`
- `GET /disconnect`
- `GET|POST /frame.jpg`

**Before you call:** The camera must be connected first: curl -s -XPOST 127.0.0.1:8881/connect (finds the camera, uses the saved user and password; poll GET /status until connected); /start answers 409 'not connected' otherwise.

Example:

```
curl -s 127.0.0.1:8881/start
```

More calls:

- stop REC: `curl -s 127.0.0.1:8881/stop`
- status: connected, REC, card time left, battery: `curl -s 127.0.0.1:8881/status`
- newest live-view picture as JPEG: `curl -s 127.0.0.1:8881/frame.jpg -o live.jpg`
- find and connect the camera: `curl -s -XPOST 127.0.0.1:8881/connect`

Evidence: TAKEOVER.md (The door); app/Door.swift

## Inputs / Outputs

Inputs:

- Sony camera on Wi-Fi (PTP-IP)

Outputs:

- recording on the camera's card
- live view JPEG frames
- status

## Hardware

- Sony alpha 7 V (ILCE-7M5)

## Works with

- Used by or talked to by: [Mantra Sony Remote (TC Jam), Android](sony_remote_controller.md)

## Code worth reusing

- `app/PtpIp.swift`: PTP-IP client (init, sessions, operations) written from the protocol description
- `app/Tunnel.swift`: SSH port forward to the camera's PTP port
- `app/Door.swift`: tiny loopback HTTP API pattern

## Notes

Loopback only. Built on Sony's protocol document, no Sony SDK code. v1 only; the alpha 7 V has no time-code read-out. REC goes to the camera's own card (not to the Mac disk; for recording to the Mac use web-cam-viewer). GET works for /start, /stop, /connect too (from app/Door.swift).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SONY_REMOTE_MAC/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SONY_REMOTE_MAC/blob/HEAD/LESSONS.md)
