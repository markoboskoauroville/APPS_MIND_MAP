# Sample Player, macOS

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Local Flask server with a web page for macOS: the same recorded cells, transcription and voice replacement as the Android app SAMPLE_PLAYER.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SAMPLE_PLAYER_MACOS](https://github.com/markoboskoauroville/SAMPLE_PLAYER_MACOS) |
| Also called | Sample Player macOS, sampleplayer |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Web |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Record a phrase into a numbered slot, transcribe it, replace the voice
- Play the set with a travelling playhead and render/download it
- Transform a slot to a cloned or generated voice and report quality (ok/smear/chirp)
- Manage voice clones with recorded consent
- Self-update with sampleplayer-update

## Ask for it when

- sample player on the Mac
- record phrases and swap the voice
- clone a voice with consent
- web sample sequencer from the terminal

## How to control it

- Level: **http**
- Type: http
- Port: chosen at start, written to ~/.sampleplayer-web/port.txt

Actions:

- `GET /api/state`
- `POST /api/record/<slot>`
- `GET /api/audio/<slot>`
- `POST /api/render`
- `GET /api/download/<slot>`
- `POST /api/meta/<slot>`
- `POST /api/delete/<slot>`
- `POST /api/transcribe/<slot>`
- `GET /api/voices/<engine>`
- `GET /api/version`
- `GET /api/cache`
- `POST /api/cache/clear`
- `POST /api/speak/<slot>`
- `GET /api/clones`
- `POST /api/clones/add`
- `POST /api/clones/consent`
- `POST /api/transform/<slot>`

**Before you call:** Start the server first (it picks a free port and writes it to ~/.sampleplayer-web/port.txt).

Example:

```
curl -s -XPOST 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/record/<slot> # records into a cell; slot names are in GET /api/state
```

More calls:

- state of all cells: `curl -s 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/state`
- transcribe a cell: `curl -s -XPOST 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/transcribe/<slot>`
- speak a cell with a cloned voice: `curl -s -XPOST 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/speak/<slot>`
- version: `curl -s 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/version`

Evidence: server.py @app.route lines 908-1803; CLAUDE_CODE_FINISH.md

## Inputs / Outputs

Inputs:

- microphone recordings
- text for speech

Outputs:

- recorded and re-voiced audio per slot
- rendered set

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Talks to: [Sample Player, Android](SAMPLE_PLAYER.md)
- Used by or talked to by: [Sample Player, Android](SAMPLE_PLAYER.md)

## Code worth reusing

- `server.py`: Flask server: slot recording, transcription, voice transform with quality report, clone consent
- `update.sh`: one-command self-install and update from GitHub with file checks
- `scripts/gates.py`: delivery gate checks

## Notes

Has an unfinished-work brief in CLAUDE_CODE_FINISH.md. Same cell concept as the Android app. Port is dynamic.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/SAMPLE_PLAYER_MACOS/blob/HEAD/README.md)
- [CLAUDE.md](https://github.com/markoboskoauroville/SAMPLE_PLAYER_MACOS/blob/HEAD/CLAUDE.md)
