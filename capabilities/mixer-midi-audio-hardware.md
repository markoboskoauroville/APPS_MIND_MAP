[Back to the index](../CAPABILITIES.md)

# Mixers, MIDI and audio hardware

## Which one to pick: Allen & Heath CQ-12T mixer (nine apps)

CQ MixPad (Mantra) is the Android remote built on the desk's decoded private protocol (TCP 51326); the protocol facts are in the public cq_mixpad_protocol, which also has the sniffer and injector. The desk allows one client at a time. To use it from a phone over a USB-LAN cable see CQ_ETHERNET_BRIDGE (a recipe, no code). From a knob controller use the OXI-CQ Bridge (oxi_e16_cq-12t, HTTP on 8753, MIDI NRPN, not the private protocol). The rest are a tutorial, a mount adapter, the Mac audio-output preference and the Ableton channel macros.

| You want | Use | How |
|---|---|---|
| control the CQ-12T from a phone (faders, PEQ, compressor, RTA, record) | [CQ MixPad (Mantra) (CQ_MIXPAD_MANTRA)](../apps/CQ_MIXPAD_MANTRA.md) |  |
| move a CQ fader or button from the OXI E16 or from a script | [OXI-CQ Bridge (oxi_e16_cq-12t)](../apps/oxi_e16_cq-12t.md) | `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'` |
| look up or send raw CQ protocol messages | [CQ MixPad Protocol (cq_mixpad_protocol)](../apps/cq_mixpad_protocol.md) | `tools/cq_inject.sh "f7 0c 0c 0d 00 00 56 5e"` |
| connect the desk to a Pixel over a USB-LAN cable | [CQ Ethernet Bridge (CQ_ETHERNET_BRIDGE)](../apps/CQ_ETHERNET_BRIDGE.md) | `adb shell am start -a android.settings.TETHER_SETTINGS` |
| learn the CQ-12T with a spoken tutorial | [CQ MixPad Tutorial (Mantra) (cq_mixpad_tutorial)](../apps/cq_mixpad_tutorial.md) | `build/start 6.2` |
| mount the CQ-12T on a VESA arm or tripod | [CQ VESA Adapter (cq_vesa_adapter)](../apps/cq_vesa_adapter.md) | `python3 drawings/make_drawings.py --measured` |
| make the Mac's audio output prefer the CQ12T | [Audio Prefer (audio-prefer)](../apps/audio-prefer.md) | `audio-prefer --once` |
| map Ableton tracks to the CQ-12T channels | [Ableton Live Actions (Mantra) (ABLETON_LIVE_ACTIONS)](../apps/ABLETON_LIVE_ACTIONS.md) |  |
| run an Android app such as CQ MixPad in a headless emulator without touching the phone | [Mantra Sandbox (MANTRA_SANDBOX)](../apps/MANTRA_SANDBOX.md) | `sandbox run macros/cqmixpad/tab_fader.macro` |

## Which one to pick: OXI E16 and MIDI controllers

The OXI E16 is used three ways: as a remote for Ableton Live or DaVinci Resolve audio (oxi-controller, UDP test door on 11010), as a controller of the CQ-12T mixer (oxi_e16_cq-12t, HTTP 8753, MIDI NRPN), and as Mackie Control under Ableton's timeline (mantra-mackie-control-translator, Hammerspoon). Generic MIDI helpers: MIDI Tools (MANTRA_MIDI_TOOLS), Controller Mapper for any USB controller (mix-ultra-mapper) and the dormant MIDI to Key Stroke (MIDI_TO_KEYSTROKE) and Mantra Controls.

| You want | Use | How |
|---|---|---|
| turn a virtual knob of the OXI E16 on the Mac remote | [Oxi Controller (E16 Remote) (oxi-controller)](../apps/oxi-controller.md) | `echo 'turn 1 5' \| nc -u -w1 127.0.0.1 11010` |
| move a CQ-12T control from the E16 or a script | [OXI-CQ Bridge (oxi_e16_cq-12t)](../apps/oxi_e16_cq-12t.md) | `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'` |
| make a knob scroll Ableton's arrangement | [Mantra Mackie Control Translator (mantra-mackie-control-translator)](../apps/mantra-mackie-control-translator.md) |  |
| map MIDI to keystrokes or Mackie commands | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](../apps/MANTRA_MIDI_TOOLS.md) |  |
| map any USB MIDI controller by guided learning | [Controller Mapper (Mantra) (mix-ultra-mapper)](../apps/mix-ultra-mapper.md) | `open -a "Controller Mapper (Mantra)" --args /path/layout.json` |

### [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md)

macOS; API: none

- map Ableton tracks to the CQ12T mixer (Ableton Live Actions)
- sync two recordings of the same concert (Ableton Live Actions)
- use a MIDI knob as a Mackie control in Live (Ableton Live Actions)
- set the loop to the transients in Ableton (Ableton Live Actions)
- copy mixer channel names into Live (Ableton Live Actions)

### [AndroidVU](../apps/ANDROIDVU.md)

Android; API: none

- show audio levels on my Android phone (AndroidVU)
- find out if Android lets me read stream volume (AndroidVU)
- VU meter overlay on the phone (AndroidVU)

### [Audio Prefer](../apps/audio-prefer.md)

macOS; API: cli. Main call: `audio-prefer --once # sets the Mac's audio output to the first available device in the fixed order (CQ12T, ADAM monitors, ...)`

- make the Mac use the mixer as sound output automatically (Audio Prefer)
- fix audio output after plugging the CQ12T (Audio Prefer)
- stop the Mac switching away from my speakers (Audio Prefer)

### [Controller Mapper (Mantra)](../apps/mix-ultra-mapper.md)

macOS; API: cli. Main call: `open -a "Controller Mapper (Mantra)" --args /path/layout.json`

Before: Controller Mapper (Mantra) opens a layout file per controller; its buttons are Accessibility ids off, top, close (press with STAR_API).

- map a new MIDI controller (Controller Mapper)
- record all controls of the Hercules DJControl Mix Ultra (Controller Mapper)
- create a layout for another DJ controller (Controller Mapper)

### [CQ Ethernet Bridge](../apps/CQ_ETHERNET_BRIDGE.md)

Android; API: adb. Main call: `adb shell am start -a android.settings.TETHER_SETTINGS # opens the phone's tethering page; switch on Ethernet tethering with the USB-LAN cable plugged in`

Before: Pixel phone with the USB-LAN cable to the CQ-12T, CQ MixPad installed on the phone. Tethering may switch off after unplug or reboot.

- control the CQ mixer by cable from the phone (CQ Ethernet Bridge)
- CQ MixPad cannot find the mixer (CQ Ethernet Bridge)
- keep internet on the phone while connected to the mixer (CQ Ethernet Bridge)

### [CQ MixPad (Mantra)](../apps/CQ_MIXPAD_MANTRA.md)

Android; API: none

- control the CQ12T from my phone (CQ MixPad)
- mix the concert from the Pixel (CQ MixPad)
- match the mixer EQ to a reference song (CQ MixPad)
- record multitrack from the CQ (CQ MixPad)

### [CQ MixPad Protocol](../apps/cq_mixpad_protocol.md)

macOS/Linux; API: cli. Main call: `tools/cq_inject.sh "f7 0c 0c 0d 00 00 56 5e" # sends raw hex to the desk through the sniffer started with: python3 tools/cq_mitm.py <desk-ip> --local`

Before: Start the man-in-the-middle sniffer first (python3 tools/cq_mitm.py `<desk-ip>` --local); the desk allows one client at a time, so the CQ MixPad app is used through it. Never test with Stereo Link, +48 V, sample rate or scene recall.

- control the Allen & Heath CQ mixer from code (CQ MixPad Protocol)
- what is the CQ-12T network protocol (CQ MixPad Protocol)
- set a CQ fader or mute over TCP (CQ MixPad Protocol)
- decode more CQ MixPad messages (CQ MixPad Protocol)

### [CQ MixPad Tutorial (Mantra)](../apps/cq_mixpad_tutorial.md)

macOS; API: cli. Main call: `build/start 6.2`

Before: Installed as a Mac app (Audio Mixing folder of the star menu); CQ MixPad must be open for the hand to click it. Hand click points depend on Live's full-screen layout.

- teach me the CQ-12T mixer (CQ MixPad Tutorial)
- learn mixing and gain staging with a guided course (CQ MixPad Tutorial)
- walk me through routing and USB recording on the mixer (CQ MixPad Tutorial)
- start lesson N of the mixer tutorial (CQ MixPad Tutorial) - call: `build/start 6`

### [CQ VESA Adapter](../apps/cq_vesa_adapter.md)

unknown; API: cli. Main call: `python3 drawings/make_drawings.py --measured`

Before: Needs the Python packages named in the repo; produces drawings, no network.

- mount the CQ-12T on a monitor arm (CQ VESA Adapter)
- VESA adapter for a mixer (CQ VESA Adapter)
- get cutting drawings for a mounting plate (CQ VESA Adapter)

### [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](../apps/MANTRA_CONTROLS.md)

macOS; API: none

- control the MIDI to keystroke mapper from a Mac window (Mantra Controls)
- switch MIDI detect on and off (Mantra Controls)
- edit MIDI mapping rows (Mantra Controls)

### [Mantra Mackie Control Translator](../apps/mantra-mackie-control-translator.md)

macOS/Hammerspoon; API: none

- control Ableton's timeline with a MIDI knob (Mantra Mackie Control Translator)
- make an OXI E16 knob scroll the arrangement (Mantra Mackie Control Translator)
- map MIDI CC to Mackie Control for Live (Mantra Mackie Control Translator)

### [MIDI to Key Stroke](../apps/MIDI_TO_KEYSTROKE.md)

macOS/Hammerspoon; API: http 8853. Main call: `curl -s 127.0.0.1:8853/health # the only documented route; the mappings are set in the app window`

Before: MIDI to Key Stroke must be running.

- map a MIDI knob to a keyboard shortcut (MIDI to Key Stroke)
- control Mac volume with a MIDI knob (MIDI to Key Stroke)
- trigger Ableton shortcuts from a controller (MIDI to Key Stroke)

### [MIDI Tools (Mantra)](../apps/MANTRA_MIDI_TOOLS.md)

macOS; API: none

- use a MIDI knob as a keyboard shortcut (MIDI Tools)
- control Ableton Live from a MIDI controller via Mackie Control (MIDI Tools)
- map MIDI to keystrokes on the Mac (MIDI Tools)

### [Oxi Controller (E16 Remote)](../apps/oxi-controller.md)

macOS; API: other. Main call: `echo 'turn 1 5' | nc -u 127.0.0.1 11010 (UDP test door; knob numbers are 1-based)`

Before: One of the two apps (Ableton Remote for OXI E16 or E16 for DaVinci Resolve) must be running; UDP 11010 is a test door (no HTTP /api). Knob numbers are 1-based.

- use the OXI E16 to control Ableton (Oxi Controller)
- knobs for DaVinci Resolve audio mixing (Oxi Controller) - call: `echo 'push 3' | nc -u -w1 127.0.0.1 11010 ; echo 'release 3' | nc -u -w1 127.0.0.1 11010`
- show Ableton values on the E16 screen (Oxi Controller)
- map an endless encoder to a Live parameter (Oxi Controller)

### [OXI-CQ Bridge](../apps/oxi_e16_cq-12t.md)

macOS; API: http 8753. Main call: `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'`

Before: Start the bridge first with ./run.sh in the repo (web UI on 127.0.0.1:8753); real MIDI needs the optional mido packages, the core needs only python3. Hardware paths are untested in the docs.

- control the CQ-12T mixer with the OXI E16 (OXI-CQ Bridge) - call: `curl -s 127.0.0.1:8753/api/state`
- set CQ fader levels from rotary knobs (OXI-CQ Bridge) - call: `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":1,"role":"push","value":127}'`
- test mixer control without hardware (OXI-CQ Bridge)

### [Plugin Assistant](../apps/PLUGIN_ASSISTANT.md)

macOS/Chrome; API: http 8873. Main call: `curl -X POST http://127.0.0.1:8873/on`

Before: Plugin Assistant (Mantra) running on 8873.

- put plug-ins on my microphone (Plugin Assistant)
- process the mic in the browser with AU effects (Plugin Assistant)
- vocal effects chain for lessons (Plugin Assistant)
- PatchWork-like mic rack (Plugin Assistant)

### [Sound Recorder (Mantra)](../apps/MANTRA_SOUND_RECORDER.md)

macOS; API: http 8869. Main call: `star fn "sound recorder" record.suno '{"out":"~/x.wav","url":"https://suno.com/song/<id>"}' # the song in Suno, start to end, auto stop, trimmed, as WAV`

Before: Sound Recorder (Mantra) v12+ running; its function door is port 8869, called through Star API (port 8863); Suno open in Firefox.

- record the sound of one app (Sound Recorder) - call: `star fn "sound recorder" record.app '{"bundle":"com.apple.Safari","out":"~/x.wav","seconds":30}'`
- record a song playing in Suno (Sound Recorder)
- record the microphone to a WAV (Sound Recorder)
- measure input level in dB (Sound Recorder)

### [Spectral Analyzer (Mantra)](../apps/SPECTRAL_ANALYZER.md)

macOS; API: cli. Main call: `SpectralAnalyzer --analyze song.wav take2.wav`

- check a master for clicks and loudness (Spectral Analyzer)
- see the spectrum of what the Mac plays (Spectral Analyzer)
- tune a voice to a piano note (Spectral Analyzer)

