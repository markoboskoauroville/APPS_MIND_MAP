[Back to the index](../CAPABILITIES.md)

# Mac system utilities

## Which one to pick: Keyboard lights and visuals

The only light hardware with an API today is the Logitech G815 keyboard, run by G815 Lights (G815_LIGHTS, HTTP 8877, stream 8878): it is a 115-key low-resolution LED display for any app's pictures or shows. Mantra Room (MANTRA_ROOM) drives it with `lights: true` in `play-loop` and has the MilkDrop visuals. There is no app for Bluetooth LED lights (Neewer) yet; Light Control is planned (see gaps).

| You want | Use | How |
|---|---|---|
| show a colour or picture on the keyboard | [G815 Lights (G815_LIGHTS)](../apps/G815_LIGHTS.md) | `curl -s -XPOST 127.0.0.1:8877/frame -H 'Content-Type: application/json' -d '{"color":"ff0000"}'` |
| play a light show on the keyboard | [G815 Lights (G815_LIGHTS)](../apps/G815_LIGHTS.md) | `curl -s -XPOST 127.0.0.1:8877/show -H 'Content-Type: application/json' -d '{"name":"rainbow","seconds":20}'` |
| play a relaxation loop with keyboard lights and MilkDrop visuals until a time | [Mantra Room (Meditation Room / Chakra and Elements Toning) (MANTRA_ROOM)](../apps/MANTRA_ROOM.md) | `curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'` |
| see which key I pressed as a big glyph | [Keyboard Monitor (Mantra) (keyboard-monitor)](../apps/keyboard-monitor.md) | `KeyboardMonitor --shot /tmp/k.png` |

## Which one to pick: Controlling a Mac app that has no API (Accessibility, macros, Star API)

Macro Recorder (MANTRA_MACRO) holds the Accessibility and screen permissions for all other apps. `macro ax-read "<app>"` lists a running app's buttons and `macro ax-press "<app>" "<label>"` presses one by its title (exact, then prefix, then part), in any running app. Ask MACRO_SKILLS first whether a macro already exists (`macroskill has`), play stored ones with `macro run "<name>"`, and fall back to OCR or picture search (`macro click-text`) when the tree has nothing. Star API (STAR_API, 8863) does the same for the Mantra star apps over HTTP (`star press "timer" "stopwatch"`), and apps may also register real functions with `star fn`. Never use synthetic key presses where the tree works.

| You want | Use | How |
|---|---|---|
| press a button in any Mac app by its label | [Macro Recorder (Mantra) (MANTRA_MACRO)](../apps/MANTRA_MACRO.md) | `macro ax-press "Safari" "Reload"` |
| see if a macro for this already exists | [Macro Skills (MACRO_SKILLS)](../apps/MACRO_SKILLS.md) | `macroskill has --json "snap a window left"` |
| play a recorded macro by name | [Macro Recorder (Mantra) (MANTRA_MACRO)](../apps/MANTRA_MACRO.md) | `macro run "Resolve - Voice Convert Render"` |
| press a control of a Mantra star app, locally or over HTTP | [Star API (Mantra) (STAR_API)](../apps/STAR_API.md) | `curl -s -XPOST 127.0.0.1:8863/apps/timer/press -H "Content-Type: application/json" -d '{"label":"stopwatch"}'` |
| run a small script of clicks and keys in one request | [Macro Recorder (Mantra) (MANTRA_MACRO)](../apps/MANTRA_MACRO.md) | `macro do 'WinActivate "DaVinci Resolve" Send "{Space}"'` |
| read another app's window as text through Queen | [Queen, Mac app (Groq AI Studio (Mantra)) (GROQ_AI_STUDIO_MAC)](../apps/GROQ_AI_STUDIO_MAC.md) |  |
| drive the owner's Firefox by text | [Firefox Control (firefox-control)](../apps/firefox-control.md) | `firefoxctl -t yshai links pdf` |

### [App Store (Mantra)](../apps/APP_STORE.md)

macOS/Web/Hammerspoon; API: http 8839. Main call: `curl -s 127.0.0.1:8839/health # the only routes are /health and /quit; the store itself is used in its window`

Before: App Store (Mantra) must be running.

- install an app without the App Store (App Store)
- find the dmg of an application (App Store)
- search for a Mac or iPhone app by name (App Store)
- put the app store to sleep (App Store)

### [Automated Mouse Actions (Mantra)](../apps/MANTRA_MOUSE.md)

macOS/Web/Hammerspoon; API: http 8831. Main call: `curl -s 127.0.0.1:8831/health # the only documented route; the actions are inside the app`

Before: Automated Mouse Actions (Mantra) must be running.

- move the mouse to the OK button automatically (Automated Mouse Actions)
- make a mouse chord open Mission Control (Automated Mouse Actions)

### [Cascade](../apps/Cascade.md)

macOS; API: none

- tidy all my windows (Cascade)
- cascade windows so I can reach each with the mouse (Cascade)
- restore my window layout (Cascade)

### [Claude Enter (Mantra)](../apps/CLAUDE_ENTER.md)

macOS/Chrome; API: none

- press Enter to send in Claude chat (Claude Enter)
- change Enter behaviour in claude.ai (Claude Enter)

### [Clean Start (Mantra)](../apps/CLEAN_START.md)

macOS; API: none

- boot the Mac without any extra programs (Clean Start)
- what starts by itself on my Mac (Clean Start)
- turn off all startup items (Clean Start)
- restore my startup items (Clean Start)

### [Code Filler (Mantra)](../apps/MANTRA_CODE_FILLER.md)

macOS/Android; API: none

- fill the SMS verification code on the Mac (Code Filler)
- copy the login code from the phone automatically (Code Filler)

### [Dock Switcher (Mantra)](../apps/MACOS_TASK_SWITCHER.md)

macOS/Hammerspoon; API: http 8861. Main call: `curl -s http://127.0.0.1:8861/apps # the open apps; from the phone use the Mac's address on the home network or Tailscale`

Before: Dock Switcher (Mantra) must be running; no token. The door contract of the manifest (/health, /api) is still being added.

- switch apps like Command-Tab but launch closed apps (Dock Switcher)
- show my Dock as a grid (Dock Switcher)
- open a Mac app from the phone (Dock Switcher)
- show the front app's menu on the phone (Dock Switcher)

### [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md)

macOS; API: http 8833. Main call: `python3 dlmon.py copy ~/Movies/big /Volumes/Backup/big/ --name "big copy"`

Before: Download, Copy and Move (Mantra) must be running (port 8833).

- register a download so I can see it (Download, Copy and Move)
- copy a big folder safely (Download, Copy and Move)
- move files with verification (Download, Copy and Move)
- what is downloading on my Mac (Download, Copy and Move)
- download a Hugging Face model with resume (Download, Copy and Move)

### [Drive Full Path (Mantra Productions)](../apps/MANTRA_DRIVE_PATH.md)

Web; API: none

- see the full Google Drive folder path (Drive Full Path)
- where am I in Google Drive (Drive Full Path)
- copy the Drive folder path (Drive Full Path)

### [Find a File (Mantra)](../apps/FIND_FILE.md)

macOS/Web/Hammerspoon; API: door 8845. Main call: `curl -s -X POST http://127.0.0.1:8845/api/find -H 'Content-Type: application/json' -d '{"folder":"~","name":"animatics"}'`

Before: Find a File (Mantra) must be running; ENGINE SPOTLIGHT is its search engine.

- find a file on the Mac by name (Find a File)
- find all files created yesterday (Find a File)
- search inside files with Spotlight (Find a File)
- where is this zip file (Find a File)
- search files inside one folder on the Mac (Find a File)
- make Spotlight index a single folder (Find a File)

### [FKeys](../apps/FKeys.md)

macOS; API: none

- make F keys work as function keys (FKeys)
- toggle media keys and F keys (FKeys)
- one click fn key mode (FKeys)

### [Free Mac](../apps/FREE_MAC.md)

macOS; API: cli. Main call: `sudo -n /usr/local/sbin/apple-door open 15m # opens the Apple door (lets Apple services through) for 15 minutes`

- open the Apple update door for 30 minutes (Free Mac) - call: `stay-off.sh --check`
- make the Mac not start when the lid opens (Free Mac)
- install command line tools without the update server (Free Mac)
- check which Apple servers are blocked (Free Mac)

### [Hammerspoon Lua Recorder](../apps/HAMMERSPOON_LUA_RECORDER.md)

macOS/Hammerspoon; API: none

- record a macro on the Mac (Hammerspoon Lua Recorder)
- keyboard and mouse recorder in Lua (Hammerspoon Lua Recorder)
- teach me Hammerspoon Lua by recording (Hammerspoon Lua Recorder)

### [Homebrew tap for Mantra tools](../apps/homebrew-pasty.md)

macOS; API: none. Main call: `brew install --cask markoboskoauroville/pasty/cascade`

- install Pasty clipboard manager (Homebrew tap for Mantra tools)
- cascade my windows on a Mac (Homebrew tap for Mantra tools)
- switch function keys to media keys (Homebrew tap for Mantra tools)
- brew tap markoboskoauroville/pasty (Homebrew tap for Mantra tools)

### [Host Editor Terminal](../apps/HOST_EDITOR_TERMINAL_MACOS.md)

macOS; API: cli. Main call: `sudo python3 host.py`

Before: Needs sudo to edit /etc/hosts; `HOSTS_FILE=<path>` tests on a copy.

- edit the hosts file (Host Editor Terminal) - call: `HOSTS_FILE=/tmp/hosts python3 host.py`
- see which domains are blocked in hosts (Host Editor Terminal)
- remove a blocked entry from hosts (Host Editor Terminal)

### [Installation Logger (Mantra)](../apps/INSTALLATION_LOGGER.md)

macOS/Web; API: http 8841. Main call: `curl -s 127.0.0.1:8841/health # only /health and /quit exist; the logger is used in its window`

Before: Port 8841 here is the Mac's logger; other apps also use 8841 on other machines.

- see what an installer put on my Mac (Installation Logger)
- uninstall an app completely using a log (Installation Logger)
- record an installation (Installation Logger)

### [Launcher (Mantra)](../apps/STAR_LAUNCHER.md)

macOS; API: accessibility. Main call: `star press "launcher" "record"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- launch an app by typing a few letters (Launcher)
- open the launcher from the G815 Pause key (Launcher)

### [MacBook Pro as external display](../apps/MacBook_Pro_as_external_display.md)

macOS/Web; API: none

- use a second MacBook as a monitor (MacBook Pro as external display)
- send the Mac screen over Thunderbolt to another Mac (MacBook Pro as external display)
- MacBook as external display plan (MacBook Pro as external display)

### [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md)

macOS/Linux; API: http 8829. Main call: `macro run "Resolve - Voice Convert Render"`

Before: Macro Recorder (Mantra) must be running on the Mac; it holds the Accessibility and Screen Recording permissions, so every other app asks it to press and capture. macro run plays a macro stored under ~/.mantra_macro/macros by its exact name.

- automate the Mac mouse and keyboard (Macro Recorder)
- record a macro and replay it (Macro Recorder)
- click a button I can describe or screenshot (Macro Recorder)
- read text off the screen (Macro Recorder)
- press a button in another app through accessibility (Macro Recorder)
- lock keyboard while Claude types (Macro Recorder)
- guard my keyboard while Claude uses the mouse (Macro Recorder)
- stop typing going into the wrong window during automation (Macro Recorder)

### [Mantra Speed Test](../apps/SPEED_TEST.md)

macOS; API: door 8960. Main call: `curl -s -XPOST 127.0.0.1:8960/api/test -H 'Content-Type: application/json' -d '{"drive":"<name from /api/drives>"}' # body field names are not in the docs`

Before: Mac app; port from MANTRA_PORTS id speedtest (8960 and up).

- test the real speed of an SSD (Mantra Speed Test)
- check drive health (Mantra Speed Test) - call: `curl -s 127.0.0.1:8960/api/drives`
- compare my drive with others (Mantra Speed Test)

### [Marco Macro Recorder (Windows)](../apps/MARCO_MACRO_RECORDER.md)

Windows; API: none

- record a macro on Windows (Marco Macro Recorder)
- learn AutoHotkey by watching what it writes (Marco Macro Recorder)
- replay my keyboard and mouse actions on Windows (Marco Macro Recorder)

### [Opening and Closing (Mantra)](../apps/OPENING_AND_CLOSING.md)

macOS; API: none

- open Chrome in a specific profile (Opening and Closing)
- close that annoying window automatically (Opening and Closing)
- start Ableton in arrangement view (Opening and Closing)

### [Pasty](../apps/Pasty.md)

macOS; API: none

- clipboard history on the Mac (Pasty)
- pin things I copy (Pasty)
- paste an earlier copied item (Pasty)
- clipboard manager (Pasty)
- clipboard history manager for Mac (Pasty)

### [Screen Brightness Automatic (Mantra)](../apps/DARKEN_THE_SCREENS.md)

macOS; API: none

- turn off my screens without sleeping the Mac (Screen Brightness Automatic)
- darken both monitors (Screen Brightness Automatic)
- set brightness to zero on all displays (Screen Brightness Automatic)

### [Star (Mantra), Lua (Hammerspoon, legacy)](../apps/MANTRA_STAR.md)

macOS/Hammerspoon; API: cli. Main call: `hs -c 'print(hs.json.encode(STAR.list()))' # Hammerspoon command line; lists the star rows`

Before: Legacy Lua star in Hammerspoon (the Swift menu is STAR_SWIFT); Hammerspoon with its hs command-line tool must be installed and running.

- start or stop one of my Mac apps from the menu bar (Star, Lua)
- see all my apps in one menu (Star, Lua)
- turn all apps off (Star, Lua)
- restart Hammerspoon with the same apps ticked (Star, Lua)

### [Star (Mantra), Swift menu](../apps/STAR_SWIFT.md)

macOS/Linux; API: cli. Main call: `open -a "Star (Mantra)" --args --print-menu # prints the menu rows; the exact binary path is in TAKEOVER.md`

Before: The six-pointed star menu launcher; rows are in ~/.config/star-rows.json.

- launch one of my Mantra apps (Star, Swift menu)
- menu with all my apps (Star, Swift menu)
- order my menu bar icons (Star, Swift menu)
- what apps are on the star menu (Star, Swift menu)

### [Star Monitor (Mantra)](../apps/STAR_MONITOR.md)

macOS; API: door 8851. Main call: `curl -s 127.0.0.1:8851/api/state`

Before: Verify first: the HTTP API on 8851 belongs to the old Flask page and may not exist in the Swift window version (v5). The window buttons answer Accessibility as off, top, close (STAR_API press).

- see which Mantra apps are running (Star Monitor)
- start or stop all my apps (Star Monitor)
- how long has each app run (Star Monitor)
- manage what comes back after restart (Star Monitor)

### [Startup (Mantra)](../apps/Startup-Mantra.md)

macOS; API: none

- choose which dictation app starts at login (Startup)
- switch between Voice to Text and Speechify at boot (Startup)

### [Swift Matrix (Mantra)](../apps/SWIFT_MATRIX.md)

macOS; API: accessibility. Main call: `star press "swift matrix" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- what starts by itself on my Mac (Swift Matrix)
- turn off auto-start of an app (Swift Matrix)
- manage login items and launch agents (Swift Matrix)

### [Timer Stopwatch Clock (Mantra)](../apps/TIMER_STOPWATCH_CLOCK.md)

macOS; API: none

- count time on screen (Timer Stopwatch Clock)
- set a countdown timer (Timer Stopwatch Clock)
- show a big clock (Timer Stopwatch Clock)

### [TinyTask to AutoHotkey](../apps/autohotkey.md)

Windows/Web; API: none

- convert a TinyTask recording to AutoHotkey (TinyTask to AutoHotkey)
- turn a macro recording into an editable script (TinyTask to AutoHotkey)

### [TP - Terminal Properties](../apps/TERMINAL_SHORTCUT_MACOS.md)

macOS; API: http 5077. Main call: `curl 'http://127.0.0.1:5077/api/search?q=clear'`

Before: TP (Terminal Properties) server on 5077.

- make a short alias for a terminal command (TP - Terminal Properties)
- type c to clear the terminal (TP - Terminal Properties)

### [Watch Folder Daemon](../apps/WATCH_FOLDER_DAEMON.md)

macOS; API: cli. Main call: `watch # menu keys: P push, T interval, S stop, F folder, L log, U update, Q quit`

- auto-push files dropped in a folder to GitHub (Watch Folder Daemon)
- upload big renders to a repo automatically (Watch Folder Daemon)


## Retired - do not use

- [Brain Brake Keyboard (Hammerspoon) (retired)](../apps/BRAIN_BRAKE_KEYBOARD.md) - GitHub marks it archived.
- [Find a File Spotlight (Mantra) (retired)](../apps/spotlight.md) - replaced by [Find a File (Mantra)](../apps/FIND_FILE.md)
- [Keyboard and Mouse Router (Mantra) (retired)](../apps/MANTRA_KEYBOARD_MOUSE_ROUTER.md) - replaced by [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md)
- [Pesty fork (archive) (retired)](../apps/pesty-fork-archive.md) - replaced by [Pasty](../apps/Pasty.md)
