[Back to the index](../CAPABILITIES.md)

# Learning and academy

### [Ableton Teacher and DaVinci Teacher apps (Mantra)](../apps/MANTRA_TEACHERS.md)

macOS; API: http 8970. Main call: `curl -s 127.0.0.1:8970/state # Ableton Teacher; DaVinci Teacher is 8971, universal 8972`

Before: The Teacher app (Ableton Teacher (Mantra) or DaVinci Teacher (Mantra)) must be running; ports are claimed in ~/.config/mantra-ports.json.

- teach me Ableton step by step (Ableton Teacher and DaVinci Teacher apps)
- DaVinci Resolve lesson helper (Ableton Teacher and DaVinci Teacher apps)
- guided lesson window on the Mac (Ableton Teacher and DaVinci Teacher apps)

### [DaVinci Grading Tutorial (Mantra)](../apps/RESOLVE_GRADING_TUTORIAL.md)

macOS; API: accessibility. Main call: `star press "grading tutorial" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- learn colour grading workflow in Resolve (DaVinci Grading Tutorial)
- listen to the grading tutorial (DaVinci Grading Tutorial)

### [MPA Academy, Android app](../apps/MPA_ACADEMY_ANDROID.md)

Android; API: none. Main call: `adb shell am start -n com.mantra.mpaacademy/.MainActivity --ez pin true`

- practise frame drum phrasing on the phone (MPA Academy, Android app)
- play the academy exercises on Android (MPA Academy, Android app)
- drum exercise player with a moving light (MPA Academy, Android app)
- add an exercise to the academy app (MPA Academy, Android app)

### [MPA Academy, website and hub](../apps/mpa-academy.md)

Web/Cloud; API: http. Main call: `no verified call: the hub Worker routes /api/backup, /api/ex and /api/notes are named in TAKEOVER.md, but their arguments and login are not in the harvested docs`

Before: Private repo with student data; the API list is partial because website/ was not harvested.

- update the percussion academy website (MPA Academy, website and hub)
- add a rhythm to the Exercise Lab (MPA Academy, website and hub)
- write a text lesson from a recorded class (MPA Academy, website and hub)
- restore the academy database (MPA Academy, website and hub)
- make a printable rhythm sheet (MPA Academy, website and hub)

### [MPA Lessons Analyzer](../apps/MPA_LESSONS_ANALYZER.md)

macOS; API: http 8965. Main call: `curl -s -XPOST 127.0.0.1:8965/open -H 'Content-Type: application/json' -d '{"path":"~/Movies/lesson1.mov"}'`

Before: MPA Lessons Analyzer (Mantra) must be running. Port 8965 may shift to the next free port; the actual port is in ~/.mantra/ports/mpa-lessons-analyzer. 8965 is ALSO the number of MANTRA_ROOM (Meditation Room): check which app answers (GET /status). LAN listener for Second Take on 8966.

- analyze a drum lesson video (MPA Lessons Analyzer)
- transcribe a lesson and mark sections (MPA Lessons Analyzer)
- split voice from drums in a recording (MPA Lessons Analyzer) - call: `curl -s -XPOST 127.0.0.1:8965/shoot/start -H 'Content-Type: application/json' -d '{"quiet":true}'`
- shoot a lesson with the phone as remote (MPA Lessons Analyzer)
- trim and export lesson takes (MPA Lessons Analyzer)

### [Percussion School (Mantra)](../apps/YSHAI_PERCUSSION_SCHOOL.md)

macOS; API: accessibility. Main call: `star press "percussion school" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- download missing percussion lessons (Percussion School)
- check which lessons I do not have yet (Percussion School)

