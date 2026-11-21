# Drive Full Path (Mantra Productions)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Firefox extension that shows the full path of the open Google Drive folder in a bar at the top, every folder a clickable link, plus a copy button.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_DRIVE_PATH](https://github.com/markoboskoauroville/MANTRA_DRIVE_PATH) |
| Also called | Drive Full Path, drive-full-path |
| Visibility | public |
| Kind | browser-extension |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | Web |
| Language | JavaScript (MV3) + HTML site |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Show the whole folder path on drive.google.com instead of '...'
- Click a folder name to go there without reload; Cmd/middle click opens a new tab
- Copy the path with one button
- Build a zip for addons.mozilla.org
- Load the extension into a running Firefox as a temporary add-on

## Ask for it when

- see the full Google Drive folder path
- where am I in Google Drive
- copy the Drive folder path

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- Google Drive page DOM

Outputs:

- path bar
- zip for AMO

## Code worth reusing

- `extension/content.js`: read Drive breadcrumbs (including hidden 'Show path' menu items) and travel to a folder
- `tools/load_in_firefox.py`: install a temporary add-on in running Firefox via WebDriver BiDi on port 9222

## Notes

Published on addons.mozilla.org (version 2). Content script on drive.google.com only; no network, no storage. Includes a promo site deployed via Pages (site/public).

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MANTRA_DRIVE_PATH/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_DRIVE_PATH/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_DRIVE_PATH/blob/HEAD/LESSONS.md)
