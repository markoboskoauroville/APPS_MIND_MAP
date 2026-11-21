# Mantra Voice (speech server)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**The system-wide local speech server: Whisper listening, cloned-voice speaking with word timings, a Voices page, and a READ button script for any page.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_VOICE](https://github.com/markoboskoauroville/MANTRA_VOICE) |
| Also called | Voices, the voice server, voiced, ears and voice, Voice engine server |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Transcribe audio with local Whisper (EN/HR/auto, word timings)
- Speak text in a cloned or Speechify voice and return mp3 plus word timings
- Queue and control a spoken reading (next, stop, pause, restart)
- Add, remove and choose voices from a short sample
- Render speech for phones over a token-guarded tailnet door
- Guard the microphone while another app records

## Ask for it when

- transcribe this audio file locally
- make the computer say this sentence
- clone a voice from a recording
- read a page aloud with the word highlighted
- speak a status message when a job is done

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8837

**Warning:** port 8837 is also quoted for [Voice Engine (Mantra)](VOICE_ENGINE.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /health`
- `POST /hear`
- `POST /say`
- `GET /say.mp3`
- `POST /speak`
- `GET /speaking`
- `POST /speak/next`
- `POST /speak/stop`
- `POST /speak/pause`
- `POST /speak/top`
- `GET /speak/bands`
- `GET /voices`
- `POST /current`
- `POST /add`
- `POST /remove`
- `POST /consent`
- `GET /micguard`
- `POST /micguard/skip`
- `GET /volume`
- `POST /volume`
- `POST /render`
- `GET /reader.js`

**Before you call:** Mantra Voice (the Flask server voiced.py) must be running on the Mac; speech and listening live only here, never start a second Whisper or TTS. Over Tailscale only /render, /hear, /voices and /health are open without the token.

Example:

```
curl -s -XPOST 127.0.0.1:8837/speak -H 'Content-Type: application/json' -d '{"text":"The render is done.","wait":true}'
```

More calls:

- stop or pause what is being read: `curl -s -XPOST 127.0.0.1:8837/speak/stop # also /speak/pause, /speak/next`
- text to an mp3 with word timings (for a page that highlights the words): `curl -s -XPOST 127.0.0.1:8837/say -H 'Content-Type: application/json' -d '{"text":"Hello"}' # answers mp3 plus tokens [{s,e,t,d}] and sents`
- what is being spoken now, and who asked: `curl -s 127.0.0.1:8837/speaking`
- list the voices: `curl -s 127.0.0.1:8837/voices`

Evidence: API.md and voiced.py

## Inputs / Outputs

Inputs:

- audio clips (wav, m4a)
- text
- voice reference samples

Outputs:

- transcripts
- mp3 speech with timing json
- spoken audio

## Hardware

- Apple silicon GPU (MLX)
- speakers
- microphone

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md), [Voice Engines (model hub)](VOICE_ENGINES.md)
- Talks to: [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md), [Mantra Voice Switch](MANTRA_VOICE_SWITCH.md), [Transcribe Voice to Text RT (Mantra) (retired)](MARKO_TRANSCRIBE.md), [Talk with Claude Code](TALK_WITH_CLAUDE.md), [Voice Cloning (Mantra)](VOICE_CLONING.md)
- Used by or talked to by: [Ableton Command Guide](ABLETON_COMMAND_GUIDE.md), [Teacher Lessons and Scripts (Ableton, DaVinci)](ABLETON_TEACHER.md), [Sound Recorder (Mantra)](MANTRA_SOUND_RECORDER.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Ableton Teacher and DaVinci Teacher apps (Mantra)](MANTRA_TEACHERS.md), [Mantra Voice Switch](MANTRA_VOICE_SWITCH.md), [Vox to Txt (Mantra)](MANTRA_VOICE_TO_TEXT.md), [Marko Bosko Therapies](MARKOBOSKO_THERAPIES.md), [Transcribe Voice to Text RT (Mantra) (retired)](MARKO_TRANSCRIBE.md), [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md), [Sample Player, macOS](SAMPLE_PLAYER_MACOS.md), [Skeleton (Mantra)](SKELETON.md), [Spectral Analyzer (Mantra)](SPECTRAL_ANALYZER.md), [Talk Mode (Mantra)](TALK_MODE.md), [Talk with Claude Code](TALK_WITH_CLAUDE.md), [TTT Voice Type keyboard](TTT.md), [Voice Cloning (Mantra)](VOICE_CLONING.md), [Voice Engine (Mantra)](VOICE_ENGINE.md), [Voice Engines (model hub)](VOICE_ENGINES.md), [Voice Engine Universal (Mantra)](VOICE_ENGINE_UNIVERSAL.md), [Voice of Claude (Mantra) (retired)](VOICE_OF_CLAUDE.md), [Claude Code hub](claude-code.md), [CQ MixPad Tutorial (Mantra)](cq_mixpad_tutorial.md)

## Code worth reusing

- `ears.py`: Whisper transcription behind a socket with warm-up and Croatian text fixes
- `clone.py`: zero-shot voice cloning from a short reference, with cache
- `timing.py`: word timings by listening again to generated speech
- `match.py`: builds a FIR curve that matches one voice to another
- `tools/voicedoor.py`: token-guarded tailnet door in front of the loopback API
- `tools/voicectl.py`: Python client and run/control helper for the server

## Notes

Not in git: voices, reference audio, caches, models. One server for all speech; do not add a second Whisper or TTS. Tailnet door exposes only /render /hear /voices /health without a token. Models live in VOICE_ENGINES hub. Very large repo because of lesson audio clips. POST /speak also takes from (who is talking) and clips (absolute file paths). The request body of POST /hear (speech to text) is not described in the harvested docs; for dictation the Vox to Txt app (MANTRA_VOICE_TO_TEXT, port 8865) has a documented /hear call. Port 8837 is the speech server; VOICE_ENGINE only talks to it (it does not own the port).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
