[Back to the index](../CAPABILITIES.md)

# Camera, video, NDI and streaming

## Which one to pick: Sony cameras: record, REC, settings, time code, live view, phone remote

Four different things are called 'record the Sony', and each has its own app. Recording the picture to the Mac disk is Webcam Recorder (web-cam-viewer, port 8867); starting REC on the camera's own card is Sony Remote (SONY_REMOTE_MAC, port 8881) or, through Imaging Edge Remote and Accessibility, `sonycam` in MACRO_SKILLS. Only one program can hold the camera's USB at a time (Imaging Edge Remote locks it, so Webcam Recorder asks for TAKE CONTROL), and a camera streaming over USB (UVC) cannot also be controlled over that cable. ISO and shutter through Webcam Recorder (`/sony/set`) are written in the code but were not verified against a real body at v27. Time code jam and Bluetooth REC for several Sonys are the Android app, not the Mac apps.

| You want | Use | How |
|---|---|---|
| record the Sony picture to a file on the Mac disk (H.265 .mov with time code) | [Webcam Recorder (Mantra) (web-cam-viewer)](../apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/record/start -H 'Content-Type: application/json' -d '{"name":"interview"}'` |
| stop that recording and get the file path | [Webcam Recorder (Mantra) (web-cam-viewer)](../apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/record/stop` |
| start REC on the camera's own card from the Mac | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](../apps/SONY_REMOTE_MAC.md) | `curl -s -XPOST 127.0.0.1:8881/connect ; curl -s 127.0.0.1:8881/start` |
| start REC on the card through Imaging Edge Remote (Accessibility), also used by the Second Take guide | [Macro Skills (MACRO_SKILLS)](../apps/MACRO_SKILLS.md) | `tools/sonycam start` |
| set ISO or shutter on a connected Sony (needs /sony/connect and /sony/takecontrol first; not verified against the body) | [Webcam Recorder (Mantra) (web-cam-viewer)](../apps/web-cam-viewer.md) | `curl -s -XPOST 127.0.0.1:8867/sony/set -H 'Content-Type: application/json' -d '{"name":"ISO","label":"ISO 800"}'` |
| jam time code into a Sony body over USB, or REC on several Sonys over Bluetooth (Android) | [Mantra Sony Remote (TC Jam), Android (sony_remote_controller)](../apps/sony_remote_controller.md) | `adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --es tc 12:00:00:00` |
| see a live-view frame of the Sony as a picture | [Sony Remote (Mantra), Mac (SONY_REMOTE_MAC)](../apps/SONY_REMOTE_MAC.md) | `curl -s 127.0.0.1:8881/frame.jpg -o live.jpg` |
| use the phone as a remote for the Mac shooting guide (watch, record, stop, next take) | [Second Take Remote (SECOND_TAKE_REMOTE)](../apps/SECOND_TAKE_REMOTE.md) |  |
| use a Pixel phone as a manual camera with exposure, white balance and NDI (this is the phone's own camera, not a Sony) | [Mantra Manual Camera (mantra-manual-camera)](../apps/mantra-manual-camera.md) | `scripts/mcam iso 400` |

### [CineView Viewer](../apps/CINEVIEW_VIEWER.md)

macOS; API: none

- view the Accsoon CineView Nano picture on the Mac (CineView Viewer)
- watch the wireless video monitor without the vendor app (CineView Viewer)

### [Cloud Mixer](../apps/CLOUD_MIXER.md)

Linux/Cloud; API: http 8841. Main call: `curl -s 127.0.0.1:8841/load -d '{"src":"/srv/cloud-mixer/media/x.mp4","id":"cam1","start":300}'`

Before: Runs on chromium-vm (port 8841 there, not on the Mac); reach it from the VM or over Tailscale.

- stream a recorded concert as a live show (Cloud Mixer)
- switch between cameras in the cloud (Cloud Mixer)
- put a lower-third text on the stream (Cloud Mixer)
- schedule a show to start at noon (Cloud Mixer)

### [Mantra Manual Camera](../apps/mantra-manual-camera.md)

macOS/Android; API: adb. Main call: `scripts/mcam iso 400`

Before: Needs the Pixel 7 on adb (cable, or wireless debugging; MCAM_SERIAL overrides) with the camera app open or openable and Settings, MORE, ADB CONTROL on (default on from v144); run from a checkout of the repo (scripts/mcam).

- use my phone as a manual camera (Mantra Manual Camera)
- stream the phone camera to OBS or vMix over NDI (Mantra Manual Camera)
- set ISO, shutter, white balance on the phone by command (Mantra Manual Camera) - call: `scripts/mcam wb 4500 ; scripts/mcam shutter 1/50 ; scripts/mcam focus 0.5`
- record a take with log curve on Android (Mantra Manual Camera)
- start all Sony cameras recording with the phone (Mantra Manual Camera)
- go live from the phone to my website (Mantra Manual Camera)

### [Mantra NDI Screen Share (Android)](../apps/mantra-ndi-screen-share-android.md)

Android; API: none

- mirror my Android screen to OBS over NDI (Mantra NDI Screen Share)
- show the phone screen in vMix (Mantra NDI Screen Share)
- stream Android screen as NDI (Mantra NDI Screen Share)

### [Mantra NDI SDK (private vendor files)](../apps/mantra-ndi-sdk.md)

Android/Cloud; API: none

- build the Android NDI app (Mantra NDI SDK)
- where are the NDI SDK headers for Android (Mantra NDI SDK)

### [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md)

Android; API: adb. Main call: `adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --es tc 12:00:00:00`

Before: Phone on adb; the camera body on USB for TC Jam. Android app with Bluetooth REC remote and time code jam.

- sync time code on my Sony cameras (Mantra Sony Remote, Android)
- start recording on all Sony cameras at once (Mantra Sony Remote, Android)
- jam timecode from the phone to a Sony A7 (Mantra Sony Remote, Android)
- clap sync for multi-camera shoot (Mantra Sony Remote, Android)
- Sony Alpha Android remote (Mantra Sony Remote, Android)

### [NDI Mantra Monitor](../apps/ndi-mantra-monitor.md)

macOS; API: none

- watch an NDI stream on the Mac (NDI Mantra Monitor)
- monitor the phone's NDI camera on the desktop (NDI Mantra Monitor)
- view an NDI source in a window (NDI Mantra Monitor)

### [obs2vmix](../apps/obs2vmix.md)

macOS; API: none

- vMix-like switcher on Mac (obs2vmix)
- OBS with a vMix look (obs2vmix)
- build the obs2vmix DMG (obs2vmix)

### [Skeleton (Mantra)](../apps/SKELETON.md)

macOS/Android; API: cli. Main call: `open -a "Skeleton (Mantra)" --args --camera ILCE-7M5 # the skeleton of the picture from the named camera`

- follow me with a skeleton on camera (Skeleton)
- check my yoga pose against a target (Skeleton)
- multi-camera body tracking (Skeleton)
- use the Pixel as a pose camera (Skeleton)

### [Sony Remote (Mantra), Mac](../apps/SONY_REMOTE_MAC.md)

macOS; API: http 8881. Main call: `curl -s 127.0.0.1:8881/start`

Before: The camera must be connected first: curl -s -XPOST 127.0.0.1:8881/connect (finds the camera, uses the saved user and password; poll GET /status until connected); /start answers 409 'not connected' otherwise.

- start and stop recording on the Sony from the Mac (Sony Remote, Mac)
- record the Sony to its card remotely (Sony Remote, Mac)
- Sony alpha remote record button (Sony Remote, Mac)
- grab a live view frame from the Sony (Sony Remote, Mac)

### [Sound Link (Mantra)](../apps/SOUND_LINK.md)

macOS/Android; API: http 8974. Main call: `curl -s -XPOST 127.0.0.1:8974/fn/source -d '{"device":"BlackHole","pair":1}'`

Before: Sound Link (Mantra) must be running; functions are registered for Star API (star fn "sound link"). Not yet proven end to end.

- send mixer audio to the camera (Sound Link) - call: `curl -s -XPOST 127.0.0.1:8974/fn/devices`
- sync desk sound with the phone camera (Sound Link)
- stream NDI camera plus mixer sound (Sound Link)
- Mac audio to Android over Wi-Fi (Sound Link)

### [Streaming Dashboard (Mantra)](../apps/STREAMING_DASHBOARD.md)

macOS/Linux/Cloud; API: door 8996. Main call: `curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"go-live","minutes":15}'`

Before: Runs on the VM (listens on the VM's Tailscale address and loopback); the token header is needed off the VM. Go-live is blocked 11:50-13:50 Zagreb time and when the site is already live.

- is my live stream working (Streaming Dashboard)
- check the streaming chain (Streaming Dashboard)
- start the test stream and go live (Streaming Dashboard)
- how many viewers are watching (Streaming Dashboard)

### [Virtual Cam (Mantra)](../apps/mantra_virtual_cam.md)

macOS/Android; API: other. Main call: `open -g mantravirtualcam://webcam/<name> # the phone camera becomes the Mac webcam (shown as OBS Virtual Camera)`

Before: Needs Mantra Manual Camera v161+ on the phone; the camera app must be in front for direct Wi-Fi.

- use my phone camera as a webcam on the Mac (Virtual Cam)
- control the Mantra Manual Camera from the Mac (Virtual Cam)
- use several phone cameras in OBS (Virtual Cam)

### [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md)

macOS; API: http 8867. Main call: `curl -s -XPOST 127.0.0.1:8867/record/start -H 'Content-Type: application/json' -d '{"name":"interview"}'`

Before: To control a Sony body (ISO, shutter, REC) call POST /sony/connect, then POST /sony/takecontrol (closes Imaging Edge Remote and takes the USB; the owner's explicit decision), before /sony/set or /sony/rec.

- record the Sony camera to disk on the Mac (Webcam Recorder) - call: `curl -s -XPOST 127.0.0.1:8867/sony/set -H 'Content-Type: application/json' -d '{"name":"ISO","label":"ISO 800"}'`
- record a webcam or capture card with sound (Webcam Recorder)
- start and stop recording by command (Webcam Recorder) - call: `curl -s -XPOST 127.0.0.1:8867/record/stop`
- check which cameras the Mac sees (Webcam Recorder)
- set ISO or shutter on the Sony from the Mac (Webcam Recorder)

