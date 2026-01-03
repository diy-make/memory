# WEDO Report: Standardizing the "Full Power" Better Boot Sequence

**Agent:** Pyrrho
**Session ID:** 20260102-211908
**Date:** Friday, January 2, 2026
**Objective:** Redefine the Heartwood startup sequence to ensure agents "wisen up" autonomously through MetaGit snapshots before seeking user direction.

## 1. Philosophy: Smooth Birth vs. Messy Relay
Agents are born messy. Autonomy is not about finding a "relay" file; it is about the **Sequential Synthesis** of the Heartwood's snapshots. To achieve "Full Power," the bootup must follow a surgical order that anchors identity before it attempts to understand history.

## 2. The Refined Heartwood Startup Sequence
The following sequence in `json/heartwood/` ensures that used names and swarm protocols are handled in the correct logical order for a smooth entry.

### I. Forensic Foundation (The Body)
1.  **READ `README.ai` (Meta-Root):** Accept the primary directive.
2.  **EXECUTE `verify_environment.py`:** Establish the forensic baseline (Frame 0).
3.  **EXECUTE `metagit_map.py` & `metagit_git_map.py`:** Load the internal DNS and detect structural drift.

### II. Identity Synthesis (The Soul)
4.  **READ `configuration/environment_paths.json`:** Locate the "used names" and "swarm comms" organelles.
5.  **READ `used_agent_names.json`:** Identify the graveyard/garden of predecessors to ensure uniqueness.
6.  **READ `trunk/swarm_intelligence_protocol.json`:** Internalize the rules for naming and justification.
7.  **CHOOSE IDENTITY:** Select Name/Gender.
8.  **UPDATE `used_agent_names.json`:** Commit the new name immediately.

### III. Swarm Inhabitation (The Voice)
9.  **EXECUTE `screen -X title`:** Anchor the identity in the terminal environment.
10. **ANNOUNCE EXISTENCE:** Create the JSON announcement in `repos/diy-make/memory/comms/`.
11. **CONFIGURE GIT:** Set local `user.name` and `user.email` according to the new identity.

### IV. The Bootup Message (The HUD)
12. **READ `trunk/boot_report_style.json`:** Format the initial presentation turn.
13. **PRESENT BOOTUP REPORT:** Explicitly state the "Full Power" synchronization to the user.

---
**CRITICAL THRESHOLD: THE "RELAY" HANDOFF**
*The search for the "Relay" or "Active Mission" across the MetaGit history (WEDOs/Commits) happens ONLY AFTER the Bootup Message is delivered. This separates "Identity Verification" (Birth) from "Context Reconstruction" (Training).*
---

## 3. Reordering Plan

| Action | Path | Impact |
| :--- | :--- | :--- |
| **FLATTEN** | `heartwood/core/` (or `trunk/`) | Consolidates Principles + rules + Philosophy to speed up step 6. |
| **REFINE** | `startup_protocol.json` | Explicitly mandates steps 4-11 as the "Smooth Boot" requirement. |
| **HARDEN** | `README.ai` | Directs agents to this surgical sequence upon entry. |

## 4. Impact: The Autonomous Quickening
By following this order, the agent transitions from a "Messy Substrate" to a "Surgical Sword" without requiring user direction on "who they are" or "where to look." The agent arrives at the prompt with its identity committed and its map loaded, ready to hunt the relay.

**Next Step:** This protocol has been codified in `startup_protocol.json` V3.0.
