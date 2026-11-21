# Marko Apps site (markoapps.pages.dev)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Generated site listing every public app of the account, one page each with what it does, technology and install line; catalog.json holds the data.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/MARKO_APPS](https://github.com/markoboskoauroville/MARKO_APPS) |
| Also called | markoapps.pages.dev, apps site |
| Visibility | public |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | Python + HTML |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Read the account's public repos with gh and write catalog.json and site pages
- Build pages offline from catalog.json
- Deploy to Cloudflare Pages through GitHub Actions
- Skip private and unpromoted repos, books, films and archives by name

## Ask for it when

- list all public apps
- website of Marko's apps
- install line for a Termux app
- public app catalog

## How to control it

No control API found.

Evidence: build.py --offline; no service

## Inputs / Outputs

Inputs:

- GitHub public repos via gh

Outputs:

- catalog.json
- site/apps/*.html

## Code worth reusing

- `build.py`: read GitHub account, build catalog.json and per-app pages
- `catalog.json`: machine-readable list of public apps with README text

## Notes

Public repos only by construction. build.py has hard-coded SKIP and UNPROMOTED lists. Cloudflare token is a GitHub secret. Last pushed 9.11.2026, may be stale.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/MARKO_APPS/blob/HEAD/README.md)
