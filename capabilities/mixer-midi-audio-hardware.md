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

- map Ableton tracks to the CQ12T mixer -> [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md) (macOS; API: none)
- sync two recordings of the same concert -> [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md) (macOS; API: none)
- use a MIDI knob as a Mackie control in Live -> [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md) (macOS; API: none)
- set the loop to the transients in Ableton -> [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md) (macOS; API: none)
- copy mixer channel names into Live -> [Ableton Live Actions (Mantra)](../apps/ABLETON_LIVE_ACTIONS.md) (macOS; API: none)
- show audio levels on my Android phone -> [AndroidVU](../apps/ANDROIDVU.md) (Android; API: none)
- find out if Android lets me read stream volume -> [AndroidVU](../apps/ANDROIDVU.md) (Android; API: none)
- VU meter overlay on the phone -> [AndroidVU](../apps/ANDROIDVU.md) (Android; API: none)
- make the Mac use the mixer as sound output automatically -> [Audio Prefer](../apps/audio-prefer.md) (macOS; API: cli) - call: `audio-prefer --once # sets the Mac's audio output to the first available device in the fixed order (CQ12T, ADAM monitors, ...)`
- fix audio output after plugging the CQ12T -> [Audio Prefer](../apps/audio-prefer.md) (macOS; API: cli)
- stop the Mac switching away from my speakers -> [Audio Prefer](../apps/audio-prefer.md) (macOS; API: cli)
- map a new MIDI controller -> [Controller Mapper (Mantra)](../apps/mix-ultra-mapper.md) (macOS; API: cli) - call: `open -a "Controller Mapper (Mantra)" --args /path/layout.json`
- record all controls of the Hercules DJControl Mix Ultra -> [Controller Mapper (Mantra)](../apps/mix-ultra-mapper.md) (macOS; API: cli)
- create a layout for another DJ controller -> [Controller Mapper (Mantra)](../apps/mix-ultra-mapper.md) (macOS; API: cli)
- control the CQ mixer by cable from the phone -> [CQ Ethernet Bridge](../apps/CQ_ETHERNET_BRIDGE.md) (Android; API: adb) - call: `adb shell am start -a android.settings.TETHER_SETTINGS # opens the phone's tethering page; switch on Ethernet tethering with the USB-LAN cable plugged in`
- CQ MixPad cannot find the mixer -> [CQ Ethernet Bridge](../apps/CQ_ETHERNET_BRIDGE.md) (Android; API: adb)
- keep internet on the phone while connected to the mixer -> [CQ Ethernet Bridge](../apps/CQ_ETHERNET_BRIDGE.md) (Android; API: adb)
- control the CQ12T from my phone -> [CQ MixPad (Mantra)](../apps/CQ_MIXPAD_MANTRA.md) (Android; API: none)
- mix the concert from the Pixel -> [CQ MixPad (Mantra)](../apps/CQ_MIXPAD_MANTRA.md) (Android; API: none)
- match the mixer EQ to a reference song -> [CQ MixPad (Mantra)](../apps/CQ_MIXPAD_MANTRA.md) (Android; API: none)
- record multitrack from the CQ -> [CQ MixPad (Mantra)](../apps/CQ_MIXPAD_MANTRA.md) (Android; API: none)
- control the Allen & Heath CQ mixer from code -> [CQ MixPad Protocol](../apps/cq_mixpad_protocol.md) (macOS/Linux; API: cli) - call: `tools/cq_inject.sh "f7 0c 0c 0d 00 00 56 5e" # sends raw hex to the desk through the sniffer started with: python3 tools/cq_mitm.py <desk-ip> --local`
- what is the CQ-12T network protocol -> [CQ MixPad Protocol](../apps/cq_mixpad_protocol.md) (macOS/Linux; API: cli)
- set a CQ fader or mute over TCP -> [CQ MixPad Protocol](../apps/cq_mixpad_protocol.md) (macOS/Linux; API: cli)
- decode more CQ MixPad messages -> [CQ MixPad Protocol](../apps/cq_mixpad_protocol.md) (macOS/Linux; API: cli)
- teach me the CQ-12T mixer -> [CQ MixPad Tutorial (Mantra)](../apps/cq_mixpad_tutorial.md) (macOS; API: cli) - call: `build/start 6.2`
- learn mixing and gain staging with a guided course -> [CQ MixPad Tutorial (Mantra)](../apps/cq_mixpad_tutorial.md) (macOS; API: cli)
- walk me through routing and USB recording on the mixer -> [CQ MixPad Tutorial (Mantra)](../apps/cq_mixpad_tutorial.md) (macOS; API: cli)
- start lesson N of the mixer tutorial -> [CQ MixPad Tutorial (Mantra)](../apps/cq_mixpad_tutorial.md) (macOS; API: cli)
- mount the CQ-12T on a monitor arm -> [CQ VESA Adapter](../apps/cq_vesa_adapter.md) (unknown; API: cli) - call: `python3 drawings/make_drawings.py --measured`
- VESA adapter for a mixer -> [CQ VESA Adapter](../apps/cq_vesa_adapter.md) (unknown; API: cli)
- get cutting drawings for a mounting plate -> [CQ VESA Adapter](../apps/cq_vesa_adapter.md) (unknown; API: cli)
- control the MIDI to keystroke mapper from a Mac window -> [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](../apps/MANTRA_CONTROLS.md) (macOS; API: none)
- switch MIDI detect on and off -> [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](../apps/MANTRA_CONTROLS.md) (macOS; API: none)
- edit MIDI mapping rows -> [Mantra Controls (MIDI to Key Stroke / MIDI to MK Control)](../apps/MANTRA_CONTROLS.md) (macOS; API: none)
- control Ableton's timeline with a MIDI knob -> [Mantra Mackie Control Translator](../apps/mantra-mackie-control-translator.md) (macOS/Hammerspoon; API: none)
- make an OXI E16 knob scroll the arrangement -> [Mantra Mackie Control Translator](../apps/mantra-mackie-control-translator.md) (macOS/Hammerspoon; API: none)
- map MIDI CC to Mackie Control for Live -> [Mantra Mackie Control Translator](../apps/mantra-mackie-control-translator.md) (macOS/Hammerspoon; API: none)
- map a MIDI knob to a keyboard shortcut -> [MIDI to Key Stroke](../apps/MIDI_TO_KEYSTROKE.md) (macOS/Hammerspoon; API: http 8853) - call: `curl -s 127.0.0.1:8853/health # the only documented route; the mappings are set in the app window`
- control Mac volume with a MIDI knob -> [MIDI to Key Stroke](../apps/MIDI_TO_KEYSTROKE.md) (macOS/Hammerspoon; API: http 8853)
- trigger Ableton shortcuts from a controller -> [MIDI to Key Stroke](../apps/MIDI_TO_KEYSTROKE.md) (macOS/Hammerspoon; API: http 8853)
- use a MIDI knob as a keyboard shortcut -> [MIDI Tools (Mantra)](../apps/MANTRA_MIDI_TOOLS.md) (macOS; API: none)
- control Ableton Live from a MIDI controller via Mackie Control -> [MIDI Tools (Mantra)](../apps/MANTRA_MIDI_TOOLS.md) (macOS; API: none)
- map MIDI to keystrokes on the Mac -> [MIDI Tools (Mantra)](../apps/MANTRA_MIDI_TOOLS.md) (macOS; API: none)
- use the OXI E16 to control Ableton -> [Oxi Controller (E16 Remote)](../apps/oxi-controller.md) (macOS; API: other) - call: `echo 'turn 1 5' | nc -u 127.0.0.1 11010 (UDP test door; knob numbers are 1-based)`
- knobs for DaVinci Resolve audio mixing -> [Oxi Controller (E16 Remote)](../apps/oxi-controller.md) (macOS; API: other)
- show Ableton values on the E16 screen -> [Oxi Controller (E16 Remote)](../apps/oxi-controller.md) (macOS; API: other)
- map an endless encoder to a Live parameter -> [Oxi Controller (E16 Remote)](../apps/oxi-controller.md) (macOS; API: other)
- control the CQ-12T mixer with the OXI E16 -> [OXI-CQ Bridge](../apps/oxi_e16_cq-12t.md) (macOS; API: http 8753) - call: `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'`
- set CQ fader levels from rotary knobs -> [OXI-CQ Bridge](../apps/oxi_e16_cq-12t.md) (macOS; API: http 8753)
- test mixer control without hardware -> [OXI-CQ Bridge](../apps/oxi_e16_cq-12t.md) (macOS; API: http 8753)
- put plug-ins on my microphone -> [Plugin Assistant](../apps/PLUGIN_ASSISTANT.md) (macOS/Chrome; API: http 8873) - call: `curl -X POST http://127.0.0.1:8873/on`
- process the mic in the browser with AU effects -> [Plugin Assistant](../apps/PLUGIN_ASSISTANT.md) (macOS/Chrome; API: http 8873)
- vocal effects chain for lessons -> [Plugin Assistant](../apps/PLUGIN_ASSISTANT.md) (macOS/Chrome; API: http 8873)
- PatchWork-like mic rack -> [Plugin Assistant](../apps/PLUGIN_ASSISTANT.md) (macOS/Chrome; API: http 8873)
- record the sound of one app -> [Sound Recorder (Mantra)](../apps/MANTRA_SOUND_RECORDER.md) (macOS; API: http 8869) - call: `star fn "sound recorder" record.suno '{"out":"~/x.wav","url":"https://suno.com/song/<id>"}' # the song in Suno, start to end, auto stop, trimmed, as WAV`
- record a song playing in Suno -> [Sound Recorder (Mantra)](../apps/MANTRA_SOUND_RECORDER.md) (macOS; API: http 8869)
- record the microphone to a WAV -> [Sound Recorder (Mantra)](../apps/MANTRA_SOUND_RECORDER.md) (macOS; API: http 8869)
- measure input level in dB -> [Sound Recorder (Mantra)](../apps/MANTRA_SOUND_RECORDER.md) (macOS; API: http 8869)
- check a master for clicks and loudness -> [Spectral Analyzer (Mantra)](../apps/SPECTRAL_ANALYZER.md) (macOS; API: cli) - call: `SpectralAnalyzer --analyze song.wav take2.wav`
- see the spectrum of what the Mac plays -> [Spectral Analyzer (Mantra)](../apps/SPECTRAL_ANALYZER.md) (macOS; API: cli)
- tune a voice to a piano note -> [Spectral Analyzer (Mantra)](../apps/SPECTRAL_ANALYZER.md) (macOS; API: cli)
