# WeDo Template: Remote Pull Thread

## Process Protocol
**Remote Pull Integration:** When processing a remote pull request, every "- [ ] WeDo:" task found in the source diff must be explicitly added to the specific instance of this todo file in the temporal directory. Each task must retain its original description and be assigned a unique WeDo ID.

## Boilerplate
- [ ] WeDo: [ID] | [Description]
  - ID: [ID]
  - Status: [ ]
  - Description: [Detailed Description]
  - Synthesis Report: Required (Must meet **Audit Scrutiny** standards; see Boilerplate Report Protocol)
  - Location Protocol: Must include both **localhost** and **remotehost** references.
