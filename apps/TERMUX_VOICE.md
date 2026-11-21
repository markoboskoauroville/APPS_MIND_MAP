# Termux Voice (voiced)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Small Python daemon in Termux that makes an Android phone speak text sent from the Mac (English or Croatian), with a queue, pause/repeat and a notification.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/TERMUX_VOICE](https://github.com/markoboskoauroville/TERMUX_VOICE) |
| Also called | voiced, phonesay, vsay |
| Visibility | public |
| Kind | service-daemon |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | macOS, Android, Termux |
| Language | Python |
| Status | active |
| Last push | 2026-11-15 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Speak text sent by HTTP on the phone, one voice at a time
- Render English via Speechify keys with Edge TTS fallback and Croatian speech
- Play sentence by sentence with mpv and notification controls pause, repeat, stop
- Start automatically when Termux opens
- Send from the Mac with phonesay

## Ask for it when

- make the phone speak
- send a spoken message to my Pixel or Nothing
- text to speech on the phone from the Mac
- phone voice daemon
- phone voice (replaces the retired Voice Engine Android)

## How to control it

- Level: **http**
- Type: http, cli
- Port: 8840

Actions:

- `GET /health`
- `POST /say`
- `POST /now`
- `POST /pause`
- `POST /repeat`
- `POST /next`
- `POST /quit`
- `phonesay nothing|pixel|both "text"`
- `vsay`

**Before you call:** Runs on the phone in Termux (voiced); from the Mac the phonesay command sends the text there (nothing | pixel | both chooses where it is spoken). Only Tailscale and loopback clients are accepted.

Example:

```
phonesay pixel "The render is done."
```

More calls:

- speak through HTTP on the phone, English or Croatian: `curl -s -XPOST 127.0.0.1:8840/say -H 'Content-Type: application/json' -d '{"text":"Dobar dan","lang":"hr"}'`
- pause, repeat or skip what is spoken: `curl -s -XPOST 127.0.0.1:8840/pause # also /repeat, /next, /now`
- is it alive: `curl -s 127.0.0.1:8840/health`
- speak on the phone and the Mac at once: `phonesay both "text"`

Evidence: TAKEOVER.md lines 5-16; voiced.py line 429

## Inputs / Outputs

Inputs:

- text from /say

Outputs:

- speech on the phone
- notification controls

## Hardware

- Android phones with Termux (Nothing, Pixel 7)

## Works with

- Uses: [Mantra Manifest](MANTRA_MANIFEST.md)
- Used by or talked to by: [Cost Agent (Mantra)](COST_AGENT.md), [Voice Engine Android (retired) (retired)](VOICE_ENGINE_ANDROID.md)

## Code worth reusing

- `voiced.py`: stdlib HTTP speech queue daemon with notification controls and a clients allowlist (Tailscale range and loopback)
- `install.sh`: one-line Termux installer with autostart in .bashrc
- `mac/phonesay`: Mac CLI that sends text to the phone voice

## Notes

Replaces the retired Voice Engine Android app (port 8720): TERMUX_VOICE is the only voice engine on the phones. Only Tailscale and loopback clients are accepted.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/TERMUX_VOICE/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/TERMUX_VOICE/blob/HEAD/LESSONS.md)
