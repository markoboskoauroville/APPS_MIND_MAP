# APPS_MIND_MAP

A map of every app, tool and reusable code module Marko Bosko has built, in one place, written for an AI session that has a task in hand.
Each repository has one card in `apps/`. Each card says what the app does, when to ask for it, how to control it from outside, and which code in it can be copied.
The apps are built so that other programs can drive them: a local HTTP door, a command line or a Python client. That is how the apps are chained into one ecosystem.
Code that already exists is reused as modules instead of written again, so MODULES.md lists what can be lifted from where.
Everything except `data/` and `prompts/` is generated from `data/apps.json` by `tools/build_map.py`. Edit the data, not the pages.

## How an AI uses this map

1. **Find the task.** Search first: `grep -ri <word> CAPABILITIES.md capabilities/ KEYWORDS.md` (a device, a port, an action name or a task word), or open `index.html` and type it. Examples that work: `sony`, `midi`, `transcribe`, `light`, `neewer`, `play-loop`, `8965`. Then read the matching file in `capabilities/` (or [CAPABILITIES.md](CAPABILITIES.md)): its task lines are grouped by category, and the first line of each app carries the port and a working example call. A "Which one to pick" guide at the top of a category chooses between look-alike apps. If the search ends at "Not built yet", no app does the job: build it as a new app. For a device see [HARDWARE.md](HARDWARE.md).
2. **Open the app card** (`apps/REPO.md`) only if you need the full action list, the evidence or the notes.
3. **Call the app through its API.** The standard protocol (the Mantra Door pattern):
   - the app listens on `127.0.0.1` only, on a port claimed in `MANTRA_PORTS` under its id (for example `meditation-room` is 8965; that number is also quoted for [MPA Lessons Analyzer](apps/MPA_LESSONS_ANALYZER.md), [Second Take Remote](apps/SECOND_TAKE_REMOTE.md), so confirm with `mantra-ports scan`);
   - `GET /health` answers `{app, name, version, pid}`; `GET /api` lists the actions, each with a one-sentence `does`; `POST /api/<action>` takes a JSON body and answers `{ok: true, result}` or `{ok: false, error}`; `GET /api/state` is optional;
   - from Python use `mantra_remote.py` (`remote.call("meditation-room", "stop")`); it talks to the Mantra Door on the Mac, which starts a stopped app, forwards the call and needs the door token (never printed or committed);
   - a call needs no token on `127.0.0.1` for an app's own door; other routes use the `X-Mantra-Token` header;
   - Android and Termux have no common door: Android apps use adb forwards, intents or an accessibility door (for example port 8790), Termux apps write their live port to `~/.mantra/ports/<command>`. Each card says which.
   - [CONTROL_API.md](CONTROL_API.md) lists every app that can be driven, grouped by how (door, http, other protocols, command line, adb, accessibility).
4. **If no app does it**, open [MODULES.md](MODULES.md): the code to copy (audio, camera, BLE and USB, UI kits, networking, AI providers, updater and more). Copy the module, do not rewrite it.
5. **See who talks to whom** in [CONNECTIONS.md](CONNECTIONS.md) and the whole picture in [MIND_MAP.md](MIND_MAP.md).
6. **If a new app is built, add its card:** add a record to `data/apps.json` (same keys as the other records), run `python3 tools/build_map.py`, commit the changed files. An app that is not on the map is not finished.

## How to claim a port for a new app

- Ask the registry for the next free number: `mantra-ports next` (from the MANTRA_PORTS card); write it in the app's README.
- In the app's server claim it: `PORT = ports.claim('<app-id>', <number>)` (Python `ports.py`, Swift `Ports.swift`, Lua `ports.lua`). It takes that number if free, else the next free one, and records it.
- Clients ask `ports.url('<app-id>', <number>)` for the live address instead of hard-coding the number.
- Before a release run `mantra-ports scan` (no port named twice) and `mantra-ports check` (names the holder of a clash).

## Rules of this ecosystem

- Every app ships the control API from its first version: `/health`, `/api`, `POST /api/<action>` on a claimed port.
- Reuse before writing: look in this map for an app to call or code to copy before building anything.
- Work in modules: a feature that another app could use lives in a module with its own path and one clear job.
- One branch, `main`. Whole-number versions, visible in the app.
- A planner model plans, briefs and scores the result; workers on lower models build and test.
- Secrets stay in local files, never in a repository. This repository holds no secrets, addresses or personal data.
- The full rules live in the private `MANTRA_MANIFEST` repository; they are not repeated here.

## The numbers

- 275 live repositories have a card (152 are apps; the rest are tools, libraries, websites, guides, data and config); 13 more are retired and marked so.
- 151 of the live ones can be driven from outside (14 at the standard door level).
- By control level: door 14, http 67, other 4, cli 52, adb 4, accessibility 10, none 124.
- By platform (a repository can be on several): macOS 153, Android 80, Termux 25, Windows 7, Linux 28, Web 75, Cloud 45, iOS 1, Hammerspoon 10, Chrome 6.
- 4 empty repositories have no card; 32 were left out for privacy (see [STATUS.md](STATUS.md)).

## Not built yet

A search that ends here means no app does the job yet.

- **Gong or singing-bowl sound source** (not built): No app generates or plays a gong or bowl. Closest: MANTRA_ROOM plays any track in a loop and has a soft bell for its session timer; SHRUTI_BOX_AND_VOICE_TRAINER is a drone and raga box, not a gong.
- **Neewer / Bluetooth LED light control** (planned): Light Control (Mantra), also called Mantra Neewer, is planned: a Mac app for the Neewer light over Bluetooth LE with a local HTTP API (kickoff prompt prompts/LIGHT_CONTROL.md). Nothing in the map controls Bluetooth LED lights; the only light API is the G815 keyboard.
- **Microphone-reactive visualization in Meditation Room** (planned): Planned in the same prompt: Mantra Room listens to the room microphone so MilkDrop follows an ambient sound such as a gong, and the colours drive the lights slowly. MANTRA_ROOM has MilkDrop visuals but no microphone input today.
- **Sony white balance, Kelvin and exposure-compensation control from a script** (planned): Planned as an addition to Webcam Recorder (web-cam-viewer) for the Alpha 7 V over USB. The overlay already lists white balance, Kelvin and EV as settings reachable through /sony/set, but the Sony USB road is not verified against a body (v27) and the manifest documents no PTP codes for them.
- **Reading aloud with word highlighting in a native Android app** (not built): MA Reader for Android (MA_READER_ANDROID) does not speak yet; use the Termux reader MA_READER_TERMUX_MACOS.
- **Story Medicine (therapeutic stories from a parent's voice note)** (planned): THERAPEUTIC_STORIES is a planned Android app; nothing runs yet.
- **Gemini chat on the phone in Termux** (planned): GCLOUD_CHAT_TERMUX is a plan; only the brief exists.
- **Standard /health + /api door on Android apps** (not built): No Android app serves the standard door; phones are reached through the Claude Control door (8790), the macro door (8841), TERMUX_VOICE (8840) or adb broadcasts.
- **Mantra Door as a repository** (not built): The token-guarded gateway to all Mac apps and the Python client mantra_remote.py are described in the manifest module remote-door.md; no repo of them is in this map.
- **Light Control (Mantra)** (planned): Planned Mac app that drives a Neewer Bluetooth LED light with smooth colour transitions and a local API, linked to Meditation Room and, through Webcam Recorder, to a Sony camera. [kickoff prompt](prompts/LIGHT_CONTROL.md), [card](apps/LIGHT_CONTROL.md)

## Categories

- [Voice, dictation and transcription](capabilities/voice-dictation-transcription.md): 35
- [Audio, music and DJ](capabilities/audio-music-dj.md): 18
- [Mixers, MIDI and audio hardware](capabilities/mixer-midi-audio-hardware.md): 18
- [Camera, video, NDI and streaming](capabilities/camera-video-ndi-streaming.md): 14
- [Film and editing (DaVinci Resolve)](capabilities/film-editing-resolve.md): 17
- [AI agents and Claude tooling](capabilities/ai-agents-claude-tooling.md): 33
- [Mac system utilities](capabilities/mac-system-utilities.md): 33
- [Android and Termux](capabilities/android-termux.md): 17
- [Remote control and networking](capabilities/remote-control-networking.md): 16
- [Lights, keyboard and visuals](capabilities/lights-keyboard-visuals.md): 2
- [Wellbeing, sound and meditation](capabilities/wellbeing-sound-meditation.md): 8
- [Websites and pages](capabilities/websites-pages.md): 13
- [Knowledge, books and guides](capabilities/knowledge-books-guides.md): 25
- [Learning and academy](capabilities/learning-academy.md): 6
- [Maps, travel and location](capabilities/maps-travel-location.md): 9
- [Keys, secrets and infrastructure](capabilities/keys-secrets-infrastructure.md): 6
- [Data, backups and misc](capabilities/data-backups-misc.md): 5

## Files

- [MIND_MAP.md](MIND_MAP.md): the brain as diagrams and as an outline.
- [CAPABILITIES.md](CAPABILITIES.md): task index (index of categories; the task lines are in `capabilities/`).
- [KEYWORDS.md](KEYWORDS.md): alphabetical keyword index (words, ports, action names).
- [CONTROL_API.md](CONTROL_API.md): how to call each app, plus the apps still without an API.
- [HARDWARE.md](HARDWARE.md): device to apps.
- [MODULES.md](MODULES.md): reusable code.
- [CONNECTIONS.md](CONNECTIONS.md): who talks to whom.
- [STATUS.md](STATUS.md): housekeeping lists.
- `index.html`: search page.
- `apps/`: one card per repository.
- `data/apps.json`: the single source of truth. `data/planned.json`: apps planned but not built. `data/guides.json`: which-one-to-pick guides and gaps. `data/repos.tsv`: repository metadata. `prompts/`: kickoff prompts for new apps.
- `tools/build_map.py`: rebuilds every generated file (`--check` exits 1 if a generated file is out of date). `tools/import_catalog.py`: one-off import of a catalog folder into `data/apps.json` with a local exclude file.

## Keeping the map current

1. Edit `data/apps.json` (or `data/planned.json`, `data/guides.json`).
2. Run `python3 tools/build_map.py` (Python 3, standard library only). It rewrites all generated files and checks that every link resolves.
3. Run it twice: the second run must change nothing. `python3 tools/build_map.py --check` does that check without writing.
4. When a planned app is built, move it from `data/planned.json` into `data/apps.json` as a full record.
