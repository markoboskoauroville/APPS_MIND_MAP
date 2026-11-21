# Teacher Lessons and Scripts (Ableton, DaVinci)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Private command-line side of the two Teachers: lesson history, live.py (Ableton via AbletonOSC), resolve.py (DaVinci Resolve) and teacher.py.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ABLETON_TEACHER](https://github.com/markoboskoauroville/ABLETON_TEACHER) |
| Also called | The Teachers, Ableton Teacher (Mantra), DaVinci Teacher (Mantra), davinci teacher |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Audio, music and DJ](../capabilities/audio-music-dj.md) |
| Platforms | macOS, Hammerspoon |
| Language | Python, Swift, Lua |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Show a floating panel with NEXT, STOP and MIC and do approved steps on the real window
- Read and set Ableton Live over AbletonOSC (live.py)
- Read and set DaVinci Resolve via its scripting API (resolve.py)
- Speak explanations with cached voice and transcribe the mic locally
- Take screenshots of the app for the AI to see

## Ask for it when

- teach me Ableton step by step
- teach me DaVinci Resolve
- set Live tempo from a script
- list Resolve timelines and clips
- put a marker on the Resolve timeline

## How to control it

- Level: **cli**
- Type: cli, osc, python-module

Actions:

- `teacher.py use|up|snap|step|reply|say|ask|down|state|transcribe`
- `live.py ping|song|get|set|ritard`
- `resolve.py ping|info|page|timelines|timeline|pool|tc|marker|renders|render|save|py`

**Before you call:** Run in a checkout of this repo. For Resolve: Resolve must be open with scripting set to Local (resolve.py sets the environment itself). For Ableton: AbletonOSC installed as the Control Surface in Live; python3 live.py ping must answer.

Example:

```
python3 resolve.py marker 250 Red "look here" # DaVinci Resolve: a timeline marker; arguments: position (250 in the README example), colour, note
```

More calls:

- Ableton: set the tempo by an AbletonOSC address: `python3 live.py set /live/song/set/tempo 96`
- Ableton: tempo, tracks, clips: `python3 live.py song`
- Resolve: move the playhead / switch page: `python3 resolve.py tc 01:00:10:00 ; python3 resolve.py page color`
- Resolve: anything else of the scripting API: `python3 resolve.py py "timeline.GetTrackCount('video')"`

Evidence: README.md "The API sides"; app/Door.swift

## Inputs / Outputs

Inputs:

- microphone
- screen of the app

Outputs:

- spoken steps
- panel text
- OSC and scripting calls

## Works with

- Uses: [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md), [Ableton Teacher and DaVinci Teacher apps (Mantra)](MANTRA_TEACHERS.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)
- Used by or talked to by: [Ableton Command Guide](ABLETON_COMMAND_GUIDE.md), [Ableton Teacher and DaVinci Teacher apps (Mantra)](MANTRA_TEACHERS.md)

## Code worth reusing

- `live.py`: AbletonOSC client over UDP to read and set Live model
- `resolve.py`: DaVinci Resolve scripting API wrapper CLI

## Notes

Swift code and build moved to public repo MANTRA_TEACHERS on 13.11.2026; this repo stays as data/history. Contains an Oracle VM scripts folder. The Teacher windows (apps with the HTTP door on 8970/8971/8972) are the Swift apps in public MANTRA_TEACHERS; this repo has only the command-line side. The marker position argument is shown as 250 with no unit in the README (a frame number is assumed).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
