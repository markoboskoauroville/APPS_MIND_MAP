# Studio Setup (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Web page of the studio gear (audio, cameras, controllers) with product links, built from a products list.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/studio-setup-mantra](https://github.com/markoboskoauroville/studio-setup-mantra) |
| Also called | studio setup, studiosetupmantra |
| Visibility | private (code not readable without access) |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Web, Cloud |
| Language | HTML, Python |
| Status | active |
| Last push | 2026-11-01 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Build a single gear page from products.json
- Read product pages on a retail site to get title, availability, badge and image
- Be linked from every public app page

## Ask for it when

- update the studio gear page
- add a product to the studio setup page

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- products.json

Outputs:

- static page

## Code worth reusing

- `tools/amazon_item.py`: reads a retail product page for title, availability, badge and main image
- `site/build.py`: generates the static gear page from a product list

## Notes

Commercial link details are left out of this record. Publication was waiting on a registration step at last note.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
