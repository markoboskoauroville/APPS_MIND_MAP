# Queen (Groq AI Studio), server and tools

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app 'Queen': local API on :8765 for chats with Claude/Gemini, deterministic Python skills and Ableton Live control by text; auto-updates itself.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/groq_ai_studio](https://github.com/markoboskoauroville/groq_ai_studio) |
| Also called | Queen, Groq AI Studio, Queen (Mantra), qwen, Queen CAPI, Quinn, Groq |
| Visibility | public |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python (backend), Swift (app) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v31 |
| Control level | http (own http routes) |

## What it can do

- Serve a local API on 127.0.0.1:8765 (Swift) proxying to a Python backend on 8766
- Run chats (CAPI) against external model providers (Claude Code, Gemini, Google Cloud) with working folder, attachments and optional cheapest-model router
- Run deterministic Python skills without a model call: list-skills, current-folder, ableton-control
- Control Ableton Live through typed, allowlisted AbletonOSC actions with a Macro Recorder takeover guard
- Run a supervised Auto Update that patches its own backend files and ships through GitHub Actions
- Keep a library of many Markdown skills (queen_skills/*.md) for Mac, WhatsApp, Sony camera, Meditation Room, router, etc.

## Ask for it when

- ask Queen to do a task on the Mac
- control Ableton Live by text command
- set the Ableton tempo
- send a prompt to Claude Code or Gemini from a script
- Queen CAPI python client
- auto-update the Queen app

## How to control it

- Level: **http**
- Type: http, python-module, cli
- Port: 8765 (Swift app; Python backend on 8766)

**Warning:** port 8765 is also quoted for [Queen auto-update (Groq Auto Update)](groq-auto-update.md), [Queen, Mac app (Groq AI Studio (Mantra))](GROQ_AI_STUDIO_MAC.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /api/capi/capabilities`
- `GET /api/capi/list`
- `GET /api/capi/get?id=`
- `POST /api/capi/new`
- `POST /api/capi/settings`
- `POST /api/capi/send`
- `POST /api/capi/start`
- `POST /api/capi/stop`
- `POST /api/capi/close`
- `GET /api/ableton/capabilities`
- `POST /api/ableton/action`
- `/api/auto_update/*`
- `ableton action: status`
- `ableton action: play`
- `ableton action: stop`
- `ableton action: continue`
- `ableton action: set_tempo`
- `ableton action: set_metronome`
- `ableton action: create_audio_track`
- `ableton action: create_midi_track`
- `ableton action: set_track_name`
- `ableton action: set_track_mute`
- `ableton action: set_track_solo`
- `ableton action: set_track_arm`
- `ableton action: set_track_volume`
- `ableton action: set_track_pan`
- `ableton action: fire_scene`
- `ableton action: fire_clip`
- `ableton action: stop_clip`
- `ableton action: load_audio_clip`
- `ableton action: load_audio_to_arrangement`
- `ableton action: list_devices`
- `ableton action: device_parameters`
- `ableton action: set_device_parameter`
- `ableton action: stop_all_clips`

**Before you call:** Queen's Swift app on 8765 and its Python backend on 8766 must be running; a CAPI chat id comes from /api/capi/list or /api/capi/new.

Example:

```
python3 tools/queen_capi.py send CHAT_ID "Run the focused tests" --wait
```

More calls:

- set the Ableton tempo through Queen: `curl -s -XPOST 127.0.0.1:8765/api/ableton/action -H 'Content-Type: application/json' -d '{"action":"set_tempo","arguments":{"bpm":120}}'`
- what Queen can do to Ableton / which chats exist: `curl -s 127.0.0.1:8765/api/ableton/capabilities ; curl -s 127.0.0.1:8765/api/capi/list`
- read a window through Accessibility (needs the Queen token header): `curl -s -XPOST 127.0.0.1:8765/api/ax/read -H 'X-Queen-Token: $(cat <queen token file>)' -H 'Content-Type: application/json' -d '{"app":"Firefox","query":"WhatsApp"}'`
- pause everything Queen does: `curl -s -XPOST 127.0.0.1:8765/api/pause`

Evidence: CAPI_PYTHON_API.md, README.md, qwen_app/queen_python_skills/ableton.py (_ACTION_SPECS), tools/queen_capi.py

## Inputs / Outputs

Inputs:

- text prompts
- attachments (images, PDF, text, audio, video)
- ~/.queen/api_token (optional)

Outputs:

- chat answers
- Ableton actions
- auto-update patches and releases

## Hardware

- Ableton Live via AbletonOSC (UDP 11000/11001 family)

## Works with

- Uses: [Ableton Live Actions (Mantra)](ABLETON_LIVE_ACTIONS.md), [Macro Recorder (Mantra)](MANTRA_MACRO.md), [Mantra Manifest](MANTRA_MANIFEST.md)
- Talks to: [Claude Code hub](claude-code.md)
- Used by or talked to by: [Queen, Mac app (Groq AI Studio (Mantra))](GROQ_AI_STUDIO_MAC.md), [Mantra Chrome Extensions](MANTRA_CHROME_EXTENSIONS.md)
- Planned, not built: [Light Control (Mantra)](LIGHT_CONTROL.md) will be driven by this app (Queen can drive it through the API)

## Code worth reusing

- `tools/queen_capi.py`: Stdlib-only Python client and CLI for Queen's CAPI and Ableton routes
- `qwen_app/queen_python_skills/ableton.py`: Typed allowlisted AbletonOSC action contract with one-based numbering and read-back
- `book_template/`: Book builder and deploy scripts (build.py, deploy.sh, style.css) used for a beginners AI book
- `queen_skills/`: Large library of Markdown skills describing how to drive Mac, phone, WhatsApp and camera tasks

## Notes

Main working repo of Queen (also called Groq AI Studio, qwen). Superset of groq-auto-update: also has gemini_image, lan_scan and webcam_recorder skills (POST /api/gemini/image). Legacy Groq chat removed in the v31 runtime; Android-emulator actions not yet converted. Mantra manifest also mentions 'queen `"<task>"'` CLI and /api/pause on this port.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/groq_ai_studio/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/groq_ai_studio/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/groq_ai_studio/blob/HEAD/LESSONS.md)
