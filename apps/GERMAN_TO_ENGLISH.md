# German to English (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Firefox extension that translates German web pages to English in place with Claude Haiku, with a one-click switch back to the German.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GERMAN_TO_ENGLISH](https://github.com/markoboskoauroville/GERMAN_TO_ENGLISH) |
| Also called | German to English |
| Visibility | private (code not readable without access) |
| Kind | browser-extension |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | Web |
| Language | JavaScript |
| Status | active |
| Last push | 2026-11-06 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Detect German pages and translate visible text, placeholders, titles and alt text in batches
- Keep the page layout and translate text added later
- Cache translations so repeat pages cost nothing
- Switch between English and the German original with a pill button
- Load as a temporary add-on through firefoxctl

## Ask for it when

- read a German website in English
- translate this German page automatically

## How to control it

No control API found.

## Code worth reusing

- `extension/content.js`: finds translatable text nodes and puts translations back while watching for page changes
- `tools/load_in_firefox.py`: load an extension folder into a running Firefox via WebDriver BiDi

## Notes

Needs a user-supplied API key; permanent install needs Mozilla signing (not done).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
