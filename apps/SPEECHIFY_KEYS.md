# Speechify Keys

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**One script line for Marko's web pages that gives keyboard control of the Speechify Chrome extension: Space, arrows, Escape, and click to read from a sentence.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/SPEECHIFY_KEYS](https://github.com/markoboskoauroville/SPEECHIFY_KEYS) |
| Also called | Speechify keys, speechify-keys.js |
| Visibility | public |
| Kind | library-module |
| Category | [Knowledge, books and guides](../capabilities/knowledge-books-guides.md) |
| Platforms | Web, Chrome |
| Language | JavaScript (served as HTML pages) |
| Status | active |
| Last push | 2026-10-29 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Play and pause Speechify with Space
- Jump one sentence back or forward with the arrow keys
- Turn Speechify off with Escape
- Start reading from a clicked sentence
- Stay inactive until Speechify's player is on the page

## Ask for it when

- keyboard control for Speechify on my pages
- read aloud from where I click
- add Speechify keys to a web page

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- key presses and clicks on the page

Outputs:

- drives the Speechify player in the page

## Code worth reusing

- `public/speechify-keys.js`: drop-in script giving Speechify keyboard control and click-to-read on any web page

## Notes

Include with ‹script src="https://speechifykeys.pages.dev/speechify-keys.js" defer›. Every page built for Marko carries this line (MANTRA_MANIFEST modules/speechify-keys.md). Tested in Chrome.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/SPEECHIFY_KEYS/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/SPEECHIFY_KEYS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/SPEECHIFY_KEYS/blob/HEAD/LESSONS.md)
