[Back to the index](../CAPABILITIES.md)

# Voice, dictation and transcription

## Which one to pick: Transcription (speech to text): Mac, Android, Termux, web, Croatian

One pick for a Croatian voice recording on the phone: MAHA_TRANSCRIBE_TERMUX_TERMINAL (command `transcribe`, active, current). The Croatian language hint is documented for the Maha Transcribe pages (Whisper on Groq); the Termux README itself does not repeat it, so check the language box in the page. Mac: dictation is Vox to Txt (MANTRA_VOICE_TO_TEXT, F1 hotkey, language en, hr or auto, port 8865 for files); a YouTube link or file goes through `scribe` (MAC_TRANSCRIBER). Android: TTT is the voice keyboard (English and Croatian engines); MAHA_TRANSCRIBE_ANDROID_2 is the native app, version 1 only the Talk to Type screen; TATA_Talk is a simple Croatian-only app in a private repo. Termux: `transcribe` (MAHA_TRANSCRIBE_TERMUX_TERMINAL) serves the page. Web and servers: the Streamlit and Flask Maha Transcribe pages (Whisper on Groq, language hint hr), 111/222 Transcribe (AssemblyAI with speakers and subtitles) and the hosted TTT Portal API. MARKO_TRANSCRIBE, MAHA_TRANSCRIBE_TERMUX and the web-view MAHA_TRANSCRIBE_ANDROID are superseded.

| You want | Use | How |
|---|---|---|
| transcribe a Croatian voice recording on the phone (Termux) | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `transcribe 9000 # in Termux: starts the Maha Transcribe page on port 9000 and opens it in Chrome; record or upload there, set the language to Croatian (hr) in the page, and paste your own Groq key once. No HTTP API: the page is the interface` |
| dictate into any Mac app with a hotkey, Croatian or English | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](../apps/MANTRA_VOICE_TO_TEXT.md) |  |
| transcribe a WAV on the Mac through a local call | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](../apps/MANTRA_VOICE_TO_TEXT.md) | `curl -s -XPOST '127.0.0.1:8865/hear?lang=hr' --data-binary @take.wav` |
| transcribe a YouTube video or audio file with Groq, AssemblyAI or Deepgram | [Mac Transcriber (scribe) (MAC_TRANSCRIBER)](../apps/MAC_TRANSCRIBER.md) | `scribe https://www.youtube.com/watch?v=<id> --engine groq --out ~/transcripts` |
| dictate Croatian on an Android phone (keyboard) | [TTT Voice Type keyboard (TTT)](../apps/TTT.md) |  |
| record and transcribe on Android in a native app (talk to type screen) | [Maha Transcribe Android (native) (MAHA_TRANSCRIBE_ANDROID_2)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) |  |
| simple one-button Croatian speech to text on Android | [TA-TA Talk (Croatian dictation) (TATA_Talk)](../apps/TATA_Talk.md) |  |
| transcribe in the browser with Groq Whisper, English or Croatian | [Maha Transcribe / TTT-LLL (Streamlit) (MAHA_TRANSCRIBE_STREAMLIT)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md) |  |
| transcribe an interview with speakers and subtitles (upload) | [222 Transcribe (222-transcribe)](../apps/222-transcribe.md) |  |
| transcribe through a hosted HTTP API | [TTT Portal (TTT_PORTAL)](../apps/TTT_PORTAL.md) | `curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe` |
| download the audio of a whole YouTube channel for transcription (Groq Whisper, optional summary) | [YT Transcriber (YT_TRANSCRIBER)](../apps/YT_TRANSCRIBER.md) | `./download_channel.sh https://www.youtube.com/@channel mychannel --limit 20` |

## Which one to pick: Read aloud / text to speech: Mac, Android, Termux, engines

On the Mac, speaking and reading are one server: Mantra Voice (MANTRA_VOICE, port 8837) with `/speak` for a spoken line and `/say` for mp3 plus word timings; VOICE_ENGINE is only the subtitle band and the global on/off switch. On the phone, `phonesay` and TERMUX_VOICE (port 8840) speak a line; the browser reader with the word lit is MA_READER_TERMUX_MACOS (Termux or Mac, Edge and Speechify voices, port 8081). The native Android app MA Reader (MA_READER_ANDROID) does not speak yet; its engine is the Kotlin library MA_READER_ENGINE (Edge speech with word timing) that TTT's LLL reader also uses. Google voices are GOOGLE_TTS_STT (gtt, 7311) and GoogleVoices (gvoice, 8300).

| You want | Use | How |
|---|---|---|
| make the Mac speak a sentence | [Mantra Voice (speech server) (MANTRA_VOICE)](../apps/MANTRA_VOICE.md) | `curl -s -XPOST 127.0.0.1:8837/speak -H 'Content-Type: application/json' -d '{"text":"The render is done.","wait":true}'` |
| get mp3 plus word timings for a highlighted reader page | [Mantra Voice (speech server) (MANTRA_VOICE)](../apps/MANTRA_VOICE.md) | `curl -s -XPOST 127.0.0.1:8837/say -H 'Content-Type: application/json' -d '{"text":"Hello"}'` |
| mute or switch all Claude voices, subtitle band, replay | [Voice Engine (Mantra) (VOICE_ENGINE)](../apps/VOICE_ENGINE.md) | `voiceengine off (writes ~/.mantra/voice_engine_state and stops the current reading)` |
| make the phone speak a sentence | [Termux Voice (voiced) (TERMUX_VOICE)](../apps/TERMUX_VOICE.md) | `phonesay pixel "The render is done."` |
| read pasted text aloud with the word lit, on the phone (Termux) or the Mac | [MA Reader Termux / macOS (Edge / Speechify) (MA_READER_TERMUX_MACOS)](../apps/MA_READER_TERMUX_MACOS.md) | `curl -s -X POST http://127.0.0.1:8081/api/say -H 'Content-Type: application/json' -d '{"text":"hello","lang":"en"}' -o out.mp3` |
| read aloud with the word lit on Android: use the Termux reader; the native app is not speaking yet | [MA Reader for Android (MA_READER_ANDROID)](../apps/MA_READER_ANDROID.md) |  |
| reuse the Edge speech client with word timing in Kotlin | [MA Reader Engine (MA_READER_ENGINE)](../apps/MA_READER_ENGINE.md) |  |
| Speechify key ring and Speechify voices on the phone | [MA Reader Speechify module (MA_READER_SPEECHIFY)](../apps/MA_READER_SPEECHIFY.md) |  |
| Google or Gemini voice for a sentence | [Google TTS and STT (gtt) (GOOGLE_TTS_STT)](../apps/GOOGLE_TTS_STT.md) | `curl -s -XPOST 127.0.0.1:7311/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}'` |
| read text aloud in a web page with word highlighting (Streamlit) | [EdgeReader (MA Reader Streamlit) (mareader)](../apps/mareader.md) |  |

## Which one to pick: Voice dictation keyboard

On Android the voice keyboard is TTT (Talk to Type, repo TTT; package seen as tttlight): dictate into any text field with cloud or offline engines, with an RE reply assistant and an adb remote API. DictateKeyboard (TTT&LLL) is the older fork with the AI reader (LLL) and is dormant; ttt-layouts restores the owner's key layout. On the Mac and Windows the equivalent is Vox to Txt (MANTRA_VOICE_TO_TEXT): press F1, talk, press F1, the words are typed at the cursor.

| You want | Use | How |
|---|---|---|
| dictate on an Android phone into any app | [TTT Voice Type keyboard (TTT)](../apps/TTT.md) |  |
| type text into the focused field of the phone from a script | [TTT Voice Type keyboard (TTT)](../apps/TTT.md) | `python3 tools/ttt_remote.py say "The render is done"` |
| restore my TTT keyboard layout on a new phone | [TTT Layouts (ttt-layouts)](../apps/ttt-layouts.md) |  |
| dictate on the Mac or Windows with F1 | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](../apps/MANTRA_VOICE_TO_TEXT.md) |  |
| older keyboard with the reader (LLL) | [TTT&LLL (Talk to Type, Look Listen Learn) (DictateKeyboard)](../apps/DictateKeyboard.md) |  |

### [111 Transcribe](../apps/111-transcribe.md)

Web/Cloud; API: none

- transcribe a long interview with speakers (111 Transcribe)
- make subtitles from a video (111 Transcribe)
- upload a file and get text (111 Transcribe)
- translate a transcript (111 Transcribe)

### [222 Transcribe](../apps/222-transcribe.md)

Web/Cloud; API: none

- transcribe this interview with speakers (222 Transcribe)
- get subtitles for a video file (222 Transcribe)
- transcribe a recording from my phone (222 Transcribe)
- make a transcript from a shared link (222 Transcribe)

### [EdgeReader (MA Reader Streamlit)](../apps/mareader.md)

Web/Cloud; API: none

- read this text aloud with highlighted words (EdgeReader)
- Croatian text to speech reader (EdgeReader)
- translate my speech between Croatian, English and German (EdgeReader)
- make per-sentence mp3 files from a text (EdgeReader)

### [Google TTS and STT (gtt)](../apps/GOOGLE_TTS_STT.md)

macOS/Android/Termux/Web; API: door 7311. Main call: `curl -s -XPOST 127.0.0.1:7311/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs`

Before: Start with the command gtt (menu and the app on localhost:7311, port 7311 or next free up to 7327). Tests make real calls and a TTS account allows about ten requests a day: run gtt test only on request.

- read text aloud with Gemini voices (Google TTS and STT) - call: `curl -s 127.0.0.1:7311/api/voices`
- transcribe audio with Gemini (Google TTS and STT)
- manage my Gemini free keys (Google TTS and STT)
- text to speech on the phone (Google TTS and STT)

### [GVoices (Google Voices)](../apps/GoogleVoices.md)

macOS/Android/Termux/Linux/Web; API: http 8300. Main call: `curl -s -XPOST 127.0.0.1:8300/api/say -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs`

Before: Start with the command gvoice (port 8300, up to 8315; the live port is in ~/.mantra/ports/gvoice). TTS only; overlaps with GOOGLE_TTS_STT.

- text to speech with a Google voice (GVoices)
- make a WAV of a sentence with Gemini (GVoices)
- gvoice command (GVoices)
- pick a Gemini voice (GVoices)

### [MA Reader Engine](../apps/MA_READER_ENGINE.md)

Android; API: none

- text to speech with word timing in Kotlin (MA Reader Engine)
- reuse the Edge voice client (MA Reader Engine)
- highlight the spoken word (MA Reader Engine)
- engine for a native Android reader (MA Reader Android, LLL in TTT) (MA Reader Engine)

### [MA Reader for Android](../apps/MA_READER_ANDROID.md)

Android; API: http. Main call: `curl -s http://127.0.0.1:<port>/api/voices # lists English and Croatian voices; the app does NOT speak yet`

Before: Only reachable from inside the phone. Text is pasted, split into sentences, rendered and archived; the voice client is the next step (README: 'It does not speak yet'). To read aloud with highlighting on the phone today use MA_READER_TERMUX_MACOS or MA_READER_SPEECHIFY (Termux).

- MA Reader on the phone (native app, text only for now) (MA Reader for Android)
- paste text and keep a reading library on Android (MA Reader for Android)

### [MA Reader Speechify module](../apps/MA_READER_SPEECHIFY.md)

Android/Termux/Web; API: http 8081. Main call: `curl http://localhost:8081/api/voices`

Before: Termux read-aloud web app (v34) with Edge and Speechify voices; routes were read from the v26 installer script and v34 has not yet run on the phone.

- use many Speechify keys with rotation (MA Reader Speechify module)
- read text aloud in Croatian or English on the phone (MA Reader Speechify module)
- wire Speechify into another app (MA Reader Speechify module)

### [MA Reader Termux / macOS (Edge / Speechify)](../apps/MA_READER_TERMUX_MACOS.md)

macOS/Android/Termux; API: http 8081. Main call: `curl -s -X POST http://127.0.0.1:8081/api/say -H 'Content-Type: application/json' -d '{"text":"hello","lang":"en"}' -o out.mp3`

Before: Install with the single-file installer (Termux or macOS); start with mareadweb, which serves the page on 8081 (updates with maread-update). Keys for Speechify come from KEYRING_TERMUX; Edge voices need no key.

- read text aloud on the phone or Mac with the word lit (MA Reader Termux / macOS)
- text to speech reader with word highlighting (MA Reader Termux / macOS) - call: `curl -s 127.0.0.1:8081/api/state`
- read aloud with highlighting on Android (in Termux, in Chrome) (MA Reader Termux / macOS)
- install the MA Reader (MA Reader Termux / macOS)

### [Mac Transcriber (scribe)](../apps/MAC_TRANSCRIBER.md)

macOS; API: cli. Main call: `scribe <youtube-url> --engine groq --out ~/transcripts`

Before: Needs the key of the chosen engine in the key ring (scribe keys shows them).

- transcribe a YouTube video to text (Mac Transcriber)
- transcribe a long audio file with timestamps (Mac Transcriber)
- check which transcription keys work (Mac Transcriber)

### [Magic Coin](../apps/magic-coin.md)

macOS; API: none

- read aloud the text under my cursor on the Mac (Magic Coin)
- floating dictation button on screen (Magic Coin)
- speech to text widget for macOS (Magic Coin)

### [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md)

macOS/Android/Termux/Linux; API: http 8420. Main call: `transcribe 9000 # starts the page on port 9000 (default 8420, next free port if taken) and opens it in Chrome`

Before: Install once (one shell command per the README) in Termux, macOS or Linux; the command prints and opens the port it got.

- use Maha Transcribe from the terminal (Maha Transcribe)
- start the dictation page locally (Maha Transcribe)
- microphone page on Termux (Maha Transcribe)
- optimise audio before upload (Maha Transcribe)
- transcribe voice on the phone in Termux (Maha Transcribe)
- run a local transcription server on Android (Maha Transcribe)

### [Maha Transcribe / TTT-LLL (Streamlit)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md)

Web/Cloud; API: http 8810. Main call: `Open the Streamlit page, record in the browser, choose language en or hr, press transcribe # no HTTP call: only GET /healthz exists`

Before: No control API: GET /healthz only says the process is up (the handover says it does not prove the app works).

- transcribe my voice in the browser (Maha Transcribe / TTT-LLL)
- dictate in Croatian or English (Maha Transcribe / TTT-LLL)
- read text aloud and show it (Maha Transcribe / TTT-LLL)
- speech to text with Groq Whisper (Maha Transcribe / TTT-LLL)

### [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md)

Android; API: none

- native Android dictation app (Maha Transcribe Android)
- speech to text on Android with big buttons (Maha Transcribe Android)
- record and transcribe on the phone (Maha Transcribe Android)
- dictate on Android (v1: the T screen only) (Maha Transcribe Android)

### [Maha Transcribe Flask](../apps/MAHA_TRANSCRIBE_FLASK.md)

Linux/Web/Cloud; API: http 8700. Main call: `curl -s -XPOST <base>/flask/api/recordings/<id>/transcribe -H 'Content-Type: application/json' -d '{"language":"hr"}'`

Before: Runs behind a login on a server (port 8700 behind the path /flask/); the shared login of the one-login-for-all-apps setup is needed, base is the hosted address (not published here).

- dictate and get text in Croatian (Maha Transcribe Flask)
- read my text aloud with highlighted words (Maha Transcribe Flask)
- keep transcripts as notes (Maha Transcribe Flask)

### [Maha Transcribe VM (TTT-LLL)](../apps/MAHA_TRANSCRIBE_VM.md)

Linux/Web/Cloud; API: http 8810. Main call: `Open the page, record in the browser, press transcribe # no HTTP call: only GET /healthz exists`

Before: No control API: GET /healthz only says the process is up.

- dictate by voice into text in the browser (Maha Transcribe VM)
- read text aloud in a chosen voice (Maha Transcribe VM)
- transcribe Croatian speech (Maha Transcribe VM)

### [Maha Transcriber and Reader (web)](../apps/maha-transcriber-reader.md)

Web; API: none

- transcribe my voice in the browser (Maha Transcriber and Reader)
- read text aloud with highlighted words (Maha Transcriber and Reader)
- Croatian text to speech (Maha Transcriber and Reader)
- test my speech API keys (Maha Transcriber and Reader)

### [Mantra Corrections](../apps/MANTRA_CORRECTIONS.md)

macOS/Android; API: none

- fix repeated dictation mistakes (Mantra Corrections)
- share dictation corrections between Mac and phone (Mantra Corrections)

### [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md)

macOS; API: http 8837. Main call: `curl -s -XPOST 127.0.0.1:8837/speak -H 'Content-Type: application/json' -d '{"text":"The render is done.","wait":true}'`

Before: Mantra Voice (the Flask server voiced.py) must be running on the Mac; speech and listening live only here, never start a second Whisper or TTS. Over Tailscale only /render, /hear, /voices and /health are open without the token.

- transcribe this audio file locally (Mantra Voice)
- make the computer say this sentence (Mantra Voice)
- clone a voice from a recording (Mantra Voice) - call: `curl -s 127.0.0.1:8837/voices`
- read a page aloud with the word highlighted (Mantra Voice)
- speak a status message when a job is done (Mantra Voice)

### [Mantra Voice to Text (downloads)](../apps/mantra-voice-to-text-downloads.md)

macOS/Windows/Web; API: none

- download Mantra Voice to Text (Mantra Voice to Text)
- free offline dictation for Mac or Windows (Mantra Voice to Text)
- press F1 and dictate anywhere (Mantra Voice to Text)

### [Marko Transcribe (Streamlit)](../apps/marko-transcribe.md)

Web/Cloud; API: none

- transcribe a long audio file online (Marko Transcribe)
- web transcription app with AssemblyAI (Marko Transcribe)

### [Sample Player, Android](../apps/SAMPLE_PLAYER.md)

Android; API: none

- record phrases on the phone and re-voice them (Sample Player, Android)
- sample player with my own voice cells (Sample Player, Android)
- record a phrase over any app with a floating button (Sample Player, Android)

### [Sample Player, macOS](../apps/SAMPLE_PLAYER_MACOS.md)

macOS/Web; API: http. Main call: `curl -s -XPOST 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/record/<slot> # records into a cell; slot names are in GET /api/state`

Before: Start the server first (it picks a free port and writes it to ~/.sampleplayer-web/port.txt).

- sample player on the Mac (Sample Player, macOS)
- record phrases and swap the voice (Sample Player, macOS)
- clone a voice with consent (Sample Player, macOS)
- web sample sequencer from the terminal (Sample Player, macOS)

### [TA-TA Talk (Croatian dictation)](../apps/TATA_Talk.md)

Android; API: none

- dictate Croatian text on a phone (TA-TA Talk)
- simple one-button voice to text (TA-TA Talk)

### [Talk Mode (Mantra)](../apps/TALK_MODE.md)

macOS; API: cli. Main call: `# no call: read state.json of the app (folder not given in the docs); Queen answers 'talk mode status'`

Before: Talk Mode (Mantra) is a client of other apps' APIs (Voice to Text, Mantra Voice); no listening server found. Queen answers 'talk mode status'. Switch keys F5-F8 since v17.

- talk to Claude with my voice (Talk Mode)
- dictate to a terminal session and hear the reply (Talk Mode)
- hands-free conversation with Claude Code (Talk Mode)
- which session am I talking to (Talk Mode)

### [Talk with Claude Code](../apps/TALK_WITH_CLAUDE.md)

macOS; API: http 8835. Main call: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py reply "..."`

Before: Talk with Claude Code (talkd.py) on 8835.

- talk to Claude Code by voice (Talk with Claude Code) - call: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py up`
- speak with the computer and hear the answer (Talk with Claude Code)

### [TTT Layouts](../apps/ttt-layouts.md)

Android; API: none

- apply my TTT keyboard layout (TTT Layouts)
- restore the TTT keys and colours on a new phone (TTT Layouts)

### [TTT Voice Type keyboard](../apps/TTT.md)

Android; API: adb. Main call: `python3 tools/ttt_remote.py say "The render is done" # speaks through TTT; type into the focused field with the type verb`

Before: Phone on adb (cable or wireless); only adb can send these broadcasts (DUMP permission). Answers land in `files/remote/<id>.json` on the phone.

- dictate on the phone into any app (TTT Voice Type keyboard)
- voice keyboard for Android (TTT Voice Type keyboard)
- reply to a message with AI by voice (TTT Voice Type keyboard)
- compare transcription engines on the phone (TTT Voice Type keyboard)
- make the phone speak via TTT (TTT Voice Type keyboard)

### [TTT&LLL (Talk to Type, Look Listen Learn)](../apps/DictateKeyboard.md)

Android; API: none

- dictate on my Android phone (TTT&LLL)
- voice typing keyboard with my own keys (TTT&LLL)
- offline Whisper keyboard (TTT&LLL)
- talk to type on Android (TTT&LLL)

### [Voice Cloning (Mantra)](../apps/VOICE_CLONING.md)

macOS; API: accessibility. Main call: `star press "voice cloning" "top"`

Before: No HTTP or CLI door of its own: the window's controls are Accessibility buttons with fixed ids, pressed through STAR_API (star press `"<app>"` `"<id>"`, or POST `127.0.0.1:8863/apps/<app>/press` `{"label":"<id>"}`); the app must be running (star open `"<app>"`). Macro Recorder needs the Accessibility permission.

- clone a new voice (Voice Cloning)
- change which voice the computer uses (Voice Cloning)

### [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md)

macOS; API: http 8837. Main call: `voiceengine off (writes ~/.mantra/voice_engine_state and stops the current reading)`

Before: Voice Engine (Mantra) is the window and the switch; the speech itself is done by MANTRA_VOICE on port 8837, which must be running. The off state does not touch speech to text.

- mute all Claude voices (Voice Engine)
- global voice on and off switch (Voice Engine)
- subtitle while Claude speaks (Voice Engine)
- replay what Claude just said (Voice Engine)
- pause the voice reading (Voice Engine)
- turn the computer voice off (Voice Engine)
- switch the voice engine on (Voice Engine)

### [Voice Engine Universal (Mantra)](../apps/VOICE_ENGINE_UNIVERSAL.md)

macOS/Android; API: none

- shared subtitle pause logic (Voice Engine Universal)
- word-exact pause for a speaking server (Voice Engine Universal)
- spec for subtitle following the voice (Voice Engine Universal)

### [Voice Engines (model hub)](../apps/VOICE_ENGINES.md)

macOS; API: cli. Main call: `voice-engines fetch qwen06 # downloads the model 'qwen06' into the shared hub`

- download a speech model (Voice Engines) - call: `voice-engines where`
- see which voice engines are installed (Voice Engines)
- move the models folder (Voice Engines)

### [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md)

macOS/Windows; API: http 8865. Main call: `curl -s -XPOST '127.0.0.1:8865/hear?lang=en' --data-binary @take.wav`

Before: Vox to Txt (Mantra) must be running (menu-bar app; its door answers only for host 127.0.0.1). Dictation itself is the F1 key: press F1, talk, press F1, the words are typed at the cursor.

- dictate into any Mac app with a hotkey (Vox to Txt)
- transcribe an audio file (Vox to Txt) - call: `curl -s -XPOST 127.0.0.1:8865/transcribe -H 'Content-Type: application/json' -d '{"path":"~/take.wav","language":"hr"}' # then: curl -s 127.0.0.1:8865/job/<id>`
- speech to text in Croatian and English (Vox to Txt)
- get text from a WAV through a local call (Vox to Txt)
- dictate text anywhere on the Mac (Vox to Txt)
- clean up dictated text (Vox to Txt)

### [YT Transcriber](../apps/YT_TRANSCRIBER.md)

macOS/Linux/Cloud; API: http 8851. Main call: `./download_channel.sh https://www.youtube.com/@channel mychannel --limit 20 # downloads audio of the last 20 videos of a channel`

- transcribe a whole YouTube channel (YT Transcriber)
- get all transcripts of a playlist (YT Transcriber)
- summarise a channel into topics (YT Transcriber)


## Retired - do not use

- [Maha Transcribe Android v3 (web view, superseded) (retired)](../apps/MAHA_TRANSCRIBE_ANDROID.md) - replaced by [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md)
- [Maha Transcribe Termux v1 (superseded) (retired)](../apps/MAHA_TRANSCRIBE_TERMUX.md) - replaced by [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md)
- [Transcribe Voice to Text RT (Mantra) (retired)](../apps/MARKO_TRANSCRIBE.md) - replaced by [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md)
- [Voice of Claude (Mantra) (retired)](../apps/VOICE_OF_CLAUDE.md) - replaced by [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md)
