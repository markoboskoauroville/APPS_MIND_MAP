# Cause and Symptom (Uzrok i simptom)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Bilingual (Croatian/English) study of one pattern: treat the cause, but make an overwhelming symptom survivable first. Sixteen chapters, encrypted static site.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/CAUSE_AND_SYMPTOM](https://github.com/markoboskoauroville/CAUSE_AND_SYMPTOM) |
| Also called | Uzrok i simptom, CAUSE AND SYMPTOM |
| Visibility | public |
| Kind | content-book-guide |
| Category | [Knowledge, books and guides](../capabilities/knowledge-books-guides.md) |
| Platforms | Web |
| Language | HTML, Python (build), Markdown |
| Status | dormant |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Hold the English and Croatian manuscripts
- Build an encrypted site (AES-256-GCM) with an instant language toggle
- Hold the illustration prompt book (pencil cause, photoreal symptom)

## Ask for it when

- read the cause and symptom book
- the book about treating cause not symptom
- Croatian version of the study

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `BOOK_PASS='...' python3 build_site.py`

**Before you call:** Builds the book site from the repo; the passphrase is the owner's (never stored in the repo).

Example:

```
BOOK_PASS='<passphrase>' python3 build_site.py
```

Evidence: README.md Rebuilding section

## Inputs / Outputs

Inputs:

- EN.md
- HR.md

Outputs:

- docs/index.html

## Code worth reusing

- `build_site.py`: encrypt two Markdown manuscripts into one static page decrypted in the browser with a passphrase

## Notes

Both manuscripts and the passphrase are not readable in the built page without the passphrase. Build needs markdown and cryptography Python packages. Not an app.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/CAUSE_AND_SYMPTOM/blob/HEAD/README.md)
