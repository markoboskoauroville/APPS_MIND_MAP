# Magic Coin

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac floating white ring: MA face transcribes speech, BA face reads aloud the text underneath it; clicks pass through the hole.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/magic-coin](https://github.com/markoboskoauroville/magic-coin) |
| Also called | MagicCoin, MA and BA coin, floating ring |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: v1.0 |
| Control level | none (no control api found) |

## What it can do

- Float a borderless click-through ring above all windows (background agent, no Dock icon)
- Transcribe speech to text (MA face)
- Screenshot the area under the ring, OCR it with Apple Vision and read it aloud (BA face)
- Show a visual shudder/pulse as feedback

## Ask for it when

- read aloud the text under my cursor on the Mac
- floating dictation button on screen
- speech to text widget for macOS

## How to control it

No control API found.

Evidence: api.txt empty; Sources/MagicCoin has App, CoinView, Keys, Reader, Transcriber only

## Inputs / Outputs

Inputs:

- microphone
- screen area under the ring (Screen Recording permission)

Outputs:

- transcribed text
- spoken audio

## Code worth reusing

- `Sources/MagicCoin/Reader.swift`: Screenshot a screen region, OCR with Vision and speak it
- `Sources/MagicCoin/CoinView.swift`: Borderless transparent floating ring panel with click-through hole

## Notes

Early v1.0 (Sept 2026), first compile was by GitHub Actions (README says it was written without a Swift toolchain). Croatian OCR is weak, English is accurate. Not a macOS Widget.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/magic-coin/blob/HEAD/README.md)
