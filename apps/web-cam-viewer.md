# Webcam Recorder (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that shows any camera the Mac sees (webcam, capture card, NDI/virtual cams, Sony over USB) with sound meters and one-key crash-safe MKV recording.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/web-cam-viewer](https://github.com/markoboskoauroville/web-cam-viewer) |
| Also called | Web Cam Viewer (Mantra), Webcam Recorder, webcam viewer, mantrawebcamrecorder |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS |
| Language | Swift |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v27 |
| Control level | http (own http routes) |

## What it can do

- Show any Mac camera full window with camera and sound-input menus and live capture statistics
- Record H.264 + AAC to Matroska in ~/Movies with real-time start time code, LOW/MID/HIGH bitrates and free-space time
- Show two VU hairline meters and warn about silent or missing sound
- Choose capture format, frame rate and device preferences, remembered per device
- Control a Sony Alpha over Wi-Fi PTP-IP or USB PTP (connect, ISO, shutter, REC, read props) when the user takes control
- Serve a loopback HTTP API so other apps and Queen can drive it
- Update itself from GitHub releases; download page with fixed DMG address

## Ask for it when

- record the Sony camera to disk on the Mac
- record a webcam or capture card with sound
- start and stop recording by command
- check which cameras the Mac sees
- set ISO or shutter on the Sony from the Mac

## How to control it

- Level: **http**
- Type: http
- Port: 8867

Actions:

- `GET /status`
- `GET /cameras`
- `GET /capture`
- `POST /camera {name|id,slice}`
- `POST /capture {format|rate|mode}`
- `POST /quality {quality: low|mid|high}`
- `POST /record/start {name?}`
- `POST /record/stop`
- `POST /snap {on}`
- `POST /front`
- `POST /fullscreen {on}`
- `GET /sounds`
- `POST /sound {name|id|none}`
- `GET /sony/status[?check=1]`
- `POST /sony/check`
- `POST /sony/connect`
- `POST /sony/disconnect`
- `POST /sony/takecontrol`
- `POST /sony/rec {on}`
- `GET /sony/prop?code=`
- `POST /sony/set {code|name, value|label}`

**Before you call:** To control a Sony body (ISO, shutter, REC) call POST /sony/connect, then POST /sony/takecontrol (closes Imaging Edge Remote and takes the USB; the owner's explicit decision), before /sony/set or /sony/rec.

Example:

```
curl -s -XPOST 127.0.0.1:8867/record/start -H 'Content-Type: application/json' -d '{"name":"interview"}'
```

More calls:

- stop the recording and get the file path: `curl -s -XPOST 127.0.0.1:8867/record/stop`
- set ISO on the connected Sony (value as the camera's own label): `curl -s -XPOST 127.0.0.1:8867/sony/set -H 'Content-Type: application/json' -d '{"name":"ISO","label":"ISO 800"}'`
- start or stop REC on the Sony's card: `curl -s -XPOST 127.0.0.1:8867/sony/rec -H 'Content-Type: application/json' -d '{"on":true}'`
- pick the camera to record from: `curl -s -XPOST 127.0.0.1:8867/camera -H 'Content-Type: application/json' -d '{"name":"<name from GET /cameras>"}'`

Evidence: app/ApiServer.swift lines 80-101 (POST /quality {quality: low|mid|high}, /fullscreen {on}, /front, /camera, /record/start, /record/stop read in the source); README.md lines 47-48

## Inputs / Outputs

Inputs:

- FaceTime/USB/NDI/Iriun/OBS virtual cameras
- any sound input
- Sony Alpha over USB or Wi-Fi

Outputs:

- MKV files `~/Movies/mb_<date>.mkv`
- status JSON
- snapshots

## Hardware

- Sony ILCE-7M5 (A7 V) over USB PTP
- UGREEN HDMI capture card
- USB webcams

## Works with

- Talks to: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)
- Used by or talked to by: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) will drive this app (the only road to the Sony camera) [http 8867]

## Code worth reusing

- `app/Recorder.swift`: Crash-safe H.264/AAC MKV recording with ffmpeg packet-copy mux
- `app/SonyPtp.swift`: Sony PTP/IP and USB PTP property read/write
- `app/ApiServer.swift`: Tiny loopback HTTP server on Network.framework with port file registration
- `app/Meter.swift`: Two-channel dB VU meter view

## Notes

Does not use the /health + /api contract; its routes are plain paths on 8867 (also registered in the manifest as Webcam Recorder). Bundle id kept from v1. Sony USB road and controls not verified against the body at v27 (21.11.2026); Wi-Fi road found ports closed. Webcam Recorder never holds an unselected Sony open. Tag list also includes v6, v7 etc.; v27 taken from TAKEOVER. Checked against app/ApiServer.swift: /quality, /fullscreen and /front exist in the source (the harvested docs list only /front). ISO, shutter, F-number, EV, white balance and Kelvin are all declared as settings the overlay can set through /sony/set, but Sony USB control is not verified against the body (v27). The camera name in /camera is whatever GET /cameras lists. Recordings land in ~/Movies as mb_YYYY-MM-DD_HH-MM-SS.mov (H.265 with time code). To start REC on the camera's own card from the Mac use SONY_REMOTE_MAC instead.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/web-cam-viewer/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/web-cam-viewer/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/web-cam-viewer/blob/HEAD/LESSONS.md)
