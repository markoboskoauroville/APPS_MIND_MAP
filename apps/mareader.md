# EdgeReader (MA Reader Streamlit)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Streamlit text-to-speech reader: paste text, pick an Edge neural voice, words highlight in time; plus a speech-to-speech translate tab.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mareader](https://github.com/markoboskoauroville/mareader) |
| Also called | MA Reader, MA Reader Web, MA Reader web port, EdgeReader |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | dormant |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Read pasted text aloud sentence by sentence with Edge neural voices in 13 languages incl. Croatian and Hindi
- Highlight each word with timing measured from the audio waveform with ffmpeg
- Keep a History of past texts and replay them
- Export a zip of per-sentence mp3, text and word timing manifest, and re-import it without resynthesis
- Translate speech: record or upload, transcribe (Groq Whisper or AssemblyAI), translate, speak
- Offer reading comfort options (themes, dyslexia font, auto scroll, ebook full-screen mode)

## Ask for it when

- read this text aloud with highlighted words
- Croatian text to speech reader
- translate my speech between Croatian, English and German
- make per-sentence mp3 files from a text

## How to control it

No control API found.

Evidence: README.md, streamlit_app.py, engine.py; no control API in api.txt hits

## Inputs / Outputs

Inputs:

- pasted text
- microphone or audio upload

Outputs:

- spoken audio
- zip of mp3 per sentence with timings

## Code worth reusing

- `engine.py`: Edge TTS synthesis with ffmpeg waveform word timing, translation and language handling
- `karaoke.py`: Word-highlighting karaoke playback component

## Notes

Runs on free Streamlit Community Cloud. Needs ffmpeg for exact timing (packages.txt). Secrets via secrets.toml (example only in repo).

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/mareader/blob/HEAD/README.md)
