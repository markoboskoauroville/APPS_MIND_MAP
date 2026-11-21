# Voice Engines (model hub)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Central registry and fetch command for the local speech and listening models used by the voice server; weights are not in git.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/VOICE_ENGINES](https://github.com/markoboskoauroville/VOICE_ENGINES) |
| Visibility | private (code not readable without access) |
| Kind | config |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Python |
| Status | dormant |
| Last push | 2026-10-31 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- List every engine, size, speed measured and who uses it
- Fetch a model into a shared Hugging Face cache through the download monitor
- Check the chosen engines are present
- Print where a model lives

## Ask for it when

- download a speech model
- see which voice engines are installed
- move the models folder

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `list`
- `where`
- `fetch`
- `check`
- `hub`
- `env`
- `open`

Example:

```
voice-engines fetch qwen06 # downloads the model 'qwen06' into the shared hub
```

More calls:

- where the models are: `voice-engines where`
- which are present: `voice-engines list`
- check them: `voice-engines check`

Evidence: README.md The command; engines.py

## Inputs / Outputs

Outputs:

- hub/ model cache

## Works with

- Uses: [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md)
- Talks to: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Code worth reusing

- `engines.json`: registry of engines with Hugging Face repos and measured speeds

## Notes

Apps never load an engine themselves; they call MANTRA_VOICE. Folder must sit at ~/Developer/VOICE_ENGINES for the server to find hub/.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
