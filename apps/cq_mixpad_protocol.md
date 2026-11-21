# CQ MixPad Protocol

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Public database of the decoded private network protocol of Allen & Heath CQ mixers (CQ-12T), plus sniffer and injector tools.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/cq_mixpad_protocol](https://github.com/markoboskoauroville/cq_mixpad_protocol) |
| Also called | CQ protocol database, Allen & Heath CQ protocol, cq mixpad protocol |
| Visibility | public |
| Kind | data |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS, Linux |
| Language | Python (tools), JSON/Markdown (data) |
| Status | active |
| Last push | 2026-11-08 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Document every decoded CQ message in protocol.json and PROTOCOL.md (inputs, mix, outputs, FX, AMM, USB routing, SD transport, RTA)
- Sniff and record traffic between CQ MixPad and the desk (cq_mitm.py)
- Inject hex messages into a running MixPad session (cq_inject.sh)
- Dump and diff the desk's full state (cq_dump.py)
- Show which messages a click produced (cq_tour.py)

## Ask for it when

- control the Allen & Heath CQ mixer from code
- what is the CQ-12T network protocol
- set a CQ fader or mute over TCP
- decode more CQ MixPad messages

## How to control it

- Level: **cli**
- Type: cli
- Port: 51326

Actions:

- `cq_mitm.py DESK_IP --local`
- `cq_tour.py --last N`
- `cq_dump.py FIRST LAST`
- `cq_inject.sh "<hex>"`

**Before you call:** Start the man-in-the-middle sniffer first (python3 tools/cq_mitm.py `<desk-ip>` --local); the desk allows one client at a time, so the CQ MixPad app is used through it. Never test with Stereo Link, +48 V, sample rate or scene recall.

Example:

```
tools/cq_inject.sh "f7 0c 0c 0d 00 00 56 5e" # sends raw hex to the desk through the sniffer started with: python3 tools/cq_mitm.py <desk-ip> --local
```

More calls:

- show the last N decoded messages: `python3 tools/cq_tour.py --last 20`
- dump a range of captured messages: `python3 tools/cq_dump.py 100 200`

Evidence: README.md, tools/, protocol.json (desk TCP 51326, MIDI TCP 51325)

## Inputs / Outputs

Inputs:

- live CQ MixPad traffic
- captures (not in git)

Outputs:

- protocol.json
- PROTOCOL.md

## Hardware

- Allen & Heath CQ-12T (and other CQ desks)

## Works with

- Talks to: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md), [CQ MixPad Tutorial (Mantra)](cq_mixpad_tutorial.md)
- Used by or talked to by: [CQ MixPad (Mantra)](CQ_MIXPAD_MANTRA.md), [Mantra Sandbox](MANTRA_SANDBOX.md), [OXI-CQ Bridge](oxi_e16_cq-12t.md)

## Code worth reusing

- `protocol.json`: Machine-readable CQ message format, channel numbers, value scales and decoded parameters for any app talking to a CQ
- `tools/cq_mitm.py`: Man-in-the-middle sniffer/injector for the CQ TCP session

## Notes

Source of truth for CQ protocol; frequency/time/ratio scales not yet calibrated. Never use Stereo Link, +48 V, sample rate or scene recall while testing. CQ allows one client at a time. Unofficial, MIT licence.

## Docs in the repo

- [README.md](https://github.com/markoboskoauroville/cq_mixpad_protocol/blob/HEAD/README.md)
- [TAKEOVER.md](https://github.com/markoboskoauroville/cq_mixpad_protocol/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/cq_mixpad_protocol/blob/HEAD/LESSONS.md)
