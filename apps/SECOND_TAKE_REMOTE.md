# Second Take Remote

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android remote control for the Second Take shooting guide on a Mac: watch, live, record, stop, again, next from the phone over a small HTTP protocol.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SECOND_TAKE_REMOTE](https://github.com/markoboskoauroville/SECOND_TAKE_REMOTE) |
| Also called | Second Take Remote (Mantra), Remote Shooting, Second Take remote |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-13 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | http (own http routes) |

## What it can do

- Control the shooting guide from the phone (WATCH, LIVE, RECORD/STOP, AGAIN, NEXT, SHOTS, MUTE)
- Find the guide by itself (last address, USB adb reverse, Bonjour)
- Show shot number, title, say text and takes
- Include a loopback mock guide (mock/guide.py) for testing

## Ask for it when

- phone remote for filming lessons
- control the recording from my phone
- shot list remote for the Mac guide

## How to control it

- Level: **http**
- Type: http
- Port: 8965 (guide side; LAN listener 8966 in MPA_LESSONS_ANALYZER)

**Warning:** port 8965 is also quoted for [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md) - confirm with `mantra-ports scan`.

Actions:

- `GET /status`
- `GET /shots`
- `POST /mute`
- `POST /watch`
- `POST /live`
- `POST /record`
- `POST /stop`
- `POST /next`
- `POST /again`
- `POST /shot`

**Before you call:** This repo is the Android CLIENT; the guide is MPA_LESSONS_ANALYZER (listener 8966, private networks and Tailscale only, first come first served by X-Remote-Id; 423 when another remote holds it). The number 8965 in older records is the guide's local port, which MANTRA_ROOM also uses.

Example:

```
curl -s -XPOST http://<guide-address>:8966/record -H 'X-Remote-Id: phone1' # the phone starts a take on the Mac guide
```

More calls:

- state: `curl -s http://<guide-address>:8966/status -H 'X-Remote-Id: phone1'`
- stop, again, next: `curl -s -XPOST http://<guide-address>:8966/stop -H 'X-Remote-Id: phone1' ; ... /again ; ... /next`

Evidence: PROTOCOL.md (the wire the guide must offer); MainActivity.kt line 192

## Inputs / Outputs

Inputs:

- guide's /status and /shots

Outputs:

- control calls to the guide
- APK

## Works with

- Uses: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)
- Used by or talked to by: [MPA Lessons Analyzer](MPA_LESSONS_ANALYZER.md)

## Code worth reusing

- `mock/guide.py`: loopback test server of the Second Take protocol
- `android/app/src/main/java/community/auroville/secondtake/remote/Protocol.kt`: client of the Second Take HTTP protocol with first-come-first-served id

## Notes

This repo is the CLIENT; the HTTP API (protocol v1) is served by the guide app. One remote at a time: busy guides answer 423. Built only by GitHub Actions. Port numbers: the phone-facing protocol is on 8966 per the MPA_LESSONS_ANALYZER docs; 8965 is the local door of the same app and also of MANTRA_ROOM. Check PROTOCOL.md in the repo before calling.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/SECOND_TAKE_REMOTE/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SECOND_TAKE_REMOTE/blob/HEAD/LESSONS.md)
