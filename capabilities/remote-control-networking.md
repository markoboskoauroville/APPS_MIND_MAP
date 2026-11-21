[Back to the index](../CAPABILITIES.md)

# Remote control and networking

### [aooserver-arm64](../apps/aooserver-arm64.md)

Linux/Cloud; API: cli. Main call: `aooserver -p 10998`

Before: Listens on UDP/TCP port 10998 by default; -l sets the log folder and -b a blocklist file.

- SonoBus server on the cloud machine (aooserver-arm64)
- audio link between the VM and my Mac with SonoBus (aooserver-arm64)
- arm64 aooserver binary (aooserver-arm64)

### [Chromium Virtual Machine (Mantra)](../apps/vm-chromium.md)

macOS/Linux/Cloud; API: door 8890. Main call: `cvm ask "Summarise the open tab in one sentence" # Mac command: asks claude.ai in the VM browser, answers as text in about 7 s`

Before: Run on the Mac (cvm is installed from mac/cvm into ~/.local/bin). The vm-agent on the VM listens on port 8890 and needs header X-Mantra-Token over Tailscale; cvm sends it. The 8890 here is on the VM, not the Mac session hub.

- use Chrome in the cloud from my Mac (Chromium Virtual Machine)
- ask Claude or Gemini in a browser tab from a script (Chromium Virtual Machine)
- clipboard between Mac and the VM (Chromium Virtual Machine)
- generate images in Gemini in batch (Chromium Virtual Machine)
- view and control another Mac or phone by VNC (Chromium Virtual Machine)

### [Connection Controller Dashboard Viewer (Mantra)](../apps/CONNECTION_CONTROLLER_DASHBOARD_VIEWER.md)

macOS; API: cli. Main call: `"/Applications/Connection Controller Dashboard Viewer (Mantra).app/Contents/MacOS/ConnectionController" --probe-json`

- check which network connection has internet (Connection Controller Dashboard Viewer)
- turn off a network interface I do not want (Connection Controller Dashboard Viewer)
- see all Mac network interfaces (Connection Controller Dashboard Viewer)

### [Connection Keeper](../apps/connection-keeper.md)

macOS/Cloud; API: http 8857. Main call: `ck-bondcheck --json # health of the bonded connection; the aggregate server on 127.0.0.1:8857 answers GET /status`

- my internet keeps dropping, keep the connection alive (Connection Keeper)
- combine phone hotspot and cable for more speed (Connection Keeper)
- switch the Mac to the phone's connection (Connection Keeper)
- test my internet speed on each line (Connection Keeper)
- check that bonding works (Connection Keeper)

### [LAN Scanner (Mantra)](../apps/LAN_SCANNER.md)

macOS; API: cli. Main call: `lanscan --json # every device on the LAN as JSON`

Before: The lanscan wrapper (in ~/.local/bin) runs the LAN Scanner (Mantra) app binary; install the app from the GitHub release first.

- which devices are on my network (LAN Scanner) - call: `lanscan --iface en0 --json`
- scan the LAN (LAN Scanner)
- find the IP of a device on the Wi-Fi (LAN Scanner)
- list network devices with maker names (LAN Scanner)

### [Mantra Ports](../apps/MANTRA_PORTS.md)

macOS; API: cli. Main call: `mantra-ports next`

Before: Install once with sh ~/Developer/MANTRA_PORTS/install.sh (copies ports.py, ports.lua, Ports.swift and the mantra-ports command into ~/.local/lib/mantra). The registry file is ~/.config/mantra-ports.json.

- which port is this app on (Mantra Ports) - call: `import sys, os; sys.path.insert(0, os.path.expanduser('~/.local/lib/mantra')); import ports; PORT = ports.claim('my-app', 8962) # id = app name, lower case, hyphens; returns the wanted port if free, else the next free one`
- avoid two apps using the same port (Mantra Ports)
- give a new local server a free port (Mantra Ports)
- find the URL of the voice server (Mantra Ports)
- check for port clashes on the Mac (Mantra Ports) - call: `mantra-ports book my-app 8962 ; mantra-ports check ; mantra-ports scan`

### [Mantra Remote Viewing (Mantra Remote)](../apps/MANTRA_REMOTE_VIEWING.md)

Android/Cloud; API: door 8841. Main call: `rvctl pixel tap 540 1200 --label "NDI" --watched --expect com.mantraproductions.manualcamera`

Before: Mac side through adb forward tcp:8790 tcp:8790. Since v63 rvctl refuses every action without --watched (ask the owner: are you watching?) and without --expect ‹package in front›, and it reads GET /foreground before acting. The Accessibility service 'Mantra Remote Viewing - Claude Control' must be switched on by hand once on the phone.

- control my phone from Claude (Mantra Remote Viewing)
- see the Mac screen on the phone (Mantra Remote Viewing)
- tap or swipe on the Android phone remotely (Mantra Remote Viewing) - call: `rvctl pixel text "hello" --watched --expect com.android.chrome ; rvctl pixel key BACK --watched --expect com.android.chrome`
- share the phone screen to a laptop (Mantra Remote Viewing)
- run a macro on the phone (Mantra Remote Viewing) - call: `mremote run pixel 'Press "CHROMIUM-VM"' # HTTP form: POST /api/run; GET /api/shot?w=360 gives one small picture`

### [Router Credits (Android)](../apps/router-credits.md)

Android; API: none

- how much data is left on the router SIM (Router Credits)
- check mobile data balance from the phone (Router Credits)
- read the router's SMS inbox (Router Credits)

### [Router Mode (Mantra)](../apps/router-mode.md)

macOS/Cloud; API: cli. Main call: `routermode status`

Before: Mantra Router mode helper (router and phone tethering).

- is my internet coming from the phone or the SIM (Router Mode)
- switch the router to SIM only (Router Mode)
- warn me when the router fell back to the SIM (Router Mode)

### [Router SMS](../apps/router-sms.md)

macOS; API: http 8880. Main call: `router-sms send <number> "text" # sends an SMS through the router SIM`

Before: Holds the router login; runs on 8880 (next free port if taken, written to ~/.mantra/ports/router-sms).

- how much mobile data is left on the router SIM (Router SMS) - call: `router-sms balance --json`
- send an SMS through the router (Router SMS)
- read SMS received by the router (Router SMS) - call: `router-sms last`
- switch the router Wi-Fi off (Router SMS)

### [Screen Copy (Mantra)](../apps/MANTRA_SCREEN_COPY.md)

macOS/Android; API: http 8883. Main call: `curl -s -XPOST 127.0.0.1:8883/record/start # records the selected phone tab; CLI: screencopy record start --serial emulator-5556 --name "01 Title"`

Before: Screen Copy (Mantra) must be running (port 8883, up to 8898; the chosen port is in ~/.mantra/ports/screen-copy) and the phone connected by adb (Wi-Fi adb needs the Local Network permission).

- see my Android phone on the Mac (Screen Copy)
- record the phone screen to a file (Screen Copy)
- tap or type on the phone from the Mac by script (Screen Copy)
- mirror several phones at once (Screen Copy)

### [Second Take Remote](../apps/SECOND_TAKE_REMOTE.md)

Android; API: http 8965. Main call: `curl -s -XPOST http://<guide-address>:8966/record -H 'X-Remote-Id: phone1' # the phone starts a take on the Mac guide`

Before: This repo is the Android CLIENT; the guide is MPA_LESSONS_ANALYZER (listener 8966, private networks and Tailscale only, first come first served by X-Remote-Id; 423 when another remote holds it). The number 8965 in older records is the guide's local port, which MANTRA_ROOM also uses.

- phone remote for filming lessons (Second Take Remote)
- control the recording from my phone (Second Take Remote)
- shot list remote for the Mac guide (Second Take Remote)

### [Star API (Mantra)](../apps/STAR_API.md)

macOS; API: http 8863. Main call: `curl -s -XPOST 127.0.0.1:8863/apps/timer/press -H "Content-Type: application/json" -d '{"label":"stopwatch"}' # same as: star press "timer" "stopwatch"`

Before: From another machine (phone, cloud session) add header X-Mantra-Token with the token in ~/.config/mantra-door.token; on 127.0.0.1 no token is needed. The server is started with: star serve (runs in the background once Star API (Mantra) is on).

- press a button in one of my Mac apps remotely (Star API)
- start an app from my phone (Star API)
- call a function of an app by name (Star API) - call: `star fn "sound recorder" record.suno '{"out":"~/x.wav","url":"https://suno.com/song/..."}'`
- list all my apps (Star API)

### [Stream Deck Remote](../apps/STREAM_DECK_REMOTE.md)

macOS/Android; API: http 8963. Main call: `curl 'http://127.0.0.1:8963/press?profile=obs&key=0'`

Before: Mac app (port 8963, MANTRA_PORTS id streamdeck-remote); the phone shows Stream Deck pages.

- use my phone as a Stream Deck (Stream Deck Remote)
- switch OBS scenes from the phone (Stream Deck Remote)
- remote for the MPA classroom (Stream Deck Remote)
- press deck keys from Android (Stream Deck Remote)
- use a Stream Deck as an application switcher (Stream Deck Remote)
- drive a Stream Deck without the Elgato app (Stream Deck Remote)

### [vm-android (Pixel 7 in Oracle Cloud)](../apps/vm-android.md)

macOS/Linux/Cloud; API: http 8897. Main call: `pixel7 test app.apk # Mac command: installs, launches, screenshots the APK on the cloud Pixel 7`

Before: Run on the Mac, where the pixel7 command is installed (mac/pixel7 into ~/.local/bin). The door pixel7d answers only on the VM's Tailscale address with header X-Mantra-Token (not on 127.0.0.1 of the Mac), so a session needs Tailscale to reach it.

- test an Android APK in the cloud (vm-android)
- take a screenshot of the Android VM (vm-android) - call: `pixel7 shot`
- tap and type on the cloud Pixel 7 (vm-android) - call: `pixel7 tap 540 1200`
- run an Android test without a phone (vm-android)
- send multichannel audio between machines (vm-android)

### [VPN (Mantra)](../apps/MANTRA_VPN.md)

macOS/Android; API: none

- route my traffic through Frankfurt (VPN)
- turn VPN on or off (VPN)
- change my public IP to Germany (VPN)
- simple Tailscale exit-node switch (VPN)

