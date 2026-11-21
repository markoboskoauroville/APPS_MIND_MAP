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

- where are the animator's frames for scene 3 -> [Animator Collaboration](../apps/ANIMATOR_COLLABORATION.md) (Web; API: none)
- hand over frames to the animator -> [Animator Collaboration](../apps/ANIMATOR_COLLABORATION.md) (Web; API: none)
- what changed in the Brain Brake frames -> [Animator Collaboration](../apps/ANIMATOR_COLLABORATION.md) (Web; API: none)
- automate Avid Media Composer clicks -> [Avid Assistant](../apps/AVID_ASSISTANT.md) (Windows; API: none)
- stop a running macro -> [Avid Assistant](../apps/AVID_ASSISTANT.md) (Windows; API: none)
- set up the edit suite monitors on Windows -> [Avid Assistant](../apps/AVID_ASSISTANT.md) (Windows; API: none)
- control Blender from the terminal -> [Blender Control](../apps/blender-control.md) (macOS; API: cli) - call: `python3 .agents/skills/blender-control/scripts/blender_cli.py ping # Blender must run with its control add-on on port 9876`
- render a Blender scene to PNG or MP4 -> [Blender Control](../apps/blender-control.md) (macOS; API: cli)
- build a 3D scene with a Python script in the open Blender -> [Blender Control](../apps/blender-control.md) (macOS; API: cli)
- change colours in a video frame by frame with Blender -> [Blender Control](../apps/blender-control.md) (macOS; API: cli)
- start the Blender bridge -> [Blender Control](../apps/blender-control.md) (macOS; API: cli)
- render the Brain Brake key -> [Brain Brake 3D](../apps/BRAIN_BRAKE_3D.md) (macOS; API: cli) - call: `/Applications/Blender.app/Contents/MacOS/Blender --background --python scripts/render_key.py`
- 3D key for the film -> [Brain Brake 3D](../apps/BRAIN_BRAKE_3D.md) (macOS; API: cli)
- run Blender headless to render stills -> [Brain Brake 3D](../apps/BRAIN_BRAKE_3D.md) (macOS; API: cli)
- get the Brain Brake theme song -> [Brain Brake audio](../apps/BRAINBREAK_AUDIO.md) (Web; API: none)
- where is the radio drama audio -> [Brain Brake audio](../apps/BRAINBREAK_AUDIO.md) (Web; API: none)
- the film's voice takes -> [Brain Brake audio](../apps/BRAINBREAK_AUDIO.md) (Web; API: none)
- see all the film's frames at once -> [Brain Brake frames](../apps/BRAIN_BRAKE_FRAMES.md) (Web; API: none)
- Brain Brake contact sheet -> [Brain Brake frames](../apps/BRAIN_BRAKE_FRAMES.md) (Web; API: none)
- full resolution frame of scene 1 -> [Brain Brake originals](../apps/BRAIN_BRAKE_ORIGINALS.md) (Web; API: none)
- where are the original film stills -> [Brain Brake originals](../apps/BRAIN_BRAKE_ORIGINALS.md) (Web; API: none)
- download an original frame -> [Brain Brake originals](../apps/BRAIN_BRAKE_ORIGINALS.md) (Web; API: none)
- review the new film frames and say keep or redo -> [Brain Brake review wall](../apps/BRAIN_BRAKE_REVIEW.md) (macOS/Web; API: door 8777) - call: `curl -s -XPOST 127.0.0.1:8777/api/verdict -H 'Content-Type: application/json' -d '{"verdict":"keep"}' # body field names are not documented; the page keys are k (keep) and r (redo)`
- show generated frames on the screen as they arrive -> [Brain Brake review wall](../apps/BRAIN_BRAKE_REVIEW.md) (macOS/Web; API: door 8777)
- send verdicts to the chat session -> [Brain Brake review wall](../apps/BRAIN_BRAKE_REVIEW.md) (macOS/Web; API: door 8777)
- upscale a blocky video for free -> [Colab Video Upscaler](../apps/colab-video-upscaler.md) (macOS/Cloud; API: cli) - call: `python3 colab_restore.py status`
- restore faces in a lecture video -> [Colab Video Upscaler](../apps/colab-video-upscaler.md) (macOS/Cloud; API: cli)
- use Colab GPU to improve Resolve clips -> [Colab Video Upscaler](../apps/colab-video-upscaler.md) (macOS/Cloud; API: cli)
- automatically grade and export in Resolve -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli) - call: `curl -s -X POST 'http://127.0.0.1:8940/run' -H 'Content-Type: application/json' -d '{"who":"me","code":"result = project.GetName()","timeout":30}'`
- switch Resolve page from a script -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- create a timeline from the selected clips -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- run Python inside DaVinci Resolve safely -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- back up and clean a Resolve project -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- toggle HD and UHD in Resolve -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- previous page in DaVinci Resolve -> [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md) (macOS; API: cli)
- make all my clips sound like the same voice -> [Free Voice Convert (Equalizer)](../apps/FREE_VOICE_CONVERT.md) (macOS/Windows; API: cli) - call: `python3 engine/fvc.py run job.json`
- fix AI video voices to match -> [Free Voice Convert (Equalizer)](../apps/FREE_VOICE_CONVERT.md) (macOS/Windows; API: cli)
- replace the Resolve voice cleanup steps -> [Free Voice Convert (Equalizer)](../apps/FREE_VOICE_CONVERT.md) (macOS/Windows; API: cli)
- stitch clips with the same sound -> [Free Voice Convert (Equalizer)](../apps/FREE_VOICE_CONVERT.md) (macOS/Windows; API: cli)
- import media in Resolve with a mouse button -> [Import Button (Mantra)](../apps/IMPORT_BUTTON.md) (macOS; API: accessibility) - call: `star press "import button" "top"`
- map a mouse thumb button to a shortcut -> [Import Button (Mantra)](../apps/IMPORT_BUTTON.md) (macOS; API: accessibility)
- make a browser MKV importable in DaVinci Resolve -> [MKV Converter (MPA)](../apps/MKV_CONVERTER.md) (macOS; API: none)
- convert classroom recordings for editing -> [MKV Converter (MPA)](../apps/MKV_CONVERTER.md) (macOS; API: none)
- switch Resolve pages from the keyboard -> [Resolve Pages (Mantra)](../apps/RESOLVE_PAGES.md) (macOS; API: accessibility) - call: `star press "resolve pages" "top"`
- see which Resolve page is open -> [Resolve Pages (Mantra)](../apps/RESOLVE_PAGES.md) (macOS; API: accessibility)
- Avid is slow because of background AI -> [Stop the Background AI in Avid Media Composer](../apps/AVID_BACKGROUND.md) (Web; API: none)
- stop Avid background services -> [Stop the Background AI in Avid Media Composer](../apps/AVID_BACKGROUND.md) (Web; API: none)
- turn off Avid transcription -> [Stop the Background AI in Avid Media Composer](../apps/AVID_BACKGROUND.md) (Web; API: none)
- where is the Brain Brake script -> [The Brain Brake (film repository)](../apps/BRAIN_BRAKE.md) (macOS/Web; API: none)
- read the film's handover -> [The Brain Brake (film repository)](../apps/BRAIN_BRAKE.md) (macOS/Web; API: none)
- rebuild the Brain Brake site -> [The Brain Brake (film repository)](../apps/BRAIN_BRAKE.md) (macOS/Web; API: none)
- what is the state of the film -> [The Brain Brake (film repository)](../apps/BRAIN_BRAKE.md) (macOS/Web; API: none)
- switch Resolve between HD and UHD -> [UHD HD Display (Mantra)](../apps/UHD_HD_DISPLAY.md) (macOS; API: accessibility) - call: `star press "uhd hd" "top"`
- see current Resolve resolution -> [UHD HD Display (Mantra)](../apps/UHD_HD_DISPLAY.md) (macOS; API: accessibility)

## Retired - do not use

- [DaVinci Resolve Assistant (retired)](../apps/DAVINCI_RESOLVE_ASSISTANT.md) - replaced by [DaVinci Resolve Actions (Mantra)](../apps/DAVINCI_RESOLVE_ACTIONS.md)
