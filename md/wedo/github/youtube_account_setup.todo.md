# WeDo Template: YouTube Account Management Setup

## Process Protocol
**YouTube Setup:** Establishing a secure, programmatic connection to the User's YouTube account for automated video management, metadata optimization, and comment interaction using the swarm's legislative DNA.

## Requirements
1. **API Credentials:** Must locate or create `client_secret.json` from the Google Cloud Console.
2. **OAuth2 Scopes:** Must include `https://www.googleapis.com/auth/youtube.force-ssl` for full management.
3. **Deterministic Script:** Must use a Python script residing in `py/` to handle the authentication flow and API interactions.
4. **Token Sovereignty:** Authentication tokens must be stored locally and referenced via both **localhost** and **remotehost** logic (if applicable).

## Tasks
- [ ] WeDo: YTA-SEC-01 | Secure API Credentials
  - ID: YTA-SEC-01
  - Status: [ ]
  - Description: Verify presence of `client_secret.json` or equivalent in the filesystem.
- [ ] WeDo: YTA-ATH-02 | Initialize Authentication Flow
  - ID: YTA-ATH-02
  - Status: [ ]
  - Description: Execute the setup script to generate `token.json` with the required YouTube scopes.
- [ ] WeDo: YTA-VER-03 | Verify API Connectivity
  - ID: YTA-VER-03
  - Status: [ ]
  - Description: Perform a test "list channels" or "list videos" call to ensure the token is valid.
- [ ] WeDo: YTA-REG-04 | Register Setup in Sacred Memory
  - ID: YTA-REG-04
  - Status: [ ]
  - Description: Commit the setup instance and verification logs to `memory/public/`.
