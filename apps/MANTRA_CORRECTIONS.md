# Mantra Corrections

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Shared correction database for the dictation and typing tools: curated replacement pairs plus what each device learned. Data only, builds nothing.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_CORRECTIONS](https://github.com/markoboskoauroville/MANTRA_CORRECTIONS) |
| Also called | dictation corrections |
| Visibility | private (code not readable without access) |
| Kind | data |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS, Android |
| Language | JSON |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Hold a curated pairs table of dictation corrections
- Collect corrections learned per device in separate files
- Let the Mac and phone dictation apps share one correction source

## Ask for it when

- fix repeated dictation mistakes
- share dictation corrections between Mac and phone

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- corrections written by dictation apps

Outputs:

- pairs.json for the dictation apps

## Works with

- Talks to: [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md), [TTT Voice Type keyboard](TTT.md)
- Used by or talked to by: [TTT Voice Type keyboard](TTT.md)

## Notes

Learned entries are personal dictation vocabulary and are not summarised here.

## Docs in the repo

- `TAKEOVER.md`
- `LESSONS.md`
