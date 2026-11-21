# Ethno Hrvatska song sheets

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Song sheets for Marko's ethno orchestra: lyrics, chords and notation as two-page PDFs for singers and guitarist, with a Swift viewer app.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/ETHNO-HRVATSKA](https://github.com/markoboskoauroville/ETHNO-HRVATSKA) |
| Also called | Etno orkestar, Ethno Hrvatska, Pjesme tekstovi |
| Visibility | public |
| Kind | content-book-guide |
| Category | [Knowledge, books and guides](../capabilities/knowledge-books-guides.md) |
| Platforms | macOS |
| Language | Python (PDF tools) + Swift (viewer) |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: yes; latest release: v2 |
| Control level | cli (command line or script only) |

## What it can do

- Hold hand-written .cho song sources (lyrics, chords, translation, form, doubts)
- Convert .cho to JSON and render PDFs with melody staff and frame-drum rhythm box
- Check every lyric line word for word against the source lyrics PDF
- Analyse rehearsal audio stems for tempo, key and chord path
- Show songs in a Swift app (app/*.swift)

## Ask for it when

- chords and lyrics for the ethno songs
- make a song sheet PDF
- check lyrics against the source
- rehearsal sheet for the guitarist

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `tools/cho2json.py`
- `tools/render_pdf.py [--png DIR]`
- `tools/check_lyrics.py`
- `tools/analysis/analyze.py`
- `tools/analysis/rhythm_check.py`
- `tools/analysis/melody_plot.py`

Example:

```
python3 tools/render_pdf.py # renders the song sheets to PDF; --png DIR for pictures
```

More calls:

- check the lyrics: `python3 tools/check_lyrics.py`
- chord file to JSON: `python3 tools/cho2json.py`

Evidence: TAKEOVER.md file table

## Inputs / Outputs

Inputs:

- songs/src/*.cho
- source/Pjesme tekstovi.pdf
- audio stems

Outputs:

- `PDFs/<nn>` `<Title>.pdf`
- songs/*.json

## Code worth reusing

- `tools/notation.py`: vector melody staff and frame-drum rhythm box for PDFs
- `tools/render_pdf.py`: JSON song data to two-page PDF with PyMuPDF and Open Sans
- `tools/check_lyrics.py`: verify lyric lines against a source PDF

## Notes

Public but unpromoted. Whisper (:8837) cannot transcribe sung rehearsal takes (hallucinates), do not use it for lyrics. songs/UNCERTAIN.md lists lines and chords needing Marko's ear. Swift app compiles only on GitHub Actions. Flipchart photos are cropped so no face shows.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/ETHNO-HRVATSKA/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/ETHNO-HRVATSKA/blob/HEAD/LESSONS.md)
