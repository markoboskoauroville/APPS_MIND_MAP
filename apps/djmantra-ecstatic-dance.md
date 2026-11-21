# DJ Mantra Ecstatic Dance page

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Bilingual (HR/EN) static page for DJ Mantra with an HLS demo-mix player with waveform, the Sounding Silence album player and a toning meditation player.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/djmantra-ecstatic-dance](https://github.com/markoboskoauroville/djmantra-ecstatic-dance) |
| Also called | DJ Mantra bio page, djmantra.pages.dev, DJ Mantra website, DJ Mantra ecstatic dance |
| Visibility | public |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | HTML (JS) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: toning-meditation |
| Control level | none (no control api found) |

## What it can do

- Present the bio, Tribal Jam Orchestra and the three-act ecstatic dance evening in Croatian and English
- Play the 1h53 demo mix as HLS with a three-band scrolling waveform, overview strip and tracklist by phase
- Play the Sounding Silence album with waveform and notes
- Play the toning meditation (one voice file over Marko's own song, chapters per element)
- Summarise and link the DJ Mantra Android app (djmantra_app)
- Deploy to Cloudflare Pages by workflow

## Ask for it when

- DJ Mantra website
- update the ecstatic dance bio page
- play the demo mix on the web
- toning meditation player page
- add a track to the mix player

## How to control it

No control API found.

Evidence: api.txt says SKIPPED large; README.md describes a static page only

## Inputs / Outputs

Inputs:

- HLS segments and wave.bin/tracks.json under assets/
- toning voice and song files

Outputs:

- static site on Cloudflare Pages

## Works with

- Uses: [DJ Mantra (Android DJ app)](djmantra_app.md)
- Used by or talked to by: [Mantra Room (Meditation Room / Chakra and Elements Toning)](MANTRA_ROOM.md), [DJ Mantra (Android DJ app)](djmantra_app.md)

## Code worth reusing

- `assets/analyzer/`: WASM audio analyzer with worker for waveform/track analysis in the browser
- `tools/toning/`: Scripts that build the toning player audio, waveform and chapter data (mentioned in README)

## Notes

Very large (566 MB) because audio is committed as HLS segments. The original mix is a GitHub Release asset (tag mix-2026-10-04). Lesson: never time-stretch or splice audio from the command line. api.txt was skipped (too large) so absence of an API is not proven, but this is a static page.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/djmantra-ecstatic-dance/blob/HEAD/README.md)
- [LESSONS.md](https://github.com/markoboskoauroville/djmantra-ecstatic-dance/blob/HEAD/LESSONS.md)
