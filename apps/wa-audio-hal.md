# WhatsApp audio HAL (moved) (retired)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

> **Retired - do not use.** Replaced by WHATSAPP_REMOTE_VIEWER.

**Moved: modified Android audio HAL so WhatsApp calls in a VM Android container send and receive audio from local devices.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/wa-audio-hal](https://github.com/markoboskoauroville/wa-audio-hal) |
| Visibility | private (code not readable without access) |
| Kind | library-module |
| Category | [Android and Termux](../capabilities/android-termux.md) |
| Platforms | Android, Linux |
| Language | C |
| Status | retired |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Provide a modified AOSP audio_hw.c with changes marked WA:
- Install or roll back the HAL in a VM Android container

## Ask for it when

- route audio of WhatsApp calls in the Android VM

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `install-on-vm.sh install`
- `install-on-vm.sh rollback`

**Before you call:** Installs on the VM; rollback undoes it.

Example:

```
tools/install-on-vm.sh install
```

Evidence: TAKEOVER.md, tools/install-on-vm.sh

## Code worth reusing

- `src/audio_hw.c`: AOSP audio HAL with hooks for custom audio routing

## Notes

README says it moved to WHATSAPP_REMOTE_VIEWER/hal on 14.11.2026; this repo is archived. RETIRED/SUPERSEDED: use WHATSAPP_REMOTE_VIEWER instead. The code moved to the repo WHATSAPP_REMOTE_VIEWER (not in this map).

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
