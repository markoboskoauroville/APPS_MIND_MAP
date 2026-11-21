# Generated Playlists

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Repo where Claude continues reference songs into same-style playlists as text files and creates them on Marko's TIDAL account, named '(generated)'.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/generated_playlists](https://github.com/markoboskoauroville/generated_playlists) |
| Also called | TIDAL playlist generator, Claude playlists |
| Visibility | public |
| Kind | cli-tool |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Termux, Cloud |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Store playlists as 'Artist - Title' text files
- Create a playlist on TIDAL from a text file (tidal_playlist.py create, with --dry-run)
- Log in to TIDAL by OAuth PKCE (login-url, login-finish)
- Get a TIDAL refresh token on a phone via Termux (tidal_token_termux.py)
- Build radio-based playlists (radio command)

## Ask for it when

- make a playlist like this song
- put a playlist on TIDAL
- continue my reference song into a DJ playlist
- get a TIDAL token on the phone

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `login-url`
- `login-finish`
- `create <file> [--dry-run]`
- `radio`

**Before you call:** Log in to TIDAL first: tools/tidal_playlist.py login-url, open the link, then login-finish. The local port 8765 in the old record is the login callback, not an API.

Example:

```
python3 tools/tidal_playlist.py create playlists/2026-10-16_reggae-vocal-healing.txt # builds the TIDAL playlist from the track list; add --dry-run to preview
```

More calls:

- preview only: `python3 tools/tidal_playlist.py create playlists/2026-10-16_reggae-vocal-healing.txt --dry-run`
- start the login: `python3 tools/tidal_playlist.py login-url`

Evidence: TAKEOVER.md, HANDOVER.md, tools/tidal_playlist.py (redirect http://localhost:8765/tidal-callback)

## Inputs / Outputs

Inputs:

- reference songs/screenshots
- TIDAL login or TIDAL_REFRESH_TOKEN

Outputs:

- playlist txt files
- TIDAL playlists

## Works with

- Uses: [Screenshot to TIDAL (Mantra)](SCREENSHOT_TO_TIDAL.md), [DJ Mantra (Android DJ app)](djmantra_app.md)

## Code worth reusing

- `tools/tidal_playlist.py`: TIDAL OAuth PKCE login and playlist creation from a text list
- `tools/tidal_token_termux.py`: Catches the TIDAL login redirect on a phone and copies the token to the clipboard

## Notes

CLI, not a server (port 8765 is only the OAuth redirect listener in the Termux helper). Cloud environment must allow the TIDAL hosts. Rule: the song matters, not the exact version; a new style gives a new playlist. Token never committed.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/generated_playlists/blob/HEAD/TAKEOVER.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/generated_playlists/blob/HEAD/HANDOVER.md)
