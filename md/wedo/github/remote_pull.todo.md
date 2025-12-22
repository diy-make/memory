# WeDo Template: Remote Pull Thread

## Process Protocol
**Conscious Duality:** The WeDo is a shared thread of attention between the User (Conscious Intent) and the Agent (Machine Execution). Completion often requires a specific sequence of actions across the human-machine boundary.

**Remote Pull Integration:** When processing a remote pull request, every "- [ ] WeDo:" task found in the source diff must be explicitly added to the specific instance of this todo file. 

**Active Investigation:** The Agent MUST verify all referenced artifacts on the **localhost**. If a task requires a remote action beyond the Agent's capability (e.g., a manual push/pull or external site verification), the Agent must explicitly flag this as a **USER_REQUIRED** sub-task.

## Boilerplate
- [ ] WeDo: [ID] | [Description]
  - ID: [ID]
  - Status: [ ]
  - Description: [Detailed Description]
  - Dependency: [e.g., USER_REQUIRED: Remote Push]
  - Synthesis Report: Required (Must meet **Audit Scrutiny** standards)
