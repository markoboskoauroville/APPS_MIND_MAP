# Cost Agent (Mantra)

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Gate that asks Marko YES or NO with the dollar estimate before any paid API call (Groq, images, Speechify above allowance) and keeps spending ledgers.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/COST_AGENT](https://github.com/markoboskoauroville/COST_AGENT) |
| Also called | Cost Agent, costagent, cost gate |
| Visibility | public |
| Kind | service-daemon |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python (gate) + Swift (dialog and dashboard) |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: yes; latest release: v3 |
| Control level | http (own http routes) |

## What it can do

- Ask for approval with an estimated cost before a paid job runs
- Remember a NO for ten minutes and ask again when a job exceeds estimate plus 20 percent
- Let calls under the ask line ($0.10) pass but record them and add up split calls
- Show today, week and month spending per provider and process on a dashboard
- Also ask on the phone (spoken question and a YES/NO page) when Marko is away
- Let free providers and Speechify within a daily allowance pass

## Ask for it when

- ask me before spending money
- how much have I spent on APIs today
- block paid calls until I approve
- cost guard for Queen

## How to control it

- Level: **http**
- Type: http, cli
- Port: 9047 (MANTRA_PORTS id costagent)

Actions:

- `GET /health`
- `GET /summary`
- `GET /pending`
- `GET /history`
- `POST /ask {who,what,provider,estimate_usd,items?,job?,timeout?}`
- `POST /spent {who,provider,usd,items?,job?,what?}`
- `POST /answer {id,answer}`
- `GET /q/<id>?t=TOKEN`
- `costagent.py serve`
- `costagent.py ask WHO WHAT PROVIDER ESTIMATE_USD [--items N] [--job J] [--timeout S]`
- `costagent.py spent WHO PROVIDER USD`
- `costagent.py status`
- `Cost Agent (Mantra).app --ask "<text>"`

**Before you call:** Cost Agent (Mantra) must be running (costagent.py serve); local callers need no token, callers from another machine send X-Cost-Token. Silence and timeout are a NO.

Example:

```
curl -s -XPOST 127.0.0.1:9047/ask -H 'Content-Type: application/json' -d '{"who":"queen","what":"describe 20 images","provider":"groq","estimate_usd":0.40,"items":20,"job":"img-batch-1"}' # answers {answer: yes|no, reason, id}
```

More calls:

- same from a shell, exit 0 = YES, 1 = NO: `python3 gate/costagent.py ask queen "describe 20 images" groq 0.40 --items 20 --job img-batch-1`
- record a real spend afterwards: `python3 gate/costagent.py spent queen groq 0.37 --job img-batch-1`
- today, week and month per provider: `python3 gate/costagent.py status`
- what is waiting for an answer: `curl -s 127.0.0.1:9047/pending`

Evidence: gate/costagent.py header line 15, TAKEOVER.md

## Inputs / Outputs

Inputs:

- cost questions from callers (who, job, estimate)

Outputs:

- YES/NO answer
- decisions.jsonl and ledgers in ~/.mantra-os/cost-agent

## Works with

- Uses: [Mantra Ports](MANTRA_PORTS.md)
- Talks to: [Termux Voice (voiced)](TERMUX_VOICE.md), [Chromium Virtual Machine (Mantra)](vm-chromium.md)

## Code worth reusing

- `gate/costagent.py`: stdlib approval gate with estimates, per-job grants, ledgers and a token-guarded remote path

## Notes

Local callers need no token; the VM must send X-Cost-Token. Test with COSTAGENT_DATA, COSTAGENT_PORT, COSTAGENT_NO_UI=1 and a fake provider, never a real paid call. Rule lives in MANTRA_MANIFEST modules/cost-agent.md. Checked against gate/costagent.py of the public repo: a NO is remembered for 10 minutes per job (deny_memory_s 600), calls under 0.10 USD pass but add up over 10 minutes, a job over estimate plus 20 percent asks again.

## Docs in the repo

- [TAKEOVER.md](https://github.com/markoboskoauroville/COST_AGENT/blob/HEAD/TAKEOVER.md)
- [LESSONS.md](https://github.com/markoboskoauroville/COST_AGENT/blob/HEAD/LESSONS.md)
