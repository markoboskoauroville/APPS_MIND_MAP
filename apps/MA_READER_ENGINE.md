# MA Reader Engine

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Shared Kotlin library: Microsoft Edge speech WebSocket client with word boundaries, plus word-timing alignment; used by TTT's LLL reader and MA Reader Android.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MA_READER_ENGINE](https://github.com/markoboskoauroville/MA_READER_ENGINE) |
| Also called | reader engine, Edge speech client |
| Visibility | public |
| Kind | library-module |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-08-09 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Open the Edge read-aloud WebSocket, send SSML and receive audio with word boundaries
- Align spoken words to text (MaAlign)
- Clean and split text into units (MaText)
- Draw waveforms (MaWaveform)
- Prove behaviour against test vectors in CI

## Ask for it when

- text to speech with word timing in Kotlin
- reuse the Edge voice client
- highlight the spoken word
- engine for a native Android reader (MA Reader Android, LLL in TTT)

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- text and voice name

Outputs:

- audio plus word boundaries

## Works with

- Talks to: [TTT&LLL (Talk to Type, Look Listen Learn)](DictateKeyboard.md), [MA Reader for Android](MA_READER_ANDROID.md)
- Used by or talked to by: [MA Reader for Android](MA_READER_ANDROID.md)

## Code worth reusing

- `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaEdgeVoice.kt`: Edge speech WebSocket client on OkHttp (do not set Sec-WebSocket-Version)
- `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaAlign.kt`: word timing alignment
- `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaText.kt`: text cleaning and sentence splitting

## Notes

Consumed as a git submodule (engine-repo), never copied. Uses an unofficial Microsoft endpoint, so it may break.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MA_READER_ENGINE/blob/HEAD/README.md)
