[Back to the index](../CAPABILITIES.md)

# Keys, secrets and infrastructure

- test an API key on the phone -> [Key Tester (Android)](../apps/Key_Tester.md) (Android; API: none)
- check which provider a key belongs to -> [Key Tester (Android)](../apps/Key_Tester.md) (Android; API: none)
- get an API key for a provider in a script -> [Keyring](../apps/KEYRING_TERMUX.md) (Android/Termux; API: door 8842) - call: `keyring get groq # prints one working key value for the provider on stdout; use as $(keyring get groq)`
- check which of my API keys still work and have credit -> [Keyring](../apps/KEYRING_TERMUX.md) (Android/Termux; API: door 8842)
- collect all API keys from my notes into one place -> [Keyring](../apps/KEYRING_TERMUX.md) (Android/Termux; API: door 8842)
- export my keys in one standard file -> [Keyring](../apps/KEYRING_TERMUX.md) (Android/Termux; API: door 8842)
- test which of my API keys still work -> [KeyringTester (Mantra)](../apps/KEY_RING_TESTER.md) (macOS; API: cli) - call: `"/Applications/KeyringTester (Mantra).app/Contents/MacOS/KeyringTester" --test ~/keys.txt # tests every key of the file; never prints a key`
- check if a Google key can use Maps or Gemini -> [KeyringTester (Mantra)](../apps/KEY_RING_TESTER.md) (macOS; API: cli)
- find dead or out-of-credit keys -> [KeyringTester (Mantra)](../apps/KEY_RING_TESTER.md) (macOS; API: cli)
- where does the cloud transcription service run -> [Oracle machine notes](../apps/oracle_machine.md) (Linux/Cloud; API: http) - call: `curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe # same API as TTT_PORTAL`
- how do I reach the Oracle machine -> [Oracle machine notes](../apps/oracle_machine.md) (Linux/Cloud; API: http)
- what ports and routes does the cloud machine serve -> [Oracle machine notes](../apps/oracle_machine.md) (Linux/Cloud; API: http)
- merge API keys into a secrets.toml on the phone -> [TOML key merger](../apps/TOML.md) (Android/Termux; API: http 8099) - call: `curl -s http://127.0.0.1:8099/api/ls # started on the phone by toml-termux.sh; the page opens in the phone browser`
- format keys as TOML without pasting them -> [TOML key merger](../apps/TOML.md) (Android/Termux; API: http 8099)
- Streamlit secrets from an exported key file -> [TOML key merger](../apps/TOML.md) (Android/Termux; API: http 8099)
- give other apps an API for transcription and speech -> [TTT Portal](../apps/TTT_PORTAL.md) (Linux/Web/Cloud; API: http) - call: `curl -s -H "Authorization: Bearer <api-key>" -F file=@clip.wav -F language=hr <portal-url>/api/v1/transcribe`
- add or remove a portal user -> [TTT Portal](../apps/TTT_PORTAL.md) (Linux/Web/Cloud; API: http)
- put a login in front of an app -> [TTT Portal](../apps/TTT_PORTAL.md) (Linux/Web/Cloud; API: http)
