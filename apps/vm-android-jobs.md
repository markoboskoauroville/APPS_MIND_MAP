# VM Android jobs mailbox

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Git mailbox for the cloud Pixel 7: push a job.json and an APK, a runner installs and taps it, and the result with screenshots comes back by git pull.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/vm-android-jobs](https://github.com/markoboskoauroville/vm-android-jobs) |
| Also called | Oracle Pixel 7 mailbox |
| Visibility | private (code not readable without access) |
| Kind | service-daemon |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Linux, Cloud |
| Language | JSON jobs |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | other (other protocols) |

## What it can do

- Install an APK on the VM's Pixel 7 container and run scripted steps (tap, wait, shot, text, key, swipe, shell)
- Return result.json, screenshots and logcat for each job
- Target one of Marko's real phones over the private network when adb is open
- Poll the repo every 20 seconds through a runner service

## Ask for it when

- test an APK on a cloud Android phone
- take screenshots of an app on the VM Pixel
- run tap and swipe steps against an app remotely

## How to control it

- Level: **other**
- Type: cli
- Protocol: git mailbox: no HTTP; push a job folder to the repo, the runner on chromium-vm pulls it every 20 seconds and writes the result back

Actions:

- `jobs/<id>/job.json (apk, seconds, steps[tap|wait|shot|text|key|swipe|shell], package, activity, device, apk_url)`
- `jobs/<id>/app.apk`
- `results/<id>/result.json`
- `results/<id>/screen.png`
- `results/<id>/<shot>.png`
- `results/<id>/logcat.txt`

**Before you call:** Work in a checkout of the repo vm-android-jobs; the id is `<date>-<app>-<short>`. The job folder is removed when the result lands.

Example:

```
ID=20261104-remote-v22; mkdir -p jobs/$ID && cp app.apk jobs/$ID/app.apk && cp job.json jobs/$ID/job.json && git add jobs/$ID && git commit -m "job $ID" && git push # then: git pull until results/$ID/result.json exists (usually under a minute)
```

More calls:

- minimal job.json: install the APK, run 10 seconds, tap, screenshot: `{"apk":"app.apk","seconds":10,"steps":[{"tap":[540,1200]},{"wait":2},{"shot":"after-tap"}]}`
- more step kinds: `{"apk":"app.apk","seconds":10,"steps":[{"text":"hello"},{"key":"BACK"},{"swipe":[540,1800,540,600,300]},{"shell":"dumpsys activity top | head -40"}]}`
- run on one of the owner's real phones instead of the cloud Pixel 7: `{"apk":"app.apk","seconds":10,"device":"nothing-phone-2a","steps":[]} # works only while adb listens on that phone`
- read the answer: `git pull && cat results/$ID/result.json # installed, crashed, anr, running, focus, steps; plus screen.png, <shot>.png, logcat.txt`

Evidence: README.md (git mailbox protocol)

## Inputs / Outputs

Inputs:

- job.json
- APK

Outputs:

- result.json
- screenshots
- logcat

## Hardware

- Android arm64 container on cloud VM

## Works with

- Uses: [vm-android (Pixel 7 in Oracle Cloud)](vm-android.md)

## Notes

Android 14 arm64 dressed as Pixel 7, no Google Play services, only arm64 or armv7 native code. Results usually appear in under a minute.

## Docs in the repo

- `README.md`
