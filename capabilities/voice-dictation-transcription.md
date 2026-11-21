[Back to the index](../CAPABILITIES.md)

# Voice, dictation and transcription

## Which one to pick: Transcription (speech to text): Mac, Android, Termux, web, Croatian

Mac: dictation is Vox to Txt (MANTRA_VOICE_TO_TEXT, F1 hotkey, language en, hr or auto, port 8865 for files); a YouTube link or file goes through `scribe` (MAC_TRANSCRIBER). Android: TTT is the voice keyboard (English and Croatian engines); MAHA_TRANSCRIBE_ANDROID_2 is the native app, version 1 only the Talk to Type screen; TATA_Talk is a simple Croatian-only app in a private repo. Termux: `transcribe` (MAHA_TRANSCRIBE_TERMUX_TERMINAL) serves the page. Web and servers: the Streamlit and Flask Maha Transcribe pages (Whisper on Groq, language hint hr), 111/222 Transcribe (AssemblyAI with speakers and subtitles) and the hosted TTT Portal API. MARKO_TRANSCRIBE, MAHA_TRANSCRIBE_TERMUX and the web-view MAHA_TRANSCRIBE_ANDROID are superseded.

| You want | Use | How |
|---|---|---|
| dictate into any Mac app with a hotkey, Croatian or English | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](../apps/MANTRA_VOICE_TO_TEXT.md) |  |
| transcribe a WAV on the Mac through a local call | [Vox to Txt (Mantra) (MANTRA_VOICE_TO_TEXT)](../apps/MANTRA_VOICE_TO_TEXT.md) | `curl -s -XPOST '127.0.0.1:8865/hear?lang=hr' --data-binary @take.wav` |
| transcribe a YouTube video or audio file with Groq, AssemblyAI or Deepgram | [Mac Transcriber (scribe) (MAC_TRANSCRIBER)](../apps/MAC_TRANSCRIBER.md) | `scribe https://www.youtube.com/watch?v=<id> --engine groq --out ~/transcripts` |
| dictate Croatian on an Android phone (keyboard) | [TTT Voice Type keyboard (TTT)](../apps/TTT.md) |  |
| record and transcribe on Android in a native app (talk to type screen) | [Maha Transcribe Android (native) (MAHA_TRANSCRIBE_ANDROID_2)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) |  |
| simple one-button Croatian speech to text on Android | [TA-TA Talk (Croatian dictation) (TATA_Talk)](../apps/TATA_Talk.md) |  |
| transcribe on the phone in Termux, or on Mac/Linux, from one command | [Maha Transcribe (Termux/terminal) (MAHA_TRANSCRIBE_TERMUX_TERMINAL)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) | `transcribe 9000` |
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

- transcribe a long interview with speakers -> [111 Transcribe](../apps/111-transcribe.md) (Web/Cloud; API: none)
- make subtitles from a video -> [111 Transcribe](../apps/111-transcribe.md) (Web/Cloud; API: none)
- upload a file and get text -> [111 Transcribe](../apps/111-transcribe.md) (Web/Cloud; API: none)
- translate a transcript -> [111 Transcribe](../apps/111-transcribe.md) (Web/Cloud; API: none)
- transcribe this interview with speakers -> [222 Transcribe](../apps/222-transcribe.md) (Web/Cloud; API: none)
- get subtitles for a video file -> [222 Transcribe](../apps/222-transcribe.md) (Web/Cloud; API: none)
- transcribe a recording from my phone -> [222 Transcribe](../apps/222-transcribe.md) (Web/Cloud; API: none)
- make a transcript from a shared link -> [222 Transcribe](../apps/222-transcribe.md) (Web/Cloud; API: none)
- read this text aloud with highlighted words -> [EdgeReader (MA Reader Streamlit)](../apps/mareader.md) (Web/Cloud; API: none)
- Croatian text to speech reader -> [EdgeReader (MA Reader Streamlit)](../apps/mareader.md) (Web/Cloud; API: none)
- translate my speech between Croatian, English and German -> [EdgeReader (MA Reader Streamlit)](../apps/mareader.md) (Web/Cloud; API: none)
- make per-sentence mp3 files from a text -> [EdgeReader (MA Reader Streamlit)](../apps/mareader.md) (Web/Cloud; API: none)
- read text aloud with Gemini voices -> [Google TTS and STT (gtt)](../apps/GOOGLE_TTS_STT.md) (macOS/Android/Termux/Web; API: door 7311) - call: `curl -s -XPOST 127.0.0.1:7311/api/speak -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs`
- transcribe audio with Gemini -> [Google TTS and STT (gtt)](../apps/GOOGLE_TTS_STT.md) (macOS/Android/Termux/Web; API: door 7311)
- manage my Gemini free keys -> [Google TTS and STT (gtt)](../apps/GOOGLE_TTS_STT.md) (macOS/Android/Termux/Web; API: door 7311)
- text to speech on the phone -> [Google TTS and STT (gtt)](../apps/GOOGLE_TTS_STT.md) (macOS/Android/Termux/Web; API: door 7311)
- text to speech with a Google voice -> [GVoices (Google Voices)](../apps/GoogleVoices.md) (macOS/Android/Termux/Linux/Web; API: http 8300) - call: `curl -s -XPOST 127.0.0.1:8300/api/say -H 'Content-Type: application/json' -d '{"text":"Dobar dan"}' # body field names beyond text are not in the docs`
- make a WAV of a sentence with Gemini -> [GVoices (Google Voices)](../apps/GoogleVoices.md) (macOS/Android/Termux/Linux/Web; API: http 8300)
- gvoice command -> [GVoices (Google Voices)](../apps/GoogleVoices.md) (macOS/Android/Termux/Linux/Web; API: http 8300)
- pick a Gemini voice -> [GVoices (Google Voices)](../apps/GoogleVoices.md) (macOS/Android/Termux/Linux/Web; API: http 8300)
- text to speech with word timing in Kotlin -> [MA Reader Engine](../apps/MA_READER_ENGINE.md) (Android; API: none)
- reuse the Edge voice client -> [MA Reader Engine](../apps/MA_READER_ENGINE.md) (Android; API: none)
- highlight the spoken word -> [MA Reader Engine](../apps/MA_READER_ENGINE.md) (Android; API: none)
- engine for a native Android reader (MA Reader Android, LLL in TTT) -> [MA Reader Engine](../apps/MA_READER_ENGINE.md) (Android; API: none)
- MA Reader on the phone (native app, text only for now) -> [MA Reader for Android](../apps/MA_READER_ANDROID.md) (Android; API: http) - call: `curl -s http://127.0.0.1:<port>/api/voices # lists English and Croatian voices; the app does NOT speak yet`
- paste text and keep a reading library on Android -> [MA Reader for Android](../apps/MA_READER_ANDROID.md) (Android; API: http)
- use many Speechify keys with rotation -> [MA Reader Speechify module](../apps/MA_READER_SPEECHIFY.md) (Android/Termux/Web; API: http 8081) - call: `curl http://localhost:8081/api/voices`
- read text aloud in Croatian or English on the phone -> [MA Reader Speechify module](../apps/MA_READER_SPEECHIFY.md) (Android/Termux/Web; API: http 8081)
- wire Speechify into another app -> [MA Reader Speechify module](../apps/MA_READER_SPEECHIFY.md) (Android/Termux/Web; API: http 8081)
- read text aloud on the phone or Mac with the word lit -> [MA Reader Termux / macOS (Edge / Speechify)](../apps/MA_READER_TERMUX_MACOS.md) (macOS/Android/Termux; API: http 8081) - call: `curl -s -X POST http://127.0.0.1:8081/api/say -H 'Content-Type: application/json' -d '{"text":"hello","lang":"en"}' -o out.mp3`
- text to speech reader with word highlighting -> [MA Reader Termux / macOS (Edge / Speechify)](../apps/MA_READER_TERMUX_MACOS.md) (macOS/Android/Termux; API: http 8081)
- read aloud with highlighting on Android (in Termux, in Chrome) -> [MA Reader Termux / macOS (Edge / Speechify)](../apps/MA_READER_TERMUX_MACOS.md) (macOS/Android/Termux; API: http 8081)
- install the MA Reader -> [MA Reader Termux / macOS (Edge / Speechify)](../apps/MA_READER_TERMUX_MACOS.md) (macOS/Android/Termux; API: http 8081)
- transcribe a YouTube video to text -> [Mac Transcriber (scribe)](../apps/MAC_TRANSCRIBER.md) (macOS; API: cli) - call: `scribe <youtube-url> --engine groq --out ~/transcripts`
- transcribe a long audio file with timestamps -> [Mac Transcriber (scribe)](../apps/MAC_TRANSCRIBER.md) (macOS; API: cli)
- check which transcription keys work -> [Mac Transcriber (scribe)](../apps/MAC_TRANSCRIBER.md) (macOS; API: cli)
- read aloud the text under my cursor on the Mac -> [Magic Coin](../apps/magic-coin.md) (macOS; API: none)
- floating dictation button on screen -> [Magic Coin](../apps/magic-coin.md) (macOS; API: none)
- speech to text widget for macOS -> [Magic Coin](../apps/magic-coin.md) (macOS; API: none)
- use Maha Transcribe from the terminal -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420) - call: `transcribe 9000 # starts the page on port 9000 (default 8420, next free port if taken) and opens it in Chrome`
- start the dictation page locally -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420)
- microphone page on Termux -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420)
- optimise audio before upload -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420)
- transcribe voice on the phone in Termux -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420)
- run a local transcription server on Android -> [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md) (macOS/Android/Termux/Linux; API: http 8420)
- transcribe my voice in the browser -> [Maha Transcribe / TTT-LLL (Streamlit)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md) (Web/Cloud; API: http 8810) - call: `Open the Streamlit page, record in the browser, choose language en or hr, press transcribe # no HTTP call: only GET /healthz exists`
- dictate in Croatian or English -> [Maha Transcribe / TTT-LLL (Streamlit)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md) (Web/Cloud; API: http 8810)
- read text aloud and show it -> [Maha Transcribe / TTT-LLL (Streamlit)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md) (Web/Cloud; API: http 8810)
- speech to text with Groq Whisper -> [Maha Transcribe / TTT-LLL (Streamlit)](../apps/MAHA_TRANSCRIBE_STREAMLIT.md) (Web/Cloud; API: http 8810)
- native Android dictation app -> [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) (Android; API: none)
- speech to text on Android with big buttons -> [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) (Android; API: none)
- record and transcribe on the phone -> [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) (Android; API: none)
- dictate on Android (v1: the T screen only) -> [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md) (Android; API: none)
- dictate and get text in Croatian -> [Maha Transcribe Flask](../apps/MAHA_TRANSCRIBE_FLASK.md) (Linux/Web/Cloud; API: http 8700) - call: `curl -s -XPOST <base>/flask/api/recordings/<id>/transcribe -H 'Content-Type: application/json' -d '{"language":"hr"}'`
- read my text aloud with highlighted words -> [Maha Transcribe Flask](../apps/MAHA_TRANSCRIBE_FLASK.md) (Linux/Web/Cloud; API: http 8700)
- keep transcripts as notes -> [Maha Transcribe Flask](../apps/MAHA_TRANSCRIBE_FLASK.md) (Linux/Web/Cloud; API: http 8700)
- dictate by voice into text in the browser -> [Maha Transcribe VM (TTT-LLL)](../apps/MAHA_TRANSCRIBE_VM.md) (Linux/Web/Cloud; API: http 8810) - call: `Open the page, record in the browser, press transcribe # no HTTP call: only GET /healthz exists`
- read text aloud in a chosen voice -> [Maha Transcribe VM (TTT-LLL)](../apps/MAHA_TRANSCRIBE_VM.md) (Linux/Web/Cloud; API: http 8810)
- transcribe Croatian speech -> [Maha Transcribe VM (TTT-LLL)](../apps/MAHA_TRANSCRIBE_VM.md) (Linux/Web/Cloud; API: http 8810)
- transcribe my voice in the browser -> [Maha Transcriber and Reader (web)](../apps/maha-transcriber-reader.md) (Web; API: none)
- read text aloud with highlighted words -> [Maha Transcriber and Reader (web)](../apps/maha-transcriber-reader.md) (Web; API: none)
- Croatian text to speech -> [Maha Transcriber and Reader (web)](../apps/maha-transcriber-reader.md) (Web; API: none)
- test my speech API keys -> [Maha Transcriber and Reader (web)](../apps/maha-transcriber-reader.md) (Web; API: none)
- fix repeated dictation mistakes -> [Mantra Corrections](../apps/MANTRA_CORRECTIONS.md) (macOS/Android; API: none)
- share dictation corrections between Mac and phone -> [Mantra Corrections](../apps/MANTRA_CORRECTIONS.md) (macOS/Android; API: none)
- transcribe this audio file locally -> [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md) (macOS; API: http 8837) - call: `curl -s -XPOST 127.0.0.1:8837/speak -H 'Content-Type: application/json' -d '{"text":"The render is done.","wait":true}'`
- make the computer say this sentence -> [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md) (macOS; API: http 8837)
- clone a voice from a recording -> [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md) (macOS; API: http 8837)
- read a page aloud with the word highlighted -> [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md) (macOS; API: http 8837)
- speak a status message when a job is done -> [Mantra Voice (speech server)](../apps/MANTRA_VOICE.md) (macOS; API: http 8837)
- download Mantra Voice to Text -> [Mantra Voice to Text (downloads)](../apps/mantra-voice-to-text-downloads.md) (macOS/Windows/Web; API: none)
- free offline dictation for Mac or Windows -> [Mantra Voice to Text (downloads)](../apps/mantra-voice-to-text-downloads.md) (macOS/Windows/Web; API: none)
- press F1 and dictate anywhere -> [Mantra Voice to Text (downloads)](../apps/mantra-voice-to-text-downloads.md) (macOS/Windows/Web; API: none)
- transcribe a long audio file online -> [Marko Transcribe (Streamlit)](../apps/marko-transcribe.md) (Web/Cloud; API: none)
- web transcription app with AssemblyAI -> [Marko Transcribe (Streamlit)](../apps/marko-transcribe.md) (Web/Cloud; API: none)
- record phrases on the phone and re-voice them -> [Sample Player, Android](../apps/SAMPLE_PLAYER.md) (Android; API: none)
- sample player with my own voice cells -> [Sample Player, Android](../apps/SAMPLE_PLAYER.md) (Android; API: none)
- record a phrase over any app with a floating button -> [Sample Player, Android](../apps/SAMPLE_PLAYER.md) (Android; API: none)
- sample player on the Mac -> [Sample Player, macOS](../apps/SAMPLE_PLAYER_MACOS.md) (macOS/Web; API: http) - call: `curl -s -XPOST 127.0.0.1:$(cat ~/.sampleplayer-web/port.txt)/api/record/<slot> # records into a cell; slot names are in GET /api/state`
- record phrases and swap the voice -> [Sample Player, macOS](../apps/SAMPLE_PLAYER_MACOS.md) (macOS/Web; API: http)
- clone a voice with consent -> [Sample Player, macOS](../apps/SAMPLE_PLAYER_MACOS.md) (macOS/Web; API: http)
- web sample sequencer from the terminal -> [Sample Player, macOS](../apps/SAMPLE_PLAYER_MACOS.md) (macOS/Web; API: http)
- dictate Croatian text on a phone -> [TA-TA Talk (Croatian dictation)](../apps/TATA_Talk.md) (Android; API: none)
- simple one-button voice to text -> [TA-TA Talk (Croatian dictation)](../apps/TATA_Talk.md) (Android; API: none)
- talk to Claude with my voice -> [Talk Mode (Mantra)](../apps/TALK_MODE.md) (macOS; API: cli) - call: `# no call: read state.json of the app (folder not given in the docs); Queen answers 'talk mode status'`
- dictate to a terminal session and hear the reply -> [Talk Mode (Mantra)](../apps/TALK_MODE.md) (macOS; API: cli)
- hands-free conversation with Claude Code -> [Talk Mode (Mantra)](../apps/TALK_MODE.md) (macOS; API: cli)
- which session am I talking to -> [Talk Mode (Mantra)](../apps/TALK_MODE.md) (macOS; API: cli)
- talk to Claude Code by voice -> [Talk with Claude Code](../apps/TALK_WITH_CLAUDE.md) (macOS; API: http 8835) - call: `python3 ~/Developer/TALK_WITH_CLAUDE/talk.py reply "..."`
- speak with the computer and hear the answer -> [Talk with Claude Code](../apps/TALK_WITH_CLAUDE.md) (macOS; API: http 8835)
- apply my TTT keyboard layout -> [TTT Layouts](../apps/ttt-layouts.md) (Android; API: none)
- restore the TTT keys and colours on a new phone -> [TTT Layouts](../apps/ttt-layouts.md) (Android; API: none)
- dictate on the phone into any app -> [TTT Voice Type keyboard](../apps/TTT.md) (Android; API: adb) - call: `python3 tools/ttt_remote.py say "The render is done" # speaks through TTT; type into the focused field with the type verb`
- voice keyboard for Android -> [TTT Voice Type keyboard](../apps/TTT.md) (Android; API: adb)
- reply to a message with AI by voice -> [TTT Voice Type keyboard](../apps/TTT.md) (Android; API: adb)
- compare transcription engines on the phone -> [TTT Voice Type keyboard](../apps/TTT.md) (Android; API: adb)
- make the phone speak via TTT -> [TTT Voice Type keyboard](../apps/TTT.md) (Android; API: adb)
- dictate on my Android phone -> [TTT&LLL (Talk to Type, Look Listen Learn)](../apps/DictateKeyboard.md) (Android; API: none)
- voice typing keyboard with my own keys -> [TTT&LLL (Talk to Type, Look Listen Learn)](../apps/DictateKeyboard.md) (Android; API: none)
- offline Whisper keyboard -> [TTT&LLL (Talk to Type, Look Listen Learn)](../apps/DictateKeyboard.md) (Android; API: none)
- talk to type on Android -> [TTT&LLL (Talk to Type, Look Listen Learn)](../apps/DictateKeyboard.md) (Android; API: none)
- clone a new voice -> [Voice Cloning (Mantra)](../apps/VOICE_CLONING.md) (macOS; API: accessibility) - call: `star press "voice cloning" "top"`
- change which voice the computer uses -> [Voice Cloning (Mantra)](../apps/VOICE_CLONING.md) (macOS; API: accessibility)
- mute all Claude voices -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837) - call: `voiceengine off (writes ~/.mantra/voice_engine_state and stops the current reading)`
- global voice on and off switch -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- subtitle while Claude speaks -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- replay what Claude just said -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- pause the voice reading -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- turn the computer voice off -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- switch the voice engine on -> [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md) (macOS; API: http 8837)
- shared subtitle pause logic -> [Voice Engine Universal (Mantra)](../apps/VOICE_ENGINE_UNIVERSAL.md) (macOS/Android; API: none)
- word-exact pause for a speaking server -> [Voice Engine Universal (Mantra)](../apps/VOICE_ENGINE_UNIVERSAL.md) (macOS/Android; API: none)
- spec for subtitle following the voice -> [Voice Engine Universal (Mantra)](../apps/VOICE_ENGINE_UNIVERSAL.md) (macOS/Android; API: none)
- download a speech model -> [Voice Engines (model hub)](../apps/VOICE_ENGINES.md) (macOS; API: cli) - call: `voice-engines fetch qwen06 # downloads the model 'qwen06' into the shared hub`
- see which voice engines are installed -> [Voice Engines (model hub)](../apps/VOICE_ENGINES.md) (macOS; API: cli)
- move the models folder -> [Voice Engines (model hub)](../apps/VOICE_ENGINES.md) (macOS; API: cli)
- dictate into any Mac app with a hotkey -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865) - call: `curl -s -XPOST '127.0.0.1:8865/hear?lang=en' --data-binary @take.wav`
- transcribe an audio file -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865)
- speech to text in Croatian and English -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865)
- get text from a WAV through a local call -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865)
- dictate text anywhere on the Mac -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865)
- clean up dictated text -> [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md) (macOS/Windows; API: http 8865)
- transcribe a whole YouTube channel -> [YT Transcriber](../apps/YT_TRANSCRIBER.md) (macOS/Linux/Cloud; API: http 8851) - call: `./download_channel.sh https://www.youtube.com/@channel mychannel --limit 20 # downloads audio of the last 20 videos of a channel`
- get all transcripts of a playlist -> [YT Transcriber](../apps/YT_TRANSCRIBER.md) (macOS/Linux/Cloud; API: http 8851)
- summarise a channel into topics -> [YT Transcriber](../apps/YT_TRANSCRIBER.md) (macOS/Linux/Cloud; API: http 8851)

## Retired - do not use

- [Maha Transcribe Android v3 (web view, superseded) (retired)](../apps/MAHA_TRANSCRIBE_ANDROID.md) - replaced by [Maha Transcribe Android (native)](../apps/MAHA_TRANSCRIBE_ANDROID_2.md)
- [Maha Transcribe Termux v1 (superseded) (retired)](../apps/MAHA_TRANSCRIBE_TERMUX.md) - replaced by [Maha Transcribe (Termux/terminal)](../apps/MAHA_TRANSCRIBE_TERMUX_TERMINAL.md)
- [Transcribe Voice to Text RT (Mantra), retired (retired)](../apps/MARKO_TRANSCRIBE.md) - replaced by [Vox to Txt (Mantra)](../apps/MANTRA_VOICE_TO_TEXT.md)
- [Voice of Claude (Mantra), retired (retired)](../apps/VOICE_OF_CLAUDE.md) - replaced by [Voice Engine (Mantra)](../apps/VOICE_ENGINE.md)
