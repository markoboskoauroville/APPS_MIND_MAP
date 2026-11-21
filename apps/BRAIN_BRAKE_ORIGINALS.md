# Brain Brake originals

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Full-resolution stills of the film, scene folders BB_C_0 to BB_C_8, public with no Pages site so raw links work without credentials. About 2.8 GB.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/BRAIN_BRAKE_ORIGINALS](https://github.com/markoboskoauroville/BRAIN_BRAKE_ORIGINALS) |
| Visibility | public |
| Kind | data |
| Category | [Film and editing (DaVinci Resolve)](../capabilities/film-editing-resolve.md) |
| Platforms | Web |
| Language | none (png), Python helpers |
| Status | dormant |
| Last push | 2026-09-10 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Store original film frames by scene and version
- Serve raw links to the animator site
- Receive `review/<frame>.png` and review/latest.json from the chat session
- Receive review/verdicts.json from the Mac review wall

## Ask for it when

- full resolution frame of scene 1
- where are the original film stills
- download an original frame

## How to control it

No control API found.

Evidence: none found (api.txt empty or no control surface in the harvested files)

## Inputs / Outputs

Outputs:

- png stills
- review folder

## Works with

- Talks to: [Animator Collaboration](ANIMATOR_COLLABORATION.md), [Brain Brake review wall](BRAIN_BRAKE_REVIEW.md)
- Used by or talked to by: [Animator Collaboration](ANIMATOR_COLLABORATION.md), [The Brain Brake (film repository)](BRAIN_BRAKE.md), [Brain Brake Keyboard (Hammerspoon) (retired)](BRAIN_BRAKE_KEYBOARD.md), [Brain Brake review wall](BRAIN_BRAKE_REVIEW.md)

## Notes

Very large. api.txt skipped. Tree listing truncated at 400 entries. Review folder is a mailbox: chat session writes frames and latest.json, Mac writes only verdicts.json.
