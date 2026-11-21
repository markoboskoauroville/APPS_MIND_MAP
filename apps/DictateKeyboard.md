# TTT&LLL (Talk to Type, Look Listen Learn)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android voice keyboard (fork of Dictate on FlorisBoard): dictate with AssemblyAI, Gemini, Anthropic or offline Whisper and Parakeet, plus an AI reader.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/DictateKeyboard](https://github.com/markoboskoauroville/DictateKeyboard) |
| Also called | Voice Type, Mantra Voice Type, Talk to Type, TTT, TTT&LLL, ttt-lll, Dictate Keyboard, Voice Type keyboard |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: build-164 |
| Control level | none (no control api found) |

## What it can do

- Type by voice in any app with a microphone key and a transcribe screen (oscilloscope, spinner, clock)
- Transcribe with AssemblyAI, Gemini, Anthropic or fully offline Whisper or Parakeet
- Import API keys from a file instead of pasting
- Compress audio to Opus before upload
- Read text aloud with the AI reader (TTS handoff in AI_READER_HANDOFF.md)
- Apply the Auroville FlorisBoard theme pack

## Ask for it when

- dictate on my Android phone
- voice typing keyboard with my own keys
- offline Whisper keyboard
- talk to type on Android

## How to control it

No control API found.

Evidence: none found; it is an input method, not a server

## Inputs / Outputs

Inputs:

- microphone

Outputs:

- text typed into the focused field

## Works with

- Uses: [Auroville FlorisBoard Theme](auroville-florisboard-theme.md)
- Used by or talked to by: [Maha Transcribe Android v3 (web view, superseded) (retired)](MAHA_TRANSCRIBE_ANDROID.md), [MA Reader Engine](MA_READER_ENGINE.md), [Auroville FlorisBoard Theme](auroville-florisboard-theme.md)

## Code worth reusing

- `app/src/main/kotlin/dev/patrickgold/florisboard/dictate/`: dictation controller: record, Opus-compress, send to a speech-to-text provider, insert text

## Notes

Package com.mantraproductions.voicetype; APK named ttt-lll-build-N.apk. Fork of DevEmperor Dictate (Apache 2.0, see ATTRIBUTION.md). Many large handoff files (HANDOFF.md, TTT_LIGHT_HANDOFF.md, TTT_LLL_UX_HANDOFF.md) hold the state; HANDOFF.md warns it may lag the git log. Release tag is build-164. Tree listing truncated at 400 files. The master TTT profile is on the Nothing Phone 2a per the manifest.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/DictateKeyboard/blob/HEAD/README.md)
- [HANDOFF.md](https://github.com/markoboskoauroville/DictateKeyboard/blob/HEAD/HANDOFF.md)
