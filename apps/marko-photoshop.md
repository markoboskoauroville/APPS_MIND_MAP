# Photopea Studio

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Minimal Streamlit shell that opens Photopea straight in the editor, hides Streamlit chrome, fills the window and adds a full-screen button.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/marko-photoshop](https://github.com/markoboskoauroville/marko-photoshop) |
| Also called | Photopea shell |
| Visibility | public |
| Kind | app |
| Category | [Data, backups and misc](../capabilities/data-backups-misc.md) |
| Platforms | Web, Cloud |
| Language | Python (Streamlit) |
| Status | dormant |
| Last push | 2026-05-30 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Embed Photopea skipping its start screen
- Hide Streamlit header, menu and footer
- Stretch the editor to the window and offer full screen

## Ask for it when

- open an online Photoshop-like editor full screen
- Photopea without the start screen

## How to control it

No control API found.

Evidence: app.py is a single Streamlit file

## Notes

Two files only (app.py, requirements.txt). Cannot remove Photopea ads (cross-origin frame). Repo name is marko-photoshop but the app is Photopea Studio.
