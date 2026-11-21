# Mind Garden

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Offline Android app of free brain exercises: number patterns, matrix puzzles, memory cards, quick math, clock reading and games.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/kognius_app](https://github.com/markoboskoauroville/kognius_app) |
| Also called | kognius, brain exercises app |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Wellbeing, sound and meditation](../capabilities/wellbeing-sound-meditation.md) |
| Platforms | Android |
| Language | JavaScript (HTML in an Android WebView) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Run cognitive exercises (patterns, odd one out, memory cards, math, clock, counting)
- Offer three games (find the pairs, spot the colour, repeat the tune)
- Work offline with no internet permission, no ads
- Generate and verify puzzles with a stress test that checks one correct answer each
- Speak prompts from pre-made audio in several languages

## Ask for it when

- brain training app offline
- puzzles and memory games for an older person
- build and release the Mind Garden APK

## How to control it

No control API found.

## Inputs / Outputs

Outputs:

- APK releases

## Hardware

- Android phone

## Code worth reusing

- `tests/stress.js`: puzzle generator stress test checking exactly one correct answer
- `.claude/skills/release-apk/SKILL.md`: skill for releasing an APK to phone, Drive and GitHub

## Notes

By rule it is never built on GitHub Actions; the APK is built in the Claude cloud container or a VM on request. Default branch is a Claude cloud branch. Releases go to phone, Drive and the repo's releases folder.

## Docs in the repo

- `README.md`
- `CLAUDE.md`
