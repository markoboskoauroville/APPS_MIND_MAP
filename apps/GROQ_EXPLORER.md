# Groq Explorer

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android playground for every Groq model: a tile deck built from the models list, each opening the right interface and showing the exact request and a curl.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GROQ_EXPLORER](https://github.com/markoboskoauroville/GROQ_EXPLORER) |
| Also called | Groq Explorer, Groq Stream Deck |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: no; latest release: v6 |
| Control level | none (no control api found) |

## What it can do

- Build a grid of tiles from the Groq models endpoint at launch
- Open the right interface per model (recorder, text to speech, chat, image chat, safety meter)
- Show each model capability card with limits and prices
- Show the exact request and answer plus a runnable curl for every call
- Rotate through several API keys with a key ring

## Ask for it when

- try every Groq model from the phone
- test Groq speech to text on Android
- see the exact Groq API call that was sent

## How to control it

No control API found.

## Code worth reusing

- `app/src/main/kotlin/com/mantra/groqexplorer/data/Ring.kt`: API key ring with logic for rotation on failure
- `app/src/main/kotlin/com/mantra/groqexplorer/net/Groq.kt`: Groq API client

## Notes

Sister app to TTT mini.

## Docs in the repo

- `README.md`
