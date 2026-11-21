[Back to the index](../CAPABILITIES.md)

# Film and editing (DaVinci Resolve)

## Which one to pick: DaVinci Resolve

Anything that must run Resolve's scripting API goes through the router in DaVinci Resolve Actions (DAVINCI_RESOLVE_ACTIONS, port 8940, `POST /run`): never open a second connection. The command-line `resolve.py` in ABLETON_TEACHER (`python3 resolve.py marker 250 Red "look here"`) is a second route for markers, timelines and render. RESOLVE_PAGES, UHD_HD_DISPLAY and IMPORT_BUTTON are small Mac helpers; DaVinci Teacher (MANTRA_TEACHERS, 8971) teaches Resolve step by step. DAVINCI_RESOLVE_ASSISTANT is superseded by DAVINCI_RESOLVE_ACTIONS.

| You want | Use | How |
|---|---|---|
| run Python in Resolve safely | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](../apps/DAVINCI_RESOLVE_ACTIONS.md) | `curl -s -X POST 'http://127.0.0.1:8940/run' -H 'Content-Type: application/json' -d '{"who":"me","code":"result = project.GetName()","timeout":30}'` |
| switch Resolve to a page | [DaVinci Resolve Actions (Mantra) (DAVINCI_RESOLVE_ACTIONS)](../apps/DAVINCI_RESOLVE_ACTIONS.md) | `curl -s -XPOST '127.0.0.1:8940/open?page=edit'` |
| add a timeline marker | [Teacher Lessons and Scripts (Ableton, DaVinci) (ABLETON_TEACHER)](../apps/ABLETON_TEACHER.md) | `python3 resolve.py marker 250 Red "look here"` |
| learn Resolve with a spoken step-by-step teacher | [Ableton Teacher and DaVinci Teacher apps (Mantra) (MANTRA_TEACHERS)](../apps/MANTRA_TEACHERS.md) |  |
| cycle the Resolve pages with a hotkey | [Resolve Pages (Mantra) (RESOLVE_PAGES)](../apps/RESOLVE_PAGES.md) |  |
| restore clips with a free GPU upscaler | [Colab Video Upscaler (colab-video-upscaler)](../apps/colab-video-upscaler.md) | `python3 colab_restore.py status` |
| repack browser-recorded lessons into Resolve-ready MOV | [MKV Converter (MPA) (MKV_CONVERTER)](../apps/MKV_CONVERTER.md) |  |

### [Animator Collaboration](../apps/ANIMATOR_COLLABORATION.md)

Web; API: none

- where are the animator's frames for scene 3 (Animator Collaboration)
- hand over frames to the animator (Animator Collaboration)
- what changed in the Brain Brake frames (Animator Collaboration)

### [Avid Assistant](../apps/AVID_ASSISTANT.md)

Windows; API: none

- automate Avid Media Composer clicks (Avid Assistant)
- stop a running macro (Avid Assistant)
- set up the edit suite monitors on Windows (Avid Assistant)

### [Blender Control](../apps/blender-control.md)

macOS; API: cli. Main call: `python3 .agents/skills/blender-control/scripts/blender_cli.py ping # Blender must run with its control add-on on port 9876`

Before: Blender running with the control add-on (TCP 9876), or add --headless for batch runs.

- control Blender from the terminal (Blender Control)
- render a Blender scene to PNG or MP4 (Blender Control) - call: `python3 .agents/skills/blender-control/scripts/blender_cli.py render`
- build a 3D scene with a Python script in the open Blender (Blender Control) - call: `python3 .agents/skills/blender-control/scripts/blender_cli.py exec "print(bpy.context.scene.name)"`
- change colours in a video frame by frame with Blender (Blender Control)
- start the Blender bridge (Blender Control)

### [Brain Brake 3D](../apps/BRAIN_BRAKE_3D.md)

macOS; API: cli. Main call: `/Applications/Blender.app/Contents/MacOS/Blender --background --python scripts/render_key.py`

Before: Blender installed in /Applications; run from the repo folder.

- render the Brain Brake key (Brain Brake 3D) - call: `Blender --background --python scripts/render_key_v2.py ; ... render_key_v3.py ; ... render_fall.py`
- 3D key for the film (Brain Brake 3D)
- run Blender headless to render stills (Brain Brake 3D)

### [Brain Brake audio](../apps/BRAINBREAK_AUDIO.md)

Web; API: none

- get the Brain Brake theme song (Brain Brake audio)
- where is the radio drama audio (Brain Brake audio)
- the film's voice takes (Brain Brake audio)

### [Brain Brake frames](../apps/BRAIN_BRAKE_FRAMES.md)

Web; API: none

- see all the film's frames at once (Brain Brake frames)
- Brain Brake contact sheet (Brain Brake frames)

### [Brain Brake originals](../apps/BRAIN_BRAKE_ORIGINALS.md)

Web; API: none

- full resolution frame of scene 1 (Brain Brake originals)
- where are the original film stills (Brain Brake originals)
- download an original frame (Brain Brake originals)

### [Brain Brake review wall](../apps/BRAIN_BRAKE_REVIEW.md)

macOS/Web; API: door 8777. Main call: `curl -s -XPOST 127.0.0.1:8777/api/verdict -H 'Content-Type: application/json' -d '{"verdict":"keep"}' # body field names are not documented; the page keys are k (keep) and r (redo)`

Before: Needs gh logged in as the repo owner; REVIEW_RAW points it at a local mock for tests.

- review the new film frames and say keep or redo (Brain Brake review wall)
- show generated frames on the screen as they arrive (Brain Brake review wall)
- send verdicts to the chat session (Brain Brake review wall)

### [Colab Video Upscaler](../apps/colab-video-upscaler.md)

macOS/Cloud; API: cli. Main call: `python3 colab_restore.py status`

Before: Needs the Colab notebook linked by 'link'; run in the repo folder.

- upscale a blocky video for free (Colab Video Upscaler) - call: `python3 colab_restore.py assemble`
- restore faces in a lecture video (Colab Video Upscaler)
- use Colab GPU to improve Resolve clips (Colab Video Upscaler)

### [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md)

macOS; API: cli. Main call: `curl -s -X POST 'http://127.0.0.1:8940/run' -H 'Content-Type: application/json' -d '{"who":"me","code":"result = project.GetName()","timeout":30}'`

Before: DaVinci Resolve Actions (Mantra) must be running; the router starts with it and ends with it, and only while Resolve runs does it answer. Never open a second Resolve connection: send everything through POST /run (HTTP codes: 200 done, 503 busy, 423 held by someone else, 504 timeout, 500 code failed).

- automatically grade and export in Resolve (DaVinci Resolve Actions) - call: `curl -s 127.0.0.1:8940/status`
- switch Resolve page from a script (DaVinci Resolve Actions)
- create a timeline from the selected clips (DaVinci Resolve Actions)
- run Python inside DaVinci Resolve safely (DaVinci Resolve Actions)
- back up and clean a Resolve project (DaVinci Resolve Actions)
- toggle HD and UHD in Resolve (DaVinci Resolve Actions)
- previous page in DaVinci Resolve (DaVinci Resolve Actions)

### [Free Voice Convert (Equalizer)](../apps/FREE_VOICE_CONVERT.md)

macOS/Windows; API: cli. Main call: `python3 engine/fvc.py run job.json`

Before: Run in the repo folder; models are fetched first with fvc.py fetch.

- make all my clips sound like the same voice (Free Voice Convert) - call: `python3 engine/fvc.py profile voice.wav marko`
- fix AI video voices to match (Free Voice Convert)
- replace the Resolve voice cleanup steps (Free Voice Convert)
- stitch clips with the same sound (Free Voice Convert)

### [Import Button (Mantra)](../apps/IMPORT_BUTTON.md)

macOS; API: accessibility. Main call: `star press "import button" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- import media in Resolve with a mouse button (Import Button)
- map a mouse thumb button to a shortcut (Import Button)

### [MKV Converter (MPA)](../apps/MKV_CONVERTER.md)

macOS; API: none

- make a browser MKV importable in DaVinci Resolve (MKV Converter)
- convert classroom recordings for editing (MKV Converter)

### [Resolve Pages (Mantra)](../apps/RESOLVE_PAGES.md)

macOS; API: accessibility. Main call: `star press "resolve pages" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- switch Resolve pages from the keyboard (Resolve Pages)
- see which Resolve page is open (Resolve Pages)

### [Stop the Background AI in Avid Media Composer](../apps/AVID_BACKGROUND.md)

Web; API: none

- Avid is slow because of background AI (Stop the Background AI in Avid Media Composer)
- stop Avid background services (Stop the Background AI in Avid Media Composer)
- turn off Avid transcription (Stop the Background AI in Avid Media Composer)

### [The Brain Brake (film repository)](../apps/BRAIN_BRAKE.md)

macOS/Web; API: none

- where is the Brain Brake script (The Brain Brake)
- read the film's handover (The Brain Brake)
- rebuild the Brain Brake site (The Brain Brake)
- what is the state of the film (The Brain Brake)

### [UHD HD Display (Mantra)](../apps/UHD_HD_DISPLAY.md)

macOS; API: accessibility. Main call: `star press "uhd hd" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- switch Resolve between HD and UHD (UHD HD Display)
- see current Resolve resolution (UHD HD Display)


## Retired - do not use

- [DaVinci Resolve Assistant (retired)](../apps/DAVINCI_RESOLVE_ASSISTANT.md) - replaced by [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md)
