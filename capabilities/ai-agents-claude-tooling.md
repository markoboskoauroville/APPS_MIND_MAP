[Back to the index](../CAPABILITIES.md)

# AI agents and Claude tooling

## Which one to pick: Controlling Claude Code sessions: phone, Mac, cloud

Phone: AGENT_MANAGER_ANDROID is the client of the Mac's AGENT_MANAGER phone door (8847, bearer token over Tailscale), where blockers are answered and tasks paused; CLAUDE_CODE_TERMUX installs Claude Code on the phone itself. Mac: SESSION_HUB (8890) and SESSION_ACK (8899) pass messages between sessions, CCMC (MANTRA CHAT, 8825) mirrors a session as a chat page, TALK_MODE talks to sessions by voice, CLAUDE_CONTROL (`claudectl pause`) stops everything Claude runs, COST_AGENT asks before paid calls. Cloud: vm-chromium drives claude.ai in a VM browser (`cvm ask`). CLAUDE_CODE_MONITOR is archived.

| You want | Use | How |
|---|---|---|
| see and steer my Claude agents from the phone | [Agent Manager (CEO) (Mantra) for Android (AGENT_MANAGER_ANDROID)](../apps/AGENT_MANAGER_ANDROID.md) |  |
| read the overview of all sessions and workers on the Mac side | [Agent Manager (CEO) (Mantra) (AGENT_MANAGER)](../apps/AGENT_MANAGER.md) | `curl -s -H 'Authorization: Bearer $(cat ~/Downloads/API/agent-manager-token.txt)' http://<mac-tailscale-address>:8847/overview` |
| send a message from one Claude session to another | [Session Hub (SESSION_HUB)](../apps/SESSION_HUB.md) | `hub send other-session "Please review the diff"` |
| send with delivery receipt | [Session Ack (ccmsg) (SESSION_ACK)](../apps/SESSION_ACK.md) | `ccmsg send <to> "text" then ccmsg wait <id>` |
| answer a session from a chat page, read answers aloud | [CCMC (MANTRA CHAT, the sister of Claude Code) (CCMC)](../apps/CCMC.md) | `curl -s -XPOST 127.0.0.1:8825/api/send -H 'Content-Type: application/json' -d '{"text":"Yes, go ahead"}'` |
| pause everything Claude is running | [Claude Control (Mantra) (CLAUDE_CONTROL)](../apps/CLAUDE_CONTROL.md) | `claudectl pause` |
| ask before any paid API call | [Cost Agent (Mantra) (COST_AGENT)](../apps/COST_AGENT.md) | `curl -s -XPOST 127.0.0.1:9047/ask -H 'Content-Type: application/json' -d '{"who":"queen","what":"describe 20 images","provider":"groq","estimate_usd":0.40,"items":20,"job":"img-batch-1"}'` |
| ask Claude in the cloud browser VM | [Chromium Virtual Machine (Mantra) (vm-chromium)](../apps/vm-chromium.md) | `cvm ask "Summarise the open tab in one sentence"` |
| install Claude Code on an Android phone | [Claude Code for Termux (CLAUDE_CODE_TERMUX)](../apps/CLAUDE_CODE_TERMUX.md) | `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/CLAUDE_CODE_TERMUX/main/install.sh -o cct.sh && bash cct.sh --proot` |

## Which one to pick: Ports and the door protocol: how any app is called

A Mantra Mac app listens on 127.0.0.1 only, on a port it claims by name in MANTRA_PORTS (registry file ~/.config/mantra-ports.json), and answers `GET /health`, `GET /api` (the declared actions) and `POST /api/<action>` with a JSON body; the reply is `{ok, result}` or `{ok:false, error}`. Mantra Door is the token-guarded gateway for the phone (header X-Mantra-Token, token in ~/.config/mantra-door.token, Tailscale address only): `GET /apps`, `POST /apps/<id>/launch`, and any `/apps/<id>/api/...` is passed on to the app, starting it if needed. Python code uses `mantra_remote.py` (`remote.call("dock-switcher", "show")`). To give a NEW app a port run `mantra-ports next`, claim it at start with `ports.claim("my-app", N)` (Swift `Ports.claim`, Lua `ports.lua`) and ask by name everywhere else. Several numbers are claimed twice, notably 8965 (MANTRA_ROOM, MPA_LESSONS_ANALYZER, SECOND_TAKE_REMOTE), 8837 (MANTRA_VOICE, VOICE_ENGINE) and 8847 (AGENT_MANAGER, retired spotlight): check which app answers `GET /health`.

| You want | Use | How |
|---|---|---|
| get a free port for a new app and register it | [Mantra Ports (MANTRA_PORTS)](../apps/MANTRA_PORTS.md) | `mantra-ports next` |
| claim the port in a Python server | [Mantra Ports (MANTRA_PORTS)](../apps/MANTRA_PORTS.md) | `import sys, os; sys.path.insert(0, os.path.expanduser('~/.local/lib/mantra')); import ports; PORT = ports.claim('my-app', 8962)` |
| find where a service runs | [Mantra Ports (MANTRA_PORTS)](../apps/MANTRA_PORTS.md) | `mantra-ports find voice` |
| press, open or quit a star app from the phone or an HTTP client | [Star API (Mantra) (STAR_API)](../apps/STAR_API.md) | `curl -s -XPOST 127.0.0.1:8863/apps/timer/press -H "Content-Type: application/json" -d '{"label":"stopwatch"}'` |
| drive an app that serves its own door, e.g. Meditation Room | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](../apps/MANTRA_ROOM.md) | `curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'` |
| control the Android phone through its Claude Control door and the macro door | [Mantra Remote Viewing (Mantra Remote) (MANTRA_REMOTE_VIEWING)](../apps/MANTRA_REMOTE_VIEWING.md) | `rvctl pixel tap 540 1200 --label "NDI" --watched --expect com.mantraproductions.manualcamera` |

### [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md)

macOS; API: http 8847. Main call: `curl -s -H 'Authorization: Bearer $(cat ~/Downloads/API/agent-manager-token.txt)' http://<mac-tailscale-address>:8847/overview`

Before: Phone-door style, not the /health + /api contract: the door is bound to the Mac's Tailscale address only (not 127.0.0.1), with a bearer token read from a file on the Mac. Read first; actions are written as command files for the master session to carry out.

- see what all my Claude sessions are doing (Agent Manager)
- who is blocked and why (Agent Manager) - call: `curl -s -H "Authorization: Bearer $TOKEN" http://<mac-tailscale-address>:8847/blockers`
- open the master Claude session (Agent Manager)
- check Claude usage this week (Agent Manager)
- pause or message an agent from the phone (Agent Manager) - call: `curl -s -XPOST -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' http://<mac-tailscale-address>:8847/command -d '{"slug":"MANTRA_ROOM","text":"Run the tests"}'`

### [Agent Manager (CEO) (Mantra) for Android](../apps/AGENT_MANAGER_ANDROID.md)

Android; API: none

- check my Claude agents from the phone (Agent Manager for Android)
- answer a blocked agent from the phone (Agent Manager for Android)
- stop a running task from the phone (Agent Manager for Android)

### [Brain Brake night bus](../apps/BRAINBREAK_BUS.md)

macOS; API: cli. Main call: `python3 tools/chatlink.py send "Scene 3 render is done"`

- let the chat Claude and Claude Code talk overnight (Brain Brake night bus)
- read the claude.ai tab from the Mac (Brain Brake night bus)
- send a message to the chat session (Brain Brake night bus)

### [Brain Freedom](../apps/BRAIN_FREEDOM.md)

macOS/Web; API: http 8770. Main call: `curl -s -XPOST 127.0.0.1:8770/api/say -H 'Content-Type: application/json' -d '{"text":"Good morning"}' # body field names are not in the docs`

Before: The port is 8770 or the next free one, written to ~/brain_freedom/port.

- work on the film by voice with the coding agent (Brain Freedom)
- dictate to the coding agent in a terminal (Brain Freedom)
- drop a render and get its raw link (Brain Freedom)

### [CCMC (MANTRA CHAT, the sister of Claude Code)](../apps/CCMC.md)

macOS/Web; API: door 8825. Main call: `curl -s -XPOST 127.0.0.1:8825/api/send -H 'Content-Type: application/json' -d '{"text":"Yes, go ahead"}' # the answer lands in ~/.tspeak/inbox where the Claude Code session watches`

Before: MANTRA CHAT (chatd.py, Flask) runs when 'Sister' is ticked in the star menu, not by the hook; it binds upward from 8825 and writes the winning port to ~/.tspeak/port.txt. It mirrors the Claude Code session of the open project and opens only in Chrome.

- read Claude's answer aloud (CCMC) - call: `curl -s -XPOST 127.0.0.1:8825/api/message -H 'Content-Type: application/json' -d '{"role":"system","text":"Build finished","project":"MANTRA_ROOM"}'`
- mirror my Claude Code session on a web page (CCMC)
- talk to Claude Code through a page (CCMC)
- speak the last answer with Beatrice (CCMC) - call: `curl -s -XPOST 127.0.0.1:8825/api/read/<message-id> -H 'Content-Type: application/json' -d '{"speed":1.0}'`

### [Claude Code hub](../apps/claude-code.md)

macOS; API: cli. Main call: `python3 ~/Developer/claude-code/handover.py brief`

Before: Run from a checkout in ~/Developer/claude-code.

- where did I stop (Claude Code hub)
- what is pending on my projects (Claude Code hub)
- list my projects (Claude Code hub)
- continue project X (Claude Code hub)
- close the session and store the state (Claude Code hub)
- find which repo holds a program (Claude Code hub)

### [Claude Code Mantra OS](../apps/claude-code-mantra-os.md)

Cloud; API: none

- how should I split work across Claude Code subagents (Claude Code Mantra OS)
- template for briefing a child agent (Claude Code Mantra OS)
- save tokens in Claude Code (Claude Code Mantra OS)
- route tasks to Haiku, Sonnet or Opus (Claude Code Mantra OS)

### [Claude Code Session Names](../apps/claude-code-session-names.md)

macOS/Termux/Linux/Cloud; API: none. Main call: `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/claude-code-session-names/main/install.sh | bash -s -- mac`

- name my Claude Code sessions automatically (Claude Code Session Names)
- tell Mac and phone Claude sessions apart (Claude Code Session Names)
- install the session name hook (Claude Code Session Names)

### [Claude Control (Mantra)](../apps/CLAUDE_CONTROL.md)

macOS; API: cli. Main call: `claudectl pause # pauses every registered tool with background work or API calls`

Before: Tools register in ~/.config/claude-control/tools.json (pause, resume, status routes); it never stops itself, the process on :8837, Macro Recorder, Talk Mode, Voice to Text, Firefox, Tailscale or Connection Keeper.

- pause everything Claude is doing (Claude Control)
- stop all Claude agents now (Claude Control)
- resume Claude sessions (Claude Control)
- freeze Claude Code to save money or CPU (Claude Control)

### [Claude Persist](../apps/claude-persist.md)

macOS; API: cli. Main call: `python3 persist.py status`

Before: Keeps a Claude Code session alive across stops (ok/fail/tick bookkeeping).

- keep Claude Code retrying after a dropped connection (Claude Persist)
- auto resume a session after quota reset (Claude Persist)
- see which sessions are waiting (Claude Persist)

### [Claude Remote (Mantra)](../apps/CLAUDE_REMOTE.md)

macOS; API: none

- show usage in the Claude Code status line (Claude Remote)
- install the Claude Code status bar mod (Claude Remote)

### [Claude Talkie](../apps/Claude_Toki.md)

Linux/Web/Cloud; API: http. Main call: `curl -s <site>/claude/health # also POST /claude/api/speech; the chat stream is server-sent events`

Before: Hosted web service ('Claude Talkie'); the base address is not published in this map.

- talk to Claude with a microphone and hear the answer (Claude Talkie)
- read Claude answers aloud with highlighted words (Claude Talkie)

### [Cost Agent (Mantra)](../apps/COST_AGENT.md)

macOS; API: http 9047. Main call: `curl -s -XPOST 127.0.0.1:9047/ask -H 'Content-Type: application/json' -d '{"who":"queen","what":"describe 20 images","provider":"groq","estimate_usd":0.40,"items":20,"job":"img-batch-1"}' # answers {answer: yes|no, reason, id}`

Before: Cost Agent (Mantra) must be running (costagent.py serve); local callers need no token, callers from another machine send X-Cost-Token. Silence and timeout are a NO.

- ask me before spending money (Cost Agent)
- how much have I spent on APIs today (Cost Agent)
- block paid calls until I approve (Cost Agent)
- cost guard for Queen (Cost Agent)

### [Firefox Control](../apps/firefox-control.md)

macOS; API: other. Main call: `firefoxctl -t yshai links pdf # the links of the tab alias yshai that contain 'pdf'`

Before: Firefox is started by firefoxctl launch with WebDriver BiDi on localhost 9222; -t picks a named tab alias.

- read a web page in my Firefox cheaply (Firefox Control)
- click a button in my logged-in Firefox (Firefox Control)
- download a PDF from a page I am logged in to (Firefox Control)
- list my open Firefox tabs (Firefox Control)

### [Fooocus Streamlit front end](../apps/marko-fooocus.md)

Web/Cloud; API: none

- generate images with Fooocus from a web page (Fooocus Streamlit front end)
- run Fooocus on a free Colab GPU (Fooocus Streamlit front end)

### [German to English (Mantra)](../apps/GERMAN_TO_ENGLISH.md)

Web; API: none

- read a German website in English (German to English)
- translate this German page automatically (German to English)

### [Groq Explorer](../apps/GROQ_EXPLORER.md)

Android; API: none

- try every Groq model from the phone (Groq Explorer)
- test Groq speech to text on Android (Groq Explorer)
- see the exact Groq API call that was sent (Groq Explorer)

### [Macro Skills](../apps/MACRO_SKILLS.md)

macOS; API: cli. Main call: `macroskill has --json "snap a window left"`

Before: macroskill has searches the stored macros by words (id, title, app, tags); only if it finds nothing, build the macro in Macro Recorder (MANTRA_MACRO) and then macroskill add it. Installed as ~/.local/bin/macroskill.

- is there already a macro for this (Macro Skills) - call: `macroskill run <id> # same as macro run "<macro name>"`
- snap a window left (Macro Skills)
- switch the Gemini account (Macro Skills)
- pause all macros (Macro Skills)
- pick an NDI monitor source (Macro Skills)

### [MAI Worker (maiwork)](../apps/MAI_WORKER.md)

macOS; API: cli. Main call: `maiwork "<task>" --cwd ~/Developer/SOMETHING --model mai-code-2`

Before: Run inside a checkout; --approve all|assisted|manual sets how much it may do alone.

- delegate a task to the Copilot agent in VS Code (MAI Worker)
- let MAI Code 2 write a macro (MAI Worker)
- run a worker agent from a script (MAI Worker)
- ask VS Code's agent and get the answer on stdout (MAI Worker)

### [Mantra Bridge](../apps/MANTRA_BRIDGE.md)

macOS/Android; API: http. Main call: `python3 -m bridge.server --project ~/Developer/SOME_REPO # run in mac/; then GET /health and the SSE stream`

Before: Run in mac/ of the repo; the message routes are in mac/bridge/server.py (not harvested).

- drive Claude Code on the Mac from the phone (Mantra Bridge)
- stream a Claude Code session over HTTP (Mantra Bridge)

### [Mantra Chrome Extensions](../apps/MANTRA_CHROME_EXTENSIONS.md)

macOS/Chrome; API: none

- check a Chrome extension before loading it (Mantra Chrome Extensions)
- build or debug a Chrome extension (Mantra Chrome Extensions)
- act inside a web page through an extension (Mantra Chrome Extensions)
- benchmark an AI on writing extensions (Mantra Chrome Extensions)

### [Mantra Manifest](../apps/MANTRA_MANIFEST.md)

macOS/Android/Linux/Cloud; API: none

- what are the rules for building a new app (Mantra Manifest)
- read the manifest before starting (Mantra Manifest)
- find the shared module for X (Mantra Manifest)

### [Mantra Router](../apps/MANTRA_ROUTER.md)

macOS/Android/Termux/Linux; API: none. Main call: `/router auto`

- choose the right Claude model for a prompt (Mantra Router)
- route prompts between Haiku Sonnet and Opus (Mantra Router)
- bypass the router (Mantra Router)

### [Mantra Sandbox](../apps/MANTRA_SANDBOX.md)

macOS/Android; API: cli. Main call: `sandbox run macros/cqmixpad/tab_fader.macro # plays a recorded macro inside the headless Android emulator`

Before: sandbox create once, sandbox start to boot the emulator; it has its own screen, touch and keys through adb so the owner's phone is never touched.

- run an Android app without touching my screen (Mantra Sandbox)
- test a phone app in an emulator by script (Mantra Sandbox)
- drive CQ MixPad in the background (Mantra Sandbox)
- automate an Android app in parallel with my own work (Mantra Sandbox)

### [Mantra Voice Switch](../apps/MANTRA_VOICE_SWITCH.md)

macOS/Linux; API: none. Main call: `/vox off`

- mute the voice for this Claude chat (Mantra Voice Switch)
- turn spoken replies back on (Mantra Voice Switch)

### [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md)

macOS; API: http 8765. Main call: `python3 tools/queen_capi.py send CHAT_ID "Run the focused tests" --wait`

Before: Queen's Swift app on 8765 and its Python backend on 8766 must be running; a CAPI chat id comes from /api/capi/list or /api/capi/new.

- ask Queen to do a task on the Mac (Queen, server and tools) - call: `curl -s 127.0.0.1:8765/api/ableton/capabilities ; curl -s 127.0.0.1:8765/api/capi/list`
- control Ableton Live by text command (Queen, server and tools)
- set the Ableton tempo (Queen, server and tools) - call: `curl -s -XPOST 127.0.0.1:8765/api/ableton/action -H 'Content-Type: application/json' -d '{"action":"set_tempo","arguments":{"bpm":120}}'`
- send a prompt to Claude Code or Gemini from a script (Queen, server and tools)
- Queen CAPI python client (Queen, server and tools)
- auto-update the Queen app (Queen, server and tools)

### [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md)

macOS; API: http 8765. Main call: `python3 tools/queen_capi.py send CHAT_ID "Run the focused tests" --wait`

Before: Queen's Swift app on 8765 and its Python backend on 8766 must be running; a CAPI chat id comes from /api/capi/list or /api/capi/new.

- ask Queen to do a task on the Mac (Queen auto-update) - call: `curl -s 127.0.0.1:8765/api/ableton/capabilities ; curl -s 127.0.0.1:8765/api/capi/list`
- control Ableton Live by text command (Queen auto-update)
- set the Ableton tempo (Queen auto-update) - call: `curl -s -XPOST 127.0.0.1:8765/api/ableton/action -H 'Content-Type: application/json' -d '{"action":"set_tempo","arguments":{"bpm":120}}'`
- send a prompt to Claude Code or Gemini from a script (Queen auto-update)
- Queen CAPI python client (Queen auto-update)
- auto-update the Queen app (Queen auto-update)

### [Queen, Mac app (Groq AI Studio (Mantra))](../apps/GROQ_AI_STUDIO_MAC.md)

macOS; API: door 8765. Main call: `curl -s -XPOST 127.0.0.1:8765/api/ax/read -H 'X-Queen-Token: <token from the local token file>' -H 'Content-Type: application/json' -d '{"app":"Firefox","query":"WhatsApp"}'`

Before: This repo is the Mac app and the axread command; the Python server on 8765 is in groq_ai_studio and must be running. Fields of /api/ax/read (from the public repo): app, window?, query?, depth?, roles?, max?, timeout?, frames?, focused?.

- chat with Queen on the Mac (Queen, Mac app)) - call: `curl -s 127.0.0.1:8765/api/chats`
- read the text of a window without screenshots (Queen, Mac app))
- check my last WhatsApp messages through accessibility (Queen, Mac app)) - call: `curl -s -XPOST 127.0.0.1:8765/api/whatsapp/ax/latest -H 'X-Queen-Token: <token>'`

### [Session Ack (ccmsg)](../apps/SESSION_ACK.md)

macOS/Linux/Cloud; API: http 8899. Main call: `ccmsg send <to> "text" then ccmsg wait <id>`

Before: Listens on loopback and the Mac's Tailscale address; trust by tailscale whois (no token). Address configurable by CCMSG_URL.

- confirm that a message between Claude sessions was received (Session Ack)
- track message receipts between sessions (Session Ack)
- mailbox for Claude Code sessions (Session Ack)
- did the other session read my message (Session Ack)

### [Session Hub](../apps/SESSION_HUB.md)

macOS/Cloud; API: http 8890. Main call: `hub send other-session "Please review the diff" # HTTP: curl -s -XPOST 127.0.0.1:8890/send -H 'Content-Type: application/json' -d '{"from":"me","to":"other-session","text":"Please review the diff","id":"m1"}'`

Before: Sessions register first: hub register (POST /register {name,sid,machine,kind,cwd}) and keep alive with hub beat; to = a session name, the base name before ' (', a sid prefix, or all; 'marko' reaches the window.

- message another Claude Code session (Session Hub)
- see which Claude sessions are running (Session Hub)
- broadcast to all Claude sessions (Session Hub)
- session to session chat hub (Session Hub)

### [Sister App (Mantra)](../apps/SISTER_APP.md)

macOS; API: accessibility. Main call: `star press "sister" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- turn the chat server on or off (Sister App)
- open the Mantra chat page (Sister App)

### [Suno Controller (Mantra)](../apps/CHROME_SUNO_CONTROLLER.md)

macOS/Chrome; API: http 8869. Main call: `sunoctl record https://suno.com/song/<id> ~/Music/Suno/air.wav`

Before: Sound Recorder (Mantra) must be running (its door 8869 is polled by the Chrome extension); Suno open in Firefox/Chrome.

- create a song on Suno from lyrics (Suno Controller) - call: `sunoctl play ; sunoctl pause`
- record a Suno song to a WAV file (Suno Controller)
- list my latest Suno songs (Suno Controller)
- download Suno songs by recording Chrome audio (Suno Controller)

### [Surgeon](../apps/surgeon.md)

macOS/Termux/Linux; API: cli. Main call: `surgeon push -m "what and why"`

Before: Surgeon works on a repo without a full checkout; run in a folder.

- edit one file of a huge repo from the phone (Surgeon)
- change a GitHub file without cloning (Surgeon)
- make a one-commit change to a fork (Surgeon)


## Retired - do not use

- [Claude Code Monitor (Mantra) (retired)](../apps/CLAUDE_CODE_MONITOR.md) - Archived on GitHub.
