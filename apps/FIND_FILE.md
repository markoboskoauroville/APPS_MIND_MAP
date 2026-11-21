# Find a File (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that finds files by name with the terminal find or Spotlight index, shows hits in four views and can reveal, open or copy the path.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/FIND_FILE](https://github.com/markoboskoauroville/FIND_FILE) |
| Also called | Find a file, find command page |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Web, Hammerspoon |
| Language | Swift (original Python/Flask page findd.py) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | door (standard door) |

## What it can do

- Search a folder by name or part of name with find -iname
- Search by creation day
- Search names and contents live through Spotlight (mdfind) and index a folder
- Filter, sort and group hits and show them in compact, list, grid and large views
- Reveal in Finder, open, open folder, copy path
- Control Spotlight indexing per drive and folder

## Ask for it when

- find a file on the Mac by name
- find all files created yesterday
- search inside files with Spotlight
- where is this zip file
- search files inside one folder on the Mac
- make Spotlight index a single folder

## How to control it

- Level: **door**
- Type: http
- Port: 8845

Actions:

- `GET /health`
- `POST /api/find`
- `POST /api/reveal`
- `POST /api/open`
- `POST /api/folder`
- `POST /api/copy`
- `POST /api/choose`

**Before you call:** Find a File (Mantra) must be running; ENGINE SPOTLIGHT is its search engine.

Example:

```
curl -s -X POST http://127.0.0.1:8845/api/find -H 'Content-Type: application/json' -d '{"folder":"~","name":"animatics"}'
```

More calls:

- reveal a file in Finder: `curl -s -XPOST 127.0.0.1:8845/api/reveal -H 'Content-Type: application/json' -d '{"path":"~/Desktop/poster.png"}'`
- open it: `curl -s -XPOST 127.0.0.1:8845/api/open -H 'Content-Type: application/json' -d '{"path":"~/Desktop/poster.png"}'`
- health: `curl -s 127.0.0.1:8845/health`

Evidence: findd.py header lines 22-29; README.md line 54

## Inputs / Outputs

Inputs:

- folder and name pattern

Outputs:

- list of hits with path, size, date

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Find a File Spotlight (Mantra) (retired)](spotlight.md)

## Notes

The HTTP page (findd.py, port 8845) is the older engine; the current app is a native Swift window that replaced it, so the API may not be served by the app itself. Body field names for /api/reveal and /api/open (path) are by analogy with /api/find and not shown in the docs. Replaces the retired Find a File Spotlight (spotlight).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
