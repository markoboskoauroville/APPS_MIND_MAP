# CQ VESA Adapter

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Design of a plate adapter that mounts the Allen & Heath CQ-12T on a VESA 75/100 arm or tripod head; 3D model and 1:1 drawings.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/cq_vesa_adapter](https://github.com/markoboskoauroville/cq_vesa_adapter) |
| Also called | CQ12T VESA adapter, mixer mount |
| Visibility | private (code not readable without access) |
| Kind | experiment |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | unknown |
| Language | Python, OpenSCAD |
| Status | active |
| Last push | 2026-10-24 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Generate a parametric 3D model of the base plate and keel (OpenSCAD)
- Generate 1:1 SVG and DXF cutting drawings
- Stamp drawings as estimate until real measurements are entered

## Ask for it when

- mount the CQ-12T on a monitor arm
- VESA adapter for a mixer
- get cutting drawings for a mounting plate

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `make_drawings.py --measured`

**Before you call:** Needs the Python packages named in the repo; produces drawings, no network.

Example:

```
python3 drawings/make_drawings.py --measured
```

Evidence: drawings/make_drawings.py (argparse), TAKEOVER.md

## Inputs / Outputs

Outputs:

- SVG and DXF drawings
- 3D model

## Hardware

- Allen & Heath CQ-12T

## Code worth reusing

- `drawings/make_drawings.py`: parametric plate drawing generator to SVG and DXF

## Notes

Design v1 only, not built; hole positions are estimates until measured.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
