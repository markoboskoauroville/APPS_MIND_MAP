# Donnie Horoscope

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Download site and web app for Donnie Horoscope, an Android astrology app rebuilt from the 1992 DOS program ZodiacSigns, with APK and manual.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/donnie-horoscope-releases](https://github.com/markoboskoauroville/donnie-horoscope-releases) |
| Also called | Donnie Horoscope releases, DonnieHoroscope, ZodiacSigns V1.66 revival |
| Visibility | public |
| Kind | website |
| Category | [Websites and pages](../capabilities/websites-pages.md) |
| Platforms | Android, Web, Cloud |
| Language | JavaScript |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Calculate birth charts (planets, Placidus/Koch houses, aspects, sensitive points) in the browser
- Draw the chart wheel and export an A4 PDF
- Pick birthplaces from an offline atlas of about 8,400 places with time zone and DST
- Open and save .HOR chart files and chart packs (.zip)
- Host the latest APK (downloads/DonnieHoroscope-latest.apk) and PDF manual
- Deploy by workflow to Cloudflare Pages

## Ask for it when

- make a birth chart horoscope
- open old ZodiacSigns .HOR files
- download the Donnie Horoscope APK
- astrology app on Android

## How to control it

No control API found.

Evidence: README.md; app/ is a browser PWA with no declared control API

## Inputs / Outputs

Inputs:

- .HOR chart files
- chart pack zips
- birth data

Outputs:

- chart wheel
- PDF export
- .HOR files

## Code worth reusing

- `app/atlas/`: Offline world city atlas (cities.tsv, countries.bin) with time zones for place lookup
- `app/donnie.js`: Astrology calculation engine compiled from the Android app code (planets, houses, aspects)
- `app/zip.js`: Small browser zip reader/writer for chart packs

## Notes

Release repo only: source of the Android app is elsewhere (named astro_dos in other docs, version 23 current). Privacy: no account, charts stay on the device or browser. Hosted at donniehoroscope.pages.dev. Named after a dog.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/donnie-horoscope-releases/blob/HEAD/README.md)
