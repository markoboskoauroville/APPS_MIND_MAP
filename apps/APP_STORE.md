# App Store (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Sleeping app store in the star menu: search an app, find the developer's own .dmg and install it; runs only while its tick is on.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/APP_STORE](https://github.com/markoboskoauroville/APP_STORE) |
| Also called | App Store that sleeps |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS, Web, Hammerspoon |
| Language | Swift, Python (Flask) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v2 |
| Control level | http (own http routes) |

## What it can do

- Search Homebrew cask index and Apple's catalogue for an app
- Find the developer's .dmg and install it
- Fix misspelled searches using a fuzzy pass and an AI engine (Gemini ring or Haiku)
- Install Mac App Store apps via mas where present
- Test the AI keys through Key Ring Tester
- Sleep completely when not ticked in the star

## Ask for it when

- install an app without the App Store
- find the dmg of an application
- search for a Mac or iPhone app by name
- put the app store to sleep

## How to control it

- Level: **http**
- Type: http
- Port: 8839

Actions:

- `GET /health`
- `POST /quit`

**Before you call:** App Store (Mantra) must be running.

Example:

```
curl -s 127.0.0.1:8839/health # the only routes are /health and /quit; the store itself is used in its window
```

More calls:

- close the app: `curl -s -XPOST 127.0.0.1:8839/quit`

Evidence: TAKEOVER.md; store.py line 482 (/health)

## Inputs / Outputs

Outputs:

- downloaded .dmg files
- installed apps

## Works with

- Uses: [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md), [KeyringTester (Mantra)](KEY_RING_TESTER.md), [Star (Mantra), Lua (Hammerspoon, legacy)](MANTRA_STAR.md)
- Used by or talked to by: [Free Mac](FREE_MAC.md)

## Notes

Swift window replaced the Flask page (App.swift); the Flask store.py is the original. Never add LaunchAgent, timers or update checks.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
- `CLAUDE.md`
