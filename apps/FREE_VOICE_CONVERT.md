# Free Voice Convert (Equalizer)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Makes AI-video voices sound the same: cleans, converts speech to a chosen voice profile with Seed-VC, matches the room sound and levels, lossless export.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/FREE_VOICE_CONVERT](https://github.com/markoboskoauroville/FREE_VOICE_CONVERT) |
| Also called | Free Voice Convert Equalizer, FVC, freevoiceconvert |
| Visibility | public |
| Kind | app |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS, Windows |
| Language | Swift + C# + Python (Seed-VC engine) |
| Status | active |
| Last push | 2026-11-10 |
| Build / release | GitHub workflow: yes; latest release: v4 |
| Control level | cli (command line or script only) |

## What it can do

- Clean speech (70 Hz high-pass, noise reduction)
- Convert speech to a profile's voice with Seed-VC (SPEECH or STUDIO model) keeping frame count so lips still fit
- Match the clip's long-term spectrum to the profile with a smooth EQ (limit 12 dB)
- Level each clip to about -16.5 LUFS
- Export one by one, stitched or both, at the source's own rate and bit depth, picture copied bit for bit
- Make a sound profile from a voice recording

## Ask for it when

- make all my clips sound like the same voice
- fix AI video voices to match
- replace the Resolve voice cleanup steps
- stitch clips with the same sound

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `fvc.py check`
- `fvc.py fetch`
- `fvc.py profile <audio> <name>`
- `fvc.py profiles`
- `fvc.py run <job.json>`

**Before you call:** Run in the repo folder; models are fetched first with fvc.py fetch.

Example:

```
python3 engine/fvc.py run job.json
```

More calls:

- check the toolchain: `python3 engine/fvc.py check`
- learn a target voice from audio: `python3 engine/fvc.py profile voice.wav marko`
- list profiles: `python3 engine/fvc.py profiles`

Evidence: engine/fvc.py docstring; progress lines start with '@' and are JSON

## Inputs / Outputs

Inputs:

- any audio or video ffmpeg reads
- voice profile recording

Outputs:

- WAV or .mov/.mkv with PCM sound
- stitched file

## Code worth reusing

- `engine/fvc.py`: headless engine CLI shared by the Mac and Windows apps, JSON progress on stdout
- `engine/dsp.py`: profile spectrum match EQ, loudness levelling and clean chain
- `engine/setup.sh`: one-shot install of uv, Python, torch on MPS and Seed-VC with models (2.7 GB)

## Notes

README says the repo is private but the harvest lists it as public; treat visibility as public per repos_full. GPL-3.0 because Seed-VC is. STUDIO mode is slow on Macs (355 s for 22 s of sound). Windows installer unproven on real Windows. Site download buttons are fixed names filled by site.yml. A donation QR image is in site/public/img; do not copy.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/FREE_VOICE_CONVERT/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/FREE_VOICE_CONVERT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/FREE_VOICE_CONVERT/blob/HEAD/LESSONS.md)
