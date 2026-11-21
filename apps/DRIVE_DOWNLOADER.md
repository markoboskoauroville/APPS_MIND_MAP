# Drive Downloader

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local web app that downloads a whole Google Drive folder with byte-level resume and MD5 verification, so a dropped connection costs seconds not gigabytes.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DRIVE_DOWNLOADER](https://github.com/markoboskoauroville/DRIVE_DOWNLOADER) |
| Also called | Drive Downloader, rclone replacement |
| Visibility | public |
| Kind | app |
| Category | [Data, backups and misc](../capabilities/data-backups-misc.md) |
| Platforms | macOS, Web |
| Language | Python (Flask, SQLite) |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Download a Drive folder into name.part files and resume with Range: bytes=N-
- Keep progress in SQLite and correct the ledger from what is really on disk
- Verify each finished file against Drive's MD5 before renaming
- Show bytes done and left, speed, time left and a per-file list
- Pause, start, rescan or delete a job

## Ask for it when

- download a big Google Drive folder reliably
- resume a broken Drive download
- fetch a 4 GB video from Drive over a bad connection

## How to control it

- Level: **http**
- Type: http
- Port: 5055

**Warning:** port 5055 is also quoted for [GDrive Downloader (Flask, macOS)](GDRIVE_DOWNLOADER_FLASK_MACOS.md) - confirm with `mantra-ports scan`.

Actions:

- `GET/POST /api/config`
- `POST /api/connect`
- `GET/POST /api/jobs`
- `POST /api/jobs/<id>/start`
- `POST /api/jobs/<id>/pause`
- `POST /api/jobs/<id>/rescan`
- `DELETE /api/jobs/<id>`
- `GET /api/jobs/<id>/status`

**Before you call:** Flask app on 5055; connect the Google account first with POST /api/connect.

Example:

```
curl -s -XPOST 127.0.0.1:5055/api/jobs -H 'Content-Type: application/json' -d '{"url":"https://drive.google.com/drive/folders/<id>"}' # creates a job; body field names are not in the docs
```

More calls:

- start job 1: `curl -s -XPOST 127.0.0.1:5055/api/jobs/1/start`
- status of job 1: `curl -s 127.0.0.1:5055/api/jobs/1/status`
- pause it: `curl -s -XPOST 127.0.0.1:5055/api/jobs/1/pause`

Evidence: app.py lines 330-417 (password-protected)

## Inputs / Outputs

Inputs:

- Google Drive folder link and credentials

Outputs:

- downloaded files, SQLite ledger

## Code worth reusing

- `drive.py`: Drive folder walk and ranged resumable download with MD5 check
- `store.py`: SQLite job and file ledger

## Notes

First screen sets a password; /api calls need that session. One job at a time. Google Docs, Sheets and Slides cannot resume and are fetched whole. WHAT_IS_NOT_TESTED.md lists untested parts. Port 5055 is not in the MANTRA_PORTS table.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/DRIVE_DOWNLOADER/blob/HEAD/README.md)
