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

- test an Android app on the Mac -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli) - call: `droid run # from inside any Android project under ~/Developer: builds, installs and starts it in the headless emulator`
- build an APK locally -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli)
- start the Pixel 7 emulator -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli)
- take a screenshot of the emulated phone -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli)
- run Android unit tests locally -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli)
- publish a local APK build -> [Android Lab](../apps/android-lab.md) (macOS/Android; API: cli)
- change the colours of my phone keyboard -> [Auroville FlorisBoard Theme](../apps/auroville-florisboard-theme.md) (Android; API: none)
- install the Auroville theme on FlorisBoard -> [Auroville FlorisBoard Theme](../apps/auroville-florisboard-theme.md) (Android; API: none)
- dark gold keyboard theme for Mantra Voice Type -> [Auroville FlorisBoard Theme](../apps/auroville-florisboard-theme.md) (Android; API: none)
- move a calendar event to another calendar -> [Calendar Events](../apps/calendar_events.md) (Android/Termux; API: cli) - call: `python -m calendar_events move --from work --title Dentist --on 2026-11-05 --to personal --yes`
- list my calendars -> [Calendar Events](../apps/calendar_events.md) (Android/Termux; API: cli)
- show events for the next week from the phone calendar -> [Calendar Events](../apps/calendar_events.md) (Android/Termux; API: cli)
- install Claude Code on my phone -> [Claude Code for Termux](../apps/CLAUDE_CODE_TERMUX.md) (Android/Termux; API: cli) - call: `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/CLAUDE_CODE_TERMUX/main/install.sh -o cct.sh && bash cct.sh --proot`
- run Claude Code in Termux -> [Claude Code for Termux](../apps/CLAUDE_CODE_TERMUX.md) (Android/Termux; API: cli)
- set up Claude on Android -> [Claude Code for Termux](../apps/CLAUDE_CODE_TERMUX.md) (Android/Termux; API: cli)
- show CPU usage in the Android status bar -> [Cockpit Android](../apps/COCKPIT_ANDROID.md) (Android; API: none)
- which apps use memory on my phone -> [Cockpit Android](../apps/COCKPIT_ANDROID.md) (Android; API: none)
- phone health notification -> [Cockpit Android](../apps/COCKPIT_ANDROID.md) (Android; API: none)
- kill a background app on Android -> [Cockpit Android](../apps/COCKPIT_ANDROID.md) (Android; API: none)
- kill memory-hungry apps on my phone -> [Cockpit Termux](../apps/COCKPIT_TERMUX.md) (Android/Termux; API: door 8860) - call: `curl -s -XPOST 127.0.0.1:8860/api/refresh`
- phone health page -> [Cockpit Termux](../apps/COCKPIT_TERMUX.md) (Android/Termux; API: door 8860)
- lift the phantom process limit -> [Cockpit Termux](../apps/COCKPIT_TERMUX.md) (Android/Termux; API: door 8860)
- see what my Android is doing -> [Cockpit Termux](../apps/COCKPIT_TERMUX.md) (Android/Termux; API: door 8860)
- put the orchestra rehearsal schedule in my calendar -> [Etno orkestar calendar assistant](../apps/ethno_orchestar.md) (Cloud; API: none)
- add concert dates from a pasted message to Google Calendar -> [Etno orkestar calendar assistant](../apps/ethno_orchestar.md) (Cloud; API: none)
- move files between phone and Mac over Wi-Fi -> [FTP Server v4](../apps/ftp-server-termux-and-terminal.md) (macOS/Android/Termux; API: http 8200) - call: `ftpserver get studio Music # fetch the folder Music from the server named studio`
- start a file server on the phone -> [FTP Server v4](../apps/ftp-server-termux-and-terminal.md) (macOS/Android/Termux; API: http 8200)
- copy a folder from the studio computer by name -> [FTP Server v4](../apps/ftp-server-termux-and-terminal.md) (macOS/Android/Termux; API: http 8200)
- give network devices friendly names -> [FTP Server v4](../apps/ftp-server-termux-and-terminal.md) (macOS/Android/Termux; API: http 8200)
- download an Instagram video on the phone -> [gi (Instagram downloader)](../apps/gi.md) (Android/Termux; API: cli) - call: `gi https://www.instagram.com/p/<shortcode>/ # downloads the post or reel`
- save an Instagram story or highlight -> [gi (Instagram downloader)](../apps/gi.md) (Android/Termux; API: cli)
- refresh the Instagram cookie -> [gi (Instagram downloader)](../apps/gi.md) (Android/Termux; API: cli)
- download an APK from someone's GitHub releases on the phone -> [GitHub Repo](../apps/GITHUB_REPO.md) (Android; API: none)
- browse a GitHub user's repos on Android -> [GitHub Repo](../apps/GITHUB_REPO.md) (Android; API: none)
- chat with Gemini on my phone -> [Google Cloud Chat for Termux](../apps/GCLOUD_CHAT_TERMUX.md) (Android/Termux; API: none)
- Gemini from Termux -> [Google Cloud Chat for Termux](../apps/GCLOUD_CHAT_TERMUX.md) (Android/Termux; API: none)
- Google Cloud chat on Android -> [Google Cloud Chat for Termux](../apps/GCLOUD_CHAT_TERMUX.md) (Android/Termux; API: none)
- switch audio output on Android with one tap -> [Mantra Route](../apps/MANTRA_ROUTE.md) (Android; API: none)
- send phone sound to the speaker or Bluetooth quickly -> [Mantra Route](../apps/MANTRA_ROUTE.md) (Android; API: none)
- mono or balance for all phone audio -> [Mantra Route](../apps/MANTRA_ROUTE.md) (Android; API: none)
- test Termux apps in a cloud session -> [Termux Emulator Image](../apps/termux-emulator-image.md) (Android/Termux/Linux/Cloud; API: cli) - call: `bash tools/cloud-android/termux-emulator.sh restore (in a MANTRA_MANIFEST checkout)`
- get an Android emulator with Termux and Claude Code in the cloud -> [Termux Emulator Image](../apps/termux-emulator-image.md) (Android/Termux/Linux/Cloud; API: cli)
- restore the Termux emulator -> [Termux Emulator Image](../apps/termux-emulator-image.md) (Android/Termux/Linux/Cloud; API: cli)
- install my Termux tools on a phone -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli) - call: `phonelink sh 'input tap 300 400'`
- launch Termux apps from a menu -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli)
- have Claude's replies read aloud on the phone -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli)
- get a notification when Claude Code finishes on the phone -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli)
- switch Claude account in Termux -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli)
- keep adb connected on the phone without Wi-Fi -> [Termux Tools](../apps/termux-tools.md) (Android/Termux; API: cli)
- make the phone speak -> [Termux Voice (voiced)](../apps/TERMUX_VOICE.md) (macOS/Android/Termux; API: http 8840) - call: `phonesay pixel "The render is done."`
- send a spoken message to my Pixel or Nothing -> [Termux Voice (voiced)](../apps/TERMUX_VOICE.md) (macOS/Android/Termux; API: http 8840)
- text to speech on the phone from the Mac -> [Termux Voice (voiced)](../apps/TERMUX_VOICE.md) (macOS/Android/Termux; API: http 8840)
- phone voice daemon -> [Termux Voice (voiced)](../apps/TERMUX_VOICE.md) (macOS/Android/Termux; API: http 8840)
- phone voice (replaces the retired Voice Engine Android) -> [Termux Voice (voiced)](../apps/TERMUX_VOICE.md) (macOS/Android/Termux; API: http 8840)
- toggle USB tethering with one tap -> [USB Tethering (Mantra)](../apps/USB_TETHERING.md) (Android; API: none)
- internet from the phone to the Mac over USB -> [USB Tethering (Mantra)](../apps/USB_TETHERING.md) (Android; API: none)
- tethering widget -> [USB Tethering (Mantra)](../apps/USB_TETHERING.md) (Android; API: none)
- test an APK on a cloud Android phone -> [VM Android jobs mailbox](../apps/vm-android-jobs.md) (Android/Linux/Cloud; API: other) - call: `ID=20261104-remote-v22; mkdir -p jobs/$ID && cp app.apk jobs/$ID/app.apk && cp job.json jobs/$ID/job.json && git add jobs/$ID && git commit -m "job $ID" && git push # then: git pull until results/$ID/result.json exists (usually under a minute)`
- take screenshots of an app on the VM Pixel -> [VM Android jobs mailbox](../apps/vm-android-jobs.md) (Android/Linux/Cloud; API: other)
- run tap and swipe steps against an app remotely -> [VM Android jobs mailbox](../apps/vm-android-jobs.md) (Android/Linux/Cloud; API: other)

## Retired - do not use

- [Voice Engine Android (retired) (retired)](../apps/VOICE_ENGINE_ANDROID.md) - replaced by [Termux Voice (voiced)](../apps/TERMUX_VOICE.md)
- [WhatsApp audio HAL (moved) (retired)](../apps/wa-audio-hal.md) - Replaced by WHATSAPP_REMOTE_VIEWER.
