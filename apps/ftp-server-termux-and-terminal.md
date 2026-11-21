# FTP Server v4

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One-file file server for phone (Termux) and Mac: anonymous FTP, web dashboard with transfer queues, name server and a terminal client.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ftp-server-termux-and-terminal](https://github.com/markoboskoauroville/ftp-server-termux-and-terminal) |
| Also called | ftpserver, TC Server, ftp server termux |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | macOS, Android, Termux |
| Language | Python, Shell |
| Status | active |
| Last push | 2026-10-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Serve anonymous FTP with resume
- Show a web dashboard with speed, transfers and history
- Browse, download and upload files and whole folders as a queue, one file at a time
- Run a name server (DNS and mDNS) with a panel to scan the network and name devices
- Copy folder trees between two servers by name (get, put, ls)
- Install itself on Termux or macOS from one script

## Ask for it when

- move files between phone and Mac over Wi-Fi
- start a file server on the phone
- copy a folder from the studio computer by name
- give network devices friendly names

## How to control it

- Level: **http**
- Type: http, cli
- Port: HTTP 8200 (8200-8215), FTP 2121, DNS 8253 UDP

Actions:

- `ftpserver`
- `ftpserver get NAME PATH`
- `ftpserver put NAME PATH`
- `ftpserver ls NAME`
- `/status`
- `/api/tree/<root>/<path>`
- `/api/mkdir/<root>/<path>`
- `/api/names`
- `/api/scan`
- `/api/whoami`
- `/up/<root>/<folder>`
- `/dl/<root>/<path>`

**Before you call:** Runs on the phone or Mac (Termux or terminal); HTTP page on 8200 (up to 8215), FTP on 2121, its own DNS on UDP 8253. Names are the machines' names it knows.

Example:

```
ftpserver get studio Music # fetch the folder Music from the server named studio
```

More calls:

- send a file: `ftpserver put studio ~/Music/song.wav`
- list a folder: `ftpserver ls studio`
- status: `curl -s 127.0.0.1:8200/status`
- known names: `curl -s 127.0.0.1:8200/api/names`

Evidence: README.md, TAKEOVER.md (routes), src/ftp_server.py

## Inputs / Outputs

Inputs:

- shared folder (phone storage or ~/Public)

Outputs:

- file transfers
- names.json

## Hardware

- Android phone
- Mac

## Code worth reusing

- `src/ftp_server.py`: single-file FTP plus HTTP queue server with DNS/mDNS name service and folder-tree client
- `tools/build.sh`: generates one-file installer from source and template

## Notes

Open to everyone on the same Wi-Fi without a password by design. Mac shares only ~/Public. Port written to ~/.mantra/ports/ftpserver while running. Never edit the generated 4-ftp-server-v4.sh by hand.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
