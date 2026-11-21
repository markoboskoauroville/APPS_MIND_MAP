[Back to the index](../CAPABILITIES.md)

# Android and Termux

## Which one to pick: Cloud VMs: Android emulator and Chromium

Two Oracle Cloud machines are reached over Tailscale. vm-android is a redroid Pixel 7 with the Mac command `pixel7` and the door pixel7d on 8897; vm-android-jobs is the git mailbox for the same phone: push `jobs/<id>/job.json` and an APK, pull `results/<id>/result.json`. vm-chromium is the Chromium VM with the vm-agent on 8890 and the Mac command `cvm`. Local, not cloud: MANTRA_SANDBOX runs a headless emulator on the Mac. Related VM services: CLOUD_MIXER and STREAMING_DASHBOARD.

| You want | Use | How |
|---|---|---|
| install and test an APK on the cloud Pixel 7 | [vm-android (Pixel 7 in Oracle Cloud) (vm-android)](../apps/vm-android.md) | `pixel7 test app.apk` |
| test an APK without Tailscale or a terminal: git mailbox | [VM Android jobs mailbox (vm-android-jobs)](../apps/vm-android-jobs.md) | `ID=20261104-remote-v22; mkdir -p jobs/$ID && cp app.apk jobs/$ID/app.apk && cp job.json jobs/$ID/job.json && git add jobs/$ID && git commit -m "job $ID" && git push` |
| use a Chromium browser in the cloud | [Chromium Virtual Machine (Mantra) (vm-chromium)](../apps/vm-chromium.md) | `cvm ask "Summarise the open tab in one sentence"` |
| mix files and live URLs into one picture on the VM | [Cloud Mixer (CLOUD_MIXER)](../apps/CLOUD_MIXER.md) | `curl -s 127.0.0.1:8841/load -d '{"src":"/srv/cloud-mixer/media/x.mp4","id":"cam1","start":300}'` |
| start or stop the live stream chain | [Streaming Dashboard (Mantra) (STREAMING_DASHBOARD)](../apps/STREAMING_DASHBOARD.md) | `curl -s -XPOST http://127.0.0.1:8996/api/action -H 'Content-Type: application/json' -H 'x-dash-token: <token>' -d '{"action":"go-live","minutes":15}'` |

### [Android Lab](../apps/android-lab.md)

macOS/Android; API: cli. Main call: `droid run # from inside any Android project under ~/Developer: builds, installs and starts it in the headless emulator`

Before: Run from inside an Android project folder; droid up starts the emulator, droid down stops it.

- test an Android app on the Mac (Android Lab)
- build an APK locally (Android Lab)
- start the Pixel 7 emulator (Android Lab) - call: `droid shot`
- take a screenshot of the emulated phone (Android Lab)
- run Android unit tests locally (Android Lab)
- publish a local APK build (Android Lab)

### [Auroville FlorisBoard Theme](../apps/auroville-florisboard-theme.md)

Android; API: none

- change the colours of my phone keyboard (Auroville FlorisBoard Theme)
- install the Auroville theme on FlorisBoard (Auroville FlorisBoard Theme)
- dark gold keyboard theme for Mantra Voice Type (Auroville FlorisBoard Theme)

### [Calendar Events](../apps/calendar_events.md)

Android/Termux; API: cli. Main call: `python -m calendar_events move --from work --title Dentist --on 2026-11-05 --to personal --yes`

Before: Needs Calendar access for the terminal on the Mac.

- move a calendar event to another calendar (Calendar Events) - call: `python -m calendar_events calendars`
- list my calendars (Calendar Events)
- show events for the next week from the phone calendar (Calendar Events) - call: `python -m calendar_events events`

### [Claude Code for Termux](../apps/CLAUDE_CODE_TERMUX.md)

Android/Termux; API: cli. Main call: `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/CLAUDE_CODE_TERMUX/main/install.sh -o cct.sh && bash cct.sh --proot`

Before: Run inside Termux; --proot installs Claude Code in a Linux proot, --native without it.

- install Claude Code on my phone (Claude Code for Termux)
- run Claude Code in Termux (Claude Code for Termux)
- set up Claude on Android (Claude Code for Termux)

### [Cockpit Android](../apps/COCKPIT_ANDROID.md)

Android; API: none

- show CPU usage in the Android status bar (Cockpit Android)
- which apps use memory on my phone (Cockpit Android)
- phone health notification (Cockpit Android)
- kill a background app on Android (Cockpit Android)

### [Cockpit Termux](../apps/COCKPIT_TERMUX.md)

Android/Termux; API: door 8860. Main call: `curl -s -XPOST 127.0.0.1:8860/api/refresh`

Before: Cockpit runs on the phone in Termux (start with the command cockpit); port 8860 or the next free one up to 8875.

- kill memory-hungry apps on my phone (Cockpit Termux)
- phone health page (Cockpit Termux)
- lift the phantom process limit (Cockpit Termux)
- see what my Android is doing (Cockpit Termux)

### [Etno orkestar calendar assistant](../apps/ethno_orchestar.md)

Cloud; API: none

- put the orchestra rehearsal schedule in my calendar (Etno orkestar calendar assistant)
- add concert dates from a pasted message to Google Calendar (Etno orkestar calendar assistant)

### [FTP Server v4](../apps/ftp-server-termux-and-terminal.md)

macOS/Android/Termux; API: http 8200. Main call: `ftpserver get studio Music # fetch the folder Music from the server named studio`

Before: Runs on the phone or Mac (Termux or terminal); HTTP page on 8200 (up to 8215), FTP on 2121, its own DNS on UDP 8253. Names are the machines' names it knows.

- move files between phone and Mac over Wi-Fi (FTP Server v4)
- start a file server on the phone (FTP Server v4)
- copy a folder from the studio computer by name (FTP Server v4)
- give network devices friendly names (FTP Server v4)

### [gi (Instagram downloader)](../apps/gi.md)

Android/Termux; API: cli. Main call: `gi https://www.instagram.com/p/<shortcode>/ # downloads the post or reel`

- download an Instagram video on the phone (gi)
- save an Instagram story or highlight (gi)
- refresh the Instagram cookie (gi) - call: `gi --cookies`

### [GitHub Repo](../apps/GITHUB_REPO.md)

Android; API: none

- download an APK from someone's GitHub releases on the phone (GitHub Repo)
- browse a GitHub user's repos on Android (GitHub Repo)

### [Google Cloud Chat for Termux](../apps/GCLOUD_CHAT_TERMUX.md)

Android/Termux; API: none

- chat with Gemini on my phone (Google Cloud Chat for Termux)
- Gemini from Termux (Google Cloud Chat for Termux)
- Google Cloud chat on Android (Google Cloud Chat for Termux)

### [Mantra Route](../apps/MANTRA_ROUTE.md)

Android; API: none

- switch audio output on Android with one tap (Mantra Route)
- send phone sound to the speaker or Bluetooth quickly (Mantra Route)
- mono or balance for all phone audio (Mantra Route)

### [Termux Emulator Image](../apps/termux-emulator-image.md)

Android/Termux/Linux/Cloud; API: cli. Main call: `bash tools/cloud-android/termux-emulator.sh restore (in a MANTRA_MANIFEST checkout)`

Before: From a MANTRA_MANIFEST checkout.

- test Termux apps in a cloud session (Termux Emulator Image)
- get an Android emulator with Termux and Claude Code in the cloud (Termux Emulator Image) - call: `bash tools/cloud-android/termux-emulator.sh start`
- restore the Termux emulator (Termux Emulator Image)

### [Termux Tools](../apps/termux-tools.md)

Android/Termux; API: cli. Main call: `phonelink sh 'input tap 300 400'`

Before: On the phone in Termux (mamc starts the apps; phonelink from the Mac sends adb commands).

- install my Termux tools on a phone (Termux Tools)
- launch Termux apps from a menu (Termux Tools)
- have Claude's replies read aloud on the phone (Termux Tools)
- get a notification when Claude Code finishes on the phone (Termux Tools) - call: `ccpush "build done"`
- switch Claude account in Termux (Termux Tools)
- keep adb connected on the phone without Wi-Fi (Termux Tools) - call: `adbup status`

### [Termux Voice (voiced)](../apps/TERMUX_VOICE.md)

macOS/Android/Termux; API: http 8840. Main call: `phonesay pixel "The render is done."`

Before: Runs on the phone in Termux (voiced); from the Mac the phonesay command sends the text there (nothing | pixel | both chooses where it is spoken). Only Tailscale and loopback clients are accepted.

- make the phone speak (Termux Voice) - call: `curl -s -XPOST 127.0.0.1:8840/say -H 'Content-Type: application/json' -d '{"text":"Dobar dan","lang":"hr"}'`
- send a spoken message to my Pixel or Nothing (Termux Voice)
- text to speech on the phone from the Mac (Termux Voice)
- phone voice daemon (Termux Voice)
- phone voice (replaces the retired Voice Engine Android) (Termux Voice)

### [USB Tethering (Mantra)](../apps/USB_TETHERING.md)

Android; API: none

- toggle USB tethering with one tap (USB Tethering)
- internet from the phone to the Mac over USB (USB Tethering)
- tethering widget (USB Tethering)

### [VM Android jobs mailbox](../apps/vm-android-jobs.md)

Android/Linux/Cloud; API: other. Main call: `ID=20261104-remote-v22; mkdir -p jobs/$ID && cp app.apk jobs/$ID/app.apk && cp job.json jobs/$ID/job.json && git add jobs/$ID && git commit -m "job $ID" && git push # then: git pull until results/$ID/result.json exists (usually under a minute)`

Before: Work in a checkout of the repo vm-android-jobs; the id is `<date>-<app>-<short>`. The job folder is removed when the result lands.

- test an APK on a cloud Android phone (VM Android jobs mailbox) - call: `{"apk":"app.apk","seconds":10,"steps":[{"tap":[540,1200]},{"wait":2},{"shot":"after-tap"}]}`
- take screenshots of an app on the VM Pixel (VM Android jobs mailbox) - call: `{"apk":"app.apk","seconds":10,"device":"nothing-phone-2a","steps":[]} # works only while adb listens on that phone`
- run tap and swipe steps against an app remotely (VM Android jobs mailbox)


## Retired - do not use

- [Voice Engine Android (retired)](../apps/VOICE_ENGINE_ANDROID.md) - replaced by [Termux Voice (voiced)](../apps/TERMUX_VOICE.md)
- [WhatsApp audio HAL (moved) (retired)](../apps/wa-audio-hal.md) - Replaced by WHATSAPP_REMOTE_VIEWER.
