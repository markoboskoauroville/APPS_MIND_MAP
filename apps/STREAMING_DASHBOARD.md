# Streaming Dashboard (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app and VM web service showing the live-stream chain (phone, Mac, VM, site) with rates, viewers and start or go-live buttons for the Meditation Room.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/STREAMING_DASHBOARD](https://github.com/markoboskoauroville/STREAMING_DASHBOARD) |
| Also called | Streaming Dashboard |
| Visibility | public |
| Kind | app |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS, Linux, Cloud |
| Language | Swift (app) and Python (VM service) |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: yes; latest release: v6 |
| Control level | door (standard door) |

## What it can do

- Show four chain lights PHONE, MAC, VM, SITE
- Start and stop the Meditation Room Linux test stream and go live on the site for 5, 15 or 30 minutes (rules enforced)
- Chart Mac-to-VM rate, ingest, viewers, VM CPU and SIM data left
- List relay streams, viewers, machine services and devices in DETAILS
- Serve the same dashboard as a web page from the VM

## Ask for it when

- is my live stream working
- check the streaming chain
- start the test stream and go live
- how many viewers are watching

## How to control it

- Level: **door**
- Type: http
- Port: 8996 (VM service)

Actions:

- `GET /`
- `GET /api/snapshot`
- `GET /api/state`
- `GET /health`
- `POST /api/action {action: start|stop|go-live|stop-live, minutes: 5|15|30}`

**Before you call:** Runs on the VM (listens on the VM's Tailscale address and loopback); the token header is needed off the VM. Go-live is blocked 11:50-13:50 Zagreb time and when the site is already live.

Example:

```
curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"go-live","minutes":15}'
```

More calls:

- state: `curl -s http://127.0.0.1:8996/api/state`
- stop a live: `curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"stop-live"}'`
- health: `curl -s http://127.0.0.1:8996/health`

Evidence: TAKEOVER.md lines 30-38; vm/streaming_dashboard_vm.py

## Inputs / Outputs

Inputs:

- MediaMTX relay API
- systemd states
- mrlinux status
- site live API

Outputs:

- dashboard window and web page
- stream start/stop commands

## Hardware

- cloud VM chromium-vm

## Works with

- Uses: [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md)
- Talks to: [Cloud Mixer](CLOUD_MIXER.md)

## Code worth reusing

- `app/collector.py`: collects relay, viewer, machine and device metrics into a snapshot
- `vm/streaming_dashboard_vm.py`: stdlib HTTP service with history and token-guarded actions
- `vm/install.sh`: installs the service on the VM with systemd

## Notes

Service listens on the VM's Tailscale address and loopback only. Go-live is blocked 11:50-13:50 Zagreb and when the site is already live. Built only by GitHub Actions.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/STREAMING_DASHBOARD/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/STREAMING_DASHBOARD/blob/HEAD/LESSONS.md)
