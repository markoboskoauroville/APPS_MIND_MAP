# Blender Control

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Controls a live open Blender 5.2 GUI (or headless Blender) from outside over a localhost TCP JSON-RPC bridge and a CLI; includes procedural 3D test projects.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/blender-control](https://github.com/markoboskoauroville/blender-control) |
| Also called | BLENDER_CONTROL, Blender bridge, blender-control skill |
| Visibility | public |
| Kind | cli-tool |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-11 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Run Python/bpy code or script files inside the open Blender GUI on its main thread
- Read scene info, set viewport shading and take viewport screenshots
- Render stills (Cycles/EEVEE, Metal GPU) and H.264 animations
- Save, open and reset .blend files
- Run headless Blender batch jobs as fallback
- Frame-precise video editing skill using Blender VSE (colour change, text removal, de-flicker)

## Ask for it when

- control Blender from the terminal
- render a Blender scene to PNG or MP4
- build a 3D scene with a Python script in the open Blender
- change colours in a video frame by frame with Blender
- start the Blender bridge

## How to control it

- Level: **cli**
- Type: cli, python-module
- Port: 9876

Actions:

- `ping`
- `get_scene_info`
- `execute_code`
- `execute_file`
- `set_viewport`
- `viewport_screenshot`
- `render_image`
- `render_animation`
- `save_blend`
- `open_blend`
- `reset_scene`

**Before you call:** Blender running with the control add-on (TCP 9876), or add --headless for batch runs.

Example:

```
python3 .agents/skills/blender-control/scripts/blender_cli.py ping # Blender must run with its control add-on on port 9876
```

More calls:

- scene information: `python3 .agents/skills/blender-control/scripts/blender_cli.py info`
- run Python inside Blender: `python3 .agents/skills/blender-control/scripts/blender_cli.py exec "print(bpy.context.scene.name)"`
- render the frame: `python3 .agents/skills/blender-control/scripts/blender_cli.py render`
- viewport screenshot: `python3 .agents/skills/blender-control/scripts/blender_cli.py screenshot`

Evidence: .agents/skills/blender-control/scripts/blender_control_bridge.py (command dispatch, lines ~66-311); blender_cli.py; README.md

## Inputs / Outputs

Inputs:

- Python/bpy scripts
- a running Blender.app 5.2 GUI
- video files for VSE editing

Outputs:

- PNG renders
- MP4 animations
- screenshots
- scene.blend files

## Hardware

- Apple Silicon Metal GPU (Cycles)

## Works with

- Uses: [Firefox Control](firefox-control.md)

## Code worth reusing

- `.agents/skills/blender-control/scripts/blender_control_bridge.py`: Thread-safe localhost TCP JSON-RPC server that runs bpy code on Blender's main thread via a timer queue
- `.agents/skills/blender-control/scripts/blender_cli.py`: CLI client for the bridge with headless fallback
- `.agents/skills/video-frame-precise-edit/SKILL.md`: Method for flicker-free, band-free frame-precise video edits in Blender VSE

## Notes

Packaged as an Antigravity workspace skill, not a Mantra remote-door app (no /health or /api). Bridge is installed into Blender's startup scripts folder. Next planned step is a Google Cloud video-prompt studio (manifest only). Contains rendered sample media, so the repo is large.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/blender-control/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/blender-control/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/blender-control/blob/HEAD/LESSONS.md)
- [HANDOVER.md](https://github.com/markoboskoauroville/blender-control/blob/HEAD/HANDOVER.md)
