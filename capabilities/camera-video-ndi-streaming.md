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

- view the Accsoon CineView Nano picture on the Mac -> [CineView Viewer](../apps/CINEVIEW_VIEWER.md) (macOS; API: none)
- watch the wireless video monitor without the vendor app -> [CineView Viewer](../apps/CINEVIEW_VIEWER.md) (macOS; API: none)
- stream a recorded concert as a live show -> [Cloud Mixer](../apps/CLOUD_MIXER.md) (Linux/Cloud; API: http 8841) - call: `curl -s 127.0.0.1:8841/load -d '{"src":"/srv/cloud-mixer/media/x.mp4","id":"cam1","start":300}'`
- switch between cameras in the cloud -> [Cloud Mixer](../apps/CLOUD_MIXER.md) (Linux/Cloud; API: http 8841)
- put a lower-third text on the stream -> [Cloud Mixer](../apps/CLOUD_MIXER.md) (Linux/Cloud; API: http 8841)
- schedule a show to start at noon -> [Cloud Mixer](../apps/CLOUD_MIXER.md) (Linux/Cloud; API: http 8841)
- use my phone as a manual camera -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb) - call: `scripts/mcam iso 400`
- stream the phone camera to OBS or vMix over NDI -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb)
- set ISO, shutter, white balance on the phone by command -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb)
- record a take with log curve on Android -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb)
- start all Sony cameras recording with the phone -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb)
- go live from the phone to my website -> [Mantra Manual Camera](../apps/mantra-manual-camera.md) (macOS/Android; API: adb)
- mirror my Android screen to OBS over NDI -> [Mantra NDI Screen Share (Android)](../apps/mantra-ndi-screen-share-android.md) (Android; API: none)
- show the phone screen in vMix -> [Mantra NDI Screen Share (Android)](../apps/mantra-ndi-screen-share-android.md) (Android; API: none)
- stream Android screen as NDI -> [Mantra NDI Screen Share (Android)](../apps/mantra-ndi-screen-share-android.md) (Android; API: none)
- build the Android NDI app -> [Mantra NDI SDK (private vendor files)](../apps/mantra-ndi-sdk.md) (Android/Cloud; API: none)
- where are the NDI SDK headers for Android -> [Mantra NDI SDK (private vendor files)](../apps/mantra-ndi-sdk.md) (Android/Cloud; API: none)
- sync time code on my Sony cameras -> [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md) (Android; API: adb) - call: `adb shell am start -n com.mantraproductions.sonyremote/.TcJamActivity --es tc 12:00:00:00`
- start recording on all Sony cameras at once -> [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md) (Android; API: adb)
- jam timecode from the phone to a Sony A7 -> [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md) (Android; API: adb)
- clap sync for multi-camera shoot -> [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md) (Android; API: adb)
- Sony Alpha Android remote -> [Mantra Sony Remote (TC Jam), Android](../apps/sony_remote_controller.md) (Android; API: adb)
- watch an NDI stream on the Mac -> [NDI Mantra Monitor](../apps/ndi-mantra-monitor.md) (macOS; API: none)
- monitor the phone's NDI camera on the desktop -> [NDI Mantra Monitor](../apps/ndi-mantra-monitor.md) (macOS; API: none)
- view an NDI source in a window -> [NDI Mantra Monitor](../apps/ndi-mantra-monitor.md) (macOS; API: none)
- vMix-like switcher on Mac -> [obs2vmix](../apps/obs2vmix.md) (macOS; API: none)
- OBS with a vMix look -> [obs2vmix](../apps/obs2vmix.md) (macOS; API: none)
- build the obs2vmix DMG -> [obs2vmix](../apps/obs2vmix.md) (macOS; API: none)
- follow me with a skeleton on camera -> [Skeleton (Mantra)](../apps/SKELETON.md) (macOS/Android; API: cli) - call: `open -a "Skeleton (Mantra)" --args --camera ILCE-7M5 # the skeleton of the picture from the named camera`
- check my yoga pose against a target -> [Skeleton (Mantra)](../apps/SKELETON.md) (macOS/Android; API: cli)
- multi-camera body tracking -> [Skeleton (Mantra)](../apps/SKELETON.md) (macOS/Android; API: cli)
- use the Pixel as a pose camera -> [Skeleton (Mantra)](../apps/SKELETON.md) (macOS/Android; API: cli)
- start and stop recording on the Sony from the Mac -> [Sony Remote (Mantra), Mac](../apps/SONY_REMOTE_MAC.md) (macOS; API: http 8881) - call: `curl -s 127.0.0.1:8881/start`
- record the Sony to its card remotely -> [Sony Remote (Mantra), Mac](../apps/SONY_REMOTE_MAC.md) (macOS; API: http 8881)
- Sony alpha remote record button -> [Sony Remote (Mantra), Mac](../apps/SONY_REMOTE_MAC.md) (macOS; API: http 8881)
- grab a live view frame from the Sony -> [Sony Remote (Mantra), Mac](../apps/SONY_REMOTE_MAC.md) (macOS; API: http 8881)
- send mixer audio to the camera -> [Sound Link (Mantra)](../apps/SOUND_LINK.md) (macOS/Android; API: http 8974) - call: `curl -s -XPOST 127.0.0.1:8974/fn/source -d '{"device":"BlackHole","pair":1}'`
- sync desk sound with the phone camera -> [Sound Link (Mantra)](../apps/SOUND_LINK.md) (macOS/Android; API: http 8974)
- stream NDI camera plus mixer sound -> [Sound Link (Mantra)](../apps/SOUND_LINK.md) (macOS/Android; API: http 8974)
- Mac audio to Android over Wi-Fi -> [Sound Link (Mantra)](../apps/SOUND_LINK.md) (macOS/Android; API: http 8974)
- is my live stream working -> [Streaming Dashboard (Mantra)](../apps/STREAMING_DASHBOARD.md) (macOS/Linux/Cloud; API: door 8996) - call: `curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"go-live","minutes":15}'`
- check the streaming chain -> [Streaming Dashboard (Mantra)](../apps/STREAMING_DASHBOARD.md) (macOS/Linux/Cloud; API: door 8996)
- start the test stream and go live -> [Streaming Dashboard (Mantra)](../apps/STREAMING_DASHBOARD.md) (macOS/Linux/Cloud; API: door 8996)
- how many viewers are watching -> [Streaming Dashboard (Mantra)](../apps/STREAMING_DASHBOARD.md) (macOS/Linux/Cloud; API: door 8996)
- use my phone camera as a webcam on the Mac -> [Virtual Cam (Mantra)](../apps/mantra_virtual_cam.md) (macOS/Android; API: other) - call: `open -g mantravirtualcam://webcam/<name> # the phone camera becomes the Mac webcam (shown as OBS Virtual Camera)`
- control the Mantra Manual Camera from the Mac -> [Virtual Cam (Mantra)](../apps/mantra_virtual_cam.md) (macOS/Android; API: other)
- use several phone cameras in OBS -> [Virtual Cam (Mantra)](../apps/mantra_virtual_cam.md) (macOS/Android; API: other)
- record the Sony camera to disk on the Mac -> [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md) (macOS; API: http 8867) - call: `curl -s -XPOST 127.0.0.1:8867/record/start -H 'Content-Type: application/json' -d '{"name":"interview"}'`
- record a webcam or capture card with sound -> [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md) (macOS; API: http 8867)
- start and stop recording by command -> [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md) (macOS; API: http 8867)
- check which cameras the Mac sees -> [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md) (macOS; API: http 8867)
- set ISO or shutter on the Sony from the Mac -> [Webcam Recorder (Mantra)](../apps/web-cam-viewer.md) (macOS; API: http 8867)
