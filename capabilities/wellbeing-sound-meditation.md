[Back to the index](../CAPABILITIES.md)

# Wellbeing, sound and meditation

### [Asana Guide (Mantra)](../apps/ASANA_GUIDE.md)

Android; API: none

- guide me through yoga poses (Asana Guide)
- explain an asana aloud (Asana Guide)
- build the asana guide APK (Asana Guide)

### [Hemi-Sync Recording Monitor (Mantra)](../apps/HEMISYNC_RECORDING_MONITOR.md)

macOS; API: none

- how far is the Hemi-Sync recording (Hemi-Sync Recording Monitor)
- monitor the long recording job (Hemi-Sync Recording Monitor)
- when will the recording finish (Hemi-Sync Recording Monitor)

### [Indian Mantras (Mantra)](../apps/INDIAN_MANTRAS.md)

macOS; API: none

- learn the Gayatri mantra word by word (Indian Mantras)
- practise Asato Ma pronunciation (Indian Mantras)
- listen to a mantra lesson offline (Indian Mantras)

### [Mantra Room (Meditation Room / Chakra and Elements Toning)](../apps/MANTRA_ROOM.md)

macOS/Android/Linux/Web; API: door 8965. Main call: `curl -s -XPOST localhost:8965/api/play-loop -d '{"output":"BlackHole 2ch","lights":true,"until":"11:55","gain_db":-5}'`

Before: The app must be running (open -g -a "Meditation Room (Mantra)"); it answers on 127.0.0.1 only, and the port is claimed through MANTRA_PORTS under the id meditation-room.

- play meditation toning with visuals (Mantra Room)
- loop meditation audio to a chosen output until a time (Mantra Room) - call: `curl -s -XPOST 127.0.0.1:8965/api/outputs`
- put visuals on the keyboard lights (Mantra Room) - call: `curl -s -XPOST 127.0.0.1:8965/api/lights -d '{"on":false}'`
- stream the meditation visuals (Mantra Room)
- breathing circle and session timer (Mantra Room)

### [Mind Garden](../apps/kognius_app.md)

Android; API: none

- brain training app offline (Mind Garden)
- puzzles and memory games for an older person (Mind Garden)
- build and release the Mind Garden APK (Mind Garden)

### [Minimalist Stopwatch](../apps/MINIMALIST_STOPWATCH.md)

Android; API: none

- big stopwatch on the phone (Minimalist Stopwatch)
- countdown timer readable across the room (Minimalist Stopwatch)
- simple clock app (Minimalist Stopwatch)

### [Shruti Box and Voice Trainer](../apps/SHRUTI_BOX_AND_VOICE_TRAINER.md)

Android; API: none

- shruti box on the phone (Shruti Box and Voice Trainer)
- drone for singing practice (Shruti Box and Voice Trainer)
- voice trainer pitch exercises (Shruti Box and Voice Trainer)
- raga drone (Shruti Box and Voice Trainer)

### [Story Medicine](../apps/THERAPEUTIC_STORIES.md)

Android; API: none

- story for a child about a hard event (Story Medicine)
- therapeutic story generator (Story Medicine)
- read a bedtime story aloud (Story Medicine)

