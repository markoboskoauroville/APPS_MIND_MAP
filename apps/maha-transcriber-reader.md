# Maha Transcriber and Reader (web)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One web page for speech-to-text and text-to-speech with word highlighting; eight voice providers; API keys stay on the device.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/maha-transcriber-reader](https://github.com/markoboskoauroville/maha-transcriber-reader) |
| Also called | Maha Transcribe, MA Reader web, maha transcriber reader, Transcribe and Read |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web |
| Language | JavaScript/HTML |
| Status | dormant |
| Last push | 2026-08-06 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Record speech and transcribe it with the user's own API keys
- Read pasted text aloud with word-by-word highlighting
- Choose among eight voice providers (browser, Gemini, Groq PlayAI, DeepInfra Kokoro, Azure, ElevenLabs, OpenAI, Google Cloud TTS)
- Load keys from a local text file into a cookie and test all keys
- Send text between the transcribe and read tabs
- Deploy as static page on GitHub Pages

## Ask for it when

- transcribe my voice in the browser
- read text aloud with highlighted words
- Croatian text to speech
- test my speech API keys

## How to control it

No control API found.

Evidence: api.txt empty; static page (index.html, tx.html, rd.html, tts.js, keys.js)

## Inputs / Outputs

Inputs:

- microphone
- pasted text
- key file

Outputs:

- text
- speech audio

## Code worth reusing

- `tts.js`: Browser-callable TTS wrapper for eight providers with CORS-checked endpoints
- `keys.js`: Loads keys in any layout from a plain text file and stores them in a cookie

## Notes

Web sibling of the desktop Maha Transcribe (desktop/Termux versions are separate repos). Cookies must be allowed or keys are forgotten. Only the browser voice gives exact word timing.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/maha-transcriber-reader/blob/HEAD/README.md)
