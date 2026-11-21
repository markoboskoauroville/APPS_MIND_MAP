# Cloud Mixer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Programmatic vision mixer on chromium-vm: mixes files, stills, colours and live URLs into one program and publishes it to the relay for the site's live player.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CLOUD_MIXER](https://github.com/markoboskoauroville/CLOUD_MIXER) |
| Also called | cloudmix, vMix in the cloud, Cloud Mixer (VM) |
| Visibility | public |
| Kind | service-daemon |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | Linux, Cloud |
| Language | Python (numpy, ffmpeg) |
| Status | active |
| Last push | 2026-11-17 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Mix inputs with CUT and CROSSFADE (picture and equal-power audio) every 40 ms into one encoder that never restarts
- Draw live text overlays and lower thirds with fades
- Show a poster between items and fade back
- Run a playlist or a show file at an exact UTC second
- Publish MPEG-TS over SRT to the MediaMTX relay path and switch the site live on and off
- Take a live SRT camera input (newest frames only)

## Ask for it when

- stream a recorded concert as a live show
- switch between cameras in the cloud
- put a lower-third text on the stream
- schedule a show to start at noon

## How to control it

- Level: **http**
- Type: http, cli, python-module
- Port: 8841 on chromium-vm (not the Mac; Mac Remote VNC also uses 8841)

**Warning:** port 8841 is also quoted for [Installation Logger (Mantra)](INSTALLATION_LOGGER.md), [Mantra Remote Viewing (Mantra Remote)](MANTRA_REMOTE_VIEWING.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /status`
- `POST /load`
- `POST /output`
- `POST /fade`
- `POST /cut`
- `POST /text_on`
- `POST /text_off`
- `POST /poster`
- `POST /playlist`
- `POST /site`
- `POST /stop`
- `bin/cloudmix`
- `from cloud_mixer.client import Mixer`

**Before you call:** Runs on chromium-vm (port 8841 there, not on the Mac); reach it from the VM or over Tailscale.

Example:

```
curl -s 127.0.0.1:8841/load -d '{"src":"/srv/cloud-mixer/media/x.mp4","id":"cam1","start":300}'
```

More calls:

- cut to a source: `curl -s -XPOST 127.0.0.1:8841/cut -d '{"id":"cam1"}'`
- stop: `curl -s -XPOST 127.0.0.1:8841/stop`
- status: `curl -s 127.0.0.1:8841/status`
- command line: `bin/cloudmix`

Evidence: TAKEOVER.md section API; cloud_mixer/server.py, client.py

## Inputs / Outputs

Inputs:

- video files
- stills
- SRT live URLs
- show.json files

Outputs:

- 720p25 H.264 + AAC program over SRT to relay
- site go/stop

## Hardware

- Oracle ARM VM, 2 cores 12 GB (chromium-vm)

## Works with

- Uses: [Santoshi Kirtan Band sites](santoshi_band_site.md)
- Talks to: [Chromium Virtual Machine (Mantra)](vm-chromium.md)
- Used by or talked to by: [Streaming Dashboard (Mantra)](STREAMING_DASHBOARD.md)

## Code worth reusing

- `cloud_mixer/engine.py`: frame-accurate Python/numpy mixer using ffmpeg only for decode and one encode
- `cloud_mixer/show.py`: run a show file at an exact UTC second with pre-checks
- `cloud_mixer/client.py`: Python client and bin/cloudmix shell command

## Notes

Listens on loopback and the VM's Tailscale address only. Not enabled at boot. The relay knows only the path santoshi. First used for a recorded-concert noon show on 15.11.2026. The Mac-side door port 8841 is a different app; check which machine you call. Body of /cut is a guess by analogy with /load (id); not shown in the docs.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/CLOUD_MIXER/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/CLOUD_MIXER/blob/HEAD/LESSONS.md)
