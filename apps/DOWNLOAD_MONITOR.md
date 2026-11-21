# Download, Copy and Move (Mantra) (was Download Monitor)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac window and local server that watch every download, copy and move with live size and speed, and run copies and moves in one verified queue.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DOWNLOAD_MONITOR](https://github.com/markoboskoauroville/DOWNLOAD_MONITOR) |
| Also called | Download Monitor, dlmon, Download Copy and Move |
| Visibility | public |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift + Python (Flask) |
| Status | active |
| Last push | 2026-11-17 |
| Build / release | GitHub workflow: yes; latest release: v9 |
| Control level | http (own http routes) |

## What it can do

- Watch downloads: Hugging Face repos, logs with tqdm lines, any growing file
- Run Hugging Face downloads resumably under the monitor
- Queue copies and moves one at a time; a move deletes the source only after count, bytes and MD5 checks and leaves a symlink
- Show live size and write speed in amber, mark files another program is writing (lsof)
- Dashboard parts with solo, notes under each file, MediaInfo columns
- Accept self-reported progress from any script (report)

## Ask for it when

- register a download so I can see it
- copy a big folder safely
- move files with verification
- what is downloading on my Mac
- download a Hugging Face model with resume

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8833

Actions:

- `GET /health`
- `GET /progress`
- `POST /report`
- `POST /control/<id>/<action>`
- `POST /forget/<id>`
- `POST /forget_many`
- `POST /copy`
- `POST /view`
- `GET /view/state`
- `POST /quit`
- `dlmon.py up`
- `dlmon.py open`
- `dlmon.py hf <repo>`
- `dlmon.py copy SRC DST`
- `dlmon.py move SRC DST`
- `dlmon.py queue`
- `dlmon.py cancel <id>`
- `dlmon.py pause|start|restart <id>`
- `dlmon.py info <id> "text"`
- `dlmon.py takeover <id>`
- `dlmon.py add <id>`
- `dlmon.py report <id> <have_mb> <want_mb>`
- `dlmon.py done|forget|clear|list|down`

**Before you call:** Download, Copy and Move (Mantra) must be running (port 8833).

Example:

```
python3 dlmon.py copy ~/Movies/big /Volumes/Backup/big/ --name "big copy"
```

More calls:

- see the queue: `python3 dlmon.py queue`
- move instead of copy: `python3 dlmon.py move ~/Downloads/x.zip ~/Archive/`
- progress over HTTP: `curl -s 127.0.0.1:8833/progress`
- cancel one: `python3 dlmon.py cancel <id>`

Evidence: monitor.py routes (lines 495-737), dlmon.py docstring, TAKEOVER.md

## Inputs / Outputs

Inputs:

- file paths
- Hugging Face repo ids
- progress reports

Outputs:

- copied or moved files
- progress page

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)
- Used by or talked to by: [App Store (Mantra)](APP_STORE.md), [Free Mac](FREE_MAC.md), [Mac Transcriber (scribe)](MAC_TRANSCRIBER.md), [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md), [Voice Engines (model hub)](VOICE_ENGINES.md), [djay Sync, command line (djay-sync)](djay-playlists.md), [Firefox Control](firefox-control.md)

## Code worth reusing

- `copier.py`: verified copy and move engine (count, bytes, MD5 of five largest, symlink left behind)
- `dlmon.py`: CLI to register and report any download
- `app/MediaInfo.swift`: MediaInfo columns for media files

## Notes

Rule (8.9.2026): every download on this Mac is registered here before it starts. Opening the app starts monitor.py if :8833 is down. Check /health first, never start a second server on another app's port.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/DOWNLOAD_MONITOR/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/DOWNLOAD_MONITOR/blob/HEAD/LESSONS.md)
