# Animator Collaboration

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Storage and handover site for the Brain Brake animation: scene-by-scene frame variations, backgrounds and foregrounds for the animator.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ANIMATOR_COLLABORATION](https://github.com/markoboskoauroville/ANIMATOR_COLLABORATION) |
| Also called | BB_C, Brain Brake animation collaboration |
| Visibility | public |
| Kind | data |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | Web |
| Language | HTML (GitHub Pages) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Hold per-scene folders (BB_C_1 to BB_C_8) of frame variations, background and foreground plates
- Log every image and why it exists in CHANGES.md
- Publish as a GitHub Pages site the animator downloads from
- Name frames by number with _vN for variations and a letter for new in-between frames

## Ask for it when

- where are the animator's frames for scene 3
- hand over frames to the animator
- what changed in the Brain Brake frames

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Inputs:

- generated frames and plates

Outputs:

- static site with shot pages
- download links

## Works with

- Uses: [Brain Brake audio](BRAINBREAK_AUDIO.md), [The Brain Brake (film repository)](BRAIN_BRAKE.md), [Brain Brake originals](BRAIN_BRAKE_ORIGINALS.md)
- Used by or talked to by: [Brain Brake audio](BRAINBREAK_AUDIO.md), [The Brain Brake (film repository)](BRAIN_BRAKE.md), [Brain Brake originals](BRAIN_BRAKE_ORIGINALS.md)

## Notes

About 960 MB: GitHub Pages fails silently above 1 GB, so audio was moved to BRAINBREAK_AUDIO and full-size stills to BRAIN_BRAKE_ORIGINALS. Do not add audio here. Release tag is an image snapshot, not an app release. Not an app.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/ANIMATOR_COLLABORATION/blob/HEAD/README.md)
