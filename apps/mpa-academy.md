# MPA Academy, website and hub

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Hub for a frame-drum percussion academy: public website, student portal, Exercise Lab of rhythms, lesson texts and hub Worker.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/mpa-academy](https://github.com/markoboskoauroville/mpa-academy) |
| Also called | Mantreshwar Percussions Academy, MPA, mpa hub, percussion academy |
| Visibility | private (code not readable without access) |
| Kind | website |
| Category | [Learning and academy](../capabilities/learning-academy.md) |
| Platforms | Web, Cloud |
| Language | JavaScript, Markdown |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Publish the academy website and a login portal on Cloudflare Pages
- Hold an Exercise Lab of rhythms, fingerings, ghost-note and phrasing exercises with codes
- Serve lesson videos with a centred play/pause player
- Make teacher-only printable A4 sheets of traditional rhythms
- Keep the database in a Worker and mirror it every minute to a private data repo with restore
- Keep lesson plans, transcripts of recorded classes and a log of requests and decisions
- Convert lesson recordings to MOV with time code (mpaconv)

## Ask for it when

- update the percussion academy website
- add a rhythm to the Exercise Lab
- write a text lesson from a recorded class
- restore the academy database
- make a printable rhythm sheet

## How to control it

- Level: **http**
- Type: http
- Port: HTTPS 443, hosted (Cloudflare hub Worker and site)

Actions:

- `/api/backup`
- `/api/ex`
- `/api/notes`

**Before you call:** Private repo with student data; the API list is partial because website/ was not harvested.

Example:

```
no verified call: the hub Worker routes /api/backup, /api/ex and /api/notes are named in TAKEOVER.md, but their arguments and login are not in the harvested docs
```

Evidence: TAKEOVER.md (hub Worker endpoints mentioned); source under website/ not harvested

## Inputs / Outputs

Inputs:

- recorded lessons
- transcripts
- teacher requests

Outputs:

- website
- portal
- PDF sheets
- database mirror

## Works with

- Used by or talked to by: [Plugin Assistant](PLUGIN_ASSISTANT.md), [Stream Deck Remote](STREAM_DECK_REMOTE.md)

## Code worth reusing

- `tools/mpaconv`: converts class recordings to MOV with time code
- `tools/sheets181.mjs`: generates A4 PDF rhythm sheets
- `.claude/skills/mpa-academy/SKILL.md`: skill describing how every academy task is done

## Notes

Private because it holds student contact details and message logs; those must not be published. Deploys only through GitHub Actions, never from the Mac. Source of the site and Worker (website/) was not in the harvest, so the API list is partial.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
