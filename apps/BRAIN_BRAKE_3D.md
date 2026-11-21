# Brain Brake 3D

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Blender scripts that model the film's brass key in plain Python and render brass and drawn-paper stills headless.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAIN_BRAKE_3D](https://github.com/markoboskoauroville/BRAIN_BRAKE_3D) |
| Visibility | public |
| Kind | cli-tool |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | macOS |
| Language | Python (Blender) |
| Status | dormant |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Regenerate the key mesh from Python (brain_break_key_source.py)
- Build brass and drawn-paper materials and lighting in Blender
- Render twelve stills including the key turning and falling, headless

## Ask for it when

- render the Brain Brake key
- 3D key for the film
- run Blender headless to render stills

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `Blender --background --python scripts/render_key.py`
- `scripts/render_key_v2.py`
- `scripts/render_key_v3.py`
- `scripts/render_fall.py`

**Before you call:** Blender installed in /Applications; run from the repo folder.

Example:

```
/Applications/Blender.app/Contents/MacOS/Blender --background --python scripts/render_key.py
```

More calls:

- second and third key render, and the fall: `Blender --background --python scripts/render_key_v2.py ; ... render_key_v3.py ; ... render_fall.py`

Evidence: TAKEOVER.md

## Inputs / Outputs

Inputs:

- mesh/brain_break_key.obj

Outputs:

- renders/ (not committed)
- stills/*.jpg

## Works with

- Uses: [The Brain Brake (film repository)](BRAIN_BRAKE.md)
- Used by or talked to by: [The Brain Brake (film repository)](BRAIN_BRAKE.md)

## Code worth reusing

- `scripts/brain_break_key_source.py`: generate an OBJ mesh in plain Python without Blender

## Notes

Size rule: never commit render sequences or packed .blend files; only mesh, scripts and a few chosen JPEG stills.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/BRAIN_BRAKE_3D/blob/HEAD/TAKEOVER.md)
