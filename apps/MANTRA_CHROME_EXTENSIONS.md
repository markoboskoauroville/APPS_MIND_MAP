# Mantra Chrome Extensions

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Home of the Chrome extensions that Queen writes and Macro Recorder loads, plus a Manifest V3 linter and a benchmark of how well Queen builds extensions.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MANTRA_CHROME_EXTENSIONS](https://github.com/markoboskoauroville/MANTRA_CHROME_EXTENSIONS) |
| Also called | Chrome extensions repo, Queen extensions |
| Visibility | public |
| Kind | library-module |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Chrome |
| Language | Python and JavaScript |
| Status | active |
| Last push | 2026-11-12 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Lint a Manifest V3 extension (extcheck.py): files, permissions, hosts, parse errors, with the exact fix
- Benchmark Queen's extension-building on seven levels L1-L7 (queen_bench.py) with graded results
- Keep example extensions: popup reading a page, service worker + badge, command bridge to a local server, human-like typing

## Ask for it when

- check a Chrome extension before loading it
- build or debug a Chrome extension
- act inside a web page through an extension
- benchmark an AI on writing extensions

## How to control it

No control API found.

Evidence: bench/L6 background.js polls http://127.0.0.1:8765/api/ext/poll and /api/ext/result (a sample bridge, not an app API)

## Inputs / Outputs

Inputs:

- extension folders

Outputs:

- lint reports
- bench/results.json

## Works with

- Uses: [Macro Recorder (Mantra)](MANTRA_MACRO.md), [Queen (Groq AI Studio), server and tools](groq_ai_studio.md)
- Used by or talked to by: [Macro Recorder (Mantra)](MANTRA_MACRO.md)

## Code worth reusing

- `tools/extcheck.py`: MV3 consistency linter: manifest vs files, chrome.* API declarations, fetch host permissions, JS parse
- `tools/queen_bench.py`: mechanical capability benchmark for extension building
- `bench/L6-command-bridge-to-a-local-server/background.js`: extension poll/result bridge to a local server

## Notes

extensions/ was empty on 12.11.2026; extctl.py (load/reload/unload per profile) not written. No CDP channel: Chrome DevTools HTTP endpoints 404. Public, unpromoted, no README by rule.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/MANTRA_CHROME_EXTENSIONS/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/MANTRA_CHROME_EXTENSIONS/blob/HEAD/LESSONS.md)
