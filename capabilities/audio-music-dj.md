[Back to the index](../CAPABILITIES.md)

# Audio, music and DJ

## Which one to pick: Ableton Live

Ableton is driven by AbletonOSC (UDP 11000 in, 11001 answers; 11001 has one owner and others send to the router on 11002). ABLETON_LIVE_ACTIONS is the Mac app with the A1 assistant, MIDI to Mackie and CQ channel macros; `python3 live.py set /live/song/set/tempo 96` in ABLETON_TEACHER is the quickest scripted call; Queen exposes `POST /api/ableton/action` and mantra_pages `POST /api/live`. ABLETON_COMMAND_GUIDE answers shortcut questions by voice; the Teacher apps (MANTRA_TEACHERS, 8970) teach step by step.

| You want | Use | How |
|---|---|---|
| set tempo or read the song from a script | [Teacher Lessons and Scripts (Ableton, DaVinci) (ABLETON_TEACHER)](../apps/ABLETON_TEACHER.md) | `python3 live.py set /live/song/set/tempo 96` |
| tell Queen to control Ableton | [Queen (Groq AI Studio), server and tools (groq_ai_studio)](../apps/groq_ai_studio.md) | `curl -s -XPOST 127.0.0.1:8765/api/ableton/action -H 'Content-Type: application/json' -d '{"action":"set_tempo","arguments":{"bpm":120}}'` |
| ask a shortcut question, or give a spoken order | [Ableton Command Guide (ABLETON_COMMAND_GUIDE)](../apps/ABLETON_COMMAND_GUIDE.md) | `python3 guide.py ask "how do I split a clip"` |
| use a MIDI knob as a Mackie control in Live | [MIDI Tools (Mantra) (MANTRA_MIDI_TOOLS)](../apps/MANTRA_MIDI_TOOLS.md) |  |
| learn Ableton with a spoken teacher | [Ableton Teacher and DaVinci Teacher apps (Mantra) (MANTRA_TEACHERS)](../apps/MANTRA_TEACHERS.md) | `curl -s 127.0.0.1:8970/state` |
| split a song into stems with Live | [Stem Separation (Mantra) (STEM_SEPARATION)](../apps/STEM_SEPARATION.md) |  |

### [Ableton Command Guide](../apps/ABLETON_COMMAND_GUIDE.md)

macOS/Web/Hammerspoon; API: http 8843. Main call: `python3 guide.py ask "how do I split a clip" # answer from the key ring (Gemini, then Haiku); a spoken order is performed in Live`

Before: Run in the repo folder; the page server guided.py serves the card page on 127.0.0.1:8843 and Live needs AbletonOSC for spoken orders (UDP 11001 is held by one process only).

- ask Ableton how to do something by voice (Ableton Command Guide)
- tell Ableton to start playing (Ableton Command Guide)
- set the tempo in Live by voice (Ableton Command Guide)
- mute a track in Live by speaking (Ableton Command Guide)

### [Charts](../apps/charts.md)

macOS; API: cli. Main call: `charts # interactive chart viewer; press o to start`

Before: Installed command; no arguments needed.

- make a Spotify playlist from a chart PDF (Charts)
- import BeatStats chart into Spotify (Charts)
- turn a top-100 PDF into a playlist (Charts)

### [DJ Mantra (Android DJ app)](../apps/djmantra_app.md)

Android/Linux; API: none

- DJ from my Android phone (DJ Mantra)
- use the Hercules Mix Ultra with the phone (DJ Mantra)
- play music from a USB stick on the phone (DJ Mantra)
- line up two songs by phrase with beat lights (DJ Mantra)
- download the DJ Mantra test APK (DJ Mantra)

### [DJ Transfer Monitor (Mantra)](../apps/DJ_TRANSFER_MONITOR.md)

macOS; API: accessibility. Main call: `star press "dj transfer" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- watch the DJ transfer to the phone (DJ Transfer Monitor)
- see how long the playlist copy will take (DJ Transfer Monitor)

### [djay Sync (Mantra), Mac window](../apps/DJING_SYNC.md)

macOS/Android; API: none

- sync my DJ playlists to the phone (djay Sync, Mac window)
- copy djay playlists to Android (djay Sync, Mac window)
- pull playlists from the phone into djay (djay Sync, Mac window)

### [djay Sync, command line (djay-sync)](../apps/djay-playlists.md)

macOS/Android; API: cli. Main call: `djay-sync --status`

Before: djay Pro and the phone must be reachable for sync (see --serial).

- sync djay playlists to my phone (djay Sync, command line) - call: `djay-sync --sync`
- put my DJ playlists on the Pixel for DJ Mantra (djay Sync, command line)
- see which playlists differ between djay and the phone (djay Sync, command line)

### [Generated Playlists](../apps/generated_playlists.md)

macOS/Termux/Cloud; API: cli. Main call: `python3 tools/tidal_playlist.py create playlists/2026-10-16_reggae-vocal-healing.txt # builds the TIDAL playlist from the track list; add --dry-run to preview`

Before: Log in to TIDAL first: tools/tidal_playlist.py login-url, open the link, then login-finish. The local port 8765 in the old record is the login callback, not an API.

- make a playlist like this song (Generated Playlists)
- put a playlist on TIDAL (Generated Playlists)
- continue my reference song into a DJ playlist (Generated Playlists)
- get a TIDAL token on the phone (Generated Playlists)

### [MA Player](../apps/ma-player.md)

Android/Termux; API: http 8084. Main call: `maplay-cmd next`

Before: Starts with maplay (page player), maplayerweb or matidal on 8084; maplay-cmd sends it commands.

- play music on the phone from the terminal (MA Player)
- control music playback from a browser on the Wi-Fi (MA Player)
- download a track from YouTube or TIDAL on the phone (MA Player)

### [Music page](../apps/music.md)

Web; API: none

- Show a single HTML page (Music page)

### [Pianoverse Demo Songs by Mantra](../apps/PIANOVERSE_DEMO_SONGS.md)

macOS; API: cli. Main call: `python3 choose.py && python3 build.py # picks the songs, then builds the demo pages`

Before: Run in the repo folder.

- build a long Ableton arrangement from MIDI files (Pianoverse Demo Songs by Mantra)
- stitch piano demos one after another (Pianoverse Demo Songs by Mantra)

### [Screenshot to TIDAL (Mantra)](../apps/SCREENSHOT_TO_TIDAL.md)

macOS; API: cli. Main call: `"Screenshot to TIDAL (Mantra).app/Contents/MacOS/<binary>" --list-playlists`

Before: Needs a TIDAL developer app key file chosen by the user; log in once with --tidal-login. Binary name inside the bundle is not in the harvested docs.

- turn a chart screenshot into a TIDAL playlist (Screenshot to TIDAL) - call: `... --sync-playlists`
- copy my djay playlists to TIDAL (Screenshot to TIDAL)

### [Shazam Local](../apps/SHAZAM_LOCAL.md)

macOS/Linux; API: cli. Main call: `shazam-local --json song clip.wav --dur 45`

Before: Run in the repo environment; 'add' builds the local fingerprint library from audio first.

- find which song this is (Shazam Local) - call: `shazam-local add song.wav`
- sync a camera audio track to a desk recording (Shazam Local)
- locate a clip inside a long recording (Shazam Local)

### [Song Simple Mixer](../apps/Song_simple_mixer.md)

Android; API: none

- mix a vocal over a backing track on the phone (Song Simple Mixer)
- remix a Suno song parts (Song Simple Mixer)
- export a simple two-track mix (Song Simple Mixer)

### [Sound Design](../apps/SOUND_DESIGN.md)

macOS; API: cli. Main call: `python3 tools/spotting.py # marks where sound is needed in a film`

- rebuild the spotting sheet after the picture changes (Sound Design)
- plan sound for a short film (Sound Design)

### [Stem Separation (Mantra)](../apps/STEM_SEPARATION.md)

macOS; API: none

- separate a song into stems (Stem Separation)
- make stems for a DJ site player (Stem Separation)

### [Suno Songs prompt database](../apps/SUNO_SONGS.md)

macOS/Chrome; API: http 47615. Main call: `python3 scripts/sunoctl.py api '{"url":"/api/clip/ID"}'`

Before: sunoctl serve runs the helper door on 47615 (up to 47630).

- make a song in a given style (Suno Songs prompt database)
- pick a Suno style by tag (Suno Songs prompt database)
- generate a Suno song from the command line (Suno Songs prompt database)
- measure the tempo and key of a reference (Suno Songs prompt database)

### [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md)

macOS/Hammerspoon; API: cli. Main call: `python3 resolve.py marker 250 Red "look here" # DaVinci Resolve: a timeline marker; arguments: position (250 in the README example), colour, note`

Before: Run in a checkout of this repo. For Resolve: Resolve must be open with scripting set to Local (resolve.py sets the environment itself). For Ableton: AbletonOSC installed as the Control Surface in Live; python3 live.py ping must answer.

- teach me Ableton step by step (Teacher Lessons and Scripts) - call: `python3 live.py set /live/song/set/tempo 96`
- teach me DaVinci Resolve (Teacher Lessons and Scripts) - call: `python3 resolve.py tc 01:00:10:00 ; python3 resolve.py page color`
- set Live tempo from a script (Teacher Lessons and Scripts)
- list Resolve timelines and clips (Teacher Lessons and Scripts)
- put a marker on the Resolve timeline (Teacher Lessons and Scripts)

### [Tidal DL](../apps/tidal_dl.md)

macOS/Termux; API: cli. Main call: `tidaldl https://tidal.com/playlist/<playlist-id> # downloads a playlist; album and track URLs work the same way`

Before: Log in to TIDAL once (the menu: run tidaldl with no argument). Real login and download still had to be tested by the owner at v22.

- download a TIDAL playlist as FLAC (Tidal DL)
- save my TIDAL album offline on the Mac (Tidal DL) - call: `tidaldl https://tidal.com/album/12345`
- TIDAL downloader on the phone (Tidal DL)

