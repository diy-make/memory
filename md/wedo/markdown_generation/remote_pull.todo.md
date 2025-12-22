# WeDo Template: Remote Pull Thread

## Process Protocol
**Remote Pull Integration:** When processing a remote pull request, every "- [ ] WeDo:" task found in the source diff must be explicitly added to the specific instance of this todo file in the temporal directory. Each task must retain its original description and be assigned a unique WeDo ID.

**Active Investigation:** The Agent MUST verify the existence of all referenced artifacts (gifs, links, local files) on the **localhost** before integration. If an artifact is missing, the Agent must notify the User.

**Audit Scrutiny:** Every integrated change and request must be granularly documented in the synthesis report.

## Boilerplate
- [ ] WeDo: [ID] | [Description]
  - ID: [ID]
  - Status: [ ]
  - Description: [Detailed Description]
  - Synthesis Report: Required (Must meet **Audit Scrutiny** standards; see Boilerplate Report Protocol)
  - Location Protocol: Must include both **localhost** and **remotehost** references.
