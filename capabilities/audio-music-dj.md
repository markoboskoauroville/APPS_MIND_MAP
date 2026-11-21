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

- ask Ableton how to do something by voice -> [Ableton Command Guide](../apps/ABLETON_COMMAND_GUIDE.md) (macOS/Web/Hammerspoon; API: http 8843) - call: `python3 guide.py ask "how do I split a clip" # answer from the key ring (Gemini, then Haiku); a spoken order is performed in Live`
- tell Ableton to start playing -> [Ableton Command Guide](../apps/ABLETON_COMMAND_GUIDE.md) (macOS/Web/Hammerspoon; API: http 8843)
- set the tempo in Live by voice -> [Ableton Command Guide](../apps/ABLETON_COMMAND_GUIDE.md) (macOS/Web/Hammerspoon; API: http 8843)
- mute a track in Live by speaking -> [Ableton Command Guide](../apps/ABLETON_COMMAND_GUIDE.md) (macOS/Web/Hammerspoon; API: http 8843)
- make a Spotify playlist from a chart PDF -> [Charts](../apps/charts.md) (macOS; API: cli) - call: `charts # interactive chart viewer; press o to start`
- import BeatStats chart into Spotify -> [Charts](../apps/charts.md) (macOS; API: cli)
- turn a top-100 PDF into a playlist -> [Charts](../apps/charts.md) (macOS; API: cli)
- DJ from my Android phone -> [DJ Mantra (Android DJ app)](../apps/djmantra_app.md) (Android/Linux; API: none)
- use the Hercules Mix Ultra with the phone -> [DJ Mantra (Android DJ app)](../apps/djmantra_app.md) (Android/Linux; API: none)
- play music from a USB stick on the phone -> [DJ Mantra (Android DJ app)](../apps/djmantra_app.md) (Android/Linux; API: none)
- line up two songs by phrase with beat lights -> [DJ Mantra (Android DJ app)](../apps/djmantra_app.md) (Android/Linux; API: none)
- download the DJ Mantra test APK -> [DJ Mantra (Android DJ app)](../apps/djmantra_app.md) (Android/Linux; API: none)
- watch the DJ transfer to the phone -> [DJ Transfer Monitor (Mantra)](../apps/DJ_TRANSFER_MONITOR.md) (macOS; API: accessibility) - call: `star press "dj transfer" "top"`
- see how long the playlist copy will take -> [DJ Transfer Monitor (Mantra)](../apps/DJ_TRANSFER_MONITOR.md) (macOS; API: accessibility)
- sync my DJ playlists to the phone -> [djay Sync (Mantra), Mac window](../apps/DJING_SYNC.md) (macOS/Android; API: none)
- copy djay playlists to Android -> [djay Sync (Mantra), Mac window](../apps/DJING_SYNC.md) (macOS/Android; API: none)
- pull playlists from the phone into djay -> [djay Sync (Mantra), Mac window](../apps/DJING_SYNC.md) (macOS/Android; API: none)
- sync djay playlists to my phone -> [djay Sync, command line (djay-sync)](../apps/djay-playlists.md) (macOS/Android; API: cli) - call: `djay-sync --status`
- put my DJ playlists on the Pixel for DJ Mantra -> [djay Sync, command line (djay-sync)](../apps/djay-playlists.md) (macOS/Android; API: cli)
- see which playlists differ between djay and the phone -> [djay Sync, command line (djay-sync)](../apps/djay-playlists.md) (macOS/Android; API: cli)
- make a playlist like this song -> [Generated Playlists](../apps/generated_playlists.md) (macOS/Termux/Cloud; API: cli) - call: `python3 tools/tidal_playlist.py create playlists/2026-10-16_reggae-vocal-healing.txt # builds the TIDAL playlist from the track list; add --dry-run to preview`
- put a playlist on TIDAL -> [Generated Playlists](../apps/generated_playlists.md) (macOS/Termux/Cloud; API: cli)
- continue my reference song into a DJ playlist -> [Generated Playlists](../apps/generated_playlists.md) (macOS/Termux/Cloud; API: cli)
- get a TIDAL token on the phone -> [Generated Playlists](../apps/generated_playlists.md) (macOS/Termux/Cloud; API: cli)
- play music on the phone from the terminal -> [MA Player](../apps/ma-player.md) (Android/Termux; API: http 8084) - call: `maplay-cmd next`
- control music playback from a browser on the Wi-Fi -> [MA Player](../apps/ma-player.md) (Android/Termux; API: http 8084)
- download a track from YouTube or TIDAL on the phone -> [MA Player](../apps/ma-player.md) (Android/Termux; API: http 8084)
- Show a single HTML page -> [Music page](../apps/music.md) (Web; API: none)
- build a long Ableton arrangement from MIDI files -> [Pianoverse Demo Songs by Mantra](../apps/PIANOVERSE_DEMO_SONGS.md) (macOS; API: cli) - call: `python3 choose.py && python3 build.py # picks the songs, then builds the demo pages`
- stitch piano demos one after another -> [Pianoverse Demo Songs by Mantra](../apps/PIANOVERSE_DEMO_SONGS.md) (macOS; API: cli)
- turn a chart screenshot into a TIDAL playlist -> [Screenshot to TIDAL (Mantra)](../apps/SCREENSHOT_TO_TIDAL.md) (macOS; API: cli) - call: `"Screenshot to TIDAL (Mantra).app/Contents/MacOS/<binary>" --list-playlists`
- copy my djay playlists to TIDAL -> [Screenshot to TIDAL (Mantra)](../apps/SCREENSHOT_TO_TIDAL.md) (macOS; API: cli)
- find which song this is -> [Shazam Local](../apps/SHAZAM_LOCAL.md) (macOS/Linux; API: cli) - call: `shazam-local --json song clip.wav --dur 45`
- sync a camera audio track to a desk recording -> [Shazam Local](../apps/SHAZAM_LOCAL.md) (macOS/Linux; API: cli)
- locate a clip inside a long recording -> [Shazam Local](../apps/SHAZAM_LOCAL.md) (macOS/Linux; API: cli)
- mix a vocal over a backing track on the phone -> [Song Simple Mixer](../apps/Song_simple_mixer.md) (Android; API: none)
- remix a Suno song parts -> [Song Simple Mixer](../apps/Song_simple_mixer.md) (Android; API: none)
- export a simple two-track mix -> [Song Simple Mixer](../apps/Song_simple_mixer.md) (Android; API: none)
- rebuild the spotting sheet after the picture changes -> [Sound Design](../apps/SOUND_DESIGN.md) (macOS; API: cli) - call: `python3 tools/spotting.py # marks where sound is needed in a film`
- plan sound for a short film -> [Sound Design](../apps/SOUND_DESIGN.md) (macOS; API: cli)
- separate a song into stems -> [Stem Separation (Mantra)](../apps/STEM_SEPARATION.md) (macOS; API: none)
- make stems for a DJ site player -> [Stem Separation (Mantra)](../apps/STEM_SEPARATION.md) (macOS; API: none)
- make a song in a given style -> [Suno Songs prompt database](../apps/SUNO_SONGS.md) (macOS/Chrome; API: http 47615) - call: `python3 scripts/sunoctl.py api '{"url":"/api/clip/ID"}'`
- pick a Suno style by tag -> [Suno Songs prompt database](../apps/SUNO_SONGS.md) (macOS/Chrome; API: http 47615)
- generate a Suno song from the command line -> [Suno Songs prompt database](../apps/SUNO_SONGS.md) (macOS/Chrome; API: http 47615)
- measure the tempo and key of a reference -> [Suno Songs prompt database](../apps/SUNO_SONGS.md) (macOS/Chrome; API: http 47615)
- teach me Ableton step by step -> [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md) (macOS/Hammerspoon; API: cli) - call: `python3 resolve.py marker 250 Red "look here" # DaVinci Resolve: a timeline marker; arguments: position (250 in the README example), colour, note`
- teach me DaVinci Resolve -> [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md) (macOS/Hammerspoon; API: cli)
- set Live tempo from a script -> [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md) (macOS/Hammerspoon; API: cli)
- list Resolve timelines and clips -> [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md) (macOS/Hammerspoon; API: cli)
- put a marker on the Resolve timeline -> [Teacher Lessons and Scripts (Ableton, DaVinci)](../apps/ABLETON_TEACHER.md) (macOS/Hammerspoon; API: cli)
- download a TIDAL playlist as FLAC -> [Tidal DL](../apps/tidal_dl.md) (macOS/Termux; API: cli) - call: `tidaldl https://tidal.com/playlist/<playlist-id> # downloads a playlist; album and track URLs work the same way`
- save my TIDAL album offline on the Mac -> [Tidal DL](../apps/tidal_dl.md) (macOS/Termux; API: cli)
- TIDAL downloader on the phone -> [Tidal DL](../apps/tidal_dl.md) (macOS/Termux; API: cli)
