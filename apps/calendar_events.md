# Calendar Events

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Command line tool that lists calendars and moves events between all of Marko's calendar accounts, via the phone or Google.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/calendar_events](https://github.com/markoboskoauroville/calendar_events) |
| Also called | calendar events, calendar mover |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Termux |
| Language | Python |
| Status | active |
| Last push | 2026-11-02 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- List every calendar with ids
- List events in a date range
- Move an event between calendars by copy, verify, then delete
- Do a dry run by default and refuse unsafe moves such as read-only targets
- Reach all phone calendars through the Android calendar provider over adb or Shizuku
- Use Google Calendar API for same-account native moves

## Ask for it when

- move a calendar event to another calendar
- list my calendars
- show events for the next week from the phone calendar

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `calendars`
- `events`
- `move`

**Before you call:** Needs Calendar access for the terminal on the Mac.

Example:

```
python -m calendar_events move --from work --title Dentist --on 2026-11-05 --to personal --yes
```

More calls:

- list the calendars: `python -m calendar_events calendars`
- list events: `python -m calendar_events events`

Evidence: README.md, calendar_events/cli.py

## Inputs / Outputs

Inputs:

- accounts.json aliases
- phone calendar provider
- Google Calendar API

Outputs:

- moved events

## Hardware

- Android phone with adb or Shizuku

## Code worth reusing

- `calendar_events/connectors/`: calendar connector interface with Android provider and Google implementations
- `calendar_events/mover.py`: safe copy-verify-delete event mover

## Notes

Default branch is a Claude cloud branch, not main. Has unit tests.

## Docs in the repo

- `README.md`
