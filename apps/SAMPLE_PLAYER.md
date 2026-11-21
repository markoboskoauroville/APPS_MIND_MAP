# Sample Player, Android

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that records 30 spoken phrases per project, transcribes them, replaces the voice and plays the set with a travelling playhead.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SAMPLE_PLAYER](https://github.com/markoboskoauroville/SAMPLE_PLAYER) |
| Also called | Sample Player, Mantra Sample Player Android |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: v27 |
| Control level | none (no control api found) |

## What it can do

- Record phrases into cells from anywhere via a floating overlay triangle
- Transcribe recorded phrases
- Replace a phrase's voice with a generated one (voice protocols from Speechify/transcribe apps)
- Play the set back with a travelling playhead and loops
- Manage API keys through a key parser and provider table

## Ask for it when

- record phrases on the phone and re-voice them
- sample player with my own voice cells
- record a phrase over any app with a floating button

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- microphone

Outputs:

- recorded cells
- re-voiced audio
- APK

## Works with

- Uses: [Key Tester (Android)](Key_Tester.md), [Maha Transcribe / TTT-LLL (Streamlit)](MAHA_TRANSCRIBE_STREAMLIT.md), [MA Reader Speechify module](MA_READER_SPEECHIFY.md), [Minimalist Stopwatch](MINIMALIST_STOPWATCH.md)
- Talks to: [Sample Player, macOS](SAMPLE_PLAYER_MACOS.md)
- Used by or talked to by: [Sample Player, macOS](SAMPLE_PLAYER_MACOS.md)

## Code worth reusing

- `app/src/main/java/com/mantra/sampleplayer/Overlay.kt`: floating overlay button that records over any app
- `app/src/main/java/com/mantra/sampleplayer/KeyRing.kt`: API key storage and key parsing
- `app/src/main/java/com/mantra/sampleplayer/Dsp.kt`: audio processing for re-voiced cells

## Notes

Only README and file tree were harvested; see HANDOFF.md and DEVELOPMENT.md in the repo for detail. macOS twin: SAMPLE_PLAYER_MACOS.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/SAMPLE_PLAYER/blob/HEAD/README.md)
