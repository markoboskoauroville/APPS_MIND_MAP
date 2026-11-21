[Back to the index](../CAPABILITIES.md)

# Keys, secrets and infrastructure

### [Key Tester (Android)](../apps/Key_Tester.md)

Android; API: none

- test an API key on the phone (Key Tester)
- check which provider a key belongs to (Key Tester)

### [Keyring](../apps/KEYRING_TERMUX.md)

Android/Termux; API: door 8842. Main call: `keyring get groq # prints one working key value for the provider on stdout; use as $(keyring get groq)`

Before: Run on the phone in Termux (loopback only; vault in ~/.keyring, mode 0600); HTTP page on 8842, up to 8857. Only `/api/keys/<id>/reveal` returns a value.

- get an API key for a provider in a script (Keyring)
- check which of my API keys still work and have credit (Keyring)
- collect all API keys from my notes into one place (Keyring)
- export my keys in one standard file (Keyring)

### [KeyringTester (Mantra)](../apps/KEY_RING_TESTER.md)

macOS; API: cli. Main call: `"/Applications/KeyringTester (Mantra).app/Contents/MacOS/KeyringTester" --test ~/keys.txt # tests every key of the file; never prints a key`

- test which of my API keys still work (KeyringTester)
- check if a Google key can use Maps or Gemini (KeyringTester)
- find dead or out-of-credit keys (KeyringTester)

### [Oracle machine notes](../apps/oracle_machine.md)

Linux/Cloud; API: http. Main call: `curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe # same API as TTT_PORTAL`

Before: This repo is documentation of the machine; the service code is elsewhere (see TTT_PORTAL). `<portal-url>` and keys are the owner's.

- where does the cloud transcription service run (Oracle machine notes)
- how do I reach the Oracle machine (Oracle machine notes)
- what ports and routes does the cloud machine serve (Oracle machine notes)

### [TOML key merger](../apps/TOML.md)

Android/Termux; API: http 8099. Main call: `curl -s http://127.0.0.1:8099/api/ls # started on the phone by toml-termux.sh; the page opens in the phone browser`

- merge API keys into a secrets.toml on the phone (TOML key merger) - call: `curl -s -XPOST http://127.0.0.1:8099/api/merge`
- format keys as TOML without pasting them (TOML key merger)
- Streamlit secrets from an exported key file (TOML key merger)

### [TTT Portal](../apps/TTT_PORTAL.md)

Linux/Web/Cloud; API: http. Main call: `curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe`

Before: An account and API key from the portal admin (the key is issued per user, never stored in git); the portal-url is a hosted address kept out of this map.

- give other apps an API for transcription and speech (TTT Portal)
- add or remove a portal user (TTT Portal)
- put a login in front of an app (TTT Portal)

