# OXI-CQ Bridge

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Python bridge that controls an Allen & Heath CQ-12T mixer from an OXI E16 knob controller via MIDI/NRPN, with a local web UI and a virtual E16.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/oxi_e16_cq-12t](https://github.com/markoboskoauroville/oxi_e16_cq-12t) |
| Also called | OXI E16 to CQ-12T, OCQ-12T replacement, oxi cq bridge |
| Visibility | public |
| Kind | app |
| Category | [Mixers, MIDI and audio hardware](../capabilities/mixer-midi-audio-hardware.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-21 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | http (own http routes) |

## What it can do

- Translate E16 encoder turns and pushes into CQ-12T NRPN (levels, pans, mutes), Program Change (scenes) and soft-key notes
- Send over USB MIDI or MIDI-over-TCP to the desk
- Edit the control mapping as plain JSON
- Show a live web UI mirroring all 16 encoders with a log, usable as a virtual E16 with no hardware
- Run 47 automated tests in four stages

## Ask for it when

- control the CQ-12T mixer with the OXI E16
- set CQ fader levels from rotary knobs
- test mixer control without hardware

## How to control it

- Level: **http**
- Type: http, midi
- Port: 8753

Actions:

- `GET /api/state`
- `GET /api/ports`
- `GET /api/stream (SSE)`
- `POST /api/inject {page,slot,role,value}`

**Before you call:** Start the bridge first with ./run.sh in the repo (web UI on 127.0.0.1:8753); real MIDI needs the optional mido packages, the core needs only python3. Hardware paths are untested in the docs.

Example:

```
curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":0,"role":"turn","value":64}'
```

More calls:

- press a knob (role push instead of turn): `curl -s -XPOST 127.0.0.1:8753/api/inject -H 'Content-Type: application/json' -d '{"page":0,"slot":1,"role":"push","value":127}'`
- current state of the virtual E16 and the mixer mapping: `curl -s 127.0.0.1:8753/api/state`
- list MIDI ports, or send to the desk over TCP or USB: `./run.sh --list-ports ; ./run.sh --input usb --output usb`
- live event stream (server-sent events): `curl -sN 127.0.0.1:8753/api/stream`

Evidence: oxi_cq_bridge/server.py lines 7-10; TAKEOVER.md quick start (./run.sh, port 8753)

## Inputs / Outputs

Inputs:

- OXI E16 over USB/Bluetooth MIDI or the virtual E16
- mapping JSON

Outputs:

- CQ-12T MIDI/NRPN over USB or TCP

## Hardware

- OXI Instruments E16
- Allen & Heath CQ-12T

## Works with

- Uses: [CQ MixPad Protocol](cq_mixpad_protocol.md)

## Code worth reusing

- `oxi_cq_bridge/cq_protocol.py`: Encode CQ-12T NRPN/PC/note messages
- `oxi_cq_bridge/server.py`: Dependency-free HTTP+SSE server with a web UI for MIDI controllers
- `oxi_cq_bridge/mapping.py`: JSON mapping engine from controller slots to mixer parameters

## Notes

Core needs only python3; real MIDI needs optional mido deps. Hardware paths marked untested in the docs (section 10 lists unproven work). The how_to_call body fields are illustrative; read server.py for exact JSON. Does not use the CQ private TCP 51326 protocol; uses the public MIDI NRPN control set. Request fields verified in oxi_cq_bridge/server.py and bridge.py of the public repo: page, slot (ints), role turn or push, value (int).

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/oxi_e16_cq-12t/blob/HEAD/TAKEOVER.md)
