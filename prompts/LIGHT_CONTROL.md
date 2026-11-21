# Kickoff prompt: Light Control (Mantra)

Paste the whole box below as the first message of a new Claude Code session opened on a new, empty
repository named `LIGHT_CONTROL`. Written 21.11.2026 from Marko's dictation and from the research
listed at the end of the box.

```text
NEW APP: "Light Control (Mantra)"  (Marko also calls it "Mantra Neewer")
Repository: markoboskoauroville/LIGHT_CONTROL (new, empty). App id: light-control.

=====================================================================
0. HOW THIS SESSION WORKS  (read before anything else)
=====================================================================
- You are the planner. Clone markoboskoauroville/MANTRA_MANIFEST, read START_HERE.md and the files it
  names as "always", then modules/fable-plans-and-scores.md and modules/workers-right-model.md.
  Fable only plans, briefs and scores. Workers (Agent tool, background) on Haiku, Sonnet or Opus do all
  the building, testing and documents, always on a model lower than yours, the cheapest that does the
  job. You score the REAL result out of 10 and send numbered corrections to the same worker until it
  is 10 of 10. You never write the app's code yourself.
- Then clone markoboskoauroville/APPS_MIND_MAP and read README.md, CAPABILITIES.md and MODULES.md.
  That repository is the map of every app and reusable module Marko already has. Before any part of
  this app is written, look there for an app to call or code to copy. Reuse first, write second.
- When the app is built, add its card to APPS_MIND_MAP (apps/LIGHT_CONTROL.md, data/apps.json,
  CAPABILITIES.md, CONNECTIONS.md) and push it. An app that is not on the map is not finished.
- Write Marko's words (section 1) word for word into momentaryupdates.md before the plan.
- One branch, main. Compiled only by a GitHub workflow copied from the manifest's workflows/
  (mac-swift.yml). Apple Silicon arm64 only. Signed "Mantra Apps". Whole-number versions, the version
  visible in the window, update-at-start kit, release marked Latest. Repository documents: TAKEOVER.md,
  LESSONS.md, momentaryupdates.md. Follow modules/swift-apps.md, workflow-interface.md,
  mantra-design-language.md, simple-first.md, one-title-only.md, no-on-off-button.md, secrets.md,
  repo-privacy.md, device-under-camera.md, marko-tests.md, four-tests.md, delivery-gate.md.
  Where two manifest rules disagree, the newest dated one wins.

=====================================================================
1. WHAT MARKO ASKED FOR  (his words, dictated 21.11.2026)
=====================================================================
"I have LED light, which has Bluetooth control, it's from Neewer. I was buying it from Amazon. And I'm
going to put one camera in front, one behind. The one in front will be Sony Alpha 7 V. And it needs to
be controlled over USB so it can adjust exposure to the right amount, color temperature to the right
amount, to be able to map all the functions of this light. We create our own light control app which is
better than original and it has more refined transitions between colors. They all have backdoor API,
Python. So Claude Code or any other code can ask the app your commands. It gives the commands and then
it can be controlled by other apps. This is how we build the whole ecosystem.

We have something we call webcam recorder which can call remote controller from Sony and then while
building there can be prompt for me, Marko, to say: please connect your Sony to USB, enable USB remote
control. And then the process starts.

We will be able to control it in a way I like. And the way I like it is to reproduce Alpha waves, Theta
waves and be connected for example with my Mantra Room application which creates sound for relaxation.
And then this app is also controlled by that app so it can create mood in a room by changing the light
colors. And the opposite way: Mantra Room needs to have microphone and then it can use the
visualization on the screen to adjust to the ambient sound. I'm going to play gong for example and then
MilkDrop will show the gong visualization. At the same time the MilkDrop colors and how it behaves is
going to trigger the light to pulsate in certain colors, but everything going very slowly."

=====================================================================
2. THE APP IN ONE PARAGRAPH
=====================================================================
A Mac app (Swift, menu bar item plus one window) that finds the Neewer light over Bluetooth LE, exposes
every function the light has, and adds what the original phone app lacks: transitions that are smooth
to the eye, a calibration of the light measured through the Sony A7 V over USB, a local HTTP API so any
other app or AI can drive it, slow brainwave-paced breathing of light, and two-way links with
Meditation Room (Mantra) so sound, on-screen visualization and room light move as one.

=====================================================================
3. FIRST QUESTIONS AND FIRST PROBES  (before any design is fixed)
=====================================================================
3.1 Which light. Not confirmed. The manifest's modules/shopping.md has "NEEWER RGB62 with Improved App
    Control" (2500-8500K, RGB, OLED, phone app) put in the Amazon basket on 13.11.2026; no order mail
    was found. Do not ask Marko for the model if a probe can answer: the first tool a worker builds is
    a BLE scanner (tools/blescan) that lists nearby peripherals with name, advertised services and
    manufacturer data, and dumps the GATT table of anything named NEEWER / NW- / NWR. Ask Marko, by
    voice (manifest modules/marko-tests.md), only to switch the light on and put it near the Mac.
    Record the result in docs/LIGHT.md: model, advertised name, protocol variant, real CCT range,
    whether it has RGB/HSI, GM tint, scenes, battery report.
3.2 How many lights. Build for N lights from the start (groups, per-light calibration), even if there is
    one today.
3.3 The second camera ("one behind"): ask Marko which body after the first working version. Design the
    camera layer so a second camera is a second instance, not a rewrite.

=====================================================================
4. HARDWARE FACTS ALREADY KNOWN  (verify each on the real device; sources at the end)
=====================================================================
NEEWER BLUETOOTH LE
- Classic protocol: service 69400001-B5A3-F393-E0A9-E50E24DCCA99, write characteristic 69400002-...,
  notify characteristic 69400003-.... Packet = 0x78, command tag, payload length, payload, checksum
  (sum of all previous bytes & 0xFF).
  Power 0x81 (payload 01 on / 02 off). CCT 0x87 (brightness 0-100, temperature in K/100; some models
  add a GM byte). HSI 0x86 (hue 16-bit little-endian 0-360, saturation 0-100, intensity 0-100).
  Scene 0x88. Status reads: 78 85 00 FD (power), 78 84 00 FC (channel).
- "Infinity" protocol (newer lights): same 0x78 prefix, tags 0x8D power, 0x8F HSI, 0x90 CCT, 0x91 scene,
  with the light's 6-byte MAC inside the packet. CoreBluetooth does not expose the MAC: obtain it from
  the advertised name / manufacturer data, from system_profiler SPBluetoothDataType, or once from Marko,
  and store it per light. Byte order after the MAC is unverified: capture and confirm on the device.
- Open-source references, both MIT (reuse allowed, keep the notice): keefo/NeewerLite (Swift, macOS;
  has a per-model capability table) and taburineagle/NeewerLite-Python. Copy the model table and the
  packet builders with attribution rather than rediscovering them.
- No published rate limit. Start at 10-15 packets per second, write-without-response, newest value
  wins (never queue stale colours). Measure the real limit on the device and write it down.
- Known traps: two byte examples in the public RGB660 notes contradict each other; brightness and
  temperature are quantised (1 % and 100 K steps), so slow fades show steps unless dithered (5.3).

SONY ALPHA 7 V  (ILCE-7M5, USB id 054c:0f56)
- Control is USB PTP on the camera's fast upper port (PORT 1) with
  MENU > Setup > USB > USB Cnct Mode (PORT1) = Remote Shoot/Trn. The A7 V has no "PC Remote" menu name.
- One program owns the USB interface at a time. Sony Imaging Edge Remote must be closed first.
  While the camera is in USB Streaming (UVC) it gives a picture but no PTP control at all, and Wi-Fi and
  Bluetooth remote are off. A phone connected to the camera blocks control from a computer.
- Marko's existing code already talks to this camera: WEB_CAM_VIEWER ("Webcam Recorder (Mantra)", Mac,
  ImageCaptureCore over USB, a five-stage Sony connection check, status at 127.0.0.1:8867
  /sony/status?check=1), sony_remote_controller (Android, PTP handshake and vendor properties for time
  code: 0xD0D3, 0xD0D6, 0xD0D7), MACRO_SKILLS tools/sonycam (drives Imaging Edge Remote by
  Accessibility). None of them reads or sets exposure, ISO or white balance yet: that is new work here.
- Two routes to exposure and white balance, to be decided by a spike (5.4):
  (a) Sony Camera Remote SDK: lists ILCE-7M5 from version 2.01.00; reads and sets shutter, aperture,
      ISO, exposure compensation, white-balance mode, colour temperature in Kelvin, tint, and gives
      live-view frames. Not yet verified: an Apple Silicon build, the redistribution terms (it may not
      be allowed in a public repository), the exact A7 V property list.
  (b) Sony vendor PTP properties through ImageCaptureCore, extending the handshake Marko already has.
  Choose (b) if the properties are reachable, because the code and its licence are already his.

=====================================================================
5. WHAT TO BUILD
=====================================================================
5.1 LIGHT ENGINE  (module LightKit, no UI, reusable by any other app)
- Discover, connect, reconnect by itself, several lights, groups.
- A capability model per light read from the model table and confirmed by probing: CCT range, GM tint,
  HSI/RGB, scenes, battery, protocol variant. The UI and the API show only what the light can do.
- Every function of the original app mapped: power, brightness, CCT, GM, HSI, RGB, every built-in scene
  with its parameters, plus anything the probe finds. docs/FUNCTION_MAP.md lists each function, its
  packet, and "verified on device: yes/no". Nothing is marked done that was not seen on the device.
- State read back from the light where the protocol allows, so the app never shows a guess as a fact.

5.2 COLOUR MODEL
- One internal colour, device independent (CIE xy + luminance, or OKLCH), converted to the light's
  CCT+GM or HSI command through the calibration of 5.5. Presets and other apps speak in Kelvin, in
  hex/RGB, in hue/saturation, and in Marko's chakra colours (manifest modules/chakra-colors.md, the
  version of 10.11.2026).

5.3 TRANSITION ENGINE  (the reason this app exists: "more refined transitions between colors")
- Every change is a ramp, never a jump (manifest modules/the-ramp.md). Interpolate in a perceptual
  space (OKLab), with brightness on a perceptual curve, not linear in the light's percent.
- Durations from 0.2 s to 60 minutes; easings (linear, ease-in-out, exponential, breathing).
- Temporal dithering between adjacent quantised steps so a one-hour sunset shows no visible stepping,
  within the packet rate measured in section 4.
- A new target arriving mid-fade bends the current fade; it never restarts from the old colour and
  never flashes.
- Scenes are timelines of keyframes (colour, time, easing), loopable, saved as JSON, shareable.

5.4 CAMERA LINK  (module CameraKit)
- Connection assistant, the same pattern as Webcam Recorder's Sony check: stages shown one by one, and
  when Marko's hand is needed the app says it in a sentence and waits, for example
  "Connect the Sony to the Mac with USB (upper port) and set USB Cnct Mode to Remote Shoot/Trn."
  The message disappears by itself when the camera answers. If Webcam Recorder (Mantra) or Imaging Edge
  Remote holds the camera, say which one and offer the one button that releases it. Before asking
  Marko anything, check the real state (manifest modules/check-before-asking.md).
- Read: shutter, aperture, ISO, exposure compensation, metering/exposure indicator, white-balance mode,
  Kelvin, tint, and live-view frames. Set: ISO, shutter, white-balance mode, Kelvin, tint.
- A spike first, one worker, one day: prove on the real A7 V which route of section 4 reads and sets
  these. Write the result into docs/CAMERA.md and into the manifest (a new module sony-exposure-wb.md).

5.5 CALIBRATION  ("adjust exposure to the right amount, color temperature to the right amount")
- With the camera on fixed manual exposure and fixed white balance, pointed at a grey card (ask Marko
  to place it; mark the region on the live view once), step the light through its brightness and CCT
  range and through the hue circle, and measure what the sensor sees: luminance and chromaticity.
- Result: per light, a table "asked for vs delivered" for intensity (percent to relative stops) and for
  colour (asked Kelvin to measured Kelvin and tint; hue to measured hue). Saved as JSON beside the
  light's record, used by 5.2 so that "5600 K at one stop less" is really that.
- Two-way match: "match camera to light" sets the camera's Kelvin and tint to the light;
  "match light to camera" sets the light so a grey card is neutral at the camera's current setting.
- "Hold exposure": while the light changes colour or level, keep the camera's exposure of the subject
  constant by trimming the light's intensity first and the camera's ISO second.
- A second camera (behind) is calibrated the same way and stored separately.

5.6 BRAINWAVE MODES  (alpha, theta) - SAFETY IS PART OF THE FEATURE
- Flashing between 3 and 30 Hz can provoke seizures; alpha (8-12 Hz) and theta (4-7 Hz) are inside
  that band. The app therefore never strobes. A brainwave rhythm is rendered in one of two ways:
  (a) as a slow breathing envelope tied to the rhythm by ratio (for example one breath of light per
      64 alpha cycles), or
  (b) as a shallow modulation of at most a few percent of luminance around a steady level, no red
      saturated flicker, depth and rate limited in code.
  The limiter lives in LightKit, below the API, so no caller, no scene and no other app can exceed it.
  The limits are constants with a test that pins them. The first use shows a one-time plain warning.
- Presets: Alpha rest, Theta drift, Sunset, Dawn, Candle, each a timeline of 5.3.
- The same clock can be shared with Meditation Room's sound (binaural or isochronic beat) so light and
  sound keep one phase (5.8).

5.7 THE API  (the backdoor: nothing is finished without it; manifest modules/remote-door.md, ports.md)
- 127.0.0.1 only, port claimed through MANTRA_PORTS under id light-control (take the number from
  mantra-ports next; never hardcode). GET /health, GET /api (every action with a "does" sentence and
  its arguments), POST /api/<action>, GET /api/state. Answers in under a second; long work answers
  "started" and reports progress in /api/state.
- Actions at least: lights, connect, power, set (kelvin | hex | hsi | chakra, brightness, seconds,
  easing, light or group), fade, scene-play, scene-stop, scene-list, scene-save, brainwave (mode,
  minutes), follow (source: meditation-room | milkdrop | audio | none), frame (a small picture or a
  list of colours, one per light: the same idea as G815 Lights' POST /frame), calibrate, camera-status,
  camera-set, match (camera-to-light | light-to-camera), stop.
- A stream endpoint for sources that send colours continuously (WebSocket or a TCP stream like G815
  Lights' 8878), rate limited and smoothed by the transition engine.
- Python: reachable through the manifest's mantra_remote.py (remote.call("light-control", "set",
  kelvin=3200, brightness=40, seconds=20)) and a one-file client tools/lightctl.py with the same verbs
  on the command line. Registered with Mantra Door so the phone can drive it.
- Every control in the window is an Accessibility button so Queen and Macro Recorder can press it;
  a Queen skill and route are written and tested (manifest modules/teach-queen.md).

5.8 MEDITATION ROOM LINK, BOTH DIRECTIONS  (repo MANTRA_ROOM, app id meditation-room, port 8965)
- Room drives light: Meditation Room already has a "lights" action and drives the Logitech G815
  keyboard. Add Light Control as a second light target there: when a loop or a style starts, Meditation
  Room calls light-control (scene or follow). This part is a change in MANTRA_ROOM, made by a worker in
  that repository, on main, with its tests.
- Light follows the picture: a "follow" source that takes dominant colours from the visualization and
  turns them into slow light. Sample the rendered frame small (for example 16x9), take 1-3 dominant
  colours, low-pass them hard (time constants of several seconds, Marko: "everything going very
  slowly"), map to the lights, pass through the limiter of 5.6.
- Upgrade asked for Meditation Room itself (a second work item, in MANTRA_ROOM): a microphone input,
  so the visualization reacts to the room's sound (a gong, a bowl) and not only to the track it plays.
  Meditation Room ALREADY has the MilkDrop visualization: butterchurn (MIT) with 100 presets, vendored
  at android/app/src/main/assets/web/vendor/butterchurn.min.js, and on the Mac mac/app/Lights.swift
  already turns the picture into colours for the G815 keyboard. Do not add a second visualizer: feed
  the existing one from the microphone (a source switch: track | microphone | both), and reuse the
  Lights.swift sampling for the colours. The visualization publishes its dominant colours on
  Meditation Room's API (/api/state and a stream), and Light Control subscribes.
  Microphone permission handled the manifest way (amber PERMISSIONS while missing). The Android app
  has no INTERNET permission today; keep that, the microphone needs none.
- Only one painter drives the G815 at a time; Light Control never writes to the keyboard itself, it
  goes through G815 Lights' own API if the keyboard should follow the same scene.
- Chain to prove at the end: gong struck in the room -> microphone -> visualization moves ->
  colours published -> light breathes in those colours, slowly, with no flash.

5.9 THE WINDOW  (simple first)
- Menu bar item with the hover card kit (manifest kits/menubar-hover): light name, colour now, battery.
- One window, numbered steps as the manifest's workflow-interface asks: 1 Light (found, connected,
  battery), 2 Colour (Kelvin/tint, hue/saturation, brightness, chakra row), 3 Scenes (the timelines),
  4 Camera (connection stages, live view with the grey-card region, calibrate, match), 5 Links
  (Meditation Room, follow source, API address). One title only, version visible, no ON/OFF button,
  nothing cut at the minimum width, landscape "camera" language of the manifest for the instruments.
- Six-letter icon, a row in the star menu.

=====================================================================
6. ORDER OF WORK  (each step is a worker's brief; score each before the next)
=====================================================================
1. Probe: tools/blescan, identify the light, capture its packets, docs/LIGHT.md.        (Sonnet)
2. LightKit: protocol, capability model, reconnect; unit tests on packet bytes against captured
   truth; a fake light for CI.                                                            (Sonnet)
3. Transition engine with the limiter; tests that pin smoothness, rate and the safety limits. (Opus)
4. API + lightctl.py + MANTRA_PORTS + Mantra Door registration. From here every later test drives
   the app through the API, not through the mouse.                                        (Sonnet)
5. Window and menu bar item.                                                              (Sonnet)
6. Camera spike on the real A7 V, then CameraKit.                                         (Opus)
7. Calibration and the two-way match.                                                     (Opus)
8. Brainwave presets and scenes.                                                          (Sonnet)
9. MANTRA_ROOM changes: light target, microphone, visualization, colour publishing.       (Opus)
10. Follow mode and the gong chain test.                                                  (Sonnet)
11. Documents, Queen skill, star row, APPS_MIND_MAP card, manifest write-back
    (new modules: neewer-ble.md, sony-exposure-wb.md, light-safety.md).                   (Haiku/Sonnet)

=====================================================================
7. HOW IT IS PROVEN  (independent truth, not the app's own word)
=====================================================================
- Packets: bytes compared with captures from the real light and with the two MIT references.
- The light really did it: the Sony (or the Pixel under the manifest's device-under-camera method)
  films the light; a script measures colour and level in the frames. A fade is smooth when no frame-to-
  frame step exceeds the threshold written in the test.
- Calibration: after calibrating, ask for five Kelvin values and three levels; the camera's
  measurement must match within the tolerance written in docs/CALIBRATION.md.
- Safety: a test drives every API action and every scene with hostile values and shows the output
  never modulates between 3 and 30 Hz above the allowed depth.
- API: a script calls every action listed by /api and checks /api/state.
- What only Marko can judge (the feel of a fade, the mood in the room) is asked of him after the
  10 of 10, by voice, one thing at a time.

=====================================================================
8. NOT IN VERSION 1
=====================================================================
DMX, lights of other brands, an Android version, cloud control. Keep LightKit's device layer behind a
protocol so a second brand (the Aputure MC Marko also owns) can be added later without touching the
transition engine or the API.

=====================================================================
9. SOURCES USED FOR THIS PROMPT  (re-check anything marked unverified on the device)
=====================================================================
- MANTRA_MANIFEST modules: remote-door, ports, keyboard-lights, logitech-g815, chakra-colors,
  sony-alpha-settings, sony-remote-wifi, the-ramp, shopping, swift-apps, fable-plans-and-scores.
- Repositories: MANTRA_ROOM, G815_LIGHTS, WEB_CAM_VIEWER, sony_remote_controller, MACRO_SKILLS.
- github.com/keefo/NeewerLite and github.com/taburineagle/NeewerLite-Python (both MIT).
- Sony Camera Remote SDK pages (ILCE-7M5 listed from 2.01.00; arm64 build and licence unverified).
- Epilepsy Society, Epilepsy Foundation, ITU-R BT.1702 on flashing light (3-30 Hz).
- Butterchurn (MIT) and projectM (LGPL-2.1).
```
