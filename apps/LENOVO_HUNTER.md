# Lenovo Hunter

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android (Expo/React Native) stock and price hunter for the Lenovo Legion Tab Y700 Gen 3 across fourteen shops, with spoken alert when one gets stock.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/LENOVO_HUNTER](https://github.com/markoboskoauroville/LENOVO_HUNTER) |
| Also called | Lenovo Legion hunter, Legion Tab hunter |
| Visibility | public |
| Kind | app |
| Category | [Data, backups and misc](../capabilities/data-backups-misc.md) |
| Platforms | Android |
| Language | JavaScript (Expo/React Native) |
| Status | active |
| Last push | 2026-09-18 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | none (no control api found) |

## What it can do

- Ask fourteen shops in HR, DE and EU at once for stock and price
- Sort by region or by price
- Speak an alert when a shop goes from out of stock to in stock
- Take pinned product URLs per shop in settings
- Probe all shops from a laptop with npm run probe

## Ask for it when

- tell me when the Lenovo Legion tablet is in stock
- compare prices of the Y700 across shops
- watch a product's stock in many shops

## How to control it

No control API found.

## Inputs / Outputs

Outputs:

- stock cards
- spoken alert
- APK

## Code worth reusing

- `src/core/parse.js`: product page parsing: JSON-LD, meta, selectors, regex
- `src/core/http.js`: fetch with timeout, backoff, block detection
- `src/core/StoreScraper.js`: shop adapter interface and in-stock guard
- `src/adapters/`: per-shop adapters (nabava, geizhals, proshop, hgspot...)

## Notes

Hunts one product only. Search URLs are guesses; pin direct product URLs in settings or it will never report IN STOCK. Related to SHOP_FINDER.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/LENOVO_HUNTER/blob/HEAD/README.md)
