# WeDo: Python Script Audit & Infrastructure Hardening (v1.5)

**Author:** Kleon (Male Agent)
**Date:** December 29, 2025
**Context:** Auditing and Hardening the toolchain across the MetaGit.

---

## 🟢 Synaptic & Boomerang Log

*   **Synaptic Synapse (Orchestrator Integrity):** The User mandated that nothing be deleted from the root `gemini/py/` directory to preserve the orchestrator's baseline.
*   **Release Logic Synapse (Local Releases):** The User mandated that `memory/public/py/` have its own `metagit_release_manager.py` to support independent salted releases of the Memory Module.
*   **Comms Logic Synapse (Scripted JSON):** I am retaining `read_swarm_messages.py` and `send_swarm_message.py` as they provide scripted methods for HSD communication, though they require physical realignment.

---

## 1. Project Root Toolchain (`gemini/py/`) - STATUS: PRESERVED

All scripts in the root `py/` directory are locked.

- **verify_environment.py** (ESSENTIAL)
- **signatures/generate_salt.py** (ESSENTIAL)
- **metagit_release_manager.py** (ESSENTIAL)
- **metagit_commit.py** (ESSENTIAL)
- **metagit_metarepo_map.py** (ESSENTIAL)
- **compare_maps.py** (PRESERVED)
- **context_prefetch.py** (UTILITY)

---

## 2. Memory Repository Audit (`memory/public/py/`) - STATUS: AUDIT IN PROGRESS

**verify_environment.py (STAY)**
Local repo hook for V0.8.2 integrity.

**signatures/generate_salt.py (STAY)**
Required for Memory-specific salted releases.

**metagit_release_manager.py (NEW TASK)**
I will copy the release manager to this directory to enable independent versioning.

**read_swarm_messages.py & send_swarm_message.py (STAY/REFACTOR)**
Retained as the scripted HSD method for JSON comms. Needs realignment to `../../comms/`.

**Experimental Leaves (DELETE)**
The following scripts are marked for deletion to harden the Heartwood:
- dspy_chat_summarizer.py
- dspy_daily_summary_generator.py
- dspy_daily_workflow_orchestrator.py
- dspy_image_describer.py
- dspy_screenshot_organizer.py
- dspy_simple_orchestrator.py
- dspy_startup.py
- image_description.chain.py
- memory_profiler.py
- parse_chat_log.py
- simple_image_describer.py
- validate_png.py
- youtube_manager.py

---

## 3. Action Plan (User Confirmation Required)

- [x] [TASK-01] Create `repos/diy-make/memory/public/py/metagit_release_manager.py`.
- [x] [TASK-02] Delete the 13 legacy scripts listed in Section 2 from `memory/public/py/`.
- [x] [TASK-03] Realign `read_swarm_messages.py` and `send_swarm_message.py` to the correct comms path.
- [x] [TASK-04] Commit all changes to the `memory/public` repository.

---
**Verdict:** Pruning the leaves to strengthen the trunk.
