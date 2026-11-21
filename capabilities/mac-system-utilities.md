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

- install an app without the App Store -> [App Store (Mantra)](../apps/APP_STORE.md) (macOS/Web/Hammerspoon; API: http 8839) - call: `curl -s 127.0.0.1:8839/health # the only routes are /health and /quit; the store itself is used in its window`
- find the dmg of an application -> [App Store (Mantra)](../apps/APP_STORE.md) (macOS/Web/Hammerspoon; API: http 8839)
- search for a Mac or iPhone app by name -> [App Store (Mantra)](../apps/APP_STORE.md) (macOS/Web/Hammerspoon; API: http 8839)
- put the app store to sleep -> [App Store (Mantra)](../apps/APP_STORE.md) (macOS/Web/Hammerspoon; API: http 8839)
- move the mouse to the OK button automatically -> [Automated Mouse Actions (Mantra)](../apps/MANTRA_MOUSE.md) (macOS/Web/Hammerspoon; API: http 8831) - call: `curl -s 127.0.0.1:8831/health # the only documented route; the actions are inside the app`
- make a mouse chord open Mission Control -> [Automated Mouse Actions (Mantra)](../apps/MANTRA_MOUSE.md) (macOS/Web/Hammerspoon; API: http 8831)
- tidy all my windows -> [Cascade](../apps/Cascade.md) (macOS; API: none)
- cascade windows so I can reach each with the mouse -> [Cascade](../apps/Cascade.md) (macOS; API: none)
- restore my window layout -> [Cascade](../apps/Cascade.md) (macOS; API: none)
- press Enter to send in Claude chat -> [Claude Enter (Mantra)](../apps/CLAUDE_ENTER.md) (macOS/Chrome; API: none)
- change Enter behaviour in claude.ai -> [Claude Enter (Mantra)](../apps/CLAUDE_ENTER.md) (macOS/Chrome; API: none)
- boot the Mac without any extra programs -> [Clean Start (Mantra)](../apps/CLEAN_START.md) (macOS; API: none)
- what starts by itself on my Mac -> [Clean Start (Mantra)](../apps/CLEAN_START.md) (macOS; API: none)
- turn off all startup items -> [Clean Start (Mantra)](../apps/CLEAN_START.md) (macOS; API: none)
- restore my startup items -> [Clean Start (Mantra)](../apps/CLEAN_START.md) (macOS; API: none)
- fill the SMS verification code on the Mac -> [Code Filler (Mantra)](../apps/MANTRA_CODE_FILLER.md) (macOS/Android; API: none)
- copy the login code from the phone automatically -> [Code Filler (Mantra)](../apps/MANTRA_CODE_FILLER.md) (macOS/Android; API: none)
- switch apps like Command-Tab but launch closed apps -> [Dock Switcher (Mantra)](../apps/MACOS_TASK_SWITCHER.md) (macOS/Hammerspoon; API: http 8861) - call: `curl -s http://127.0.0.1:8861/apps # the open apps; from the phone use the Mac's address on the home network or Tailscale`
- show my Dock as a grid -> [Dock Switcher (Mantra)](../apps/MACOS_TASK_SWITCHER.md) (macOS/Hammerspoon; API: http 8861)
- open a Mac app from the phone -> [Dock Switcher (Mantra)](../apps/MACOS_TASK_SWITCHER.md) (macOS/Hammerspoon; API: http 8861)
- show the front app's menu on the phone -> [Dock Switcher (Mantra)](../apps/MACOS_TASK_SWITCHER.md) (macOS/Hammerspoon; API: http 8861)
- register a download so I can see it -> [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md) (macOS; API: http 8833) - call: `python3 dlmon.py copy ~/Movies/big /Volumes/Backup/big/ --name "big copy"`
- copy a big folder safely -> [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md) (macOS; API: http 8833)
- move files with verification -> [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md) (macOS; API: http 8833)
- what is downloading on my Mac -> [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md) (macOS; API: http 8833)
- download a Hugging Face model with resume -> [Download, Copy and Move (Mantra) (was Download Monitor)](../apps/DOWNLOAD_MONITOR.md) (macOS; API: http 8833)
- see the full Google Drive folder path -> [Drive Full Path (Mantra Productions)](../apps/MANTRA_DRIVE_PATH.md) (Web; API: none)
- where am I in Google Drive -> [Drive Full Path (Mantra Productions)](../apps/MANTRA_DRIVE_PATH.md) (Web; API: none)
- copy the Drive folder path -> [Drive Full Path (Mantra Productions)](../apps/MANTRA_DRIVE_PATH.md) (Web; API: none)
- find a file on the Mac by name -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845) - call: `curl -s -X POST http://127.0.0.1:8845/api/find -H 'Content-Type: application/json' -d '{"folder":"~","name":"animatics"}'`
- find all files created yesterday -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845)
- search inside files with Spotlight -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845)
- where is this zip file -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845)
- search files inside one folder on the Mac -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845)
- make Spotlight index a single folder -> [Find a File (Mantra)](../apps/FIND_FILE.md) (macOS/Web/Hammerspoon; API: door 8845)
- make F keys work as function keys -> [FKeys](../apps/FKeys.md) (macOS; API: none)
- toggle media keys and F keys -> [FKeys](../apps/FKeys.md) (macOS; API: none)
- one click fn key mode -> [FKeys](../apps/FKeys.md) (macOS; API: none)
- open the Apple update door for 30 minutes -> [Free Mac](../apps/FREE_MAC.md) (macOS; API: cli) - call: `sudo -n /usr/local/sbin/apple-door open 15m # opens the Apple door (lets Apple services through) for 15 minutes`
- make the Mac not start when the lid opens -> [Free Mac](../apps/FREE_MAC.md) (macOS; API: cli)
- install command line tools without the update server -> [Free Mac](../apps/FREE_MAC.md) (macOS; API: cli)
- check which Apple servers are blocked -> [Free Mac](../apps/FREE_MAC.md) (macOS; API: cli)
- record a macro on the Mac -> [Hammerspoon Lua Recorder](../apps/HAMMERSPOON_LUA_RECORDER.md) (macOS/Hammerspoon; API: none)
- keyboard and mouse recorder in Lua -> [Hammerspoon Lua Recorder](../apps/HAMMERSPOON_LUA_RECORDER.md) (macOS/Hammerspoon; API: none)
- teach me Hammerspoon Lua by recording -> [Hammerspoon Lua Recorder](../apps/HAMMERSPOON_LUA_RECORDER.md) (macOS/Hammerspoon; API: none)
- install Pasty clipboard manager -> [Homebrew tap for Mantra tools](../apps/homebrew-pasty.md) (macOS; API: none) - call: `brew install --cask markoboskoauroville/pasty/cascade`
- cascade my windows on a Mac -> [Homebrew tap for Mantra tools](../apps/homebrew-pasty.md) (macOS; API: none)
- switch function keys to media keys -> [Homebrew tap for Mantra tools](../apps/homebrew-pasty.md) (macOS; API: none)
- brew tap markoboskoauroville/pasty -> [Homebrew tap for Mantra tools](../apps/homebrew-pasty.md) (macOS; API: none)
- edit the hosts file -> [Host Editor Terminal](../apps/HOST_EDITOR_TERMINAL_MACOS.md) (macOS; API: cli) - call: `sudo python3 host.py`
- see which domains are blocked in hosts -> [Host Editor Terminal](../apps/HOST_EDITOR_TERMINAL_MACOS.md) (macOS; API: cli)
- remove a blocked entry from hosts -> [Host Editor Terminal](../apps/HOST_EDITOR_TERMINAL_MACOS.md) (macOS; API: cli)
- see what an installer put on my Mac -> [Installation Logger (Mantra)](../apps/INSTALLATION_LOGGER.md) (macOS/Web; API: http 8841) - call: `curl -s 127.0.0.1:8841/health # only /health and /quit exist; the logger is used in its window`
- uninstall an app completely using a log -> [Installation Logger (Mantra)](../apps/INSTALLATION_LOGGER.md) (macOS/Web; API: http 8841)
- record an installation -> [Installation Logger (Mantra)](../apps/INSTALLATION_LOGGER.md) (macOS/Web; API: http 8841)
- launch an app by typing a few letters -> [Launcher (Mantra)](../apps/STAR_LAUNCHER.md) (macOS; API: accessibility) - call: `star press "launcher" "record"`
- open the launcher from the G815 Pause key -> [Launcher (Mantra)](../apps/STAR_LAUNCHER.md) (macOS; API: accessibility)
- use a second MacBook as a monitor -> [MacBook Pro as external display](../apps/MacBook_Pro_as_external_display.md) (macOS/Web; API: none)
- send the Mac screen over Thunderbolt to another Mac -> [MacBook Pro as external display](../apps/MacBook_Pro_as_external_display.md) (macOS/Web; API: none)
- MacBook as external display plan -> [MacBook Pro as external display](../apps/MacBook_Pro_as_external_display.md) (macOS/Web; API: none)
- automate the Mac mouse and keyboard -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829) - call: `macro run "Resolve - Voice Convert Render"`
- record a macro and replay it -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- click a button I can describe or screenshot -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- read text off the screen -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- press a button in another app through accessibility -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- lock keyboard while Claude types -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- guard my keyboard while Claude uses the mouse -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- stop typing going into the wrong window during automation -> [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md) (macOS/Linux; API: http 8829)
- test the real speed of an SSD -> [Mantra Speed Test](../apps/SPEED_TEST.md) (macOS; API: door 8960) - call: `curl -s -XPOST 127.0.0.1:8960/api/test -H 'Content-Type: application/json' -d '{"drive":"<name from /api/drives>"}' # body field names are not in the docs`
- check drive health -> [Mantra Speed Test](../apps/SPEED_TEST.md) (macOS; API: door 8960)
- compare my drive with others -> [Mantra Speed Test](../apps/SPEED_TEST.md) (macOS; API: door 8960)
- record a macro on Windows -> [Marco Macro Recorder (Windows)](../apps/MARCO_MACRO_RECORDER.md) (Windows; API: none)
- learn AutoHotkey by watching what it writes -> [Marco Macro Recorder (Windows)](../apps/MARCO_MACRO_RECORDER.md) (Windows; API: none)
- replay my keyboard and mouse actions on Windows -> [Marco Macro Recorder (Windows)](../apps/MARCO_MACRO_RECORDER.md) (Windows; API: none)
- open Chrome in a specific profile -> [Opening and Closing (Mantra)](../apps/OPENING_AND_CLOSING.md) (macOS; API: none)
- close that annoying window automatically -> [Opening and Closing (Mantra)](../apps/OPENING_AND_CLOSING.md) (macOS; API: none)
- start Ableton in arrangement view -> [Opening and Closing (Mantra)](../apps/OPENING_AND_CLOSING.md) (macOS; API: none)
- clipboard history on the Mac -> [Pasty](../apps/Pasty.md) (macOS; API: none)
- pin things I copy -> [Pasty](../apps/Pasty.md) (macOS; API: none)
- paste an earlier copied item -> [Pasty](../apps/Pasty.md) (macOS; API: none)
- clipboard manager -> [Pasty](../apps/Pasty.md) (macOS; API: none)
- clipboard history manager for Mac -> [Pasty](../apps/Pasty.md) (macOS; API: none)
- turn off my screens without sleeping the Mac -> [Screen Brightness Automatic (Mantra)](../apps/DARKEN_THE_SCREENS.md) (macOS; API: none)
- darken both monitors -> [Screen Brightness Automatic (Mantra)](../apps/DARKEN_THE_SCREENS.md) (macOS; API: none)
- set brightness to zero on all displays -> [Screen Brightness Automatic (Mantra)](../apps/DARKEN_THE_SCREENS.md) (macOS; API: none)
- start or stop one of my Mac apps from the menu bar -> [Star (Mantra), Lua (Hammerspoon, legacy)](../apps/MANTRA_STAR.md) (macOS/Hammerspoon; API: cli) - call: `hs -c 'print(hs.json.encode(STAR.list()))' # Hammerspoon command line; lists the star rows`
- see all my apps in one menu -> [Star (Mantra), Lua (Hammerspoon, legacy)](../apps/MANTRA_STAR.md) (macOS/Hammerspoon; API: cli)
- turn all apps off -> [Star (Mantra), Lua (Hammerspoon, legacy)](../apps/MANTRA_STAR.md) (macOS/Hammerspoon; API: cli)
- restart Hammerspoon with the same apps ticked -> [Star (Mantra), Lua (Hammerspoon, legacy)](../apps/MANTRA_STAR.md) (macOS/Hammerspoon; API: cli)
- launch one of my Mantra apps -> [Star (Mantra), Swift menu](../apps/STAR_SWIFT.md) (macOS/Linux; API: cli) - call: `open -a "Star (Mantra)" --args --print-menu # prints the menu rows; the exact binary path is in TAKEOVER.md`
- menu with all my apps -> [Star (Mantra), Swift menu](../apps/STAR_SWIFT.md) (macOS/Linux; API: cli)
- order my menu bar icons -> [Star (Mantra), Swift menu](../apps/STAR_SWIFT.md) (macOS/Linux; API: cli)
- what apps are on the star menu -> [Star (Mantra), Swift menu](../apps/STAR_SWIFT.md) (macOS/Linux; API: cli)
- see which Mantra apps are running -> [Star Monitor (Mantra)](../apps/STAR_MONITOR.md) (macOS; API: door 8851) - call: `curl -s 127.0.0.1:8851/api/state`
- start or stop all my apps -> [Star Monitor (Mantra)](../apps/STAR_MONITOR.md) (macOS; API: door 8851)
- how long has each app run -> [Star Monitor (Mantra)](../apps/STAR_MONITOR.md) (macOS; API: door 8851)
- manage what comes back after restart -> [Star Monitor (Mantra)](../apps/STAR_MONITOR.md) (macOS; API: door 8851)
- choose which dictation app starts at login -> [Startup (Mantra)](../apps/Startup-Mantra.md) (macOS; API: none)
- switch between Voice to Text and Speechify at boot -> [Startup (Mantra)](../apps/Startup-Mantra.md) (macOS; API: none)
- what starts by itself on my Mac -> [Swift Matrix (Mantra)](../apps/SWIFT_MATRIX.md) (macOS; API: accessibility) - call: `star press "swift matrix" "top"`
- turn off auto-start of an app -> [Swift Matrix (Mantra)](../apps/SWIFT_MATRIX.md) (macOS; API: accessibility)
- manage login items and launch agents -> [Swift Matrix (Mantra)](../apps/SWIFT_MATRIX.md) (macOS; API: accessibility)
- count time on screen -> [Timer Stopwatch Clock (Mantra)](../apps/TIMER_STOPWATCH_CLOCK.md) (macOS; API: none)
- set a countdown timer -> [Timer Stopwatch Clock (Mantra)](../apps/TIMER_STOPWATCH_CLOCK.md) (macOS; API: none)
- show a big clock -> [Timer Stopwatch Clock (Mantra)](../apps/TIMER_STOPWATCH_CLOCK.md) (macOS; API: none)
- convert a TinyTask recording to AutoHotkey -> [TinyTask to AutoHotkey](../apps/autohotkey.md) (Windows/Web; API: none)
- turn a macro recording into an editable script -> [TinyTask to AutoHotkey](../apps/autohotkey.md) (Windows/Web; API: none)
- make a short alias for a terminal command -> [TP - Terminal Properties](../apps/TERMINAL_SHORTCUT_MACOS.md) (macOS; API: http 5077) - call: `curl 'http://127.0.0.1:5077/api/search?q=clear'`
- type c to clear the terminal -> [TP - Terminal Properties](../apps/TERMINAL_SHORTCUT_MACOS.md) (macOS; API: http 5077)
- auto-push files dropped in a folder to GitHub -> [Watch Folder Daemon](../apps/WATCH_FOLDER_DAEMON.md) (macOS; API: cli) - call: `watch # menu keys: P push, T interval, S stop, F folder, L log, U update, Q quit`
- upload big renders to a repo automatically -> [Watch Folder Daemon](../apps/WATCH_FOLDER_DAEMON.md) (macOS; API: cli)

## Retired - do not use

- [Brain Brake Keyboard (Hammerspoon) (retired)](../apps/BRAIN_BRAKE_KEYBOARD.md) - GitHub marks it archived.
- [Find a File Spotlight (Mantra), retired (retired)](../apps/spotlight.md) - replaced by [Find a File (Mantra)](../apps/FIND_FILE.md)
- [Keyboard and Mouse Router (Mantra), retired (retired)](../apps/MANTRA_KEYBOARD_MOUSE_ROUTER.md) - replaced by [Macro Recorder (Mantra)](../apps/MANTRA_MACRO.md)
- [Pesty fork (archive) (retired)](../apps/pesty-fork-archive.md) - replaced by [Pasty](../apps/Pasty.md)
