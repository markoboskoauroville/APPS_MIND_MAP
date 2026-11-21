# Reusable modules

522 code modules in 223 repositories that another app could copy instead of rewriting. Each row: what it does, the repository card, and the path inside the repository. Private repositories are marked; ask Marko for access or copy the idea. Modules of retired apps are marked (retired).

## Remote door, ports and control API (45)

| What it does | Repo | Path |
|---|---|---|
| shared turn (flock) so only one program holds AbletonOSC answer port 11001 at a time; copied into other Swift apps | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) | `app/LiveTurn.swift` |
| MANTRA_PORTS claim helper | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) | `app/Ports.swift` |
| stdlib HTTP door bound to Tailscale address with bearer token re-read on every request | [Agent Manager (CEO) (Mantra) (AGENT_MANAGER)](apps/AGENT_MANAGER.md) | `helper/server.py` |
| Cloudflare Pages proxy that strips Origin so the state service answers | [ARKOD Layer (web) (arkod_web)](apps/arkod_web.md) | `functions/api/oss/[[path]].js` |
| Chrome MV3 service worker that polls a local door for commands and runs them in a dedicated tab | [Suno Controller (Mantra) (CHROME_SUNO_CONTROLLER)](apps/CHROME_SUNO_CONTROLLER.md) (private) | `extension/background.js` |
| three checks on every /api call so only the local page can POST | [Cockpit Termux (COCKPIT_TERMUX)](apps/COCKPIT_TERMUX.md) | `localguard.py` |
| preferred port, next fifteen, then OS port; writes `~/.mantra/ports/<command>` | [Cockpit Termux (COCKPIT_TERMUX)](apps/COCKPIT_TERMUX.md) | `portpick.py` |
| Swift port claiming/registry (MANTRA_PORTS) incl. fixed-port owner and UDP | [Connection Keeper (connection-keeper)](apps/connection-keeper.md) | `Sources/Aggregate/Ports.swift` |
| shared use of Ableton's OSC reply port with a lock so two sessions do not collide | [CQ MixPad Tutorial (Mantra) (cq_mixpad_tutorial)](apps/cq_mixpad_tutorial.md) (private) | `app/LiveTurn.swift` |
| timed hosts-file door with a root copy and a sudoers rule so apps can open it without a password | [Free Mac (FREE_MAC)](apps/FREE_MAC.md) (private) | `apple-door.sh` |
| preferred-port then next-free port picker | [GDrive Downloader (Flask, macOS) (GDRIVE_DOWNLOADER_FLASK_MACOS)](apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (private) | `portpick.py` |
| preferred port then next fifteen then any | [GVoices (Google Voices) (GoogleVoices)](apps/GoogleVoices.md) | `portpick.py` |
| loopback-only guard with three checks on every /api call | [Keyring (KEYRING_TERMUX)](apps/KEYRING_TERMUX.md) | `localguard.py` |
| pick a free port in a range | [Keyring (KEYRING_TERMUX)](apps/KEYRING_TERMUX.md) | `portpick.py` |
| claim a port from the MANTRA_PORTS registry with health path | [Dock Switcher (Mantra) (MACOS_TASK_SWITCHER)](apps/MACOS_TASK_SWITCHER.md) | `app/Ports.swift` |
| in-app loopback HTTP server feeding a WebView UI | [Maha Transcribe Android v3 (web view, superseded) (MAHA_TRANSCRIBE_ANDROID) (retired, use MAHA_TRANSCRIBE_ANDROID_2)](apps/MAHA_TRANSCRIBE_ANDROID.md) | `app/src/main/kotlin/com/mantraproductions/mahatranscribe/MahaServer.kt` |
| local-only request guard for /api POSTs | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `localguard.py` |
| never-fail port picker | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `portpick.py` |
| standard-library HTTP server with SSE and Last-Event-ID replay | [Mantra Bridge (MANTRA_BRIDGE)](apps/MANTRA_BRIDGE.md) (private) | `mac/bridge/httpd.py` |
| install a temporary add-on in running Firefox via WebDriver BiDi on port 9222 | [Drive Full Path (Mantra Productions) (MANTRA_DRIVE_PATH)](apps/MANTRA_DRIVE_PATH.md) | `tools/load_in_firefox.py` |
| MANTRA_PORTS claim helper | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) | `app/Ports.swift` |
| stdlib fixed-port static server that refuses another port | [Mantra Pages (mantra_pages)](apps/mantra_pages.md) (private) | `server.py` |
| Swift half, copied into each Swift app that serves HTTP | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) (private) | `Ports.swift` |
| Hammerspoon half of the same registry | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) (private) | `ports.lua` |
| Python port claim/find/url, stdlib only | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) (private) | `ports.py` |
| AccessibilityService door: gestures, screenshot, node tree, visible pointer | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `android/app/src/main/java/com/mantra/remote/ClaudeControl.kt` |
| HTTP door with /health, /api, /api/run per the remote-door protocol | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `android/app/src/main/java/com/mantra/remote/MacroDoor.kt` |
| standard remote-door HTTP server (/health, /api, `/api/<action>`) in Swift | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `mac/app/Door.swift` |
| loopback HTTP JSON control server with port range | [Screen Copy (Mantra) (MANTRA_SCREEN_COPY)](apps/MANTRA_SCREEN_COPY.md) | `app/ControlServer.swift` |
| tiny JSON-over-HTTP function door registered for STAR_API | [Sound Recorder (Mantra) (MANTRA_SOUND_RECORDER)](apps/MANTRA_SOUND_RECORDER.md) (private) | `app/Door.swift` |
| small loopback HTTP door with MANTRA_PORTS claim | [Ableton Teacher and DaVinci Teacher apps (Mantra) (MANTRA_TEACHERS)](apps/MANTRA_TEACHERS.md) | `app/Door.swift` |
| token-guarded tailnet door in front of the loopback API | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `tools/voicedoor.py` |
| small local HTTP server pattern for a SwiftUI app | [MPA Lessons Analyzer (MPA_LESSONS_ANALYZER)](apps/MPA_LESSONS_ANALYZER.md) | `app/Http.swift` |
| free port picker | [Store & Pool Finder (SHOP_FINDER)](apps/SHOP_FINDER.md) | `portpick.py` |
| tiny loopback HTTP API pattern | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](apps/SONY_REMOTE_MAC.md) | `app/Door.swift` |
| SSH port forward to the camera's PTP port | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](apps/SONY_REMOTE_MAC.md) | `app/Tunnel.swift` |
| Star API functions door | [Sound Link (Mantra) (SOUND_LINK)](apps/SOUND_LINK.md) | `app/Door.swift` |
| library, CLI and HTTP server for app control by Accessibility labels | [Star API (Mantra) (STAR_API)](apps/STAR_API.md) (private) | `starapi.py` |
| obs-websocket v5 client reading port and password from OBS config | [Stream Deck Remote (STREAM_DECK_REMOTE)](apps/STREAM_DECK_REMOTE.md) | `mac/app/OBS.swift` |
| Pins adb to 127.0.0.1:5555 and scans for the Wi-Fi debug port in one asyncio process | [Termux Tools (termux-tools)](apps/termux-tools.md) | `adbup/adbup` |
| free port picker | [TOML key merger (TOML)](apps/TOML.md) | `portpick.py` |
| Token-protected HTTP door over adb: install, test, tap, swipe, screenshot, logcat, shell | [vm-android (Pixel 7 in Oracle Cloud) (vm-android)](apps/vm-android.md) | `api/pixel7d.py` |
| Remote-door style HTTP agent with declared actions (/api) and token auth | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `agent/vm-agent.py` |
| Tiny loopback HTTP server on Network.framework with port file registration | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `app/ApiServer.swift` |
| Preferred port then next fifteen then OS port picker | [ZET Strike (zet_strike)](apps/zet_strike.md) | `app/portpick.py` |

## Updater, installer and releases (24)

| What it does | Repo | Path |
|---|---|---|
| shell four-test harness (mechanism, real, ugly, upgrade) for installers | [Claude Code for Termux (CLAUDE_CODE_TERMUX)](apps/CLAUDE_CODE_TERMUX.md) | `tests/lib.sh` |
| pull newest version and restart | [Cockpit Termux (COCKPIT_TERMUX)](apps/COCKPIT_TERMUX.md) | `selfupdate.py` |
| one-shot install of uv, Python, torch on MPS and Seed-VC with models (2.7 GB) | [Free Voice Convert (Equalizer) (FREE_VOICE_CONVERT)](apps/FREE_VOICE_CONVERT.md) | `engine/setup.sh` |
| generates one-file installer from source and template | [FTP Server v4 (ftp-server-termux-and-terminal)](apps/ftp-server-termux-and-terminal.md) (private) | `tools/build.sh` |
| versionless installer that reads LATEST and verifies the download | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](apps/GOOGLE_TTS_STT.md) | `get.sh` |
| self-update | [GVoices (Google Voices) (GoogleVoices)](apps/GoogleVoices.md) | `selfupdate.py` |
| mac-updater kit that asks at start for a newer GitHub release | [Hemi-Sync Recording Monitor (Mantra) (HEMISYNC_RECORDING_MONITOR)](apps/HEMISYNC_RECORDING_MONITOR.md) | `app/Updater.swift` |
| pull newest version from GitHub and restart | [Keyring (KEYRING_TERMUX)](apps/KEYRING_TERMUX.md) | `selfupdate.py` |
| skill for releasing an APK to phone, Drive and GitHub | [Mind Garden (kognius_app)](apps/kognius_app.md) (private) | `.claude/skills/release-apk/SKILL.md` |
| Edge speech WebSocket client on OkHttp (do not set Sec-WebSocket-Version) | [MA Reader Engine (MA_READER_ENGINE)](apps/MA_READER_ENGINE.md) | `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaEdgeVoice.kt` |
| self-update installer pattern | [MA Reader Termux / macOS (Edge / Speechify) (MA_READER_TERMUX_MACOS)](apps/MA_READER_TERMUX_MACOS.md) | `update.sh` |
| self-contained installer carrying all three apps and a verified-download pattern (get.sh) | [Maha Commute (MAHA_COMMUTE)](apps/MAHA_COMMUTE.md) | `30-maha_commute_v30.sh` |
| git-pull self-update | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `selfupdate.py` |
| Linux versions of the macro verbs | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `linux/mantra_macro/verbs.py` |
| check GitHub releases for a newer APK | [Minimalist Stopwatch (MINIMALIST_STOPWATCH)](apps/MINIMALIST_STOPWATCH.md) | `app/src/main/java/com/mantra/stopwatch/UpdateCheck.kt` |
| Updater kit for GitHub Latest releases in a menu-bar app | [Router Mode (Mantra) (router-mode)](apps/router-mode.md) | `app/Updater.swift` |
| one-command self-install and update from GitHub with file checks | [Sample Player, macOS (SAMPLE_PLAYER_MACOS)](apps/SAMPLE_PLAYER_MACOS.md) | `update.sh` |
| Termux global command with boot/update/install subcommands | [Store & Pool Finder (SHOP_FINDER)](apps/SHOP_FINDER.md) | `mapool` |
| GitHub self-updater | [Store & Pool Finder (SHOP_FINDER)](apps/SHOP_FINDER.md) | `selfupdate.py` |
| installs the six-icon set onto apps | [Star (Mantra), Swift menu (STAR_SWIFT)](apps/STAR_SWIFT.md) | `icons6/install_icons.py` |
| installs the service on the VM with systemd | [Streaming Dashboard (Mantra) (STREAMING_DASHBOARD)](apps/STREAMING_DASHBOARD.md) | `vm/install.sh` |
| one-line Termux installer with autostart in .bashrc | [Termux Voice (voiced) (TERMUX_VOICE)](apps/TERMUX_VOICE.md) | `install.sh` |
| Release gates that must pass before shipping | [Tidal DL (tidal_dl)](apps/tidal_dl.md) | `gates/run_gates.py` |
| Generates macOS and Termux installers from one source plus .sh.in templates | [Tidal DL (tidal_dl)](apps/tidal_dl.md) | `tools/build_installers.py` |

## AI providers, agents and prompts (38)

| What it does | Repo | Path |
|---|---|---|
| AbletonOSC client over UDP to read and set Live model | [Teacher Lessons and Scripts (Ableton, DaVinci) (ABLETON_TEACHER)](apps/ABLETON_TEACHER.md) (private) | `live.py` |
| collects Claude Code sessions, tasks, VM services and phones with timeouts; prints text or JSON | [Agent Manager (CEO) (Mantra) (AGENT_MANAGER)](apps/AGENT_MANAGER.md) | `helper/collect.py` |
| CLI client for the bridge with headless fallback | [Blender Control (blender-control)](apps/blender-control.md) | `.agents/skills/blender-control/scripts/blender_cli.py` |
| Thread-safe localhost TCP JSON-RPC server that runs bpy code on Blender's main thread via a timer queue | [Blender Control (blender-control)](apps/blender-control.md) | `.agents/skills/blender-control/scripts/blender_control_bridge.py` |
| Method for flicker-free, band-free frame-precise video edits in Blender VSE | [Blender Control (blender-control)](apps/blender-control.md) | `.agents/skills/video-frame-precise-edit/SKILL.md` |
| find the claude.ai tab in Chrome, read the finished reply, send text without moving the mouse | [Brain Brake night bus (BRAINBREAK_BUS)](apps/BRAINBREAK_BUS.md) | `tools/chatlink.py` |
| Claude Code SessionStart/UserPromptSubmit/Stop hook that feeds the chat page | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](apps/CCMC.md) | `chat_hook.py` |
| Speechify client with one-sentence cache | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](apps/CCMC.md) | `speechify.py` |
| PDF page OCR via Gemini plus Spotify track matching with Google-Search fallback | [Charts (charts)](apps/charts.md) (private) | `charts` |
| hook that names a Claude Code cloud session | [Claude Code hub (claude-code)](apps/claude-code.md) (private) | `.claude/hooks/cloud_session_name.py` |
| Stdlib-only locked per-day counter and Claude Code hook that returns sessionTitle | [Claude Code Session Names (claude-code-session-names)](apps/claude-code-session-names.md) | `session_name.py` |
| hook-driven retry and resume scheduler for Claude Code sessions | [Claude Persist (claude-persist)](apps/claude-persist.md) (private) | `persist.py` |
| find Claude Code process roots and trees from ps, SIGSTOP/SIGCONT them safely, protect named processes | [Claude Control (Mantra) (CLAUDE_CONTROL)](apps/CLAUDE_CONTROL.md) | `app/Core.swift` |
| stdlib approval gate with estimates, per-job grants, ledgers and a token-guarded remote path | [Cost Agent (Mantra) (COST_AGENT)](apps/COST_AGENT.md) | `gate/costagent.py` |
| Claude commands: test-on-phone, test-tidal, capture-mix-ultra (device test workflows) | [DJ Mantra (Android DJ app) (djmantra_app)](apps/djmantra_app.md) | `.claude/commands/` |
| Flask app with Gemini TTS/STT, key ring, ledger and fallback | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](apps/GOOGLE_TTS_STT.md) | `src/10_app.py` |
| Book builder and deploy scripts (build.py, deploy.sh, style.css) used for a beginners AI book | [Queen auto-update (Groq Auto Update) (groq-auto-update)](apps/groq-auto-update.md) | `book_template/` |
| Book builder and deploy scripts (build.py, deploy.sh, style.css) used for a beginners AI book | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](apps/groq_ai_studio.md) | `book_template/` |
| API key ring with logic for rotation on failure | [Groq Explorer (GROQ_EXPLORER)](apps/GROQ_EXPLORER.md) (private) | `app/src/main/kotlin/com/mantra/groqexplorer/data/Ring.kt` |
| Groq API client | [Groq Explorer (GROQ_EXPLORER)](apps/GROQ_EXPLORER.md) (private) | `app/src/main/kotlin/com/mantra/groqexplorer/net/Groq.kt` |
| endpoints, paging, models, speech marks, errors | [MA Reader Speechify module (MA_READER_SPEECHIFY)](apps/MA_READER_SPEECHIFY.md) (private) | `SPEECHIFY_API_GUIDE.md` |
| key ring, parser, rotation and tester | [MA Reader Speechify module (MA_READER_SPEECHIFY)](apps/MA_READER_SPEECHIFY.md) (private) | `speechify_keyring.py` |
| reference Flask routes for Speechify | [MA Reader Speechify module (MA_READER_SPEECHIFY)](apps/MA_READER_SPEECHIFY.md) (private) | `speechify_routes.py` |
| record, ffmpeg 16 kHz mono FLAC prep, Groq Whisper call with key rotation | [Maha Transcribe / TTT-LLL (Streamlit) (MAHA_TRANSCRIBE_STREAMLIT)](apps/MAHA_TRANSCRIBE_STREAMLIT.md) | `app.py` |
| AHP client: JSON-RPC over a Unix-socket WebSocket to VS Code's agent host | [MAI Worker (maiwork) (MAI_WORKER)](apps/MAI_WORKER.md) | `maiwork.py` |
| persistent Claude Code subprocess wrapper reading NDJSON events | [Mantra Bridge (MANTRA_BRIDGE)](apps/MANTRA_BRIDGE.md) (private) | `mac/bridge/session.py` |
| prompt to model judgement | [Mantra Router (MANTRA_ROUTER)](apps/MANTRA_ROUTER.md) (private) | `mod/hooks/judge.ts` |
| Claude Code mod registration with the band UI | [Mantra Router (MANTRA_ROUTER)](apps/MANTRA_ROUTER.md) (private) | `mod/hooks/register.tsx` |
| engine selection with Whisper, Groq and ring of keys | [Transcribe Voice to Text RT (Mantra) (MARKO_TRANSCRIBE) (retired, use MANTRA_VOICE_TO_TEXT)](apps/MARKO_TRANSCRIBE.md) (private) | `App/Sources/Engines.swift` |
| local LLM text-style cleanup server | [Transcribe Voice to Text RT (Mantra) (MARKO_TRANSCRIBE) (retired, use MANTRA_VOICE_TO_TEXT)](apps/MARKO_TRANSCRIBE.md) (private) | `server/styled.py` |
| skill describing how every academy task is done | [MPA Academy, website and hub (mpa-academy)](apps/mpa-academy.md) (private) | `.claude/skills/mpa-academy/SKILL.md` |
| make per-sentence Speechify audio with word marks and key rotation | [DaVinci Grading Tutorial (Mantra) (RESOLVE_GRADING_TUTORIAL)](apps/RESOLVE_GRADING_TUTORIAL.md) (private) | `tools/build_audio.py` |
| drop-in script giving Speechify keyboard control and click-to-read on any web page | [Speechify Keys (SPEECHIFY_KEYS)](apps/SPEECHIFY_KEYS.md) | `public/speechify-keys.js` |
| 15-key deck model and key rendering | [Stream Deck Remote (STREAM_DECK_REMOTE)](apps/STREAM_DECK_REMOTE.md) | `mac/app/Deck.swift` |
| Claude Code hook that sends phone notifications and lets a button push text back | [Termux Tools (termux-tools)](apps/termux-tools.md) | `notify/ccnotify.py` |
| Claude hook speaker with word timing and subtitle feed | [Termux Tools (termux-tools)](apps/termux-tools.md) | `talker/talker.py` |
| Skill telling sessions the VM is 'this machine' and how to work on it | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `.claude/skills/this-machine/SKILL.md` |
| encrypted key ring read from a key file with forward-only cursor | [Voice Engine Android (VOICE_ENGINE_ANDROID) (retired, use TERMUX_VOICE)](apps/VOICE_ENGINE_ANDROID.md) | `android/app/src/main/java/community/auroville/voiceengine/GroqKeys.kt` |

## Speech, transcription and voice (43)

| What it does | Repo | Path |
|---|---|---|
| AssemblyAI transcription engine with multi-key fallback and ffmpeg handling, usable outside Streamlit | [111 Transcribe (111-transcribe)](apps/111-transcribe.md) | `transcribe_engine.py` |
| AssemblyAI transcription engine with key ring failover | [222 Transcribe (222-transcribe)](apps/222-transcribe.md) (private) | `transcribe_engine.py` |
| match a spoken word to a key command | [Brain Brake Keyboard (Hammerspoon) (BRAIN_BRAKE_KEYBOARD) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md) | `voice_match.py` |
| Flask server with pty terminal over websocket, voice transcription with key fallback, image-drop-to-git pipeline, key harvester | [Brain Freedom (BRAIN_FREEDOM)](apps/BRAIN_FREEDOM.md) | `src/bf_server.py` |
| browser recording to ffmpeg to Whisper path | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](apps/CCMC.md) | `voice.py` |
| prints or speaks the project handover at session start | [Claude Code hub (claude-code)](apps/claude-code.md) (private) | `handover.py` |
| glides the real mouse to a control of another app, clicks it, with a ring and caption | [CQ MixPad Tutorial (Mantra) (cq_mixpad_tutorial)](apps/cq_mixpad_tutorial.md) (private) | `app/Hand.swift` |
| builds per-sentence narration with word marks via TTS, only for edited sentences | [CQ MixPad Tutorial (Mantra) (cq_mixpad_tutorial)](apps/cq_mixpad_tutorial.md) (private) | `tools/build_audio.py` |
| dictation controller: record, Opus-compress, send to a speech-to-text provider, insert text | [TTT&LLL (Talk to Type, Look Listen Learn) (DictateKeyboard)](apps/DictateKeyboard.md) | `app/src/main/kotlin/dev/patrickgold/florisboard/dictate/` |
| voice descriptions and emotion direction | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](apps/GOOGLE_TTS_STT.md) | `src/42_voicesex.py` |
| renders every sentence in every voice once, keyed by hash | [Indian Mantras (Mantra) (INDIAN_MANTRAS)](apps/INDIAN_MANTRAS.md) (private) | `tools/render_voices.py` |
| chunked transcription with engine order, key rotation and per-chunk resume | [Mac Transcriber (scribe) (MAC_TRANSCRIBER)](apps/MAC_TRANSCRIBER.md) (private) | `scribe.py` |
| Screenshot a screen region, OCR with Vision and speak it | [Magic Coin (magic-coin)](apps/magic-coin.md) | `Sources/MagicCoin/Reader.swift` |
| Browser-callable TTS wrapper for eight providers with CORS-checked endpoints | [Maha Transcriber and Reader (web) (maha-transcriber-reader)](apps/maha-transcriber-reader.md) | `tts.js` |
| recording and WAV writing for Android | [Maha Transcribe Android (native) (MAHA_TRANSCRIBE_ANDROID_2)](apps/MAHA_TRANSCRIBE_ANDROID_2.md) | `app/src/main/kotlin/com/mantra/mahatranscribe/audio/Recorder.kt` |
| masked API key ring handling | [Maha Transcribe Android (native) (MAHA_TRANSCRIBE_ANDROID_2)](apps/MAHA_TRANSCRIBE_ANDROID_2.md) | `app/src/main/kotlin/com/mantra/mahatranscribe/logic/Keys.kt` |
| transcription HTTP call to a provider | [Maha Transcribe Android (native) (MAHA_TRANSCRIBE_ANDROID_2)](apps/MAHA_TRANSCRIBE_ANDROID_2.md) | `app/src/main/kotlin/com/mantra/mahatranscribe/net/Transcribe.kt` |
| store-first recording queue with SQLite WAL and Waitress in Termux | [Maha Transcribe Termux v1 (superseded) (MAHA_TRANSCRIBE_TERMUX) (retired, use MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX.md) | `1-maha-transcribe-v1-termux.sh` |
| zero-shot voice cloning from a short reference, with cache | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `clone.py` |
| Whisper transcription behind a socket with warm-up and Croatian text fixes | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `ears.py` |
| builds a FIR curve that matches one voice to another | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `match.py` |
| word timings by listening again to generated speech | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `timing.py` |
| Python client and run/control helper for the server | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) (private) | `tools/voicectl.py` |
| TTT dictate/NLP corrections in Swift (Croatian fixes, names) | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](apps/MANTRA_VOICE_TO_TEXT.md) | `mac/Sources/Corrections.swift` |
| transcription engine abstraction over several providers | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](apps/MANTRA_VOICE_TO_TEXT.md) | `mac/Sources/Engines.swift` |
| Edge TTS synthesis with ffmpeg waveform word timing, translation and language handling | [EdgeReader (MA Reader Streamlit) (mareader)](apps/mareader.md) | `engine.py` |
| AssemblyAI upload/poll engine with key ring, retry and verdict logic | [Marko Transcribe (Streamlit) (marko-transcribe)](apps/marko-transcribe.md) | `transcribe_engine.py` |
| audio catalogue run using local Whisper to check tracks | [Marko Bosko Therapies (MARKOBOSKO_THERAPIES)](apps/MARKOBOSKO_THERAPIES.md) | `tools/hsrun.py` |
| CLI that splits a drum lesson into voice and drum tracks (ffmpeg + parameter presets) | [MPA Lessons Analyzer (MPA_LESSONS_ANALYZER)](apps/MPA_LESSONS_ANALYZER.md) | `drumsplit/main.swift` |
| audio processing for re-voiced cells | [Sample Player, Android (SAMPLE_PLAYER)](apps/SAMPLE_PLAYER.md) | `app/src/main/java/com/mantra/sampleplayer/Dsp.kt` |
| Flask server: slot recording, transcription, voice transform with quality report, clone consent | [Sample Player, macOS (SAMPLE_PLAYER_MACOS)](apps/SAMPLE_PLAYER_MACOS.md) | `server.py` |
| voice activity detection with noise-floor threshold | [Talk Mode (Mantra) (TALK_MODE)](apps/TALK_MODE.md) | `app/Audio.swift` |
| client for the Mantra voice /hear and /speak API and phrase noise filters | [Talk Mode (Mantra) (TALK_MODE)](apps/TALK_MODE.md) | `app/Voice.swift` |
| Mac CLI that sends text to the phone voice | [Termux Voice (voiced) (TERMUX_VOICE)](apps/TERMUX_VOICE.md) | `mac/phonesay` |
| stdlib HTTP speech queue daemon with notification controls and a clients allowlist (Tailscale range and loopback) | [Termux Voice (voiced) (TERMUX_VOICE)](apps/TERMUX_VOICE.md) | `voiced.py` |
| uses the Mac microphone as the phone's recording source | [TTT Voice Type keyboard (TTT)](apps/TTT.md) | `dictate/audio/MacMicLink.kt` |
| routes cloud dictation through a relay with AAC upload | [TTT Voice Type keyboard (TTT)](apps/TTT.md) | `engines/FrankfurtRelay.kt` |
| resizable subtitle card that follows the spoken word | [Voice Engine (Mantra) (VOICE_ENGINE)](apps/VOICE_ENGINE.md) | `app/Subtitle.swift` |
| CLI for the one global voice ON/OFF state file | [Voice Engine (Mantra) (VOICE_ENGINE)](apps/VOICE_ENGINE.md) | `tools/voiceengine` |
| subtitle overlay drawn over other apps | [Voice Engine Android (VOICE_ENGINE_ANDROID) (retired, use TERMUX_VOICE)](apps/VOICE_ENGINE_ANDROID.md) | `android/app/src/main/java/community/auroville/voiceengine/Overlay.kt` |
| the call contract between voice server and subtitle | [Voice Engine Universal (Mantra) (VOICE_ENGINE_UNIVERSAL)](apps/VOICE_ENGINE_UNIVERSAL.md) | `SPEC.md` |
| pause/continue state machine for a subtitle synced to a voice server | [Voice Engine Universal (Mantra) (VOICE_ENGINE_UNIVERSAL)](apps/VOICE_ENGINE_UNIVERSAL.md) | `swift/PauseSync.swift` |
| one-at-a-time download, transcribe, knowledge pass with resume | [YT Transcriber (YT_TRANSCRIBER)](apps/YT_TRANSCRIBER.md) (private) | `yt_transcribe.py` |

## MIDI, OSC and mixers (36)

| What it does | Repo | Path |
|---|---|---|
| turns a spoken order into AbletonOSC messages restricted to /live/ addresses | [Ableton Command Guide (ABLETON_COMMAND_GUIDE)](apps/ABLETON_COMMAND_GUIDE.md) (private) | `act.py` |
| Python OSC client for AbletonOSC using the same shared-turn rule | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) | `helpers/liveosc.py` |
| drives CQ MixPad by accessibility: connect, scenes, input source, names | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) | `helpers/mixpad.py` |
| Python client and bin/cloudmix shell command | [Cloud Mixer (CLOUD_MIXER)](apps/CLOUD_MIXER.md) | `cloud_mixer/client.py` |
| frame-accurate Python/numpy mixer using ffmpeg only for decode and one encode | [Cloud Mixer (CLOUD_MIXER)](apps/CLOUD_MIXER.md) | `cloud_mixer/engine.py` |
| run a show file at an exact UTC second with pre-checks | [Cloud Mixer (CLOUD_MIXER)](apps/CLOUD_MIXER.md) | `cloud_mixer/show.py` |
| decoded CQ-12T protocol (moved to public repo cq_mixpad_protocol on 8.11.2026) | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](apps/CQ_MIXPAD_MANTRA.md) | `PROTOCOL.md` |
| CQ-12T wire protocol client (handshake, get, set, dump) | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](apps/CQ_MIXPAD_MANTRA.md) | `android/app/src/main/java/com/mantra/cqmixpad/Cq.kt` |
| Machine-readable CQ message format, channel numbers, value scales and decoded parameters for any app talking to a CQ | [CQ MixPad Protocol (cq_mixpad_protocol)](apps/cq_mixpad_protocol.md) | `protocol.json` |
| Man-in-the-middle sniffer/injector for the CQ TCP session | [CQ MixPad Protocol (cq_mixpad_protocol)](apps/cq_mixpad_protocol.md) | `tools/cq_mitm.py` |
| Typed allowlisted AbletonOSC action contract with one-based numbering and read-back | [Queen auto-update (Groq Auto Update) (groq-auto-update)](apps/groq-auto-update.md) | `qwen_app/queen_python_skills/ableton.py` |
| Stdlib-only Python client and CLI for Queen's CAPI and Ableton routes | [Queen auto-update (Groq Auto Update) (groq-auto-update)](apps/groq-auto-update.md) | `tools/queen_capi.py` |
| Typed allowlisted AbletonOSC action contract with one-based numbering and read-back | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](apps/groq_ai_studio.md) | `qwen_app/queen_python_skills/ableton.py` |
| Stdlib-only Python client and CLI for Queen's CAPI and Ableton routes | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](apps/groq_ai_studio.md) | `tools/queen_capi.py` |
| Mackie Control message encoder (buttons, 14-bit faders, V-Pot, jog) | [Mantra Mackie Control Translator (mantra-mackie-control-translator)](apps/mantra-mackie-control-translator.md) (private) | `mcu.lua` |
| rule engine translating MIDI input kinds to Mackie output kinds | [Mantra Mackie Control Translator (mantra-mackie-control-translator)](apps/mantra-mackie-control-translator.md) (private) | `rules.lua` |
| tool to send raw Mackie messages for testing | [Mantra Mackie Control Translator (mantra-mackie-control-translator)](apps/mantra-mackie-control-translator.md) (private) | `tests/sendmk.c` |
| Mackie Control engine: MIDI in to MCU commands for Live | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) | `app/MackieEngine.swift` |
| MIDI to key stroke engine with rules | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) | `app/MidiKeysEngine.swift` |
| ready macros for CQ MixPad tabs, layers, gain/gate/comp/PEQ panels and faders | [Mantra Sandbox (MANTRA_SANDBOX)](apps/MANTRA_SANDBOX.md) | `macros/cqmixpad/` |
| OSC wire helper for Live questions | [Star (Mantra), Lua (Hammerspoon, legacy) (MANTRA_STAR)](apps/MANTRA_STAR.md) (private) | `a1_ears.py` |
| pure Lua OSC encode/decode for AbletonOSC | [Star (Mantra), Lua (Hammerspoon, legacy) (MANTRA_STAR)](apps/MANTRA_STAR.md) (private) | `a1_osc.lua` |
| shared MIDI device watcher and incoming-message monitor | [MIDI to Key Stroke (MIDI_TO_KEYSTROKE)](apps/MIDI_TO_KEYSTROKE.md) (private) | `midiwatch.lua` |
| ask AbletonOSC to show a view until it answers | [Opening and Closing (Mantra) (OPENING_AND_CLOSING)](apps/OPENING_AND_CLOSING.md) (private) | `app/Ableton.swift` |
| OXI E16 Remote Mode: SysEx screen/ring protocol over CoreMIDI | [Oxi Controller (E16 Remote) (oxi-controller)](apps/oxi-controller.md) | `Sources/E16/E16Remote.swift` |
| Resolve mixer client through the Resolve Actions router with mute-by-gain workaround | [Oxi Controller (E16 Remote) (oxi-controller)](apps/oxi-controller.md) | `app/Resolve.swift` |
| AbletonOSC handler adding /live/view/zoom_arrangement | [Oxi Controller (E16 Remote) (oxi-controller)](apps/oxi-controller.md) | `tools/AbletonOSC-view.py` |
| Encode CQ-12T NRPN/PC/note messages | [OXI-CQ Bridge (oxi_e16_cq-12t)](apps/oxi_e16_cq-12t.md) | `oxi_cq_bridge/cq_protocol.py` |
| JSON mapping engine from controller slots to mixer parameters | [OXI-CQ Bridge (oxi_e16_cq-12t)](apps/oxi_e16_cq-12t.md) | `oxi_cq_bridge/mapping.py` |
| Dependency-free HTTP+SSE server with a web UI for MIDI controllers | [OXI-CQ Bridge (oxi_e16_cq-12t)](apps/oxi_e16_cq-12t.md) | `oxi_cq_bridge/server.py` |
| write MIDI clips and colours into a running Live set over AbletonOSC in batches of 100 notes | [Pianoverse Demo Songs by Mantra (PIANOVERSE_DEMO_SONGS)](apps/PIANOVERSE_DEMO_SONGS.md) (private) | `build.py` |
| reed tuning, wavetable and mixer, no Android dependency | [Shruti Box and Voice Trainer (SHRUTI_BOX_AND_VOICE_TRAINER)](apps/SHRUTI_BOX_AND_VOICE_TRAINER.md) | `app/src/main/java/com/mantra/shrutibox/Reeds.kt` |
| decode and resample to 48 kHz stereo | [Song Simple Mixer (Song_simple_mixer)](apps/Song_simple_mixer.md) | `app/src/main/java/community/auroville/mantra/mixer/Decoder.kt` |
| mix, limiter and dithered export | [Song Simple Mixer (Song_simple_mixer)](apps/Song_simple_mixer.md) | `app/src/main/java/community/auroville/mantra/mixer/Mix.kt` |
| band-wise vocal-aware ducking of a backing track | [Song Simple Mixer (Song_simple_mixer)](apps/Song_simple_mixer.md) | `app/src/main/java/community/auroville/mantra/mixer/Space.kt` |
| NDI video + mixer audio encoder pushing RTMP at 25 fps | [Sound Link (Mantra) (SOUND_LINK)](apps/SOUND_LINK.md) | `studio/studio.py` |

## Audio, music and DJ (33)

| What it does | Repo | Path |
|---|---|---|
| align two recordings of the same music to the sample and export equal-length WAVs; runs without Live (--a --b --out) | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) | `helpers/audio_sync.py` |
| renders sentence audio, joins it and writes timing JSON for word highlighting | [Asana Guide (Mantra) (ASANA_GUIDE)](apps/ASANA_GUIDE.md) (private) | `tools/render_audio.py` |
| CPU percent from idle counters when /proc/stat is denied (Android 16) | [Cockpit Android (COCKPIT_ANDROID)](apps/COCKPIT_ANDROID.md) | `app/src/main/java/com/mantra/cockpit/Sampler.kt` |
| WASM audio analyzer with worker for waveform/track analysis in the browser | [DJ Mantra Ecstatic Dance page (djmantra-ecstatic-dance)](apps/djmantra-ecstatic-dance.md) | `assets/analyzer/` |
| Scripts that build the toning player audio, waveform and chapter data (mentioned in README) | [DJ Mantra Ecstatic Dance page (djmantra-ecstatic-dance)](apps/djmantra-ecstatic-dance.md) | `tools/toning/` |
| Research on beat grid and slicer behaviour of djay for reuse | [DJ Mantra (Android DJ app) (djmantra_app)](apps/djmantra_app.md) | `docs/research/djay-beatgrid-slicer.md` |
| Mixxx engine tree (268 top-level entries) with Android Oboe audio output | [DJ Mantra (Android DJ app) (djmantra_app)](apps/djmantra_app.md) | `lib/` |
| JSON song data to two-page PDF with PyMuPDF and Open Sans | [Ethno Hrvatska song sheets (ETHNO-HRVATSKA)](apps/ETHNO-HRVATSKA.md) | `tools/render_pdf.py` |
| profile spectrum match EQ, loudness levelling and clean chain | [Free Voice Convert (Equalizer) (FREE_VOICE_CONVERT)](apps/FREE_VOICE_CONVERT.md) | `engine/dsp.py` |
| serves a folder of music as a web player controlling mpv over IPC | [MA Player (ma-player)](apps/ma-player.md) (private) | `bin/maweb-engine` |
| ffmpeg audio optimisation | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `audioprep.py` |
| loop playback to a chosen output device | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `mac/app/Player.swift` |
| jitter-buffered audio output per tab | [Screen Copy (Mantra) (MANTRA_SCREEN_COPY)](apps/MANTRA_SCREEN_COPY.md) | `app/Audio.swift` |
| scrcpy-server protocol client: video H.264 to VideoToolbox, raw audio | [Screen Copy (Mantra) (MANTRA_SCREEN_COPY)](apps/MANTRA_SCREEN_COPY.md) | `app/Session.swift` |
| IOProc based input and output with dB metering | [Sound Recorder (Mantra) (MANTRA_SOUND_RECORDER)](apps/MANTRA_SOUND_RECORDER.md) (private) | `app/Audio.swift` |
| capture one app's audio through a CoreAudio process tap | [Sound Recorder (Mantra) (MANTRA_SOUND_RECORDER)](apps/MANTRA_SOUND_RECORDER.md) (private) | `app/ProcTap.swift` |
| Word-highlighting karaoke playback component | [EdgeReader (MA Reader Streamlit) (mareader)](apps/mareader.md) | `karaoke.py` |
| one audio player module shared by sample list and demo therapy mode | [Marko Bosko Therapies (MARKOBOSKO_THERAPIES)](apps/MARKOBOSKO_THERAPIES.md) | `site/player.js` |
| controller layout format (shapes, LEDs, steps) usable as a template | [Controller Mapper (Mantra) (mix-ultra-mapper)](apps/mix-ultra-mapper.md) (private) | `layouts/hercules-djcontrol-mix-ultra.json` |
| AudioTrack sample sequencer whose light follows playbackHeadPosition | [MPA Academy, Android app (MPA_ACADEMY_ANDROID)](apps/MPA_ACADEMY_ANDROID.md) | `android/app/src/main/java/com/mantra/mpaacademy/Engine.kt` |
| slicing of strokes/clips from audio | [MPA Lessons Analyzer (MPA_LESSONS_ANALYZER)](apps/MPA_LESSONS_ANALYZER.md) | `app/Slicer.swift` |
| AVAudioEngine Audio Unit rack with bypass, reorder and meters | [Plugin Assistant (PLUGIN_ASSISTANT)](apps/PLUGIN_ASSISTANT.md) | `app/Rack.swift` |
| API key storage and key parsing | [Sample Player, Android (SAMPLE_PLAYER)](apps/SAMPLE_PLAYER.md) | `app/src/main/java/com/mantra/sampleplayer/KeyRing.kt` |
| floating overlay button that records over any app | [Sample Player, Android (SAMPLE_PLAYER)](apps/SAMPLE_PLAYER.md) | `app/src/main/java/com/mantra/sampleplayer/Overlay.kt` |
| loopback test server of the Second Take protocol | [Second Take Remote (SECOND_TAKE_REMOTE)](apps/SECOND_TAKE_REMOTE.md) | `mock/guide.py` |
| AudioTrack float synth engine on its own thread | [Shruti Box and Voice Trainer (SHRUTI_BOX_AND_VOICE_TRAINER)](apps/SHRUTI_BOX_AND_VOICE_TRAINER.md) | `app/src/main/java/com/mantra/shrutibox/Engine.kt` |
| measures audio/video offset from a clap | [Sound Link (Mantra) (SOUND_LINK)](apps/SOUND_LINK.md) | `tools/clap_offset.py` |
| pitch to note and piano mapping | [Spectral Analyzer (Mantra) (SPECTRAL_ANALYZER)](apps/SPECTRAL_ANALYZER.md) (private) | `app/Pitch.swift` |
| spectrogram rendering | [Spectral Analyzer (Mantra) (SPECTRAL_ANALYZER)](apps/SPECTRAL_ANALYZER.md) (private) | `app/Spek.swift` |
| Shell wrapper that reaches a phone's adb via loopback or Shizuku with a keep-alive watcher | [Termux Tools (termux-tools)](apps/termux-tools.md) | `phonelink` |
| loopback guard against cross-tab requests to a local server | [TOML key merger (TOML)](apps/TOML.md) | `guard.py` |
| SonoBus-based multichannel audio sender/receiver with VU strip for Mac, Linux, Android | [vm-android (Pixel 7 in Oracle Cloud) (vm-android)](apps/vm-android.md) | `mantra-sonobus/` |
| AOSP audio HAL with hooks for custom audio routing | [WhatsApp audio HAL (moved) (wa-audio-hal) (retired)](apps/wa-audio-hal.md) (private) | `src/audio_hw.c` |

## Camera, video and NDI (56)

| What it does | Repo | Path |
|---|---|---|
| DaVinci Resolve scripting API wrapper CLI | [Teacher Lessons and Scripts (Ableton, DaVinci) (ABLETON_TEACHER)](apps/ABLETON_TEACHER.md) (private) | `resolve.py` |
| small NDI source finder/receiver used to check emulator NDI streams | [Android Lab (android-lab)](apps/android-lab.md) (private) | `ndi_find.c` |
| Kotlin horoscope engine (planets, houses, aspects) and text-mode screen renderer | [Astro DOS (astro_dos)](apps/astro_dos.md) (private) | `android/app/src/main/java/com/astrodos/zodiac` |
| generate an OBJ mesh in plain Python without Blender | [Brain Brake 3D (BRAIN_BRAKE_3D)](apps/BRAIN_BRAKE_3D.md) | `scripts/brain_break_key_source.py` |
| Annex-B H.264/HEVC NAL parsing for VideoToolbox | [CineView Viewer (CINEVIEW_VIEWER)](apps/CINEVIEW_VIEWER.md) (private) | `Sources/CineViewCore/NAL.swift` |
| reassembles fragmented video messages into frames | [CineView Viewer (CINEVIEW_VIEWER)](apps/CINEVIEW_VIEWER.md) (private) | `Sources/CineViewCore/Reassembler.swift` |
| waits for Resolve's API and parks Resolve on a safe page | [Colab Video Upscaler (colab-video-upscaler)](apps/colab-video-upscaler.md) (private) | `resolve_up.py` |
| man-in-the-middle proxy to capture the desk protocol | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](apps/CQ_MIXPAD_MANTRA.md) | `tools/cq_mitm.py` |
| Resolve page switching | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ACTIONS.md) | `app/Pages.swift` |
| safe cleanup of Resolve renders, caches and proxies to Trash | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ACTIONS.md) | `scripts/Project Backup.py` |
| command line client for the router | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ACTIONS.md) | `scripts/resolve-run` |
| queue, timeout and BUSY detection for Resolve's scripting API; run code with resolve, project, pm in a killable worker | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ACTIONS.md) | `scripts/resolve_router.py` |
| resolves macOS URL bookmarks to find moved files | [djay Sync, command line (djay-sync) (djay-playlists)](apps/djay-playlists.md) (private) | `tools/resolve_bookmarks.swift` |
| vector melody staff and frame-drum rhythm box for PDFs | [Ethno Hrvatska song sheets (ETHNO-HRVATSKA)](apps/ETHNO-HRVATSKA.md) | `tools/notation.py` |
| Large library of Markdown skills describing how to drive Mac, phone, WhatsApp and camera tasks | [Queen auto-update (Groq Auto Update) (groq-auto-update)](apps/groq-auto-update.md) | `queen_skills/` |
| Large library of Markdown skills describing how to drive Mac, phone, WhatsApp and camera tasks | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](apps/groq_ai_studio.md) | `queen_skills/` |
| build image plates for the book | [Moving Air (Hi-Fi and Acoustics) (HIFI_AND_ACOUSTICS)](apps/HIFI_AND_ACOUSTICS.md) | `make_plates.py` |
| Streamlit localStorage bridge via declare_component | [Maha Transcribe / TTT-LLL (Streamlit) (MAHA_TRANSCRIBE_STREAMLIT)](apps/MAHA_TRANSCRIBE_STREAMLIT.md) | `ls_bridge.py` |
| Streamlit custom component bridging browser localStorage via postMessage | [Maha Transcribe VM (TTT-LLL) (MAHA_TRANSCRIBE_VM)](apps/MAHA_TRANSCRIBE_VM.md) (private) | `ls_bridge.py` |
| NDI sender bridge with hardware encoder keyframe handling for Android | [Mantra Manual Camera (mantra-manual-camera)](apps/mantra-manual-camera.md) | `app/src/main/cpp/ndi_bridge.cpp` |
| Headless camera streaming mode for a Mac-side consumer | [Mantra Manual Camera (mantra-manual-camera)](apps/mantra-manual-camera.md) | `app/src/main/java/com/mantraproductions/ndi/SkeletonMode.kt` |
| Python adb driver for the camera: state, settings, ISO, shutter, WB, focus, lens, snap | [Mantra Manual Camera (mantra-manual-camera)](apps/mantra-manual-camera.md) | `scripts/mcam` |
| NDI sender bridge for Android (compressed and full paths) | [Mantra NDI Screen Share (Android) (mantra-ndi-screen-share-android)](apps/mantra-ndi-screen-share-android.md) | `app/src/main/cpp/ndi_bridge.cpp` |
| Pure functions for sizing, orientation, bitrate and NDI cost estimates, with unit tests | [Mantra NDI Screen Share (Android) (mantra-ndi-screen-share-android)](apps/mantra-ndi-screen-share-android.md) | `app/src/main/java/com/mantraproductions/ndiscreen/Mechanism.kt` |
| template-match finder with ScreenCaptureKit and Accelerate | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Eye.swift` |
| mapsforge to PNG tile rendering | [Mantra Map Server (MANTRA_MAP_SERVER)](apps/MANTRA_MAP_SERVER.md) | `app/src/main/java/com/mantra/mapserver/Renderer.kt` |
| headless MilkDrop visual render for streaming | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `linux/mrvisuals.py` |
| NDI output of the visuals | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `mac/app/Ndi.swift` |
| VideoToolbox H.264/H.265 decoder finding parameter sets by NAL type | [Virtual Cam (Mantra) (mantra_virtual_cam)](apps/mantra_virtual_cam.md) (private) | `Sources/Decoder.swift` |
| feeds frames into OBS Virtual Camera's sink without OBS running | [Virtual Cam (Mantra) (mantra_virtual_cam)](apps/mantra_virtual_cam.md) (private) | `Sources/VirtualCamera.swift` |
| Resolve utility script that repacks and imports into a bin by time code | [MKV Converter (MPA) (MKV_CONVERTER)](apps/MKV_CONVERTER.md) (private) | `resolve/MPA Import.py` |
| module map and shim header exposing the NDI C API to Swift | [NDI Mantra Monitor (ndi-mantra-monitor)](apps/ndi-mantra-monitor.md) (private) | `CNDI/` |
| Swift wrapper around the NDI C library for finding and receiving sources | [NDI Mantra Monitor (ndi-mantra-monitor)](apps/ndi-mantra-monitor.md) (private) | `Sources/NDI.swift` |
| Resolve hotkey helper | [Oxi Controller (E16 Remote) (oxi-controller)](apps/oxi-controller.md) | `tools/resolve_keys.py` |
| script that turns raw images into the book plates | [The Patient Ground (PERMACULTURE_FIELD_BOOK)](apps/PERMACULTURE_FIELD_BOOK.md) | `make_plates.py` |
| Resolve scripting helper with a line protocol: open, pages, quit | [Resolve Pages (Mantra) (RESOLVE_PAGES)](apps/RESOLVE_PAGES.md) (private) | `helper/pages_helper.py` |
| Admin LIVE tab: start/stop a VDO.Ninja stream with Drive recording | [Santoshi Kirtan Band sites (santoshi_band_site)](apps/santoshi_band_site.md) | `admin/live.js` |
| builds the book plates from the images | [Being a Self Publisher (SELF_PUBLISHER)](apps/SELF_PUBLISHER.md) | `make_plates.py` |
| Network.framework HTTP plus SSE server for a Swift app | [Session Hub (SESSION_HUB)](apps/SESSION_HUB.md) | `app/Server.swift` |
| whole library and CLI: landmarks, chroma, align; needs numpy scipy ffmpeg | [Shazam Local (SHAZAM_LOCAL)](apps/SHAZAM_LOCAL.md) (private) | `shazam_local.py` |
| camera calibration: board detection, bundle adjustment, triangulation, linear algebra | [Skeleton (Mantra) (SKELETON)](apps/SKELETON.md) | `app/Calib/` |
| capture plus Vision body pose | [Skeleton (Mantra) (SKELETON)](apps/SKELETON.md) | `app/Camera.swift` |
| discovers and starts adb phones as cameras, clock sync with NTP-style exchange | [Skeleton (Mantra) (SKELETON)](apps/SKELETON.md) | `app/PhoneSource.swift` |
| renders yoga pose mannequins | [Skeleton (Mantra) (SKELETON)](apps/SKELETON.md) | `blender/yoga_poses.py` |
| Sony Bluetooth LE remote commander: REC on all and recording reports | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](apps/sony_remote_controller.md) | `app/src/main/java/com/mantraproductions/sonyremote/BleRemote.kt` |
| SMPTE LTC generator at 25 fps | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](apps/sony_remote_controller.md) | `app/src/main/java/com/mantraproductions/sonyremote/Ltc.kt` |
| Camera2 plus ML Kit OCR that reads a time code off a camera screen | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](apps/sony_remote_controller.md) | `app/src/main/java/com/mantraproductions/sonyremote/ScreenReader.kt` |
| Probe of Sony A7 V PTP/IP live view and properties from the Mac | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](apps/sony_remote_controller.md) | `tools/a7v_probe.py` |
| PTP-IP client (init, sessions, operations) written from the protocol description | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](apps/SONY_REMOTE_MAC.md) | `app/PtpIp.swift` |
| build and merge a cue sheet from frame JSON, preserving manual columns | [Sound Design (SOUND_DESIGN)](apps/SOUND_DESIGN.md) (private) | `tools/spotting.py` |
| libndi through ctypes: find NDI sources and receive frames | [Sound Link (Mantra) (SOUND_LINK)](apps/SOUND_LINK.md) | `studio/ndi.py` |
| IOKit HID driver for the original Stream Deck: key images, presses, brightness | [Stream Deck Control (Mantra) (stream-deck-control) (retired, use STREAM_DECK_REMOTE)](apps/stream-deck-control.md) (private) | `app/Deck.swift` |
| stdlib HTTP service with history and token-guarded actions | [Streaming Dashboard (Mantra) (STREAMING_DASHBOARD)](apps/STREAMING_DASHBOARD.md) | `vm/streaming_dashboard_vm.py` |
| reads a retail product page for title, availability, badge and main image | [Studio Setup (Mantra) (studio-setup-mantra)](apps/studio-setup-mantra.md) (private) | `tools/amazon_item.py` |
| Crash-safe H.264/AAC MKV recording with ffmpeg packet-copy mux | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `app/Recorder.swift` |
| Sony PTP/IP and USB PTP property read/write | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `app/SonyPtp.swift` |

## Bluetooth, USB and devices (16)

| What it does | Repo | Path |
|---|---|---|
| Termux to ADB wireless-debugging bridge for force-stop and kill-all | [Cockpit Termux (COCKPIT_TERMUX)](apps/COCKPIT_TERMUX.md) | `bridge.py` |
| Lists USB-attached Android phones over adb and pushes a helper binary | [Connection Keeper (connection-keeper)](apps/connection-keeper.md) | `Sources/Shared/Phones.swift` |
| parser for djay's YapDatabase playlist storage (TSAF) and adb file push with resume | [djay Sync, command line (djay-sync) (djay-playlists)](apps/djay-playlists.md) (private) | `djay_sync.py` |
| Logitech HID++ per-key lighting | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `src/hidpp.swift` |
| cookie refresh by driving Firefox's Export Cookies extension over adb taps | [gi (Instagram downloader) (gi)](apps/gi.md) (private) | `gi.py` |
| ICMP sweep, NetBIOS and SSDP device discovery | [LAN Scanner (Mantra) (LAN_SCANNER)](apps/LAN_SCANNER.md) | `app/Discover.swift` |
| keeps USB and wireless debugging enabled | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `android/app/src/main/java/com/mantra/remote/DebugKeeper.kt` |
| adb over Wi-Fi client inside the app | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `android/app/src/main/java/com/mantra/remote/adb/AdbLink.kt` |
| turn the visual into G815 key colours with bilinear sampling | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `mac/app/Lights.swift` |
| routing ladder with probes: policy, MediaRouter2, communication device | [Mantra Route (MANTRA_ROUTE)](apps/MANTRA_ROUTE.md) | `app/src/main/java/com/mantra/route/Router.kt` |
| adb wrapper: headless AVD lifecycle, input, uiautomator dump, macro runner | [Mantra Sandbox (MANTRA_SANDBOX)](apps/MANTRA_SANDBOX.md) | `bin/sandbox` |
| Mantra Link client with adb forward per phone | [Virtual Cam (Mantra) (mantra_virtual_cam)](apps/mantra_virtual_cam.md) (private) | `Sources/Link.swift` |
| wraps getUserMedia to swap the mic for a named device | [Plugin Assistant (PLUGIN_ASSISTANT)](apps/PLUGIN_ASSISTANT.md) | `extension/inject.js` |
| collects relay, viewer, machine and device metrics into a snapshot | [Streaming Dashboard (Mantra) (STREAMING_DASHBOARD)](apps/STREAMING_DASHBOARD.md) | `app/collector.py` |
| adb-based remote client for the keyboard | [TTT Voice Type keyboard (TTT)](apps/TTT.md) | `tools/ttt_remote.py` |
| toggles USB tethering via shell through Shizuku | [USB Tethering (Mantra) (USB_TETHERING)](apps/USB_TETHERING.md) | `android/app/src/main/java/community/auroville/usbtether/Tether.kt` |

## Android and Termux (18)

| What it does | Repo | Path |
|---|---|---|
| bash driver: Java 17 selection, emulator boot wait, build, sign, keep APK, tap-text via view tree | [Android Lab (android-lab)](apps/android-lab.md) (private) | `droid` |
| find a UI node by text in the Android view tree | [Android Lab (android-lab)](apps/android-lab.md) (private) | `find_node.py` |
| parcel, style, cache, mark file, owner book and outline logic ported from Kotlin | [ARKOD Layer (web) (arkod_web)](apps/arkod_web.md) | `public/js/core/` |
| calendar connector interface with Android provider and Google implementations | [Calendar Events (calendar_events)](apps/calendar_events.md) (private) | `calendar_events/connectors/` |
| LUFS, LRA and 31-band analysis of a reference track and matching to EQ | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](apps/CQ_MIXPAD_MANTRA.md) | `android/app/src/main/java/com/mantra/cqmixpad/reference/Analyzer.kt` |
| Astrology calculation engine compiled from the Android app code (planets, houses, aspects) | [Donnie Horoscope (donnie-horoscope-releases)](apps/donnie-horoscope-releases.md) | `app/donnie.js` |
| Catches the TIDAL login redirect on a phone and copies the token to the clipboard | [Generated Playlists (generated_playlists)](apps/generated_playlists.md) | `tools/tidal_token_termux.py` |
| clean_text and split_units ported from Python, tested against it | [MA Reader for Android (MA_READER_ANDROID)](apps/MA_READER_ANDROID.md) | `app/src/main/kotlin/dev/mantraproductions/reader/text/MaText.kt` |
| word timing alignment | [MA Reader Engine (MA_READER_ENGINE)](apps/MA_READER_ENGINE.md) | `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaAlign.kt` |
| text cleaning and sentence splitting | [MA Reader Engine (MA_READER_ENGINE)](apps/MA_READER_ENGINE.md) | `engine/src/main/kotlin/dev/mantraproductions/reader/engine/MaText.kt` |
| pure Kotlin RFB 3.8 VNC server with ZRLE and Raw tiles | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `android/app/src/main/java/com/mantra/remote/VncServer.kt` |
| MilkDrop visualizer in the browser (vendored) | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `android/app/src/main/assets/web/vendor/butterchurn.min.js` |
| drive Tailscale for Android with CONNECT_VPN and USE_EXIT_NODE intents | [VPN (Mantra) (MANTRA_VPN)](apps/MANTRA_VPN.md) | `android/app/src/main/java/com/mantraproductions/vpn/TailscaleCtl.kt` |
| client of the Second Take HTTP protocol with first-come-first-served id | [Second Take Remote (SECOND_TAKE_REMOTE)](apps/SECOND_TAKE_REMOTE.md) | `android/app/src/main/java/community/auroville/secondtake/remote/Protocol.kt` |
| watches the USB_STATE broadcast | [USB Tethering (Mantra) (USB_TETHERING)](apps/USB_TETHERING.md) | `android/app/src/main/java/community/auroville/usbtether/UsbWatch.kt` |
| same pause/continue logic for Android | [Voice Engine Universal (Mantra) (VOICE_ENGINE_UNIVERSAL)](apps/VOICE_ENGINE_UNIVERSAL.md) | `kotlin/PauseSync.kt` |
| words, pieces and clock for a reading | [Voice Engine Universal (Mantra) (VOICE_ENGINE_UNIVERSAL)](apps/VOICE_ENGINE_UNIVERSAL.md) | `kotlin/Reading.kt` |
| Host, Origin/Referer and X-ZET header guard for a localhost Flask server (copied from KEYRING_TERMUX) | [ZET Strike (zet_strike)](apps/zet_strike.md) | `app/localguard.py` |

## Mac automation and accessibility (74)

| What it does | Repo | Path |
|---|---|---|
| interruptible sleep (AbSleep) and coordinate mapping (MapPoint) for macros | [Avid Assistant (AVID_ASSISTANT)](apps/AVID_ASSISTANT.md) (private) | `scripts/A1_ASSISTANT/A1_ASSISTANT_v100_classic.ahk` |
| clipboard bucket queue with a menu | [Brain Brake Keyboard (Hammerspoon) (BRAIN_BRAKE_KEYBOARD) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md) | `paste_queue.lua` |
| the four-tests runner pattern for Hammerspoon modules | [Brain Brake Keyboard (Hammerspoon) (BRAIN_BRAKE_KEYBOARD) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md) | `tests/run_tests.sh` |
| Accessibility bridge to read and move other apps' windows | [Cascade (Cascade)](apps/Cascade.md) | `Sources/Cascade/AXBridge.swift` |
| cascade layout maths per display | [Cascade (Cascade)](apps/Cascade.md) | `Sources/Cascade/CascadeLayout.swift` |
| record and restore window geometry and order | [Cascade (Cascade)](apps/Cascade.md) | `Sources/Cascade/Snapshots.swift` |
| green/amber/grey menu-bar band | [Claude Control (Mantra) (CLAUDE_CONTROL)](apps/CLAUDE_CONTROL.md) | `app/StatusBand.swift` |
| enumerate and toggle launchd and login items with memory of user choices | [Clean Start (Mantra) (CLEAN_START)](apps/CLEAN_START.md) | `app/Engine.swift` |
| accessibility helper for window tests | [Clean Start (Mantra) (CLEAN_START)](apps/CLEAN_START.md) | `tools/ax.py` |
| Keeps Tailscale up as a guard daemon | [Connection Keeper (connection-keeper)](apps/connection-keeper.md) | `Sources/Daemon/TailscaleGuard.swift` |
| per-interface internet probing with bound ping and curl fallback | [Connection Controller Dashboard Viewer (Mantra) (CONNECTION_CONTROLLER_DASHBOARD_VIEWER)](apps/CONNECTION_CONTROLLER_DASHBOARD_VIEWER.md) (private) | `app/Network.swift` |
| MediaInfo columns for media files | [Download, Copy and Move (Mantra) (was Download Monitor) (DOWNLOAD_MONITOR)](apps/DOWNLOAD_MONITOR.md) | `app/MediaInfo.swift` |
| build the fn swap map from the Mac's key table | [FKeys (FKeys)](apps/FKeys.md) | `Sources/FKeys/FnKeyMap.swift` |
| apply and clear hidutil key remapping | [FKeys (FKeys)](apps/FKeys.md) | `Sources/FKeys/Hidutil.swift` |
| registered global hotkey without Input Monitoring | [FKeys (FKeys)](apps/FKeys.md) | `Sources/FKeys/HotKey.swift` |
| headless engine CLI shared by the Mac and Windows apps, JSON progress on stdout | [Free Voice Convert (Equalizer) (FREE_VOICE_CONVERT)](apps/FREE_VOICE_CONVERT.md) | `engine/fvc.py` |
| HTTP and TCP light API, ten shows, picture-to-keys mapping, yield-to-typing | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `app/LightShow.swift` |
| Swift client for the light API | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `src/lightclient.swift` |
| command-line reader of the macOS Accessibility tree that outputs JSON | [Queen, Mac app (Groq AI Studio (Mantra)) (GROQ_AI_STUDIO_MAC)](apps/GROQ_AI_STUDIO_MAC.md) (private) | `axread/main.swift` |
| macro recorder core with marker-bounded file writing | [Hammerspoon Lua Recorder (HAMMERSPOON_LUA_RECORDER)](apps/HAMMERSPOON_LUA_RECORDER.md) | `marco_recorder.lua` |
| guard that the window has one title only | [Hemi-Sync Recording Monitor (Mantra) (HEMISYNC_RECORDING_MONITOR)](apps/HEMISYNC_RECORDING_MONITOR.md) | `check_one_title.sh` |
| key parser by shape and classifier of HTTP results with mask() output | [KeyringTester (Mantra) (KEY_RING_TESTER)](apps/KEY_RING_TESTER.md) (private) | `app/Engine.swift` |
| borderless non-activating HUD-glass floating panel | [Keyboard Monitor (Mantra) (keyboard-monitor)](apps/keyboard-monitor.md) (private) | `app/Blob.swift` |
| listen-only CGEventTap decoding keys, modifiers left/right and media keys | [Keyboard Monitor (Mantra) (keyboard-monitor)](apps/keyboard-monitor.md) (private) | `app/Keys.swift` |
| MAC address to maker lookup from the IEEE table | [LAN Scanner (Mantra) (LAN_SCANNER)](apps/LAN_SCANNER.md) | `app/Oui.swift` |
| read Dock persistent apps and icons | [Dock Switcher (Mantra) (MACOS_TASK_SWITCHER)](apps/MACOS_TASK_SWITCHER.md) | `app/Dock.swift` |
| Carbon hot key and double-Ctrl event tap | [Dock Switcher (Mantra) (MACOS_TASK_SWITCHER)](apps/MACOS_TASK_SWITCHER.md) | `app/Keys.swift` |
| small HTTP listener for phone control; AXPress of front app menu | [Dock Switcher (Mantra) (MACOS_TASK_SWITCHER)](apps/MACOS_TASK_SWITCHER.md) | `app/Remote.swift` |
| the has/run/add/sync command over action cards | [Macro Skills (MACRO_SKILLS)](apps/MACRO_SKILLS.md) (private) | `macro_skills.py` |
| Borderless transparent floating ring panel with click-through hole | [Magic Coin (magic-coin)](apps/magic-coin.md) | `Sources/MagicCoin/CoinView.swift` |
| shared Swift UI parts for control windows | [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control) (MANTRA_CONTROLS)](apps/MANTRA_CONTROLS.md) | `Sources/Common/Parts.swift` |
| HTTP client helpers for a state/do JSON engine | [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control) (MANTRA_CONTROLS)](apps/MANTRA_CONTROLS.md) | `Sources/Common/Server.swift` |
| accessibility tree read/press | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/AX.swift` |
| input guard with owner queue and focus restore | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Guard.swift` |
| window layouts (from Rectangle, see THIRD_PARTY) | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Layouts.swift` |
| input lock with event tap | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Lock.swift` |
| screen OCR | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Ocr.swift` |
| PauseGate for pause/resume of all work | [Macro Recorder (Mantra) (MANTRA_MACRO)](apps/MANTRA_MACRO.md) | `app/Pause.swift` |
| Accessibility and Input Monitoring permission handling | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) | `app/Permissions.swift` |
| picks the default button of a dialog from the accessibility tree, with tests | [Automated Mouse Actions (Mantra) (MANTRA_MOUSE)](apps/MANTRA_MOUSE.md) (private) | `default_button.lua` |
| per-phone recorder with pause and next-clip | [Screen Copy (Mantra) (MANTRA_SCREEN_COPY)](apps/MANTRA_SCREEN_COPY.md) | `app/Recorder.swift` |
| start servers from Hammerspoon without hs.execute | [Star (Mantra), Lua (Hammerspoon, legacy) (MANTRA_STAR)](apps/MANTRA_STAR.md) (private) | `spawn.lua` |
| teacher engine shared by both apps | [Ableton Teacher and DaVinci Teacher apps (Mantra) (MANTRA_TEACHERS)](apps/MANTRA_TEACHERS.md) | `app/Teacher.swift` |
| key ring and retry logic | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](apps/MANTRA_VOICE_TO_TEXT.md) | `mac/Sources/Chain.swift` |
| find exit node and set/clear it via the Tailscale CLI | [VPN (Mantra) (MANTRA_VPN)](apps/MANTRA_VPN.md) | `mac/Sources/Tailscale.swift` |
| self-writing macro recorder with teaching status line | [Marco Macro Recorder (Windows) (MARCO_MACRO_RECORDER)](apps/MARCO_MACRO_RECORDER.md) | `13-Marco_Macro_Recorder_AHK_v13.ahk` |
| read Chrome profiles from Local State and open missing profile windows | [Opening and Closing (Mantra) (OPENING_AND_CLOSING)](apps/OPENING_AND_CLOSING.md) (private) | `app/Chrome.swift` |
| global hotkey registration for a menu bar Mac app | [Pasty (Pasty)](apps/Pasty.md) | `Sources/Pasty/Hotkey/HotKeyCenter.swift` |
| clipboard change watcher | [Pasty (Pasty)](apps/Pasty.md) | `Sources/Pasty/Monitor/ClipboardMonitor.swift` |
| pastes a clip into the previous app | [Pasty (Pasty)](apps/Pasty.md) | `Sources/Pasty/Monitor/PasteService.swift` |
| Global hotkey registration and recorder | [Pesty fork (archive) (pesty-fork-archive) (retired, use Pasty)](apps/pesty-fork-archive.md) | `Sources/Pesty/Hotkey/HotKeyCenter.swift` |
| Polls the macOS pasteboard and stores clips by type | [Pesty fork (archive) (pesty-fork-archive) (retired, use Pasty)](apps/pesty-fork-archive.md) | `Sources/Pesty/Monitor/ClipboardMonitor.swift` |
| data-driven diagram drawing with lit parts | [DaVinci Grading Tutorial (Mantra) (RESOLVE_GRADING_TUTORIAL)](apps/RESOLVE_GRADING_TUTORIAL.md) (private) | `app/DiagramView.swift` |
| shared menu-bar hover card kit file | [Resolve Pages (Mantra) (RESOLVE_PAGES)](apps/RESOLVE_PAGES.md) (private) | `app/HoverCard.swift` |
| Hover card UI for a menu-bar item | [Router Mode (Mantra) (router-mode)](apps/router-mode.md) | `app/HoverCard.swift` |
| Vision OCR for ranked lists with noise filters | [Screenshot to TIDAL (Mantra) (SCREENSHOT_TO_TIDAL)](apps/SCREENSHOT_TO_TIDAL.md) (private) | `app/OCR.swift` |
| read djay playlists and tags, match and sync | [Screenshot to TIDAL (Mantra) (SCREENSHOT_TO_TIDAL)](apps/SCREENSHOT_TO_TIDAL.md) (private) | `app/PlaylistSync.swift` |
| TIDAL PKCE login, search, scoring, playlists | [Screenshot to TIDAL (Mantra) (SCREENSHOT_TO_TIDAL)](apps/SCREENSHOT_TO_TIDAL.md) (private) | `app/Tidal.swift` |
| click and step finder: 1 ms high-passed energy against a 40 ms median | [Spectral Analyzer (Mantra) (SPECTRAL_ANALYZER)](apps/SPECTRAL_ANALYZER.md) (private) | `app/Detect.swift` |
| Carbon hot key registration with no permission | [Launcher (Mantra) (STAR_LAUNCHER)](apps/STAR_LAUNCHER.md) (private) | `Sources/Hotkey.swift` |
| orders third-party menu bar items into fixed places | [Star (Mantra), Swift menu (STAR_SWIFT)](apps/STAR_SWIFT.md) | `app/MenuBar.swift` |
| launchd login item | [Star (Mantra), Swift menu (STAR_SWIFT)](apps/STAR_SWIFT.md) | `launchd/com.mantra.star.plist` |
| step sequence for stem separation inside Live | [Stem Separation (Mantra) (STEM_SEPARATION)](apps/STEM_SEPARATION.md) (private) | `app/Separator.swift` |
| joins the MPA classroom websocket as a hidden teacher remote | [Stream Deck Remote (STREAM_DECK_REMOTE)](apps/STREAM_DECK_REMOTE.md) | `mac/app/Classroom.swift` |
| iTerm2 AppleScript: list sessions, write text without newline then Return | [Talk Mode (Mantra) (TALK_MODE)](apps/TALK_MODE.md) | `app/ITerm.swift` |
| click-through red border overlay on all screens | [Talk Mode (Mantra) (TALK_MODE)](apps/TALK_MODE.md) | `app/RedEdge.swift` |
| shared menu-bar hover card kit file | [UHD HD Display (Mantra) (UHD_HD_DISPLAY)](apps/UHD_HD_DISPLAY.md) (private) | `app/HoverCard.swift` |
| Dock/tray and window helper for the VM desktop | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `desktop/chromium-vm-dock.py` |
| Swift RFB viewer and built-in VNC server with Apple login (ARD) and ZRLE (per TAKEOVER) | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `viewer/` |
| menu bar replay player for the last spoken message | [Voice Engine (Mantra) (VOICE_ENGINE)](apps/VOICE_ENGINE.md) | `app/Replay.swift` |
| reply helper binary | [Voice Engine (Mantra) (VOICE_ENGINE)](apps/VOICE_ENGINE.md) | `reply/main.swift` |
| Two-channel dB VU meter view | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `app/Meter.swift` |
| WebDriver BiDi client over WebSocket to Firefox | [Percussion School (Mantra) (YSHAI_PERCUSSION_SCHOOL)](apps/YSHAI_PERCUSSION_SCHOOL.md) (private) | `app/Bidi.swift` |
| catalogue compare and download pipeline | [Percussion School (Mantra) (YSHAI_PERCUSSION_SCHOOL)](apps/YSHAI_PERCUSSION_SCHOOL.md) (private) | `app/Pipeline.swift` |

## Networking, sync and remote machines (28)

| What it does | Repo | Path |
|---|---|---|
| Go relay that bonds several TCP/UDP legs with reordering and resend | [Connection Keeper (connection-keeper)](apps/connection-keeper.md) | `Sources/Bond/server` |
| CLI to register and report any download | [Download, Copy and Move (Mantra) (was Download Monitor) (DOWNLOAD_MONITOR)](apps/DOWNLOAD_MONITOR.md) | `dlmon.py` |
| Drive folder walk and ranged resumable download with MD5 check | [Drive Downloader (DRIVE_DOWNLOADER)](apps/DRIVE_DOWNLOADER.md) | `drive.py` |
| minimal WebDriver BiDi client: session, script.evaluate, cookie-based download | [Firefox Control (firefox-control)](apps/firefox-control.md) (private) | `firefoxctl` |
| single-file FTP plus HTTP queue server with DNS/mDNS name service and folder-tree client | [FTP Server v4 (ftp-server-termux-and-terminal)](apps/ftp-server-termux-and-terminal.md) (private) | `src/ftp_server.py` |
| segmented byte-range download with resume | [GDrive Downloader (Flask, macOS) (GDRIVE_DOWNLOADER_FLASK_MACOS)](apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (private) | `segmented.py` |
| fetch with timeout, backoff, block detection | [Lenovo Hunter (LENOVO_HUNTER)](apps/LENOVO_HUNTER.md) | `src/core/http.js` |
| standard terminal screen for Flask servers | [MA Reader Speechify module (MA_READER_SPEECHIFY)](apps/MA_READER_SPEECHIFY.md) (private) | `server_screen.py` |
| extension poll/result bridge to a local server | [Mantra Chrome Extensions (MANTRA_CHROME_EXTENSIONS)](apps/MANTRA_CHROME_EXTENSIONS.md) | `bench/L6-command-bridge-to-a-local-server/background.js` |
| resumable region download | [Mantra Map Server (MANTRA_MAP_SERVER)](apps/MANTRA_MAP_SERVER.md) | `app/src/main/java/com/mantra/mapserver/Download.kt` |
| per-caller tile counters | [Mantra Map Server (MANTRA_MAP_SERVER)](apps/MANTRA_MAP_SERVER.md) | `app/src/main/java/com/mantra/mapserver/Usage.kt` |
| embedded BRouter routing engine (see LICENSE-BROUTER) | [Mantra Trail (MANTRA_TRAIL)](apps/MANTRA_TRAIL.md) | `app/src/main/java/btools/` |
| tile fetching over HTTP | [Mantra Trail (MANTRA_TRAIL)](apps/MANTRA_TRAIL.md) | `app/src/main/java/com/mantra/trail/TileHttp.kt` |
| Cloudflare Pages deploy with token from environment or local file | [Marko Bosko Therapies (MARKOBOSKO_THERAPIES)](apps/MARKOBOSKO_THERAPIES.md) | `deploy.sh` |
| WebView driver that logs in to the TP-Link router and sends/reads SMS | [Router Credits (Android) (router-credits)](apps/router-credits.md) | `app/src/main/java/com/mantra/routercredits/Driver.kt` |
| Parser for the operator's balance reply (with unit test) | [Router Credits (Android) (router-credits)](apps/router-credits.md) | `app/src/main/java/com/mantra/routercredits/Reply.kt` |
| TP-Link MR router client: RSA/AES login, read WAN/LTE status, switch mode | [Router Mode (Mantra) (router-mode)](apps/router-mode.md) | `routermode.py` |
| headless Firefox BiDi driver that logs into a router page and operates its SMS and Wi-Fi menus | [Router SMS (router-sms)](apps/router-sms.md) (private) | `router-sms` |
| Durable Object WebSocket room for chat and viewer count with rate limits | [Santoshi Kirtan Band sites (santoshi_band_site)](apps/santoshi_band_site.md) | `room/worker.js (per TAKEOVER)` |
| stdlib HTTP mailbox with sqlite and long-poll wait | [Session Ack (ccmsg) (SESSION_ACK)](apps/SESSION_ACK.md) | `server/session_ack_server.py` |
| systemd unit for the mailbox | [Session Ack (ccmsg) (SESSION_ACK)](apps/SESSION_ACK.md) | `server/systemd/session-ack.service` |
| stdlib Python client for the hub (works through a SOCKS5 proxy for cloud sessions) | [Session Hub (SESSION_HUB)](apps/SESSION_HUB.md) | `cli/hub` |
| stdlib server for a static page with proxying of paid map APIs so keys stay server-side | [Store & Pool Finder (SHOP_FINDER)](apps/SHOP_FINDER.md) | `serve.py` |
| Tile HTTP loading for the map | [Spar Locator / DM Finder (spar_locator)](apps/spar_locator.md) | `app/src/main/java/com/mantra/spar/TileHttp.kt` |
| Flask server wrapping mdimport, mdfind and Quick Look thumbnails | [Find a File Spotlight (Mantra) (spotlight) (retired, use FIND_FILE)](apps/spotlight.md) (private) | `spotlightd.py` |
| syncs learned corrections with a shared repo | [TTT Voice Type keyboard (TTT)](apps/TTT.md) | `nlp/MaCorrectionsSync.kt` |
| export allowed browser-profile cookies to the server on a schedule | [YT Transcriber (YT_TRANSCRIBER)](apps/YT_TRANSCRIBER.md) (private) | `cookie_sync.py` |
| Map tile proxy for OSM, Esri and Google sessions | [ZET Strike (zet_strike)](apps/zet_strike.md) | `app/tiles.py` |

## UI kits, pages and design (30)

| What it does | Repo | Path |
|---|---|---|
| fly-through scanning of the map for parcels | [ARKOD Layer (web) (arkod_web)](apps/arkod_web.md) | `public/js/scan.js` |
| FlorisBoard theme JSON stylesheets that can be copied as a template for another colour theme | [Auroville FlorisBoard Theme (auroville-florisboard-theme)](apps/auroville-florisboard-theme.md) | `stylesheets/` |
| doorbell pattern: poll one tiny JSON over raw URL, one writer per file, SSE page refresh | [Brain Brake review wall (BRAIN_BRAKE_REVIEW)](apps/BRAIN_BRAKE_REVIEW.md) | `review_wall.py` |
| encrypt two Markdown manuscripts into one static page decrypted in the browser with a passphrase | [Cause and Symptom (Uzrok i simptom) (CAUSE_AND_SYMPTOM)](apps/CAUSE_AND_SYMPTOM.md) | `build_site.py` |
| page ring and back-one-page logic shared with the star | [DaVinci Resolve Assistant (DAVINCI_RESOLVE_ASSISTANT) (retired, use DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ASSISTANT.md) | `star/pages_helper.py` |
| Small browser zip reader/writer for chart packs | [Donnie Horoscope (donnie-horoscope-releases)](apps/donnie-horoscope-releases.md) | `app/zip.js` |
| 115 key positions on a 24 x 7.5 key-unit board | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `layout.json` |
| finds translatable text nodes and puts translations back while watching for page changes | [German to English (Mantra) (GERMAN_TO_ENGLISH)](apps/GERMAN_TO_ENGLISH.md) (private) | `extension/content.js` |
| guard so only the local page can POST | [GVoices (Google Voices) (GoogleVoices)](apps/GoogleVoices.md) | `localguard.py` |
| generate climate zone map data | [Kukljica EcoOasis (KUKLJICA_ECOOASIS)](apps/KUKLJICA_ECOOASIS.md) | `tools/build_kg.py` |
| Three crops chooser: crop table plus Koppen-Geiger climate map in plain JS | [Kukljica EcoOasis (KUKLJICA_ECOOASIS)](apps/KUKLJICA_ECOOASIS.md) | `tri/` |
| product page parsing: JSON-LD, meta, selectors, regex | [Lenovo Hunter (LENOVO_HUNTER)](apps/LENOVO_HUNTER.md) | `src/core/parse.js` |
| drops one-word commands to a running player | [MA Player (ma-player)](apps/ma-player.md) (private) | `bin/maplay-cmd` |
| Loads keys in any layout from a plain text file and stores them in a cookie | [Maha Transcriber and Reader (web) (maha-transcriber-reader)](apps/maha-transcriber-reader.md) | `keys.js` |
| cassette-style frontend component | [Maha Transcribe / TTT-LLL (Streamlit) (MAHA_TRANSCRIBE_STREAMLIT)](apps/MAHA_TRANSCRIBE_STREAMLIT.md) | `cassette_frontend/index.html` |
| Tile cache for cadastre and map layers | [Mantra ARKOD (mantra_arkod)](apps/mantra_arkod.md) | `app/src/main/java/com/mantra/arkod/CacheTiles.kt` |
| read Drive breadcrumbs (including hidden 'Show path' menu items) and travel to a folder | [Drive Full Path (Mantra Productions) (MANTRA_DRIVE_PATH)](apps/MANTRA_DRIVE_PATH.md) | `extension/content.js` |
| urllib-only client CLI | [Screen Copy (Mantra) (MANTRA_SCREEN_COPY)](apps/MANTRA_SCREEN_COPY.md) | `python/screencopy.py` |
| read GitHub account, build catalog.json and per-app pages | [Marko Apps site (markoapps.pages.dev) (MARKO_APPS)](apps/MARKO_APPS.md) | `build.py` |
| generates a controller layout from measured positions | [Controller Mapper (Mantra) (mix-ultra-mapper)](apps/mix-ultra-mapper.md) (private) | `tools/make_mix_ultra_layout.py` |
| Design notes for the vMix-style OBS user interface | [obs2vmix (obs2vmix)](apps/obs2vmix.md) | `docs/obs2vmix-ui.md` |
| CMake feature switch that builds the vMix-style UI inside OBS | [obs2vmix (obs2vmix)](apps/obs2vmix.md) | `frontend/cmake/feature-obs2vmix.cmake` |
| four-test runner (mechanism, UI, ugly, upgrade) | [Store & Pool Finder (SHOP_FINDER)](apps/SHOP_FINDER.md) | `tests/run_all.py` |
| builds the single-page book from content_*.py | [Six Levels of Claude (SIX_LEVELS_OF_CLAUDE)](apps/SIX_LEVELS_OF_CLAUDE.md) | `build.py` |
| VTM map with store markers and a location dot | [Spar Locator / DM Finder (spar_locator)](apps/spar_locator.md) | `app/src/main/java/com/mantra/spar/SparMap.kt` |
| generates the static gear page from a product list | [Studio Setup (Mantra) (studio-setup-mantra)](apps/studio-setup-mantra.md) (private) | `site/build.py` |
| tag-filtered style menu | [Suno Songs prompt database (SUNO_SONGS)](apps/SUNO_SONGS.md) (private) | `scripts/menu.py` |
| Four-stage test harness (mechanism, UI, ugly cases, upgrade) | [Termux Tools (termux-tools)](apps/termux-tools.md) | `tests/run_all.py` |
| edge session check with HMAC and routing | [TTT Portal (TTT_PORTAL)](apps/TTT_PORTAL.md) (private) | `pages/functions/_middleware.js` |
| accounts with salted scrypt, signed session tokens, admin panel and API keys | [TTT Portal (TTT_PORTAL)](apps/TTT_PORTAL.md) (private) | `portal.py` |

## Files, data and text (18)

| What it does | Repo | Path |
|---|---|---|
| parser for the 20-byte TinyTask .rec record format and AHK v2 generator | [TinyTask to AutoHotkey (autohotkey)](apps/autohotkey.md) (private) | `app.py` |
| status line script that writes per-session usage JSON to a cache folder | [Claude Remote (Mantra) (CLAUDE_REMOTE)](apps/CLAUDE_REMOTE.md) (private) | `statusline-usage.py` |
| SQLite job and file ledger | [Drive Downloader (DRIVE_DOWNLOADER)](apps/DRIVE_DOWNLOADER.md) | `store.py` |
| TIDAL OAuth PKCE login and playlist creation from a text list | [Generated Playlists (generated_playlists)](apps/generated_playlists.md) | `tools/tidal_playlist.py` |
| provider and Google API test table: key shapes, hints and the cheapest test call per provider | [KeyringTester (Mantra) (KEY_RING_TESTER)](apps/KEY_RING_TESTER.md) (private) | `shared/endpoints.json` |
| copy of the shared provider test table | [Key Tester (Android) (Key_Tester)](apps/Key_Tester.md) (private) | `app/src/main/assets/endpoints.json` |
| shared-login cookie check copied from the portal | [Maha Transcribe Flask (MAHA_TRANSCRIBE_FLASK)](apps/MAHA_TRANSCRIBE_FLASK.md) (private) | `ttt_auth.py` |
| MV3 consistency linter: manifest vs files, chrome.* API declarations, fetch host permissions, JS parse | [Mantra Chrome Extensions (MANTRA_CHROME_EXTENSIONS)](apps/MANTRA_CHROME_EXTENSIONS.md) | `tools/extcheck.py` |
| machine-readable list of public apps with README text | [Marko Apps site (markoapps.pages.dev) (MARKO_APPS)](apps/MARKO_APPS.md) | `catalog.json` |
| stopwatch and timer state logic | [Minimalist Stopwatch (MINIMALIST_STOPWATCH)](apps/MINIMALIST_STOPWATCH.md) | `app/src/main/java/com/mantra/stopwatch/Stopwatch.kt` |
| generates phrasing rhythm data for exercises.json | [MPA Academy, Android app (MPA_ACADEMY_ANDROID)](apps/MPA_ACADEMY_ANDROID.md) | `tools/phrasing-rhythms.mjs` |
| Parses store lists and computes open-now with holidays and extra days | [Spar Locator / DM Finder (spar_locator)](apps/spar_locator.md) | `app/src/main/java/com/mantra/spar/Stores.kt` |
| 28 drives with rated and measured numbers and review links | [Mantra Speed Test (SPEED_TEST)](apps/SPEED_TEST.md) (private) | `reference.json` |
| clone-less file fetch, diff and single-commit push through the GitHub API | [Surgeon (surgeon)](apps/surgeon.md) (private) | `surgeon` |
| merges keys into a TOML secrets file | [TOML key merger (TOML)](apps/TOML.md) | `merge.py` |
| parses several exported key-file formats | [TOML key merger (TOML)](apps/TOML.md) | `parsers.py` |
| registry of engines with Hugging Face repos and measured speeds | [Voice Engines (model hub) (VOICE_ENGINES)](apps/VOICE_ENGINES.md) (private) | `engines.json` |
| Key file parser for API keys | [ZET Strike (zet_strike)](apps/zet_strike.md) | `app/keyparse.py` |

## Other (63)

| What it does | Repo | Path |
|---|---|---|
| API key ring with probing, verdicts, dead-key fingerprints and engine fallback | [Ableton Command Guide (ABLETON_COMMAND_GUIDE)](apps/ABLETON_COMMAND_GUIDE.md) (private) | `guide.py` |
| command that writes the hand-over STATE.md and opens a Master session | [Agent Manager (CEO) (Mantra) (AGENT_MANAGER)](apps/AGENT_MANAGER.md) | `helper/mantra_master.py` |
| scheduled Worker that fetches when a service becomes available | [ARKOD Layer (web) (arkod_web)](apps/arkod_web.md) | `fetcher/worker.js` |
| pre-push hook refusing media, keys and binaries | [Asana Guide (Mantra) (ASANA_GUIDE)](apps/ASANA_GUIDE.md) (private) | `tools/check_no_media.py` |
| reverse-engineering notes of the DOS binary and its calculation engine | [Astro DOS (astro_dos)](apps/astro_dos.md) (private) | `analysis/` |
| safe copy-verify-delete event mover | [Calendar Events (calendar_events)](apps/calendar_events.md) (private) | `calendar_events/mover.py` |
| key ring with fingerprints only and fallback between keys | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](apps/CCMC.md) | `ring.py` |
| sentence splitting, language detection per sentence, quota arithmetic | [Claude Talkie (Claude_Toki)](apps/Claude_Toki.md) (private) | `core.py` |
| TokiReader player that lights the current sentence and word from the media clock | [Claude Talkie (Claude_Toki)](apps/Claude_Toki.md) (private) | `static/reader.js` |
| draw a number as a status-bar notification icon | [Cockpit Android (COCKPIT_ANDROID)](apps/COCKPIT_ANDROID.md) | `app/src/main/java/com/mantra/cockpit/NumberIcon.kt` |
| generates the Colab restore notebook | [Colab Video Upscaler (colab-video-upscaler)](apps/colab-video-upscaler.md) (private) | `make_notebook.py` |
| parametric plate drawing generator to SVG and DXF | [CQ VESA Adapter (cq_vesa_adapter)](apps/cq_vesa_adapter.md) (private) | `drawings/make_drawings.py` |
| timeline from selected Media Pool clips | [DaVinci Resolve Assistant (DAVINCI_RESOLVE_ASSISTANT) (retired, use DAVINCI_RESOLVE_ACTIONS)](apps/DAVINCI_RESOLVE_ASSISTANT.md) | `Create Timeline.py` |
| Offline world city atlas (cities.tsv, countries.bin) with time zones for place lookup | [Donnie Horoscope (donnie-horoscope-releases)](apps/donnie-horoscope-releases.md) | `app/atlas/` |
| verified copy and move engine (count, bytes, MD5 of five largest, symlink left behind) | [Download, Copy and Move (Mantra) (was Download Monitor) (DOWNLOAD_MONITOR)](apps/DOWNLOAD_MONITOR.md) | `copier.py` |
| verify lyric lines against a source PDF | [Ethno Hrvatska song sheets (ETHNO-HRVATSKA)](apps/ETHNO-HRVATSKA.md) | `tools/check_lyrics.py` |
| Python client for the light API | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `tools/lightshow.py` |
| same-origin guard for a local web app | [GDrive Downloader (Flask, macOS) (GDRIVE_DOWNLOADER_FLASK_MACOS)](apps/GDRIVE_DOWNLOADER_FLASK_MACOS.md) (private) | `localguard.py` |
| load an extension folder into a running Firefox via WebDriver BiDi | [German to English (Mantra) (GERMAN_TO_ENGLISH)](apps/GERMAN_TO_ENGLISH.md) (private) | `tools/load_in_firefox.py` |
| reader module (MA Reader) | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](apps/GOOGLE_TTS_STT.md) | `src/41_reader.py` |
| key ring with fallback | [GVoices (Google Voices) (GoogleVoices)](apps/GoogleVoices.md) | `ring.py` |
| terminal console helper | [Keyring (KEYRING_TERMUX)](apps/KEYRING_TERMUX.md) | `console.py` |
| real provider key tests (smallest work call per provider) | [Keyring (KEYRING_TERMUX)](apps/KEYRING_TERMUX.md) | `probes.py` |
| puzzle generator stress test checking exactly one correct answer | [Mind Garden (kognius_app)](apps/kognius_app.md) (private) | `tests/stress.js` |
| build the OUI maker table | [LAN Scanner (Mantra) (LAN_SCANNER)](apps/LAN_SCANNER.md) | `tools/make_oui.py` |
| per-shop adapters (nabava, geizhals, proshop, hgspot...) | [Lenovo Hunter (LENOVO_HUNTER)](apps/LENOVO_HUNTER.md) | `src/adapters/` |
| shop adapter interface and in-stock guard | [Lenovo Hunter (LENOVO_HUNTER)](apps/LENOVO_HUNTER.md) | `src/core/StoreScraper.js` |
| delivery gate audit script | [MA Reader Termux / macOS (Edge / Speechify) (MA_READER_TERMUX_MACOS)](apps/MA_READER_TERMUX_MACOS.md) | `2py_gate_audit.py` |
| word timing experiments | [MA Reader Termux / macOS (Edge / Speechify) (MA_READER_TERMUX_MACOS)](apps/MA_READER_TERMUX_MACOS.md) | `2py_word_timing_lab.py` |
| one markdown card per stored action with id, app, kind, needs and state | [Macro Skills (MACRO_SKILLS)](apps/MACRO_SKILLS.md) (private) | `actions/` |
| sentence and word highlighting player | [Maha Transcribe Flask (MAHA_TRANSCRIBE_FLASK)](apps/MAHA_TRANSCRIBE_FLASK.md) (private) | `static/reader.js` |
| terminal dashboard | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `console.py` |
| Vendored Ceres solver used by the tracker JNI | [Mantra Manual Camera (mantra-manual-camera)](apps/mantra-manual-camera.md) | `app/src/main/cpp/third_party/ceres` |
| Script that sweeps requests into the remote cache repository | [Mantra ARKOD (mantra_arkod)](apps/mantra_arkod.md) | `scripts/remote-cache/sweep.py` |
| mechanical capability benchmark for extension building | [Mantra Chrome Extensions (MANTRA_CHROME_EXTENSIONS)](apps/MANTRA_CHROME_EXTENSIONS.md) | `tools/queen_bench.py` |
| Durable Object counter with once-per-day visitor dedupe | [Mantra Download Counter (MANTRA_DOWNLOAD_COUNTER)](apps/MANTRA_DOWNLOAD_COUNTER.md) (private) | `src/worker.js` |
| generate illustration plates for the book | [The Playable Instruction (Mantra filmmaking) (MANTRA_FILMMAKING)](apps/MANTRA_FILMMAKING.md) | `make_plates.py` |
| quick-settings volume tile | [Mantra Route (MANTRA_ROUTE)](apps/MANTRA_ROUTE.md) | `app/src/main/java/com/mantra/route/VolumeTileService.kt` |
| generate book illustration plates | [The Chat That Forgets (Mantra Software book) (MANTRA_SOFTWARE)](apps/MANTRA_SOFTWARE.md) | `make_plates.py` |
| Web Mercator and geo helpers | [Mantra Trail (MANTRA_TRAIL)](apps/MANTRA_TRAIL.md) | `app/src/main/java/com/mantra/trail/Geo.kt` |
| per-session switch stored in session state, plus tool-call refusal | [Mantra Voice Switch (MANTRA_VOICE_SWITCH)](apps/MANTRA_VOICE_SWITCH.md) (private) | `mod/hooks/register.tsx` |
| EN and HR dictionaries, bigrams, trigrams | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](apps/MANTRA_VOICE_TO_TEXT.md) | `mac/Resources/dict/` |
| generate book plates | [The Oldest Drum (Mediterranean percussion) (MEDITERRANEAN_PERCUSSION)](apps/MEDITERRANEAN_PERCUSSION.md) | `make_plates.py` |
| LED colour output for the E16 controller | [MIDI to Key Stroke (MIDI_TO_KEYSTROKE)](apps/MIDI_TO_KEYSTROKE.md) (private) | `e16led.lua` |
| persist an editable rule table | [MIDI to Key Stroke (MIDI_TO_KEYSTROKE)](apps/MIDI_TO_KEYSTROKE.md) (private) | `tablekeep.lua` |
| press the Mac volume keys so the native blob appears | [MIDI to Key Stroke (MIDI_TO_KEYSTROKE)](apps/MIDI_TO_KEYSTROKE.md) (private) | `volume.lua` |
| converts class recordings to MOV with time code | [MPA Academy, website and hub (mpa-academy)](apps/mpa-academy.md) (private) | `tools/mpaconv` |
| generates A4 PDF rhythm sheets | [MPA Academy, website and hub (mpa-academy)](apps/mpa-academy.md) (private) | `tools/sheets181.mjs` |
| delivery gate checks | [Sample Player, macOS (SAMPLE_PLAYER_MACOS)](apps/SAMPLE_PLAYER_MACOS.md) | `scripts/gates.py` |
| CLI and hook handlers for message ids, receipts, spool and git fallback | [Session Ack (ccmsg) (SESSION_ACK)](apps/SESSION_ACK.md) | `ccmsg.py` |
| builds the book plates | [The Long Night (SHAMANIC_PATHS)](apps/SHAMANIC_PATHS.md) | `make_plates.py` |
| builds the book plates | [Soak Your Nuts (SOAK_YOUR_NUTS)](apps/SOAK_YOUR_NUTS.md) | `make_plates.py` |
| uncached benchmark engine with F_NOCACHE, fsync and random data | [Mantra Speed Test (SPEED_TEST)](apps/SPEED_TEST.md) (private) | `engine.py` |
| builds the book plates | [The Descent (SRI_AUROBINDO_AND_MOTHER)](apps/SRI_AUROBINDO_AND_MOTHER.md) | `make_plates.py` |
| local Chromium extension plus bridge to drive suno.com | [Suno Songs prompt database (SUNO_SONGS)](apps/SUNO_SONGS.md) (private) | `extensions/suno_controller` |
| measure tempo, key and bar sections of a track | [Suno Songs prompt database (SUNO_SONGS)](apps/SUNO_SONGS.md) (private) | `scripts/measure.py` |
| guard so only local browser requests pass | [TP - Terminal Properties (TERMINAL_SHORTCUT_MACOS)](apps/TERMINAL_SHORTCUT_MACOS.md) (private) | `localguard.py` |
| shortname rules and conflict classification | [TP - Terminal Properties (TERMINAL_SHORTCUT_MACOS)](apps/TERMINAL_SHORTCUT_MACOS.md) (private) | `naming.py` |
| generate the guarded zsh include and marker block | [TP - Terminal Properties (TERMINAL_SHORTCUT_MACOS)](apps/TERMINAL_SHORTCUT_MACOS.md) (private) | `shell.py` |
| reference therapeutic stories in English and Croatian | [Story Medicine (THERAPEUTIC_STORIES)](apps/THERAPEUTIC_STORIES.md) | `corpus/` |
| Mailbox job runner using flock to share one phone between processes | [vm-android (Pixel 7 in Oracle Cloud) (vm-android)](apps/vm-android.md) | `api/jobrunner.py` |
| settle-then-push worker with remote verification | [Watch Folder Daemon (WATCH_FOLDER_DAEMON)](apps/WATCH_FOLDER_DAEMON.md) (private) | `bin/worker.py` |
| builds the book plates | [The Thread and the Still Lake (YOGA_SUTRAS)](apps/YOGA_SUTRAS.md) | `make_plates.py` |
