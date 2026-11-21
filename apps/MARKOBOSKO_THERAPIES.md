# Marko Bosko Therapies

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Website for an immersive therapy room (projected underwater reef, speakers, Mac mini) and a colour-and-sound room with Hemi-Sync samples.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MARKOBOSKO_THERAPIES](https://github.com/markoboskoauroville/MARKOBOSKO_THERAPIES) |
| Also called | markoboskotherapies.pages.dev, Marko Bosko Therapies |
| Visibility | public |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | Python tools + HTML |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Present the immersive room, its setup and an equipment table with prices on a static page
- Play sample audio and a full-screen demo therapy mode with butterchurn visuals
- Recommend albums with short reasons
- Deploy to Cloudflare Pages with deploy.sh (wrangler pages deploy)
- Catalogue and tag Hemi-Sync audio with local Whisper checks (tools/hs*.py)

## Ask for it when

- therapy room website
- immersive room equipment list
- Hemi-Sync sample player page
- colour and sound therapy page

## How to control it

No control API found.

Evidence: none found (deploy.sh and tools only; Whisper via MANTRA_VOICE :8837 /hear is used as a client)

## Inputs / Outputs

Inputs:

- audio files
- instrument data (site/data/instruments.json)

Outputs:

- static site on Cloudflare Pages

## Works with

- Uses: [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [Mantra Voice (speech server)](MANTRA_VOICE.md)

## Code worth reusing

- `site/player.js`: one audio player module shared by sample list and demo therapy mode
- `tools/hsrun.py`: audio catalogue run using local Whisper to check tracks
- `deploy.sh`: Cloudflare Pages deploy with token from environment or local file

## Notes

Public unpromoted repo (no README by rule). Pictures were still placeholders at last note. No donation bowl by owner's decision. Pages project must exist; deploy never uses wrangler deploy.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MARKOBOSKO_THERAPIES/blob/HEAD/TAKEOVER.md)
