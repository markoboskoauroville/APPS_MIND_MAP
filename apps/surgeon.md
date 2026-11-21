# Surgeon

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**Edits single files of a GitHub repo through the API without cloning it, and pushes the changes as one real commit.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/surgeon](https://github.com/markoboskoauroville/surgeon) |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS, Termux, Linux |
| Language | Python |
| Status | active |
| Last push | 2026-09-16 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | cli (command line or script only) |

## What it can do

- Fetch only the named files and keep a pristine copy to diff
- Search code, list directories and show files without keeping them
- Create a branch, add, delete and revert files
- Push all changes as one commit

## Ask for it when

- edit one file of a huge repo from the phone
- change a GitHub file without cloning
- make a one-commit change to a fork

## How to control it

- Level: **cli**
- Type: cli

Actions:

- `init`
- `branch`
- `find`
- `ls`
- `show`
- `get`
- `status`
- `diff`
- `push`
- `new`
- `rm`
- `revert`
- `sync`

**Before you call:** Surgeon works on a repo without a full checkout; run in a folder.

Example:

```
surgeon push -m "what and why"
```

More calls:

- list files and show one: `surgeon ls ; surgeon show README.md`
- status and diff: `surgeon status ; surgeon diff`

Evidence: README.md

## Inputs / Outputs

Inputs:

- GitHub repo via gh login

Outputs:

- git commits

## Code worth reusing

- `surgeon`: clone-less file fetch, diff and single-commit push through the GitHub API

## Notes

Needs python3 and a logged-in gh.

## Docs in the repo

- `README.md`
