# Opening and Closing (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that sets up apps as they start (Chrome profiles, Ableton Arrangement view) and closes nuisance windows and banners.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/OPENING_AND_CLOSING](https://github.com/markoboskoauroville/OPENING_AND_CLOSING) |
| Also called | Automatic Closer, Speechify Splash Closer |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Mac system utilities](../capabilities/mac-system-utilities.md) |
| Platforms | macOS |
| Language | Swift |
| Status | dormant |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: v3 |
| Control level | none (no control api found) |

## What it can do

- Open ticked Chrome profiles at Chrome start and set the last used one
- Switch Ableton Live to Arrangement View at every start through AbletonOSC
- Close the Speechify Home window at launch
- Close the Login Item Added and Disk Not Ejected banners after 3 s
- Give each closer its own ON/OFF row

## Ask for it when

- open Chrome in a specific profile
- close that annoying window automatically
- start Ableton in arrangement view

## How to control it

No control API found.

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)

## Code worth reusing

- `app/Chrome.swift`: read Chrome profiles from Local State and open missing profile windows
- `app/Ableton.swift`: ask AbletonOSC to show a view until it answers

## Notes

Repo renamed twice; bundle id stays community.auroville.speechifysplashcloser so the Accessibility grant carries over. Needs Accessibility. A new closer is a row in the THINGS list.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
