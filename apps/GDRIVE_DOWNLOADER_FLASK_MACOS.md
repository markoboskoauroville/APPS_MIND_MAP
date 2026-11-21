# GDrive Downloader (Flask, macOS)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local Flask app that scans a Google Drive folder, reports files and size, then clones the whole tree to disk with byte-level resume and MD5 verification.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GDRIVE_DOWNLOADER_FLASK_MACOS](https://github.com/markoboskoauroville/GDRIVE_DOWNLOADER_FLASK_MACOS) |
| Also called | GDrive Downloader, Google Drive downloader, GDriveDownloader |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Data, backups and misc](../capabilities/data-backups-misc.md) |
| Platforms | macOS, Web |
| Language | Python (Flask, SQLite) |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Scan a Drive folder and report folders, files and gigabytes before downloading
- Clone the full folder tree with the same layout
- Resume a single file from the exact byte using Range requests
- Survive crashes using a SQLite ledger and check the disk before each run
- Verify files against Drive MD5
- Sign in via public link, service account, OAuth or API key

## Ask for it when

- download a whole Google Drive folder to this Mac
- resume a big Drive download after the connection dropped
- check how big a Drive folder is

## How to control it

- Level: **http**
- Type: http
- Port: 5055

**Warning:** port 5055 is also quoted for [Drive Downloader](DRIVE_DOWNLOADER.md) - confirm with `mantra-ports scan`.

Actions:

- `GET|POST /api/config`
- `GET|POST /api/credentials`
- `POST /api/signin/find`
- `GET|POST /api/signin`
- `POST /api/connect`
- `GET|POST /api/jobs`
- `POST /api/jobs/<id>/scan|start|pause|rename|repair|rescan|verify`
- `GET /api/jobs/<id>/status|verdicts`

**Before you call:** Flask app on 5055; sign in and connect first (POST /api/signin, POST /api/connect); same API as DRIVE_DOWNLOADER.

Example:

```
curl -s -XPOST 127.0.0.1:5055/api/jobs/1/start
```

More calls:

- list jobs: `curl -s 127.0.0.1:5055/api/jobs`
- status and verdicts of job 1: `curl -s 127.0.0.1:5055/api/jobs/1/status ; curl -s 127.0.0.1:5055/api/jobs/1/verdicts`
- verify a finished job: `curl -s -XPOST 127.0.0.1:5055/api/jobs/1/verify`

Evidence: app.py route decorators (api.txt)

## Inputs / Outputs

Inputs:

- Drive folder link or id
- credentials (kept local)

Outputs:

- local copy of the Drive tree

## Code worth reusing

- `segmented.py`: segmented byte-range download with resume
- `portpick.py`: preferred-port then next-free port picker
- `localguard.py`: same-origin guard for a local web app

## Notes

Used as rclone OAuth source by the Elevate Media monitor. Keyless public mode caps at 50 entries per folder page; use a credentialed mode for big folders (documented in README).

## Docs in the repo

- `README.md`
