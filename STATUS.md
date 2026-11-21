# Status and housekeeping

## Counts

- Records read from the catalog: 324
- Left out for privacy: 32
- Empty repositories, no card: 4
- Cards written: 288 (275 live, 13 retired)
- Live cards by control level: door 14, http 67, other 4, cli 52, adb 4, accessibility 10, none 124

## Empty repositories

- `CLAUDE_CODE_LOCAL` (private)
- `MANTRA_REMOTE` (private)
- `MANTRA_REMOTE_CLIENT` (private)
- `song-analasys` (private)

## Retired or archived, and what replaced them

- [Brain Brake Keyboard (Hammerspoon) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md): GitHub marks it archived.
- [Claude Code Monitor (Mantra) (retired)](apps/CLAUDE_CODE_MONITOR.md): Archived on GitHub.
- [DaVinci Resolve Assistant (retired)](apps/DAVINCI_RESOLVE_ASSISTANT.md): replaced by [DaVinci Resolve Actions (Mantra)](apps/DAVINCI_RESOLVE_ACTIONS.md)
- [Maha Transcribe Android v3 (web view, superseded) (retired)](apps/MAHA_TRANSCRIBE_ANDROID.md): replaced by [Maha Transcribe Android (native)](apps/MAHA_TRANSCRIBE_ANDROID_2.md)
- [Maha Transcribe Termux v1 (superseded) (retired)](apps/MAHA_TRANSCRIBE_TERMUX.md): replaced by [Maha Transcribe (Termux/terminal)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md)
- [Keyboard and Mouse Router (Mantra), retired (retired)](apps/MANTRA_KEYBOARD_MOUSE_ROUTER.md): replaced by [Macro Recorder (Mantra)](apps/MANTRA_MACRO.md)
- [Transcribe Voice to Text RT (Mantra), retired (retired)](apps/MARKO_TRANSCRIBE.md): replaced by [Vox to Txt (Mantra)](apps/MANTRA_VOICE_TO_TEXT.md)
- [Pesty fork (archive) (retired)](apps/pesty-fork-archive.md): replaced by [Pasty](apps/Pasty.md)
- [Find a File Spotlight (Mantra), retired (retired)](apps/spotlight.md): replaced by [Find a File (Mantra)](apps/FIND_FILE.md)
- [Stream Deck Control (Mantra), retired (retired)](apps/stream-deck-control.md): replaced by [Stream Deck Remote](apps/STREAM_DECK_REMOTE.md)
- [Voice Engine Android (retired) (retired)](apps/VOICE_ENGINE_ANDROID.md): replaced by [Termux Voice (voiced)](apps/TERMUX_VOICE.md)
- [Voice of Claude (Mantra), retired (retired)](apps/VOICE_OF_CLAUDE.md): replaced by [Voice Engine (Mantra)](apps/VOICE_ENGINE.md)
- [WhatsApp audio HAL (moved) (retired)](apps/wa-audio-hal.md): Replaced by WHATSAPP_REMOTE_VIEWER.

## Low-confidence records to re-read

- [Brain Brake book](apps/BRAIN_BRAKE_BOOK.md): The Brain Brake as a book (BOOK.md) with narrated audio per section in Hume and other voices, built by Python.
- [Google Cloud Chat for Termux](apps/GCLOUD_CHAT_TERMUX.md): Planned Termux copy of Queen's Google Cloud chat: Flask+waitress page for Gemini models paid from the GCP free credit; only the brief exists so far.
- [Key Tester (Android)](apps/Key_Tester.md): Android app for testing API keys per provider; its README is only a download link, the source tree names a key parser, provider table and Google matrix.
- [Maha Transcribe Android (native)](apps/MAHA_TRANSCRIBE_ANDROID_2.md): Native Kotlin/Compose rewrite of Maha Transcribe for Android; version 1 is the T (talk to type) screen only, built for a dyslexic, low-vision user.
- [Mantra Voice to Text (downloads)](apps/mantra-voice-to-text-downloads.md): Release-files-only repo for Mantra Voice to Text, free offline Whisper dictation for Mac and Windows (press F1, talk, press F1).
- [Fooocus Streamlit front end](apps/marko-fooocus.md): Streamlit front end with a Google Colab notebook backend for Fooocus image generation (early experiment).
- [Marko Transcribe (Streamlit)](apps/marko-transcribe.md): Streamlit web transcriber that sends audio to AssemblyAI with a rotating ring of keys, ffmpeg handling and results logged to Google Sheets (v3.16).
- [Music page](apps/music.md): Single index.html music page; purpose not documented.
- [Star Monitor (Mantra)](apps/STAR_MONITOR.md): Mac window that manages every app of the star menu: start, stop, order, run-time tracking and which apps come back after a restart.

## Port collisions

Same port number written in more than one card (may be different machines; each card carries a warning; check with `mantra-ports scan`):

- 5055: [Drive Downloader](apps/DRIVE_DOWNLOADER.md), [GDrive Downloader (Flask, macOS)](apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md)
- 8081: [MA Reader Speechify module](apps/MA_READER_SPEECHIFY.md), [MA Reader Termux / macOS (Edge / Speechify)](apps/MA_READER_TERMUX_MACOS.md)
- 8765: [Queen auto-update (Groq Auto Update)](apps/groq-auto-update.md), [Queen (Groq AI Studio), server and tools](apps/groq_ai_studio.md), [Queen, Mac app (Groq AI Studio (Mantra))](apps/GROQ_AI_STUDIO_MAC.md)
- 8810: [Maha Transcribe / TTT-LLL (Streamlit)](apps/MAHA_TRANSCRIBE_STREAMLIT.md), [Maha Transcribe VM (TTT-LLL)](apps/MAHA_TRANSCRIBE_VM.md)
- 8837: [Mantra Voice (speech server)](apps/MANTRA_VOICE.md), [Voice Engine (Mantra)](apps/VOICE_ENGINE.md)
- 8841: [Cloud Mixer](apps/CLOUD_MIXER.md), [Installation Logger (Mantra)](apps/INSTALLATION_LOGGER.md), [Mantra Remote Viewing (Mantra Remote)](apps/MANTRA_REMOTE_VIEWING.md)
- 8847: [Agent Manager (CEO) (Mantra)](apps/AGENT_MANAGER.md), [Find a File Spotlight (Mantra), retired (retired)](apps/spotlight.md)
- 8851: [Star Monitor (Mantra)](apps/STAR_MONITOR.md), [YT Transcriber](apps/YT_TRANSCRIBER.md)
- 8869: [Suno Controller (Mantra)](apps/CHROME_SUNO_CONTROLLER.md), [Sound Recorder (Mantra)](apps/MANTRA_SOUND_RECORDER.md)
- 8890: [Session Hub](apps/SESSION_HUB.md), [Chromium Virtual Machine (Mantra)](apps/vm-chromium.md)
- 8965: [Mantra Room (Meditation Room / Chakra and Elements Toning)](apps/MANTRA_ROOM.md), [MPA Lessons Analyzer](apps/MPA_LESSONS_ANALYZER.md), [Second Take Remote](apps/SECOND_TAKE_REMOTE.md)

Mentioned in notes:

- [Agent Manager (CEO) (Mantra)](apps/AGENT_MANAGER.md): Port 8847 was also used by the retired spotlight (Find a File Spotlight).
- [Brain Freedom](apps/BRAIN_FREEDOM.md): Base port 8770 clashes with ahkedit's 8770 in the MANTRA_PORTS table.
- [Claude Remote (Mantra)](apps/CLAUDE_REMOTE.md): name chosen to avoid the clash.
- [Installation Logger (Mantra)](apps/INSTALLATION_LOGGER.md): Port 8841 is also quoted for another app in the manifest port table.
- [The Playable Instruction (Mantra filmmaking)](apps/MANTRA_FILMMAKING.md): TAKEOVER wins on conflicts.
- [Mantra Room (Meditation Room / Chakra and Elements Toning)](apps/MANTRA_ROOM.md): Port 8965 is also quoted for MPA_LESSONS_ANALYZER and SECOND_TAKE_REMOTE: confirm with GET /health (this app answers app: meditation-room) before calling.

## Duplicates and superseded pairs

- [222 Transcribe](apps/222-transcribe.md): Copy of 111-transcribe made for a second user.
- [Avid Assistant](apps/AVID_ASSISTANT.md): Superseded versions kept as history.
- [Brain Brake Keyboard (Hammerspoon) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md): RETIRED/SUPERSEDED: no replacement is named in the docs.
- [Brain Brake night bus](apps/BRAINBREAK_BUS.md): likely superseded by newer session tooling.
- [Claude Code Monitor (Mantra) (retired)](apps/CLAUDE_CODE_MONITOR.md): RETIRED/SUPERSEDED: no replacement is named in the docs.
- [DaVinci Resolve Assistant (retired)](apps/DAVINCI_RESOLVE_ASSISTANT.md): Superseded in practice by DAVINCI_RESOLVE_ACTIONS (same scripts plus the router and an app). RETIRED/SUPERSEDED: use DAVINCI_RESOLVE_ACTIONS instead.
- [TTT&LLL (Talk to Type, Look Listen Learn)](apps/DictateKeyboard.md): Fork of DevEmperor Dictate (Apache 2.0, see ATTRIBUTION.md).
- [Find a File (Mantra)](apps/FIND_FILE.md): Replaces the retired Find a File Spotlight (spotlight).
- [Queen auto-update (Groq Auto Update)](apps/groq-auto-update.md): Near duplicate of groq_ai_studio with the same README and API.
- [How I Made the TTT Keyboard](apps/HOW_I_MADE_TTT.md): Documentation about the TTT mini Android keyboard (a fork of Dictate).
- [Installation Logger (Mantra)](apps/INSTALLATION_LOGGER.md): the Python page is the older engine replaced by a Swift window.
- [Maha Transcribe Android v3 (web view, superseded) (retired)](apps/MAHA_TRANSCRIBE_ANDROID.md): Later superseded by the native MAHA_TRANSCRIBE_ANDROID_2. RETIRED/SUPERSEDED: use MAHA_TRANSCRIBE_ANDROID_2 instead.
- [Maha Transcribe Termux v1 (superseded) (retired)](apps/MAHA_TRANSCRIBE_TERMUX.md): superseded by MAHA_TRANSCRIBE_TERMUX_TERMINAL. RETIRED/SUPERSEDED: use MAHA_TRANSCRIBE_TERMUX_TERMINAL instead.
- [Maha Transcribe VM (TTT-LLL)](apps/MAHA_TRANSCRIBE_VM.md): Hard fork of MAHA_TRANSCRIBE_STREAMLIT.
- [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](apps/MANTRA_CONTROLS.md): MIDI Tools (Mantra) replaces them (v8 starts MIDI Tools instead of Hammerspoon). Likely superseded.
- [Keyboard and Mouse Router (Mantra), retired (retired)](apps/MANTRA_KEYBOARD_MOUSE_ROUTER.md): RETIRED/SUPERSEDED: use MANTRA_MACRO instead.
- [MIDI Tools (Mantra)](apps/MANTRA_MIDI_TOOLS.md): Replaces MANTRA_CONTROLS windows and the Lua engines.
- [Transcribe Voice to Text RT (Mantra), retired (retired)](apps/MARKO_TRANSCRIBE.md): RETIRED/SUPERSEDED: use MANTRA_VOICE_TO_TEXT instead.
- [Pasty](apps/Pasty.md): Fork of momenbasel/pesty (MIT).
- [Pesty fork (archive) (retired)](apps/pesty-fork-archive.md): Description says ARCHIVE, superseded by the private Pasty repo, safe to delete. RETIRED/SUPERSEDED: use Pasty instead.
- [Router Credits (Android)](apps/router-credits.md): Android twin of the Mac router-sms.
- [Sample Player, Android](apps/SAMPLE_PLAYER.md): macOS twin: SAMPLE_PLAYER_MACOS.
- [Find a File Spotlight (Mantra), retired (retired)](apps/spotlight.md): RETIRED/SUPERSEDED: use FIND_FILE instead.
- [Stream Deck Control (Mantra), retired (retired)](apps/stream-deck-control.md): replaced by Stream Deck Remote (Mantra). RETIRED/SUPERSEDED: use STREAM_DECK_REMOTE instead.
- [Termux Voice (voiced)](apps/TERMUX_VOICE.md): Replaces the retired Voice Engine Android app (port 8720): TERMUX_VOICE is the only voice engine on the phones.
- [TTT Voice Type keyboard](apps/TTT.md): Fork of Dictate (DevEmperor) on FlorisBoard, Apache 2.0.
- [Voice Engine Android (retired) (retired)](apps/VOICE_ENGINE_ANDROID.md): RETIRED/SUPERSEDED: use TERMUX_VOICE instead.
- [Voice of Claude (Mantra), retired (retired)](apps/VOICE_OF_CLAUDE.md): RETIRED/SUPERSEDED: use VOICE_ENGINE instead.
- [WhatsApp audio HAL (moved) (retired)](apps/wa-audio-hal.md): RETIRED/SUPERSEDED: use WHATSAPP_REMOTE_VIEWER instead.

## Catalog judgement and control level disagree

Catalog says no or unknown, but actions are listed (level shown):

- [Brain Brake Keyboard (Hammerspoon) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md) (cli)
- [CQ Ethernet Bridge](apps/CQ_ETHERNET_BRIDGE.md) (adb)
- [CQ MixPad Protocol](apps/cq_mixpad_protocol.md) (cli)
- [DJ Transfer Monitor (Mantra)](apps/DJ_TRANSFER_MONITOR.md) (accessibility)
- [Import Button (Mantra)](apps/IMPORT_BUTTON.md) (accessibility)
- [Maha Transcribe / TTT-LLL (Streamlit)](apps/MAHA_TRANSCRIBE_STREAMLIT.md) (http)
- [Maha Transcribe VM (TTT-LLL)](apps/MAHA_TRANSCRIBE_VM.md) (http)
- [MIDI to Key Stroke](apps/MIDI_TO_KEYSTROKE.md) (http)
- [Pianoverse Demo Songs by Mantra](apps/PIANOVERSE_DEMO_SONGS.md) (cli)
- [Sound Design](apps/SOUND_DESIGN.md) (cli)
- [Launcher (Mantra)](apps/STAR_LAUNCHER.md) (accessibility)
- [Star Monitor (Mantra)](apps/STAR_MONITOR.md) (door)
- [Swift Matrix (Mantra)](apps/SWIFT_MATRIX.md) (accessibility)
- [Talk Mode (Mantra)](apps/TALK_MODE.md) (cli)
- [Termux Emulator Image](apps/termux-emulator-image.md) (cli)

## Control level may be out of date

Level is http or door, but the notes say the API may belong to an older version of the app:

- [Find a File (Mantra)](apps/FIND_FILE.md) (door): The HTTP page (findd.py, port 8845) is the older engine; the current app is a native Swift window that replaced it, so the API may not be served by the app itself.
- [Installation Logger (Mantra)](apps/INSTALLATION_LOGGER.md) (http): the Python page is the older engine replaced by a Swift window.
- [Star Monitor (Mantra)](apps/STAR_MONITOR.md) (door): the HTTP API on 8851 belongs to the older Flask page and may not exist in the Swift version.

## Repositories with unmerged branches

- [Connection Keeper](apps/connection-keeper.md): 1
- [DJ Mantra (Android DJ app)](apps/djmantra_app.md): 1
- [Kukljica EcoOasis](apps/KUKLJICA_ECOOASIS.md): 3
- [Mantra Manual Camera](apps/mantra-manual-camera.md): 3
- [Mantra Remote Viewing (Mantra Remote)](apps/MANTRA_REMOTE_VIEWING.md): 1
- [obs2vmix](apps/obs2vmix.md): 17
