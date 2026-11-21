# Firefox Control

[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)

**firefoxctl: lets Claude Code drive Marko's own running Firefox through WebDriver BiDi with text in, text out, no screenshots.**

| Fact | Value |
|---|---|
| Repo | [markoboskoauroville/firefox-control](https://github.com/markoboskoauroville/firefox-control) |
| Also called | firefoxctl, firefox_control |
| Visibility | private (code not readable without access) |
| Kind | cli-tool |
| Category | [AI agents and Claude tooling](../capabilities/ai-agents-claude-tooling.md) |
| Platforms | macOS |
| Language | Python |
| Status | active |
| Last push | 2026-11-14 |
| Build / release | GitHub workflow: no; latest release: none recorded |
| Control level | other (other protocols) |

## What it can do

- List tabs, open URLs, read a page's visible text and links
- Click by CSS selector or visible text
- Fill form fields (password fields refused)
- Run JavaScript in a page and print JSON
- Download a URL with the tab's cookies without passing bytes through the model
- Restart Firefox with the control port on, restoring tabs

## Ask for it when

- read a web page in my Firefox cheaply
- click a button in my logged-in Firefox
- download a PDF from a page I am logged in to
- list my open Firefox tabs

## How to control it

- Level: **other**
- Type: cli, websocket
- Port: 9222 (Firefox WebDriver BiDi, localhost only)

Actions:

- `status`
- `launch`
- `tabs`
- `open`
- `text`
- `links`
- `click`
- `fill`
- `eval`
- `download`
- `activate`

**Before you call:** Firefox is started by firefoxctl launch with WebDriver BiDi on localhost 9222; -t picks a named tab alias.

Example:

```
firefoxctl -t yshai links pdf # the links of the tab alias yshai that contain 'pdf'
```

More calls:

- what is open: `firefoxctl tabs`
- open a page: `firefoxctl open https://example.com`
- page text: `firefoxctl text`
- run JavaScript: `firefoxctl eval "document.title"`

Evidence: README.md, firefoxctl

## Inputs / Outputs

Inputs:

- running Firefox with remote debugging port

Outputs:

- page text
- link lists
- downloads

## Works with

- Talks to: [Download, Copy and Move (Mantra) (was Download Monitor)](DOWNLOAD_MONITOR.md)
- Used by or talked to by: [Blender Control](blender-control.md), [Router SMS](router-sms.md)

## Code worth reusing

- `firefoxctl`: minimal WebDriver BiDi client: session, script.evaluate, cookie-based download

## Notes

Uses his own profile with logins. Firefox must be started via 'firefoxctl launch' (flag cannot be set by preference). Dock-started Firefox has no control port. Needs websocket-client.

## Docs in the repo

- `README.md`
- `TAKEOVER.md`
- `LESSONS.md`
