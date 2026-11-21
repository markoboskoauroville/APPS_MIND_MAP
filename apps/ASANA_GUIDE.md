# Asana Guide (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android guide for yoga poses: one picture, Sanskrit and English name, explanation read aloud with highlighted words.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ASANA_GUIDE](https://github.com/markoboskoauroville/ASANA_GUIDE) |
| Also called | Asana Guide |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | Android |
| Language | Kotlin (Python tools) |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Show one asana per screen with picture and names
- Read the explanation aloud with sentence and word highlighting
- Browse by list or arrows and show sequences such as Sun Salutation
- Render audio from text with a tool script

## Ask for it when

- guide me through yoga poses
- explain an asana aloud
- build the asana guide APK

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- asanas.json catalogue
- pre-rendered audio

Outputs:

- Android APK

## Code worth reusing

- `tools/render_audio.py`: renders sentence audio, joins it and writes timing JSON for word highlighting
- `tools/check_no_media.py`: pre-push hook refusing media, keys and binaries

## Notes

Lives primarily in a Drive repository; images and audio are not on GitHub. Built on the Mac with Gradle. Third-party images need permission before any public use.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
- `CLAUDE.md`
