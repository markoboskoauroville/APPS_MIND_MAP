# Sound Link (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that sends stereo sound (e.g. from an XLR mixer) over Wi-Fi to the Manual Camera Android app; includes a Studio encoder that pairs NDI video with mixer**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SOUND_LINK](https://github.com/markoboskoauroville/SOUND_LINK) |
| Also called | Sound Link, Studio (Mantra) |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS, Android |
| Language | Swift (app) and Python (studio/) |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Choose an input device and a channel pair and SEND it to a Manual Camera phone on the Wi-Fi
- Show meters, latency, buffer, dropouts, loss and drift while sending
- Expose a local door to list devices, set the source, send, stop
- Studio scripts: receive NDI video, mix with the mixer audio, encode and push RTMP
- Send an NDI test source with a tone

## Ask for it when

- send mixer audio to the camera
- sync desk sound with the phone camera
- stream NDI camera plus mixer sound
- Mac audio to Android over Wi-Fi

## How to control it

- Level: **http**
- Type: http
- Port: 8974

Actions:

- `/fn/status`
- `/fn/devices`
- `/fn/source`
- `/fn/send`
- `/fn/stop`
- `/fn/permissions`

**Before you call:** Sound Link (Mantra) must be running; functions are registered for Star API (star fn "sound link"). Not yet proven end to end.

Example:

```
curl -s -XPOST 127.0.0.1:8974/fn/source -d '{"device":"BlackHole","pair":1}'
```

More calls:

- list audio devices: `curl -s -XPOST 127.0.0.1:8974/fn/devices`
- status: `curl -s -XPOST 127.0.0.1:8974/fn/status`
- start sending: `curl -s -XPOST 127.0.0.1:8974/fn/send`
- stop: `curl -s -XPOST 127.0.0.1:8974/fn/stop`

Evidence: TAKEOVER.md line 13 and 36; app/Door.swift; registered in ~/.config/star-fns/sound-link.json

## Inputs / Outputs

Inputs:

- audio input device or XLR mixer (16 or 18 channels)
- Manual Camera NDI HX stream

Outputs:

- audio sent to the phone
- RTMP stream from studio.py
- log file

## Hardware

- XLR mixer / BlackHole
- Pixel phone running Manual Camera

## Works with

- Uses: [Mantra Manual Camera](mantra-manual-camera.md)

## Code worth reusing

- `studio/ndi.py`: libndi through ctypes: find NDI sources and receive frames
- `studio/studio.py`: NDI video + mixer audio encoder pushing RTMP at 25 fps
- `tools/clap_offset.py`: measures audio/video offset from a clap
- `app/Door.swift`: Star API functions door

## Notes

Not yet proven per TAKEOVER: real Pixel NDI into studio.py, the mixer, A/V sync. A Swift 'Studio (Mantra)' app was planned.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SOUND_LINK/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SOUND_LINK/blob/HEAD/LESSONS.md)
