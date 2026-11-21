# Router Credits (Android)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Android app that checks the remaining data on the SIM inside the home 4G router by driving the router's web page and parsing the operator's SMS reply.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/router-credits](https://github.com/markoboskoauroville/router-credits) |
| Also called | Router Credits, TP-Link data balance Android |
| Visibility | public |
| Kind | app |
| Category | [Remote control and networking](../capabilities/remote-control-networking.md) |
| Platforms | Android |
| Language | Kotlin |
| Status | active |
| Last push | 2026-11-09 |
| Build / release | GitHub workflow: yes; latest release: v6 |
| Control level | none (no control api found) |

## What it can do

- Open the router's admin page in a WebView and log in with the saved password
- Send the operator balance SMS from the router's own SMS page
- Poll the router inbox for the reply and parse used and total MB
- Optionally text the result to a chosen phone number through the router SIM
- Log every check and step to files, and read the router inbox into the log

## Ask for it when

- how much data is left on the router SIM
- check mobile data balance from the phone
- read the router's SMS inbox

## How to control it

No control API found.

Evidence: TAKEOVER.md (former README); app is a UI app, no server or intent API found in api.txt

## Inputs / Outputs

Inputs:

- router admin page
- router password (kept only on the phone)

Outputs:

- balance status
- log files router-credits.log and checks.jsonl

## Works with

- Uses: [Router SMS](router-sms.md)

## Code worth reusing

- `app/src/main/java/com/mantra/routercredits/Driver.kt`: WebView driver that logs in to the TP-Link router and sends/reads SMS
- `app/src/main/java/com/mantra/routercredits/Reply.kt`: Parser for the operator's balance reply (with unit test)

## Notes

The router allows one logged-in device, so a check logs other sessions off (Mac router tab, router-sms). No README file; docs are in TAKEOVER.md. Android twin of the Mac router-sms.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/router-credits/blob/HEAD/TAKEOVER.md)
