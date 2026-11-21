# Capabilities: which app does what

One heading per app: platforms, API level and port, the main call and a `Before:` line when the call needs a step first. Below it the app's task phrases; a `call:` appears on a task only when it is the call for that task. API values: `door N` (standard door on port N), `http N`, `cli`, `adb`, `accessibility`, `other`, `none`. Retired apps are listed per category under "Retired - do not use", never as live lines. Search: `grep -ri <word> CAPABILITIES.md capabilities/ KEYWORDS.md`, or open `index.html`.

This index is small on purpose: pick the category, open its file (one file has all task lines of that category, with the port and a working call on the first line of each app). Guides that say which app to pick are at the top of each category file.

## Categories

- [Voice, dictation and transcription](capabilities/voice-dictation-transcription.md): 35 apps - 111 Transcribe, 222 Transcribe, EdgeReader, Google TTS and STT, GVoices, MA Reader Engine, MA Reader for Android, MA Reader Speechify module, MA Reader Termux / macOS, Mac Transcriber, Magic Coin, Maha Transcribe, Maha Transcribe / TTT-LLL, Maha Transcribe Android, and more
- [Audio, music and DJ](capabilities/audio-music-dj.md): 18 apps - Ableton Command Guide, Charts, DJ Mantra, DJ Transfer Monitor, djay Sync, Mac window, djay Sync, command line, Generated Playlists, MA Player, Music page, Pianoverse Demo Songs by Mantra, Screenshot to TIDAL, Shazam Local, Song Simple Mixer, Sound Design, and more
- [Mixers, MIDI and audio hardware](capabilities/mixer-midi-audio-hardware.md): 18 apps - Ableton Live Actions, AndroidVU, Audio Prefer, Controller Mapper, CQ Ethernet Bridge, CQ MixPad, CQ MixPad Protocol, CQ MixPad Tutorial, CQ VESA Adapter, Mantra Controls, Mantra Mackie Control Translator, MIDI to Key Stroke, MIDI Tools, Oxi Controller, and more
- [Camera, video, NDI and streaming](capabilities/camera-video-ndi-streaming.md): 14 apps - CineView Viewer, Cloud Mixer, Mantra Manual Camera, Mantra NDI Screen Share, Mantra NDI SDK, Mantra Sony Remote, Android, NDI Mantra Monitor, obs2vmix, Skeleton, Sony Remote, Mac, Sound Link, Streaming Dashboard, Virtual Cam, Webcam Recorder
- [Film and editing (DaVinci Resolve)](capabilities/film-editing-resolve.md): 17 apps - Animator Collaboration, Avid Assistant, Blender Control, Brain Brake 3D, Brain Brake audio, Brain Brake frames, Brain Brake originals, Brain Brake review wall, Colab Video Upscaler, DaVinci Resolve Actions, Free Voice Convert, Import Button, MKV Converter, Resolve Pages, and more
- [AI agents and Claude tooling](capabilities/ai-agents-claude-tooling.md): 33 apps - Agent Manager, Agent Manager for Android, Brain Brake night bus, Brain Freedom, CCMC, Claude Code hub, Claude Code Mantra OS, Claude Code Session Names, Claude Control, Claude Persist, Claude Remote, Claude Talkie, Cost Agent, Firefox Control, and more
- [Mac system utilities](capabilities/mac-system-utilities.md): 33 apps - App Store, Automated Mouse Actions, Cascade, Claude Enter, Clean Start, Code Filler, Dock Switcher, Download, Copy and Move, Drive Full Path, Find a File, FKeys, Free Mac, Hammerspoon Lua Recorder, Homebrew tap for Mantra tools, and more
- [Android and Termux](capabilities/android-termux.md): 17 apps - Android Lab, Auroville FlorisBoard Theme, Calendar Events, Claude Code for Termux, Cockpit Android, Cockpit Termux, Etno orkestar calendar assistant, FTP Server v4, gi, GitHub Repo, Google Cloud Chat for Termux, Mantra Route, Termux Emulator Image, Termux Tools, and more
- [Remote control and networking](capabilities/remote-control-networking.md): 16 apps - aooserver-arm64, Chromium Virtual Machine, Connection Controller Dashboard Viewer, Connection Keeper, LAN Scanner, Mantra Ports, Mantra Remote Viewing, Router Credits, Router Mode, Router SMS, Screen Copy, Second Take Remote, Star API, Stream Deck Remote, and more
- [Lights, keyboard and visuals](capabilities/lights-keyboard-visuals.md): 2 apps - G815 Lights, Keyboard Monitor
- [Wellbeing, sound and meditation](capabilities/wellbeing-sound-meditation.md): 8 apps - Asana Guide, Hemi-Sync Recording Monitor, Indian Mantras, Mantra Room, Mind Garden, Minimalist Stopwatch, Shruti Box and Voice Trainer, Story Medicine
- [Websites and pages](capabilities/websites-pages.md): 13 apps - DJ Mantra booking questionnaire, DJ Mantra Ecstatic Dance page, Donnie Horoscope, Green and Go Croatian Islands, Kukljica EcoOasis, Mantra Download Counter, Mantra Pages, Marko Apps site, Marko Bosko Therapies, Ples Duše pages, Santoshi Kirtan Band sites, Studio Setup, Work in Progress page
- [Knowledge, books and guides](capabilities/knowledge-books-guides.md): 25 apps - AI for Beginners, Astro DOS, Being a Self Publisher, Brain Brake book, Cause and Symptom, Ethno Hrvatska song sheets, How I Made the TTT Keyboard, How to Create a Winning Film, How to read a frame and hear what belongs in it, Manifest Intro, Moving Air, Ogledalo i prozor, Ogledalo i prozor references, Six Levels of Claude, and more
- [Learning and academy](capabilities/learning-academy.md): 6 apps - Ableton Teacher and DaVinci Teacher apps, DaVinci Grading Tutorial, MPA Academy, Android app, MPA Academy, website and hub, MPA Lessons Analyzer, Percussion School
- [Maps, travel and location](capabilities/maps-travel-location.md): 9 apps - ARKOD Layer, Maha Commute, Mantra ARKOD, Mantra Map Server, Mantra Maps, Mantra Trail, Spar Locator / DM Finder, Store & Pool Finder, ZET Strike
- [Keys, secrets and infrastructure](capabilities/keys-secrets-infrastructure.md): 6 apps - Key Tester, Keyring, KeyringTester, Oracle machine notes, TOML key merger, TTT Portal
- [Data, backups and misc](capabilities/data-backups-misc.md): 5 apps - Drive Downloader, GDrive Downloader, Lenovo Hunter, Photopea Studio, TataTalk (TataTalk)

## Which one to pick: guides

- Transcription (speech to text): Mac, Android, Termux, web, Croatian -> [Voice, dictation and transcription](capabilities/voice-dictation-transcription.md)
- Read aloud / text to speech: Mac, Android, Termux, engines -> [Voice, dictation and transcription](capabilities/voice-dictation-transcription.md)
- Voice dictation keyboard -> [Voice, dictation and transcription](capabilities/voice-dictation-transcription.md)
- Ableton Live -> [Audio, music and DJ](capabilities/audio-music-dj.md)
- Allen & Heath CQ-12T mixer (nine apps) -> [Mixers, MIDI and audio hardware](capabilities/mixer-midi-audio-hardware.md)
- OXI E16 and MIDI controllers -> [Mixers, MIDI and audio hardware](capabilities/mixer-midi-audio-hardware.md)
- Sony cameras: record, REC, settings, time code, live view, phone remote -> [Camera, video, NDI and streaming](capabilities/camera-video-ndi-streaming.md)
- DaVinci Resolve -> [Film and editing (DaVinci Resolve)](capabilities/film-editing-resolve.md)
- Controlling Claude Code sessions: phone, Mac, cloud -> [AI agents and Claude tooling](capabilities/ai-agents-claude-tooling.md)
- Ports and the door protocol: how any app is called -> [AI agents and Claude tooling](capabilities/ai-agents-claude-tooling.md)
- Keyboard lights and visuals -> [Mac system utilities](capabilities/mac-system-utilities.md)
- Controlling a Mac app that has no API (Accessibility, macros, Star API) -> [Mac system utilities](capabilities/mac-system-utilities.md)
- Cloud VMs: Android emulator and Chromium -> [Android and Termux](capabilities/android-termux.md)
- Maps, location, transit -> [Maps, travel and location](capabilities/maps-travel-location.md)

## Not built yet

Searches that end here mean no app on this map does the job yet.

- **Gong or singing-bowl sound source** (not built): No app generates or plays a gong or bowl. Closest: MANTRA_ROOM plays any track in a loop and has a soft bell for its session timer; SHRUTI_BOX_AND_VOICE_TRAINER is a drone and raga box, not a gong.
- **Neewer / Bluetooth LED light control** (planned): Light Control (Mantra), also called Mantra Neewer, is planned: a Mac app for the Neewer light over Bluetooth LE with a local HTTP API (kickoff prompt prompts/LIGHT_CONTROL.md). Nothing in the map controls Bluetooth LED lights; the only light API is the G815 keyboard.
- **Microphone-reactive visualization in Meditation Room** (planned): Planned in the same prompt: Mantra Room listens to the room microphone so MilkDrop follows an ambient sound such as a gong, and the colours drive the lights slowly. MANTRA_ROOM has MilkDrop visuals but no microphone input today.
- **Sony white balance, Kelvin and exposure-compensation control from a script** (planned): Planned as an addition to Webcam Recorder (web-cam-viewer) for the Alpha 7 V over USB. The overlay already lists white balance, Kelvin and EV as settings reachable through /sony/set, but the Sony USB road is not verified against a body (v27) and the manifest documents no PTP codes for them.
- **Reading aloud with word highlighting in a native Android app** (not built): MA Reader for Android (MA_READER_ANDROID) does not speak yet; use the Termux reader MA_READER_TERMUX_MACOS.
- **Story Medicine (therapeutic stories from a parent's voice note)** (planned): THERAPEUTIC_STORIES is a planned Android app; nothing runs yet.
- **Gemini chat on the phone in Termux** (planned): GCLOUD_CHAT_TERMUX is a plan; only the brief exists.
- **Standard /health + /api door on Android apps** (not built): No Android app serves the standard door; phones are reached through the Claude Control door (8790), the macro door (8841), TERMUX_VOICE (8840) or adb broadcasts.
- **Mantra Door as a repository** (not built): The token-guarded gateway to all Mac apps and the Python client mantra_remote.py are described in the manifest module remote-door.md; no repo of them is in this map.
- **Light Control (Mantra)** (planned): Planned Mac app that drives a Neewer Bluetooth LED light with smooth colour transitions and a local API, linked to Meditation Room and, through Webcam Recorder, to a Sony camera. [kickoff prompt](prompts/LIGHT_CONTROL.md)
