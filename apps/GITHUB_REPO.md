# GitHub Repo

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app: type a GitHub username, browse public repositories, open releases and download release files to the phone.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/GITHUB_REPO](https://github.com/markoboskoauroville/GITHUB_REPO) |
| Also called | GitHub Repo |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: v1 |
| Control level | none (no control api found) |

## What it can do

- List a user's public repositories newest first with a filter
- Show each repository's releases and files
- Download a release file with Android DownloadManager into Downloads
- Store an optional token encrypted with Android Keystore to raise the rate limit

## Ask for it when

- download an APK from someone's GitHub releases on the phone
- browse a GitHub user's repos on Android

## How to control it

No control API found.

## Notes

Public repositories only, even with a token.

## Docs in the repo

- `README.md`
