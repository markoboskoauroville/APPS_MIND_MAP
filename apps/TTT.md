# TTT Voice Type keyboard

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android voice-typing keyboard (Talk to Type): dictate into any text field with cloud or offline engines, with an RE reply assistant and an adb remote API. Fork**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TTT](https://github.com/markoboskoauroville/TTT) |
| Also called | Talk to Type, Voice Type, TTT Advanced Keyboard, TTT&LLL, Dictate Keyboard |
| Visibility | public |
| Kind | app |
| Category | [Voice, dictation and transcription](../capabilities/voice-dictation-transcription.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: build-697 |
| Control level | adb (android adb / intents) |

## What it can do

- Dictate into any text field with AssemblyAI, Gemini, Anthropic or offline Whisper/Parakeet
- Open a dedicated transcribe screen with oscilloscope and clock
- RE reply assistant: pop-up chat above the keyboard to reply, fix, translate; WhatsApp tab
- Route cloud dictation through a Frankfurt relay and use the Mac microphone over Screen Copy
- Re-transcribe history entries in another language, share corrections with MANTRA_CORRECTIONS
- Import keys from a file, never pasted
- Be driven by adb broadcasts (type, status, RE engine, RE ask, say, compare)

## Ask for it when

- dictate on the phone into any app
- voice keyboard for Android
- reply to a message with AI by voice
- compare transcription engines on the phone
- make the phone speak via TTT

## How to control it

- Level: **adb**
- Type: adb-intent

Actions:

- `dev.ttt.remote.TYPE`
- `dev.ttt.remote.STATUS`
- `dev.ttt.remote.RE_ENGINE`
- `dev.ttt.remote.RE_ASK`
- `dev.ttt.engines.SAY`
- `dev.ttt.engines.RE_COMPARE`
- `dev.ttt.engines.AAC_BENCH`
- `dev.ttt.engines.EXPORT_UI`
- `tools/ttt_remote.py`

**Before you call:** Phone on adb (cable or wireless); only adb can send these broadcasts (DUMP permission). Answers land in `files/remote/<id>.json` on the phone.

Example:

```
python3 tools/ttt_remote.py say "The render is done" # speaks through TTT; type into the focused field with the type verb
```

More calls:

- type text into the focused text field: `python3 tools/ttt_remote.py type "hello" # broadcast dev.ttt.remote.TYPE`
- key counts per ring (never the key values): `python3 tools/ttt_remote.py status # broadcast dev.ttt.remote.STATUS`
- ask the RE reply assistant: `# broadcast dev.ttt.remote.RE_ASK; the exact verb of tools/ttt_remote.py is not in the harvested docs`
- speed/accuracy bench AAC against WAV in Frankfurt: `adb shell am broadcast -a dev.ttt.engines.AAC_BENCH`

Evidence: TAKEOVER.md (Remote API, 13.11.2026), tools/ttt_remote.py; only adb can send (DUMP permission)

## Inputs / Outputs

Inputs:

- microphone
- key files
- Mac microphone over Screen Copy

Outputs:

- transcribed text in the focused field
- RE replies
- spoken output
- engine comparison json

## Hardware

- Android phone microphone

## Works with

- Uses: [Mantra Corrections](MANTRA_CORRECTIONS.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Talks to: [Screen Copy (Mantra)](MANTRA_SCREEN_COPY.md)
- Used by or talked to by: [Mantra Corrections](MANTRA_CORRECTIONS.md), [Screen Copy (Mantra)](MANTRA_SCREEN_COPY.md), [TTT Layouts](ttt-layouts.md)

## Code worth reusing

- `engines/FrankfurtRelay.kt`: routes cloud dictation through a relay with AAC upload
- `dictate/audio/MacMicLink.kt`: uses the Mac microphone as the phone's recording source
- `nlp/MaCorrectionsSync.kt`: syncs learned corrections with a shared repo
- `tools/ttt_remote.py`: adb-based remote client for the keyboard

## Notes

Big repo with a long DEVELOPMENT.md; HANDOFF.md is the start. Fork of Dictate (DevEmperor) on FlorisBoard, Apache 2.0. Package seen as com.mantraproductions.tttlight. Ancestor/siblings: TTT_MINI, TTT&LLL. The exact subcommand names of tools/ttt_remote.py other than say are taken from the broadcast names (TYPE, STATUS, RE_ASK) and were not checked against the script.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/TTT/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/TTT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/TTT/blob/HEAD/LESSONS.md)
