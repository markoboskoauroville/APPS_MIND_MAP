# Transcribe Voice to Text RT (Mantra), retired (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md). Replaced by MANTRA_VOICE_TO_TEXT.

**Floating Mac dictation stripe: press F1, speak, it transcribes (Whisper local or Groq), optionally cleans the text with an LLM, and types it at the cursor.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MARKO_TRANSCRIBE](https://github.com/markoboskoauroville/MARKO_TRANSCRIBE) |
| Also called | Marko Transcribe, Voice to Text, Transcribe Voice to Text, Mantra voice to text |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift |
| Status | retired |
| Last push | 2026-11-01 |
| Build / release | GitHub workflow: no; latest release: v9 |
| Control level | none (no control api found) |

## What it can do

- Record on F1 and type the transcript where the cursor is
- Transcribe with local Whisper, Groq Whisper or hand over to Speechify
- Clean the text in a chosen style with a local or Groq or Haiku model
- Apply standing name corrections in code
- Keep a history and offer Copy when typing fails

## Ask for it when

- dictate text anywhere on the Mac
- speech to text in Croatian or English
- clean up dictated text

## How to control it

No control API found.

Evidence: none found; only a --import-keys command line flag

## Inputs / Outputs

Inputs:

- microphone

Outputs:

- typed text
- clipboard

## Hardware

- microphone

## Works with

- Uses: [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Mantra Voice (speech server)](MANTRA_VOICE.md), [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)

## Code worth reusing

- `server/styled.py`: local LLM text-style cleanup server
- `App/Sources/Engines.swift`: engine selection with Whisper, Groq and ring of keys

## Notes

Merged on 1.11.2026 into the repo MANTRA_VOICE_TO_TEXT (v3); this repo keeps history up to v29. Use that repo instead. RETIRED/SUPERSEDED: use MANTRA_VOICE_TO_TEXT instead.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
