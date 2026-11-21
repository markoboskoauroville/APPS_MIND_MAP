# Astro DOS

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android remake of a classic MS-DOS astrology program, reverse-engineered from the original, with a modern skin.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/astro_dos](https://github.com/markoboskoauroville/astro_dos) |
| Also called | astrodos, zodiac |
| Visibility | private (code not readable without access) |
| Kind | app |
| Category | [Knowledge, books and guides](../capabilities/knowledge-books-guides.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: none recorded |
| Control level | none (no control api found) |

## What it can do

- Calculate birth horoscopes (planets, houses, aspects) with the engine ported from the DOS original
- Render the original text-mode screens with CP437 and EGA/VGA-accurate fonts
- Offer a modern touch UI on top of the faithful mode
- Pick a birth place from a built-in city atlas and map picker
- Export charts to PDF
- Save and open chart files in the original format

## Ask for it when

- make a birth chart on the phone
- astrology horoscope app
- open old DOS astrology chart files
- draw a chart wheel and export PDF

## How to control it

No control API found.

## Inputs / Outputs

Inputs:

- birth data (name, place, date, time)
- chart files of the DOS program

Outputs:

- horoscope charts
- PDF export

## Code worth reusing

- `android/app/src/main/java/com/astrodos/zodiac`: Kotlin horoscope engine (planets, houses, aspects) and text-mode screen renderer
- `analysis/`: reverse-engineering notes of the DOS binary and its calculation engine

## Notes

Original DOS binary and analysis notes are kept in the repo. No remote control API.

## Docs in the repo

- `README.md`
