# gi (Instagram downloader)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Termux command that downloads Instagram posts, reels, stories and highlights and fetches its own login cookie from Firefox.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/gi](https://github.com/markoboskoauroville/gi) |
| Also called | gi-update, instagram downloader |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Python |
| Status | active |
| Last push | 2026-10-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Download posts, reels, stories, highlights and carousels from a URL
- Refresh the session cookie hands-free by driving Firefox over adb
- Use gallery-dl first and yt-dlp as fallback
- Update itself and its engines (gi-update)

## Ask for it when

- download an Instagram video on the phone
- save an Instagram story or highlight
- refresh the Instagram cookie

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `gi <url>`
- `gi --cookies`
- `gi-update`

Example:

```
gi https://www.instagram.com/p/<shortcode>/ # downloads the post or reel
```

More calls:

- use browser cookies: `gi --cookies`
- update the tool: `gi-update`

Evidence: README.md, gi.py (argparse)

## Inputs / Outputs

Inputs:

- Instagram URL
- Firefox session cookie

Outputs:

- downloaded media files

## Hardware

- Android phone with wireless debugging

## Code worth reusing

- `gi.py`: cookie refresh by driving Firefox's Export Cookies extension over adb taps

## Notes

The cookie file never leaves the phone and is gitignored. It never types a password.

## Docs in the repo

- `README.md`
