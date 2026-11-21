# Hardware: which apps drive which device

Device families first, then the apps that name a device of that family (live, then planned, then retired). The exact device wording from each card is in brackets.

## Neewer Bluetooth LED light

- [Light Control (Mantra) (planned)](apps/LIGHT_CONTROL.md) (Neewer Bluetooth LED light)

## Sony cameras (Alpha, ILCE-7M5, A6600)

### Which one to pick: Sony cameras: record, REC, settings, time code, live view, phone remote

Four different things are called 'record the Sony', and each has its own app. Recording the picture to the Mac disk is Webcam Recorder (web-cam-viewer, port 8867); starting REC on the camera's own card is Sony Remote (SONY_REMOTE_MAC, port 8881) or, through Imaging Edge Remote and Accessibility, `sonycam` in MACRO_SKILLS. Only one program can hold the camera's USB at a time (Imaging Edge Remote locks it, so Webcam Recorder asks for TAKE CONTROL), and a camera streaming over USB (UVC) cannot also be controlled over that cable. ISO and shutter through Webcam Recorder (`/sony/set`) are written in the code but were not verified against a real body at v27. Time code jam and Bluetooth REC for several Sonys are the Android app, not the Mac apps.

| You want | Use | How |
|---|---|---|
| record the Sony picture to a file on the Mac disk (H.265 .mov with time code) | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/record/start -H 'Content-Type: application/json' -d '{"name":"interview"}'` |
| stop that recording and get the file path | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/record/stop` |
| start REC on the camera's own card from the Mac | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](apps/SONY_REMOTE_MAC.md) | `curl -s -XPOST 127.0.0.1:8881/connect ; curl -s 127.0.0.1:8881/start` |
| start REC on the card through Imaging Edge Remote (Accessibility), also used by the Second Take guide | [Macro Skills (MACRO_SKILLS)](apps/MACRO_SKILLS.md) | `tools/sonycam start` |
| set ISO or shutter on a connected Sony (needs /sony/connect and /sony/takecontrol first; not verified against the body) | [Webcam Recorder (Mantra) (web-cam-viewer)](apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/sony/set -H 'Content-Type: application/json' -d '{"name":"ISO","label":"ISO 800"}'` |
| jam time code into a Sony body over USB, or REC on several Sonys over Bluetooth (Android) | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](apps/sony_remote_controller.md) | `adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --es tc 12:00:00:00` |
| see a live-view frame of the Sony as a picture | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](apps/SONY_REMOTE_MAC.md) | `curl -s 127.0.0.1:8881/frame.jpg -o live.jpg` |
| use the phone as a remote for the Mac shooting guide (watch, record, stop, next take) | [Second Take Remote (SECOND_TAKE_REMOTE)](apps/SECOND_TAKE_REMOTE.md) |  |
| use a Pixel phone as a manual camera with exposure, white balance and NDI (this is the phone's own camera, not a Sony) | [Mantra Manual Camera (mantra-manual-camera)](apps/mantra-manual-camera.md) | `scripts/mcam iso 400` |

- [Mantra Manual Camera](apps/mantra-manual-camera.md) (Sony Alpha cameras (REC over Bluetooth, timecode over USB))
- [Mantra Sony Remote (TC Jam), Android](apps/sony_remote_controller.md) (Sony Alpha 7 V / a6600 and other Alphas)
- [MPA Lessons Analyzer](apps/MPA_LESSONS_ANALYZER.md) (Sony camera via Webcam Recorder / Sony remote)
- [Skeleton (Mantra)](apps/SKELETON.md) (Sony ILCE-7M5 over USB)
- [Sony Remote (Mantra), Mac](apps/SONY_REMOTE_MAC.md) (Sony alpha 7 V (ILCE-7M5))
- [Webcam Recorder (Mantra)](apps/web-cam-viewer.md) (Sony ILCE-7M5 (A7 V) over USB PTP)
- [Light Control (Mantra) (planned)](apps/LIGHT_CONTROL.md) (Sony Alpha 7 V (through Webcam Recorder))

## Allen & Heath CQ mixers

### Which one to pick: Allen & Heath CQ-12T mixer (nine apps)

CQ MixPad (Mantra) is the Android remote built on the desk's decoded private protocol (TCP 51326); the protocol facts are in the public cq_mixpad_protocol, which also has the sniffer and injector. The desk allows one client at a time. To use it from a phone over a USB-LAN cable see CQ_ETHERNET_BRIDGE (a recipe, no code). From a knob controller use the OXI-CQ Bridge (oxi_e16_cq-12t, HTTP on 8753, MIDI NRPN, not the private protocol). The rest are a tutorial, a mount adapter, the Mac audio-output preference and the Ableton channel macros.

| You want | Use | How |
|---|---|---|
| control the CQ-12T from a phone (faders, PEQ, compressor, RTA, record) | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](apps/CQ_MIXPAD_MANTRA.md) |  |
| move a CQ fader or button from the OXI E16 or from a script | [OXI-CQ Bridge (oxi_e16_cq-12t)](apps/oxi_e16_cq-12t.md) | `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'` |
| look up or send raw CQ protocol messages | [CQ MixPad Protocol (cq_mixpad_protocol)](apps/cq_mixpad_protocol.md) | `tools/cq_inject.sh "f7 0c 0c 0d 00 00 56 5e"` |
| connect the desk to a Pixel over a USB-LAN cable | [CQ Ethernet Bridge (CQ_ETHERNET_BRIDGE)](apps/CQ_ETHERNET_BRIDGE.md) | `adb shell am start -a android.settings.TETHER_SETTINGS` |
| learn the CQ-12T with a spoken tutorial | [CQ MixPad Tutorial (Mantra) (cq_mixpad_tutorial)](apps/cq_mixpad_tutorial.md) | `build/start 6.2` |
| mount the CQ-12T on a VESA arm or tripod | [CQ VESA Adapter (cq_vesa_adapter)](apps/cq_vesa_adapter.md) | `python3 drawings/make_drawings.py --measured` |
| make the Mac's audio output prefer the CQ12T | [Audio Prefer (audio-prefer)](apps/audio-prefer.md) | `audio-prefer --once` |
| map Ableton tracks to the CQ-12T channels | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](apps/ABLETON_LIVE_ACTIONS.md) |  |
| run an Android app such as CQ MixPad in a headless emulator without touching the phone | [Mantra Sandbox (MANTRA_SANDBOX)](apps/MANTRA_SANDBOX.md) | `sandbox run macros/cqmixpad/tab_fader.macro` |

- [Ableton Live Actions (Mantra)](apps/ABLETON_LIVE_ACTIONS.md) (Allen & Heath CQ-12T (via CQ MixPad, USB multitrack))
- [Audio Prefer](apps/audio-prefer.md) (Allen & Heath CQ-12T)
- [CQ Ethernet Bridge](apps/CQ_ETHERNET_BRIDGE.md) (Allen & Heath CQ-12T)
- [CQ MixPad (Mantra)](apps/CQ_MIXPAD_MANTRA.md) (Allen & Heath CQ-12T)
- [CQ MixPad Protocol](apps/cq_mixpad_protocol.md) (Allen & Heath CQ-12T (and other CQ desks))
- [CQ MixPad Tutorial (Mantra)](apps/cq_mixpad_tutorial.md) (Allen & Heath CQ-12T)
- [CQ VESA Adapter](apps/cq_vesa_adapter.md) (Allen & Heath CQ-12T)
- [OXI-CQ Bridge](apps/oxi_e16_cq-12t.md) (Allen & Heath CQ-12T)

## Ableton Live

### Which one to pick: Ableton Live

Ableton is driven by AbletonOSC (UDP 11000 in, 11001 answers; 11001 has one owner and others send to the router on 11002). ABLETON_LIVE_ACTIONS is the Mac app with the A1 assistant, MIDI to Mackie and CQ channel macros; `python3 live.py set /live/song/set/tempo 96` in ABLETON_TEACHER is the quickest scripted call; Queen exposes `POST /api/ableton/action` and mantra_pages `POST /api/live`. ABLETON_COMMAND_GUIDE answers shortcut questions by voice; the Teacher apps (MANTRA_TEACHERS, 8970) teach step by step.

| You want | Use | How |
|---|---|---|
| set tempo or read the song from a script | [Teacher Lessons and Scripts (Ableton, DaVinci) (ABLETON_TEACHER)](apps/ABLETON_TEACHER.md) | `python3 live.py set /live/song/set/tempo 96` |
| tell Queen to control Ableton | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](apps/groq_ai_studio.md) | `curl -s -XPOST 127.0.0.1:8765/api/ableton/action -H 'Content-Type: application/json' -d '{"action":"set_tempo","arguments":{"bpm":120}}'` |
| ask a shortcut question, or give a spoken order | [Ableton Command Guide (ABLETON_COMMAND_GUIDE)](apps/ABLETON_COMMAND_GUIDE.md) | `python3 guide.py ask "how do I split a clip"` |
| use a MIDI knob as a Mackie control in Live | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) |  |
| learn Ableton with a spoken teacher | [Ableton Teacher and DaVinci Teacher apps (Mantra) (MANTRA_TEACHERS)](apps/MANTRA_TEACHERS.md) | `curl -s 127.0.0.1:8970/state` |
| split a song into stems with Live | [Stem Separation (Mantra) (STEM_SEPARATION)](apps/STEM_SEPARATION.md) |  |

- [MIDI Tools (Mantra)](apps/MANTRA_MIDI_TOOLS.md) (Ableton Live with MackieControl surface and optional AbletonOSC)
- [Queen (Groq AI Studio), server and tools](apps/groq_ai_studio.md) (Ableton Live via AbletonOSC (UDP 11000/11001 family))
- [Queen auto-update (Groq Auto Update)](apps/groq-auto-update.md) (Ableton Live via AbletonOSC (UDP 11000/11001 family))

## OXI E16 and MIDI controllers

### Which one to pick: OXI E16 and MIDI controllers

The OXI E16 is used three ways: as a remote for Ableton Live or DaVinci Resolve audio (oxi-controller, UDP test door on 11010), as a controller of the CQ-12T mixer (oxi_e16_cq-12t, HTTP 8753, MIDI NRPN), and as Mackie Control under Ableton's timeline (mantra-mackie-control-translator, Hammerspoon). Generic MIDI helpers: MIDI Tools (MANTRA_MIDI_TOOLS), Controller Mapper for any USB controller (mix-ultra-mapper) and the dormant MIDI to Key Stroke (MIDI_TO_KEYSTROKE) and Mantra Controls.

| You want | Use | How |
|---|---|---|
| turn a virtual knob of the OXI E16 on the Mac remote | [Oxi Controller (E16 Remote) (oxi-controller)](apps/oxi-controller.md) | `echo 'turn 1 5' \| nc -u -w1 127.0.0.1 11010` |
| move a CQ-12T control from the E16 or a script | [OXI-CQ Bridge (oxi_e16_cq-12t)](apps/oxi_e16_cq-12t.md) | `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'` |
| make a knob scroll Ableton's arrangement | [Mantra Mackie Control Translator (mantra-mackie-control-translator)](apps/mantra-mackie-control-translator.md) |  |
| map MIDI to keystrokes or Mackie commands | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](apps/MANTRA_MIDI_TOOLS.md) |  |
| map any USB MIDI controller by guided learning | [Controller Mapper (Mantra) (mix-ultra-mapper)](apps/mix-ultra-mapper.md) | `open -a "Controller Mapper (Mantra)" --args /path/layout.json` |

- [Ableton Live Actions (Mantra)](apps/ABLETON_LIVE_ACTIONS.md) (MIDI controllers (e.g. OXI E16))
- [Controller Mapper (Mantra)](apps/mix-ultra-mapper.md) (Hercules DJControl Mix Ultra; any USB MIDI controller)
- [DJ Mantra (Android DJ app)](apps/djmantra_app.md) (Hercules DJControl Mix Ultra)
- [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](apps/MANTRA_CONTROLS.md) (MIDI controllers (via the engines))
- [Mantra Mackie Control Translator](apps/mantra-mackie-control-translator.md) (OXI Instruments E16; IAC MIDI driver)
- [MIDI to Key Stroke](apps/MIDI_TO_KEYSTROKE.md) (any USB MIDI controller; IAC Driver for tests)
- [MIDI Tools (Mantra)](apps/MANTRA_MIDI_TOOLS.md) (Any MIDI controller (E16 colour helper))
- [Oxi Controller (E16 Remote)](apps/oxi-controller.md) (OXI Instruments E16)
- [OXI-CQ Bridge](apps/oxi_e16_cq-12t.md) (OXI Instruments E16)
- [Pianoverse Demo Songs by Mantra](apps/PIANOVERSE_DEMO_SONGS.md) (IAC Driver)
- [Shruti Box and Voice Trainer](apps/SHRUTI_BOX_AND_VOICE_TRAINER.md) (USB MIDI keyboard (Launchkey Mini MK4))

## Logitech G815 keyboard and RGB lighting

### Which one to pick: Voice dictation keyboard

On Android the voice keyboard is TTT (Talk to Type, repo TTT; package seen as tttlight): dictate into any text field with cloud or offline engines, with an RE reply assistant and an adb remote API. DictateKeyboard (TTT&LLL) is the older fork with the AI reader (LLL) and is dormant; ttt-layouts restores the owner's key layout. On the Mac and Windows the equivalent is Vox to Txt (MANTRA_VOICE_TO_TEXT): press F1, talk, press F1, the words are typed at the cursor.

| You want | Use | How |
|---|---|---|
| dictate on an Android phone into any app | [TTT Voice Type keyboard (TTT)](apps/TTT.md) |  |
| type text into the focused field of the phone from a script | [TTT Voice Type keyboard (TTT)](apps/TTT.md) | `python3 tools/ttt_remote.py say "The render is done"` |
| restore my TTT keyboard layout on a new phone | [TTT Layouts (ttt-layouts)](apps/ttt-layouts.md) |  |
| dictate on the Mac or Windows with F1 | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](apps/MANTRA_VOICE_TO_TEXT.md) |  |
| older keyboard with the reader (LLL) | [TTT&LLL (Talk to Type, Look Listen Learn) (DictateKeyboard)](apps/DictateKeyboard.md) |  |

### Which one to pick: Keyboard lights and visuals

The only light hardware with an API today is the Logitech G815 keyboard, run by G815 Lights (G815_LIGHTS, HTTP 8877, stream 8878): it is a 115-key low-resolution LED display for any app's pictures or shows. Mantra Room (MANTRA_ROOM) drives it with `lights: true` in `play-loop` and has the MilkDrop visuals. There is no app for Bluetooth LED lights (Neewer) yet; Light Control is planned (see gaps).

| You want | Use | How |
|---|---|---|
| show a colour or picture on the keyboard | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"color":"ff0000"}'` |
| play a light show on the keyboard | [G815 Lights (G815_LIGHTS)](apps/G815_LIGHTS.md) | `curl -s -XPOST 127.0.0.1:8877/show -H 'Content-Type: application/json' -d '{"name":"rainbow","seconds":20}'` |
| play a relaxation loop with keyboard lights and MilkDrop visuals until a time | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'` |
| see which key I pressed as a big glyph | [Keyboard Monitor (Mantra) (keyboard-monitor)](apps/keyboard-monitor.md) | `KeyboardMonitor --shot /tmp/k.png` |

- [Avid Assistant](apps/AVID_ASSISTANT.md) (OpenRGB lighting (optional))
- [G815 Lights](apps/G815_LIGHTS.md) (Logitech G815 keyboard (HID++))
- [Launcher (Mantra)](apps/STAR_LAUNCHER.md) (Logitech G815 (Pause key))
- [Mantra Room (Meditation Room / Chakra and Elements Toning)](apps/MANTRA_ROOM.md) (Logitech G815 keyboard)

## Elgato Stream Deck

- [Stream Deck Remote](apps/STREAM_DECK_REMOTE.md) (Elgato Stream Deck 15-key)
- [Stream Deck Control (Mantra), retired (retired)](apps/stream-deck-control.md) (Elgato Stream Deck original 15-key (0x0fd9:0x0060))

## Capture cards, webcams and NDI gear

- [CineView Viewer](apps/CINEVIEW_VIEWER.md) (Accsoon CineView Nano)
- [Mantra Manual Camera](apps/mantra-manual-camera.md) (USB cable for NDI without network)
- [Mantra Room (Meditation Room / Chakra and Elements Toning)](apps/MANTRA_ROOM.md) (NDI network)
- [Mantra Sony Remote (TC Jam), Android](apps/sony_remote_controller.md) (Accsoon CineView Nano (planned mode))
- [Skeleton (Mantra)](apps/SKELETON.md) (Mac cameras)
- [Webcam Recorder (Mantra)](apps/web-cam-viewer.md) (UGREEN HDMI capture card; USB webcams)

## Microphones, speakers and audio outputs

### Which one to pick: Read aloud / text to speech: Mac, Android, Termux, engines

On the Mac, speaking and reading are one server: Mantra Voice (MANTRA_VOICE, port 8837) with `/speak` for a spoken line and `/say` for mp3 plus word timings; VOICE_ENGINE is only the subtitle band and the global on/off switch. On the phone, `phonesay` and TERMUX_VOICE (port 8840) speak a line; the browser reader with the word lit is MA_READER_TERMUX_MACOS (Termux or Mac, Edge and Speechify voices, port 8081). The native Android app MA Reader (MA_READER_ANDROID) does not speak yet; its engine is the Kotlin library MA_READER_ENGINE (Edge speech with word timing) that TTT's LLL reader also uses. Google voices are GOOGLE_TTS_STT (gtt, 7311) and GoogleVoices (gvoice, 8300).

| You want | Use | How |
|---|---|---|
| make the Mac speak a sentence | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) | `curl -s -XPOST 127.0.0.1:8837/speak -H 'Content-Type: application/json' -d '{"text":"The render is done.","wait":true}'` |
| get mp3 plus word timings for a highlighted reader page | [Mantra Voice (speech server) (MANTRA_VOICE)](apps/MANTRA_VOICE.md) | `curl -s -XPOST 127.0.0.1:8837/say -H 'Content-Type: application/json' -d '{"text":"Hello"}'` |
| mute or switch all Claude voices, subtitle band, replay | [Voice Engine (Mantra) (VOICE_ENGINE)](apps/VOICE_ENGINE.md) | `voiceengine off (writes ~/.mantra/voice_engine_state and stops the current reading)` |
| make the phone speak a sentence | [Termux Voice (voiced) (TERMUX_VOICE)](apps/TERMUX_VOICE.md) | `phonesay pixel "The render is done."` |
| read pasted text aloud with the word lit, on the phone (Termux) or the Mac | [MA Reader Termux / macOS (Edge / Speechify) (MA_READER_TERMUX_MACOS)](apps/MA_READER_TERMUX_MACOS.md) | `curl -s -X POST http://127.0.0.1:8081/api/say -H 'Content-Type: application/json' -d '{"text":"hello","lang":"en"}' -o out.mp3` |
| read aloud with the word lit on Android: use the Termux reader; the native app is not speaking yet | [MA Reader for Android (MA_READER_ANDROID)](apps/MA_READER_ANDROID.md) |  |
| reuse the Edge speech client with word timing in Kotlin | [MA Reader Engine (MA_READER_ENGINE)](apps/MA_READER_ENGINE.md) |  |
| Speechify key ring and Speechify voices on the phone | [MA Reader Speechify module (MA_READER_SPEECHIFY)](apps/MA_READER_SPEECHIFY.md) |  |
| Google or Gemini voice for a sentence | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](apps/GOOGLE_TTS_STT.md) | `curl -s -XPOST 127.0.0.1:7311/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}'` |
| read text aloud in a web page with word highlighting (Streamlit) | [EdgeReader (MA Reader Streamlit) (mareader)](apps/mareader.md) |  |

- [Ableton Command Guide](apps/ABLETON_COMMAND_GUIDE.md) (microphone)
- [Audio Prefer](apps/audio-prefer.md) (ADAM Audio D3V; MacBook Pro speakers)
- [Maha Transcribe (Termux/terminal)](apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (microphone)
- [Maha Transcribe / TTT-LLL (Streamlit)](apps/MAHA_TRANSCRIBE_STREAMLIT.md) (microphone)
- [Maha Transcribe Android (native)](apps/MAHA_TRANSCRIBE_ANDROID_2.md) (Android microphone)
- [Mantra Room (Meditation Room / Chakra and Elements Toning)](apps/MANTRA_ROOM.md) (any audio output (e.g. BlackHole 2ch))
- [Mantra Route](apps/MANTRA_ROUTE.md) (Bluetooth / USB / hearing-aid outputs)
- [Mantra Voice (speech server)](apps/MANTRA_VOICE.md) (speakers; microphone)
- [Plugin Assistant](apps/PLUGIN_ASSISTANT.md) (microphone; BlackHole 2ch virtual device)
- [Screen Copy (Mantra)](apps/MANTRA_SCREEN_COPY.md) (Mac microphone)
- [Sound Link (Mantra)](apps/SOUND_LINK.md) (XLR mixer / BlackHole)
- [Sound Recorder (Mantra)](apps/MANTRA_SOUND_RECORDER.md) (any CoreAudio input and output device)
- [Spectral Analyzer (Mantra)](apps/SPECTRAL_ANALYZER.md) (BlackHole 2ch; audio interface or speakers)
- [Talk Mode (Mantra)](apps/TALK_MODE.md) (microphone)
- [Talk with Claude Code](apps/TALK_WITH_CLAUDE.md) (microphone; speakers)
- [TTT Voice Type keyboard](apps/TTT.md) (Android phone microphone)
- [Vox to Txt (Mantra)](apps/MANTRA_VOICE_TO_TEXT.md) (microphone)
- [Maha Transcribe Android v3 (web view, superseded) (retired)](apps/MAHA_TRANSCRIBE_ANDROID.md) (Android microphone)
- [Maha Transcribe Termux v1 (superseded) (retired)](apps/MAHA_TRANSCRIBE_TERMUX.md) (phone microphone)
- [Transcribe Voice to Text RT (Mantra), retired (retired)](apps/MARKO_TRANSCRIBE.md) (microphone)

## Android phones (Pixel, Nothing) and emulators

### Which one to pick: Controlling Claude Code sessions: phone, Mac, cloud

Phone: AGENT_MANAGER_ANDROID is the client of the Mac's AGENT_MANAGER phone door (8847, bearer token over Tailscale), where blockers are answered and tasks paused; CLAUDE_CODE_TERMUX installs Claude Code on the phone itself. Mac: SESSION_HUB (8890) and SESSION_ACK (8899) pass messages between sessions, CCMC (MANTRA CHAT, 8825) mirrors a session as a chat page, TALK_MODE talks to sessions by voice, CLAUDE_CONTROL (`claudectl pause`) stops everything Claude runs, COST_AGENT asks before paid calls. Cloud: vm-chromium drives claude.ai in a VM browser (`cvm ask`). CLAUDE_CODE_MONITOR is archived.

| You want | Use | How |
|---|---|---|
| see and steer my Claude agents from the phone | [Agent Manager (CEO) (Mantra) for Android (AGENT_MANAGER_ANDROID)](apps/AGENT_MANAGER_ANDROID.md) |  |
| read the overview of all sessions and workers on the Mac side | [Agent Manager (CEO) (Mantra) (AGENT_MANAGER)](apps/AGENT_MANAGER.md) | `curl -s -H 'Authorization: Bearer $(cat ~/Downloads/API/agent-manager-token.txt)' http://<mac-tailscale-address>:8847/overview` |
| send a message from one Claude session to another | [Session Hub (SESSION_HUB)](apps/SESSION_HUB.md) | `hub send other-session "Please review the diff"` |
| send with delivery receipt | [Session Ack (ccmsg) (SESSION_ACK)](apps/SESSION_ACK.md) | `ccmsg send <to> "text" then ccmsg wait <id>` |
| answer a session from a chat page, read answers aloud | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](apps/CCMC.md) | `curl -s -XPOST 127.0.0.1:8825/api/send -H 'Content-Type: application/json' -d '{"text":"Yes, go ahead"}'` |
| pause everything Claude is running | [Claude Control (Mantra) (CLAUDE_CONTROL)](apps/CLAUDE_CONTROL.md) | `claudectl pause` |
| ask before any paid API call | [Cost Agent (Mantra) (COST_AGENT)](apps/COST_AGENT.md) | `curl -s -XPOST 127.0.0.1:9047/ask -H 'Content-Type: application/json' -d '{"who":"queen","what":"describe 20 images","provider":"groq","estimate_usd":0.40,"items":20,"job":"img-batch-1"}'` |
| ask Claude in the cloud browser VM | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `cvm ask "Summarise the open tab in one sentence"` |
| install Claude Code on an Android phone | [Claude Code for Termux (CLAUDE_CODE_TERMUX)](apps/CLAUDE_CODE_TERMUX.md) | `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/CLAUDE_CODE_TERMUX/main/install.sh -o cct.sh && bash cct.sh --proot` |

### Which one to pick: Cloud VMs: Android emulator and Chromium

Two Oracle Cloud machines are reached over Tailscale. vm-android is a redroid Pixel 7 with the Mac command `pixel7` and the door pixel7d on 8897; vm-android-jobs is the git mailbox for the same phone: push `jobs/<id>/job.json` and an APK, pull `results/<id>/result.json`. vm-chromium is the Chromium VM with the vm-agent on 8890 and the Mac command `cvm`. Local, not cloud: MANTRA_SANDBOX runs a headless emulator on the Mac. Related VM services: CLOUD_MIXER and STREAMING_DASHBOARD.

| You want | Use | How |
|---|---|---|
| install and test an APK on the cloud Pixel 7 | [vm-android (Pixel 7 in Oracle Cloud) (vm-android)](apps/vm-android.md) | `pixel7 test app.apk` |
| test an APK without Tailscale or a terminal: git mailbox | [VM Android jobs mailbox (vm-android-jobs)](apps/vm-android-jobs.md) | `ID=20261104-remote-v22; mkdir -p jobs/$ID && cp app.apk jobs/$ID/app.apk && cp job.json jobs/$ID/job.json && git add jobs/$ID && git commit -m "job $ID" && git push` |
| use a Chromium browser in the cloud | [Chromium Virtual Machine (Mantra) (vm-chromium)](apps/vm-chromium.md) | `cvm ask "Summarise the open tab in one sentence"` |
| mix files and live URLs into one picture on the VM | [Cloud Mixer (CLOUD_MIXER)](apps/CLOUD_MIXER.md) | `curl -s 127.0.0.1:8841/load -d '{"src":"/srv/cloud-mixer/media/x.mp4","id":"cam1","start":300}'` |
| start or stop the live stream chain | [Streaming Dashboard (Mantra) (STREAMING_DASHBOARD)](apps/STREAMING_DASHBOARD.md) | `curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"go-live","minutes":15}'` |

- [Calendar Events](apps/calendar_events.md) (Android phone with adb or Shizuku)
- [Code Filler (Mantra)](apps/MANTRA_CODE_FILLER.md) (Android phone over adb)
- [Connection Keeper](apps/connection-keeper.md) (USB-tethered Android phone over adb; phone hotspots)
- [CQ Ethernet Bridge](apps/CQ_ETHERNET_BRIDGE.md) (Pixel 7)
- [CQ MixPad (Mantra)](apps/CQ_MIXPAD_MANTRA.md) (Pixel 7)
- [DJ Mantra (Android DJ app)](apps/djmantra_app.md) (Pixel 7 test phone)
- [djay Sync (Mantra), Mac window](apps/DJING_SYNC.md) (Android phone over adb)
- [djay Sync, command line (djay-sync)](apps/djay-playlists.md) (Android phone over adb (Wi-Fi or USB))
- [FTP Server v4](apps/ftp-server-termux-and-terminal.md) (Android phone)
- [gi (Instagram downloader)](apps/gi.md) (Android phone with wireless debugging)
- [MA Player](apps/ma-player.md) (Android phone)
- [Mantra ARKOD](apps/mantra_arkod.md) (Android phone GPS)
- [Mantra Manual Camera](apps/mantra-manual-camera.md) (Pixel 7 and Nothing Phone (Android))
- [Mantra Remote Viewing (Mantra Remote)](apps/MANTRA_REMOTE_VIEWING.md) (Android phones (Pixel 7, Nothing Phone))
- [Mantra Route](apps/MANTRA_ROUTE.md) (Nothing Phone (2a) on Android 16)
- [Mantra Sandbox](apps/MANTRA_SANDBOX.md) (Android emulator (AVD mantra_sandbox, serial emulator-5580))
- [Mantra Trail](apps/MANTRA_TRAIL.md) (phone GPS, compass, accelerometer)
- [Mind Garden](apps/kognius_app.md) (Android phone)
- [Router Mode (Mantra)](apps/router-mode.md) (Android phone with Ethernet dongle (tethering))
- [Screen Copy (Mantra)](apps/MANTRA_SCREEN_COPY.md) (Android phones over USB/Wi-Fi/Tailscale)
- [Skeleton (Mantra)](apps/SKELETON.md) (Pixel/Nothing phones with Manual Camera)
- [Sound Link (Mantra)](apps/SOUND_LINK.md) (Pixel phone running Manual Camera)
- [Spar Locator / DM Finder](apps/spar_locator.md) (Android phone GPS)
- [Termux Tools](apps/termux-tools.md) (Android phone (Pixel 7, Nothing Phone))
- [Termux Voice (voiced)](apps/TERMUX_VOICE.md) (Android phones with Termux (Nothing, Pixel 7))
- [USB Tethering (Mantra)](apps/USB_TETHERING.md) (Nothing Phone 2a; Pixel 7)
- [Virtual Cam (Mantra)](apps/mantra_virtual_cam.md) (Android phone camera)
- [VM Android jobs mailbox](apps/vm-android-jobs.md) (Android arm64 container on cloud VM)
- [ZET Strike](apps/zet_strike.md) (Android phone GPS)
- [Voice Engine Android (retired) (retired)](apps/VOICE_ENGINE_ANDROID.md) (Android phones (Nothing A142))

## Routers, cables and network adapters

### Which one to pick: Ports and the door protocol: how any app is called

A Mantra Mac app listens on 127.0.0.1 only, on a port it claims by name in MANTRA_PORTS (registry file ~/.config/mantra-ports.json), and answers `GET /health`, `GET /api` (the declared actions) and `POST /api/<action>` with a JSON body; the reply is `{ok, result}` or `{ok:false, error}`. Mantra Door is the token-guarded gateway for the phone (header X-Mantra-Token, token in ~/.config/mantra-door.token, Tailscale address only): `GET /apps`, `POST /apps/<id>/launch`, and any `/apps/<id>/api/...` is passed on to the app, starting it if needed. Python code uses `mantra_remote.py` (`remote.call("dock-switcher", "show")`). To give a NEW app a port run `mantra-ports next`, claim it at start with `ports.claim("my-app", N)` (Swift `Ports.claim`, Lua `ports.lua`) and ask by name everywhere else. Several numbers are claimed twice, notably 8965 (MANTRA_ROOM, MPA_LESSONS_ANALYZER, SECOND_TAKE_REMOTE), 8837 (MANTRA_VOICE, VOICE_ENGINE) and 8847 (AGENT_MANAGER, retired spotlight): check which app answers `GET /health`.

| You want | Use | How |
|---|---|---|
| get a free port for a new app and register it | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) | `mantra-ports next` |
| claim the port in a Python server | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) | `import sys, os; sys.path.insert(0, os.path.expanduser('~/.local/lib/mantra')); import ports; PORT = ports.claim('my-app', 8962)` |
| find where a service runs | [Mantra Ports (MANTRA_PORTS)](apps/MANTRA_PORTS.md) | `mantra-ports find voice` |
| press, open or quit a star app from the phone or an HTTP client | [Star API (Mantra) (STAR_API)](apps/STAR_API.md) | `curl -s -XPOST 127.0.0.1:8863/apps/timer/press -H "Content-Type: application/json" -d '{"label":"stopwatch"}'` |
| drive an app that serves its own door, e.g. Meditation Room | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](apps/MANTRA_ROOM.md) | `curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'` |
| control the Android phone through its Claude Control door and the macro door | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](apps/MANTRA_REMOTE_VIEWING.md) | `rvctl pixel tap 540 1200 --label "NDI" --watched --expect com.mantraproductions.manualcamera` |

- [Connection Keeper](apps/connection-keeper.md) (Ethernet adapter)
- [CQ Ethernet Bridge](apps/CQ_ETHERNET_BRIDGE.md) (USB-to-LAN dongle)
- [DJ Mantra (Android DJ app)](apps/djmantra_app.md) (USB sticks/SD cards)
- [LAN Scanner (Mantra)](apps/LAN_SCANNER.md) (Mac network interfaces)
- [MacBook Pro as external display](apps/MacBook_Pro_as_external_display.md) (USB-C dummy display plug; Thunderbolt 4 cable)
- [Mantra Sony Remote (TC Jam), Android](apps/sony_remote_controller.md) (USB-C)
- [Router Mode (Mantra)](apps/router-mode.md) (TP-Link TL-MR110 4G outdoor router)
- [Router SMS](apps/router-sms.md) (TP-Link 4G router with SIM)
- [Session Ack (ccmsg)](apps/SESSION_ACK.md) (always-on VM (chromium-vm) reachable over Tailscale)
- [USB Tethering (Mantra)](apps/USB_TETHERING.md) (USB cable to Mac)
- [Virtual Cam (Mantra)](apps/mantra_virtual_cam.md) (USB cable)

## Cloud and Linux virtual machines

- [aooserver-arm64](apps/aooserver-arm64.md) (Oracle arm64 VM chromium-vm)
- [Chromium Virtual Machine (Mantra)](apps/vm-chromium.md) (Oracle Cloud Ampere A1 VM)
- [Cloud Mixer](apps/CLOUD_MIXER.md) (Oracle ARM VM, 2 cores 12 GB (chromium-vm))
- [Mantra Remote Viewing (Mantra Remote)](apps/MANTRA_REMOTE_VIEWING.md) (Linux VM)
- [Streaming Dashboard (Mantra)](apps/STREAMING_DASHBOARD.md) (cloud VM chromium-vm)
- [vm-android (Pixel 7 in Oracle Cloud)](apps/vm-android.md) (Oracle Cloud Ampere A1 VM (no KVM))

## Mouse and trackball

- [Automated Mouse Actions (Mantra)](apps/MANTRA_MOUSE.md) (mouse with extra buttons)
- [Import Button (Mantra)](apps/IMPORT_BUTTON.md) (mouse with extra buttons)
- [Brain Brake Keyboard (Hammerspoon) (retired)](apps/BRAIN_BRAKE_KEYBOARD.md) (Kensington trackball)

## Mac computers, displays and GPU

- [Android Lab](apps/android-lab.md) (Apple Silicon Mac (emulator))
- [Avid Assistant](apps/AVID_ASSISTANT.md) (two-monitor Windows workstation)
- [Blender Control](apps/blender-control.md) (Apple Silicon Metal GPU (Cycles))
- [Chromium Virtual Machine (Mantra)](apps/vm-chromium.md) (Mac running the viewer)
- [CQ MixPad Tutorial (Mantra)](apps/cq_mixpad_tutorial.md) (external monitor)
- [FTP Server v4](apps/ftp-server-termux-and-terminal.md) (Mac)
- [MacBook Pro as external display](apps/MacBook_Pro_as_external_display.md) (MacBook Pro 14 M1 Pro; MacBook Pro 16 M1 Pro)
- [Macro Recorder (Mantra)](apps/MANTRA_MACRO.md) (Mac display and input devices)
- [Mantra Remote Viewing (Mantra Remote)](apps/MANTRA_REMOTE_VIEWING.md) (Mac)
- [Mantra Voice (speech server)](apps/MANTRA_VOICE.md) (Apple silicon GPU (MLX))
- [Screen Brightness Automatic (Mantra)](apps/DARKEN_THE_SCREENS.md) (built-in display; BenQ monitor)

## Other devices

- [Mantra Speed Test](apps/SPEED_TEST.md) (external or internal SSD)
- [Pianoverse Demo Songs by Mantra](apps/PIANOVERSE_DEMO_SONGS.md) (IK Multimedia Pianoverse)
