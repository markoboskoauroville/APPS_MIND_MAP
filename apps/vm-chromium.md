# Chromium Virtual Machine (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Chromium-only Ubuntu ARM VM in Oracle Cloud reached by VNC, with a token HTTP agent (vm-agent), Mac cvm and vmr commands, workers and a Swift VNC viewer.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/vm-chromium](https://github.com/markoboskoauroville/vm-chromium) |
| Also called | chromium-vm, Chromebook in Oracle Cloud, cvm, vm-agent, vmr, VM Router, Remote Viewing (Mantra) Mac |
| Visibility | public |
| Kind | service-daemon |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | macOS, Linux, Cloud |
| Language | Python (plus Swift viewer) |
| Status | active |
| Last push | 2026-11-19 |
| Build / release | GitHub workflow: yes; latest release: v45 |
| Control level | door (standard door) |

## What it can do

- Run Chrome/Chromium in the cloud VM and show it by VNC in the Mac app Chromium Virtual Machine (Mantra)
- Serve vm-agent with /health, /api and POST `/api/<action>` for clipboard, typing, keys, tabs, page text, eval, shots and file transfer
- Drive Claude/Gemini chats with cvm ask, cvm new, cvm eval and route many sessions through vm-router/vmr
- Send every finished download to Google Drive and delete it from the VM
- Run background workers such as Gemini image batches
- Provide a Swift VNC viewer and server (Remote Viewing Mantra v39-v45) with ARD login, ZRLE
- Host core services: session-ack (receipts) and ttt-relay (transcription relay)

## Ask for it when

- use Chrome in the cloud from my Mac
- ask Claude or Gemini in a browser tab from a script
- clipboard between Mac and the VM
- generate images in Gemini in batch
- view and control another Mac or phone by VNC

## How to control it

- Level: **door**
- Type: remote-door-http, cli
- Port: 8890

**Warning:** port 8890 is also quoted for [Session Hub](SESSION_HUB.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `GET /api`
- `screen_modes`
- `clip_get`
- `clip_set`
- `type`
- `paste_text`
- `key`
- `ls`
- `shot`
- `tabs`
- `open`
- `page_text`
- `eval`
- `claude_ask`
- `downloads`
- `paste_files`
- `cdp`
- `status`
- `capture`
- `claude_last`
- `PUT|GET /files/<name>`
- `cvm new|ask|paste|type|key|clip|put|get|ls|tabs|open|text|eval|shot`
- `vmr -s NAME ... (router on 127.0.0.1:8891)`

**Before you call:** Run on the Mac (cvm is installed from mac/cvm into ~/.local/bin). The vm-agent on the VM listens on port 8890 and needs header X-Mantra-Token over Tailscale; cvm sends it. The 8890 here is on the VM, not the Mac session hub.

Example:

```
cvm ask "Summarise the open tab in one sentence" # Mac command: asks claude.ai in the VM browser, answers as text in about 7 s
```

More calls:

- start a fresh claude.ai chat tab as cvm's tab: `cvm new`
- open a URL and read its text: `cvm open https://example.com ; cvm text`
- run JavaScript in the page: `cvm eval "document.title"`
- last resort: a picture of the VM screen; or send a file up: `cvm shot ; cvm put report.pdf`

Evidence: agent/vm-agent.py (ACTIONS dict, /health and /api handlers), README.md fast channel section

## Inputs / Outputs

Inputs:

- VNC input
- Tailscale
- Google account profiles

Outputs:

- answers as text
- files in Google Drive
- screens

## Hardware

- Oracle Cloud Ampere A1 VM
- Mac running the viewer

## Works with

- Uses: [Session Ack (ccmsg)](SESSION_ACK.md), [vm-android (Pixel 7 in Oracle Cloud)](vm-android.md)
- Used by or talked to by: [Agent Manager (CEO) (Mantra)](AGENT_MANAGER.md), [Cloud Mixer](CLOUD_MIXER.md), [Cost Agent (Mantra)](COST_AGENT.md), [VPN (Mantra)](MANTRA_VPN.md), [vm-android (Pixel 7 in Oracle Cloud)](vm-android.md)

## Code worth reusing

- `agent/vm-agent.py`: Remote-door style HTTP agent with declared actions (/api) and token auth
- `desktop/chromium-vm-dock.py`: Dock/tray and window helper for the VM desktop
- `.claude/skills/this-machine/SKILL.md`: Skill telling sessions the VM is 'this machine' and how to work on it
- `viewer/`: Swift RFB viewer and built-in VNC server with Apple login (ARD) and ZRLE (per TAKEOVER)

## Notes

Follows the remote-door contract (/health, /api, POST `/api/<action>`) on the VM. Two token files: one for the VM, one on the Mac. Large and fast-moving (v45, 19.11.2026); a cloud session cannot reach the VM without Tailscale auth key in its environment. Action list read from the source's ACTIONS dict; exact argument shapes are in /api. Tags v43-v45 are viewer builds. Argument shapes of each cvm verb are shown by GET /api on the VM; the examples follow the verb list in the README (cvm new|ask|paste|type|key|clip|put|get|ls|tabs|open|text|eval|shot).

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/vm-chromium/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/vm-chromium/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/vm-chromium/blob/HEAD/LESSONS.md)
