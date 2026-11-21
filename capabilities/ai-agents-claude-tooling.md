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

- see what all my Claude sessions are doing -> [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md) (macOS; API: http 8847) - call: `curl -s -H 'Authorization: Bearer $(cat ~/Downloads/API/agent-manager-token.txt)' http://<mac-tailscale-address>:8847/overview`
- who is blocked and why -> [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md) (macOS; API: http 8847)
- open the master Claude session -> [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md) (macOS; API: http 8847)
- check Claude usage this week -> [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md) (macOS; API: http 8847)
- pause or message an agent from the phone -> [Agent Manager (CEO) (Mantra)](../apps/AGENT_MANAGER.md) (macOS; API: http 8847)
- check my Claude agents from the phone -> [Agent Manager (CEO) (Mantra) for Android](../apps/AGENT_MANAGER_ANDROID.md) (Android; API: none)
- answer a blocked agent from the phone -> [Agent Manager (CEO) (Mantra) for Android](../apps/AGENT_MANAGER_ANDROID.md) (Android; API: none)
- stop a running task from the phone -> [Agent Manager (CEO) (Mantra) for Android](../apps/AGENT_MANAGER_ANDROID.md) (Android; API: none)
- let the chat Claude and Claude Code talk overnight -> [Brain Brake night bus](../apps/BRAINBREAK_BUS.md) (macOS; API: cli) - call: `python3 tools/chatlink.py send "Scene 3 render is done"`
- read the claude.ai tab from the Mac -> [Brain Brake night bus](../apps/BRAINBREAK_BUS.md) (macOS; API: cli)
- send a message to the chat session -> [Brain Brake night bus](../apps/BRAINBREAK_BUS.md) (macOS; API: cli)
- work on the film by voice with the coding agent -> [Brain Freedom](../apps/BRAIN_FREEDOM.md) (macOS/Web; API: http 8770) - call: `curl -s -XPOST 127.0.0.1:8770/api/say -H 'Content-Type: application/json' -d '{"text":"Good morning"}' # body field names are not in the docs`
- dictate to the coding agent in a terminal -> [Brain Freedom](../apps/BRAIN_FREEDOM.md) (macOS/Web; API: http 8770)
- drop a render and get its raw link -> [Brain Freedom](../apps/BRAIN_FREEDOM.md) (macOS/Web; API: http 8770)
- read Claude's answer aloud -> [CCMC (MANTRA CHAT, the sister of Claude Code)](../apps/CCMC.md) (macOS/Web; API: door 8825) - call: `curl -s -XPOST 127.0.0.1:8825/api/send -H 'Content-Type: application/json' -d '{"text":"Yes, go ahead"}' # the answer lands in ~/.tspeak/inbox where the Claude Code session watches`
- mirror my Claude Code session on a web page -> [CCMC (MANTRA CHAT, the sister of Claude Code)](../apps/CCMC.md) (macOS/Web; API: door 8825)
- talk to Claude Code through a page -> [CCMC (MANTRA CHAT, the sister of Claude Code)](../apps/CCMC.md) (macOS/Web; API: door 8825)
- speak the last answer with Beatrice -> [CCMC (MANTRA CHAT, the sister of Claude Code)](../apps/CCMC.md) (macOS/Web; API: door 8825)
- where did I stop -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli) - call: `python3 ~/Developer/claude-code/handover.py brief`
- what is pending on my projects -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli)
- list my projects -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli)
- continue project X -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli)
- close the session and store the state -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli)
- find which repo holds a program -> [Claude Code hub](../apps/claude-code.md) (macOS; API: cli)
- how should I split work across Claude Code subagents -> [Claude Code Mantra OS](../apps/claude-code-mantra-os.md) (Cloud; API: none)
- template for briefing a child agent -> [Claude Code Mantra OS](../apps/claude-code-mantra-os.md) (Cloud; API: none)
- save tokens in Claude Code -> [Claude Code Mantra OS](../apps/claude-code-mantra-os.md) (Cloud; API: none)
- route tasks to Haiku, Sonnet or Opus -> [Claude Code Mantra OS](../apps/claude-code-mantra-os.md) (Cloud; API: none)
- name my Claude Code sessions automatically -> [Claude Code Session Names](../apps/claude-code-session-names.md) (macOS/Termux/Linux/Cloud; API: none) - call: `curl -fsSL https://raw.githubusercontent.com/markoboskoauroville/claude-code-session-names/main/install.sh | bash -s -- mac`
- tell Mac and phone Claude sessions apart -> [Claude Code Session Names](../apps/claude-code-session-names.md) (macOS/Termux/Linux/Cloud; API: none)
- install the session name hook -> [Claude Code Session Names](../apps/claude-code-session-names.md) (macOS/Termux/Linux/Cloud; API: none)
- pause everything Claude is doing -> [Claude Control (Mantra)](../apps/CLAUDE_CONTROL.md) (macOS; API: cli) - call: `claudectl pause # pauses every registered tool with background work or API calls`
- stop all Claude agents now -> [Claude Control (Mantra)](../apps/CLAUDE_CONTROL.md) (macOS; API: cli)
- resume Claude sessions -> [Claude Control (Mantra)](../apps/CLAUDE_CONTROL.md) (macOS; API: cli)
- freeze Claude Code to save money or CPU -> [Claude Control (Mantra)](../apps/CLAUDE_CONTROL.md) (macOS; API: cli)
- keep Claude Code retrying after a dropped connection -> [Claude Persist](../apps/claude-persist.md) (macOS; API: cli) - call: `python3 persist.py status`
- auto resume a session after quota reset -> [Claude Persist](../apps/claude-persist.md) (macOS; API: cli)
- see which sessions are waiting -> [Claude Persist](../apps/claude-persist.md) (macOS; API: cli)
- show usage in the Claude Code status line -> [Claude Remote (Mantra)](../apps/CLAUDE_REMOTE.md) (macOS; API: none)
- install the Claude Code status bar mod -> [Claude Remote (Mantra)](../apps/CLAUDE_REMOTE.md) (macOS; API: none)
- talk to Claude with a microphone and hear the answer -> [Claude Talkie](../apps/Claude_Toki.md) (Linux/Web/Cloud; API: http) - call: `curl -s <site>/claude/health # also POST /claude/api/speech; the chat stream is server-sent events`
- read Claude answers aloud with highlighted words -> [Claude Talkie](../apps/Claude_Toki.md) (Linux/Web/Cloud; API: http)
- ask me before spending money -> [Cost Agent (Mantra)](../apps/COST_AGENT.md) (macOS; API: http 9047) - call: `curl -s -XPOST 127.0.0.1:9047/ask -H 'Content-Type: application/json' -d '{"who":"queen","what":"describe 20 images","provider":"groq","estimate_usd":0.40,"items":20,"job":"img-batch-1"}' # answers {answer: yes|no, reason, id}`
- how much have I spent on APIs today -> [Cost Agent (Mantra)](../apps/COST_AGENT.md) (macOS; API: http 9047)
- block paid calls until I approve -> [Cost Agent (Mantra)](../apps/COST_AGENT.md) (macOS; API: http 9047)
- cost guard for Queen -> [Cost Agent (Mantra)](../apps/COST_AGENT.md) (macOS; API: http 9047)
- read a web page in my Firefox cheaply -> [Firefox Control](../apps/firefox-control.md) (macOS; API: other) - call: `firefoxctl -t yshai links pdf # the links of the tab alias yshai that contain 'pdf'`
- click a button in my logged-in Firefox -> [Firefox Control](../apps/firefox-control.md) (macOS; API: other)
- download a PDF from a page I am logged in to -> [Firefox Control](../apps/firefox-control.md) (macOS; API: other)
- list my open Firefox tabs -> [Firefox Control](../apps/firefox-control.md) (macOS; API: other)
- generate images with Fooocus from a web page -> [Fooocus Streamlit front end](../apps/marko-fooocus.md) (Web/Cloud; API: none)
- run Fooocus on a free Colab GPU -> [Fooocus Streamlit front end](../apps/marko-fooocus.md) (Web/Cloud; API: none)
- read a German website in English -> [German to English (Mantra)](../apps/GERMAN_TO_ENGLISH.md) (Web; API: none)
- translate this German page automatically -> [German to English (Mantra)](../apps/GERMAN_TO_ENGLISH.md) (Web; API: none)
- try every Groq model from the phone -> [Groq Explorer](../apps/GROQ_EXPLORER.md) (Android; API: none)
- test Groq speech to text on Android -> [Groq Explorer](../apps/GROQ_EXPLORER.md) (Android; API: none)
- see the exact Groq API call that was sent -> [Groq Explorer](../apps/GROQ_EXPLORER.md) (Android; API: none)
- is there already a macro for this -> [Macro Skills](../apps/MACRO_SKILLS.md) (macOS; API: cli) - call: `macroskill has --json "snap a window left"`
- snap a window left -> [Macro Skills](../apps/MACRO_SKILLS.md) (macOS; API: cli)
- switch the Gemini account -> [Macro Skills](../apps/MACRO_SKILLS.md) (macOS; API: cli)
- pause all macros -> [Macro Skills](../apps/MACRO_SKILLS.md) (macOS; API: cli)
- pick an NDI monitor source -> [Macro Skills](../apps/MACRO_SKILLS.md) (macOS; API: cli)
- delegate a task to the Copilot agent in VS Code -> [MAI Worker (maiwork)](../apps/MAI_WORKER.md) (macOS; API: cli) - call: `maiwork "<task>" --cwd ~/Developer/SOMETHING --model mai-code-2`
- let MAI Code 2 write a macro -> [MAI Worker (maiwork)](../apps/MAI_WORKER.md) (macOS; API: cli)
- run a worker agent from a script -> [MAI Worker (maiwork)](../apps/MAI_WORKER.md) (macOS; API: cli)
- ask VS Code's agent and get the answer on stdout -> [MAI Worker (maiwork)](../apps/MAI_WORKER.md) (macOS; API: cli)
- drive Claude Code on the Mac from the phone -> [Mantra Bridge](../apps/MANTRA_BRIDGE.md) (macOS/Android; API: http) - call: `python3 -m bridge.server --project ~/Developer/SOME_REPO # run in mac/; then GET /health and the SSE stream`
- stream a Claude Code session over HTTP -> [Mantra Bridge](../apps/MANTRA_BRIDGE.md) (macOS/Android; API: http)
- check a Chrome extension before loading it -> [Mantra Chrome Extensions](../apps/MANTRA_CHROME_EXTENSIONS.md) (macOS/Chrome; API: none)
- build or debug a Chrome extension -> [Mantra Chrome Extensions](../apps/MANTRA_CHROME_EXTENSIONS.md) (macOS/Chrome; API: none)
- act inside a web page through an extension -> [Mantra Chrome Extensions](../apps/MANTRA_CHROME_EXTENSIONS.md) (macOS/Chrome; API: none)
- benchmark an AI on writing extensions -> [Mantra Chrome Extensions](../apps/MANTRA_CHROME_EXTENSIONS.md) (macOS/Chrome; API: none)
- what are the rules for building a new app -> [Mantra Manifest](../apps/MANTRA_MANIFEST.md) (macOS/Android/Linux/Cloud; API: none)
- read the manifest before starting -> [Mantra Manifest](../apps/MANTRA_MANIFEST.md) (macOS/Android/Linux/Cloud; API: none)
- find the shared module for X -> [Mantra Manifest](../apps/MANTRA_MANIFEST.md) (macOS/Android/Linux/Cloud; API: none)
- choose the right Claude model for a prompt -> [Mantra Router](../apps/MANTRA_ROUTER.md) (macOS/Android/Termux/Linux; API: none) - call: `/router auto`
- route prompts between Haiku Sonnet and Opus -> [Mantra Router](../apps/MANTRA_ROUTER.md) (macOS/Android/Termux/Linux; API: none)
- bypass the router -> [Mantra Router](../apps/MANTRA_ROUTER.md) (macOS/Android/Termux/Linux; API: none)
- run an Android app without touching my screen -> [Mantra Sandbox](../apps/MANTRA_SANDBOX.md) (macOS/Android; API: cli) - call: `sandbox run macros/cqmixpad/tab_fader.macro # plays a recorded macro inside the headless Android emulator`
- test a phone app in an emulator by script -> [Mantra Sandbox](../apps/MANTRA_SANDBOX.md) (macOS/Android; API: cli)
- drive CQ MixPad in the background -> [Mantra Sandbox](../apps/MANTRA_SANDBOX.md) (macOS/Android; API: cli)
- automate an Android app in parallel with my own work -> [Mantra Sandbox](../apps/MANTRA_SANDBOX.md) (macOS/Android; API: cli)
- mute the voice for this Claude chat -> [Mantra Voice Switch](../apps/MANTRA_VOICE_SWITCH.md) (macOS/Linux; API: none) - call: `/vox off`
- turn spoken replies back on -> [Mantra Voice Switch](../apps/MANTRA_VOICE_SWITCH.md) (macOS/Linux; API: none)
- ask Queen to do a task on the Mac -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765) - call: `python3 tools/queen_capi.py send CHAT_ID "Run the focused tests" --wait`
- control Ableton Live by text command -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765)
- set the Ableton tempo -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765)
- send a prompt to Claude Code or Gemini from a script -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765)
- Queen CAPI python client -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765)
- auto-update the Queen app -> [Queen (Groq AI Studio), server and tools](../apps/groq_ai_studio.md) (macOS; API: http 8765)
- ask Queen to do a task on the Mac -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765) - call: `python3 tools/queen_capi.py send CHAT_ID "Run the focused tests" --wait`
- control Ableton Live by text command -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765)
- set the Ableton tempo -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765)
- send a prompt to Claude Code or Gemini from a script -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765)
- Queen CAPI python client -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765)
- auto-update the Queen app -> [Queen auto-update (Groq Auto Update)](../apps/groq-auto-update.md) (macOS; API: http 8765)
- chat with Queen on the Mac -> [Queen, Mac app (Groq AI Studio (Mantra))](../apps/GROQ_AI_STUDIO_MAC.md) (macOS; API: door 8765) - call: `curl -s -XPOST 127.0.0.1:8765/api/ax/read -H 'X-Queen-Token: <token from the local token file>' -H 'Content-Type: application/json' -d '{"app":"Firefox","query":"WhatsApp"}'`
- read the text of a window without screenshots -> [Queen, Mac app (Groq AI Studio (Mantra))](../apps/GROQ_AI_STUDIO_MAC.md) (macOS; API: door 8765)
- check my last WhatsApp messages through accessibility -> [Queen, Mac app (Groq AI Studio (Mantra))](../apps/GROQ_AI_STUDIO_MAC.md) (macOS; API: door 8765)
- confirm that a message between Claude sessions was received -> [Session Ack (ccmsg)](../apps/SESSION_ACK.md) (macOS/Linux/Cloud; API: http 8899) - call: `ccmsg send <to> "text" then ccmsg wait <id>`
- track message receipts between sessions -> [Session Ack (ccmsg)](../apps/SESSION_ACK.md) (macOS/Linux/Cloud; API: http 8899)
- mailbox for Claude Code sessions -> [Session Ack (ccmsg)](../apps/SESSION_ACK.md) (macOS/Linux/Cloud; API: http 8899)
- did the other session read my message -> [Session Ack (ccmsg)](../apps/SESSION_ACK.md) (macOS/Linux/Cloud; API: http 8899)
- message another Claude Code session -> [Session Hub](../apps/SESSION_HUB.md) (macOS/Cloud; API: http 8890) - call: `hub send other-session "Please review the diff" # HTTP: curl -s -XPOST 127.0.0.1:8890/send -H 'Content-Type: application/json' -d '{"from":"me","to":"other-session","text":"Please review the diff","id":"m1"}'`
- see which Claude sessions are running -> [Session Hub](../apps/SESSION_HUB.md) (macOS/Cloud; API: http 8890)
- broadcast to all Claude sessions -> [Session Hub](../apps/SESSION_HUB.md) (macOS/Cloud; API: http 8890)
- session to session chat hub -> [Session Hub](../apps/SESSION_HUB.md) (macOS/Cloud; API: http 8890)
- turn the chat server on or off -> [Sister App (Mantra)](../apps/SISTER_APP.md) (macOS; API: accessibility) - call: `star press "sister" "top"`
- open the Mantra chat page -> [Sister App (Mantra)](../apps/SISTER_APP.md) (macOS; API: accessibility)
- create a song on Suno from lyrics -> [Suno Controller (Mantra)](../apps/CHROME_SUNO_CONTROLLER.md) (macOS/Chrome; API: http 8869) - call: `sunoctl record https://suno.com/song/<id> ~/Music/Suno/air.wav`
- record a Suno song to a WAV file -> [Suno Controller (Mantra)](../apps/CHROME_SUNO_CONTROLLER.md) (macOS/Chrome; API: http 8869)
- list my latest Suno songs -> [Suno Controller (Mantra)](../apps/CHROME_SUNO_CONTROLLER.md) (macOS/Chrome; API: http 8869)
- download Suno songs by recording Chrome audio -> [Suno Controller (Mantra)](../apps/CHROME_SUNO_CONTROLLER.md) (macOS/Chrome; API: http 8869)
- edit one file of a huge repo from the phone -> [Surgeon](../apps/surgeon.md) (macOS/Termux/Linux; API: cli) - call: `surgeon push -m "what and why"`
- change a GitHub file without cloning -> [Surgeon](../apps/surgeon.md) (macOS/Termux/Linux; API: cli)
- make a one-commit change to a fork -> [Surgeon](../apps/surgeon.md) (macOS/Termux/Linux; API: cli)

## Retired - do not use

- [Claude Code Monitor (Mantra) (retired)](../apps/CLAUDE_CODE_MONITOR.md) - Archived on GitHub.
