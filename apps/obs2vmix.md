# obs2vmix

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Fork of OBS Studio for Mac (Apple Silicon) that re-skins OBS as a vMix-style switcher: Studio Mode only, two monitors, five thumbnails, right-click actions.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/obs2vmix](https://github.com/markoboskoauroville/obs2vmix) |
| Also called | OBS to vMix, obs2vmix OBS fork, OBS Studio fork |
| Visibility | public |
| Kind | fork |
| Category | [Camera, video, NDI and streaming](../capabilities/camera-video-ndi-streaming.md) |
| Platforms | macOS |
| Language | C/C++ (OBS Studio), Qt |
| Status | dormant |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Run OBS Studio in a vMix-like switcher layout (Studio Mode always on)
- Provide Source and Final monitors with draggable panes
- Switch via menus on the right mouse button with no text labels
- Update itself from the Help menu (obs2vmix-update tool)
- Build macOS DMGs by GitHub workflow

## Ask for it when

- vMix-like switcher on Mac
- OBS with a vMix look
- build the obs2vmix DMG

## How to control it

No control API found.

Evidence: api.txt only shows OBS repo scripts; no obs2vmix control API found (OBS's own plugin/websocket features not examined)

## Inputs / Outputs

Inputs:

- cameras, NDI, capture sources (as OBS)

Outputs:

- live stream/recording (as OBS)

## Code worth reusing

- `frontend/cmake/feature-obs2vmix.cmake`: CMake feature switch that builds the vMix-style UI inside OBS
- `docs/obs2vmix-ui.md`: Design notes for the vMix-style OBS user interface

## Notes

Default branch is master (upstream OBS); Marko's work lives on branch obs2vmix/seam (version 0.4.3, Sept 2026), not on master. The 17 'unmerged' branches are mostly old upstream OBS release branches. Release workflow publishes two macOS DMGs. Large repo.

Unmerged branches with commits ahead of main: 17.
