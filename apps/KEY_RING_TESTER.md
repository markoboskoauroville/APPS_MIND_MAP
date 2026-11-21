# KeyringTester (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Mac app that finds API keys in files by shape and tests each with the cheapest read its provider offers, showing a masked table of what works.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/KEY_RING_TESTER](https://github.com/markoboskoauroville/KEY_RING_TESTER) |
| Also called | Key Ring Tester, KeyringTester |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Keys, secrets and infrastructure](../capabilities/keys-secrets-infrastructure.md) |
| Platforms | macOS |
| Language | Swift (original Python tester) |
| Status | active |
| Last push | 2026-11-04 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Parse keys out of any file or a whole folder by their shape and labels
- Test each key with a harmless read such as a model list or token request
- Ask one Google key across about 32 Google APIs and show each verdict
- Show results as a masked table (works, invalid, quota, rate-limited and so on)
- Print the table from the command line
- Share one endpoints table with the Android Key_Tester

## Ask for it when

- test which of my API keys still work
- check if a Google key can use Maps or Gemini
- find dead or out-of-credit keys

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `--test <files>`
- `--parse <files>`
- `--open <files>`
- `--all`
- `--expand`

Example:

```
"/Applications/KeyringTester (Mantra).app/Contents/MacOS/KeyringTester" --test ~/keys.txt # tests every key of the file; never prints a key
```

More calls:

- only parse and list providers: `... --parse ~/keys.txt`
- test all files it knows: `... --all`

Evidence: README.md; TAKEOVER.md

## Inputs / Outputs

Inputs:

- key files in the local API folder

Outputs:

- masked results table

## Works with

- Uses: [Key Tester (Android)](Key_Tester.md)
- Used by or talked to by: [App Store (Mantra)](APP_STORE.md), [Key Tester (Android)](Key_Tester.md)

## Code worth reusing

- `shared/endpoints.json`: provider and Google API test table: key shapes, hints and the cheapest test call per provider
- `app/Engine.swift`: key parser by shape and classifier of HTTP results with mask() output

## Notes

Never prints a full key. Used by App Store settings and guide apps to check key rings.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
