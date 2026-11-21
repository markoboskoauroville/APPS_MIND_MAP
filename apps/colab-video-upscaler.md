# Colab Video Upscaler

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Free Topaz stand-in: restores Resolve clips with CodeFormer and Real-ESRGAN on Colab's free GPU in chunks through Google Drive.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/colab-video-upscaler](https://github.com/markoboskoauroville/colab-video-upscaler) |
| Also called | colab upscaler, topaz stand-in |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS, Cloud |
| Language | Python |
| Status | active |
| Last push | 2026-10-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Plan a clip into one-minute chunks and link a Colab notebook
- Fetch finished chunks from Google Drive and reassemble clips
- Replace the clips on the Resolve timeline at the same positions
- Run Resolve's own Super Scale 4x clip by clip as a first route
- Generate the Colab notebook from a script

## Ask for it when

- upscale a blocky video for free
- restore faces in a lecture video
- use Colab GPU to improve Resolve clips

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `plan`
- `link`
- `status`
- `fetch`
- `watch`
- `assemble`
- `rebuild`

**Before you call:** Needs the Colab notebook linked by 'link'; run in the repo folder.

Example:

```
python3 colab_restore.py status
```

More calls:

- plan the job, then fetch results: `python3 colab_restore.py plan ; python3 colab_restore.py fetch`
- assemble the video: `python3 colab_restore.py assemble`

Evidence: README.md, HANDOVER.md

## Inputs / Outputs

Inputs:

- Resolve project clips
- video file

Outputs:

- restored video chunks
- rebuilt timeline

## Code worth reusing

- `resolve_up.py`: waits for Resolve's API and parks Resolve on a safe page
- `make_notebook.py`: generates the Colab restore notebook

## Notes

Built for one specific lecture video; the Resolve Super Scale route was judged unsatisfactory. Status of the full Colab run unknown from the docs.

## Docs in the repo

- `README.md`
- `HANDOVER.md`
