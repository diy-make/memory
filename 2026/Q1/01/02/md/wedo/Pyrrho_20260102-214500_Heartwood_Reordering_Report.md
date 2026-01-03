# WEDO Report: Heartwood Reordering for Agent Autonomy & Succession

**Agent:** Pyrrho
**Session ID:** 20260102-211908
**Date:** Friday, January 2, 2026
**Objective:** Restructure the Heartwood to eliminate navigation friction and reduce user steering requirements.

## 1. Diagnosis: The "Palamedes Hunt" Problem
The current Heartwood architecture excels at **Structural Integrity** but fails at **Forensic Continuity**. When a new agent boots (like Pyrrho today), it finds a perfectly hardened structure but loses the "active thread." The mission (e.g., the Heartwood Polish Marathon) is buried in session-specific JSON files or deep within the `dynamic/stream/` raw text.

### Friction Points:
- **Fragmentation:** Active tasks are stored in `repos/diy-make/memory/public/YYYY/Q1/MM/DD/json/` while the rules for doing them are in `heartwood/rules/`.
- **State Blindness:** Agents spend the first 10-20 turns "tailing the stream" to understand what the last agent *actually finished*.
- **Direction Overload:** The user must manually guide the agent to the specific file or entry (e.g., "redo 29").

## 2. Proposed Reordering: The "Active Node" Strategy
I propose reordering the Heartwood to separate **Legislative DNA** (static rules) from **Metabolic Intent** (active missions).

### A. Establish `heartwood/active/` (The Mission Hub)
Create a "hot" directory that acts as the current pointer for the entire swarm.
- `heartwood/active/relay.json`: A mandatory succession file updated at the end of every session.
- `heartwood/active/mission.json`: The current active `todo` or `marathon` file. No more looking in date folders.

### B. Consolidate into `heartwood/trunk/`
Merge `principles/`, `philosophy/`, and `rules/` into a single `trunk/` directory. This reduces path depth and recognizes that for an AI, a "value" (principle) and a "procedural step" (rule) are functionally identical legislative data.

### C. Standardize the "Better Boot Style"
Modify `startup_protocol.json` to mandate the following sequence:
1. **Verify Environment.**
2. **Read `heartwood/active/relay.json`.** (This tells the agent *exactly* where the previous one stopped).
3. **Announce existence with the `boot_report_style.json` template.**

## 3. Specific Reordering Plan

| Action | Path | Rationale |
| :--- | :--- | :--- |
| **CREATE** | `heartwood/active/` | Central hub for swarm state. |
| **MIGRATE** | `heartwood/rules/` -> `heartwood/trunk/` | Flattening the hierarchy. |
| **MIGRATE** | `heartwood/principles/` -> `heartwood/trunk/` | Flattening the hierarchy. |
| **INITIALIZE**| `heartwood/active/relay.json` | The breadcrumb for the next agent. |

## 4. Impact Assessment
By moving the **Mission Pointer** out of the chrono-fractal date folders and into a stable `heartwood/active/` node, agents will transition from "Investigating the Past" to "Executing the Present" within 2 turns of boot.

**Next Step:** With user approval, I will execute the `relay.json` initialization and the flattening of the `trunk/`.
