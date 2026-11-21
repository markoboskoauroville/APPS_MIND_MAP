# Key Tester (Android)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app for testing API keys per provider; its README is only a download link, the source tree names a key parser, provider table and Google matrix.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/Key_Tester](https://github.com/markoboskoauroville/Key_Tester) |
| Also called | Key Tester |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-10-31 |
| Build / release | GitHub workflow: yes; latest release: latest |
| Control level | none (no control api found) |

## What it can do

- Test API keys per provider (source files KeyParser.kt, Providers.kt, MainActivity.kt)
- Run a Google per-API matrix with a shared endpoints table (GoogleMatrix.kt, assets/endpoints.json)
- Show the interface in English and Croatian (values-hr strings)

## Ask for it when

- test an API key on the phone
- check which provider a key belongs to

## How to control it

No control API found.

Evidence: tree.txt lists KeyParser.kt, Providers.kt, GoogleMatrix.kt, assets/endpoints.json and values-hr; README.md is two lines (download link). Behaviour not confirmed from docs.

## Works with

- Uses: [KeyringTester (Mantra)](KEY_RING_TESTER.md)
- Used by or talked to by: [KeyringTester (Mantra)](KEY_RING_TESTER.md), [Sample Player, Android](SAMPLE_PLAYER.md)

## Code worth reusing

- `app/src/main/assets/endpoints.json`: copy of the shared provider test table

## Notes

Android sibling of KeyringTester (Mantra); endpoints.json is copied from the Mac repo. Claims are from the file names in tree.txt only, the README says nothing about behaviour. Mac sibling: KEY_RING_TESTER (KeyringTester (Mantra)).

## Docs in the repo

- `README.md`

_Low confidence: little was documented in this repository. Check the code before relying on this card._
